from collections import defaultdict

row = []
col = []
C=dict()
costs=dict()
demand=dict()
supply=dict()
SUPPLY=0
DEMAND=0
r = int(input("Enter number of origins: "))
c = int(input("Enter number of destination: "))
print("Enter origin name")
for i in range(0,r):
    a=input()
    row.append(a)
print("Enter destination name")
for i in range(0,c):
    a=input()
    col.append(a)
print("Enter Supply")

for i in row:
    a=int(input())
    supply[i]=a
    SUPPLY+=a
print("Enter Demand")
for j in col:
    a=int(input())
    demand[j]=a
    DEMAND+=a

print("Enter costs")

for i in row:
    a1=[]
    for j in col:
        a=int(input())
        C[j]=a
    costs[i] = C
    C={}
if SUPPLY!=DEMAND:
    print("Unbalanced Problem")
    a = 'Dummy'
    if SUPPLY > DEMAND:
        print("Adding Column")
        col.append(a)
        demand['Dummy']=SUPPLY-DEMAND
        for i in row:
            costs[i]['Dummy']=0
    else:
        print("Adding Column")
        row.append(a)
        supply['Dummy']=DEMAND-SUPPLY
        for i in col:
            costs['Dummy'][i]=0
else:
    print("Balanced Problem")

cols = sorted(demand.keys())
res = dict((k, defaultdict(int)) for k in costs)
g = {}
for x in supply:
    g[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g])
for x in demand:
    g[x] = sorted(costs.keys(), key=lambda g: costs[g][x])
 
while g:
    d = {}
    for x in demand:
        d[x] = (costs[g[x][1]][x] - costs[g[x][0]][x]) if len(g[x]) > 1 else costs[g[x][0]][x]
    s = {}
    for x in supply:
        s[x] = (costs[x][g[x][1]] - costs[x][g[x][0]]) if len(g[x]) > 1 else costs[x][g[x][0]]
    f = max(d, key=lambda n: d[n])
    t = max(s, key=lambda n: s[n])
    t, f = (f, g[f][0]) if d[f] > s[t] else (g[t][0], t)
    v = min(supply[f], demand[t])
    res[f][t] += v
    demand[t] -= v
    if demand[t] == 0:
        for k, n in supply.items():
            if n != 0:
                g[k].remove(t)
        del g[t]
        del demand[t]
    supply[f] -= v
    if supply[f] == 0:
        for k, n in demand.items():
            if n != 0:
                g[k].remove(f)
        del g[f]
        del supply[f]
print("The entered costs are:")
s="\t"
for n in col:
    s=s+n+"\t"
print (s)
cost = 0
for i in row:
    s=i+"\t"
    for j in col:
        s=s+str(costs[i][j])+"\t"
    print(s)
for g in sorted(costs):
    for n in cols:
        y = res[g][n]
        cost += y * costs[g][n]
print("\nBasic Feasible Solution By Vogel's Approximation:" )
s="\t"
for n in col:
    s=s+n+"\t"
print (s)
for i in row:
    s=i+"\t"
    for j in col:
        s=s+str(res[i][j])+"\t"
    print(s)

print ("\nTotal Cost = ", cost)