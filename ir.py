#boas vindas
print("Olá, vamos calcular seu imposto de renda?")

#string
salario = int(input("Digite seu salário:"))

#tentando fase 1
if salario <= 1903.98:
    print("Livre de imposto de renda.")
elif salario >= 1903.99 and salario <= 2826.65:
    #7.5% do salario
    porcentagem = 7.5 / 100
    #conta
    sobra_salario = salario - porcentagem * salario
    valor_pagar = porcentagem * salario
    print("sua aliquota é de 7.5% valor a pagar é de: R$", valor_pagar)
elif salario >= 2826.66 and salario <= 3751.05:
    #15% do salario
    porcentagem = 15 / 100
    #conta
    sobra_salario = salario - porcentagem * salario
    valor_pagar = porcentagem * salario
    print("sua aliquola é de 15% valor a pagar é de: R$", valor_pagar)
elif salario >= 3751.06 and salario <= 4664.68:
    #22.5% do salario
    porcentagem = 22.5 / 100
    #conta
    sobra_salario = salario - porcentagem * salario
    valor_pagar = porcentagem * salario
    print("sua aliquola é de 22.5% valor a pagar é de: R$", valor_pagar)
else:
    #27.5% do salario
    porcentagem = 27.5 / 100
    #conta
    sobra_salario = salario - porcentagem * salario
    valor_pagar = porcentagem * salario
    print("sua aliquola é de 27.5% valor a pagar é de: R$", valor_pagar)
    #Obrigada.
print(f"o salario liquido é de R${sobra_salario}.")