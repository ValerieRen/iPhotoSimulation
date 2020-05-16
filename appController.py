from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QGroupBox, \
    QGridLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5 import QtCore
from mapContainer import MapContainer
from photoContainer import PhotoContainer
import sys
import photo


class AppController(QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        self.handlePhotos = photo.Photo()
        self.create_window_view()

    def create_window_view(self):
        self.create_navigation()
        self.create_header()
        self.create_container()

        initLayout = QGridLayout()
        initLayout.addWidget(self.navigation, 1, 1, 8, 1)
        initLayout.addWidget(self.header, 1, 2, 1, 7)
        initLayout.addWidget(self.container, 2, 2, 7, 7)

        self.initWidget = QWidget(self)
        self.initWidget.setLayout(initLayout)

        w = 1280
        h = 700
        self.setWindowTitle("Photo Manager")
        self.setCentralWidget(self.initWidget)
        self.resize(w, h)

    def create_navigation(self):
        self.navigationLayout = QVBoxLayout()
        self.navigationLayout.addWidget(QPushButton('Library'), alignment=QtCore.Qt.AlignTop)
        self.navigationLayout.addWidget(QPushButton('Timeline'), alignment=QtCore.Qt.AlignTop)
        self.navigationLayout.addWidget(QPushButton('Timeline2'), alignment=QtCore.Qt.AlignTop)

        self.navigation = QGroupBox()
        self.navigation.setLayout(self.navigationLayout)

    def create_header(self):
        self.photoButton = QPushButton('Grid')
        self.mapButton = QPushButton('Map')

        self.photoButton.clicked.connect(self.show_photo)
        self.mapButton.clicked.connect(self.show_map)

        self.headerLayout = QHBoxLayout()
        self.headerLayout.addWidget(self.photoButton, alignment=QtCore.Qt.AlignVCenter)
        self.headerLayout.addWidget(self.mapButton, alignment=QtCore.Qt.AlignVCenter)
        self.header = QGroupBox()
        self.header.setLayout(self.headerLayout)

    def create_container(self):
        self.containerLayout = QGridLayout()
        self.container = QGroupBox()
        self.container.setLayout(self.containerLayout)
        self.show_default()

    def show_map(self):
        if self.containerLayout.count() > 0:
            self.containerLayout.itemAt(0).widget().deleteLater()
        self.map_window = MapContainer()
        self.containerLayout.addWidget(self.map_window)

    def show_photo(self):
        if self.containerLayout.count() > 0:
            self.containerLayout.itemAt(0).widget().deleteLater()
        self.photo_window = PhotoContainer(self.container.geometry())
        self.containerLayout.addWidget(self.photo_window)

    def show_default(self):
        self.photo_window = PhotoContainer(self.container.geometry())
        self.containerLayout.addWidget(self.photo_window)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = AppController()
    application.show()
    app.exec_()