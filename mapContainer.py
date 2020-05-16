from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys

class MapContainer(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Map Window')

        layout = QtWidgets.QGridLayout()

        self.view = QWebEngineView()
        self.view.load(QtCore.QUrl("https://api06.dev.openstreetmap.org"))
        layout.addWidget(self.view)

        self.setLayout(layout)
