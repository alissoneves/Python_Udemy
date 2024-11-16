
def multiplica(*args):
    total = 1
    for numero in args: 
        total *= numero
    return total 
  
multiplicador = multiplica(1811, 11, 3)
print (f'Valor da multiplicação: {multiplicador}')

def par_impar(multiplicador): 

    Multiplo_de_Dois = multiplicador % 2 == 0 

    if Multiplo_de_Dois:
        
        return f'O número: {multiplicador} é par'
        
    return f'O número: {multiplicador} é impar'

print (par_impar(multiplicador)) 


