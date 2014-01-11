#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import datetime

class PostData(object):
	def __init__(self):
		self.url = unicode()  # sanitized final url for the blog post 
		self.author = unicode()
		self.date = unicode()
		self.dateParsed = None
		self.tags = list()
		self.tagsURL = unicode() # tags with href and ready to display
		self.title = unicode()
		self.mainText = unicode()

		
		
		
