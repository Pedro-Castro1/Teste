def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos_no_intervalo(inicio, fim):
    return [num for num in range(inicio, fim + 1) if eh_primo(num)]

inicio = 10
fim = 100
print(f'Números primos entre {inicio} e {fim}:', primos_no_intervalo(inicio, fim))
print ('commit 111')