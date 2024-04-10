## TAREA 1 - ALONSO ANDRES HERRERA ROZAS

Para esta tarea 1, se desarrollaron las 7 vistas solicitadas.

Para `agregar-producto.html` y `agregar-pedido` se generaron los forms solicitados. Además, usando JS se creo un render condicional, es decir, no se muestran comunas o productos hasta que se seleccione region o tipo de producto respectivamente, de esta forma evitamos inputs erroneos por parte de los usuarios. La seleccion de productos se hace con el mouse y el control, de esta manera se pueden seleccionar varias opciones de productos. Para los demas campos se hicieron validaciones simples con JS, y para el campo de numero de celular, el input valido que recibe el programa son numeros con codigo de Chile, es decir con el formato 569XXXXXXXX. Finalmente, el botón de agregar producto o agregar pedido, muetra una alerta que solicita la confirmacion del usuario al registrar el forms. Si confirma entonces se deja de mostrar el formulario y se muestra un boton para volver a `index.html`, de lo contrario, si lo cancela se sigue mostrando el formulario con los campos conteniendo la informacion que se agrego previamente.

Para `ver-pedidos.html` e `ver-productos.html` se utilizo una tabla simple para mostrar 5 registros estaticos de ejemplo. Se puede hacer click sobre una fila de esta tabla para ir a `informacion-pedido.html` o `informacion-producto.html` segun la vista correspondiente. Aca se muestran los detalles, y para `informacion-producto.html` se usa JS para modificar el tamaño de la imagen del producto con posibilidad de volver al tamaño original o inicial haciendo click nuevamente.

Soy consciente que se podría hacer una mejor administración y organización de funciones y archivos para evitar repeticiones de código y seguir los principios SOLID, sin embargo por temas de tiempo, carga académica y simplicidad se dejó como está. Espero para la siguiente entrega solucionar este tema.

:D
