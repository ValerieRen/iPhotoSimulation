from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from PyQt5.QtWidgets import QWidget


class Photo(QWidget):
    def __init__(self):
        super(Photo, self).__init__()

    def get_image_meta_info(self, filename):
        exif_data = {}
        with Image.open(filename) as img:
            data = img._getexif()
            for (tag, value) in data.items():
                decoded = TAGS.get(tag)
                exif_data[decoded] = value

            if "GPSInfo" in exif_data:
                gps_data = {}
                for tag, value in exif_data['GPSInfo'].items():
                    decoded = GPSTAGS.get(tag)
                    gps_data[decoded] = value
                exif_data['GPSInfo'] = gps_data

        return exif_data

    def get_lat_lon(self, exif_data):
        lat = None
        lon = None

        if "GPSInfo" in exif_data:
            gps_info = exif_data["GPSInfo"]
            gps_latitude = self._get_if_exist(gps_info, "GPSLatitude")
            gps_latitude_ref = self._get_if_exist(gps_info, 'GPSLatitudeRef')
            gps_longitude = self._get_if_exist(gps_info, 'GPSLongitude')
            gps_longitude_ref = self._get_if_exist(gps_info, 'GPSLongitudeRef')

            if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
                lat = self._convert_to_degress(gps_latitude)
                if gps_latitude_ref != "N":
                    lat = 0 - lat

                lon = self._convert_to_degress(gps_longitude)
                if gps_longitude_ref != "E":
                    lon = 0 - lon

    # show photo location
    def _get_if_exist(self, data, key):
        if key in data:
            return data[key]

        return None

    def _convert_to_degress(self, value):
        """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
        d0 = value[0][0]
        d1 = value[0][1]
        d = float(d0) / float(d1)

        m0 = value[1][0]
        m1 = value[1][1]
        m = float(m0) / float(m1)

        s0 = value[2][0]
        s1 = value[2][1]
        s = float(s0) / float(s1)

        return d + (m / 60.0) + (s / 3600.0)

