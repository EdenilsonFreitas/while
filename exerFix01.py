#Questão 01
# # Mensagem inicial (opcional)
# print("=== Exibindo números de 1 a 100 ===\n")

# contador = 1

# while contador <= 100:
#     print(contador)
#     contador += 1

# # Mensagem final
# print("\nPrograma encerrado. Todos os números de 1 a 100 foram exibidos.")


#Questao 02


# # Mensagem inicial
# print("=== Programa de Soma de Valores ===")
# print("Digite números para somar.")
# print("Quando digitar 0, o programa será encerrado e mostrará o resultado.\n")

# soma = 0

# while True:
#     numero = float(input("Digite um valor: "))

#     if numero == 0:
#         break

#     soma += numero

# # Resultado final
# print("\nSomatório dos valores digitados:", soma)
# print("Programa encerrado.")

#Questao 03

# Senha armazenada
senha_correta = "1234"

# Solicita a senha ao usuário
senha = input("Digite a senha: ")

# Enquanto a senha estiver incorreta
while senha != senha_correta:
    print("Senha incorreta! Tente novamente.")
    senha = input("Digite a senha: ")

# Quando acertar a senha
print("Senha correta! Acesso permitido.")
print("Programa encerrado.")