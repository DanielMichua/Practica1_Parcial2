import random
from networkx.utils.decorators import nodes_or_number
import numpy as np
from numpy.core.numeric import array_equiv
import matplotlib.pyplot as plt
import networkx as nx

#definimos como random las velocidades de los caballos
c1 = random.uniform(1,100)
c2 = random.uniform(1, 100)
c3 = random.uniform(1, 100)
c4 = random.uniform(1, 100)
c5 = random.uniform(1, 100)
c6 = random.uniform(1, 100)
c7 = random.uniform(1, 100)
c8 = random.uniform(1, 100)
c9 = random.uniform(1, 100)
c10 = random.uniform(1, 100)
c11 = random.uniform(1, 100)
c12 = random.uniform(1, 100)
c13 = random.uniform(1, 100)
c14 = random.uniform(1, 100)
c15 = random.uniform(1, 100)
c16 = random.uniform(1, 100)
c17 = random.uniform(1, 100)
c18 = random.uniform(1, 100)
c19 = random.uniform(1, 100)
c20 = random.uniform(1, 100)
c21 = random.uniform(1, 100)
c22 = random.uniform(1, 100)
c23 = random.uniform(1, 100)
c24 = random.uniform(1, 100)
c25 = random.uniform(1, 100)

print("Aqui se muestran sus velocidades:\n")
print("\t Caballo 1:",c1,"\n","\t Caballo 2:",c2,"\n","\t Caballo 3:",c3,"\n","\t Caballo 4:",c4,"\n","\t Caballo 5:",c5,"\n","\t Caballo 6:",c6,"\n","\t Caballo 7:",c7,"\n","\t Caballo 8:",c8,"\n","\t Caballo 9:",c9,"\n","\t Caballo 10:",c10,"\n","\t Caballo 11:",c11,"\n","\t Caballo 12:",c12,"\n","\t Caballo 13:",c13,"\n","\t Caballo 14:",c14,"\n","\t Caballo 15:",c15,"\n","\t Caballo 16:",c16,"\n","\t Caballo 17:",c17,"\n","\t Caballo 18:",c18,"\n","\t Caballo 19:",c19,"\n","\t Caballo 20:",c20,"\n","\t Caballo 21:",c21,"\n","\t Caballo 22:",c22,"\n","\t Caballo 23:",c23,"\n","\t Caballo 24:",c24,"\n","\t Caballo 25:",c25,"\n")
#Guarda las velocidades de los caballos en arreglos de 5, para la primera carrera
CT = np.array([[c1,c2,c3,c4,c5],[c6,c7,c8,c9,c10],[c11,c12,c13,c14,c15],[c16,c17,c18,c19,c20],[c21,c22,c23,c24,c25]])
print("\t Las velocidades de los caballos dentro del arreglo quedan asi: \n",CT,"\n")
#ahora ordenamos las velocidades del mas lento al mas rapido
CT.sort()
print("\t Los primeros 5 campeones quedarian asi:\n",CT)
#ahora, los campeones de campeones compiten
#Declaramos las velocidades dentro de un arreglo, nuevamente para poder comparar entre el campeon de campeones
velocidades = np.array([[c1,c2,c3,c4,c5,], [c6,c7,c8,c9,c10], [c11,c12,c13,c14,c15], [c16,c17,c18,c19,c20], [c21,c22,c23,c24,c25]])
ca6 = [velocidades[0,0], velocidades[1,0], velocidades[2,0], velocidades[3,0], velocidades[4,0]]
#los corremos a los 5 campeones de campeones
ca6.sort()
print("\n\t Carrera 6: \n",ca6)


for x in range(5):#para comparar a los 5 mas rapidos hacemos lo siguiente, uno para la posicion en X y otra en Y
    for y in range(5):
        if ca6[0] == CT[x][y]:
            ganador = (x*5) + (y*1) + 1
            i = x
        #i va a almacenar la fila en donde esta el caballo ganador
print("\n*************El caballo más rápido de todos es***************\n")
print("\t\t\t ",str(ganador))
print("\n*************************************************************\n")

#una vez tenemos al caballo mas rapido de todos, buscamos al segundo mas rapido, y lo hacemos sorteanndo entre los 5 mas rapidos del top, entre el grupo a y c, sin contar al mas rapido de todos
ca7= [velocidades[i,1], ca6[1], ca6[2], ca6[3], ca6[4] ]
ca7.sort()
print("\n\t Carrera 7: \n",ca7)
for x in range(5):
    for y in range(5):
        if ca7[0] == CT[x][y]:
            ganador2 = (x*5) + (y*1) +1

        
print("\n*************El segundo caballo más rápido de todos es***************\n")
print("\t\t\t ",str(ganador2))
print("\n*********************************************************************\n")
print("El minimo de carreras para encontrar a los 2 mas rapidos son: 7")
#Para hacer los grafos hacemos lo siguiente
Gr = nx.Graph() # Creamos el grafo con la funcion Graph

Gr.add_node("Ganador")
Gr.add_node("Ganador 2")


Gr.add_node("sub1")
Gr.add_node("sub2")
Gr.add_node("sub3")
Gr.add_node("sub4")
Gr.add_node("sub5")

Gr.add_nodes_from(["sub1.1", "sub1.2", "sub1.3"])
Gr.add_nodes_from(["sub2.1", "sub2.2", "sub2.3"])
Gr.add_nodes_from(["sub3.1", "sub3.2", "sub3.3", "sub3.4"])
Gr.add_nodes_from(["sub4.1", "sub4.2", "sub4.3", "sub4.4"])
Gr.add_nodes_from(["sub5.1", "sub5.2", "sub5.3", "sub5.4"])

#Añadimos a nuestras variables como aristas
Gr.add_edge("Ganador", "Ganador 2")

Gr.add_edge("Ganador 2", "sub1")
Gr.add_edge("Ganador 2", "sub2")
Gr.add_edge("Ganador 2", "sub3")
Gr.add_edge("Ganador 2", "sub4")
Gr.add_edge("Ganador 2", "sub5")

Gr.add_edges_from([("sub1", "sub1.1"),("sub1", "sub1.2"), ("sub1", "sub1.3")])
Gr.add_edges_from([("sub2", "sub2.1"),("sub2", "sub2.2"), ("sub2", "sub2.3")])
Gr.add_edges_from([("sub3", "sub3.1"),("sub3", "sub3.2"), ("sub3", "sub3.3"), ("sub3", "sub3.4")])
Gr.add_edges_from([("sub4", "sub4.1"),("sub4", "sub4.2"), ("sub4", "sub4.3"), ("sub4", "sub4.4")])
Gr.add_edges_from([("sub5", "sub5.1"),("sub5", "sub5.2"), ("sub5", "sub5.3"), ("sub5", "sub5.4")])

#graficar 
nx.draw(Gr, node_size = 50, width = 0.3, with_labels=False)
plt.show() #Muestra el grafo