Aqui se encontra a implementação de 6 algoritmos utilizados para comparação de
genomas utilizando Intervalos Comuns como medida de similiridade. Um deles é um algoritmo de Programação Linear, outros 3 são heurísticas criadas à partir da análise do primeiro algoritmo todos propostos por Angibaud no artigo citado abaixo e por fim uma heurística proposta por
nós durante nossa pesquisa. Os conceitos explorados por estes algoritmos são descritos em 

Angibaud et al. - 2007 - A pseudo-boolean framework for computing rearrangement distances between genomes with duplicates e 

Angibaud et al. - 2009 - On the Approximability of Comparing Genomes with Duplicates.

Os algoritmos são eles:

Os 4 primeiros foram propostos em (Angibaud et. al. 2007)
Common-Intervals-Program
    o qual foi implementado utilizando o solver Gurobi
Iterative-Longest-Common-Substring - ILCS
Improved-Iterative-Longest-Common-Substring - IILCS
Hybrid_k

Find-Disturb-Matches
    Uma heurística proposta por nós em nossa pesquisa para abordar o mesmo problema.


