new_member = input("ingrese nuevo mienbro: ")

file = open("members.txt","r")
miembros_existentes = file.readlines()
file.close()

miembros_existentes.append(new_member + "\n")

file = open("members.txt", "w")
miembros_existentes = file.writelines(miembros_existentes)
file.close()


