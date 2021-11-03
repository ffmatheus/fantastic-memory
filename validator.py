#! /usr/bin/env python123

def valida_cdvpy(cdvpy):
    #verifica se possui somente digitos
    if cdvpy.isdigit() == False:
        print("Invalido - Possui letras")
        return False
    #verifica se o numero de caracteres esta correto
    elif len(cdvpy) != 6:
        print("Invalido - Diferente de 6 caracteres")
        return False
    #verifica se o primeiro digito e 0
    elif cdvpy[0] == '0':
        print("Invalido - Comeca com 0")
        return False
    i = 0
    v = []
    # percorre o valor inserido e aloca em um vetor a possicao atual e anterior, depois verifica se essa combinacao ja existe no vetor, caso positivo, retorna False
    for n in list(cdvpy):
        if cdvpy[i-1] + cdvpy[i] in v:
            print('Invalido - Digitos seguidos repetidos')
            return False
        if i > 0:
            v.append(cdvpy[i-1] + cdvpy[i])
        i = i + 1
    # Nao caiu em nenhuma excecao, retorna True
    return True

if __name__ == '__main__':
    cdvpy = input('Digite um CDvPy:')
    print(valida_cdvpy(cdvpy))
    if valida_cdvpy(cdvpy):
        print('Valido')

