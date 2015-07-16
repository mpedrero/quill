#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import codecs
import shutil
import pystache
import containers.TagData as TagData
import PyRSS2Gen as RSS2
import datetime


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
		if self.blogMetadata.comments.lower() == "yes":
			content = {"title": post.title, "date": post.date, "post_text": post.mainText, "index": "index.html", "tags": post.tagsURL, "tagname": self.blogMetadata.tagName+" ", "etime": post.timeToRead, "comments": self.blogMetadata.disqusCode}
		else:
			content = {"title": post.title, "date": post.date, "post_text": post.mainText, "index": "index.html", "tags": post.tagsURL, "tagname": self.blogMetadata.tagName+" ", "etime": post.timeToRead}

		f = codecs.open(os.path.join(self.outputFolder, post.url),'w','utf-8')
		f.write(renderer.render_path(os.path.join(self.templateFolder, "postTemplate.html"),content))
		f.close()
		
	def generateIndex(self, postList, blogSettings):
		lim = len(postList)
		inc = int(self.blogMetadata.postsPerPage)
		lower = 0
		upper = lower+inc
		pageNum = 1
		pageMax = lim/inc

		if lim%inc != 0:
			pageMax = pageMax + 1

		while upper < lim:
			self.generateIndexPage(postList[lower:upper],pageNum, pageMax, blogSettings)
			lower = upper
			upper = lower+inc
			pageNum = pageNum+1

		
		self.generateIndexPage(postList[lower:],pageNum, pageMax, blogSettings)

	def generateIndexPage(self, postList, pageNum, pageMax, blogSettings):
		listOfEntries = unicode()
	
		# Instantiate Renderer
		renderer = pystache.Renderer(file_encoding='utf-8', string_encoding='utf-8', decode_errors='utf-8')
		
		if pageNum == 1:
			f = codecs.open(os.path.join(self.outputFolder, "index.html"),'w','utf-8')
		else: 
			f = codecs.open(os.path.join(self.outputFolder, str("page" + str(pageNum) + ".html")),'w','utf-8')
		
		for post in postList:
			if post is postList[-1]:
				listOfEntries = listOfEntries + u'<div class="last-entry"><p class="entry-date">'+post.date+u'</p><a class="entry-link" href="./'+post.url+u'">'+unicode(post.title)+u'</a></div>'+u'\n'
			else:
				listOfEntries = listOfEntries + u'<div class="entry"><p class="entry-date">'+post.date+u'</p><a class="entry-link" href="./'+post.url+u'">'+unicode(post.title)+u'</a></div>'+u'\n'
		
		# Generate dict
		
		# Generate pagination
		pagination = unicode()

		# Newer pages
		if pageNum > 2:
			pagination = pagination + u'<a class="newer-entries" href=' + u'page' + str(pageNum-1) + u'.html>' + u'&larr; ' + self.blogMetadata.newerPosts + u'</a>'
		elif pageNum == 2:
			pagination = pagination + u'<a class="newer-entries" href=index.html>' + u'&larr; ' + self.blogMetadata.newerPosts + u'</a>'

		# Page n of m
		pagination = pagination + u'<span class="page-number">'+ self.blogMetadata.page + u' ' + str(pageNum) + u' ' + self.blogMetadata.of + u' ' + str(pageMax) + u'</span>'

		# Older pages
		if pageNum < pageMax:
			pagination = pagination + u'<a class="older-entries" href=' + u'page' + str(pageNum+1) + u'.html>' + self.blogMetadata.olderPosts + u' &rarr;' + u'</a>'

		# Generate link to about page if present
		if blogSettings.displayAboutMe.lower() == "yes":
			about = unicode()
			about = u'<a class="about" href="./about.html" >'+unicode(self.blogMetadata.aboutHeader)+u'</a>'
			content = {"index": u"./index.html", "rss": u"<a href=feed.xml>rss</a>", "title": self.blogMetadata.blogName, "entries": listOfEntries, "about": about, "pagination": pagination}
			f.write(renderer.render_path(os.path.join(self.templateFolder, "indexTemplate.html"),content))
		else:
			content = {"index": u"./index.html", "rss": u"<a href=feed.xml>rss</a>", "title": self.blogMetadata.blogName, "entries": listOfEntries, "pagination": pagination}
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
			tag.postList.sort(key=lambda PostData: PostData.dateParsed, reverse=True)		

		# For each tag, generate list of entries (currently only title)
		for tag in listOfTags:
			listOfEntries = unicode()
			
			# Instantiate Renderer
			renderer = pystache.Renderer()
			
			f = codecs.open(os.path.join(self.tagsFolder, tag.url),'w','utf-8')
		
			for post in tag.postList:
				if post is tag.postList[-1]:
					listOfEntries = listOfEntries + u'<div class="last-entry"><p class="entry-date">'+post.date+u'</p><a class="entry-link" href="../'+post.url+u'">'+post.title+u'</a></div>'+u'\n'
				else:
					listOfEntries = listOfEntries + u'<div class="entry"><p class="entry-date">'+post.date+u'</p><a class="entry-link" href="../'+post.url+u'">'+post.title+u'</a></div>'+u'\n'
			
			
			# Generate dict
			content = {"title": self.blogMetadata.blogName, "tag-name": tag.name, "tag-header": self.blogMetadata.tagHeader, "entries": listOfEntries}
			f.write(renderer.render_path(os.path.join(self.templateFolder, "tagTemplate.html"),content))		
			f.close()
			
	def generateAbout(self,post):
		# Instantiate Renderer
		renderer = pystache.Renderer()
		
		# Generate dict
		content = {"title": post.title, "post_text": post.mainText, "index": u"index.html", }
		
		f = codecs.open(os.path.join(self.outputFolder, post.url),'w','utf-8')
		f.write(renderer.render_path(os.path.join(self.templateFolder, "postTemplate.html"),content))
		f.close()
		
	def generateRSS(self,postList):

		# create items
		rssItems = []

		for post in postList:
			if self.blogMetadata.completeFeed.lower() == "yes":
				rssItems.append(RSS2.RSSItem(
					title = post.title,
					link =  self.blogMetadata.blogURL+'/'+post.url,
					description = post.mainText,
					guid = RSS2.Guid(self.blogMetadata.blogURL+'/'+post.url),
					pubDate = post.dateParsed))
			else:
				rssItems.append(RSS2.RSSItem(
					title = post.title,
					link =  self.blogMetadata.blogURL+'/'+post.url,
					description = '<a href='+self.blogMetadata.blogURL+'/'+post.url+'>'+post.title+'</a>',
					guid = RSS2.Guid(self.blogMetadata.blogURL+'/'+post.url),
					pubDate = post.dateParsed))

		rss = RSS2.RSS2(
			title = self.blogMetadata.blogName,
			link = self.blogMetadata.blogURL+u"/index.html", 
			description = self.blogMetadata.blogDescription,
			lastBuildDate = datetime.datetime.now(),
			items = rssItems,
			image = RSS2.Image(self.blogMetadata.blogURL+u'/logo.png', self.blogMetadata.blogName, self.blogMetadata.blogURL+u'/index.html')
		)
		rss.write_xml(open(os.path.join(self.outputFolder, "feed.xml"),'w'))
					
		
		
