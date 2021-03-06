from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from photo import photo


class PhotoContainer(QWidget):

    def __init__(self, geometry):
        QWidget.__init__(self)
        self.setWindowTitle('Photo Window')

        self.layout = QGridLayout()
        self.handlePhotos = photo.Photo()

        sortedPhotoList = self.handlePhotos.get_sorted_photo_by_date()
        self.display_photos_in_grid(sortedPhotoList, geometry)
        self.setContentsMargins(20, 0, 20, 0)
        self.setLayout(self.layout)

    def display_photos_in_grid(self, photolist, geometry):
        number_of_img_per_row = 5
        # width = geometry.width() / number_of_img_per_row + number_of_img_per_row * 16
        row = 0
        col = 0

        for x in range(0, len(photolist)):
            if row == number_of_img_per_row:
                row = 0
                col += 1
            label = QLabel()
            pixmap = QPixmap(photolist[x].get("file"))
            # label.resize(width, width)
            label.setFixedHeight(230)
            label.setFixedWidth(200)
            label.setPixmap(pixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatio))
            row += 1
            self.layout.addWidget(label, col, row)

