"""
Proyecto Final Python (entrega final)
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
    puntuacion_total = 0
    puntuacion_literatura = 0
    puntuacion_historia = 0
    puntuacion_geografia = 0
    puntuacion_deportes = 0
    puntuacion_ciencias = 0
    row = 0
    while(row <= 4):
        col = 0
        while(col <= 2):
            if(lista_respuestas[row][col] == respuestas_usuario[row][col]):
                puntuacion_total += 1
                if(row == 0):
                    puntuacion_literatura += 1
                elif(row == 1):
                    puntuacion_historia += 1
                elif(row == 2):
                    puntuacion_geografia += 1
                elif(row == 3):
                    puntuacion_deportes += 1
                elif(row == 4):
                    puntuacion_ciencias += 1
            col += 1
        row += 1
    lista_puntuaciones = [puntuacion_total]
    lista_puntuaciones.append(puntuacion_literatura)
    lista_puntuaciones.append(puntuacion_historia)
    lista_puntuaciones.append(puntuacion_geografia)
    lista_puntuaciones.append(puntuacion_deportes)
    lista_puntuaciones.append(puntuacion_ciencias)
    return lista_puntuaciones
"""
================== función verificadora  =====================================
"""
def verificador(respuesta, lista_respuestas, lista_correcciones, row, col):
    """
    (uso de condicionales, uso de funciones y listas anidadas)
    recibe: respuesta en string, lista anidada con las respuestas correctas,
    lista anidada con las correciones que recibirá el usuario, fila y columna
    en forma de número entero
    compara respuesta individual dada por el usuario con la lista para
    verificar si es correcta, utilizando los índices de fila y columna
    correspondientes
    devuelve: "¡Correcto!" al usuario si la respuesta es la esperada
    si no, le dice que es incorrecta y le informa de cuál era la esperada
    """
    if(respuesta == lista_respuestas[row][col]):
        print("\n¡Correcto!")
    else:
        print("\nIncorrecto. La respuesta era",lista_correcciones[row][col])
"""
================== función para imprimir preguntas  ==========================
"""
def imprime_preguntas(lista_preguntas, cont):
    """
    (uso de funciones y listas)
    recibe: lista que contiene las preguntas y opciones que se le desplegarán
    al usuario en consola y contador en forma de número entero
    devuelve: en orden, cada pregunta y sus cuatro opciones, dependiendo del
    índice en la lista determinado por el contador
    """
    print(lista_preguntas[cont])
"""
========  parte principal del programa =======================================
"""
lista_respuestas = [["a","b","d"],
                    ["c","d","a"],
                    ["b","c","b"],
                    ["c","a","c"],
                    ["d","a","b"]]
respuestas_usuario = [["","",""],
                      ["","",""],
                      ["","",""],
                      ["","",""],
                      ["","",""]]
lista_correcciones = [["Miguel de Cervantes","Frankestein","El Hobbit"],
                     ["1939","1776","EE.UU. y la URSS"],
                     ["Canberra","Barcelona","Asia"],
                     ["Argentina","Tokio","10 minutos"],
                     ["Júpiter","118","32"]]
lista_preguntas = ["\n1. ¿Quién fue el autor de Don Quijote de la Mancha?\n\
a) Miguel de Cervantes\nb) Federico García Lorca\nc) Gustavo Adolfo Bécquer\n\
d) William Shakespeare\n","\n2. ¿Cúal de estos libros escribió\
 Mary Shelley?\na) Drácula\nb) Frankestein\nc) Harry Potter\n\
d) La Divina Comedia\n","\n3. ¿Cuál de estos NO forma parte de la trilogía\
 del Señor de los Anillos?\na) Las Dos Torres\nb) El Regreso del Rey\
 \nc) La Comunidad del Anillo\nd) El Hobbit\n","\n4. ¿En qué año comenzó la\
 Segunda Guerra Mundial?\na) 1930\nb) 1945\nc) 1939\nd) 1936\n","\n5. ¿En qué\
 año declaró EE.UU. su independencia?\na) 1900\nb) 1789\nc) 1752\nd) 1776\n",
"\n6. ¿Qué dos países protagonizaron la Guerra Fría?\na) EE.UU. y la URSS\
\nb) EE.UU. y China\nc) EE.UU. y Reino Unido\nd) La URSS y China\n",
"\n7. ¿Cuál es la capital de Australia?\na) Sydney\nb) Canberra\n\
c) Melbourne\nd) Adelaida\n","\n8. ¿Dónde se encuentra la Sagrada Familia?\
\na) Madrid\nb) Buenos Aires\nc) Barcelona\nd) Nueva York\n","\n9. ¿Cuál es\
 el continente más grande del mundo?\na) América\nb) Asia\nc) Europa\n\
d) África\n","\n10. ¿Qué país ganó el Mundial de fútbol en 2022?\na) Francia\
\nb) Brasil\nc) Argentina\nd) España\n","\n11. ¿Dónde se celebraron las\
 Olimpiadas de 2020?\na) Tokio\nb) Atenas\nc) Londres\nd) París\n",
"\n12. ¿Cúanto dura un cuarto en baloncesto?\na) 5 minutos\nb) 15 minutos\
\nc) 10 minutos\nd) 40 minutos\n","\n13. ¿Qué planeta es el más grande\
 del sistema solar?\na) Saturno\nb) La Tierra\nc) Marte\nd) Júpiter\n",
"\n14. ¿Cuántos elementos tiene la tabla periódica?\na) 118\nb) 120\nc) 200\
\nd) 4\n","\n15. ¿Cuántos dientes tiene una persona adulta?\na) 25\nb) 32\
\nc) 20\nd) 36\n"]
cont = 0
row = 0
col = 0
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
imprime_preguntas(lista_preguntas, cont)
cont += 1
respuesta = input()
respuestas_usuario[0][0] = respuesta
verificador(respuesta, lista_respuestas, lista_correcciones, row, col)
imprime_preguntas(lista_preguntas, cont)
cont += 1
respuesta = input()
respuestas_usuario[0][1] = respuesta
col = 1
verificador(respuesta, lista_respuestas, lista_correcciones, row, col)
imprime_preguntas(lista_preguntas, cont)
cont += 1
respuesta = input()
respuestas_usuario[0][2] = respuesta
col = 2
verificador(respuesta, lista_respuestas, lista_correcciones, row, col)
imprime_preguntas(lista_preguntas, cont)
cont += 1
respuesta = input()
respuestas_usuario[1][0] = respuesta
row = 1
col = 0
verificador(respuesta, lista_respuestas, lista_correcciones, row, col)
imprime_preguntas(lista_preguntas, cont)
cont += 1
respuesta = input()
respuestas_usuario[1][1] = respuesta
col = 1
verificador(respuesta, lista_respuestas, lista_correcciones, row, col)
imprime_preguntas(lista_preguntas, cont)
cont += 1
respuesta = input()
respuestas_usuario[1][2] = respuesta
col = 2
verificador(respuesta, lista_respuestas, lista_correcciones, row, col)
imprime_preguntas(lista_preguntas, cont)
cont += 1
respuesta = input()
respuestas_usuario[2][0] = respuesta
row = 2
col = 0
verificador(respuesta, lista_respuestas, lista_correcciones, row, col)
imprime_preguntas(lista_preguntas, cont)
cont += 1
respuesta = input()
respuestas_usuario[2][1] = respuesta
col = 1
verificador(respuesta, lista_respuestas, lista_correcciones, row, col)
imprime_preguntas(lista_preguntas, cont)
cont += 1
respuesta = input()
respuestas_usuario[2][2] = respuesta
col = 2
verificador(respuesta, lista_respuestas, lista_correcciones, row, col)
imprime_preguntas(lista_preguntas, cont)
cont += 1
respuesta = input()
respuestas_usuario[3][0] = respuesta
row = 3
col = 0
verificador(respuesta, lista_respuestas, lista_correcciones, row, col)
imprime_preguntas(lista_preguntas, cont)
cont += 1
respuesta = input()
respuestas_usuario[3][1] = respuesta
col = 1
verificador(respuesta, lista_respuestas, lista_correcciones, row, col)
imprime_preguntas(lista_preguntas, cont)
cont += 1
respuesta = input()
respuestas_usuario[3][2] = respuesta
col = 2
verificador(respuesta, lista_respuestas, lista_correcciones, row, col)
imprime_preguntas(lista_preguntas, cont)
cont += 1
respuesta = input()
respuestas_usuario[4][0] = respuesta
row = 4
col = 0
verificador(respuesta, lista_respuestas, lista_correcciones, row, col)
imprime_preguntas(lista_preguntas, cont)
cont += 1
respuesta = input()
respuestas_usuario[4][1] = respuesta
col = 1
verificador(respuesta, lista_respuestas, lista_correcciones, row, col)
imprime_preguntas(lista_preguntas, cont)
cont += 1
respuesta = input()
respuestas_usuario[4][2] = respuesta
col = 2
verificador(respuesta, lista_respuestas, lista_correcciones, row, col)
lista_puntuaciones = contador_puntuacion(respuestas_usuario)
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
