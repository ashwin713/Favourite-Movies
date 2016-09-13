import webbrowser

class Movie():
	def __init__(self, movie_title, movie_story_line, poster_image, trailer_youtube):
		self.title = movie_title
		self.story_line = movie_story_line
		self.poster_image = poster_image
		self.trailer_youtube = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube)
