class Coordenada:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distancia(self, otra_coordenada):
		x_dif = (self.x - otra_coordenada.x)**2
		y_dif = (self.y - otra_coordenada.y)**2
		return f'{round((x_dif + y_dif)**0.5, 3)} metros'


if __name__ == '__main__':

	coord_1 = Coordenada(3, 30)
	coord_2 = Coordenada(4,  8)

	# print(coord_1.distancia(coord_2))

	print(isinstance(coord_2, Coordenada))