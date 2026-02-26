lista_principal = [25.1, 25.5, 24.9, 26.0, 25.8] # Lista base
print(f'Lista inicial: {lista_principal}')

# Adição de novos valores
lista_principal.append(55.5) # Adição do número 55.5
lista_principal.append(43.5) # Adição do número 43.5
lista_principal.append(54.8) # Adição do número 54.8
print(f'Lista pós modificação: {lista_principal}')

# Elementos especificos
print(f'Primeiro elemento: {lista_principal[0]}') # O primeiro indice é 0 na lista (nesse caso [0] = 25.1)
print(f'Segundo elemento: {lista_principal[1]}') # Depois vem o próximo (seguindo a lógica matematica, depois do zero vem o um, logo [1] = 25.5)
print(f'Último elemento: {lista_principal[-1]}') # [-1] pode ser utilizado para encontrar o último valor adicionado

# Modificação de um ponto especifico
lista_principal[3] = 25.0 # Atribuição de 25.0 para a terceira posição
print(f'Terceira linha foi modificada de 24.9 para {lista_principal[3]}. Lista completa: {lista_principal}')

# Remoção de elemento
lista_principal.pop(-1) # Remove o último elemento
print(f'Lista pós modificação: {lista_principal}')

# Verificação do tamanho de uma lista
print(f'Número total de valores registrados: {len(lista_principal)}')

# Verificação de existência de um valor
if 26.2 in lista_principal:
    print("A lista possui o termo 26.2") # Se a lista possuir o valor "26.2" essa mensagem será exibida
else:
    print("A lista não possui este valor!") # Se a lista não possui este valor, essa mensagem será exibida no lugar

# Ordenamento de leitura
lista_principal.sort()
print(f'Leitura ordenada: {lista_principal}') # Lista mostra do menor para o maior valor

# EXEMPLOS COM DICIONARIOS
comidas = {
    "comida_1": "salgadinho",
    "comida_2": "pão",
    "comida_3": "refrigerante",
    "comida_4": "coxinha",
    "comida_5": "sonho"
} # Dicionario base

# Adição de novas comidas
comidas.update({"comida_6": "pastel"}) # Comida 6 com o id "Pastel" será adicionado
comidas.update({"comida_7": "guaraná"}) # Comida 7 com o id "Guaraná" será adicionado
print(f"Comidas pós mudança: {comidas}")

# Acesso de um dado especifico 
comida6 = comidas["comida_6"]
comida4 = comidas["comida_4"]
print(f"A comida 6 é: {comida6}")
print(f"Comida 4 é: {comida4}")

# Modificando uma comida
comidas["comida_2"] = "banana"
print(f"Comidas pós mudança: {comidas}")

# Tamanho da lista
print(f"Tamanho do dicionario é: {len(comidas)}")

# Remoção de elemento
del comidas["comida_5"]
print(f"Comidas pós mudança: {comidas}")

# Listando todas as comidas cadastradas
print(f"Comidas atualmente registradas: {comidas.keys()}")