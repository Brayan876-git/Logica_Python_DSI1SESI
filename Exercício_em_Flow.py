for pacote in range(0, 9 + 1, 1):
    print("===== SEJA BEM-VINDO =====")
    print("Quanto pesa o pacote?")
    pacote = float(input())
    if pacote == 2:
        print("Pacote classificado como Leve")
        custo = 10.0
        print("Custo Fixo: R$10,00 ")
        peso = 2
    else:
        if pacote >= 2 and pacote < 10:
            print("Pacote Classificado como Padrão ")
            custo = 20.0
            print("Custo fixo: R$20,00 ")
            peso = 5
        else:
            if pacote >= 10 and pacote < 100:
                print("Pacote classificado como Pesado ")
                print("Custo fixo: R$30,00")
                custo = 30.0
                peso = 10
            else:
                print("Peso Indevido ")
    print("Pacote está com destino internacional? ")
    internacional = input()
    if internacional == "sim":
        print("Será aplicado um acréscimo de 20% sobre o valor do pacote ")
        custo = custo + custo * 0.2
        peso = peso % 10
    else:
        print("Tudo bem.")
print("Calculando o Valor final...")
print("Custo total: R$" + str(custo) + ".00" + " Peso total acumulada:" + str(peso) + "Kg.")
print("fim")
