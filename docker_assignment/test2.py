# Calculadora de Indice de Masa Corporal

def calcula_imc(peso, altura):
    return peso / altura ** 2

def main():
    peso = 66
    altura = 1.81
    print('Peso (kg): ', peso)
    print('Altura (metros): ', altura)
    imc = calcula_imc(peso, altura)
    print('Tu IMC es: {:.2f}'.format(imc))

if __name__ == '__main__':
    main()