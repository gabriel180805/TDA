import gudhi 
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


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
    if verbose: print('The simplicial complex admits '+repr(nbr_components)+' connected component(s).')
    return nbr_components

def EulerCharacteristic(simpcomplex, verbose = 'True'):
    num_simplices = [0 for i in range(simpcomplex.dimension()+1)]
    for filtration in simpcomplex.get_simplices():
        simplex = filtration[0]
        num_simplices[len(simplex)-1]+=1
    Euler_characteristic = sum(num_simplices[::2]) - sum(num_simplices[1::2])
    if verbose: print('Característica De Euler = '+repr(Euler_characteristic)+'.')
    return Euler_characteristic

def letter_A():
    simpcomplex = gudhi.SimplexTree()

    simpcomplex.insert([0,1])
    simpcomplex.insert([1,2])
    simpcomplex.insert([2,0])
    simpcomplex.insert([3,0])
    simpcomplex.insert([4,1])
    return simpcomplex

def letter_B():
    simpcomplex = gudhi.SimplexTree()

    simpcomplex.insert([0,1])
    simpcomplex.insert([1,2])
    simpcomplex.insert([2,0])
    simpcomplex.insert([2,3])
    simpcomplex.insert([3,4])
    simpcomplex.insert([4,2])
    return simpcomplex

def letter_C():
    simpcomplex = gudhi.SimplexTree()

    simpcomplex.insert([0,1])
    return simpcomplex

def letter_D():
    simpcomplex = gudhi.SimplexTree()

    simpcomplex.insert([0,1])
    simpcomplex.insert([1,2])
    simpcomplex.insert([2,0])
   
    return simpcomplex

def letter_E():
    simpcomplex = gudhi.SimplexTree()

    simpcomplex.insert([0,1])
    simpcomplex.insert([1,2])
    simpcomplex.insert([2,3])
    simpcomplex.insert([2,4])
    simpcomplex.insert([4,5])
    return simpcomplex

def letter_F():
    simpcomplex = gudhi.SimplexTree()

    simpcomplex.insert([0,1])
    simpcomplex.insert([1,2])
    simpcomplex.insert([2,3])
    simpcomplex.insert([2,4])
    
    return simpcomplex

def letter_G():
    simpcomplex = gudhi.SimplexTree()

    simpcomplex.insert([0,1])
    return simpcomplex

def letter_H():
    simpcomplex = gudhi.SimplexTree()

    simpcomplex.insert([0,2])
    simpcomplex.insert([1,3])
    simpcomplex.insert([2,3])
    simpcomplex.insert([2,4])
    simpcomplex.insert([3,5])
    
    return simpcomplex

simpcomplex = letter_H()    
DrawSimplicialComplex(simpcomplex)
EulerCharacteristic(simpcomplex)