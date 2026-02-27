# Com o if permitimos que seja colocado uma condição para determinada ação ser executada
temperatura = 32
if temperatura > 25:
    print("Está quente")
elif temperatura < 25: # Segunda verificação de um estado
    print("Está gelada!")
else: # Caso nenhum estado seja sendo correspondido, executa a exceção
    print("O ambiente está bom!")