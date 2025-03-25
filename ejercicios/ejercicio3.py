#filenames = ['doc.txt', 'report.txt', 'presentation.txt']

#for filename in filenames:
 #   file = open(filename, "w")
  #  file.writelines("hello")
   # file.close()
   
filenames = ["a.txt", "b.txt", "c.txt"]

for filename in filenames:
    file = open(filename, "r")
    contenido = file.read()
    print(contenido)
    
  