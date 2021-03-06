import networkx as nx

borders = nx.Graph()
not_borders1 = nx.DiGraph()
# not_borders2 = nx.MultiDiGraph()

# clustering() 函数不能作用在有向图上
# nx.clustering(not_borders1) //wrong
nx.clustering(nx.Graph(not_borders1))


borders.add_node("Zimbabwe")
borders.add_nodes_from(["Lugandon", "Zambia", "Portugal", "Kuwait", "Colombia"])

borders.remove_node("Lugandon")
borders.add_edge("Zambia", "Zimbabwe")
borders.add_edges_from([("Uganda", "Rwanda"), ("Uganda", "Kenya"), ("Uganda", "South Sudan"),
                        ("Uganda", "Tanzania"), ("Uganda", "Democratic Republic of the Congo")])

# write
with open("borders.graphml", "wb") as netfile:
    nx.write_pajek(borders, netfile)

# read
with open("borders.graphml", "rb") as netfile:
    borders = nx.read_pajek(netfile)