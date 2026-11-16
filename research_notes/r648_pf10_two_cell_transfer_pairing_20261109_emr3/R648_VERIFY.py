#!/usr/bin/env python3
"""R648: exact V29 two-Cell transfer-coupling residual tests (Python stdlib)."""
from itertools import product
from fractions import Fraction
import json

Q = 4
PORTS = range(Q)
EDGES = tuple((a,b) for a in PORTS for b in PORTS)
BI_EDGES = tuple((d,a,b) for d in ('xy','yx') for a,b in EDGES)

def zeros(): return [[0]*Q for _ in PORTS]
def fresh():
    return {'Nxy':zeros(),'Nyx':zeros(),
            'x':{'M':zeros(),'rin':[0]*Q,'rout':[0]*Q},
            'y':{'M':zeros(),'rin':[0]*Q,'rout':[0]*Q}}
def transfer(L,d,a,b):
    source,target=('x','y') if d=='xy' else ('y','x')
    L['N'+d][a][b] += 1
    L[source]['rout'][a] += 1
    L[target]['rin'][b] += 1

def margins(N):
    return ([sum(N[i]) for i in PORTS],
            [sum(N[i][j] for i in PORTS) for j in PORTS])

def recover(r,c,z):
    assert sum(r)==sum(c)
    N=zeros()
    for i in range(Q-1):
        for j in range(Q-1): N[i][j]=z[i][j]
    for i in range(Q-1): N[i][Q-1]=r[i]-sum(N[i][j] for j in range(Q-1))
    for j in range(Q-1): N[Q-1][j]=c[j]-sum(N[i][j] for i in range(Q-1))
    N[Q-1][Q-1]=r[Q-1]-sum(N[Q-1][j] for j in range(Q-1))
    assert all(v>=0 for row in N for v in row)
    assert margins(N)==(r,c)
    return N

def derived(s):
    M=s['M']; ro=s['rout']; ri=s['rin']
    Om=[[M[i][j]-M[j][i] for j in PORTS] for i in PORTS]
    I=[sum(M[i])+ri[i] for i in PORTS]
    O=[sum(M[j][i] for j in PORTS)+ro[i] for i in PORTS]
    u=[I[i]-O[i] for i in PORTS]
    assert u==[sum(Om[i])+ri[i]-ro[i] for i in PORTS]
    return u,Om

def verify(L):
    for d in ('xy','yx'):
        r,c=margins(L['N'+d]); source,target=('x','y') if d=='xy' else ('y','x')
        assert L[source]['rout']==r and L[target]['rin']==c
        assert recover(r,c,[row[:3] for row in L['N'+d][:3]])==L['N'+d]
    ux,Ox=derived(L['x']); uy,Oy=derived(L['y'])
    assert sum(ux)+sum(uy)==0
    assert Ox==Oy==zeros()
    return True

def rank(A):
    A=[[Fraction(v) for v in row] for row in A]
    nr,nc=len(A),len(A[0]); k=0
    for j in range(nc):
        pivot=next((i for i in range(k,nr) if A[i][j]),None)
        if pivot is None:continue
        A[k],A[pivot]=A[pivot],A[k]
        v=A[k][j]; A[k]=[x/v for x in A[k]]
        for i in range(nr):
            if i!=k and A[i][j]:
                t=A[i][j];A[i]=[A[i][l]-t*A[k][l] for l in range(nc)]
        k+=1
        if k==nr:break
    return k

A=[[int(a==i) for a,b in EDGES] for i in PORTS]
A += [[int(b==j) for a,b in EDGES] for j in PORTS]
Z=[[int(a==i and b==j) for a,b in EDGES] for i in range(3) for j in range(3)]
assert rank(A)==7 and rank(A+Z)==16
for i in range(3):
    for j in range(3):
        B=zeros();B[i][j]=1;B[i][3]=-1;B[3][j]=-1;B[3][3]=1
        assert margins(B)==([0]*Q,[0]*Q)

words_one=0
for n in range(4):
    for word in product(EDGES,repeat=n):
        L=fresh()
        for a,b in word:transfer(L,'xy',a,b)
        assert verify(L)
        words_one+=1
assert words_one==4369
words_both=0
for n in range(3):
    for word in product(BI_EDGES,repeat=n):
        L=fresh()
        for ev in word:transfer(L,*ev)
        assert verify(L)
        words_both+=1
assert words_both==1057

A0=fresh();B0=fresh()
for a,b in ((0,0),(1,1)):transfer(A0,'xy',a,b)
for a,b in ((0,1),(1,0)):transfer(B0,'xy',a,b)
assert A0['x']==B0['x'] and A0['y']==B0['y']
assert A0['Nxy']!=B0['Nxy']
assert A0['Nxy'][0][0]==1 and B0['Nxy'][0][0]==0
seen=set()
for event in BI_EDGES:
    L=fresh();transfer(L,*event)
    signature=tuple(tuple(L[c][field]) for c in ('x','y') for field in ('rin','rout'))
    assert signature not in seen
    seen.add(signature)
assert len(seen)==32
E=[[0]*32 for _ in range(16)]
for k in range(8):
    for j in range(16): E[k][j]=A[k][j]
    for j in range(16): E[k+8][j+16]=A[k][j]
Z2=[[v for v in z]+[0]*16 for z in Z]+[[0]*16+list(z) for z in Z]
assert rank(E)==14 and rank(E+Z2)==32

report={
 'marker':'R648_TRANSFER_PAIRING_NINE_PLUS_NINE_EXACT_PASS',
 'model':'two distinct typed X6 Cells x,y; four declared PF10 ports per Cell; V29 PASS/TRANSFER cumulative rules',
 'science_pin':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
 'source_pin':'V29@b62110008321d9147212cb89f2627ff613c2550d',
 'one_way':{'rank_margins':7,'rank_repaired':16,'minimal_additive_residuals':9},
 'two_way':{'rank_margins':14,'rank_repaired':32,'minimal_additive_residuals':18},
 'one_way_words_len_le3':words_one,
 'both_directions_words_len_le2':words_both,
 'pair_collision_length':2,
 'single_events_unique':len(seen),
 'pair_A_nonzero':[[0,0],[1,1]],
 'pair_B_nonzero':[[0,1],[1,0]],
 'mathematical_basis':'B_ij=E_ij-E_i3-E_3j+E_33, i,j=0..2',
 'rank_scope':'linear additive labeled transfer-counter augmentation over rationals/integers, not arbitrary encodings',
 'driver_reviewed':False,'formal_claim':False
}
print(json.dumps(report,ensure_ascii=False,indent=2))
