#!/usr/bin/python

# Copyright 2018, Gurobi Optimization, LLC

# This program implements the ILP Program Common-Intervals-Matching
# under the maximum matching model
# as studied in the article 
# A Pseudo-Boolean Framework for Computing Rearrangement Distances
# between Genomes with Duplicates

from gurobipy import *
import sys
sys.path.insert(0, '../gurobi')
import time
from datetime import datetime 
from calculaL import calculaL
import os
from runRules import *

try:
    # Create a new model
    m = Model("mip1")

    #current directory
    curDir = os.getcwd()
    paths = curDir.split('/')
    
    #------- Bind input file --------#
    '''inputPath = '/'.join(paths[:-1]) + '/genomasDeInput/'
    inputName = sys.argv[1]
    pathToInput = inputPath+inputName'''

    pathToInput = sys.argv[1]    
    myInputfile = open(pathToInput, 'r')
    inputName = sys.argv[1].split('/')[-1]

    #------- Bind file for Output --------#
    if 'isHeu' not in sys.argv:
        pathToOutput = os.getcwd().replace('gurobi', '/saidas/gurobiSaidas/%s_quadro_gurobi' % inputName)
        outputPath = pathToOutput.replace('%s_quadro_gurobi' % inputName, '')
        myoutFile = open(pathToOutput, 'w')

    else:
        #print 'isHeu esta'
        if len(sys.argv) != 7:
            print 'sys.argv size nao pode ser diferente de 7, abortando...'
            exit()
        else:
            # sys.argv deve estar assim: ['nome', 'pathToInput','1', '2', '3', 'isHeu', 'pathToOutput']
            # caso contrario aborte!
           
            pathToOutput = sys.argv[6]
            outputPath = '/'.join(pathToOutput.split('/')[:-1])+'/'
            myoutFile = open(sys.argv[6]+'_quadro_gurobi', 'w')

    #------- Executing process ---------#
    # Read genome sequences
    genomeA = myInputfile.readline().rstrip('\n').split()
    genomeB = myInputfile.readline().rstrip('\n').split()

    a = ' '.join(genomeA)
    b = ' '.join(genomeB)

    #myoutFile.write('input name: %s\n\n' % inputName)
    myoutFile.write(a+'\n')
    myoutFile.write(b+'\n\n')

    print(type(genomeA), genomeA, genomeB, inputName,'a')

    lenGA = len(genomeA)
    lenGB = len(genomeB)

    # Create Variables Cijkl
    listOfTuples = [(i,j,k,l) for i in range(lenGA) for j in range(i, lenGA) for k in range(lenGB) for l in range(k,lenGB)]
    C = m.addVars(listOfTuples, vtype = GRB.BINARY, name='c')
    
    # TA AQUIIIIII if i != j and k != l
    
    # Create Variables Xik
    varList = [(i,k) for i in range(lenGA) for k in range(lenGB) if genomeA[i] == genomeB[k]]
    X = m.addVars(varList, vtype = GRB.BINARY, name='x')

    # MARKER: Neste ponto todas as Variaveis ja foram definidas

    # Seguem implementacoes de 4 regras para se melhorar o tempo de computacao atravez da estrategia de
    # se diminuir o numero de variaveis e constraints

    print C[(0,1,0,1)].varName
    # RULE 1: Descartar intervalos comuns de tamanho 1. Podemos computar em um passo de pre-processamento o numero d1 e d2
    # de genes que precisam ser deletados em G1 e G2 para se obter o maximum matching entre os genomas.
    # Portanto, sabemos que os genomas resultantes consistirao de L = n1 - d1 = n2 - d2 genes onde
    # L = somatorio do minimo da ocorrencia de cada gene em G1 e G2

    if '1' in sys.argv:
        timeOfRule1, numberToBeAdded = runRule1(C, X, m, genomeA, genomeB)
        PartialResult = numberToBeAdded
    else:
        timeOfRule1 = 0.0

    print('o tamanho de C antes da regra 2 eh:', len(C))
    
    # RULE 2: Deletar de C todas as variaveis cijkl para as quais as condicoes de borda nao valem
    if '2' in sys.argv:
        timeOfRule2 = runRule2(C, X, m)
    else:
        timeOfRule2 = 0.0

    print('o tamanho de C depois da regra 2 eh:', len(C))

    if '3' in sys.argv:
        timeOfRule3 = runRule3(C, X, m, genomeA, genomeB)
    else:
        timeOfRule3 = 0.0

    if '4' in sys.argv:
        timeOfRule4, numberToBeAdded = runRule4(C, X, m, genomeA, genomeB)
        PartialResult += numberToBeAdded
    else:
        timeOfRule4 = 0.0

    # Set objective
    m.setObjective(C.sum(), GRB.MAXIMIZE)

    # Add constraints: C.01
    m.addConstrs((X.sum(i, "*") <= 1 for i in range(lenGA)), "C.01")
    
    # Add constraints: C.02
    m.addConstrs((X.sum("*", j) <= 1 for j in range(lenGB)), "C.02")
    #print C

    # Add constraints: C.03
    for cijkl in C:
       # print 'running c.03'
        i, j, k, l = cijkl #cijkl eh uma tupla
        a = 4*C[cijkl]
        lisk = [val1 for val1 in range(i,j+1)]
        lisi = [val for val in range(k,l+1)]
        b = X.sum(i, lisi)
        c = X.sum(j, lisi)
        d = X.sum(lisk, k)
        e = X.sum(lisk, l)
        m.addConstr(a - b - c - d - e <= 0, "C.03.c["+str(i)+','+str(j)+','+str(k)+','+str(l)+']')
    #
    m.update()
    startConstraints = time.time()
    for cijkl in C:
       # print 'debug %s' % str(cijkl)

        i = cijkl[0]; j = cijkl[1]; k = cijkl[2]; l = cijkl[3]
        lisij = [val for val in range(i+1, j)]
        lisk = [val for val in range(0,k)]
        lisl = [val for val in range(l+1, lenGB)]

        for item in lisij:
            # Add constraint: C.04
            listOff = X.select(item, lisk)
            if(listOff):
                for element in listOff:
                    m.addConstr(C[i,j,k,l] + element <= 1, 'C.04')

            # Add constraint: C.05
            listOff2 = X.select(item, lisl)
            if(listOff2):
                for element in listOff2:
                    m.addConstr(C[i,j,k,l] + element <= 1, 'C.05')

        liskl = [val for val in range(k+1, l)]
        lisi = [val for val in range(0,i)]
        lisj = [val for val in range(j+1,lenGA)]

        for item in liskl:
            # Add constraint: C.06
            listOff = X.select(lisi, item)
            if(listOff):
                for element in listOff:
                    m.addConstr(C[i,j,k,l] + element <= 1, 'C.06')

            # Add constraint: C.07
            listOff2 = X.select(lisj, item)
            if(listOff2):
                for element in listOff2:
                    m.addConstr(C[i,j,k,l] + element <= 1, 'C.07')
    
    # Here: count the time for the constraints from 4 to 7  
    constraintsTime = time.time() - startConstraints
    
    # MARKER: Neste ponto todas as Constraints ja foram definidas

    # Add constraint: C.08
    fmly = {}
    # create dictionary {gene family : members of family in GA}
    for idx, itm in enumerate(genomeA):
        if(itm not in fmly):
            fmly[itm] = [idx]
        else:
            fmly[itm].extend([idx])
    
    # create dictionary {gene family : numbers of members of family in GB}
    fmly2 = {}
    for itm in genomeB:
        if(itm not in fmly2):
            fmly2[itm] = 1
        else:
            fmly2[itm] = fmly2[itm] + 1
    # at this point fmly2 holds the number of presences of each family in GB
    
    numDuplicates = 0
    # the code below stores in fmly2 for each family present in GA and GB the min number of appearances
        # considering GA and GB, that is used for mapping the most duplicate genes possible in maximum matching model
    for itm in fmly2:
        if(itm in fmly):
            numDuplicates = numDuplicates + fmly2[itm] + len(fmly[itm]) - 2
            fmly2[itm] = min(fmly2[itm], len(fmly[itm]))
            #print itm, fmly2[itm], len(fmly[itm]),  fmly2[itm] + len(fmly[itm]) - 2, numDuplicates

    for g in fmly:
        # essential verification
        if(g in fmly2):
            # this code adds the constraint C.08, telling m.addConstr(X.sum(fmly[g], '*') == fmly2[g]) we say
                # that we want to match the most duplicates possible, this is the maximum matching model
            m.addConstr(X.sum(fmly[g], '*') == fmly2[g])

    startOpt = time.time()
    # Optimize model
    m.optimize()
    optmizingTime = time.time() - startOpt

    Result = PartialResult + m.objVal

    myoutFile.write('Obj: %d\n\n' % (Result))
    for v in m.getVars():
        if v.x == 1:
        #if(v.varName[0] == 'x'):
            myoutFile.write('%s %g\n' % (v.varName, v.x))
            #print('%s %g' % (v.varName, v.x))
            pass

    print PartialResult+m.objVal
    
    for c in m.getConstrs():
        #print(c.constrName, c.rhs)
        #myoutFile.write(c.constrName + " " + str(c.rhs) + "\n")
        pass


    #myout = open('aila', 'w')

    rulesTime = timeOfRule1 + timeOfRule2 + timeOfRule3 + timeOfRule4

    totalTime = rulesTime + optmizingTime + constraintsTime

    Result = PartialResult + m.objVal

    #a = '%-12s\t%-5s\t%-5s\t%-5s\t%-5s\t%-5s\t%-5s\t%-5s\t%-5s\t%-5s\t' % ('Name', 'Size', 'Dbls','R2','R3','R4','Cnstr','Opt','Total','Rsult')
    a = '%-12s\t%-5s\t%-5s\t%-5s\t%-5s\t%-5s\t%-5s\t%-5s\t%-5s\t%-5s\t%-5s\t' % ('Name', 'Size', 'Dbls','R1','R2','R3','R4','Cnstr','Opt','Total','Rsult')

    generalOutput = open(outputPath+'mainResultsGurobi', 'a+')

    #generalOutput.write('{}%t\t{}%r\n'.format(a, ''))
    generalOutput.write('%12s\t%-5d\t%-5d\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%-5d\t\n' % (inputName, lenGA, numDuplicates, timeOfRule1,timeOfRule2, timeOfRule3, timeOfRule4, constraintsTime,optmizingTime, totalTime, Result))
    
    print('inputfile: %s, Obj: %d, partialResult: %d, total: %d' % (inputName, m.objVal, PartialResult, Result))

except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')
