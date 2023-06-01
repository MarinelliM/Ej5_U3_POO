# from zope.interface import interface
# from zope.interface import implementer
# from ClaseObjeto import Objeto
# #from interface import CInterface
# from abc import ABC, abstractclassmethod
# class CInterface(interface):
#     @abstractclassmethod
#     def insertarElemento(objeto,posicion):
#         pass
#     @abstractclassmethod
#     def agregarElemento(elemento):
#         pass
#     @abstractclassmethod
#     def mostrarElemento(posicion):
#         pass

# @implementer(CInterface)
# class Coleccion(CInterface):
#     __lista: list
from zope.interface import Interface, implementer,IInterfaceDeclaration
from ClaseObjeto import Objeto
#from abc import ABC, abstractmethod

class CInterface(IInterfaceDeclaration):
    #@abstractmethod
    def insertarElemento(self, objeto, posicion):
        pass

    #@abstractmethod
    def agregarElemento(self, elemento):
        pass

    #@abstractmethod
    def mostrarElemento(self, posicion):
        pass

@implementer(CInterface)
class Coleccion:
    __lista: list

    def __init__(self) -> None:
        self.__lista = []

    def agregarElemento(self,elemento):
        self.__lista.append(elemento)
    
    def insertarElemento(self,objeto,posicion):
        if posicion < 0 or posicion > len(self.__lista):
            raise Exception('La posicion no es valida')
        else: self.__lista.insert(posicion,objeto)

    def mostrarElemento(self,posicion):
            if posicion < 0 or posicion >= len(self.__lista):
                raise Exception('La posicion no es valida')
            else: 
                print('Objeto:')
                self.__lista[posicion].mostrar()

    # def cole(self, manejadorco: CInterface):
    #     posicion = str(input('Posicion:'))
    #     manejadorco.mostrarElemento(posicion)

    def test(self):
        manejador = Coleccion()
        numero = int(input('Ingrese un numero:'))
        palabra = str(input('Ingrese una palabra:'))
        objeto = Objeto(numero,palabra)
        manejador.agregarElemento(objeto)
        print('\n')
        numero2 = int(input('Ingrese un numero:'))
        palabra2 = str(input('Ingrese una palabra:'))
        objeto2 = Objeto(numero2,palabra2)
        posicion = int(input('Ingrese la posicion donde quiere insertar al objeto:'))
        manejador.insertarElemento(objeto2,posicion)
        print('\n')
        posicion2 = int(input('Ingrese la posicion del objeto que quiere mostrar:'))
        manejador.mostrarElemento(posicion2)
        print('\n')
    
if __name__ == '__main__':
    c = Coleccion()
    c.test()