# FaceMaskRecognition
Using a CNN (Convolutional Neural Network) trained to classify images, we process video in real time on a raspberry. Frame by frame we evaluate if a face by frame has been detected. IN case of being detected, we will proceed to classify it as: • With mask • Without mask
1. Problema propuesto a resolver.
Elaborar una aplicación que implemente el concepto y visón del internet de las cosas (IoT).

2. Características importantes a considerar, como por ejemplo en qué condiciones mejora el tiempo del concurrente al secuencial o viceversa.
- Implementar tres capaz de aplicación, 
    1. Aplicación sistema embebido, 
    2. Aplicación sistema servidor y 
    3. Aplicación dispositivo móvil, ésta última no necesariamente tiene que ser una aplicación para smartphone o dispositivo móvil, incluso puede ser un servicio web.
- Por ningún motivo el sistema embebido debe de implementar funciones de la aplicación servidor.
- La comunicación debe de realizarse única y exclusivamente de la aplicación cliente a la aplicación servidor, y de la aplicación servidor a la aplicación del sistema embebido, y al contrario, por ningún motivo la aplicación del dispositivo móvil debe de establecer comunicación con el sistema embebido.

 
3. Algoritmo propuesto e implementación del proceso.
 
 Utilizando una CNN (Convolutional Neural Network) entrenada para clasificar imágenes, procesamos en una raspberry, video en tiempo real. Frame por frame evaluamos si se ha detectado un rostro a cuadro. EN caso de ser detectado, procederemos a clasificarlo como:
•	Con cubrebocas
•	Sin cubrebocas 
Según el resultado de esta validación, realizamos una solicitud a nuestro web server. En caso de que la validación haya apuntado a que el usuario si tiene cubre bocas, el web service generara una cadena de caracteres aleatoria de 13 espacios y será lo que regresara a nuestra raspberry. En caso de indicar lo contrario, el web service regresara un mensaje negativo avisando que no se encontró un usuario con cubrebocas. Una vez que ya tenemos esta cadena de caracteres, la convertimos en un código QR con la intención de ser leído y valide un acceso con contraseña. Este código QR es enviado via telegram haciendo uso de un bot de la misma plataforma. Este bot es manipulado vía comandos de Python, y esta habilitado para enviar texto plano e imágenes. En un caso negativo, se le hace llegar al usuario un mensaje en el que se le notifica que no se le permite el acceso dado a que se detecto que no esta usando cubrebocas.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. Problem proposed to solve.
Develop an application that implements the concept and vision of the Internet of Things (IoT).

2. Important characteristics to consider, such as under what conditions the concurrent time improves to the sequential one or vice versa.
- Implement three capable of application,
    1. Embedded system application,
    2. Application system server and
    3. Mobile device application, the latter does not necessarily have to be an application for a smartphone or mobile device, it can even be a web service.
- For no reason the embedded system must implement functions of the server application.
- Communication must be carried out solely and exclusively from the client application to the server application, and from the server application to the application of the embedded system, and on the contrary, for no reason should the application of the mobile device establish communication with the embedded system .


3. Proposed algorithm and implementation of the process.
 
 Using a CNN (Convolutional Neural Network) trained to classify images, we process video in real time on a raspberry. Frame by frame we evaluate if a face by frame has been detected. IN case of being detected, we will proceed to classify it as:
• With mask
• Without mask
According to the result of this validation, we make a request to our web server. In case the validation has pointed out that the user does have mouth covers, the web service will generate a random string of 13 spaces and it will be what it will return to our raspberry. In case of indicating otherwise, the web service will return a negative message advising that a user with a mask was not found. Once we have this string of characters, we convert it into a QR code with the intention of being read and validate an access with a password. This QR code is sent via telegram using a bot from the same platform. This bot is manipulated via Python commands, and is enabled to send plain text and images. In a negative case, the user is sent a message in which they are notified that they are not allowed access since it was detected that they are not wearing a mask.