from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QGroupBox, \
    QGridLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, pyqtSlot
import sys

from Ui_Window import Ui_Window
from photo import Photo


class MainWindow(QMainWindow, Ui_Window):

    def __init__(self):
        super().__init__()
        self.gridButton = QPushButton('Grid', self)
        self.mapButton = QPushButton('Map', self)

        self.create_window_view()

    def create_window_view(self):
        initLayout = QGridLayout()

        self.create_navigation()
        self.create_container()

        initLayout.addWidget(self.navigation, 0, 0)
        initLayout.addWidget(self.container, 0, 1, 0, 4)

        initWidget = QWidget(self)
        initWidget.setLayout(initLayout)

        w = 1280
        h = 800
        self.setWindowTitle("Photo Manager")
        self.setCentralWidget(initWidget)
        self.resize(w, h)

    def create_navigation(self):
        self.navigation = QGroupBox()

        navigationLayout = QVBoxLayout()
        navigationLayout.addWidget(QPushButton('Library'))
        navigationLayout.addWidget(QPushButton('Timeline'))

        self.navigation.setLayout(navigationLayout)

    def create_container(self):

        self.gridButton.setDefault(True)

        self.gridButton.clicked.connect(self.create_container)
        self.mapButton.clicked.connect(self.create_container)

        headerLayout = QHBoxLayout()
        headerLayout.addWidget(self.gridButton)
        headerLayout.addWidget(self.mapButton)
        header = QWidget()
        header.setLayout(headerLayout)

        # self.view = QWebEngineView()
        # self.view.load(QUrl("https://api06.dev.openstreetmap.org"))

        self.container = QGroupBox()
        containerLayout = QGridLayout()
        containerLayout.addWidget(header, 0, 0)
        containerLayout.addWidget(MainWindow.btnState(self), 1, 0, 16, 0)

        self.container.setLayout(containerLayout)

    def btnState(self):
        if self.mapButton.isChecked():
            print('show mapButton')
            return self.show_photos_in_map()
        else:
            print('show gridButton')
            return self.show_photos_list()

    def show_photos_list(self):
        print('show photos')

    def show_photos_in_map(self):
        print('show map')
        mapView = QWebEngineView()
        # mapView.load(QUrl("https://api06.dev.openstreetmap.org"))
        mapView.load(QUrl("https://www.openstreetmap.org/relation/3486449"))

      # exif_data = Photo.get_image_meta_info('img/IMG_7228.JPG')
        return mapView


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())
