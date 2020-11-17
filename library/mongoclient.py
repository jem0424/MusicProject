from pymongo import MongoClient


class Mongo(object):
    def __init__(self, track):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.myDB
        self.db.data.insert_one(
            {"track_id": track.id, "song": track.track_name, "artist": track.artist, "comments": track.comments,
             "location": track.location})

