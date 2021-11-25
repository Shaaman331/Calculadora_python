print("\nDigite: \n\na para adição \ns para subtração \nm para multiplicação \nd para divisão")

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo numero: "))

escolha = input("Escolha a operação:")

# adição
if escolha == 'a':
    print(a + b)

# subtração

if escolha == 's':
    print(a - b)

# multiplicação

if escolha == 'm':
    print(a * b)

# divisão
if escolha == 'd':
    print(a / b)    
