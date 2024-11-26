def numero_rever(num_rever):
    
    num_rever = list(num_rever)
    num_rever.reverse()
    return ''.join(num_rever)
    
print(numero_rever(input('Digite um número: ')))

#------------------------------------------------------------

def numero_rever(num_rever):
    
    num_rever = str(num_rever)
    num_invert = num_rever[::-1]

    return num_invert
    
print(numero_rever(input('Digite um número: ')))