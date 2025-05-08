def calculator():
    print("Bem-vindo à Calculadora!")
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    try:
        choice = int(input("Digite o número da operação (1/2/3/4): "))

        if choice in [1, 2, 3, 4]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if choice == 1:
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif choice == 2:
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif choice == 3:
                print(f"Resultado: {num1} * {num2} = {num1 * num2}")
            elif choice == 4:
                if num2 != 0:
                    print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida. Por favor, escolha entre 1 e 4.")
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")

if __name__ == "__main__":
    calculator()