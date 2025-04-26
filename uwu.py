import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QLabel, QLineEdit, QPushButton)
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def f():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Построение гистограммы")
    window.resize(600, 500)

    layout = QVBoxLayout()

    label = QLabel("Введите свои числа через запятую")
    layout.addWidget(label)

    input_field = QLineEdit()
    layout.addWidget(input_field)

    fig = Figure()
    canvas = FigureCanvas(fig)
    layout.addWidget(canvas)

    def plot_histogram():
        text = input_field.text()
        val = [float(x) for x in text.split(",")]

        fig.clear()
        ax = fig.add_subplot(111)

        bar_num = range(1, len(val) + 1)

        ax.bar(bar_num, val, color='pink')

        ax.set_title("Гистограмма")
        canvas.draw()

    def generate_random():
        num = [random.randint(1, 100) for _ in range(10)]
        input_field.setText(",".join(map(str, num)))

    def generate_random():
        num = [str(random.randint(1, 100)) for _ in range(10)]

        input_field.setText(", ".join(num))

    btn_plot = QPushButton("Построить гистограмму")
    btn_plot.clicked.connect(plot_histogram)
    layout.addWidget(btn_plot)

    btn1 = QPushButton("Случайные числа")
    btn1.clicked.connect(generate_random)
    layout.addWidget(btn1)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    f()