import pcbnew
import math

class SerpentineVector():

    def __init__(self):
        
        self.edgecuts = []
        self.f_copper = []
        self.b_copper = []

    def calculate_vectors(self, params):
        """
        parameters:
        -----------
        radius
        amplitude
        alpha
        length
        wc
        width
        pitch
        margin
        """

    def validate(self, params):
        try:
            self.calculate_vectors(params)
        except Exception as e:
            return False, str(e)
    

