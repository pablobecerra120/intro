#def matrizprincipal(archivo):
	#leer = open(archivo)
	#lista=[]
	#for linea in leer:
		#l=linea.strip().split("::")
		#lista.append(l[0])
	#leer.close()
	#return lista
#def abs(archivo2):
	#lista=matrizprincipal(archivo)
	#leer2=open(archivo2)
	#for linea in leer2:
	    #l=linea.strip().split("::")
		#if lista[0] == l[1]:

def hacermatriz(archivo1, archivo2):
	peliculas=open(archivo1)
	ratings=open(archivo2)
	lista=[]
	for linea in range(len(archivo1)):
		lista.append([])
	for user in ratings:
		usuario= user.strip.split("::")
		lista[int(usuario[1])].append(int[usuario[2]])
	peliculas.close()
	ratings.close()
	return lista
print hacermatriz("peliculastest.txt", "ratingstest.txt")


