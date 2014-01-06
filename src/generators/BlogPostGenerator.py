import os
import codecs
import shutil
import pystache
import containers.TagData as TagData


class BlogPostGenerator:
	def __init__(self, blogMetadata):
		self.blogMetadata = blogMetadata
		self.outputFolder = blogMetadata.blogFolder
		self.templateFolder = blogMetadata.themesFolder
		self.tagsFolder = os.path.join(self.outputFolder,"tags")
				
	def loadTheme(self, themeName="default"):
		self.templateFolder = os.path.join(self.templateFolder,themeName)
		shutil.copy2(os.path.join(self.templateFolder,"post.css"), self.outputFolder)
		shutil.copy2(os.path.join(self.templateFolder,"index.css"), self.outputFolder)
		shutil.copy2(os.path.join(self.templateFolder,"tag.css"), self.outputFolder)
		shutil.copy2(os.path.join(self.templateFolder,"logo.png"), self.outputFolder)
		shutil.copy2(os.path.join(self.templateFolder,"favicon.png"), self.outputFolder)
		try:
			shutil.copy2(os.path.join(self.templateFolder,"back.png"), self.outputFolder)
		except:
			pass
		
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
		content = {"title": post.title, "date": post.date, "post_text": post.mainText, "index": "index.html", "tags": post.tagsURL, "tagname": self.blogMetadata.tagName+" "}
		
		f = codecs.open(os.path.join(self.outputFolder, post.url),'w','utf-8')
		f.write(renderer.render_path(os.path.join(self.templateFolder, "postTemplate.html"),content))
		f.close()
		
	def generateIndex(self, postList, blogSettings):
		lim = len(postList)+1
		inc = int(self.blogMetadata.postsPerPage)
		lower = 0
		upper = lower+inc
		pageNum = 1
		pageMax = lim/inc + 1

		while upper < lim:
			self.generateIndexPage(postList[lower:upper],pageNum, pageMax, blogSettings)
			lower = upper
			upper = lower+inc
			pageNum = pageNum+1

		if upper != lim:
			self.generateIndexPage(postList[lower:],pageNum, pageMax, blogSettings)

	def generateIndexPage(self, postList, pageNum, pageMax, blogSettings):
		listOfEntries = str()
	
		# Instantiate Renderer
		renderer = pystache.Renderer()
		
		if pageNum == 1:
			f = codecs.open(os.path.join(self.outputFolder, "index.html"),'w','utf-8')
		else: 
			f = codecs.open(os.path.join(self.outputFolder, str("page" + str(pageNum) + ".html")),'w','utf-8')
		
		for post in postList:
			if post is postList[-1]:
				listOfEntries = listOfEntries + '<div class="last-entry"><p class="entry-date">'+post.date+'</p><a class="entry-link" href="./'+post.url+'">'+post.title+'</a></div>'+'\n'
			else:
				listOfEntries = listOfEntries + '<div class="entry"><p class="entry-date">'+post.date+'</p><a class="entry-link" href="./'+post.url+'">'+post.title+'</a></div>'+'\n'
		
		
		# Generate dict
		
		# Generate pagination
		pagination = unicode()

		# Newer pages
		if pageNum > 2:
			pagination = pagination + u'<a class="newer-entries" href=' + 'page' + str(pageNum-1) + '.html>' + '&larr; ' + self.blogMetadata.newerPosts + '</a>'
		elif pageNum == 2:
			pagination = pagination + u'<a class="newer-entries" href=index.html>' + '&larr; ' + self.blogMetadata.newerPosts + '</a>'

		# Page n of m
		pagination = pagination + u'<span class="page-number">'+ self.blogMetadata.page + ' ' + str(pageNum) + ' ' + self.blogMetadata.of + ' ' + str(pageMax) + '</span>'

		# Older pages
		if pageNum < pageMax:
			pagination = pagination + u'<a class="older-entries" href=' + 'page' + str(pageNum+1) + '.html>' + self.blogMetadata.olderPosts + ' &rarr;' + '</a>'
		
		# Generate link to about page if present
		if blogSettings.displayAboutMe.lower() == "yes":
			about = unicode()
			about = u'<a class="about" href="./about.html" >'+self.blogMetadata.aboutHeader+u'</a>'
			content = {"index": "./index.html", "title": self.blogMetadata.blogName, "entries": listOfEntries, "about": about, "pagination": pagination}
			f.write(renderer.render_path(os.path.join(self.templateFolder, "indexTemplate.html"),content))
		else:
			content = {"index": "./index.html", "title": self.blogMetadata.blogName, "entries": listOfEntries, "pagination": pagination}
			f.write(renderer.render_path(os.path.join(self.templateFolder, "indexTemplate.html"),content))
		
		
		f.close()
		
	def generateTags(self, postList):
		listOfTags = list()
		listOfTagNames = list()
		
		# Verify if there is a /tags folder, if not, create
		if not os.path.exists(self.tagsFolder):
			os.makedirs(self.tagsFolder)
		
		# Make a list of tags
		for post in postList:
			for tag in post.tags:
				if not tag in listOfTagNames:
					listOfTagNames.append(tag)
					
					newTag = TagData.TagData(tag)
					listOfTags.append(newTag)
					
				# Dirty method, don't judge me :(
				listOfTags[listOfTagNames.index(tag)].postList.append(post)
			
		# Order posts by date, descending
		for tag in listOfTags:
			tag.postList.sort(key=lambda PostData: PostData.date, reverse=True)		

		# For each tag, generate list of entries (currently only title)
		for tag in listOfTags:
			listOfEntries = str()
			
			# Instantiate Renderer
			renderer = pystache.Renderer()
			
			f = codecs.open(os.path.join(self.tagsFolder, tag.url),'w','utf-8')
		
			for post in tag.postList:
				if post is tag.postList[-1]:
					listOfEntries = listOfEntries + '<div class="last-entry"><p class="entry-date">'+post.date+'</p><a class="entry-link" href="../'+post.url+'">'+post.title+'</a></div>'+'\n'
				else:
					listOfEntries = listOfEntries + '<div class="entry"><p class="entry-date">'+post.date+'</p><a class="entry-link" href="../'+post.url+'">'+post.title+'</a></div>'+'\n'
			
			
			# Generate dict
			content = {"title": self.blogMetadata.blogName, "tag-name": tag.name, "tag-header": self.blogMetadata.tagHeader, "entries": listOfEntries}
			f.write(renderer.render_path(os.path.join(self.templateFolder, "tagTemplate.html"),content))		
			f.close()
			
	def generateAbout(self,post):
		# Instantiate Renderer
		renderer = pystache.Renderer()
		
		# Generate dict
		content = {"title": post.title, "post_text": post.mainText, "index": "index.html", }
		
		f = codecs.open(os.path.join(self.outputFolder, post.url),'w','utf-8')
		f.write(renderer.render_path(os.path.join(self.templateFolder, "postTemplate.html"),content))
		f.close()
		
			
					
		
		
