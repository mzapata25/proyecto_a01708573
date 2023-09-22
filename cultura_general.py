"""
Proyecto Final Python (avance 5)
Quiz de cultura general.
El programa realiza una serie de preguntas
y compara las respuesta con las del usuario para evaluarlo.
Al final le da un marcador al usuario.
"""
"""
================== función contadora  ========================================
"""
def contador_puntuacion (respuestas_usuario):
    """
    (uso de condicionales, uso de funciones, uso de ciclo while y listas)
    recibe: respuesta en lista formada por strings
    compara lista de respuestas con respuesta deseada para cada pregunta
    si la respuesta dada es la esperada
    se suma 1 a la puntuación
    devuelve: puntuación total del usuario
    """
    #La puntuación comienza en 0, se suma un punto por respuesta correcta
    puntuacion = 0
    #El contador hace que el ciclo se realice el número de respuestas dadas
    cont = 1   
    while cont <= 5:
        #Siempre se compara la misma posición en ambas listas
        if(lista_respuestas[0] == respuestas_usuario[0]):
            #Cada respuesta correcta suma un punto a la puntuación del usuario
            puntuacion += 1
        #Se borra cada ítem de cada lista, para evitar la repetición
        del lista_respuestas[0]
        del respuestas_usuario [0]
        #El contador aumenta en 1 cada vez que se repite el ciclo
        cont += 1
    return puntuacion
"""
========  parte principal del programa =======================================
"""
#Lista que contiene todas las respuestas correctas
lista_respuestas = ["Miguel de Cervantes","1939","Canberra","Argentina",\
"Júpiter"]
#Lista a la que el usuario irá añadiendo sus respuestas
respuestas_usuario = []
#Introducción para que el usuario entienda el funcionamiento
print("\nBienvenido al quiz de cultura general.")
print("Se le darán 5 preguntas, con 4 opciones de respuesta cada una.")
print("Solo una de ellas es la correcta.")
print("Se sumará 1 punto por cada respuesta correcta a su puntuación total.")
print("Se tiene que dar la respuesta tal y como está escrita en el programa.")
print("¡Buena suerte!")
print("\n1. ¿Quién fue el autor de Don Quijote de la Mancha?")
print("a) Miguel de Cervantes")
print("b) Federico García Lorca")
print("c) Gustavo Adolfo Bécquer")
print("d) William Shakespeare\n")
#El usuario da su respuesta en forma de input tipo string.
respuesta = input()
#Se añade la respuesta dada por el usuario a la lista
respuestas_usuario.append(respuesta)
print("\n2. ¿En qué año comenzó la Segunda Guerra Mundial?")
print("a) 1930")
print("b) 1945")
print("c) 1939")
print("d) 1936\n")
respuesta = input()
respuestas_usuario.append(respuesta)
print("\n3. ¿Cuál es la capital de Australia?")
print("a) Sydney")
print("b) Canberra")
print("c) Melbourne")
print("d) Adelaida\n")
respuesta = input()
respuestas_usuario.append(respuesta)
print("\n4. ¿Qué país ganó el Mundial de fútbol en 2022?")
print("a) Francia")
print("b) Brasil")
print("c) Argentina")
print("d) España\n")
respuesta = input()
respuestas_usuario.append(respuesta)
print("\n5. ¿Qué planeta es el más grande del sistema solar?")
print("a) Saturno")
print("b) La Tierra")
print("c) Marte")
print("d) Júpiter\n")
respuesta = input()
respuestas_usuario.append(respuesta)
#Dependiendo de la puntuación final, se le comunica al usuario su rendimiento
puntuacion_final = contador_puntuacion(respuestas_usuario)
if(puntuacion_final == 5):
    print("¡Enhorabuena!")
    print("¡Usted ha contestado todas las preguntas correctamente!")
elif(puntuacion_final == 4):
    print("Le falta 1 punto para tener el 100%.")
    print("Mejor suerte la próxima vez.")
else:
    puntuacion_faltante = 5 - puntuacion_final
    print("Le faltan",puntuacion_faltante,"puntos para tener el 100%.")
    print("Mejor suerte la próxima vez.")
