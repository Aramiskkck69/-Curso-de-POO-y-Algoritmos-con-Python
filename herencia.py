class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):

    def __init__(self, lado): #se define el constructor
        #"""
        # se hace una instancia y a los metodos
        # de la super clase padre y se sustituye
        # base = lado y altura = lado
        # """
        super().__init__(lado, lado)


class Triangulo(Rectangulo):

    def __init__(self, base_t, altura_t):
        super().__init__(base_t, altura_t)

    def area(self):
        return (self.base * self.altura)/2



if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())


    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())

    triangulo = Triangulo(base_t=3, altura_t=4)
    print(triangulo.area())

