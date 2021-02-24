import random

def busqueda_lienal(lista, objetivo):
    match = False

    for element in lista:
        if element == objetivo:
            match = True

    return match


if __name__ == '__main__':

    list_size = int(input("Tamaño de tu lista: "))
    objetivo = int(input("Que numero quieres encontrar? "))

    lista = [random.randint(0, 100) for i in range(list_size)]

    encontrado = busqueda_lienal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')

