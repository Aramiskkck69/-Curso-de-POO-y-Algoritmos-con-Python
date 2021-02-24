class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura='caleinte'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centifugar()

    def _llenar_tanque_de_agua(self, tempertatura):
        print(f'Llenando el tanque con agua {tempertatura}')

    def _anadir_jabon(self):
        print('Anadiendo jabon')

    def _lavar(self):
        print('Lavar la ropa')

    def _centifugar(self):
        print('Centrifugar')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()
