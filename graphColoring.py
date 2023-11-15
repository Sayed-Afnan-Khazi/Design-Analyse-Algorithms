colours = {1: 'Red' ,2: 'Green',3: 'Blue'}
m = len(colours) # Number of colors
n = 4 # Number of nodes
node_colours = [None]*n

## Example 1
# node_graph = [
# [0,1,0,0],
# [1,0,1,1],
# [0,1,0,0],
# [0,1,0,0]
# ]

## Example 2
# node_graph = [
# [0,1,0,1],
# [1,0,1,1],
# [0,1,0,1],
# [1,1,1,0]
# ]

def isSafe(k,colour):
    global node_graph, n
    for i in range(n):
        if node_graph[k][i] == 1 and node_colours[i] == colours[colour]:
            print (k,i, "are connected and have the same color")
            return False
    return True


def colour_node(k):
    global node_colours, node_graph, m, colours
    print(node_colours)
    for colour in colours:
        print("Checking isSafe(",k,colour,")")
        if isSafe(k,colour):
            print(k, 'is safe with',colours[colour])
            node_colours[k] = colours[colour]
            print(node_colours)
            if (k+1) < n:
                print ("Checking next node: Node", k+1)
                colour_node(k+1)
                return
            else:
                # Complete coloring
                print("COMPLETE! !!!:", node_colours)
                return
        else:
            print(k, 'is not safe with',colours[colour])

colour_node(0)