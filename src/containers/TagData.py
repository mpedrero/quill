import slugify

class TagData(object):
	def __init__(self):
		self.name = unicode()   # tag name
		self.url = unicode()	# sanitized final url for the blog post 
		self.postList = list() 	# list of PostData entries with tag
		
	def __init__(self, name):
		self.name = name   # tag name
		self.url = unicode()	# sanitized final url for the blog post 
		self.postList = list() 	# list of PostData entries with tag
		
		self.url = slugify.slugify(self.name)+".html"
