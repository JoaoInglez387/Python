while True:
    try:
        N = int(input())
        
    except EOFError:
        break
    
    for i in range(N):
        ab = input().split()
        
        if ab[0][-len(ab[1]):] == ab[1]:
            print('encaixa')
        else:
            print('nao encaixa')
