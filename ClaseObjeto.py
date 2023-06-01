class Objeto:
    __numero: int
    __palabra: str

    def __init__(self,numero,palabra) -> None:
        self.__numero = numero
        self.__palabra = palabra

    def mostrar(self):
        print('Numero: {}, Palabra: {}'.format(self.__numero,self.__palabra))