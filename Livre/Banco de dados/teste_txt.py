valores_celulares = [850, 2230, 1500, 3500, 5000]

''' 
'W'  = Usado somente para escrever algo
'''

#with open('valores_celulares.txt','w') as arquivo:
   # for valor in valores_celulares:
       # arquivo.write(str(valor) + '\n')'''
        
'''
'a'  = Usando para acrescentar algo 
'''

with open('valores_celulares.txt','a') as arquivo:
    for valor in valores_celulares:
        arquivo.write(str(valor) + '\n')
        
'''
'r' = Usado para somente ler algo 
'''

#with open('valores_celulares.txt','r') as arquivo:
    #for valor in valores_celulares:
        #print(valor)

#with open('valores_celulares.txt','r') as arquivo:
    #for valor in arquivo:
        #print(valor)
        
''' 
'r+' = Usado para ler e escreve algo
'''

#with open('valores_celulares.txt','r+') as arquivo:
    #for valor in arquivo:
        #print(valor)
    #arquivo.write('9000')