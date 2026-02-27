class ValvulaDeControle:
    def __init__(self, id, tipo_fluido):
        self.id_valvula = id
        self.tipo_fluido = tipo_fluido
        self.abertura = 0.0
        self.status = "Em operação"

    def ajuste_abertura(self, percentual_almejado):
        if 0 <= percentual_almejado <= 100:
            self.abertura = float(percentual_almejado)
            print(f"{self.id_valvula} Abertura ajustada para {self.abertura}%")
        else:
            self.status = "Parado"
            print(f"{self.id_valvula} Não está em condições de operação. Por favor, verifique o percentual desejado")

    def relato_estado(self):
        estado = (f"--- Relatório da Válvula {self.id_valvula} ---\n"
                  f"  Fluido: {self.tipo_fluido}\n"
                  f"  Abertura: {self.abertura}%\n"
                  f"  Status: {self.status}\n"
                  f"------------------------------------")
        return estado
    
# Fim da criação da Classe

# Criando objetos
valvula_agua = ValvulaDeControle("A-24", "Água Resfriada")
valvula_ar = ValvulaDeControle("T-50A", "Ar Comprimido")
print("--" * 10)

# Realizando as tarefas dos objetos
valvula_agua.ajuste_abertura(110)
valvula_ar.ajuste_abertura(100)
print("--" * 10)
print(valvula_agua.relato_estado())
print(valvula_ar.relato_estado())
