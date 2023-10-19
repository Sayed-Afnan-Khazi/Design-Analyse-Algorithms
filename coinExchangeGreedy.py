# Assume sorted for now
D = list(map(int,input("Enter Denominations, separated by commas:").split(",")))
v = int(input("Enter the value to be exchanged:"))

X = [0]*len(D)

for i in range(len(D)):
    if D[i]>v:
        continue
    elif D[i] == v:
        # print("Exact value present", D[i])
        X[i]=1
        break
    else:
        v=v-D[i]
        X[i]=1
else:
    if v!=0:
        print("Not possible to exchange this value for the given denominations")
        print("Nearest Value:", sum([D[i] for i in range(len(D)) if X[i]==1]))

print("Denominations:",D)
print("Selected:",X)
print("Denominations Given:",[D[i] for i in range(len(D)) if X[i]==1 ])