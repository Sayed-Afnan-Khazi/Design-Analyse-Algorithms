# Huffman Encoding algorithm for variable length encoding

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.letter = None
def __str__(self):
    return str(self. value)

decodeTable = {}

def walk(Nod, currentPath=''):
    global decodeTable
    if Nod == None:
        return None
    # print(Nod.value)
    if Nod.letter:
        # print("Letter",Nod.letter, "Path", currentPath)
        decodeTable[currentPath] = Nod.letter
    resetPath = currentPath
    if Nod.left:
        # print("Left of", Nod.value)
        currentPath += '0'
        walk (Nod.left, currentPath)
    currentPath = resetPath
    if Nod.right:
        # print("Right of", Nod.value)
        currentPath += '1'
        walk (Nod. right, currentPath)


def index0fMin(arr):
    return arr.index(min(arr))

def indexofSecondMin(arr):
    temp = list (arr)
    secondMin = sorted (temp)[1]
    return arr.index (secondMin)

letters = ['E', 'A', 'D', 'B', 'C']
times = [2,3,4,5,6]
# times = [2,3,4,4,7]

nodes = [Node(value, None, None) for value in times]

for i in range(len (nodes)):
    nodes[i].letter = letters[i]


# print ([node.letter for node in nodes])

que = times
# que = [2,3,4,4,7]

while len(nodes) > 1:
    # print("Queue: ", que)
    # print("Nodes:", [node. value for node in nodes])
    # Finding the two mininum nodes, to merge
    minIndex = index0fMin(que)
    secondMinIndex = indexofSecondMin(que)
    # print("minIndex", minIndex)
    # print("secondMinIndex", secondMinIndex)
    # Creating the merged node
    newNode = Node(nodes[minIndex].value + nodes[secondMinIndex].value, nodes[minIndex], nodes[secondMinIndex])
    # print("New Node Value:", newNode. value)
    # print("Queue Before Removal:" ,que)
    # Removing merged values from the queue
    que.pop(minIndex)
    if minIndex < secondMinIndex:
        que.pop(secondMinIndex-1)
    else:
        que.pop(secondMinIndex)
    # print("Queue After Removal:",que)
    # Removing merged values from the nodes list
    # print("Nodes Before Removal:",[node.value for node in nodes])
    nodes.pop(minIndex)
    if minIndex < secondMinIndex:
        nodes.pop(secondMinIndex-1)
    else:
        nodes.pop(secondMinIndex)
    # Appending the new node's value to the queue
    que.append(newNode.value)
    # Appending the new node to the nodes list
    nodes.append(newNode)
    # print("Nodes After Removal:", [node.value for node in nodes])
    # print ("Queue:", que)
    # print ("Nodes:", [node.value for node in nodes])

walk(nodes[-1])
print(decodeTable)


def decodeString(st, decodeTable):
    decodedString=''
    i=0
    while i<len(st):
        if len(st[i:i+2])==2 and st[i:i+2] in decodeTable:
            decodedString += decodeTable[st[i:i+2]]
            i+=2
        elif len(st[i:i+3])==3 and st[i:i+3] in decodeTable:
            decodedString += decodeTable[st[i:i+3]]
            i+=3
        else:
            i+=1 # Is this necessary?
    return decodedString

print(decodeString('001111101',decodeTable))


def encodeString (plainString, decodeTable):
    encodeTable = {}
    for key in decodeTable:
        encodeTable[decodeTable[key]] = key
    encodedString = ''
    for letter in plainString:
        if letter in encodeTable:
            encodedString += encodeTable[letter]
        else:
            print("Unknown letter:",letter)
    else:
        return encodedString
    
print(encodeString('DCCA', decodeTable))

print(decodeString(encodeString('DCCA',decodeTable), decodeTable))