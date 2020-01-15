import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5 import QtCore
from PIL import Image, ExifTags
from PIL.ExifTags import GPSTAGS, TAGS
import osmapi as osm

app = QApplication([])
window = QWidget()
#
#
# def get_exif(filename):
#     image = Image.open(filename)
#     image.verify()
#     return image._getexif()
#
#
# def get_geo_tag(exif):
#     if not exif:
#         raise ValueError("No EXIF metadata found")
#
#     geotagging = {}
#     for (idx, tag) in TAGS.items():
#         if tag == 'GPSInfo':
#             if idx not in exif:
#                 raise ValueError("No EXIF geotagging found")
#
#             for (key, val) in GPSTAGS.items():
#                 if key in exif[idx]:
#                     geotagging[val] = exif[idx][key]
#
#     return geotagging
#
#
# def get_lat_lon(exif_data):
#     lat = None
#     lon = None
#
#     if "GPSInfo" in exif_data:
#         gps_info = exif_data["GPSInfo"]
#         gps_latitude = _get_if_exist(gps_info, "GPSLatitude")
#         gps_latitude_ref = _get_if_exist(gps_info, 'GPSLatitudeRef')
#         gps_longitude = _get_if_exist(gps_info, 'GPSLongitude')
#         gps_longitude_ref = _get_if_exist(gps_info, 'GPSLongitudeRef')
#
#         if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
#             lat = _convert_to_degress(gps_latitude)
#             if gps_latitude_ref != "N":
#                 lat = 0 - lat
#
#             lon = _convert_to_degress(gps_longitude)
#             if gps_longitude_ref != "E":
#                 lon = 0 - lon
#
#     return lat, lon
#
#
# def get_image_meta_info(filename):
#     exif_data = {}
#     with Image.open(filename) as img:
#         data = img._getexif()
#         for (tag, value) in data.items():
#             decoded = TAGS.get(tag)
#             exif_data[decoded] = value
#
#         if "GPSInfo" in exif_data:
#             gps_data = {}
#             for tag, value in exif_data['GPSInfo'].items():
#                 decoded = GPSTAGS.get(tag)
#                 gps_data[decoded] = value
#             exif_data['GPSInfo'] = gps_data
#
#     return exif_data


######## show photo location  ########
# def _get_if_exist(data, key):
#     if key in data:
#         return data[key]
#
#     return None
#
#
# def _convert_to_degress(value):
#     """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
#     d0 = value[0][0]
#     d1 = value[0][1]
#     d = float(d0) / float(d1)
#
#     m0 = value[1][0]
#     m1 = value[1][1]
#     m = float(m0) / float(m1)
#
#     s0 = value[2][0]
#     s1 = value[2][1]
#     s = float(s0) / float(s1)
#
#     return d + (m / 60.0) + (s / 3600.0)
#

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # layout = QVBoxLayout()
    ######## show buttons  ########
    # layout.addWidget(QPushButton('Top'))
    # layout.addWidget(QPushButton('Bottom'))
    # api = osm.OsmApi(api="https://api06.dev.openstreetmap.org", username="piqaluyak52", password="")

    # exif = get_exif('img/IMG_7228.JPG')
    # print(exif)
    # print('1----')
    # geotags = get_geo_tag(exif)
    # print(geotags)
    # exif_data = get_image_meta_info('img/IMG_7228.JPG')
    # print(exif_data)
    # print(get_lat_lon(exif_data))

    ######## show map  ########
    # web = QWebEngineView()
    # web.load(QUrl("https://www.openstreetmap.org/relation/3486449"))
    # web.load(QUrl("https://api06.dev.openstreetmap.org"))
    # layout.addWidget(web)

    # window.setLayout(layout)
    # window.setWindowState(QtCore.Qt.WindowMaximized)
    # window.show()
    app.exec_()
