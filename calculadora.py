
def calculadora():
    while True:
        print("\n===== CALCULADORA =====")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")

        opcao = input("Escolha uma operação: ")

        if opcao == "0":
            print("Calculadora encerrada!")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida! Tente novamente.")
            continue

        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: digite apenas números.")
            continue

        if opcao == "1":
            resultado = numero1 + numero2
        elif opcao == "2":
            resultado = numero1 - numero2
        elif opcao == "3":
            resultado = numero1 * numero2
        elif opcao == "4":
            if numero2 == 0:
                print("Erro: não é possível dividir por zero.")
                continue
            resultado = numero1 / numero2

        print(f"Resultado: {resultado:g}")


calculadora()
