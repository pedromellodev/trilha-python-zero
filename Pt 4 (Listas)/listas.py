# O Padrão de criação de listas é o uso de colchetes "[]"

lst = [1, 2, 3, 4, 5]
print(lst)

lst2 = [1, 2, 3, 4, True]
print(lst2)

lst3 = [1, 2, [3, 4], True]
print(lst3)

lst4 = list(range(0,10))
print(lst4)

# Consultando o tamanho da lista
print(len(lst3))

# Alterando um item da lista
lst[-1] = False
print(lst)

for n in range(0, len(lst4)):
    print(lst4[n])
