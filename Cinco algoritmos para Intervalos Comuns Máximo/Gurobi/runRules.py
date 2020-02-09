import sys
sys.path.insert(0, '../gurobi') 
from calculaL import calculaL
import time 

# RULE 1:
# a parte de remover os intervalos comuns de tamanho 1 ja foi feita la em cima
def runRule1(C, X, m, genomeA, genomeB):
    print 'Rodando Rule1'
    print 'Tamanho previo de C:', len(C)

    startTime = time.time()

    lenGA, lenGB = len(genomeA), len(genomeB)

    # Create lisoftuples that will be removed
    listOfTuples = [(i,j,k,l) for i in range(lenGA) for j in range(i, lenGA) for k in range(lenGB) for l in range(k,lenGB) if i == j and k == l]
    
    m.update()
    for cijkl in listOfTuples:
        #print C[cijkl]
        m.remove(C[cijkl])
        del C[cijkl]

    numberToBeAdded = calculaL(genomeA, genomeB)
    print 'Tamanho posterior de C: %d, numAdded: %d' % (len(C), numberToBeAdded)

    return time.time()-startTime, numberToBeAdded

def runRule2(C, X, m):
    print 'Rodando Rule2'
    print 'Tamanho previo de C:', len(C)

    start = time.time()
    m.update()
    lista = []
    for cijkl in C:
        i = cijkl[0]; j = cijkl[1]; k = cijkl[2]; l = cijkl[3]
        lisk = [val1 for val1 in range(i,j+1)]
        lisi = [val for val in range(k,l+1)]

        # r2 significa que eh a implementacao da rule 2

        # parte 1 da RULE 2
        rule2 = X.select(lisk[0], lisi)
        rul2 = X.select(lisk[len(lisk)-1], lisi)
        if len(rule2) == 0 or len(rul2) == 0:
            lista.append(cijkl)
            continue

        # parte 3 da RULE 2
        rule2 = X.select(lisk, lisi[0])
        rul2 = X.select(lisk, lisi[len(lisi)-1])
        if len(rule2) == 0 or len(rul2) == 0:
            lista.append(cijkl)
            continue

    m.update()
    for cijkl in lista:
        m.remove(C[cijkl])
        del C[cijkl]

    print 'Tamanho posterior de C:', len(C)

    end = time.time()
    return end - start

def occ(char, lis, string):
    count = 0
    for x in lis:
        if char == string(x):
            count = count + 1
    return count

def find(lista, genoma, gene):
    for x in lista:
        if gene == genoma[x]:
            return x

def runRule3(C, X, m, ga, gb):
    print 'Rodando Rule3'
    print 'Tamanho de previo de C:', len(C)

    start = time.time()
    m.update()
    lista = []

    for cijkl in C:

        i = cijkl[0]; j = cijkl[1]; k = cijkl[2]; l = cijkl[3]
        lisk = [val1 for val1 in range(i,j+1)]
        lisi = [val for val in range(k,l+1)]
        lisga = [val for val in range(len(ga))]
        lisgb = [val for val in range(len(gb))]

        verified = []
        for element in lisk:
            g = ga[element]
            #print g, verified
            if g in verified or cijkl in lista:
                continue
            #print 'passei o continue'
            pos = find(lisi, gb, g)
            occ1 = len(X.select(lisk, pos))
            occ2 = len(X.select(element, lisi))
            occga = len(X.select(lisga, pos))
            occgb = len(X.select(element, lisgb))
            verified.append(g)

            if abs(occ1 - occ2) > abs(occga - occgb):
                lista.append(cijkl)
                break

    m.update()
    for cijkl in lista:
        m.remove(C[cijkl])
        del C[cijkl]

    print 'Tamanho posterior de C:', len(C)

    end = time.time()
    return end - start

def getFamilies(genome, i, j):
    fmly = []
    for x in range(i, j+1):
        if genome[x] not in fmly:
            fmly.append(genome[x])

    return fmly


def part1(familiesij, X, lisi, lisj, lisgb, gb):
    # Prop1 vou conseguir a occ1(cada gene) pra isso vou fazer um truque
    ##print 'entrei em part1, familiesij:', familiesij
    for gene in familiesij:            
        # find() encontra a posicao de 'gene' no genomaB (gb)
        posInGB = find(lisgb, gb, gene)
        part1Prop1 = len(X.select(lisi, posInGB))
        part2Prop1 = len(X.select(lisj, posInGB))

       # print 'p1p1', part1Prop1, 'p2p1', part2Prop1

        if part1Prop1 + part2Prop1 == 0:
            continue
        else:
            #print 'vou retornar 0 do part1'
            return 0

##    print 'vou retornar 1 do part1'
    return 1

def part2(familieskl, X, lisk, lisl, lisga, ga):
    #print 'entrei em part2, familieskl:', familieskl
    # Prop1 vou descolar a occ1(cada gene) pra isso vou fazer um truque
    for gene in familieskl:            
        posInGA = find(lisga, ga, gene)
        part1Prop2 = len(X.select(posInGA, lisk))
        part2Prop2 = len(X.select(posInGA, lisl))

        if part1Prop2 + part2Prop2 == 0:
            continue
        else:
            #print 'vou retornar 0 do partq'
            return 0

    #print 'vou retornar 1 do part2'
    return 1

def part3(X, lisgb, gb, lisga, ga, genei, genej):
    #print 'to no part3, genei:', genei, 'genej:', genej
    posInGB = find(lisgb, gb, genei)
    occ1 = len(X.select(lisga, posInGB))

    posInGA = find(lisga, ga, genei)
    occ2 = len(X.select(posInGA, lisgb))

    if occ1 > occ2:
        #print 'vou retornar 0 do part3 na primeira parte'
        return 0

    posInGB = find(lisgb, gb, genej)
    occ1 = len(X.select(lisga, posInGB))

    posInGA = find(lisga, ga, genej)
    occ2 = len(X.select(posInGA, lisgb))

    if occ1 > occ2:
        #print 'vou retornar 0 do part3, na segunda parte'
        return 0
    else:
        #print 'vou retornar 1 do part3'
        return 1

def part4(X, lisgb, gb, lisga, ga, genek, genel):
    #print 'to no part4, genek:', genek, 'genel', genel
    posInGB = find(lisgb, gb, genek)
    occ1 = len(X.select(lisga, posInGB))

    posInGA = find(lisga, ga, genek)
    occ2 = len(X.select(posInGA, lisgb))

    if occ1 < occ2:
        #print 'vou retornar 0 do part4 na primeira parte'
        return 0

    posInGB = find(lisgb, gb, genel)
    occ1 = len(X.select(lisga, posInGB))

    posInGA = find(lisga, ga, genel)
    occ2 = len(X.select(posInGA, lisgb))

    if occ1 < occ2:
        #print 'vou retornar 0 do part4 na segunda parte'
        return 0
    else:
        #print 'vou retornar 1 do part4'
        return 1

# a regra 4 nunca sera utilizada pois ela esta errada e eu acredito muito nisso!
def runRule4(C, X, m, ga, gb):
    print 'Rodando Rule4'
    print 'Tamanho previo de C:', len(C)

    start = time.time()
    m.update()
    lista = []
    for cijkl in C:

        i = cijkl[0]; j = cijkl[1]; k = cijkl[2]; l = cijkl[3]

        lisi = [val for val in range(i)]
        lisj = [val for val in range(j+1, len(ga))]
        lisk = [val for val in range(k)]
        lisl = [val for val in range(l+1, len(gb))]
        lisga = [val for val in range(len(ga))]
        lisgb = [val for val in range(len(gb))]

        familiesij = getFamilies(ga, i, j)
        familieskl = getFamilies(gb, k, l)
        #print 'cijkl:', cijkl
    
        prop1 = part1(familiesij, X, lisi, lisj, lisgb, gb)
        if prop1 != 1:
            continue

        prop2 = part2(familieskl, X, lisk, lisl, lisga, ga)
        if prop2 != 1:
            continue

        prop3 = part3(X, lisgb, gb, lisga, ga, ga[i], ga[j])
        if prop3 != 1:
            continue

        prop4 = part4(X, lisgb, gb, lisga, ga, gb[k], gb[l])
        if prop4 != 1:
            continue

        lista.append(cijkl)

    m.update()
    #print C
    count = 0
    for cijkl in lista:
        #print 'vou remover:', cijkl
        m.remove(C[cijkl])
        del C[cijkl]
        count += 1

    print 'Tamanho posterior de C:', len(C)

    end = time.time()
    return end - start, count