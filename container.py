from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QPushButton, QTabWidget


class Container(QTabWidget):

    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.mapLayout = QtWidgets.QGridLayout(self.centralwidget)

    def setupContainer(self):
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab = QtWidgets.QWidget()
        self.photoListLayout = QtWidgets.QGridLayout(self.tab)

    def showPhotoListTab(self):
        gridView = QGroupBox("Grid")
        layout = QGridLayout()

        layout.addWidget(QPushButton('1'), 0, 0)
        layout.addWidget(QPushButton('2'), 0, 1)
        layout.addWidget(QPushButton('3'), 0, 2)
        layout.addWidget(QPushButton('4'), 0, 3)
        layout.addWidget(QPushButton('5'), 0, 4)
        layout.addWidget(QPushButton('1'), 1, 0)
        layout.addWidget(QPushButton('2'), 1, 1)
        layout.addWidget(QPushButton('3'), 1, 2)
        layout.addWidget(QPushButton('4'), 1, 3)
        layout.addWidget(QPushButton('5'), 1, 4)
        gridView.setLayout(layout)

    def showMapTab(self):
        mapView = QWebEngineView()
        # mapView.load(QUrl("https://api06.dev.openstreetmap.org"))
        mapView.load(QUrl("https://www.openstreetmap.org/relation/3486449"))

