import requests,json,sys,time,csv
import networkx as nx
import matplotlib.pyplot as plt

def read_csv(file):
    results = []
    with open(file, 'r', newline = '', encoding = 'utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            results.append(list(map(lambda x:x.strip() , row)))
    return results

trans = read_csv('trans.csv')


source = sys.argv[1]
target = sys.argv[2]
cheap = 1000
if len(sys.argv) > 3 :
    cheap = int(sys.argv[3])

raw_edge = []
for e in trans[1:]:
    costx = int(e[0])
    x = e[1]
    costy = int(e[2])
    y = e[3]
    costz = int(e[4])
    z = e[5]
    
    if costy > cheap:
        continue
    raw_edge.append([x, y, z])

            

G = nx.DiGraph()
for e in raw_edge:
    G.add_edge(e[0], e[2], weight = 1)

dist = nx.all_shortest_paths(G, source = source, target = target, weight = 'weight')
opt_paths = [p for p in dist]
edge_show = {}
for path in opt_paths:
    pre = '-1'
    for node in path:
        if pre != '-1':
            edge_show[(pre, node)] = {}
        pre = node

for e in raw_edge:
    if (e[0], e[2]) in edge_show:
        edge_show[(e[0], e[2])][e[1]] = 1

edge_show_com = [[k[0], k[1], '/'.join(list(v.keys()))] for k, v in edge_show.items()]
G2 = nx.DiGraph()
for e in edge_show_com:
    G2.add_edge(e[0], e[1], weight = 1)

label = {}
for e in edge_show_com:
    label[(e[0], e[1])] = e[2]

# show G2
pos = nx.spring_layout(G2)
nx.draw(G2, pos, with_labels = True, node_size = 450, font_size = 6)
nx.draw_networkx_edge_labels(G2, pos, edge_labels = label, font_size = 8)


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
