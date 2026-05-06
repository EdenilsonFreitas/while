#Questão 04
# import random

# # Gera um número aleatório entre 1 e 100
# numero_secreto = random.randint(1, 100)

# palpites = 0
# acertou = False

# print("Tente adivinhar o número entre 1 e 100!")

# while not acertou:
#     try:
#         chute = int(input("Digite seu palpite: "))
#         palpites += 1

#         if chute < numero_secreto:
#             print("Muito baixo! Tente novamente.")
#         elif chute > numero_secreto:
#             print("Muito alto! Tente novamente.")
#         else:
#             acertou = True
#             print(f"Parabéns! Você acertou o número {numero_secreto}!")
#     except ValueError:
#         print("Por favor, digite um número válido.")

# print(f"Você precisou de {palpites} palpites.")
# print("Programa encerrado.")

#Questão 05
"""
Escreva um programa que solicita ao usuário um valore numérico inteiro positivo e, em
seguida, calcule o fatorial desse número usando um loop do tipo while. Ao final o
programa deverá exibir o valor do fatorial do número informado pelo usuário e término
do programa.
"""
# #Solicita um número inteiro positivo
# numero = int(input("Digite um número inteiro positivo: "))

# # Validação simples
# while numero < 0:
#     numero = int(input("Valor inválido. Digite um número inteiro positivo: "))

# fatorial = 1
# contador = 1

# # Cálculo do fatorial usando while
# while contador <= numero:
#     fatorial *= contador
#     contador += 1

# # Exibe o resultado
# print(f"O fatorial de {numero} é {fatorial}.")
# print("Programa encerrado.")

#Questão 06

"""
Escreva um programa que peça ao usuário para digitar um número “n” inteiro positivo
e, em seguida, imprima os “n” primeiros termos da sequência de Fibonacci. A
sequência de Fibonacci é dada pela somatório de dois números que resulta no seu
sucessor. Ex: 0, 1, 1, 2, 3, 5, 8... Esses são os 7 primeiros números da sequência.
Exiba os números na tela e informa o término do programa ao final.
"""
# # Solicita um número inteiro positivo
# n = int(input("Digite um número inteiro positivo: "))

# # Validação simples
# while n <= 0:
#     n = int(input("Valor inválido. Digite um número inteiro positivo: "))

# # Inicializa os dois primeiros termos
# a, b = 0, 1
# contador = 0

# print(f"Os {n} primeiros termos da sequência de Fibonacci são:")

# # Loop para gerar os termos
# while contador < n:
#     print(a, end=" ")
#     a, b = b, a + b
#     contador += 1

# print("\nPrograma encerrado.")

#Questão 07
"""
Escreva um algoritmo que solicite ao usuário um número entre 1 e 10.000 e
depois informe ao usuário se o número digitado é primo ou não. Um número é
dito ser primo quando ele é divisível apenas por 1 e ele mesmo. Ao término,
informe que o programa foi encerrado.
"""
# Solicita um número entre 1 e 10.000
# numero = int(input("Digite um número entre 1 e 10000: "))

# # Validação do intervalo
# while numero < 1 or numero > 10000:
#     numero = int(input("Valor inválido. Digite um número entre 1 e 10000: "))

# # Verificação se é primo
# if numero == 1:
#     primo = False
# else:
#     primo = True
#     divisor = 2

#     while divisor <= numero // 2:
#         if numero % divisor == 0:
#             primo = False
#             break
#         divisor += 1

# # Resultado
# if primo:
#     print(f"O número {numero} é primo.")
# else:
#     print(f"O número {numero} não é primo.")

# print("Programa encerrado.")

# Questão 08

"""
Escreva um programa que peça ao usuário para digitar um número inteiro e,
em seguida, calcule a soma dos dígitos desse número usando um loop while.
Ao término, informe que o programa foi encerrado.
Ex: entrada: 19.623 → saída: 21; entrada: 456 → saída: 15;
"""
