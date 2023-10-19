# 0/1 Knapsack Problem

# Assuming that the input is sorted in ascending order of weights
P=list(map(int,input("Enter P").split(',')))
W=list(map(int,input("Enter W").split (',')))
n=len(P)
P=[0]+P
W=[0]+W	
m=int(input("Weight of knapsack:"))

C=[]
for i in range(n+1):
	C.append([0]*(m+1))
	
print ("Initial:")
for row in C:
    print(row)

for i in range(1,n+1): 
    for w in range(1,m+1):
        if i-1<0:
            C[i][w] = C[i-1][w-W[i]] + P[i]
        elif w-W[i]<0:
            C[i][w] = C[i-1][w]
        else:
            C[i][w] = max(C[i-1][w], C[i-1][w-W[i]] + P[i])
        print(f"Step {i}, {w}:")
        for row in C:
            print(row)

print("Final:")
for row in C:
    print (row)

# Picking the items

x = [0]*n

i = n
w = m

# Max Profit = South East Corner Cell
profit = C[i][w]

P=P[1:]

while profit >= 0 and i-1>=0:
    # print ("Row Before:", C[1-11)
    # print ("Row Current:", C[i])
    # print("profit in C[i-1]", profit in C[i-1])
    if profit not in C[i-1]:
        x[i-1] = 1
        # print ("INCLUDE!!")
        # print("Profits List:", P)
        profit = profit - P[i-1]
        # print("New Profit:",profit)
    else:    
        x[i-1] = 0
#	print("New x:",x)
    i-=1

print("Answer:")
print(x)
