inp = """\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

with open("day11.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n")

for i, line in enumerate(inp):
    node, neighbours = line.split(": ")
    neighbours = neighbours.split()
    line = (node, [neighbours, 0])
    inp[i] = line

inp = dict(inp)
inp["out"] = [[], 0]
# print(inp)

considered_nodes = ["you"]
inp["you"][-1] = 1
while len(considered_nodes) > 0:
    new_considered_nodes = []
    for node in considered_nodes:
        cur_node_score = inp[node][-1]
        for neighbour in inp.get(node, [[], 0])[0]:
            inp[neighbour][-1] += cur_node_score
            if neighbour not in new_considered_nodes:
                new_considered_nodes.append(neighbour)
    considered_nodes = new_considered_nodes

print("PART 1:", inp["out"][-1])

# PART 2 ---------------------------------------------------------
import time
start = time.time()
inp = """\
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

with open("day11.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n")

for i, line in enumerate(inp):
    node, neighbours = line.split(": ")
    neighbours = neighbours.split()
    line = (node, [neighbours, 0, 0, 0])
    inp[i] = line

inp = dict(inp)
inp["out"] = [[], 0, 0, 0]

def create_graph():
    graph = {"svr": [[], [1,0,0]]}
    for node in list(inp.keys()):
        if node == "svr":
            continue
        past_neighbours = []
        for other_node, (neighbours, _, _, _) in inp.items():
            if node != other_node:
                # print(node, other_node)
                if node in neighbours:
                    past_neighbours.append(other_node)
        graph[node] = [past_neighbours, [0, 0, 0]]
    return graph

graph = create_graph()

# calculate sum of paths up to each node
# keeping track of all paths so far
# as well as paths that go through 'fft' (second number)
# and 'dac' (third number)
# if a current node's predecessors have not all been calculated
# (i.e., the first score is 0), push it to the end of the list
# and evaluate the next node that is now at position i
# this also creates a topological order of the graph
topological_order = list(graph)
i = 0
while i < len(graph):
    node = topological_order[i]
    neighbours, scores = graph[node]
    all_neighbours_calculated = True
    for neighbour in neighbours:
        if graph[neighbour][1][0] == 0:
            node = topological_order.pop(i)
            topological_order.append(node)
            all_neighbours_calculated = False
            break
    if not all_neighbours_calculated:
        continue
    for neighbour in neighbours:
        for k, score in enumerate(graph[neighbour][1]):
            graph[node][1][k] += score
    if node == "fft":
        scores[1] += scores[0]
    elif node == "dac":
        scores[2] += scores[1]
    i += 1

end = time.time()
print("PART 2:", graph["out"][1][2])
print(f"{(end-start)*1000:>7.2f} ms")

# # instead of pushing the unusable element to the end of the list
# # this looks for the next element that satisfies being usable
# # then puts that element in the current position in the list
# # incurs more steps though
# # still fast :)
# graph = create_graph()
# topological_order = list(graph)
# i = 0
# j = 0
# skips = 0
# while i < len(graph):
#     node = topological_order[i+j]
#     neighbours, scores = graph[node]
#     all_neighbours_calculated = True
#     for neighbour in neighbours:
#         if graph[neighbour][1][0] == 0:
#             all_neighbours_calculated = False
#             j += 1
#             break
#     if not all_neighbours_calculated:
#         continue
#     for neighbour in neighbours:
#         for k, score in enumerate(graph[neighbour][1]):
#             graph[node][1][k] += score
#     if node == "fft":
#         scores[1] += scores[0]
#     elif node == "dac":
#         scores[2] += scores[1]
#     node = topological_order.pop(i+j)
#     topological_order.insert(i, node)
#     i += 1
#     skips += j
#     j = 0

# print("PART 2:", graph["out"][1][2], skips)