def conta(num):
    return len(num)

print(conta(input('Digite um número: ')))

#---------------------------------------------------------------
def conta(num: int):
    return len((str(num)))

print(conta(input('Digite um número: ')))