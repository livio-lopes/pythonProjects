# Programinha para somar duas Listas
# Feito por Lívio Lopes


lista_1 = [1,2,3,4,5,6,7]
lista_2 = [1,2,3,4]

#Combinando as listas
soma = zip(lista_1,lista_2)
#Formando lista de somas dos valores desempacotados
total = [x + y for x,y in soma]
print(total)