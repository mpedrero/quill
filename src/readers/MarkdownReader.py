#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import markdown
import codecs
import containers.PostData as PostData
import os
import slugify # https://github.com/un33k/python-slugify
import dateutil.parser # pip install python-dateutil
from urlparse import urljoin

class MarkdownReader:
	def __init__(self,postsFolder):
		self.postsFolder = postsFolder
	
	''' Read and process the Markdown file without reading the metadata '''			
	def readNoMetadata(self, filename):
		f = codecs.open(filename,'r',"utf-8")
				
		md = markdown.Markdown()	
		mainText = md.convert(f.read())
		
		postData = PostData.PostData()

			
		# Mediante este reemplazo anadimos una clase a los bloques de codigo para poderles
		# aplicar un estilo determinado. Hay que comprobar si es error prone
		postData.mainText = mainText.replace("<pre><code>",'<pre class="block_code"><code class="block_code">')
		 
		postData.url = slugify.slugify(filename.replace(self.postsFolder,"",1).rstrip('.md'))+".html"
		
		return postData
	
	''' Read and process the Markdown file. Metadata is mandatory '''	
	def read(self, filename, blogSettings):
		f = codecs.open(filename,'r',"utf-8")
				
		md = markdown.Markdown(extensions = ['meta', 'smarty'])	
		mainText = md.convert(f.read())
		
		postData = PostData.PostData()
		
		try:
			postData.author = md.Meta["author"][0]
		except:
			try:
				postData.author = blogSettings.blogAuthor
			except:
				print "Missing author in post", filename
				quit()
			
		try:
			postData.date = md.Meta["date"][0]
		except:
			print "Missing date in post", filename
			quit()

		try:
			postData.dateParsed = dateutil.parser.parse(postData.date)
			postData.date = postData.dateParsed.strftime("%d %b %Y")
		except:
			print "Date not recognized. Try YYYY/MM/DD"

		try:
			for tag in md.Meta["tags"]:
				postData.tags.append(tag)
				postData.tagsURL = postData.tagsURL + '<a class="tag" href="tags/'+slugify.slugify(tag)+'.html">'+tag+'</a> '
		except:
			pass
			
		try:
			postData.title = md.Meta["title"][0]
		except:
			print "Missing title in post", filename
			quit()
			
		# Calculate and generate wordcount
		try:
			numWords = 0
			f.seek(0,0)
			for line in f:
				numWords += len(line.split())
				
			ela = int(numWords/270)
			
			if (ela == 0):
				postData.timeToRead = u'<span class="etime">' + u'Less than a min read' + u'</span>'
			else:
				postData.timeToRead = u'<span class="etime">' + str(ela)+u" "+u"min read" + u"</span>"
				
		except:
			print "Unable to estimate read time"
			
		# Mediante este reemplazo anadimos una clase a los bloques de codigo para poderles
		# aplicar un estilo determinado. Hay que comprobar si es error prone
		postData.mainText = mainText.replace("<pre><code>",'<pre class="block_code"><code class="block_code">')
		 
		postData.url = slugify.slugify(filename.replace(self.postsFolder,"",1).rstrip('.md'))+".html"
		print "BLOGURL",blogSettings.blogURL
		print "ARTICLE",postData.url
		postData.permalink = '/'.join([x.strip('/') for x in [blogSettings.blogURL,postData.url]])
		print "PERMALINK:",postData.permalink
		return postData
		
		
		
		
