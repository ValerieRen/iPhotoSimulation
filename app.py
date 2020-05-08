from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QGroupBox, \
    QGridLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5 import QtCore
import sys

from Ui_Window import Ui_Window


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.create_window_view()

    def create_window_view(self):
        initLayout = QGridLayout()

        self.create_navigation()
        self.create_header()
        self.create_container()

        initLayout.addWidget(self.navigation, 1, 1, 8, 1)
        initLayout.addWidget(self.header, 1, 2, 1, 7)
        initLayout.addWidget(self.container, 2, 2, 7, 7)
        # for i in range(1, 5):
        #     for j in range(1, 5):
        #         initLayout.addWidget(QPushButton("B" + str(i) + str(j)), i, j)

        initWidget = QWidget(self)
        initWidget.setLayout(initLayout)

        w = 1280
        h = 700
        self.setWindowTitle("Photo Manager")
        self.setCentralWidget(initWidget)
        self.resize(w, h)

    def create_navigation(self):
        self.navigation = QGroupBox()

        navigationLayout = QVBoxLayout()
        navigationLayout.addWidget(QPushButton('Library'), alignment=QtCore.Qt.AlignTop)
        navigationLayout.addWidget(QPushButton('Timeline'), alignment=QtCore.Qt.AlignTop)
        navigationLayout.addWidget(QPushButton('Timeline2'), alignment=QtCore.Qt.AlignTop)

        self.navigation.setLayout(navigationLayout)

    def create_header(self):
        self.gridButton = QPushButton('Grid', self)
        self.mapButton = QPushButton('Map', self)

        self.gridButton.clicked.connect(self.btnGridstate)
        self.mapButton.clicked.connect(self.btnMapstate)

        headerLayout = QHBoxLayout()
        headerLayout.addWidget(self.gridButton, alignment=QtCore.Qt.AlignVCenter)
        headerLayout.addWidget(self.mapButton, alignment=QtCore.Qt.AlignVCenter)
        self.header = QGroupBox()
        self.header.setLayout(headerLayout)

    def create_container(self):
        self.view = QWebEngineView()
        self.view.load(QUrl("https://api06.dev.openstreetmap.org"))

        containerLayout = QGridLayout()
        containerLayout.addWidget(self.view)
        self.container = QGroupBox()
        self.container.setLayout(containerLayout)

    def btnGridstate(self):
        print('show gridbutton')
        self.view.load(QUrl("https://api06.dev.openstreetmap.org"))

    def btnMapstate(self):
        print('show mapButton')
        self.view.load(QUrl("https://www.openstreetmap.org/relation/3486449"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())
