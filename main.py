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

def cria_campo(c, l):
    if not isinstance(c, str) or not isinstance(l, int):
        return ValueError('cria_campo: argumentos invalidos')
    if len(c) != 1 :
        return ValueError('cria_campo: argumentos invalidos')
    if l not in range(1, 100):
        return ValueError('cria_campo: argumentos invalidos')
    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    campo = {alf[i]:[] for i in range(alf.index(c)+1)}
    for i in range(len(campo)):
        for j in range(1,l+1):
            campo[list(campo.keys())[i]].append(cria_parcela())
    return campo

def copia_campo(m):
    return m.copy()

def obtem_ultima_coluna(m):
    return list(m.values())[-1]

def obtem_ultima_linha(m):
    return list(m[i][-1] for i in m.keys())

def obtem_parcela(m,c):
    return m[c[0]][c[1]-1]

def obtem_coordenadas(m,s):
    if s == 'limpas':
        q = '?'
    if s == 'tapadas':
        q = '#'
    if s == 'marcadas':
        q = '@'
    if s == 'minadas':
        q = True
    coord = []
    if q in '?#Q':
        for i,j in m.items():
            for k in range(len(j)):
                if j[k][0] == q:
                    coord.append([i, k+1])
    if q == True:
        for i,j in m.items():
            for k in range(len(j)):
                if j[k][1] == q:
                    coord.append([i, k+1])
    return tuple(coord)

def obtem_numero_minas_vizinhas(m,c):
    viz = list(obtem_coordenadas_vizinhas(c))
    i = 0
    while i < len(viz):
        if viz[i][0] not in list(m.keys()) or viz[i][1] not in range(1,len(m[list(m.keys())[0]])+1):
            viz.remove(viz[i])
        else:
            i += 1
    minas = 0
    for i in range(len(viz)):
        if m[viz[i][0]][viz[i][1]-1] == True:
            minas += 1
    return minas

def eh_campo(c):
    if not isinstance(c, dict):
        return False
    for k,v in c.values():
        if not isinstance(k, str) or not isinstance(v, list):
            return False
    else:
        return True

def eh_coordenada_do_campo(m,c):
    if c[0] in list(m.keys()) and c[1] in range(1, len(m[list(m.keys())[0]]) + 1):
        return True
    else:
        return False

def eh_campos_iguais(m1, m2):
    if m1.items() == m2.items():
        return True
    else:
        return False

def campo_para_str(m):
    campo = '   '
    for i in range(len(m.keys())):
        campo += str(list(m.keys())[i])
    campo += '\n  +'
    for i in range(len(m.keys())):
        campo += '-'
    campo += '+'

    for i in range(len(m[list(m.keys())[0]])): #RANGE LINHAS
        campo += '\n0' + str(i+1) + '|'
        for j in range(len(list(m.keys()))):

            campo += str(m[list(m.keys())[j]][i][0])
        campo += '|'

    campo += '\n  +'
    for i in range(len(m.keys())):
        campo += '-'
    campo += '+'
    return campo

def coloca_minas(m, c, g, n):
    return

'''def limpa_campo(m,c):
    if m[c[0]][c[1]-1][0] == '?':
        return m
    elif m[c[0]][c[1]-1][0] == '#':
        limpa_parcela(m[c[0]][c[1]-1])
    if obtem_numero_minas_vizinhas(m,c) == 0:
        for i in range(len(obtem_coordenadas_vizinhas(c))):
            limpa_parcela(m[obtem_coordenadas_vizinhas(c)[i][0]][obtem_coordenadas_vizinhas(c)[i][1]])



        return m'''

m = cria_campo('E',5)

for l in 'ABC':esconde_mina(obtem_parcela(m, cria_coordenada(l,1)))
for l in 'BC':esconde_mina(obtem_parcela(m, cria_coordenada(l,2)))
for l in 'DE':limpa_parcela(obtem_parcela(m, cria_coordenada(l,1)))
for l in 'AD':limpa_parcela(obtem_parcela(m, cria_coordenada(l,2)))
for l in 'ABCDE':limpa_parcela(obtem_parcela(m, cria_coordenada(l,3)))

alterna_bandeira(obtem_parcela(m, cria_coordenada('D',4)))
print(campo_para_str(m))