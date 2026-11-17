#!/usr/bin/env python3
"""Independent Python 3.10+ certificate for PREFIX-878.
Counts each rational-slope line by congruence classes, and filters old
certificates only on mathematically eligible odd-odd points.
"""
import json
from itertools import combinations
B=19
Q=(1<<B)-1
families=((3,2,'3to2'),(2,3,'2to3'),(4,1,'4to1'),(1,4,'1to4'))
D=set(1<<i for i in range(1,B))
D.update((1<<i)+(1<<j) for i in range(1,B) for j in range(1,i))
D.update((1<<i)-(1<<j) for i in range(1,B+1) for j in range(1,i))
Ds=D|{1<<B,1<<(B+1)}
Ep={1}|{(1<<i)+s for i in range(1,B+1) for s in (-1,1)}
E=Ep|{-x for x in Ep}
assert (len(D),len(Ds),len(E)) == (307,309,74)

def previous(x,y):
    return abs(x-y) in D or 3*x-y in Ds or 2*x-y in E or 2*y-x in E

def valid(x,y):
    return 1<=x<=Q and 1<=y<=Q and (x&1) and (y&1) and x!=y

def line_x(k,l,e):
    # From y=(k*x-e)/l and 1<=y<=Q, obtain exact bounded x interval.
    lo=max(1,(e+l+k-1)//k)
    hi=min(Q,(e+l*Q)//k)
    step=2*l
    for residue in range(1,step+1,2):
        if (k*residue-e-l)%step: continue
        first=lo+(residue-lo)%step
        for x in range(first,hi+1,step):
            yield x,(k*x-e)//l

stats=[]
for k,l,name in families:
    raw=new=diagonal=0
    for e in sorted(E):
        for x,y in line_x(k,l,e):
            assert (x&1) and (y&1) and 1<=x<=Q and 1<=y<=Q
            if x==y:
                diagonal+=1
                continue
            raw+=1
            if not previous(x,y):new+=1
    stats.append((name,raw,new,diagonal))

# Independent analytic line intersections. All families encode k*x-l*y=e.
cross=set()
for (k,l,_),(m,n,_) in combinations(families,2):
    det=l*m-k*n
    assert det
    for e in E:
        for f in E:
            num_x=l*f-n*e
            num_y=k*f-m*e
            if num_x%det or num_y%det:continue
            x,y=num_x//det,num_y//det
            if valid(x,y) and not previous(x,y):cross.add((x,y))
mult={2:0,3:0,4:0}
for x,y in cross:
    hits=sum(k*x-l*y in E for k,l,_ in families)
    assert hits>=2
    mult[hits]+=1
net=sum(row[2] for row in stats)-sum((n-1)*num for n,num in mult.items())
assert stats==[
('3to2',6291415,6266455,36),
('2to3',6291415,6270009,36),
('4to1',4587503,4576829,18),
('1to4',4587503,4577295,18)]
assert mult=={2:1635,3:51,4:12}
assert net==21688815
result={'status':'INDEPENDENT_EXACT_CHECK_PASSED','families':[{'name':n,'raw':r,'new_beyond_877':z,'diagonal_omitted':d}for n,r,z,d in stats], 'cross_family_multiplicities':mult, 'net_new':net, 'cumulative_certified':181323035+net}
print(json.dumps(result,indent=2))
