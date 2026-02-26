evento_contagem = 250 # número inteiro

sensor_temperatura = 27.5 # float

nome_dispositivo = "Matheusp" # string

funcionamento_sistema = True # bool

#Conversões
# str -> int
numero_str = "123"
numero_int = int(numero_str)
print(numero_int) # Saída: 123
# str -> float
numero_str_2 = "456"
numero_float = float(numero_str_2)
print(numero_float) # Saída: 456
# float -> str
numero_float2 = 25.5
numero_str_3 = str(numero_float2)
print(numero_str_3) # Saída: "25.5"
# float -> int
numero_inteiro = 1
float_numero = float(numero_inteiro)
print(float_numero) # Saída: 1.0

#Atribuições múltiplas
a, b, c = 1, 2, 3
print(a, b, c) # Saída: 1 2 3
a = b = c = 3
print(a, b, c) # Saída: 3 3 3
