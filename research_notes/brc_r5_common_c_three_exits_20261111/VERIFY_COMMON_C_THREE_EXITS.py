#!/usr/bin/env python3
"""R5 exact common-C branching theorem, frozen seven-ratio Blackwell fiber."""
from fractions import Fraction as F
R=(2,10,15,20,25,30,38)
S=(1,2,3,5)
ARCS=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j)
E0=tuple(map(F,('219346331/10192753200,7664319/135903376,2813871/16987922,'
 '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,393042/8493961,196521/33975844,'
 '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,5251441/33975844,166713611/1274094150,'
 '2500147/33975844,393042/8493961,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,7664319/135903376,451274777/3397584400').split(',')))
V=tuple((i,j) for j in S for i in range(7)); ix={a:k for k,a in enumerate(V)}
A=[[int(ii==i) for ii,jj in V] for i in range(7)]
A += [[int(jj==j) for ii,jj in V] for j in S]
A += [[R[ii]*int(jj==j) for ii,jj in V] for j in S]
b=[sum((z for (ii,j),z in zip(ARCS,E0) if ii==i and j in S),F(0)) for i in range(7)]
b += [sum((z for (ii,j),z in zip(ARCS,E0) if j==p),F(0)) for p in S]
b += [sum((R[ii]*z for (ii,j),z in zip(ARCS,E0) if j==p),F(0)) for p in S]
assert len(V)==28 and len(ARCS)==30 and len(A)==len(b)==15
C=tuple(map(F,('10022571/135903376,74268405/475661816,0,0,0,0,10022571/475661816,'
 '0,122039541/1902647264,196521/67951688,0,0,0,26530335/1902647264,'
 '0,0,11485487/67951688,377644447/2548188300,5499155/67951688,0,831435/33975844,'
 '0,6092151/1902647264,0,0,680265/67951688,2161731/33975844,27135015/1902647264').split(',')))
XA=tuple(map(F,('10022571/135903376,1383455/16987922,1544855/16987922,0,0,0,5863/1213423,'
 '0,0,196521/2426846,0,0,0,0,'
 '0,264166201/1902647264,0,377644447/2548188300,5499155/67951688,0,103987795/1902647264,'
 '0,6092151/1902647264,0,0,680265/67951688,2161731/33975844,27135015/1902647264').split(',')))
assert len(XA)==len(C)==28
def atom(other,row):
    h=[F(0)]*28
    for target,value in row.items():
        h[ix[(target,3)]]=F(value)
        h[ix[(target,other)]]=-F(value)
    assert all(sum(a*v for a,v in zip(line,h))==0 for line in A)
    return tuple(h)
def step(x,h,t):return tuple(a+t*v for a,v in zip(x,h))
def mask(x):return {i for i in range(7) if x[ix[(i,3)]]>0}
def check(x,expected):
    assert min(x)>=0 and all(sum(a*v for a,v in zip(line,x))==rhs for line,rhs in zip(A,b))
    assert mask(x)==expected,(mask(x),expected)
    return sum(v>0 for v in x)
MA,MC,MB={1,3,4,6},{2,3,4,6},{2,3,4,5}
h1=atom(1,{1:-23,2:28,6:-5})
h2=atom(2,{1:-23,2:28,6:-5})
t1,t2=F('1544855/475661816'),F('5306067/1902647264')
W=step(XA,h1,t1)
assert step(W,h2,t2)==C
print('EXACT_A_TO_C',check(XA,MA),check(W,MA|MC),check(C,MC),'t1',t1,'t2',t2)
c=C[ix[(6,3)]]
print('COMMON_C_SOURCE3_6',c)
for m in (2,3,4):
    row={m:-8,5:38-R[m],6:R[m]-30}
    assert sum(row.values())==0 and sum(R[i]*z for i,z in row.items())==0
    h=atom(5,row)
    t=c/F(30-R[m]);Y=step(C,h,t)
    count=check(Y,MB)
    slack_m=C[ix[(m,3)]]-8*t
    slack_comp=C[ix[(5,5)]]-(38-R[m])*t
    assert slack_m>0 and slack_comp>=0
    print('BRANCH',m,'t',t,'row',row,'remaining_source3_m',slack_m,'remaining_source5_target5',slack_comp,'terminal_positive_arcs',count)
print('POSSIBLE_THIRD_TARGETS',tuple(sorted(MC & MB)))
print('PASS_R5_EXACT_COMMON_C_THREE_BRANCH_ATOMIC_EXITS')
