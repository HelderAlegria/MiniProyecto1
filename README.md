# MiniProyecto1

FUNCIONAMIENTO DEL PROGRAMA DRAG & DROP
¿Qué hace el programa?
Este programa usa la cámara para detectar las manos y permite mover un cuadro azul en la pantalla solo con juntar el pulgar y el dedo índice, como si se estuviera agarrando el objeto virtual.

¿Cómo funciona paso a paso?
Activa la cámara para capturar el video en tiempo real.
Detecta las manos utilizando la herramienta MediaPipe.
Busca los puntos clave del pulgar y la punta del dedo indicé para agarrar y soltar.
Calcula la distancia entre los dedos.
Si los dedos están muy cerca, menos de 40 píxeles, el programa entiende que se está agarrando el objeto y se puede mover con gusto.
Si los dedos se separan, el programa entiende que lo estás soltando y el cuadrado se queda donde se dejó.

¿Qué librerías se utilizan?
OpenCV: Para mostrar el video y dibujar el cuadrado.
MediaPipe: Para detectar las manos y saber dónde están los dedos.
Numpy: Para hacer cálculos, en este caso para verificar la distancia entre los dedos.
