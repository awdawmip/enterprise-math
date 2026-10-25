#!/usr/bin/env python3
"""R4-EC12: exact symbolically certified positive Laurent realization. Python3+SymPy."""
from collections import deque
from sympy import Matrix, Symbol, zeros, cancel
z=Symbol("z",nonzero=True)
edge={0:((2,-1,-1),(2,+1,-1)),1:((0,-1,-1),(0,+1,-1)),2:((1,+1,+1),(2,+1,-1))}
def move(s,a):
    q,r,e,t=s
    q1,eta,b=edge[q][a]
    e1=e*eta
    r1=2 if r==2 else (0 if a else (1 if r==0 else 2))
    return (q1,r1,e1,t+e1*b)
todo=deque([(0,0,1,0)]); seen=set()
while todo:
    state=todo.popleft()
    if state[:3] in seen: continue
    seen.add(state[:3])
    for a in (0,1):todo.append(move(state,a))
states=sorted(seen); assert len(states)==14
idx={s:i for i,s in enumerate(states)}
T=zeros(14)
for j,state in enumerate(states):
    for a in (0,1):
        dest=move((*state,0),a)
        T[idx[dest[:3]],j]+=z**dest[3]
channels=[(q,dirty,e) for q in range(3) for dirty in (0,1) for e in (-1,1)]
C=zeros(12,14)
for j,(q,r,e) in enumerate(states):
    C[channels.index((q,int(r==2),e)),j]=1
v=zeros(14,1);v[idx[(0,0,1)]]=1
l0=Matrix([-z**-2,1,-z**-2,1]+[0]*10)
l1=Matrix([0]*4+[1,-z**-2,1,-z**-2,-z**-2,1,-z**-2,1,-z**-2,1])
assert l0.T*T==zeros(1,14) and l1.T*T==zeros(1,14)
assert (l0.T*v)[0]==1
assert T[:,2]==T[:,3] and T[:,6]==T[:,7]
keep=[j for j in range(14) if j not in (3,7)]
U=T[:,keep]; V=zeros(12,14)
for j in range(14):V[keep.index({3:2,7:6}.get(j,j)),j]=1
assert U*V==T
W=V*U; a=V*v; D=C*U
assert all(x==0 or x.as_coeff_Mul()[0]>0 for x in W)
assert all(x==0 or x.as_coeff_Mul()[0]>0 for x in D)
A=zeros(13);A[1:13,0]=a;A[1:13,1:13]=W
B=(C*v).row_join(D); b=zeros(13,1);b[0]=1
for n in range(9):
    exact=C*(T**n)*v
    assert all(cancel(x)==0 for x in B*(A**n)*b-exact)
    if n>=1:
        assert all(cancel(x)==0 for x in D*(W**(n-1))*a-exact)
T2=T.subs(z,2)
rows=[0,1,2,4,5,6,7,8,9,10,11,12]
cols=[0,1,2,4,5,6,8,9,10,11,12,13]
assert T2.extract(rows,cols).det()==4
seq=[];st=v
for n in range(26):
    seq.append(C*st);st=T2*st
full=Matrix(13,13,lambda i,j:
  seq[j+(0 if i<=10 else 1)][i if i<=10 else i-7])
tailrows=[0,1,2,4,5,6,7,8,9,10,16,17]
tail=Matrix(12,12,lambda i,j:seq[(tailrows[i]//12)+j+1][tailrows[i]%12])
assert full.det()==-1212467180625/2048
assert tail.det()==1212467180625/2048
print("PASS rank(T)=12: minor at z=2 is 4")
print("PASS full Hankel determinant:",full.det())
print("PASS tail Hankel determinant:",tail.det())
print("PASS exact 13-state and 12-state positive-Laurent identities, n=0..8")
