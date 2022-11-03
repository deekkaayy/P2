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
    if not lin in range(1, 100) or not col.isupper():
        raise ValueError('cria_coordenada: argumentos invalidos')
    return (col,lin)

def obtem_coluna(c):
    return c[0]

def obtem_linha(c):
    return c[1]

def eh_coordenada(c):
    if type(c) != tuple:
        return False
    elif c[0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or c[1] not in range(1,100):
        return False
    else:
        return True

def coordenadas_iguais(c1, c2):
    if c1[0] == c2[0] and c1[1] == c2[1]:
        return True
    else:
        return False

def coordenada_para_str(c):
    if c[1] < 10:
        return str(c[0]) + '0' + str(c[1])
    else:
        return str(c[0]) + str(c[1])

def str_para_coordenada(s):
    g = []
    if len(s) == 2:
        g.append(s[0])
        g.append(s[1])
    if len(s) == 3:
        g.append(s[0])
        g.append(s[1:])
    return tuple(g)




def obtem_coordenadas_vizinhas(c):
    viz = []
    x = [-1, 0, 1, 1, 1, 0, -1, -1]
    y = [-1, -1, -1, 0, 1, 1, 1, 0]
    for i in range(8):
        cTemp = list(c)
        cTemp[0] = chr(ord(cTemp[0]) + x[i])
        cTemp[1] = cTemp[1] + y[i]
        if eh_coordenada(tuple(cTemp)):
            viz.append(tuple(cTemp))
    return tuple(viz)

def obtem_coordenada_aleatoria(c, g):
    return [gera_carater_aleatorio(g, c[0]), gera_numero_aleatorio(g, c[1])]



g1 = cria_gerador(32, 1)
c3 = cria_coordenada('Z', 99)
print(obtem_coordenada_aleatoria(c3, g1))