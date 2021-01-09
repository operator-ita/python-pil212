from abc import ABC, abstractmethod


def nombre():
    pass 

class EspadaFuego():
    def atacar(self):
        print("Atacar")


class EspadaHielo():
    def restarurarse(self):
        print("restaurarse")


espada1 = EspadaFuego()
espada2 = EspadaFuego()
espada1.atacar()
espada2.atacar()
type(espada1)

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
        
# g = Gato()

"""
g.mover()
g.comer()
""" 


