for i in range(10): # Usado principalmente quando já sabemos quantas repetições terá
    print("Produto", i+1, "verificado")

# Quando não sabemos quantas repetições será necessários para alcançar
# O objetivo desejado, usamos o While

temp = 15

while temp <= 25:
    print(f'Temperatura atual: {temp:.2f}')
    temp += 1

# Outros exemplos

dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

for x in dias:
    print(f'Dia atual: {x}')