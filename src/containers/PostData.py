class PostData(object):
	def __init__(self):
		self.url = unicode()  # sanitized final url for the blog post 
		self.author = unicode()
		self.date = unicode()
		self.tags = list()
		self.title = unicode()
		self.mainText = unicode()
		
		
