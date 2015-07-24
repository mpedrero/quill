Quill - A (very) simple blog engine
===================================
**TODO for future releases**

* Show a text snippet in index pages (summary)
* User Manual
* Developer Manual
* **[IN PROGRESS]** Integrate Pygments for syntax highlighting
* [BUG] Program fails when About Me = Yes and no about file
* [BUG] Program fails when theme has not `fonts/` folder
* Detecting changes in folders
* SQLite database for entries and tags (neccesary?)
* Choose webserver (lighttpd?, custom?)
* --reconfigure option to generate quill.cfg
* --reparse option to delete all blog folder (useful when some articles have been deleted)
* --blog <blogid> option to generate only specified blog (¿?)
* --upload option to upload blog to server if has been successfully generated (ssh)

**TODO for version 0.1:**

* **[DONE]** MarkDown -> HTML converter
* **[DONE]** Folder structure
* **[DONE]** Multipagination in index pages
* **[DONE]** Favicon 
* **[DONE]** Simple CSS sample
* **[DONE]** Config via .ini or similar
* **[DONE]** Tag support
* **[DONE]** RSS/Atom
* **[DONE]** Dropbox Integration
* **[DONE]** Bad encoding sometimes ¿¿?? Apparently, when I set 1 post per page, if title has no special characters, encoding fails. If not, encoding seems correct...

**TODO for version 0.2**

* **[DONE]** Add comments
* **[DONE]** Display time to read
* **[DONE]** Author tag
* **[DONE]** Permalink tag
* **[DONE]** Author in config and use it by default in absence of metadata in post
* **[DONE]** Theme with PT and PT Sans
* **[DONE]** More specific tags to further customisation
* **[DONE]** Smartypants support
* **[DONE]** Google Analytics Support
* **[DONE]** Social integration (twitter, facebook, g+?)
* **[DONE]** Erase blog folder before regenerate the blog
* Better default theme


**Suitable Tags for templates**

0. General tags
  {{index}}        href to blog index page

1. Tags related to article

		  {{title}}        Title of the article.                    No html element.
		  {{date}}         Date of the article.                     No html element.
		  {{{etime}}}      Estimated reading time of the article    <span class="etime" />
		  {{author}}       List of article author                   No html element.
		  {{{tags}}}       List of article tags                     <a href="..." class="tag">tag1</a> ...
		  {{{post_text}}}  Text of the article                      Html content. Should be inside a <div>
		  {{{comments}}}   Code to embed disqus comments            Html content. Should be inside a <div>
		  {{permalink}}    Permalink to current article             No html element.

		  {{{tagsURL}}}    Tags with "<a href...>" ready to display
		  {{shTwitter}}    Custom link to share article on Twitter  No html element.
		  {{shFacebook}}   Custom link to share article on Facebook No html element.
		  {{shGplus}}      Custom link to share article on G+       No html element.
  
