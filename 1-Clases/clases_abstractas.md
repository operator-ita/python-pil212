# Clases abstractas en Python
octubre 5, 2020 Por Daniel Rodríguez 

Un concepto importante en programación orientada a objetos es el de las clases abstractas. Unas clases en las que se pueden definir tanto métodos como propiedades, pero que no pueden ser instancias directamente. Solamente se pueden usar para construir subclases. Permitiendo así tener una única implementación de los métodos compartidos, evitando la duplicación de código. Hoy vamos a ver cómo definir las clases abstractas en Python.

Propiedades de las clases abstractas
La primera propiedad de las clases abstractas es que no puede ser instanciadas. Simplemente proporciona una interfaz para las subclases derivadas y evitando así la duplicación de código.

Otra característica de estas clases es que no es necesario que tengan una implementación de todos los métodos necesarios. Pudiendo ser estos abstractos. Los métodos abstractos son aquellos que solamente tienen una declaración, pero no una implementación detallada de las funcionalidades.

Las clases derivadas de las clases abstractas debe implementar necesariamente todos los métodos abstractos para poder crear una clase que se ajuste a la interfaz definida. En el caso de que no se defina alguno de los métodos no se podrá crear la clase.

Resumiendo, las clases abstractas define una interfaz común para las subclases. Proporciona atributos y métodos comunes para todas las subclases evitando así la necesidad de duplicar código. Imponiendo además lo métodos que deber ser implementados para evitar inconsistencias entre las subclases.

## Creación de clases abstractas en Python
Para poder crear clases abstractas en Python es necesario importar la clase ABC y el decorador abstractmethod del modulo abc (Abstract Base Classes). Un módulo que se encuentra en la librería estándar del lenguaje, por lo que no es necesario instalar. Así para definir una clase privada solamente se tiene que crear una clase heredada de ABC con un método abstracto.

```python
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass
```

Ahora si se intenta crear una instancia de la clase animal, Python no lo permitirá indicando que no es posible. Es importante notar que que si la clase no hereda de ABC o contiene por lo menos un método abstracto, Python permitirá instancias las clases.

```python
class Animal(ABC):
    def mover(self):
        pass
    
Animal()
class Animal():
    @abstractmethod
    def mover(self):
        pass
    
Animal()
```

## Métodos en las subclases
Las subclases tienen que implementar todos los métodos abstractos, en el caso de que falta alguno de ellos Python no permitirá instancias tampoco la clase hija.

```python
class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def comer(self):
        print('Animal come')
        
class Gato(Animal):
    def mover(self):
        print('Mover gato')
        
g = Gato() # Error
```

Por otro lado, desde los métodos de las subclases podemos llamar a las implementaciones de la clase abstracta con el comando super() seguido del nombre del método.

```python
class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def comer(self):
        print('Animal come')
        
class Gato(Animal):
    def mover(self):
        print('Mover gato')
        
        
    def comer(self):
        super().comer()
        print('Gato come')
        
g = Gato()
g.mover()
g.comer()
```

Mover gato
Animal come
Gato come

## Conclusiones
En esta entrada se ha visto cómo se pueden usar el patrón de clase abstracta en Python. Un patrón que es clave en programación orientada a objetos para evitar la repetición de código, centralizando las funcionalidades comunes en una clase que sirve de plantilla para las clases hijas