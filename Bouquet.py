import gudhi
import networkx as nx
import matplotlib.pyplot as plt
n = 5

sc = gudhi.SimplexTree()

sc.insert([0])

for i in range(n):
    sc.insert([0, 2*i+1])
    sc.insert([0, 2*i+2])
    sc.insert([2*i+1, 2*i+2])

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

def EulerCharacteristic(simpcomplex, verbose = 'True'):
    num_simplices = [0 for i in range(simpcomplex.dimension()+1)]
    for filtration in simpcomplex.get_simplices():
        simplex = filtration[0]
        num_simplices[len(simplex)-1]+=1
    Euler_characteristic = sum(num_simplices[::2]) - sum(num_simplices[1::2])
    if verbose: print('Característica De Euler = '+repr(Euler_characteristic)+'.')
    return Euler_characteristic   
    
DrawSimplicialComplex(sc)
print('N = '+repr(n))
EulerCharacteristic(sc)
