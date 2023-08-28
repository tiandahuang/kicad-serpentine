import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class PlotSim():

    def __init__(self) -> None:
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal', adjustable='datalim')

    def show(self):
        plt.show()

    def plot_arc(self, arc):
        cx, cy, r, th1, th2 = self.spline_to_arc(arc)
        if arc.y2 < arc.y1: th1, th2 = th2, th1     # flip to account for clockwise drawing
        print(r, th1, th2)
        self.plot_points([(arc.x1, arc.y1), (arc.x2, arc.y2), (arc.x3, arc.y3), (cx, cy)])
        self.ax.add_patch(patches.Arc((cx, cy), 
                                      2*r, 2*r, 
                                      theta1=th1, theta2=th2, 
                                      linewidth=arc.w))

    def plot_lineseg(self, lineseg):
        self.plot_points([(lineseg.x1, lineseg.y1), (lineseg.x2, lineseg.y2)])
        self.ax.add_patch(patches.Polygon([(lineseg.x1, lineseg.y1),
                                          (lineseg.x2, lineseg.y2)],
                                          closed=False, fill=False,
                                          linewidth=lineseg.w))
        
    def plot_points(self, pts):
        [self.ax.plot(*pt, marker='o', markersize=5, color='red') for pt in pts]

    @staticmethod
    def spline_to_arc(arc):
        # x1, y1, x2, y2, x3, y3 --> x, y, r, th1, th2
        A = np.array([[2 * (arc.x1 - arc.x3), 2 * (arc.y1 - arc.y3)],
                        [2 * (arc.x1 - arc.x2), 2 * (arc.y1 - arc.x2)]])
        b = np.array([arc.x1**2 + arc.y1**2 - arc.x3**2 - arc.y3**2,
                        arc.x1**2 + arc.y1**2 - arc.x2**2 - arc.y2**2])
        cx, cy = np.linalg.solve(A, b)
        r = np.linalg.norm([arc.x1 - cx, arc.y1 - cy])
        th1, th2 = np.arcsin([(cy - arc.y1) / r, (cy - arc.y3) / r])
        th1, th2 = np.degrees([-th1, np.pi + th2])

        return cx, cy, r, th1, th2

"""
fig, ax = plt.subplots()

w = 2
arc = self.Arc(0, 0, 1, 1, 2, 0, 2)
cx, cy, r, th1, th2 = spline_to_arc(arc)

ax.add_patch(patches.Arc((cx, cy), r, r, theta1=th1, theta2=th2, linewidth=w))
ax.plot(cx, cy, marker='o', markersize=5, color='red')
print(r, th1, th2)

ax.set_aspect('equal', adjustable='datalim')
plt.show()
"""
