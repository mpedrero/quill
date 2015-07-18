title:   ¡Bienvenido a Quill!
author:  Quill
date:    2014-01-01
tags:    quill
         

Si puedes ver este artículo, Quill se ha instalado sin problemas ¡Enhorabuena! Ahora es el momento de personalizar tu nuevo blog.

# Primeros pasos con Quill

En la carpeta de Quill, además del ejecutable `quill.exe` y varios archivos binarios, encontrarás el archivo `quill.cfg` que es donde puedes cambiar la configuración de Quill.

## Editando quill.cfg

El archivo de configuración se puede modificar con cualquier editor de texto. Lo que hay que cambiar es el texto que está detrás del símbolo `=`. El texto de antes son los diferentes campos que se describen a continuación, y Quill los utiliza para saber a qué nos estamos refiriendo. De todas formas, si no te quieres complicar la vida, simplemente escribe el nombre que quieres dar a tu blog en el campo `BlogName` y guarda el archivo.

Si quieres editar aspectos más avanzados, a continuación puedes ver todas las opciones disponibles:

### Editando quill.cfg

El archivo de configuración se puede modificar con cualquier editor de texto. Lo que hay que cambiar es el texto que está detrás del símbolo `=`. El texto de antes son los diferentes campos que se describen a continuación, y Quill los utiliza para saber a qué nos estamos refiriendo. De todas formas, si no te quieres complicar la vida, simplemente escribe el nombre que quieres dar a tu blog en el campo `BlogName` y guarda el archivo.

Si quieres editar aspectos más avanzados, a continuación puedes ver todas las opciones disponibles:

#### Editando quill.cfg

El archivo de configuración se puede modificar con cualquier editor de texto. Lo que hay que cambiar es el texto que está detrás del símbolo `=`. El texto de antes son los diferentes campos que se describen a continuación, y Quill los utiliza para saber a qué nos estamos refiriendo. De todas formas, si no te quieres complicar la vida, simplemente escribe el nombre que quieres dar a tu blog en el campo `BlogName` y guarda el archivo.

Si quieres editar aspectos más avanzados, a continuación puedes ver todas las opciones disponibles:

##### Editando quill.cfg

El archivo de configuración se puede modificar con cualquier editor de texto. Lo que hay que cambiar es el texto que está detrás del símbolo `=`. El texto de antes son los diferentes campos que se describen a continuación, y Quill los utiliza para saber a qué nos estamos refiriendo. De todas formas, si no te quieres complicar la vida, simplemente escribe el nombre que quieres dar a tu blog en el campo `BlogName` y guarda el archivo.

Si quieres editar aspectos más avanzados, a continuación puedes ver todas las opciones disponibles:

###### Editando quill.cfg

El archivo de configuración se puede modificar con cualquier editor de texto. Lo que hay que cambiar es el texto que está detrás del símbolo `=`. El texto de antes son los diferentes campos que se describen a continuación, y Quill los utiliza para saber a qué nos estamos refiriendo. De todas formas, si no te quieres complicar la vida, simplemente escribe el nombre que quieres dar a tu blog en el campo `BlogName` y guarda el archivo.

Si quieres editar aspectos más avanzados, a continuación puedes ver todas las opciones disponibles:

## Sección Basic

+ **BlogName**: Aquí puedes escribir el nombre de tu blog. Aparecerá en la página principal del mismo.
+ **Theme**: Aquí puedes seleccionar un tema (puedes ver los temas disponibles en la carpeta *themes*. Si no quieres cambiarlo, se usará el tema por defecto.

## Sección Folders

En esta sección podremos modificar las carpetas donde vayamos a guardar nuestras entradas, los temas, etc. Normalmente lo único que querrás cambiar aquí es el directorio donde se generará el blog.

+ **PostsFolder**: Aquí puedes modificar la carpeta donde guardarás las entradas de tu blog.
+ **DraftsFolder**: Aquí puedes modificar la carpeta donde guardarás los borradores de las entradas de tu blog. Estas entradas no se publicarán hasta que no las muevas a la carpeta PostsFolder.
+ **ThemesFolder**: Aquí puedes modificar la carpeta donde se guardan los distintos temas del blog.
+ **BlogFolder**: Aquí puedes modificar la carpeta donde se generará el blog. Una idea interesante puede ser poner esta carpeta dentro del directorio `Public` de Dropbox. De este modo podrás ver tu blog online en cuanto lo generes.
+ **ImgsFolder**: Aquí puedes modificar la carpeta donde se almacenarán las imágenes de las entradas. Una idea interesante es poner esta carpeta dentro del directorio de las entradas, para que sean más sencillas de referenciar en Markdown. Ahora mismo,esta carpeta debe llamarse `images`, aunque se podrá configurar completamente en la siguiente versión.

## Sección BlogContent

+ **AboutMe**: Este campo está activado por defecto (Yes). De este modo, Quill busca si existe una entrada con el nombre `about.md` y la considera el *about me* del blog. Si no quieres que el blog tenga esta característica, cámbiala a No.
+ **PostsPerPage**: Este campo indica el número de entradas que se mostrarán en cada página del índice de entradas. Por defecto está establecido en 10. Ahora mismo, esta opción no está habilitada, ya que Quill de momento no separa las entradas en páginas. En la siguiente versión se habilitará la paginación.

## Sección Misc

+ **TagName**: Aquí puedes establecer el texto que se mostrará antes de las etiquetas de la entrada.
+ **TagHeader**: Aquí puedes establecer el texto que se mostrará en el encabezado del índice de una determinada etiqueta.
+ **AboutHeader**: Aquí puedes establecer el texto que se mostrará en la página principal para llevarte a la página *about me*.
+ **Footer**: Aquí puedes establecer el texto que se mostrará al pie de la página principal. En esta versión Quill no procesa este pie de página, aunque se activará más adelante.

# Escribiendo tu primera entrada

Para escribir tu primera entrada, crea un archivo de texto vacío con cualquier editor (en Windows puedes usar MarkdownPad o el mismo Bloc de Notas) y copia lo siguiente:

	title:   Mi título
	author:  John Doe
	date:    2013-12-31
	tags:    quill

Estos datos son necesarios para que Quill establezca el título del artículo, su autor, la fecha de publicación y las etiquetas (éstas últimas son opcionales). Es importante que la fecha esté en formato `YYYY-MM-DD`.

Cuando hayas terminado de modificar estos datos, deja una línea en blanco (pulsando INTRO un par de veces) y empieza a escribir tu entrada. 

Si tienes alguna duda sobre Markdown, puedes mirar la [página oficial](http://daringfireball.net/projects/markdown/syntax), puedes consultar esta [hoja resumen](http://packetlife.net/media/library/16/Markdown.pdf) o incluso puedes ver cómo se ha escrito esta entrada abriendo el fichero `welcome.md` de tu carpeta de entradas.

Cuando termines de escribir la entrada, guárdala en el directorio de entradas con la extensión `.md`.

# Publicando tu primera entrada

Para publicar tu entrada, basta con hacer doble click en el icono del programa `quill.exe`. Puedes crear un acceso directo para no tener que ir a la carpeta cada vez que quieras publicar una nueva entrada.

Si todo ha ido bien, deberías ver algo parecido a la siguiente imagen:

![Todo perfecto](images/perfecto.png)

Pulsa INTRO para cerrar la ventana y ya tendrás tu blog completo en la carpeta del blog (por defecto es `mi-blog`, pero puedes cambiarla en `quill.cfg`. Para ver tu blog, basta con hacer doble click en la página de inicio `index.html`

# Consejo extra

Cuando termines, seguramente querrás borrar esta entrada para que no aparezca en tu blog. En lugar de eso, muévela a un sitio seguro (como la carpeta de borradores). De este modo, cuando quieras escribir una nueva entrada, puedes cargar ésta a modo de guía para no olvidarte de ningún campo importante.
