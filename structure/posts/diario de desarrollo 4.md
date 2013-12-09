title:   Etiquetas
author:  Manuel Pedrero
date:    2013-12-09
tags:    quill
         development

Aunque Quill pretende ser un engine para blog simple, sí que soportará etiquetas. Las etiquetas o *tags* son muy útiles para mantener organizados los distintos temas del blog, y permiten a su vez que el lector pueda descubrir artículos relacionados con una entrada interesante que acabe de leer: bastará con que pulse en una de las etiquetas del blog para que se muestre una lista de todas las entradas.

También existen las categorías que, aunque funcionalmente son similares, cumplen un cometido ligeramente distinto. Todavía no he decidido si Quill soportará categorías, ya que quiero mantenerlo simple.

# Tratamiento de las etiquetas

Asignar etiquetas a una entrada del blog es tan simple como escribirlas en el encabezado del texto, una en cada línea. Un ejemplo puede ser esta entrada, que como todas las del *diario de desarrollo de Quill* tiene las etiquetas *quill* y *development*. En mi caso las he definido como:

    tags: quill
          development
  
Internamente, si en el fichero de configuración hemos especificado que queremos mostrar las etiquetas, el engine analizará las entradas que hayamos escrito (en el directorio `/posts`) en busca de etiquetas, y construirá una lista de etiquetas. A continuación generará un directorio `/tags` en el blog final y una página para cada etiqueta que contendrá la lista de entradas que la contengan con su correspondiente enlace. Este enfoque, aunque simple, tiene ciertas ventajas:

+ Mantenemos una estructura de directorios sencilla en el blog final.
+ Podemos enlazar fácilmente a las páginas generadas. Por ejemplo, para enlazar a la [lista de entradas de la etiqueta quill](tags/quill.html), simplemente enlazamos a `tags/quill.html`.
+ Aunque seguramente la página de inicio del blog tenga más adelante la opción de mostrar una lista de etiquetas, se pueden ver rápidamente ya que estarán todas en el directorio `/tags` del blog.

# Versión 0.1 en camino

Una vez implementadas las etiquetas, la primera versión de Quill estará lista para ser liberada. Aún estoy pensando qué licencia utilizar y dónde subir el repositorio público, aunque seguramente opte por GitHub. 

Sin embargo, aunque no falte mucho por añadir, aún no sé cuánto tiempo me llevará publicar esta primera versión: quiero redactar un manual de uso y configuración básico y pulir un poco el tema por defecto para que sea un engine funcional desde la primera versión.

