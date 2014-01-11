#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import markdown
import codecs
import ConfigParser
import readers.MarkdownReader as MarkdownReader
import containers.PostData as PostData
import generators.BlogPostGenerator as BlogPostGenerator
import os


class BlogMetadata():
	def __init__(self):
		self.blogName = unicode()
		self.blogDescription = unicode()
		self.blogURL = unicode()
		self.blogTheme = unicode()
	
		self.postsFolder = unicode()
		self.draftsFolder = unicode()
		self.themesFolder = unicode()
		self.imagesFolder = unicode()
		self.blogFolder = unicode()

		self.displayAboutMe = unicode()
		self.postsPerPage = unicode()
		self.completeFeed = unicode()
		self.comments = unicode()
		self.disqusCode = unicode()
		
		self.tagName = unicode()
		self.tagHeader = unicode()
		self.aboutHeader = unicode()
		self.newerPosts = unicode()
		self.olderPosts = unicode()
		self.page = unicode()
		self.of = unicode()
		
	''' Reads quill.cfg file to load blog settings '''
	def loadConfig(self,filename):
		config = ConfigParser.RawConfigParser()
		config.readfp(codecs.open(filename,'r','utf-8'))

		self.blogName = config.get("Basic", "BlogName")
		self.blogDescription = config.get("Basic", "BlogDescription")
		self.blogURL = config.get("Basic", "BlogURL")
		self.blogTheme = config.get("Basic", "Theme")

		self.postsFolder = config.get("Folders", "PostsFolder")
		self.draftsFolder = config.get("Folders", "DraftsFolder")
		self.themesFolder = config.get("Folders", "ThemesFolder")
		self.imagesFolder = config.get("Folders", "ImgsFolder")
		self.blogFolder = config.get("Folders", "BlogFolder")

		self.displayAboutMe = config.get("BlogContent", "AboutMe")
		self.postsPerPage = config.get("BlogContent", "PostsPerPage")
		self.completeFeed = config.get("BlogContent", "CompleteFeed")
		self.comments = config.get("BlogContent", "Comments")

		self.tagName = config.get("Misc", "TagName")
		self.tagHeader = config.get("Misc", "TagHeader")
		self.aboutHeader = config.get("Misc", "AboutHeader")
		self.newerPosts = config.get("Misc", "NewerPosts")
		self.olderPosts = config.get("Misc", "OlderPosts")
		self.page = config.get("Misc", "Page")
		self.of = config.get("Misc", "Of")
		

def main():
	# Variables
	postList = list()
	postDataList = list()
	
	# 0. Display program and version
	print "quill - v0.1a"
	print

	# 1. Read config file to load the metadata
	print "Reading config file...",
	blogSettings = BlogMetadata()
	blogSettings.loadConfig("quill.cfg")	
	print "[OK]"
	
	# 1.1. If comments are enabled, load Disqus string to adding it to the posts
	print "Comments?",
	if blogSettings.comments.lower() == "yes":
		print "Yes, loading Disqus.txt"
		disqusFile = open("disqus.txt","r")
		blogSettings.disqusCode = disqusFile.read()
	else:
		print "No, skipping..."


	# 2. Analyse postsFolder and search *.md files to process
	print "Processing posts...",

	# 2.1 Generate list of files to process
	for root, dirs, files in os.walk(blogSettings.postsFolder):
		for file in files:
		    if file.endswith(".md"):
		         postList.append(os.path.join(root, file))
	print "[OK]"
	
	
	# 3. Process *.md files to generate PostData
	print "Generating post data...",
	reader = MarkdownReader.MarkdownReader(blogSettings.postsFolder)
	
	if blogSettings.displayAboutMe.lower() == "yes":
		for post in postList:
			if post.lower().endswith("about.md"):
				aboutPost = reader.readNoMetadata(post)
				aboutPost.title = blogSettings.aboutHeader
			else:
				postDataList.append(reader.read(post))
	else:
		try:
			os.remove(os.path.join(blogSettings.blogFolder,"about.html"))
		except:
			pass
			
		for post in postList:
			if post.lower().endswith("about.md"):
				pass
			else:
				postDataList.append(reader.read(post))
		
	# 3.1. Order PostData files by date (newest posts first)
	postDataList.sort(key=lambda PostData: PostData.dateParsed, reverse=True) 
	print "[OK]"

	# 4. Generate blog from Post
	print "Generating blog...",
	
	# 4.1. Initialise generator and set theme
	generator = BlogPostGenerator.BlogPostGenerator(blogSettings)
	generator.loadTheme(blogSettings.blogTheme)
	
	# 4.2. Copy images
	generator.loadImages()
	
	# 4.2. Generate blog entries
	for post in postDataList:
		generator.generatePost(post)
		
	# 4.3. Generate index
	generator.generateIndex(postDataList, blogSettings)
		
	# 4.4. Generate about page
	if blogSettings.displayAboutMe.lower() == "yes":
		generator.generateAbout(aboutPost)
		
	print "[OK]"
	
	# 5. Generate tags (if necessary)
	print "Generating tags...",
	
	generator.generateTags(postDataList)
	
	print "[OK]"

	# 6. Generate RSS (if necessary)
	print "Generating RSS feed...",
	generator.generateRSS(postDataList)
	print "[OK]"
	
	print
	print "Blog complete. Press ENTER key to exit"
	raw_input()




if __name__ == "__main__":
	main()
