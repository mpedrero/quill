# [Quill](http://quillbe.com) - A (very) simple blog engine

By Manuel Pedrero

Quill is a (very) simple blog generator. It takes a `posts` folder with blog entries written in Markdown, processes them and builds an entire blog. Quill have not any server dependencies like PHP or databases, so you can host the blog in many servers, including  [NGINX](http://nginx.org/), [Apache](http://httpd.apache.org/), [Lighttpd](http://www.lighttpd.net/)... even your Dropbox Public folder is OK.

## Current features

* Blog entries written in Markdown
* No server side requirements (only http server)
* One click publishing
* Simple CSS theme, mobile aware
* Custom themes support
* Single file configuration
* Tags support
* RSS feed
* Dropbox aware
* Comments support via Disqus
* Windows builds

## Planned features

* Social integration
* Analytics
* Pygments integration for syntax highlighting
* Estimated read time
* Complete entries in RSS feed
* User manual (wiki?)
* Developer manual (wiki?)
* Better logo
* Autonomous comment system


## Getting Started

### Windows
If you are using **Windows**, the easiest way is to [download latest release](https://dl.dropboxusercontent.com/u/2904420/quill-builds/quill-latest.zip). Unzip it in your preferred folder and double-click in `quill.exe`. Your blog will be generated in `blog` subfolder.

### Linux and MacOS
If you are using **Linux**, **MacOS** or you prefer to use Quill from source code:

1. Install Python 2.X.
2. Install Python `pip` and `setuptools`. If you are using Windows, you can install them [from here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools).
3. Install Quill dependencies using pip:

		pip install PyRRS2Gen
		pip install pystache
		pip install python-dateutil
		pip install python-markdown
		pip install slugify

4. Download Quill source from GitHub.
5. Execute Quill with `python quill.py` to create (or regenerate) your blog. It will be generated in `blog` subfolder.


## Dependencies
* **PyRSS2Gen**: RSS generator (python)
* **pystache**: Mustache template system (python)
* **python-dateutil**: Date and time handling (python)
* **python-markdown**: Markdown engine (python)
* **slugify**: String cleaning (python)

## Contributors

* Background pattern in `ghost-dropbox` theme downloaded from [SubtlePatterns](http://subtlepatterns.com/). Thanks to Atle Mo!
* `Ghost-dropbox` theme, currently used as the default Quill theme is heavily inspired in default theme from [Ghost blogging platform](https://ghost.org/). by John O'Nolan. If you want to contribute a new theme, contact me please.

## License

See [LICENSE](https://github.com/mpedrero/quill/blob/master/LICENSE.md).
