from requests import get
from simplejson import loads


class SpotifyClient(object):
    def __init__(self):
        self.spotify_token = "BQDhGzZyZ9R7TpHHwuK5I6da4g4rB91YiQyNEufEWPLB" \
                             "-hC4M2byUcDxMPbbeO9Pun6fSE3YgaGWBtkjnyuFSEgLbypHwGkPK2lr2Ip_oj0iRQe0ptQ7AmRaSo6iru9yo2" \
                             "vQQXT7eFf73GIJChKsyWL70afi3KCgSATfEZmkCVCv76-J0igqL6BWTu45B6xMMkTM--OZrbn4yHUv6K-7j1HNB" \
                             "mOMqjI "

    def check_profile(self):
        response = get("https://api.spotify.com/v1/me", headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.spotify_token)
        })
        if response.status_code == 200:
            print("Success")

    def get_playlists(self):
        response = get("https://api.spotify.com/v1/users/jmunoz96/playlists", headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.spotify_token)
        })
        items = loads(response.text)["items"]
        playlists = [field["name"] for field in items]
        for playlist in playlists:
            print(playlist)


if __name__ == '__main__':
    spotify = SpotifyClient()
    spotify.get_playlists()
