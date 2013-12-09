title:   Dependencias de Quill
author:  Manuel Pedrero
date:    2013-12-08
tags:    quill
         development
         
Quill depende de las siguientes librerías externas de Python:

+ **python-markdown**: se utiliza para convertir los posts de Markdown a código HTML. Está disponible en los repositorios de la mayoría de distribuciones Linux.
+ **pystache**: es un _wrapper_ de la librería [Mustache](http://mustache.github.io/) que se usa para definir plantillas y poder configurar el aspecto de las distintas secciones del blog (página principal, about, posts, etc). Esta librería se puede obtener de su [repositorio en GitHub](https://github.com/defunkt/pystache)
+ **slugify**: se utiliza para generar direcciones web legibles. Con esto conseguimos direcciones como `miblog/tutorial-markdown`en lugar de `miblog/article/213833`. Los nombres se generan a partir del nombre del archivo del post original escrito en Markdown. Esta librería se puede obtener de su [repositorio en GitHub](https://github.com/un33k/python-slugify)

Además de éstas, Quill hace uso de las siguientes librerías internas de Python:

+ **os**: se utiliza sobre todo para realizar operaciones sobre los archivos (crear nuevos archivos para los posts, copiar los ficheros CSS y las imágenes, crear directorios si es necesario, etc).
+ **codecs**: se utiliza para poder aceptar de forma transparente distintos _encodings_ de texto como `latin-1`, que suele usarse por defecto en Windows o `utf-8`, que se suele usar en Linux. Gracias a esta clase evitamos problemas con acentos o caracteres no ASCII.
+ **shutil**: se utiliza para algunas operaciones sobre archivos y directorios que no cubre el paquete **os**. específicamente la copia y eliminación recursiva de directorios.