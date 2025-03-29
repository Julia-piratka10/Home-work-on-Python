import numpy as np
from PyQt5 import QtWidgets
from zd1 import Ui_MainWindow
import sys
import matplotlib.pyplot as plt
g = 9.81

class plot(QtWidgets.QMainWindow):
    def __init__(self):
        super(plot, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn1.clicked.connect(self.btnClicked)

    def btnClicked(self):
        try:
            v = float(self.ui.v.text())
            a = float(self.ui.a.text())
            a_rad = np.radians(a)
            t = 2 * v * np.sin(a_rad) / g
            t_point = np.linspace(0, t, 200)
            x = v * np.cos(a_rad) * t_point
            y = v * np.sin(a_rad) * t_point - 0.5 * g * t_point**2
            plt.figure()
            plt.plot(x, y)
            plt.axis('equal')
            plt.axhline(0, color='black')
            plt.show()
        except ValueError:
            None

app = QtWidgets.QApplication([])
window = plot()
window.show()

sys.exit(app.exec())