import webbrowser


class Video():
    """Video class will be the Parent for all video related classes like
    Movie, TVShow and many more. This class has been created with the intention to
    keep the design Open for Extension"""

    # Constructor of Video is instantiated based on the passed in parameters
    def __init__(self, title):
        self.title = title


class Movie(Video):
    """Movie class is the only Video class available in this project at present.
    There will be some more peers to Movie class in future depending on the need.
    Remember Movie is a Video too"""

    # Constructor of Movie is instantiated based on the passed in parameters
    def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_trailer_youtube):
        Video.__init__(self, movie_title)
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer_youtube

    # show_trailer method open the trailer of the intended Movie object in
    # webbrowser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
