#TAD gerador

def cria_gerador(b, s):
    if not isinstance(b, int) or not isinstance(s, int):
        raise ValueError('cria_gerador: argumentos invalidos')
    if not b in (32, 64):
        raise ValueError('cria_gerador: argumentos invalidos')
    if not s > 0:
        raise ValueError('cria_gerador: argumentos invalidos')
    return [b, s]


def cria_copia_gerador(g):
    copia = g.copy()
    return copia


def obtem_estado(g):
    return g[1]


def define_estado(g, n):
    g[1] = n
    return g[1]

def xorshift(b, s):
    if b == 32:
        s ^= (s << 13) & 0xFFFFFFFF
        s ^= (s >> 17) & 0xFFFFFFFF
        s ^= (s << 5) & 0xFFFFFFFF
    if b == 64:
        s ^= (s << 13) & 0xFFFFFFFFFFFFFFFF
        s ^= (s >> 7) & 0xFFFFFFFFFFFFFFFF
        s ^= (s << 17) & 0xFFFFFFFFFFFFFFFF
    return s

def atualiza_estado(g):
    g[1] = xorshift(g[0], g[1])
    return g[1]

def eh_gerador(g):
    if len(g) == 2 and g[0] in (32, 64) and isinstance(g[1], int) and g[1] > 0:
        return True
    else:
        return False

def geradores_iguais(g1, g2):
    if g1[0] == g2[0] and g1[1] == g2[1]:
        return True
    else:
        return False

def gerador_para_str(g):
    return 'xorshift' + str(g[0]) + '(s=' + str(g[1]) + ')'

def mod(n1, n2):
    return n1 % n2

def gera_numero_aleatorio(g, n):
    return 1 + mod(atualiza_estado(g), n)

def gera_string(l):
    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alf[:alf.index(l)]

def gera_carater_aleatorio(g, n):
    return gera_string(n)[mod(atualiza_estado(g), len(gera_string(n))+1)]

#TAD coordenada
def cria_coordenada(col, lin):
    if not isinstance(col, str) or not isinstance(lin, int):
        raise ValueError('cria_coordenada: argumentos invalidos')
    if not lin in range(1, 99) or not col.isupper():
        raise ValueError('cria_coordenada: argumentos invalidos')
    return (col,lin)

def obtem_coluna(c):
    return c[0]

def obtem_linha(c):
    return c[1]

def eh_coordenada(c):
    if type(c) != tuple:
        return False
    elif type(c[0]) != str or type(c[1]) not in range(1,99):
        return False
    else:
        return True


g2 = cria_gerador(64, 1)
[atualiza_estado(g2) for n in range(5)]

print(gera_carater_aleatorio(g2, 'Z'))