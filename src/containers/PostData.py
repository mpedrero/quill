#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import datetime

class PostData(object):
	def __init__(self):
		self.url = unicode()  # sanitized final url for the blog post
		self.permalink = unicode() 
		self.author = unicode()
		self.date = unicode()
		self.dateParsed = None
		self.tags = list()
		self.tagsURL = unicode() # tags with href and ready to display
		self.title = unicode()
		self.mainText = unicode()
		self.timeToRead = unicode() # estimated read time
		
		# sharing services
		self.twitterShare = unicode()
		self.facebookShare = unicode()
		self.gplusShare = unicode()

		
		
		
