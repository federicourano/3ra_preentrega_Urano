Hola!!

Esta es mi trabajo final, espero que les guste.

Mi trabajo se llama "Libreria Virtual". Consiste, como su nombre indica, 
en una libreria donde podremos ver informacion de libros, autores, sagas 
y el staff que alli trabaja. Esta informacion solo es accecible una vez
que hayamos creado un usuario y logueado. 


Para acceder, levantar el servidor y dirigirse a http://localhost:8000/miaplicacion/


Para crear un usuario, hacer click en "registrarse" y rellenar con la info pedida.

Para loguearse, hacer click en "Login" y rellenar los datos pedidos.

Ya contamos con un superusuario creado, su username es "admin" y su contraseña es "coderhouse"



Los modelos que uso son, justamente, libros, autores, sagas, y staff.

Libros contiene el ID, nombre del libro y cantidad de paginas del libro.

Autores contiene el ID, nombre, apellido y edad del autor.

Sagas contiene el ID, nombre de la saga y cantidad de libros que conforman esa saga.

Staff contiene el ID, nombre, apellido, dni, y email del staff


Si estamos logueado, ademas de ver la informacion, podremos agregar, modificar o eliminar 
informacion que hay en los modelos. Es decir, por ejemplo, en la parte de libros
podremos agregar un libro, modificarlo, o borrarlo.

Tambien, solo en la seccion de libros, contamos con un boton de busqueda, en el cual
si escribimos el nombre del libro, nos traera todos los libros con ese nombre
(Por ejemplo, si buscamos la palabra "el" nos traera todos los libros que contengan "el" en el nombre)

Se puede editar la informacion del perfil del usuario logueado, es decir, su nombre y apellido y email
en la seccion de "editar perfil". 
Tambien se puede modificar su contraseña en la seccion de "Cambiar contraseña"

Se puede cambiar su foto avatar, en la seccion "Cambiar avatar"

Se puede hacer logout en la seccion de "Logout"

Se puede acceder al panel de "Administracion" siendo un superusuario

Y hay una seccion de "Acerca de mi" que tiene informacion mia, y de como la pase en el curso







