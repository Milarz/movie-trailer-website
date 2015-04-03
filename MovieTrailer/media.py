import webbrowser


class Movie():
    #Represents individual films.
    VALID_RATINGS = ["G", "PG", "PG-13", "R", "X"]
    def __init__(self, title, storyline, poster_url, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

    #Test methods using default browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_poser(self):
        webbrowser.open(self.poster_image_url)
