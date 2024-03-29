from matrices import *
import unittest

#probabilidad([(-3,-1),(0,-2),(0,1),(2,0)],2)
def probabilidad(vector,pos):
    return float("%.6f" % (Norma([[vector[pos]]])**2/Norma([vector])**2))


#Matriz Compleja --> ket
#normKet([[(-3,-1)],[(0,2)],[(0,1)],[(2,0)]])
def normKet(ket):
    normalizada=complejoPorMatriz((1/Norma(ket),0),ket)
    return bonitaCompleja(normalizada)


#Matriz Compleja --> ket    
#Bra([[(-3,-1)],[(0,2)],[(0,1)],[(2,0)]])
def Bra(ket):
    ket=conjugada(ket)
    return transpuestaVector(ket[0]);
    

#Matriz Compleja --> ket1
#Matriz Compleja --> ket2
"""
ket1=[[((2**0.5/2),0),(0,(2**0.5/2))]]
ket2=[[(0,(2**0.5/2)),(-(2**0.5/2),0)]]
amplitudTransicion(ket1,ket2)
"""
def amplitudTransicion(ket1,ket2):    
    rta=multiplicacionDeMatricesComplejas(ket1,Bra(ket2))
    a=0
    b=0
    for i in range(len(rta)):
        a+=float("%.4f" % (rta[0][0][0]))
        b+=float("%.4f" % (rta[0][0][1])) 
    return (a,b)

#Matriz Compleja --> observable
#Matriz Compleja --> ket
"""
observable=[[(1,0),(0,-1)],[(0,1),(2,0)]]
ket=[[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]
valorMedio (observable,ket)
"""
def valorMedio (observable,ket):
    if(Hermitian(observable)==False ):
        return "el observable debe ser una matriz herminitana"
    p= multiplicacionDeMatricesComplejas(adjunta(observable),ket)
    x=(0,0)
    p=conjugada(p)
    for i in range(len(p)):
        for j in range(len(p[0])):
            x=sumas(x,producto(p[i][j],ket[i][j]))        
    return x

#Matriz Compleja --> observable
#Matriz Compleja --> ket
"""
observable=[[(1,0),(0,-1)],[(0,1),(2,0)]]
ket=[[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]
Varianza(observable ,ket)
"""
def Varianza(observable ,ket):
    if(Hermitian(observable)==False ):
        return "el observable debe ser una matriz herminitana"
    observable= adjunta(observable)
    valor= valorMedio(observable,ket)
    MI = [[ valor if j == i else (0,0) for j in range(len(observable))] for i in range(len(observable[0]))]
    res= restaMatrices(observable,MI)
    res2=multiplicacionDeMatricesComplejas(res,res)
    ket=adjunta(ket)
    r1= multiplicacionDeMatricesComplejas(ket,res2)
    x=(0,0)
    
    for i in range(len(r1)):
        for j in range(len(r1[0])):
            x=sumas(x,producto(r1[i][j],ket[i][j]))        
    return x
#entero --> tiempos
#Matriz Compleja --> ket
#lista de Matrizes --> arreglo
"""
ket=[[(1,0)],[(0,0)]]
m1=[[(0,0),(1,0)],[(1,0),(0,0)]]
m2=[[(2**0.5/2,0),(2**0.5/2,0)],[(2**0.5/2,0),(2**0.5/2,0)]]
arreglo=[[[(0,0),(1,0)],[(1,0),(0,0)]],[[(2**0.5/2,0),(2**0.5/2,0)],[(2**0.5/2,0),(2**0.5/2,0)]]]
DinamicaDelSistema(2, ket,arreglo)
"""
def DinamicaDelSistema(tiempos, ket,arreglo):
    fin=ket
    for i in range(tiempos):
        fin=multiplicacionDeMatricesComplejas(arreglo[i],fin)
    return fin

class TestUM(unittest.TestCase):
    #probabilidad
    def test_caso_probabilidad_1(self):
        self.assertEqual(0.052632,probabilidad([(-3,-1),(0,-2),(0,1),(2,0)],2))
    
    #amplitudTransicion
    def test_caso_amplitudTransicion_1(self):
        ket1=[[((2**0.5/2),0),(0,(2**0.5/2))]]
        ket2=[[(0,(2**0.5/2)),(-(2**0.5/2),0)]]
        self.assertEqual((0.0, -1.0),amplitudTransicion(ket1,ket2))
    #ValorMedio
    def test_caso_ValorMedio_1(self):
        observable=[[(1,0),(0,-1)],[(0,1),(2,0)]]
        ket=[[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]
        self.assertEqual((1.0000000000000007, 0.0),Varianza (observable,ket))

    #Varianza
    def test_caso_Varianza_1(self):
        observable=[[(1,0),(0,-1)],[(0,1),(2,0)]]
        ket=[[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]
        self.assertEqual((2.5000000000000004,0),valorMedio (observable,ket))
    #dinamicaDelSistema
    def test_caso_dinamicaDelSistema_1(self):
       ket=[[(1,0)],[(0,0)]]
       m1=[[(0,0),(1,0)],[(1,0),(0,0)]]
       m2=[[(2**0.5/2,0),(2**0.5/2,0)],[(2**0.5/2,0),(2**0.5/2,0)]]
       arreglo=[m1,m2]
       self.assertEqual([[(0.7071067811865476, 0.0)], [(0.7071067811865476, 0.0)]],DinamicaDelSistema(2, ket,arreglo))

if __name__ =='__main__':
    unittest.main()


