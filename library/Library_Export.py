import xml.etree.ElementTree as ET
from library.Tracks import Tracks
from library.mongoclient import Mongo


class Library(object):
    def __init__(self, xml_file):
        self.xml = ET.parse(xml_file).find('dict').find('dict').findall('dict')
        self.tracks = [Tracks(row) for row in self.xml]

    def load_library(self):
        for track in self.tracks:
            track.comments = track.find_comments()
            track.location = track.find_location()
            Mongo(track)
