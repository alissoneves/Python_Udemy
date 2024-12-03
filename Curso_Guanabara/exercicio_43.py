peso = float(input('Digite o primeiro o seu peso: '))
altura = float(input('Digite agora a sua altura: '))

base1 = altura * altura
imc = peso / base1

if imc <= 18.5: 
    
    print (f'Seu IMC é no valor de: {imc:.1f}, você está ABAIXO DO PESO!')

elif imc > 18.5 and imc < 25: 
    
    print (f'Seu IMC é no valor de: {imc:.1f}, você está PESO IDEAL!')

elif imc > 25 and imc < 30: 
    
    print (f'Seu IMC é no valor de: {imc:.1f}, você está SOBREPESO!')  

elif imc > 30 and imc < 40: 
    
    print (f'Seu IMC é no valor de: {imc:.1f}, você está OBESIDADE!')  

elif imc >= 40:
    
    print (f'Seu IMC é no valor de: {imc:.1f}, você está OBESIDADE MÓRBIDA!')                  