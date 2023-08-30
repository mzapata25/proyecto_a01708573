"""
Proyecto Final Python (avance 3)
Quiz de cultura general.
El programa realiza una serie de preguntas
y compara las respuesta con las del usuario para evaluarlo.
Al final le da un marcador al usuario y muestra sus errores.
"""
"""
================== función verificadora  =====================================
"""
def verificador_respuesta (respuesta):
    """
    (uso de condicionales, uso de funciones)
    recibe: respuesta variable en string
    compara variable con respuesta deseada para cada pregunta
    si la respuesta dada es la esperada
    se determina como el booleano True
    devuelve: booleano True si la respuesta es correcta
    si no, devuelve el input del usuario
    """
    if(var == 1):
        if(respuesta == "a"):
            respuesta = True
    elif(var == 2):
        if(respuesta == "c"):
            respuesta = True
    elif(var == 3):
        if(respuesta == "b"):
            respuesta = True
    elif(var == 4):
        if(respuesta == "c"):
            respuesta = True
    elif(var == 5):
        if(respuesta == "d"):
            respuesta = True
    return respuesta
"""
========  parte principal del programa =======================================
"""
#La variable var es la que comunica a la función cuál pregunta se responde
var = 1
#La puntuación comienza en 0, se suma un punto por respuesta correcta
puntuacion = 0
#Introducción para que el usuario entienda el funcionamiento
print("\nBienvenido al quiz de cultura general.")
print("Se le darán 5 preguntas, con 4 opciones de respuesta cada una.")
print("Solo una de ellas es la correcta.")
print("Se sumará 1 punto por cada respuesta correcta a su puntuación total.")
print("Solo se admitirá la respuesta como una sola letra en minúscula.")
print("¡Buena suerte!")
print("\n1. ¿Quién fue el autor de Don Quijote de la Mancha?")
print("a) Miguel de Cervantes")
print("b) Federico García Lorca")
print("c) Gustavo Adolfo Bécquer")
print("d) William Shakespeare\n")
#El usuario de su respuesta en forma de input tipo string.
respuesta = input()
#Se llama a la función verificadora para comprobar si la respuesta es correcta
if(verificador_respuesta(respuesta) == True):
    #Se le comunica al usuario que acertó
    print ("\n¡Correcto!")
    #Se suma un punto al total del usuario, que acertó la respuesta
    puntuacion = puntuacion + 1
    #Se suma 1 a var, para que la función verifique la siguiente respuesta
    var = var + 1
    #Se le comunica al usuario su puntuación hasta ese momento
    print("Su puntuación actual es de:",puntuacion)
else:
    #Se le comunica al usuario la respuesta que era la correcta
    print("\nIncorrecto. La respuesta correcta era Miguel de Cervantes.")
    var = var + 1
    print("Su puntuación actual es de:",puntuacion)
print("\n2. ¿En qué año comenzó la Segunda Guerra Mundial?")
print("a) 1930")
print("b) 1945")
print("c) 1939")
print("d) 1936\n")
respuesta = input()
if(verificador_respuesta(respuesta) == True):
    print("\n¡Correcto!")
    puntuacion = puntuacion + 1
    var = var + 1
    print("Su puntuación actual es de:",puntuacion)
else:
    print("\nIncorrecto. La respuesta correcta era 1939.")
    var = var + 1
    print("Su puntuación actual es de:",puntuacion)
print("\n3. ¿Cuál es la capital de Australia?")
print("a) Sydney")
print("b) Canberra")
print("c) Melbourne")
print("d) Adelaida\n")
respuesta = input()
if(verificador_respuesta(respuesta) == True):
    print("\n¡Correcto!")
    puntuacion = puntuacion + 1
    var = var + 1
    print("Su puntuación actual es de:",puntuacion)
else:
    print("\nIncorrecto. La respuesta correcta era Canberra.")
    var = var + 1
    print("Su puntuación actual es de:",puntuacion)
print("\n4. ¿Qué país ganó el Mundial de fútbol en 2022?")
print("a) Francia")
print("b) Brasil")
print("c) Argentina")
print("d) España\n")
respuesta = input()
if(verificador_respuesta(respuesta) == True):
    print("\n¡Correcto!")
    puntuacion = puntuacion + 1
    var = var + 1
    print("Su puntuación actual es de:",puntuacion)
else:
    print("\nIncorrecto. La respuesta correcta era Argentina.")
    var = var + 1
    print("Su puntuación actual es de:",puntuacion)
print("\n5. ¿Qué planeta es el más grande del sistema solar?")
print("a) Saturno")
print("b) La Tierra")
print("c) Marte")
print("d) Júpiter\n")
respuesta = input()
if(verificador_respuesta(respuesta) == True):
    print("\n¡Correcto!")
    puntuacion = puntuacion + 1
    print("Su puntuación actual es de:",puntuacion)
else:
    print("\nIncorrecto. La respuesta correcta era Júpiter.")
    print("Su puntuación actual es de:",puntuacion)
print("\nAquí finaliza el quiz.")
#Dependiendo de la puntuación final, se le comunica al usuario su rendimiento
if puntuacion == 5:
    print("¡Enhorabuena!")
    print("¡Usted ha contestado todas las preguntas correctamente!")
elif puntuacion == 4:
    print("Le falta 1 punto para tener el 100%.")
    print("Mejor suerte la próxima vez.")
else:
    puntuacion_faltante = 5 - puntuacion
    print("Le faltan",puntuacion_faltante,"puntos para tener el 100%.")
    print("Mejor suerte la próxima vez.")
