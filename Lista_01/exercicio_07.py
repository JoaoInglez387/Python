def hora_mm(tempo):
    
    horas = tempo.split(':')[0]
    minutos = tempo.split(':')[1]
    
    try:
        horas = int(horas)
    except:
        return 'Erro! As horas contém alguma letra'

    try:
        minutos = int(minutos)
    except:
        return 'Erro! Os minutos contém alguma letra'
    
    if horas == 00:
        return f'São Meia noite'
    elif horas == 1:
        return f'São {horas} hora'
    
    
    if minutos == 0 or minutos == 1:
        return f'São {horas} horas e {minutos} minuto'
    else:
        return f'São {horas} horas e {minutos} minutos'
   
print(hora_mm(input('Digite sua hora: ')))