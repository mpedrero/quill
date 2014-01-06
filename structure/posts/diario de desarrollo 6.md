title: Desarrollando Quill (VI) - Paginación de entradas
author: Manuel Pedrero
date: 2014/1/6
tags: quill
      diario desarrollo

Cuando un blog comienza a tener un número de entradas considerable, cargarlas todas en la página principal puede resultar poco adecuado. Por una parte, la página puede llegar a ser muy larga, por lo que dificultamos la navegación del lector. Por otra parte, al cargar mucho contenido necesitamos transferir más datos, por lo que la carga se enlentece.

El problema se acentúa si pensamos que cuando un lector habitual accede al blog, normalmente lo que querrá es comprobar si hay alguna entrada nueva y leerla, no navegar buscando entradas antiguas. La solución más obvia es *paginar* el blog, de manera que cuando se acceda al mismo sólo se muestren las entradas más recientes. Para acceder a entradas más antiguas se deberá pulsar en un botón, con lo que se cargarán otra tanda de entradas.

Como se puede ver en este mismo blog, Quill implementa esta paginación y da al usuario la posibilidad de modificar el número de entradas que quiere mostrar en cada página. Para ello bastará con que edite el fichero `quill.cfg` y modifique el valor de la entrada `PostPerPage`, que actualmente está a 5.

Con esta característica implementada, lo único que me queda por incluir (además de retocar el tema por defecto) es la generación de un feed RSS, y con esto tendré lista la primera versión pública de Quill.

