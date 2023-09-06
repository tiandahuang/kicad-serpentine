import pcbnew
import wx
import math
import collections

class SerpentineVector():

    def __init__(self):
        
        self.vectors = {
            'edgecuts':{'width':0, 'offsets':[], 'segments':[]},
            'f_copper':{'width':0, 'offsets':[], 'segments':[]},
            'b_copper':{'width':0, 'offsets':[], 'segments':[]}}

        # https://docs.kicad.org/doxygen-python-7.0/classpcbnew_1_1PCB__TRACK.html
        # https://docs.kicad.org/doxygen-python-7.0/classpcbnew_1_1SHAPE__SEGMENT.html
        self.LineSeg = collections.namedtuple('LineSeg', ['x1', 'y1', 'x2', 'y2'])

        # https://docs.kicad.org/doxygen-python-7.0/classpcbnew_1_1PCB__ARC.htm
        # https://docs.kicad.org/doxygen-python-7.0/classpcbnew_1_1SHAPE__ARC.html
        self.Arc = collections.namedtuple('Arc', ['x1', 'y1', 'x2', 'y2', 'x3', 'y3'])

    def calculate_vectors(self, params):
        raise Exception(str(params))
        """
        parameters:
        -----------
        radius
        amplitude
        alpha
        length
        pitch
        f_wc
        f_width
        b_wc
        b_width
        noedge
        """

        def wc_to_offsets(wc, width, pitch):
            init_ofs = 0 if (wc % 2 != 0) else ((width + pitch) / 2)
            ofs = [(init_ofs + (i * (width + pitch))) * flip for i in range((wc + 1) // 2) for flip in (-1, 1)]
            return ofs[1:] if len(ofs) > 0 and (wc % 2 != 0) else ofs

        # calculate number of serpentines and offsets
        f_width, f_wc, b_width, b_wc, pitch = [params[p] for p in ('f_width', 'f_wc', 'b_width', 'b_wc', 'pitch')]
        self.vectors['f_copper']['width'] = f_width
        self.vectors['f_copper']['offsets'] = wc_to_offsets(f_wc, f_width, pitch)
        self.vectors['b_copper']['width'] = b_width
        self.vectors['b_copper']['offsets'] = wc_to_offsets(b_wc, b_width, pitch)
        if not params['noedge']:
            f_border = (max(self.vectors['f_copper']['offsets']) + f_width / 2 + pitch) if f_wc > 0 else 0
            b_border = (max(self.vectors['b_copper']['offsets']) + b_width / 2 + pitch) if b_wc > 0 else 0
            self.vectors['edgecuts']['offsets'] = [max(f_border, b_border), -max(f_border, b_border)]

        # calculate coordinates for pattern template
        rad, ampl, alph = params['radius'], params['amplitude'], params['alpha']
        sin_a, cos_a = math.sin(math.radians(alph)), math.cos(math.radians(alph))

        half_angle = (alph + 90) / 2
        sin_th, cos_th = math.sin(math.radians(half_angle)), math.cos(math.radians(half_angle))

        def get_arc_pts(ofs):
            return [
                (-(rad + ofs) * cos_a, (rad + ofs) * (1 + sin_a) - ofs),
                (0, -ofs),
                ((rad + ofs) * cos_a, (rad + ofs) * (1 + sin_a) - ofs)]
    
        def get_halfarc_pts(ofs):
            return [
                (-(rad + ofs) * sin_th, (rad + ofs) * (1 - cos_th) - ofs),
                ((rad + ofs) * sin_th, (rad + ofs) * (1 - cos_th) - ofs)]

        pattern_width = 2 * ((rad + (rad - ampl) * sin_a) / cos_a)
        num_iterations = (max(2, math.floor(params['length'] / pattern_width)) // 2) * 2

        for layer in self.vectors:
            for ofs in self.vectors[layer]['offsets']:
                arc_pts = get_arc_pts(ofs)
                inv_arc_pts = get_arc_pts(-ofs)
                halfarc_pts = get_halfarc_pts(ofs)

                all_points = [arc_pts[1], halfarc_pts[1], arc_pts[2]]
                for i in range(1, num_iterations):
                    pts = arc_pts if (i % 2 == 0) else self.mirror_pts_y(inv_arc_pts, ampl)
                    pts = self.translate_pts(pts, i * pattern_width, 0)
                    all_points.extend(pts)
                pts = [arc_pts[0], halfarc_pts[0], arc_pts[1]]
                pts = self.translate_pts(pts, (i + 1) * pattern_width, 0)
                all_points.extend(pts)

                i = cnt = 0
                while (i < len(all_points) - 2):
                    p1, p2, p3 = [all_points[i + j] for j in range(3)]
                    if cnt % 2 == 0: 
                        seg = self.Arc(*p1, *p2, *p3)
                        i += 2
                    else:
                        seg = self.LineSeg(*p1, *p2)
                        i += 1
                    self.vectors[layer]['segments'].append(seg)
                    cnt += 1
    
    def route_vectors(self):
        self.board = pcbnew.GetBoard()
        self.group = pcbnew.PCB_GROUP(self.board)
        self.board.Add(self.group)
        name_to_layer = {'edgecuts':pcbnew.Edge_Cuts,
                         'f_copper':pcbnew.F_Cu,
                         'b_copper':pcbnew.B_Cu}

        for layer in self.vectors:
            width = self.vectors[layer]['width']
            pcblayer = name_to_layer[layer]
            for s in self.vectors[layer]['segments']:
                if type(s) is self.Arc:
                    obj = self.arc_to_pcbarc(s, width, pcblayer)
                else:       # type is LineSeg
                    obj = self.line_to_pcbtrack(s, width, pcblayer)
                self.board.Add(obj)
                self.group.AddItem(obj)

        pcbnew.Refresh()

    def arc_to_pcbarc(self, arc, width, layer):
        if layer != pcbnew.Edge_Cuts:
            pcbarc = pcbnew.PCB_ARC(self.board)
            pcbarc.SetStart(self.xy_to_pcbpoint(arc.x1, arc.y1))
            pcbarc.SetMid(self.xy_to_pcbpoint(arc.x2, arc.y2))
            pcbarc.SetEnd(self.xy_to_pcbpoint(arc.x3, arc.y3))
        else:
            pcbarc = pcbnew.PCB_SHAPE(self.board, pcbnew.SHAPE_T_ARC)
            pcbarc.SetArcGeometry(self.xy_to_pcbpoint(arc.x1, arc.y1),
                               self.xy_to_pcbpoint(arc.x2, arc.y2),
                               self.xy_to_pcbpoint(arc.x3, arc.y3))
        pcbarc.SetLayer(layer)
        pcbarc.SetWidth(pcbnew.FromMM(width))
        
        return pcbarc

    def line_to_pcbtrack(self, lineseg, width, layer):
        track = (pcbnew.PCB_TRACK(self.board) if layer != pcbnew.Edge_Cuts else
                 pcbnew.PCB_SHAPE(self.board, pcbnew.SHAPE_T_SEGMENT))
        track.SetLayer(layer)
        track.SetWidth(pcbnew.FromMM(width))
        track.SetStart(self.xy_to_pcbpoint(lineseg.x1, lineseg.y1))
        track.SetEnd(self.xy_to_pcbpoint(lineseg.x2, lineseg.y2))
        return track
    
    def xy_to_pcbpoint(self, x, y):
        return pcbnew.VECTOR2I_MM(x+100, y+100)

    @staticmethod
    def mirror_pts_y(pts, y):
        return [(_x, (2 * y) - _y) for _x, _y in pts]

    @staticmethod
    def translate_pts(pts, x, y):
        return [(x + _x, y + _y) for _x, _y in pts]

    @staticmethod
    def pts_to_center_arc(center, start_point, middle_point, end_point):
        pass

    def validate(self, params):
        try:
            self.calculate_vectors(params)
        except Exception as e:
            return False, str(e)
        return True, None
    
    def run(self, params):
        try:
            self.calculate_vectors(params)
            self.route_vectors()
        except Exception as e:
            return False, str(e)
        return True, None
    

if __name__ == '__main__':
    from serpentine_plotsim import PlotSim
    a = SerpentineVector()
    a.calculate_vectors({"radius":2,
                         "amplitude":5,
                         "alpha":10,
                         "length":20,
                         "pitch":0.3,
                         "f_wc":2,
                         "f_width":0.4,
                         "b_wc":3,
                         "b_width":0.2,
                         "noedge":False})

