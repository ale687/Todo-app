import json

with open("bonus/preguntas.json", "r") as file:
    contenido = file.read()
    
data = json.loads(contenido)


for preguntas in data:
    print(preguntas["pregunta"])
    for index, respuestas in enumerate(preguntas["respuestas"]):
        print(index + 1, "-", respuestas)
    respuesta_usuario = int(input("Introduzca su respuesta: "))
    preguntas["respuesta_usuario"] = respuesta_usuario
  
        
puntuacion = 0        
for index, preguntas in enumerate(data):
    if preguntas["respuesta_usuario"] == preguntas["respuesta_correcta"]:
        puntuacion = puntuacion + 1
        resultado = "Respuesta correcta"    
    else:
        resultado = "Respuesta incorrecta"
    mensaje = f"""
     {index + 1} {resultado} - Tu respuesta: {preguntas['respuesta_usuario']}  respuesta correcta: {preguntas['respuesta_correcta']}
    """
    print(mensaje)
    

print(puntuacion, "/", len(data))