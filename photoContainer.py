from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
import sys
import photo

class PhotoContainer(QWidget):
`
    def __init__(self, geometry):
        QWidget.__init__(self)
        self.setWindowTitle('Photo Window')

        self.layout = QGridLayout()
        self.handlePhotos = photo.Photo()

        sortedPhotoList = self.handlePhotos.get_photo_by_date()
        self.display_photos_in_grid(sortedPhotoList, geometry)
        self.setLayout(self.layout)

    def display_photos_in_grid(self, list, geometry):
        number_of_img_per_row = 4
        width = geometry.width() / number_of_img_per_row
        row = 0
        col = 0
        print(geometry.width())
        print(width)

        for x in range(0, len(list)):
            if (row == number_of_img_per_row):
                row = 0
                col += 1
            label = QLabel()
            pixmap = QPixmap(list[x].get("file"))
            label.resize(width, width)
            label.setPixmap(pixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatio))
            row += 1
            self.layout.addWidget(label, col, row)
