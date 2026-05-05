#questão 01

# for i in range(2, 13, 2):
#     print(i, end=", ")

#questão 02

# # Programa para imprimir números de 1 até o valor digitado
# numero = int(input("Digite um valor positivo: "))
# for i in range(1, numero + 1):
#     print(i)
# print("Programa encerrado.")

#questão 03


# v_ini = int(input("Digite o valor inicial (positivo): "))
# v_fim = int(input("Digite o valor final (positivo): "))

# # Garantindo que o intervalo funcione corretamente
# if v_ini <= v_fim:
#     for i in range(v_ini, v_fim + 1):
#         print(i)
# else:
#     for i in range(v_ini, v_fim - 1, -1):
#         print(i)

# print("Programa encerrado.")

#questão 04

# v_ini = int(input("Digite o valor inicial (positivo): "))
# v_fim = int(input("Digite o valor final (positivo): "))

# # Garante a ordem correta
# if v_ini < v_fim:
#     for i in range(v_ini + 1, v_fim):
#         print(i)
# else:
#     for i in range(v_ini - 1, v_fim, -1):
#         print(i)

# print("Programa encerrado.")

#questão 05
"""
Escreva um programa que solicite do usuário dois valores positivos. Em
seguida, imprima todos os números primos contidos dentro desse intervalo e o
somatório desses números primos. Ao término, informe que o programa foi
encerrado.
"""
v_ini = int(input("Digite o valor inicial (positivo): "))
v_fim = int(input("Digite o valor final (positivo): "))

soma = 0

# Garante a ordem correta
if v_ini > v_fim:
    v_ini, v_fim = v_fim, v_ini

for num in range(v_ini, v_fim + 1):
    if num > 1:
        primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                primo = False
                break
        if primo:
            print(num)
            soma += num

print("Somatório dos primos:", soma)
print("Programa encerrado.")