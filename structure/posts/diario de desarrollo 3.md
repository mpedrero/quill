title:   Desarrollando Quill (II) - Gestión de temas
author:  Manuel Pedrero
date:    2013-12-01
tags:    quill
         development

Aunque Quill está pensado para que el usuario pueda empezar a utilizarlo simplemente escribiendo su primera entrada en Markdown, la primera versión soportará temas personalizados, permitiendo a cualquier persona que sepa un poco de CSS modificar la apariencia de Quill y dejarla a su gusto.

Quill incluye un tema por defecto pensado para verse en todos los navegadores mayoritarios (aún estoy pensando si considerar IE6 mayoritario ;). Los temas en Quill se componen de un par de ficheros CSS y, opcionalmente, un par de ficheros plantilla:

## Ficheros plantilla 

Existen dos ficheros plantilla por defecto: `indexTemplate.html` y `postTemplate.html`. Quill utiliza el sistema de plantillas [Mustache](http://mustache.github.io/), que es bastante simple y cumple sobradamente con su propósito. Si cambiamos estos archivos podremos modificar la estructura de las entradas del blog o del índice de entradas. Por ejemplo, si queremos eliminar la fecha de nuestras entradas en nuestro tema, bastará con eliminar `{{date}}` del fichero correspondiente, o si queremos incluir las etiquetas antes del texto de la entrada, simplemente eliminaremos `{{tags}}` de su ubicación actual y lo incluiremos justo encima de la etiqueta `{{{post_text}}}`. Es una forma muy sencilla y al mismo tiempo potente de definir la estructura general de los elementos del blog.

## Ficheros CSS

Los ficheros CSS definirán los estilos a aplicar en la página principal del blog y en cada una de las entradas. En el tema por defecto, se han utilizado algunos constructores de CSS3, como *media queries* para optimizar el estilo del blog en dispositivos móviles o bordes y sombras para estilizar las entradas.

## Ficheros opcionales

Quill permite personalizar la fuente haciendo uso del constructor `@font-face` de CSS3. Si bien es posible utilizar alguna fuente web como [Google Fonts](http://www.google.com/fonts), se puede utilizar una fuente del propio servidor. Para ello, basta con crear un directorio `fonts` en la carpeta del tema e incluir dentro todas las fuentes que vayan a utilizarse. Cuando Quill detecte ese directorio en el tema, lo copiará al blog final, posibilitando el uso de fuentes personalizadas locales.

Es importante que el directorio se llame exactamente `fonts`, ya que Quill busca específicamente ese nombre en el directorio del tema durante la generación del blog.

## Creación de nuevos temas para Quill

Crear un nuevo tema para Quill es bastante sencillo. Simplemente se debe crear un directorio con el nombre del tema en la carpeta `themes` e incluir al menos los dos ficheros plantilla (indexTemplate.html y postTemplate.html) y los dos ficheros CSS base (index.css y post.css). Para activar el tema en el blog bastará con escribir su nombre en el fichero `quill.cfg`. La próxima vez que se genere el blog se utilizarán las plantillas del nuevo tema y se les aplicarán los estilos CSS correspondientes.

