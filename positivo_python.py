#UNID 1
print("Olá Mundo")
# O comando "print" é responsável por exibir na tela, ou melhor, "imprimir" o resultado de qualquer váriavel.

#UNID 2
a = 5 # O sinal de igual (=) atribui um valor a uma variável.
b = 7
c = 5 + 7 # O sinal de mais (+) soma os valores atribuidos a uma ou mais variáveis. E o mesmo ocorre com o sinal de menos (-), o asterisco (*) que realiza multiplicação, a barra (/) para divizão e porcentagem (%) em operações de mod.
print (c)
# Aqui eu apresento variáveis inteiras ou variáveis int; são variáveis que tem valores inteiros atribuidos a elas.

d = 1.5
e = 1.5
f = 1.5 + 1.5
print (f)
# Aqui é apresentado variáveis fracionadas ou variáveis float; são variáveis que tem valores de numeros fracionados decimais a uma variavel.

g = "Eu estou aqui"
print (g)
# Aqui estou representando uma variável de texto ou variável string; são variáveis que tem valores textuais atribuidos a elas, ou seja, assim como "print" estes tipos de variáis também posso exibir textos em tela.

a > d # "true"
a < b # "true"
# Usando os sinais de relação (< / >) permite que relacionemos uma variável a outra.

a >= d
a <= b
# Nesta situação o programa terá de avaliar se "a" é igual ou maior que "d" e se "a" é maior ou igual a "d".

d == e # "true"
a == b # "false"
# Quando o sinal de igual é repetido duas vezes (==) o programa compara o valor de duas variáveis, se forem iguais o programa a testa como verdadeiro, se forem diferentes o programa atesta como falso.

a != b # "true"
d != e # "false"
# Neste caso com o ponto de esclamação e o sinal de igual (!=) eu faço a comparação para saber se os valores das variáveis são diferentes uma das outras.

#UNID 3
idade = int(input("Insira sua idade")) # "int" está presente para determinar que o valor a ser inserido deve ser inteiro

if idade >= 18:
    print ("Idade maior de 18 anos.")
else:
    print ("Idade menor de 18 anos")
# "if" é responsável por começar uma sentença; neste caso se o valor for superior a 18, será exibida a mensagem deque é maior de 18 anos; mas se a caso for menor de 18 "else" exibira de mensagem de que é menor de 18 anos. É similar as questões para determinar se algo é "verdadeiro" ou "falso".

if idade >= 18 and idade <= 21:
    print ("Idade entre 18 e 21 anos")
# Mesma situação anterior; porém a caso for maior ou menor a algum dos dois valores, óbviamente a sentença será falsa assim encerrando esta parte do algoritmo; no entanto se a resposta estiver entre os dois valores, será exibida a mensagem e a sentença será considerada falsa.

nome = "Insira seu nome"
nome = input ("Digite seu nome") 
print ("Belo nome! Prazer em te conhecer")

#UNID 3
for i in range(0,3,1): # "0" é a inicialização (apartir de onde o algoritmo vai começar a contar), "3" a condição de parada (quantidade de vezes que deve ser repitido) e "1" o enclemento (como ele vai contar)
    print ("oi")
# "rage" serve para a repetição de determinada ação.
# "for" (para) assim como o "if" (se) são condições dentro da programação que você determina para que o programa execute.

#UNID 4
i = 0
while i < 3:
    print ("oi")
    i = i + 1
# "while" (enquanto) também é uma condição que pode ser imposto dentro do algoritmo do programa. E aqui, assim como no "for" impoem uma condição de repetição.

idade = [85, 36, 12, 4] # Cada número dentro do colchetes ([]) representa uma seção da lista.
print (idade[0]) # O 0 e 1 são respectivamente a primeira e a segunda seção da lista por isso na tela só irá aparecer o 85 e o 36.
print (idade[1])
# Aqui é apresentado o conceito de vetores para se criar uma lista em python com cada seção sendo exibida atravez do "print".


# *ERA DE UM ARQUIVO ANTO* 
encerrar = "S"
encerrar - input ("Digite 'Sim' para encerrar")
# "input" é um comando que permite a interação do usuário com o programa, para que assim o algoritmo termine de executar sua função.
