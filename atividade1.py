#Identificador de maioridade
nome = input("Qual o seu nome? ")
idade_txt = input("Qual a sua idade? ") #idade em texto
idade_n = int(idade_txt) #convertendo para a idade ser igual a número inteiro

If(idade>=18): #Verificando se a pessoa é mairo de idade ou não
    print(f"Olá, {nome}! você é maior de idade.")
else:
    print(f"Olá, {nome}! você é menor de idade.")