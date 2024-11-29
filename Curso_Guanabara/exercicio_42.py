r1 = float(input('Digite o primeiro segmento do seu triângulo: '))
r2 = float(input('Digite o segundo segmento do seu triângulo: '))
r3 = float(input('Digite o terceiro segmento do seu triângulo: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('Os segmentos acima PODEM FORMAR um triângulo!')
    if r1 == r2 == r3: 
        print ('Esse triângulo é EQUILÁTERO!')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1: 
        print ('Esse triângulo é ISÓCELES!')
    elif r1 != r2 != r3 or r1 != r3 != r2 or r2 != r3 != r1:    
         print ('Esse triângulo é ESCALENO!')
else:    
    print ('Os segmentos acima NÃO PODEM FORMAR um triânguloo!')