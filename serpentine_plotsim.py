import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class PlotSim():

    colors = 'bgcmy'

    def __init__(self) -> None:
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal', adjustable='datalim')

    def show(self):
        plt.show()

    def plot_arc(self, arc):
        cx, cy, r, th1, th2 = self.spline_to_arc(arc)
        self.plot_points([(arc.x1, arc.y1), (arc.x2, arc.y2), (arc.x3, arc.y3), (cx, cy)])
        self.ax.add_patch(patches.Arc((cx, cy), 
                                      2*r, 2*r, 
                                      theta1=th1, theta2=th2,
                                      color=self.colors[arc.w],
                                      linewidth=4))
        
    def plot_arc_safe(self, arc):
        self.plot_points([(arc.x1, arc.y1), (arc.x2, arc.y2), (arc.x3, arc.y3)])
        self.ax.add_patch(patches.Polygon([(arc.x1, arc.y1),
                                           (arc.x2, arc.y2)],
                                          closed=False, fill=False,
                                          color=self.colors[arc.w],
                                          linewidth=4))
        self.ax.add_patch(patches.Polygon([(arc.x2, arc.y2),
                                           (arc.x3, arc.y3)],
                                          closed=False, fill=False,
                                          color=self.colors[arc.w],
                                          linewidth=4))

    def plot_lineseg(self, lineseg):
        self.plot_points([(lineseg.x1, lineseg.y1), (lineseg.x2, lineseg.y2)])
        self.ax.add_patch(patches.Polygon([(lineseg.x1, lineseg.y1),
                                           (lineseg.x2, lineseg.y2)],
                                          closed=False, fill=False,
                                          color=self.colors[lineseg.w],
                                          linewidth=4))
        
    def plot_points(self, pts):
        [self.ax.plot(*pt, marker='o', markersize=5, color='r') for pt in pts]

    @staticmethod
    def spline_to_arc(arc):
        # x1, y1, x2, y2, x3, y3 --> x, y, r, th1, th2
        A = np.array([[2 * (arc.x1 - arc.x3), 2 * (arc.y1 - arc.y3)],
                      [2 * (arc.x1 - arc.x2), 2 * (arc.y1 - arc.y2)]])
        b = np.array([arc.x1**2 + arc.y1**2 - arc.x3**2 - arc.y3**2,
                      arc.x1**2 + arc.y1**2 - arc.x2**2 - arc.y2**2])
        cx, cy = np.linalg.solve(A, b)
        r = np.linalg.norm([arc.x1 - cx, arc.y1 - cy])
        th1, th2 = np.degrees(np.arcsin([min((cy - arc.y1) / r, 1.0), min((cy - arc.y3) / r, 1.0)]))

        x1_pos, y1_pos = (cx - arc.x1) > 0, (cy - arc.y1) > 0
        x3_pos, y3_pos = (cx - arc.x3) > 0, (cy - arc.y3) > 0
        if (x1_pos ^ y1_pos): th1 = 180 - th1
        if (x3_pos ^ y3_pos): th2 = 180 - th2

        return cx, cy, r, th1, th2
