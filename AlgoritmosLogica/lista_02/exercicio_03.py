
nm_time1 = input('Digite nome do time: ')
gols_1 = int(input('Número de gol: '))
nm_time2 = input('Digite nome time: ')
gols_2 = int(input('Número de gol: '))
if gols_1 > gols_2:
    print(f'O time {nm_time1} foi o vencedor\
        \nResultado: {gols_1} X {gols_2}')
elif gols_1 < gols_2:
    print(f'O time {nm_time2} foi o vencedor\
        \nResultado: {gols_1} X {gols_2}')
else:
    print(f'EMPATE \n{gols_1} X {gols_2}')