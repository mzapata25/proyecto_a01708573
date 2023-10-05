"""
Proyecto Final Python (avance 7)
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
    (uso de condicionales, uso de funciones, uso de ciclo while, listas 
    y listas anidadas)
    recibe: respuesta en lista anidada formada por strings
    compara lista de respuestas con respuesta deseada para cada pregunta
    si la respuesta dada es la esperada
    se suma 1 a la puntuación
    devuelve: lista con puntuación total del usuario 
    y puntuación por categorías
    """
    #La puntuación comienza en 0, se suma un punto por respuesta correcta
    puntuacion_total = 0
    #Cada categoría tiene su propia puntuación
    puntuacion_literatura = 0
    puntuacion_historia = 0
    puntuacion_geografia = 0
    puntuacion_deportes = 0
    puntuacion_ciencias = 0
    #Row se refiere a la fila, cada categoría tiene su propia fila
    row = 0
    #El ciclo se repite hasta agotar todas las filas
    while row <= 4:
        #Col se refiere a la columna, cada fila tiene 3 columnas
        col = 0
        #El ciclo se repite hasta agotar las columnas de una fila
        while col <= 2:
            #Siempre se compara la misma posición en ambas listas
            if(lista_respuestas[row][col] == respuestas_usuario[row][col]):
                #Cada respuesta correcta suma un punto a la puntuación total
                puntuacion_total += 1
                #El condicional es para identificar la fila y su categoría
                if(row == 0):
                    #Se suma también un punto por categoría correspondiente
                    puntuacion_literatura += 1
                elif(row == 1):
                    puntuacion_historia += 1
                elif(row == 2):
                    puntuacion_geografia += 1
                elif(row == 3):
                    puntuacion_deportes += 1
                elif(row == 4):
                    puntuacion_ciencias += 1
            #La columna aumenta en 1 cada vez que se repite el ciclo
            col += 1
        #La fila aumenta en 1 cada vez que se repite el ciclo
        row += 1
    #Se crea lista_puntuaciones con puntuacion_total como su primer valor
    lista_puntuaciones = [puntuacion_total]
    #Con el append se añade a lista_puntuaciones los puntos de cada categoría
    lista_puntuaciones.append(puntuacion_literatura)
    lista_puntuaciones.append(puntuacion_historia)
    lista_puntuaciones.append(puntuacion_geografia)
    lista_puntuaciones.append(puntuacion_deportes)
    lista_puntuaciones.append(puntuacion_ciencias)
    #La función devuelve lista_puntuaciones
    return lista_puntuaciones
"""
========  parte principal del programa =======================================
"""
#Lista anidada que contiene todas las respuestas correctas
lista_respuestas = [["a","b","d"],
                    ["c","d","a"],
                    ["b","c","b"],
                    ["c","a","c"],
                    ["d","a","b"]]
#Lista anidada a la que el usuario irá añadiendo sus respuestas
respuestas_usuario = [["","",""],
                      ["","",""],
                      ["","",""],
                      ["","",""],
                      ["","",""]]
#Introducción para que el usuario entienda el funcionamiento
print("\nBienvenido al quiz de cultura general.")
print("Se le darán 15 preguntas, con 4 opciones de respuesta cada una.")
print("Solo una de ellas es la correcta.")
print("Las preguntas se dividen en 5 categorías: literatura, historia, \
geografía, deportes y ciencias.")
print("Se sumará 1 punto por cada respuesta correcta a su puntuación total.")
print("Después de cada pregunta se le informará de la respuesta correcta \
si la ha fallado. En caso contrario, se le informará de su acierto.")
print("Al final del quiz, se le informará de su puntuación por cada \
categoría y también de su puntuación total.")
print("Solo se admitirá la respuesta como una sola letra en minúscula.")
print("¡Buena suerte!")
print("\n1. ¿Quién fue el autor de Don Quijote de la Mancha?")
print("a) Miguel de Cervantes")
print("b) Federico García Lorca")
print("c) Gustavo Adolfo Bécquer")
print("d) William Shakespeare\n")
#El usuario da su respuesta en forma de input tipo string.
respuesta = input()
#Se añade la respuesta dada por el usuario a la lista anidada
respuestas_usuario[0][0] = respuesta
'''
El condicional evalúa si la respuesta del usuario es la correcta o no y
se le informa correspondientemente.
'''
if(respuesta == "a"):
    print ("\n¡Correcto!")
else:
    print("\nIncorrecto. La respuesta era Miguel de Cervantes.")
print("\n2. ¿Cúal de estos libros escribió Mary Shelley?")
print("a) Drácula")
print("b) Frankestein")
print("c) Harry Potter")
print("d) La Divina Comedia\n")
respuesta = input()
respuestas_usuario[0][1] = respuesta
if(respuesta == "b"):
    print("\n¡Correcto!")
else:
    print("\nIncorrecto. La respuesta era Frankestein.")
print("\n3. Nombre del tercer libro del Señor de los Anillos.")
print("a) Las Dos Torres")
print("b) El Hobbit")
print("c) La Comunidad del Anillo")
print("d) El Regreso del Rey\n")
respuesta = input()
respuestas_usuario[0][2] = respuesta
if(respuesta == "d"):
    print("\n¡Correcto!")
else:
    print("\nIncorrecto. La respuesta era El Regreso del Rey.")
print("\n4. ¿En qué año comenzó la Segunda Guerra Mundial?")
print("a) 1930")
print("b) 1945")
print("c) 1939")
print("d) 1936\n")
respuesta = input()
respuestas_usuario[1][0] = respuesta
if(respuesta == "c"):
    print("\n¡Correcto!")
else:
    print("\nIncorrecto. La respuesta era 1939.")
print("\n5. ¿En qué año declaró EE.UU. su independencia?")
print("a) 1900")
print("b) 1789")
print("c) 1752")
print("d) 1776\n")
respuesta = input()
respuestas_usuario[1][1] = respuesta
if(respuesta == "d"):
    print("\n¡Correcto!")
else:
    print("\nIncorrecto. La respuesta era 1776.")
print("\n6. ¿Qué dos países protagonizaron la Guerra Fría?")
print("a) EE.UU. y la URSS")
print("b) EE.UU. y China")
print("c) EE.UU. y Reino Unido")
print("d) La URSS y China\n")
respuesta = input()
respuestas_usuario[1][2] = respuesta
if(respuesta == "a"):
    print("\n¡Correcto!")
else:
    print("\nIncorrecto. La respuesta era EE.UU y la URSS.")
print("\n7. ¿Cuál es la capital de Australia?")
print("a) Sydney")
print("b) Canberra")
print("c) Melbourne")
print("d) Adelaida\n")
respuesta = input()
respuestas_usuario[2][0] = respuesta
if(respuesta == "b"):
    print("\n¡Correcto!")
else:
    print("\nIncorrecto. La respuesta era Canberra.")
print("\n8. ¿Dónde se encuentra la Sagrada Familia?")
print("a) Madrid")
print("b) Buenos Aires")
print("c) Barcelona")
print("d) Nueva York\n")
respuesta = input()
respuestas_usuario[2][1] = respuesta
if(respuesta == "c"):
    print("\n¡Correcto!")
else:
    print("\nIncorrecto. La respuesta era Barcelona.")
print("\n9. ¿Cuál es el continente más grande del mundo?")
print("a) América")
print("b) Asia")
print("c) Europa")
print("d) África\n")
respuesta = input()
respuestas_usuario[2][2] = respuesta
if(respuesta == "b"):
    print("\n¡Correcto!")
else:
    print("\nIncorrecto. La respuesta era Asia.")
print("\n10. ¿Qué país ganó el Mundial de fútbol en 2022?")
print("a) Francia")
print("b) Brasil")
print("c) Argentina")
print("d) España\n")
respuesta = input()
respuestas_usuario[3][0] = respuesta
if(respuesta == "c"):
    print("\n¡Correcto!")
else:
    print("\nIncorrecto. La respuesta era Argentina.")
print("\n11. ¿Dónde se celebraron las Olimpiadas de 2020?")
print("a) Tokio")
print("b) Atenas")
print("c) Londres")
print("d) París\n")
respuesta = input()
respuestas_usuario[3][1] = respuesta
if(respuesta == "a"):
    print("\n¡Correcto!")
else:
    print("\nIncorrecto. La respuesta era Tokio.")
print("\n12. ¿Cúanto dura un cuarto en baloncesto?")
print("a) 5 minutos")
print("b) 15 minutos")
print("c) 10 minutos")
print("d) 40 minutos\n")
respuesta = input()
respuestas_usuario[3][2] = respuesta
if(respuesta == "c"):
    print("\n¡Correcto!")
else:
    print("\nIncorrecto. La respuesta era 10 minutos.")
print("\n13. ¿Qué planeta es el más grande del sistema solar?")
print("a) Saturno")
print("b) La Tierra")
print("c) Marte")
print("d) Júpiter\n")
respuesta = input()
respuestas_usuario[4][0] = respuesta
if(respuesta == "d"):
    print("\n¡Correcto!")
else:
    print("\nIncorrecto. La respuesta era Júpiter.")
print("\n14. ¿Cuántos elementos tiene la tabla periódica?")
print("a) 118")
print("b) 120")
print("c) 200")
print("d) 4\n")
respuesta = input()
respuestas_usuario[4][1] = respuesta
if(respuesta == "a"):
    print("\n¡Correcto!")
else:
    print("\nIncorrecto. La respuesta era 118.")
print("\n15. ¿Cuántos dientes tiene una persona adulta?")
print("a) 25")
print("b) 32")
print("c) 20")
print("d) 36\n")
respuesta = input()
respuestas_usuario[4][2] = respuesta
if(respuesta == "b"):
    print("\n¡Correcto!")
else:
    print("\nIncorrecto. La respuesta era 32.")
#La lista contiene la puntuación total y la puntuación por categorías
lista_puntuaciones = contador_puntuacion(respuestas_usuario)
#Dependiendo de la puntuación final, se le comunica al usuario su rendimiento
print("\nEstas son sus puntuaciones por categorías:")
print("\nLiteratura:",lista_puntuaciones[1],"de 3.")
print("Historia:",lista_puntuaciones[2],"de 3.")
print("Geografía:",lista_puntuaciones[3],"de 3.")
print("Deportes:",lista_puntuaciones[4],"de 3.")
print("Ciencias:",lista_puntuaciones[5],"de 3.")
puntuacion_final = lista_puntuaciones[0]
if(puntuacion_final == 15):
    print("\n¡Enhorabuena!")
    print("¡Usted ha contestado todas las preguntas correctamente!")
    print("Puntuación final:",puntuacion_final,"aciertos.")
elif(puntuacion_final == 14):
    print("\nLe falta 1 punto para tener el 100%.")
    print("Mejor suerte la próxima vez.")
    print("Puntuación final:",puntuacion_final,"aciertos.")
else:
    puntuacion_faltante = 15 - puntuacion_final
    print("\nLe faltan",puntuacion_faltante,"puntos para tener el 100%.")
    print("Mejor suerte la próxima vez.")
    print("Puntuación final:",puntuacion_final,"aciertos.")
