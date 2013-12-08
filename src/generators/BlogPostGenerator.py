import os
import codecs
import shutil
import pystache


class BlogPostGenerator:
	def __init__(self, blogMetadata):
		self.blogMetadata = blogMetadata
		self.outputFolder = blogMetadata.blogFolder
		self.templateFolder = blogMetadata.themesFolder
				
	def loadTheme(self, themeName="default"):
		self.templateFolder = os.path.join(self.templateFolder,themeName)
		shutil.copy2(os.path.join(self.templateFolder,"post.css"), self.outputFolder)
		shutil.copy2(os.path.join(self.templateFolder,"index.css"), self.outputFolder)
		shutil.copy2(os.path.join(self.templateFolder,"logo.png"), self.outputFolder)
		try:
			shutil.rmtree(os.path.join(self.outputFolder,"fonts"))
		except:
			pass
		shutil.copytree(os.path.join(self.templateFolder,"fonts"), os.path.join(self.outputFolder,"fonts"))
		
	def loadImages(self):
		try:
			shutil.rmtree(os.path.join(self.outputFolder,"images"))
		except:
			pass
		shutil.copytree(self.blogMetadata.imagesFolder, os.path.join(self.outputFolder,"images"))
		
	def generatePost(self, post):
	
		# Instantiate Renderer
		renderer = pystache.Renderer()
		
		# Generate dict
		content = {"title": post.title, "date": post.date, "post_text": post.mainText, "index": "index.html"}
		
		f = codecs.open(os.path.join(self.outputFolder, post.url),'w','utf-8')
		f.write(renderer.render_path(os.path.join(self.templateFolder, "postTemplate.html"),content))
		f.close()
		
	def generateIndex(self, postList):
		listOfEntries = str()
	
		# Instantiate Renderer
		renderer = pystache.Renderer()
		
		
		
		f = codecs.open(os.path.join(self.outputFolder, "index.html"),'w','utf-8')
		
		for post in postList:
			listOfEntries = listOfEntries + '<p><a class="entry" href="'+post.url+'">'+post.title+'</a></p>'+'\n'
		
		
		# Generate dict
		content = {"title": self.blogMetadata.blogName, "entries": listOfEntries}
		f.write(renderer.render_path(os.path.join(self.templateFolder, "indexTemplate.html"),content))
		
		
		f.close()
		
