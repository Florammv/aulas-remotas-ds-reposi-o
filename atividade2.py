#Tabuada
n_txt = input("Digite um número para exibir sua tabuada: ")
n = int(n_txt) #convertendo de texto para número 

print("Tabuada do número ", n, ": ")

for i in range(1,11): #criando o loop
resultado = n * i

print(n, "x", i, "= ", resultado)