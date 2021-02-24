class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        print("Estoy en el wrapper")
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no esta en la lista')


if __name__ == '__main__':
    casilla = CasillaDeVotacion(123, ['Mexico', 'Morelos'])
    # print(casilla._region)
    casilla.region = 'Morelos'
    print(casilla._region)


# class Millas:
#
#     def __init__(self):
#         self._distancia = 0
#
#     # Función para obtener el valor de _distancia
#     # Usando el decorador property
#     @property
#     def obtener_distancia(self):
#         print("Llamada al método getter")
#         return self._distancia
#
#     # Función para definir el valor de _distancia
#     @obtener_distancia.setter
#     def definir_distancia(self, valor):
#         if valor < 0:
#             raise ValueError("No es posible convertir distancias menores a 0.")
#         print("Llamada al método setter")
#         self._distancia = valor
#
#
# if __name__ == '__main__':
#     # Creamos un nuevo objeto
#     avion = Millas()
#     # Indicamos la distancia
#     avion.distancia = 200
#     print(avion.distancia)
