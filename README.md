# Teoría Cuántica básica

##### En este repositorio se desarrollaran los programing drills del caputulo 4 del libro quantum computing for computer scientists en el cualse desarrolaran los siguientes puntos
1. Sistema de la posición de la partícula en una recta. Usuario especifica el número de puntos posibles y un vector ket y el sistema calcula las probabilidades de encontrar partícula en una posición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación

2. Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.

3. El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.

4. Se considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema calcula el estado final a partir de un estado inicial.

- Probabilidad
  - Descripcion entrada 
    - Vector -> ket
    - Entero -> Posicion de la cual se quiere ver la probabilidad de la particula
   - Entrada Ejemplo
   ~~~~
    probabilidad([(-3,-1),(0,-2),(0,1),(2,0)],2)
   ~~~~

- Amplitud
  - Descripcion entrada 
    - Vector -> ket1
    - Vector -> ket2
  - Entrada Ejemplo
   ~~~~
    ket1=[[((2**0.5/2),0),(0,(2**0.5/2))]]
    ket2=[[(0,(2**0.5/2)),(-(2**0.5/2),0)]]
    amplitudTransicion(ket1,ket2)
   ~~~~
- Valor Medio
  - Descripcion entrada
    - Matriz Compleja -> Observable
    - Matriz Compleja -> Ket
  - Entrada Ejemplo
  ~~~~
  observable=[[(1,0),(0,-1)],[(0,1),(2,0)]]
  ket=[[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]
  valorMedio (observable,ket)
  ~~~~

- Valor Medio
  - Descripcion entrada
    - Matriz Compleja -> Observable
    - Matriz Compleja -> Ket
  - Entrada Ejemplo
   ~~~~
    observable=[[(1,0),(0,-1)],[(0,1),(2,0)]]
    ket=[[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]
    Varianza(observable ,ket))
   ~~~~

- Valor Medio
  - Descripcion entrada
    - #entero --> tiempos
    - Matriz Compleja --> ket
    - lista de Matrizes Complejas --> arreglo
  - Entrada Ejemplo
  ~~~~
    ket=[[(1,0)],[(0,0)]]
    m1=[[(0,0),(1,0)],[(1,0),(0,0)]]
    m2=[[(2**0.5/2,0),(2**0.5/2,0)],[(2**0.5/2,0),(2**0.5/2,0)]]
    arreglo=[m1,m2]
    DinamicaDelSistema(2, ket,arreglo)
   ~~~~
  



# Pruebas
#### Al compilar el archivo automaticamente se ejecutan 15 pruebas que verifican todas las operaciones especificadas anteriormente.
#### para ejecutar el archivo matrices.py sigua las siguientes intrucciones:

1. Descargue el repositorio
~~~~
git clone https://github.com/ItaloNovoa/lab2-CNYT.git
~~~~
2. Ingrese al cmd/Terminal o simbolo del sistema
3. Ingresar a la carpeta de archivo 
4. digitar (Windows):
~~~~
python  lab4CNYT.py 
~~~~ 
4.digitar (Ubuntu, Mac)
~~~~
python3 lab4CNYT.py
~~~~
