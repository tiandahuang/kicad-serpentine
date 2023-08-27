import pcbnew
import math
import collections

class SerpentineVector():

    def __init__(self):
        
        self.edgecuts = []
        self.f_copper = []
        self.b_copper = []

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

    def validate(self, params):
        try:
            self.calculate_vectors(params)
        except Exception as e:
            return False, str(e)
    

