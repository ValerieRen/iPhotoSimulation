from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QGroupBox, \
    QGridLayout, QScrollArea, QAbstractScrollArea
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt, QRect
from PyQt5 import QtCore
from mapContainer import MapContainer
from photoContainer import PhotoContainer
import sys
import photo


class AppController(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(AppController, self).__init__(*args, **kwargs)

        w = 1580
        h = 900
        widget = QWidget()
        self.setWindowTitle("Photo Manager")
        self.setCentralWidget(widget)
        self.resize(w, h)

        self.mainLayout = QHBoxLayout()
        self.panelLayout = QVBoxLayout()
        navLayout = QVBoxLayout()
        headerLayout = QHBoxLayout()

        libraryButton = QPushButton('Library')
        timelineButton = QPushButton('Timeline')
        photoButton = QPushButton('Grid')
        mapButton = QPushButton('Map')

        libraryButton.setFixedSize(200, 30)
        timelineButton.setFixedSize(200, 30)
        navLayout.addWidget(libraryButton, 0, alignment=QtCore.Qt.AlignTop)
        navLayout.addWidget(timelineButton, 1, alignment=QtCore.Qt.AlignTop)

        photoButton.clicked.connect(self.show_photo)
        mapButton.clicked.connect(self.show_map)

        headerLayout.addWidget(photoButton)
        headerLayout.addWidget(mapButton)

        self.show_default()

        self.panelLayout.addLayout(headerLayout)
        self.panelLayout.addWidget(self.container)
        self.mainLayout.addLayout(navLayout)
        self.mainLayout.addLayout(self.panelLayout)

        widgegit.setLayout(self.mainLayout)

    def show_default(self):
        self.container = ScrollPhotoBox()

    def show_map(self):
        self.delete_widget()
        self.container = MapContainer()
        self.panelLayout.addWidget(self.container)

    def show_photo(self):
        self.delete_widget()
        self.container = ScrollPhotoBox()
        self.panelLayout.addWidget(self.container)

    def delete_widget(self):
        self.container.setParent(None)


class ScrollPhotoBox(QScrollArea):
   def __init__(self, parent=None):
      super(ScrollPhotoBox, self).__init__(parent)

      self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
      self.setWidgetResizable(True)
      self.setWidget(PhotoContainer(self.geometry()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = AppController()
    application.show()
    app.exec_()