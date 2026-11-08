"""V27 signed BRC score equality: original M versus restored R651 q34.
Run next to R651_VERIFY_COMPACT.py. Python standard library only.
"""
from itertools import combinations, product
from R651_VERIFY_COMPACT import fields, state, recover

TRIADS=tuple(combinations(range(6),3))
MATCHINGS=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),
           ((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
NEIGH={s:tuple(t for t in TRIADS if len(set(s)&set(t))==2) for s in TRIADS}
def brc(s,m):
    z=set(s)
    if any((a in z)+(b in z)!=1 for a,b in m):return 0
    return 1 if sum(b in z for a,b in m)%2==0 else -1
C={s:tuple(brc(s,m) for m in MATCHINGS) for s in TRIADS}
def omega_of(M):return [[M[i][j]-M[j][i] for j in range(4)] for i in range(4)]
def score(u,om,s,t):
    return sum(u[i]*C[t][i] for i in range(4))+sum(C[s][i]*om[i][j]*C[t][j]
                                      for i in range(4) for j in range(4))
ALPH=(('P',0,0,1),('P',0,1,0),('P',1,2,3),
      ('T',0,0,1),('T',1,2,3),('P',0,3,2))
prefixes=checks=0
for n in range(4):
    for word in product(ALPH,repeat=n):
        for k in range(1,n+1):
            prefix=word[:k]
            z,original=fields(prefix)
            restored=recover(z[2]);M,_,_=state(prefix)
            assert original==restored
            prefixes+=1
            for c in (0,1):
                u0=[original[4][c][i]-original[5][c][i] for i in range(4)]
                u1=[restored[4][c][i]-restored[5][c][i] for i in range(4)]
                O=omega_of(M[c])
                restored_O=[[0]*4 for _ in range(4)]
                for (i,j),v in zip(combinations(range(4),2),z[2][c*6:c*6+6]):
                    restored_O[i][j]=v;restored_O[j][i]=-v
                for s in TRIADS:
                    for t in NEIGH[s]:
                        assert score(u0,O,s,t)==score(u1,restored_O,s,t)
                        checks+=1
assert prefixes==726, prefixes
assert checks==261360, checks
print('R651_V27_SIGNED_SCORE_EXTENSION_PASS', prefixes, checks)
