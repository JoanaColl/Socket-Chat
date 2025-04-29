
# Socket-Chat 🚀

## Propuesta Formativa Obligatoria 

Implementación de un Chat Básico Cliente-Servidor con Sockets y Base de Datos
### Objetivo 
Aprender a configurar un servidor de sockets en Python que reciba mensajes de clientes, 
los almacene en una base de datos y envíe confirmaciones, aplicando buenas prácticas de 
modularización y manejo de errores.  
Utilizar los comentarios para explicar tus configuraciones en el servidor. 

### Servidor

Creá un socket que escuche en localhost:5000. 
Usá funciones separadas para: 
- Inicializar el socket. 
- Aceptar conexiones y recibir mensajes. 
- Guardar cada mensaje en una DB SQLite con los campos: id, contenido, fecha_envio, ip_cliente. 
- Manejar errores (puerto ocupado, DB no accesible). 
- Responde al cliente con: "Mensaje recibido: <timestamp>". 

### Cliente: 
- Debe tener la capacidad de  conectarse al servidor y enviar múltiples mensajes hasta que el usuario escriba éxito. 
- Mostrá la respuesta del servidor para cada mensaje. 

### Algunas recomendaciones: 
- Usá el módulo sqlite3 para la base de datos. 
- Comentá cada sección clave (ej: # Configuración del socket TCP/IP). 
- Ejecutá pruebas locales (primero servidor, luego cliente en otra terminal). 
## Demo

![DB Demo](https://raw.githubusercontent.com/JoanaColl/Socket-Chat/refs/heads/main/demo.png)

## Authors

- [@JoanaColl](https://www.github.com/JoanaColl)

