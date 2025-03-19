def calculadora(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input("primeiro valor: "))
    valor2 = int(input("segundo valor: "))
    resultado = calculadora(valor1, valor2)
    print(resultado)