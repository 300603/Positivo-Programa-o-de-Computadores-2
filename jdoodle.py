x = 10
y = 20
z = x + y
print ('A somando basica 10 + 20 é igual a', z)

print ('Isto é óbvio, e qualquer maquina mesmo sem um programa muito complexo consegue realizar esta conta.')
print ('No entanto as maquinas não conseguem contar até o número especificado, por exemplo:')

print ('se eu inserir o valor "31", a maquina contará 31 unidades numéricas, ou seja, de 0 até 30, desta forma parando no número "30"')
for z in range (31):
    print (z)

print ('Agora se um ser humano contasse, o individuo iniciaria a contágem de 1 até 30 ou 31, mas como isto é representado na programação.')
print ('A forma textual é universal, ou seja, todos dão o mesmo nome, com talvez uma ou outra denominando de forma diferente, mas a maioria se usa "for", que derivado do inglês significa "para" no português.')
print ('Exercendo sua função, assim como já revelado antes, com a função "for", é possivel fazer a maquina contar de 0 até um valor determinado, mas também é possivel fazer com que ela realize uma função em loop (repitir a mesma coisa sem parar). Exemplo:')
print ('se em "for", perdir para que seja empresso o nome Mateus 10 vezes...')
for Mateus in range (10):
    print ('Mateus')
    
print ('A forma de se fazer é bem simples com: https://dkrn4sk0rn31v.cloudfront.net/uploads/2021/01/como-funciona-o-for...in-no-python.png')

print ('Mas claro, contagem ou repetição não é a unica coisa possivel de se fazer com o "for", outra de suas funções é fazer ele contar quantas vezas foi reptida uma palavra; por exemplo:')
for m in range (10):
    print (m)
    print ('Mateus')
    
print ('Deixando de lado a função "for", porque não falamos um pouco mais das variáveis; exemplo:')
print ('digamos que a variável "a" é igual a 15, "b" igual a 15 e "c" igual a soma das duas (a+b), mas não será necessário resultado.')
a = 15
b = 15
c = a + b
print (c)

print ('no entanto, também é possivel dividir (/), multiplicar (*) e subtrair (-)')
a = 15
b = 15
c = a * b
print (c)

a = 15
b = 15
c = a / b
print (c)

a = 15
b = 15
c = a - b
print (c)

print ('e além destas variaveis numéricas, como já devem ter percebido, também é possivel declarar variáveis escritas, por exemplo:')
print ('a variável "pai" irá declarar o resultado "Irineu", variável "mãe" o resultado "Karina", variável "filho" o resultado "Mateus" e "filha" o resultado "Maria"')
pai = "Irine"
mãe = "Kariana"
filho = "Mateus"
filha = "Maria"
print (pai)
print (mãe)
print (filho)
print (filha)

print ('mas também é possivel executalas como uma unica variável, podendo denominar de variável "família"')
pai = "Irineu"
mãe = "Kariana"
filho = "Mateus"
filha = "Maria"
família = pai, mãe, filho, filha
print (família)

print ('Uma função um pouco mais complexa é a "if", que assim como muitas, derivado do inglês, significa "se", ou seja, no caso de alguma ocorrencia fora do padrão definino, o "if" será usado; por exemplo')
print ('no exemplo da função anterior, foi usado as variantes "pai", "mãe", "filho", "filha" e para mostrar seus resultados (no caso o nome de cada membro da familia) foi emitida a variavel "família". Agora se eu pegar a variável "pai" e pedir para que seja emitida a mensagem afirmando que o resultado de "pai" está correto, será emitida')
if pai == 'Irineu':
    print ("Esta afirmativa está correta. O nome de 'pai' é", pai)
    
print ('mas e se no caso não fosse este o nome, se o nome fosse outro, neste cenário adicionariamos o "else" (do inglês significa "outra") para se acrecentar uma nova vertente; exemplo:')

if pai == filho:
    print ("Esta afirmativa está correta. O nome de Irineu é o nome do pai")
else:
    print("Esta afirmativa é incorreta. Mateus é o nome do filho")
    
print ('e o que mostra para o computador que a afirmativa é verdadeira são os iguais juntos "==" significando verdadeiro, então se eu dicer "pai" == "Irineu", o resultado é verdadeiro, porém se for "pai" == "filho", o resultado será falso e como eu pedi para emitir uma mensagem, ele irá mostrar a mensagem que desejei.')

print ('Agora a pergunta que não quer se calar, quando é que eu vou interagir com o meu próprio programa? Como permito a interação do usuário com aquilo que está na tela?')
print ('E por incrivel que pareça, isto é mais simples doque imagina, mas vamos continuar no básico ok?')
print ('Bem, quando se trata de um texto, já pegando de exemplo o Google, que alem de exibição de texto, também depende daquilo que o usuário digita na área de comando, pode ter certeza que ali tem um "input"; "input" não é nada mais nada menos um campo de digitação do usuário, por exemplo:')

criador = "Mateus Zanin"
criador - input ("Qual nome do criador deste texto?")