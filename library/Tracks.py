class Tracks(object):
    def __init__(self, row):
        self.row = row
        self.id = row[1].text
        self.track_name = row[3].text
        self.artist = row[5].text
        self.length = len(row)
        self.comments = None
        self.location = None

    def find_comments(self):
        for field in range(self.length):
            if self.row[field].text == "Comments":
                # print(self.row[field + 1].text)
                self.comments = self.row[field + 1].text
        return self.comments

    def find_location(self):
        for field in range(self.length):
            if self.row[field].text == "Location":
                # print(self.row[field + 1].text)
                self.location = self.row[field + 1].text
        return self.location

    def __repr__(self):
        return f'id={self.id},track_name={self.track_name},artist={self.artist},length={self.length}' \
               f',comments={self.comments}, location={self.location} '
