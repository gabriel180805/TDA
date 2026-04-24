import gudhi
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

pos = {0: [0.29409772548731694, 0.6646626625013836],
1: [0.01625840776679577, 0.1676405753593595],
2: [0.15988905150272759, 0.6411323760808338],
3: [0.9073191075894482, -0.16417982219713312],
4: [-0.18661467838673884, 0.31618948583046413],
5: [-0.3664040542098381, 0.9098590694955988],
6: [-0.43753448716144905, -0.8820102274699417],
7: [0.4096730199915961, -0.23801426675264126],
8: [0.5903822103474676, -0.7285102954232894],
9: [0.9133851839417766, -0.6606557328320093],
10: [-0.15516122940597588, 0.7565411235103017],
11: [-0.38626186295039866, -0.3662321656058476],
12: [0.005209710070218199, 0.27655964872153116],
13: [0.670078068894711, -0.00932202688834849],
14: [-0.011268465716772091, 0.24340880308017376],
15: [-0.6441978411451603, -0.9672635759413206],
16: [-0.2841794022401025, -0.6734801188906114],
17: [-0.15473260248990717, -0.1365357396855129],
18: [0.7177096105982121, 0.9378197891592468],
19: [-0.4677068504994166, 0.1533930130294956],
20: [-0.32379909116817096, 0.9694800649768063],
21: [-0.2886940472879451, -0.039544695812395725],
22: [-0.5900701743351606, 0.8350804500575086],
23: [0.14931959728335853, 0.869106793774487],
24: [-0.14500672678238824, -0.3170082291070364],
25: [0.07324547392476122, 0.6653572287065117],
26: [-0.662990048258566, 0.1908198608241125],
27: [-0.25641262456436276, -0.9844196180941553],
28: [-0.5105685407819842, -0.4236604017060557],
29: [0.6792549581008038, -0.026215820387260003]}

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
    if verbose: print('Admite '+repr(nbr_components)+' componentes conexas')
    return nbr_components

def Exercício_25(r):
    s = gudhi.SimplexTree()
    for i in range(30):
        s.insert([i])

    keys = list(pos.keys())

    for a in range(len(keys)):
        for b in range(a):
            i = keys[a]
            j = keys[b]
            if np.linalg.norm(np.array(pos[i]) - np.array(pos[j])) <= r:
                s.insert([i, j])

    DrawSimplicialComplex(s, pos)

    NumberOfConnectedComponents(s)

Exercício_25(r = 0.02)   