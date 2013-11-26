import markdown
import codecs
import containers.PostData as PostData
import os
import slugify # https://github.com/un33k/python-slugify

class MarkdownReader:
	def __init__(self,postsFolder):
		self.postsFolder = postsFolder
				
	def read(self,filename):
		f = codecs.open(filename,'r',"utf-8")
				
		md = markdown.Markdown(extensions = ['meta'])	
		mainText = md.convert(f.read())
		
		postData = PostData.PostData()
		
		postData.author = md.Meta["author"][0]
		postData.date = md.Meta["date"][0]

		for tag in md.Meta["tags"]:
			postData.tags.append(tag[0])

		postData.title = md.Meta["title"][0]
		postData.mainText = mainText
		
		postData.url = slugify.slugify(filename.replace(self.postsFolder,"",1).rstrip('.md'))+".html"
		
		return postData
		
		
		
