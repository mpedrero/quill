title:   Desarrollando Quill (V) - Página About
author:  Manuel Pedrero
date:    2013-12-28
tags:    quill
         diario desarrollo

De momento, y en aras de mantener los tres principios de Quill (simple, ligero, elegante) no quiero añadir los típicos botones de redes sociales a cada entrada del blog. Una posibilidad alternativa que he barajado es ponerlos al final de la entrada y de forma poco intrusiva, para que el lector, **una vez haya leído el artículo** se plantee si quiere o no compartirlo. Sin embargo, por ahora prefiero que la página de la entrada del blog quede lo más limpia posible.

¿Y si el lector desea más información sobre el autor, o buscarlo en alguna red social o, simplemente, ponerse en contacto con él? Para eso existe la página *about me*, donde el autor puede dejar su correo, dar algunos datos sobre él mismo, poner alguna foto, etc.

Para la primera versión de Quill, la única funcionalidad que queda por implementar (aunque varias aún necesitan un pulido) es dar la posibilidad al autor de escribir dicha página. El enfoque más simple que se me ocurre es que escriba en su directorio de entradas una con el nombre `about.md` y que Quill se encargue de maquetar dicha página y enlazarla en la página principal del blog. Otro enfoque sería crearla a partir de los datos del archivo de configuración `quill.cfg`, aunque esta opción me gusta menos. La ventaja del segundo enfoque es que permitiría usar los datos del autor, las redes sociales o la dirección de correo para añadirlas en el resto de entradas, pero tengo que pensar con mucho cuidado qué mantener en la versión final.

> "La perfección se alcanza, no cuando no hay nada más que añadir, sino cuando ya no queda nada más que quitar"

Una vez haya terminado la página about y refactorizado un poco el código (aunque es bastante simple) subiré la primera versión a GitHub y, si no hay ningún bug importante, me pondré a trabajar tranquilamente en la versión 0.2 que incluirá, entre otras características, la generación de un feed RSS, algo prácticamente necesario en un blog si el lector quiere agregarlo a algún servicio como Feedly.
