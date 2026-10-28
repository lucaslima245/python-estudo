vendas = [100, 50, 30, 60]

print(vendas[0]) #pegar um item da lista

print(len(vendas)) #mostra o tamanho da lista

#somar todos os itens

print(max(vendas)) #mostra maior valor

print(min(vendas))

print(sum(vendas)) #mostra a soma da lista


#encontrar um elemento(a posicao do elemento)

produtos = ["iphone", "ipad","apple watch", "airpod","macbook"]

print("airpod" in produtos)

posicao = produtos.index("ipad") 

print(posicao)

#editar um item

lista_precos = [500, 399, 300, 100]

novo_preco = lista_precos[0] + 100

lista_precos[0] = novo_preco

print(lista_precos)

#remover um item da lista

produtos.remove("macbook")

print(produtos)


produtos.pop(0)
item_removido = produtos.pop(0)

print(produtos)
print(item_removido)



#adicionar um item na lista

produtos.append("macbook") #adiciona no o item no final da lista

print(produtos) 

lista2 = ["pc", "air tag", "caixa de som"]

produtos.extend(lista2) #adiciona um lista na outra

print(produtos)



#inserir um item em uma posicao especifica

produtos.insert(0, "airpod max")
print(produtos)

#contar quantas vezes um item tem na lista
print(produtos.count("airpod"))

#ordenar um lista
lista_precos.sort(reverse = True)  #ordem numerica

print(lista_precos)

produtos.sort() #organiza em ordem alfabetica

