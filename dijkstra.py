'''Algorithm to find the shortest path from a source node to every other node in a weighted directed graph.'''
'''DOES NOT WORK WITH -VE WEIGHTS'''
class Node:
    def __init__(self, name):
        self.name = name
        self.connected_to = {}
        self.dist = 9999 # Infinity
        self.parent = None
    
    def connect (self, node, weight):
        '''Connects this node with the parameter node with a weight of the parameter weight'''
        self.connected_to[node] = weight
    
    def weight_to(self, node):
        '''Returns the weight of the connection between this node and the parameter node if a connection exists, otherwise returns None'''
        if self.connected_to[node]:
            # Connected
            return self. connected_to[node]
        else:
            # Not connected
            return None
    def list_connections (self):
        return self.connected_to
    

def extractMin(w):
    '''Returns the node from w that has the minimum dist value'''
    return min(w,key= lambda node: node.dist)

def printResults(sol):
    print("V:", [node.name for node in sol])
    print("D:", [node.dist for node in sol])
    print("P:", [node.parent.name for node in sol])


def dijkstras(src,w: list[Node],sol):
    # Select the source
    src.dist = 0
    src.parent = Node ("Start")

    # The Algorithm
    while len(w)!=0:
        i = 0
        u = extractMin(w)
        sol.append(u)
        w.remove(u)
        for node in u.list_connections():
            if node.dist > u.dist + u.weight_to(node):
                node.dist = u.dist + u.weight_to(node)
                node.parent = u
    else:
        # Complete
        printResults (sol)


# Running the algorithm:


## Example 1:

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")

A.connect(B,10)
A.connect(C,3)
A.connect(D,20)
B.connect(D,5)
C.connect(B,2)
C.connect(D,3)


sol = []
w = [A,B,C,D]


dijkstras (A,w,sol)

## Example 2:

A = Node("A")
B = Node("B")
C = Node("C")

A.connect(B,10)
A.connect(C,2)
C.connect(B,4)

sol = []
w = [A,B,C]

dijkstras (A,w,sol)

# Example 3:

S = Node("S")
A = Node("A")
B = Node("B")
C = Node("C")
E = Node("E")
F = Node("F")
G = Node("G")
D = Node("D")

S.connect(A,1)
S.connect(C,5)
S.connect(G,6)
A.connect(B,2)
B.connect(D,3)
C.connect(E,8)
C.connect(D,4)
G.connect(E,7)
E.connect(F,9)
F.connect(D,2)

sol = []
W = [A,B,C,D,E,F,G,S]

dijkstras(S,W,sol)