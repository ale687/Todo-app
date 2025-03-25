contenidos = ["tengo que crear varias listas", "esto es una prueba", "tengo que escribir mas"]
filenames = ["doc.txt", "report.txt", "presentacion.txt"]

for contenido, filename in zip(contenidos, filenames):
    file = open(f"./files/{filename}", "w")
    file.write(contenido)