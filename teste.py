def numero_do_meio(lista,comeco,fim):

    lista_indices = []

    for i in range(comeco, fim + 1):
        lista_indices.append(i)

    media_indices = sum(lista_indices) // len(lista_indices)

    return lista[media_indices]


lista = [100,201,315,405,406,407,500,600,700,900,1000,1003]

print(numero_do_meio(lista, 4, 6))
