puntuacion = 0
print("\nBienvenido al quiz de cultura general.")
print("Se le darán 5 preguntas, con 4 opciones de respuesta cada una.")
print("Solo una de ellas es la correcta.")
print("Se sumará 1 punto por cada respuesta correcta a su puntuación total.")
print("¡Buena suerte!")
print("\n1. ¿Quién fue el autor de Don Quijote de la Mancha?")
print("a) Miguel de Cervantes")
print("b) Federico García Lorca")
print("c) Gustavo Adolfo Bécquer")
print("d) William Shakespeare\n")
respuesta_1 = input()
if respuesta_1 == "a" or respuesta_1 == "A":
    print ("\n¡Correcto!")
    puntuacion = puntuacion + 1
    print("Su puntuación actual es de:",puntuacion)
else:
    print("\nIncorrecto. La respuesta correcta era Miguel de Cervantes.")
    print("Su puntuación actual es de:",puntuacion)
print("\n2. ¿En qué año comenzó la Segunda Guerra Mundial?")
print("a) 1930")
print("b) 1945")
print("c) 1939")
print("d) 1936\n")
respuesta_2 = input()
if respuesta_2 == "c" or respuesta_2 == "C":
    print("\n¡Correcto!")
    puntuacion = puntuacion + 1
    print("Su puntuación actual es de:",puntuacion)
else:
    print("\nIncorrecto. La respuesta correcta era 1939.")
    print("Su puntuación actual es de:",puntuacion)
print("\n3. ¿Cuál es la capital de Australia?")
print("a) Sydney")
print("b) Canberra")
print("c) Melbourne")
print("d) Adelaida\n")
respuesta_3 = input()
if respuesta_3 == "b" or respuesta_3 == "B":
    print("\n¡Correcto!")
    puntuacion = puntuacion + 1
    print("Su puntuación actual es de:",puntuacion)
else:
    print("\nIncorrecto. La respuesta correcta era Canberra.")
    print("Su puntuación actual es de:",puntuacion)
print("\n4. ¿Qué país ganó el Mundial de fútbol en 2022?")
print("a) Francia")
print("b) Brasil")
print("c) Argentina")
print("d) España\n")
respuesta_4 = input()
if respuesta_4 == "c" or respuesta_4 == "C":
    print("\n¡Correcto!")
    puntuacion = puntuacion + 1
    print("Su puntuación actual es de:",puntuacion)
else:
    print("\nIncorrecto. La respuesta correcta era Argentina.")
    print("Su puntuación actual es de:",puntuacion)
print("\n5. ¿Qué planeta es el más grande del sistema solar?")
print("a) Saturno")
print("b) La Tierra")
print("c) Marte")
print("d) Júpiter\n")
respuesta_5 = input()
if respuesta_5 == "d" or respuesta_5 == "D":
    print("\n¡Correcto!")
    puntuacion = puntuacion + 1
    print("Su puntuación actual es de:",puntuacion)
else:
    print("\nIncorrecto. La respuesta correcta era Júpiter.")
    print("Su puntuación actual es de:",puntuacion)
print("\nAquí finaliza el quiz.")
if puntuacion == 5:
    print("¡Enhorabuena! Usted ha contestado todas las preguntas correctamente!")
elif puntuacion == 4:
    print("Le falta 1 punto para tener todas las respuestas correctas.")
    print("Mejor suerte la próxima vez.")
else:
    puntuacion_faltante = 5 - puntuacion
    print("Le faltan",puntuacion_faltante,"puntos para tener todas las respuestas correctas.")
    print("Mejor suerte la próxima vez.")