"""Independent reference: no imports of development or the vendored toolkit.

Coordinates are nonnegative min-zero triples; endpoint reduction repeatedly
rewrites the leftmost neighbouring equal-chart syllables. The main program
uses integer pairs and a right-edge stack. They are compared by exact digests.
"""
from itertools import product, permutations
from pathlib import Path
import hashlib,json
import sympy as s


def canonical(t):
    m=min(t)
    return tuple(a-m for a in t)


def nf(history):
    w=[]
    for v,k,sgn in history:
        t=[0,0,0]; t[k]=sgn
        w.append((v,canonical(t)))
    changed=True
    while changed:
        changed=False
        for i,(v,t) in enumerate(w):
            if t==(0,0,0):
                w.pop(i); changed=True; break
            if i+1<len(w) and w[i+1][0]==v:
                tt=canonical(tuple(a+b for a,b in zip(t,w[i+1][1])))
                w[i:i+2]=[(v,tt)]; changed=True; break
    return w

alphabet=tuple((v,k,sgn) for v in range(4) for k in range(3) for sgn in (-1,1))
h=hashlib.sha256(); profiles=[]
for length in range(4):
    endpoints=set();returns=0
    for digits in product(range(24),repeat=length):
        out=nf(tuple(alphabet[i] for i in digits))
        enc=[[v,*t] for v,t in out]
        h.update((json.dumps(enc,separators=(',',':'))+'\n').encode())
        endpoints.add(tuple(out)); returns+=len(out)==0
    profiles.append((len(endpoints),returns))
primary=json.loads(Path('verification_primary.json').read_text())
assert h.hexdigest()==primary['short_history_digest']
assert profiles==[(a['endpoints'],a['returns']) for a in primary['profiles']]

# Independent signed K4 incidence algebra for the reciprocal-seam quotient.
E=tuple((u,v) for u in range(4) for v in range(u+1,4))
B=s.zeros(6,4)
for i,(u,v) in enumerate(E): B[i,u]=1; B[i,v]=-1
# Operational basis AB, AC, BC and all six normal-form increments.
F=s.Matrix([[1,0,-1,0,1,0],[0,1,-1,0,0,1],[0,0,0,1,-1,1]])
assert B.rank()==3 and F.rank()==3 and F*B==s.zeros(3,4)
assert s.Matrix.hstack(F[:,0],F[:,1],F[:,3])==s.eye(3)
from sympy.matrices.normalforms import smith_normal_form
S=smith_normal_form(B,domain=s.ZZ)
diag=[abs(S[i,i]) for i in range(4) if S[i,i]!=0]
assert diag==[1,1,1]
# Unsigned shared-positive quotient, for contrast only.
U=B.applyfunc(abs)
S2=smith_normal_form(U,domain=s.ZZ)
diag2=[abs(S2[i,i]) for i in range(4) if S2[i,i]!=0]
assert diag2==[1,1,1,2]

# All 24 natural flag permutations descend to operational flat coordinates.
G=list(permutations(range(4)))
actions={}
for g in G:
    P=s.zeros(6)
    for i,(u,v) in enumerate(E):
        j=E.index(tuple(sorted((g[u],g[v]))))
        P[j,i]=1 if g[u]<g[v] else -1
    A=(F*P)[:,[0,1,3]]
    assert A*F==F*P and A.det()==1
    actions[g]=A
for g in G:
    for k in G:
        comp=tuple(g[k[v]] for v in range(4))
        assert actions[g]*actions[k]==actions[comp]

out={'status':'PASS_INDEPENDENT_IMPLEMENTATION_NOT_EXTERNAL_REVIEW',
     'short_history_digest':h.hexdigest(),'short_histories_checked':sum(24**n for n in range(4)),
     'signed_incidence_rank':int(B.rank()),'signed_smith_nonzero':list(map(int,diag)),
     'unsigned_smith_nonzero':list(map(int,diag2)),
     'flat_rotation_actions':24,'flat_rotation_group_products':576,
     'not_imported':['x6_development.py','six_axis.py','vendor/atlas_brc.py']}
Path('verification_reference.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
