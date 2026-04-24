import gudhi
import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools

def DrawSimplicialComplex(simpcomplex, pos=None):
    nodes=[]; edges=[]
    for filtr in simpcomplex.get_skeleton(1):
        simplex = filtr[0]
        if len(simplex)==1:
            nodes.append(simplex[0])
        if len(simplex)==2:
            edges.append(simplex)
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    if pos == None:
        pos = nx.spring_layout(G)
    nx.draw(G, pos=pos, with_labels=True, font_weight='bold', node_color='magenta')
    plt.show()
    
def NumberOfConnectedComponents(simpcomplex, verbose = 'True'):
    simpcomplex.compute_persistence()
    nbr_components = simpcomplex.betti_numbers()[0]
    if verbose: print('admite '+repr(nbr_components)+' componentes conexas')
    return nbr_components

def EulerCharacteristic(simpcomplex, verbose = 'True'):
    num_simplices = [0 for i in range(simpcomplex.dimension()+1)]
    for filtration in simpcomplex.get_simplices():
        simplex = filtration[0]
        num_simplices[len(simplex)-1]+=1
    Euler_characteristic = sum(num_simplices[::2]) - sum(num_simplices[1::2])
    if verbose: print('Característica De Euler = '+repr(Euler_characteristic)+'.')
    return Euler_characteristic

def Exercício_26(n,p):
    V = list(range(n))
    simpcomplex = gudhi.SimplexTree()
    for i in range(n):
        simpcomplex.insert([i])
    for v in itertools.combinations(V,2):
        if random.random()<p:
            simpcomplex.insert(list(v))

    EulerCharacteristic(simpcomplex)
    NumberOfConnectedComponents(simpcomplex)
    DrawSimplicialComplex(simpcomplex)

Exercício_26(n = 10, p = 0.5)