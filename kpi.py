nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
bonus_porc = float(input("Digite o valor do seu bônus: "))

bonus = 1000 + salario * bonus_porc

print(f"Olá {nome}, o seu bônus foi de {bonus}!")
