n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é:{} \n o Produto é {} \n A divisão é {:.3f} '.format(s,m,d), end ='')
print('A divisao inteira é {} e a potência é:{}' .format(di, e))
