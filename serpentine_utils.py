# import pcbnew
from serpentine_plotsim import PlotSim
import math
import collections

class SerpentineVector():

    def __init__(self):
        
        self.edgecuts = []
        self.f_copper = []
        self.b_copper = []
        self.centerline = []

        # https://docs.kicad.org/doxygen-python-7.0/classpcbnew_1_1PCB__TRACK.html
        # https://docs.kicad.org/doxygen-python-7.0/classpcbnew_1_1SHAPE__SEGMENT.html
        self.LineSeg = collections.namedtuple('LineSeg', ['x1', 'y1', 'x2', 'y2', 'w'])

        # https://docs.kicad.org/doxygen-python-7.0/classpcbnew_1_1PCB__ARC.htm
        # https://docs.kicad.org/doxygen-python-7.0/classpcbnew_1_1SHAPE__ARC.html
        self.Arc = collections.namedtuple('Arc', ['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'w'])

    def calculate_vectors(self, params):
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

        rad, ampl, alph = params['radius'], params['amplitude'], params['alpha']
        sin_a, cos_a = math.sin(math.radians(alph)), math.cos(math.radians(alph))

        pattern_pts = [
            (-rad * cos_a, rad * (1 + sin_a)),
            (0, 0),
            (rad * cos_a, rad * (1 + sin_a)),
            ((rad + (rad - ampl) * sin_a) / cos_a, ampl)
        ]

        half_angle = (alph + 90) / 2
        sin_th, cos_th = math.sin(math.radians(half_angle)), math.cos(math.radians(half_angle))
        ends_arcmid = [
            (-rad * sin_th, rad * (1 - cos_th)),
            (rad * sin_th, rad * (1 - cos_th))
        ]

        plts = PlotSim()
        
        arc1 = self.Arc(*pattern_pts[1], *ends_arcmid[1], *pattern_pts[2], 4)
        # arc1 = self.Arc(*pattern_pts[0], *pattern_pts[1], *pattern_pts[2], 4)
        seg1 = self.LineSeg(*pattern_pts[2], *pattern_pts[3], 4)

        plts.plot_arc(arc1)
        # plts.plot_lineseg(seg1)
        plts.show()

    def validate(self, params):
        try:
            self.calculate_vectors(params)
        except Exception as e:
            return False, str(e)
    

if __name__ == '__main__':
    SerpentineVector().calculate_vectors({'radius':1,
                                          'amplitude':3,
                                          'alpha':10})
