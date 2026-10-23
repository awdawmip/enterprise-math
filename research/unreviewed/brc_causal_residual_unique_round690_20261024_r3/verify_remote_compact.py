"""Exact BRC terminal-round classification, rational witnesses (no floating point)."""
from fractions import Fraction as F
from itertools import product
Q={'0':(1,665,1,333),'2':(333,333,1,333),'3':(1,1,1,997)}
E=((0,1),(1,2),(1,3),(2,3)); A='023'; D=1000
DEG=tuple(sum(i in e for e in E) for i in range(4))
BASE=[tuple(Q[a][i] for a in A) for i in range(4)]+[
    tuple(Q[a][i]+Q[a][j] for a in A) for i,j in E]
COEF={a:([DEG[i]*(D-Q[a][i]) for i in range(4)],
         [D-Q[a][i]-Q[a][j] for i,j in E]) for a in A}
POW=[[[b**k for k in range(690)] for b in row] for row in BASE]
counts={a:[0,0,0] for a in A}; pos=[]
for x in range(690):
    for y in range(690-x):
        z=689-x-y
        mon=[p[0][x]*p[1][y]*p[2][z] for p in POW]
        for a in A:
            ci,ce=COEF[a]
            val=sum(ci[i]*mon[i] for i in range(4)) - sum(ce[j]*mon[4+j] for j in range(4))
            s=(val>0)-(val<0);counts[a][s+1]+=1
            if val>0:pos.append((a,x,y,z))
assert pos==[('0',0,0,689)]
assert counts=={'0':[238394,0,1],'2':[238395,0,0],'3':[238395,0,0]}
assert sum(map(sum,counts.values()))==715185

def occupancy(w):
    n=len(w)
    if n<2:return F(0)
    state=[0]*16;state[0]=1
    for a in w:
        nxt=[0]*16
        for mask,number in enumerate(state):
            if number:
                for i,q in enumerate(Q[a]):nxt[mask|(1<<i)]+=number*q
        state=nxt
    return F(sum(state[(1<<i)|(1<<j)] for i,j in E),D**n)

def residual(w):
    d=[occupancy(w[:t]) for t in range(len(w)+1)]
    V=sum((max(d[t]-d[t-1],0) for t in range(2,len(d))), F(0))
    return V-max(d),max(d),d

assert residual('0203')[0]==0
assert residual('0230')[0]==F(193723,125000000)
ru,mu,_=residual('032');rv,mv,_=residual('023')
assert ru==rv==0 and mu==F(333,500) and mv==F(8684,15625)
assert residual('0320')[0]==F(8973220797,125000000000)
assert residual('0230')[0]==F(193723,125000000)
assert all(residual(''.join(w))[0]==0 for n in range(4) for w in product(A,repeat=n))
# Verify latest-round residual gain using integer ratio certificates.
pure3=lambda s:2*(2**s+998**s-997**s-3)
F690=4002+1334*997**689-668*998**689-668*2**689
assert F690>0
assert 100*pure3(400)>29*D**400
assert 50*(D*pure3(689)+F690)<13*D**690
print('PASS: 238395 prefix count vectors, 715185 exact signs; unique 3^6890')
print('PASS: R permutation and causal-peak counterexamples; exact tail witness')
