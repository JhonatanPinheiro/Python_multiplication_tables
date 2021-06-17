#Faça um programa que leia um número inteiro qualquer e monstre na tela a sua tabuada 

inputNumber = int(input('Enter the number of times tables you want to know: ')) 

multNumber = inputNumber
varNumber = 0
result = 0

print('\n-- Start-- \n')

while varNumber < 1000:
    varNumber+=1
    result = (varNumber * multNumber)
    print('{0} x {1} = {2}'.format(multNumber,varNumber,result))
else:
    print('\n-- End --')
    