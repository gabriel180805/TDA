import gudhi
import matplotlib.pyplot as plt
import networkx as nx


toro = gudhi.SimplexTree()
def DrawSimplicialComplex(toro, pos=None):
    nodes=[]; edges=[]
    for filtr in toro.get_skeleton(1):
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

toro.insert([0,3,7])
toro.insert([0,2,7])
toro.insert([2,7,5])
toro.insert([2,1,5])
toro.insert([1,5,3])
toro.insert([0,1,3])

toro.insert([3,4,8])
toro.insert([3,7,8])
toro.insert([4,0,2])
toro.insert([4,2,8])
toro.insert([8,2,1])
toro.insert([8,1,6])

toro.insert([6,1,0])
toro.insert([6,4,0])
toro.insert([5,6,4])
toro.insert([5,4,3])
toro.insert([7,8,6])
toro.insert([7,5,6])

EulerCharacteristic(toro)
DrawSimplicialComplex(toro)