alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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
    if col not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or not isinstance(lin, int):
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

#TAD parcela

def cria_parcela():
    return ['#', False]

def cria_copia_parcela(p):
    return p.copy()

def limpa_parcela(p):
    if p[1] == False:
        p[0] = '?'
        return p
    if p[1] == True:
        p[0] = 'X'
        return p

def marca_parcela(p):
    p[0] = '@'
    return p

def desmarca_parcela(p):
    p[0] = '#'
    return p

def esconde_mina(p):
    p[1] = True
    return p

def eh_parcela(p):
    if isinstance(p, list) and len(p) == 2:
        return True
    else:
        return False

def eh_parcela_tapada(p):
    if p[0] == '#' and eh_parcela(p):
        return True
    else:
        return False

def eh_parcela_marcada(p):
    if p[0] == '@' and eh_parcela(p):
        return True
    else:
        return False

def eh_parcela_limpa(p):
    if p[0] == '?' and eh_parcela(p):
        return True
    else:
        return False

def eh_parcela_minada(p):
    if p[1] and eh_parcela(p):
        return True
    else:
        return False

def parcelas_iguais(p1, p2):
    if eh_parcela(p1) and eh_parcela(p2):
        if p1[0] == p2[0] and p1[1] == p2[1]:
            return True
    else:
        return False

def parcela_para_str(p):
    return p[0]

def alterna_bandeira(p):
    if p[0] == '@':
        p[0] = '#'
        return True
    if p[0] == '#':
        p[0] = '@'
        return True
    return False

#TAD CAMPO

def cria_campo(c, l):
    if not isinstance(c, str) or not isinstance(l, int):
        return ValueError('cria_campo: argumentos invalidos')
    if len(c) != 1 :
        return ValueError('cria_campo: argumentos invalidos')
    if l not in range(1, 100):
        return ValueError('cria_campo: argumentos invalidos')
    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    campo = []
    i = 0
    campoFinal = []
    for i in range(l):
        campo += [[cria_parcela() for j in range(alf.index(c)+1)]]


    return campo

def copia_campo(m):
    return m.copy()

def obtem_ultima_coluna(m):
    return alf[(len(m[-1]) - 1)]

def obtem_ultima_linha(m):
    return len(m)

def obtem_parcela(m,c):
    return m[obtem_linha(c) - 1][alf.index(obtem_coluna(c))]

def obtem_coordenadas(m, s):
    coords = []
    if s == 'limpas':
        for i in range(len(m)):
            for j in range(len(m[i])):
                if eh_parcela_limpa(m[i][j]):
                    coords.append((alf[j], i + 1))
    if s == 'tapada':
        for i in range(len(m)):
            for j in range(len(m[i])):
                if eh_parcela_tapada(m[i][j]):
                    coords.append((alf[j], i+1))
    if s == 'marcada':
        for i in range(len(m)):
            for j in range(len(m[i])):
                if eh_parcela_marcada(m[i][j]):
                    coords.append((alf[j], i+1))
    if s == 'minadas':
        for i in range(len(m)):
            for j in range(len(m[i])):
                if eh_parcela_minada(m[i][j]):
                    coords.append((alf[j], i+1))
    return tuple(coords)

def obtem_numero_minas_vizinhas(m, c):
    minas = 0
    for i in obtem_coordenadas_vizinhas(c):
        if eh_coordenada_do_campo(m,i ) and eh_parcela_minada(obtem_parcela(m, i)) :
            minas += 1

    return minas


def eh_campo(m):
    if not isinstance(m, list):
        return False
    for i in m:
        if not isinstance(i,list):
            return False
        for j in i:
            if not eh_parcela(j):
                return False
    else:
        return True

def eh_coordenada_do_campo(m, c):
    if c[0] not in alf[:alf.index(obtem_ultima_coluna(m))] or c[1] not in range(obtem_ultima_linha(m)):
        return False
    else:
        return True

def campos_iguais(m1,m2):
    if len(m1) != len(m2):
        return False
    if not isinstance(m1, list) or not isinstance(m2, list):
        return False
    for i in range(len(m1)):
        if not isinstance(m1[i], list) or not isinstance(m2[i], list):
            return False
        if m1[i] != m2[i]:
            return False
        for k in range(m1[i]):
            if m1[i][k] != m[i][k]:
                return False
    return True

def campo_para_str(m):
    campo = '   '
    for i in range(alf.index(obtem_ultima_coluna(m))+1):
        campo += alf[i]
    campo += '\n  +'
    for i in range(alf.index(obtem_ultima_coluna(m))+1):
        campo += '-'
    campo += '+'

    for i in range(obtem_ultima_linha(m)):  # N LINHAS
        if i + 1 < 10:
            campo += '\n0' + str(i + 1) + '|'
        elif i + 1 >= 10:
            campo += '\n' + str(i + 1) + '|'
        for j in range(len(m[i])):
            if parcela_para_str(m[i][j]) == '?':
                if obtem_numero_minas_vizinhas(m, (str(alf[j]), i + 1)) == 0:
                    campo += ' '
                elif obtem_numero_minas_vizinhas(m, (alf[j],i +1 )) != 0:
                    campo += str(obtem_numero_minas_vizinhas(m, (alf[j],i +1 )))
            else:
                campo += parcela_para_str(m[i][j])
        campo += '|'

    campo += '\n  +'
    for i in range(alf.index(obtem_ultima_coluna(m))+1):
        campo += '-'
    campo += '+'
    return campo

def coloca_minas(m, c, g, n):
    coordsOcupados = []
    while len(obtem_coordenadas(m, 'minadas')) < n:
        coordAleatoria = obtem_coordenada_aleatoria(((obtem_ultima_coluna(m), obtem_ultima_linha(m))), g)
        if coordAleatoria not in obtem_coordenadas_vizinhas(c) or coordAleatoria != c or coordAleatoria not in coordsOcupados:
            m[obtem_linha(coordAleatoria)][obtem_coluna(coordAleatoria)][1] = True
            coordsOcupados += coordAleatoria
    return m

def limpa_campo(m, c):
    p = obtem_parcela(m,c)
    if eh_parcela_limpa(p):
        return m
    limpa_parcela(p)
    if parcela_para_str(p) == 'X':
        return m
    if obtem_numero_minas_vizinhas(m,c) == 0:
        for i in obtem_coordenadas_vizinhas(c):
            if eh_coordenada_do_campo(m, i) and eh_parcela_tapada(obtem_parcela(m,i)):
                limpa_parcela(obtem_parcela(m,i))
            else:
                limpa_campo(m,i)
    return m


m = cria_campo('E', 5)

for l in 'ABC': esconde_mina(obtem_parcela(m, cria_coordenada(l, 1)))
for l in 'BC': esconde_mina(obtem_parcela(m, cria_coordenada(l, 2)))
for l in 'DE': limpa_parcela(obtem_parcela(m, cria_coordenada(l, 1)))
for l in 'AD': limpa_parcela(obtem_parcela(m, cria_coordenada(l, 2)))
for l in 'ABCDE': limpa_parcela(obtem_parcela(m, cria_coordenada(l, 3)))

alterna_bandeira(obtem_parcela(m, cria_coordenada('D', 4)))
esconde_mina(obtem_parcela(m,('D',1)))
print(obtem_parcela(m, ('D',1)))
print(eh_parcela_minada(obtem_parcela(m, ('D',1))))
print(eh_coordenada_do_campo(m,('D', 1)))
print(obtem_numero_minas_vizinhas(m, ('D', 1)))
print(campo_para_str(m))