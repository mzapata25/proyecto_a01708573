# Proyecto01

## Quiz de cultura general 

### Contexto
"Se entiende como cultura general al conjunto de conocimientos que una persona posee sobre una gran variedad de temas, ya sean estos adquiridos mediante el estudio reglado, la investigación autodidacta, o la experiencia de los hechos acaecidos a lo largo de su vida.

Desde un punto de vista práctico, más que para la aplicación de dichos conocimientos en un área concreta, la cultura general sirve para contar con un mejor criterio y una mayor amplitud de miras.
Es decir, contar con una cultura general amplia proporciona una perspectiva más amplia del mundo, ya que nos permite entenderlo no sólo desde los parámetros de nuestra propia cultura, sino también entendiendo las motivaciones y razones que llevan a otros a comportarse de un modo distinto.

Si bien la cultura general es acumulativa y nunca deja de construirse, las bases de ésta suelen proporcionarse en la escuela mediante una serie de materias que se consideran imprescindibles para que el individuo pueda desenvolverse posteriormente con normalidad en cualquier ámbito.

Así, las Matemáticas son una parte importante ya que están presentes en acciones de la vida cotidiana como el intercambio de bienes y dinero. Sumar, restar, multiplicar y dividir pueden considerarse acciones básicas de cultura general sin las cuales, un sinfín de actividades resultarían problemáticas.
La Historia y la Geografía también se consideran como pilares de la cultura general, dado que por una parte nos ponen en antecedentes de los hechos acaecidos con anterioridad a nuestra presencia en el mundo, y por otra, nos dan una orientación de la donde se sitúan los diferentes pueblos, países y culturas que habitan la Tierra.
El Lenguaje, por su parte, nos enseña a expresarnos con precisión y de éste modo nos facilita la capacidad de comunicarnos y transmitir ideas.

A partir de aquí, el campo de materias que puede abarcar la cultura general es infinito, ya que el saber no conoce límites. Sin embargo, es importante señalar que el objetivo de poseer una cultura general amplia no es dominar estas materias sino contar con el mayor número de referencias posibles que nos permitan estructuras nuestras propias ideas de forma coherente y apoyadas en argumentos.
El desarrollo de una cultura general amplia nos permite entender mejor nuestro entorno y los acontecimientos que en él suceden, ya que para valorar cada hecho disponemos de un abanico de explicaciones y causas que podemos contrastar y que nos permiten llegar a nuestras propias conclusiones." fuente https://www.definicionabc.com/general/cultura-general.php

Este programa consiste en quiz de preguntas de cultura general. Se ejecuta en la terminal de Python 3. En cada pregunta, se le ofrecerá al usuario una serie de respuesta, de las cuales solo una es la correcta. Cuando el usuario conteste, se le informará si ha acertado o no y se mostrará la puntuación acumulada hasta ese momento. Al final, se le informa de la puntuación total.

### Idea
Tuve esta idea porque siempre me gustó ver concursos de televisión donde salían este tipo de preguntas, y saber contestarlas correctamente. Creo que es un buen pasatiempo, además de que son conocimiento que la gente debería tener, ya que, en mi opinión, saber más del mundo que te rodea hace que lo entiendas mejor. También tuve otras ideas parecidas al principio, como la de hacer un quiz de preguntas sobre algún deporte o competición en concreto, pero creo que esto es mejor, porque funciona con el público en general, y no solo con un grupo específico.
### Estructuras de decisión (avance 4)
Este proyecto ya contiene estructuras de decisión, ya que se han usado en avances anteriores. Dentro de la función verificador_respuesta, se utilizan las estructuras if y elif entre las líneas 21 y 34 para comprobar si la respuesta dada a cada pregunta es la esperada, siendo estas estructuras las cuales determinarán que la variable respuesta sea igual al booleano True de ser así. Luego, se llama a la función verificador_respuesta ya en la parte principal del programa, donde se informa al usuario si ha dado la respuesta correcta (usando la estructura if) y, en caso contrario, se usa la estructura else. Estos usos están presentes en las líneas 59, 68, 79, 84, 94, 99, 109, 114, 124 y 128. Finalmente, se usan las estructuras if, elif y else en las líneas 133, 136 y 139 para dar el resultado final al usuario y las respuestas que le faltan para obtener el 100%, en el caso de acertarlas todas también se informa al usuario de esto.
