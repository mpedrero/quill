title:   Desarrollando Quill
author:  Manuel Pedrero
date:    2013-11-25
tags:    quill
         development

A la hora de desarrollar Quill, he intentado fijarme unas metas plausibles y 
alcanzables. Para ello, lo primero que hice fue establecer una serie de objetivos
básicos para tener una versión mínimamente funcional pero con una buena arquitectura
que permitiese ampliarla más adelante.

De cara a la versión 0.1, fijé los siguientes objetivos:

**Versión 0.1**

* Desarrollar un conversor que permita leer un fichero Markdown y generar el código
  HTML equivalente.
  
* Diseñar una estructura de ficheros y directorios clara y coherente tanto para el
  programa como para el blog generado.
  
* Diseñar un tema básico para las entradas del blog y para la página principal, que
  contendrá el índice de entradas.
  
* Desarrollar un parseador para el fichero de configuración, que seguirá el formato *.ini*
  por ser sencillo de entender, sencillo de editar y sencillo de parsear.

A día de hoy, estos objetivos están prácticamente cubiertos. En su estado actual,
el engine carga la configuración desde el fichero `quill.cfg`, accede al directorio
donde el usuario ha puesto las entradas de los blogs, procesa los ficheros Markdown
y genera unos ficheros de datos intermedios en memoria, en este caso en el objeto `PostData`
que contiente campos para almacenar diversos metadatos del post, como el autor, la fecha, los
tags o el propio contenido. Una vez procesados todos los ficheros Markdown, el engine
generará el blog en el directorio especificado por el usuario en el fichero `quill.cfg`. Para
ello comienza generando un fichero HTML por cada entrada que ha procesado y a continuación
genera una página principal, que de momento sólo contiene el logotipo del blog, su nombre y
un índice de entradas que enlaza a cada una de ellas.

Si estás leyendo esta entrada quiere decir que el engine funciona aunque sea en su forma
más básica, ya que la entrada ha sido generada a partir de un fichero Markdown.

Aunque el aspecto del blog todavía es bastante tosco, sí que se ha conseguido una
buena arquitectura, ya que permite extender el engine fácilmente y a la vez mantiene un diseño muy simple. Si hablamos de posibilidades de ampliación, a día de hoy el engine permite:

* Crear nuevos temas y cargarlos al vuelo a la hora de generar el blog, o especificándolo
  manualmente en el fichero `quill.cfg`
  
* Crear nuevas estructuras de páginas para las entradas, el índice o cualquier otro
  tipo de página que se desee generar. Esto ha sido posible gracias a permitir el uso
  de templates. En concreto, Quill es compatible con el sistema de templates [Mustache](http://mustache.github.io/),
  que sigue la filosofía de diseño simple del engine. Mediante el uso de templates y 
  la modificación de ficheros CSS es muy sencillo crear nuevos temas para personalizar
  el blog. Para crear un nuevo tema basta con crear una nueva carpeta en el nuevo directorio de
  temas, copiar los archivos CSS y HTML de los templates y cargar el tema en el fichero
  `quill.cfg`.
  
* Es muy sencillo ampliar el soporte de Quill a otros formatos de entrada como Textile, Rdoc
  o RST. Quill utiliza un formato intermedio para transformar los ficheros Markdown en el blog (PostData).
  Se ha modularizado el conversor de Markdown a PostData, por lo que para añadir soporte a otro
  formato de entrada, sólo hay que implementar otro *reader* que transforme el texto de entrada
  a PostData. Una vez hecho esto, el engine se encargaría del resto de operaciones.
  
* Asimismo, es sencillo implementar nuevos tipos de página (como un About Me), ya que los generadores
  de contenido, que se encargan de transformar el formato intermedio PostData a un conjunto de 
  ficheros HTML también están encapsulados en el módulo *generators*, lo que permite implementar
  nuevos generadores que añadan nuevas funcionalidades.
  
La estructura seguida por Quill está inspirada en la usada en [Pelican](http://docs.getpelican.com/en/3.3.0/report.html#design-process) aunque con un diseño bastante más simple (Pelican tiene muchísimas más funcionalidades disponibles). 
  
Un problema que por ahora no ha sido solventado es el uso de imágenes locales a la hora de
redactar textos. Por ahora, seguramente se opte por colocar un subdirectorio `/images` en la
carpeta de los posts, de modo que el usuario referencie todas las imágenes de los posts dentro de
dicha carpeta y el generador simplemente copie la carpeta y su contenido al blog una vez procesados los ficheros. Aunque Quill permite usar subdirectorios en la carpeta `/posts` es probable que
haya problemas con la generación de referencias a imágenes si se usan subdirectorios. Es probable
que el sistema se mejore en un futuro para corregir estos errores.

De cara a versiones posteriores, se barajan características como:
* RSS/Atom

* Integración con Dropbox

* Integración con Disqus (o similar)

* Integración con redes sociales

* Tags

* Categorías

Sin embargo, no es seguro que finalmente se implementen todas estas funciones. Quill pretende
ser un engine **simple, ligero y elegante**, por lo que habrá que estudiar cuando llegue el momento
qué características son realmente compatibles con esta filosofía.
