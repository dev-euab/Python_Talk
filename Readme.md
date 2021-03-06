#Python 馃悕
By Eric Uriel Avila Barrios 馃

##驴Qu茅 es Python?

* 馃憠馃徏 Sintaxis sencilla y "amigable 馃え" 馃憟馃徏
* Gran cantidad de Bibliotecas 馃槑
* Gran Comunidad 馃ぉ

#1.- Instalaci贸n 鈿欙笍

##Windows

![https://www.python.org/downloads/](img/python_windows.png)

> Nota durante la instalaci贸n aceptar que agregue Python al **PATH**

[Python Instalador](https://www.python.org/downloads/windows/)

####Comando  *CMD* 馃憞馃徏

```
	python --version
```	



##Mac / Linux
Normalmente traen por defecto Python instalado, para comprobar abriremos una terminal y ejecutaremos el siguiente Comando

####Comando  *Terminal* 馃憞馃徏

```
	python --version
```	

![https://www.python.org/downloads/](img/terminal.png)


> Se observa que existe de manera 馃巿**global**馃巿 una versi贸n de Python


**_Comprobar instalaci贸n_**

![Python Environment](img/python.png)

#2.- Ejecuci贸n 馃 鈱笍
Una vez que se comprob贸 que **Python**  est谩 instalado de manera correcta, podemos proseguir a hacer nuestro primer programa 鉁?

Todo programa de Python termina con una extensi贸n **.py**

Se puede utilizar el Editor de preferencia, en este caso ser谩 **VSCODE** 馃檵馃徎鈥嶁檪锔?

![Python Environment](img/vscode.png)

####Comando  *Terminal* 馃憞馃徏

```
	python [nombre del archivo Python]
```	

![Python Environment](img/1_01.png)

馃帄馃帀 YEAH!!!... 馃帄馃帀

#3.- Estructura en Python 馃悕
**驴QU脡?**馃え **驴Estructura?...**馃槙
As铆 es, normalmente en la mayor铆a de lenguajes de programaci贸n tu haces una funci贸n o un bloque de c贸digo y no importa c贸mo lo escribas, siempre y cuando respetes el "inicio" y el "fin", el abrir y cerrar llaves, corchetes. Y 驴a d贸nde quiero llegar?... 鈽癸笍 pues la manera de declarar una funci贸n, una condici贸n, un ciclo un bloque de c贸digo tiene la peculiaridad de la **IDENTACI脫N** 馃

Veamos un ejemplo 馃槈

![Python Environment](img/2_02.png)

Un momento... 驴d贸nde esta el punto y coma? 馃槺

> En Python puedes prescindir del **;**


#4.- Interacci贸n con Python

Python como se le aprecia, tiene su ambiente por medio de la **terminal** 馃枼 con la cual podemos interactuar para poder ingresar datos

![Python Environment](img/3_01.png)

Si quisi茅ramos ingresar alg煤n tipo de dato especifico seria de la siguiente manera

```python
int( input ("Ingresa un valor tipo Entero") )
float( input ("Ingresa un valor tipo Entero") )
str( input ("Ingresa un valor tipo Text") )
```
> Se **parsea** antes de ejecutar el **Input** para definir su valor 

#5.- Igual que todos...
Al igual que cualquier otro lenguaje de programaci贸n Python cuenta con sus 

##Tipos de Datos

```python
* string
* int
* float
* boolean
* list
* tuplas => es una lista que no puede cambiar (inmutable)
* diccionarios => {"key" : "value" , "key" : "value" }
* None == Null (En otros lenguajes de programaci贸n)
```

##Operadores Aritm茅ticos
```python
+
-
*
/
```
![Python Environment](img/4_01.png)

##Operadores L贸gicos
```python
==
!=
<
<=
>
>=
```
![Python Environment](img/5_01.png)

>Nota cuando uno declara una variable, est谩 puede tener el mismo nombre que otra siempre y cuando cambie una letra May煤scula o Min煤scula a esto se le conoce como => **Case Sensitive**
>
>Se puede declarar un "bloque" de variables en una sola linea y asignar el valor de cada uno respetando el orden en el cual fue declarado

```python
nombre, edad = "Luis", 28
```

##Ciclos
```python
#FOR
for contador in range(1,10):
	print contador
```

```python
#WHILE
	numero = 0
	while numero <= 10:
		print numero
		numero += 1
```

```python
#DO WHILE
#NO EXISTE EN PYTHON
```

###Constante
En Python no existe como tal los valores constantes, no existe un m茅todo para "definirlos" o "asignar" el tipo "constante", se utiliza una regla de escritura la cual al poner todo el nombre en may煤scula

```python
PI = 3.1416
```

##Funciones
Tambi茅n cuenta con su respectiva declaraci贸n de una Funci贸n

![Python Environment](img/6_01.png)

>Si dese谩ramos pasar los argumentos en otro orden se puede hacer de la siguiente manera, ejemplo:

```python
def argumentos(a,b)
	return a - b

argumentos(b=20,a=10)
```

>En caso de que se desconozca la cantidad de argumentos que vayan a pasar por la funci贸n, se hace de la siguiente manera

```python
def muchosArgumentos(*args):
	print(args)

muchosArgumentos(1,2,3,a,b,c,d,e)
```

>Y si se decidiera hacer un diccionario seria de la siguiente manera

```python
def muchosKeyArgumentos(**kwargs):
	print(kwargs)

muchosKeyArgumentos(a=1,b=2,c=3)
```

##Clases

La declaraci贸n de una Clase es de la siguiente manera

```python	
class nombreClase()
	#Constructor
	def __init_(self,args):
		self.argumentoA = ""
		self.argumentoB = ""
		print("Se ha instanciado la clase")
		
	def metodoA()
		pass
	
	def metodoB()
		pass
	
	def __metodoPrivado()
		pass
		
	#Destructor de clase
	def __del__(self)

```

Instanciar una clase

```Python
clase = nombreClase()
```

#Casos donde se aplica Python

##Python y RaspBerry

U cualquier otra plataforma de "mini computadoras"

![RaspBerryPi](img/rasp.jpg)

Dado al proceso de montaje de est谩 "mini computadora" es posible accesar a los *pines* para poder interactuar con *m贸dulos* que se conectaran a ellos utilizando librer铆as desarrolladas en **Python**

[Python + RaspBerry PI](https://projects.raspberrypi.org/en/projects?software[]=python)

##Python An谩lisis de Im谩genes / Video


Una librer铆a llamada *OPENCV* es utilizada en Python para el an谩lisis de videos y de im谩genes.

![Logo OPENCV](img/logopencv.png)


![Curve Lane Detection](img/opencv.png)

[Video => Curve Lane Detection](https://www.youtube.com/watch?v=-RuWTwDlot8&feature=youtu.be&fbclid=IwAR0r8OSPHKaNMDG6zD62vNWwkiFQ_LN6tbboko76HJak-obEcY9F-9qGDFs)


###Su repositorio en GITHUB

[OpencV](https://github.com/opencv/opencv)

###Grupos en Facebook
[Grupo Opencv A](https://web.facebook.com/groups/17450909269/)

[Grupo Opencv B](https://web.facebook.com/groups/2069477769970396/learning_content/)

##Servicios Web

Algo maravilloso es que puedes tener desde un sitio Web hasta una poderosa API, dos conocidos **DJANGO** y **Flask**

![Logo OPENCV](img/django.png)
[GITHUB DJANGO](https://github.com/django/django)


![Logo OPENCV](img/flask.png)
[GITHUB FLASK](https://github.com/pallets/flask)


#TIP 馃槒
Si tienes una emergencia y solo quieres ver como se ver铆an algunos estilos **CSS** , algunos **JAVASCRIPT**, un sitio web solo su **FRONT END** utiliza

####Comando  *CMD* 馃憞馃徏

```
	#2.7
	python -m SimpleHTTPServer 8000
```	

```
	#3.X
	python -m http.server 8000
```	 

#YA QUIERO EMPEZAR!!!... Alto ah铆!!! 馃が 馃檮
Un consejo antes de bajar librer铆as e intentar construir tu pr贸ximo Tesla System... 馃槰

Utiliza una de las librer铆as mas *geniales* 馃槑  de Python llamada **PIPENV**, la cual nos provee le capacidad de tener tu **ambiente de desarrollo** de manera independiente a tu **SO** 馃く

![Logo PIPENV](img/logopipenv.png)

[PIP ENV](https://pipenv-fork.readthedocs.io/en/latest/)



![RaspBerryPi](img/pipenv.png)

