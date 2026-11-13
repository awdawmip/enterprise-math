#!/usr/bin/env python3
"""R474 exact finite checker. Uses arbitrary-precision integers only."""
from itertools import product, combinations
from hashlib import sha256
import json

def aget(a,k): return a[k] if 0 <= k < len(a) else 0

def det(M):
    if len(M)==1: return M[0][0]
    if len(M)==2: return M[0][0]*M[1][1]-M[0][1]*M[1][0]
    x,y,z=M
    return x[0]*(y[1]*z[2]-y[2]*z[1])-x[1]*(y[0]*z[2]-y[2]*z[0])+x[2]*(y[0]*z[1]-y[1]*z[0])

def d2(a,j): return aget(a,j)**2-aget(a,j-1)*aget(a,j+1)
def d3(a,j): return det([[aget(a,j+c-i) for c in range(3)] for i in range(3)])

def all_ordinary(a):
    n=len(a)-1
    for m in (1,2,3):
        for C in combinations(range(n+m),m):
            d=det([[aget(a,c-i) for c in C] for i in range(m)])
            if d<0: return False,(m,C,d)
    return True,None

def exact_edge_witness(a):
    n=len(a)-1
    assert all(d2(a,j)>=0 for j in range(n+1))
    for j in range(1,n):
        if d2(a,j)==0:
            assert d2(a,j-1)>0
            C=(j,j+1,n+1)
            D=det([[aget(a,c-i) for c in C] for i in range(3)])
            assert D<0 and a[j]*D==-a[n]*a[j+1]*d2(a,j-1)
            return (j,C,D)
    return None

def run():
    counts=[]; stream=sha256()
    for n,b in ((2,6),(3,6),(4,6),(5,6),(6,4)):
        sharp=weak=weak_false=0
        for a in product(range(1,b+1),repeat=n+1):
            d2s=[d2(a,j) for j in range(n+1)]
            d3s=[d3(a,j) for j in range(n+1)]
            S=all(x>0 for x in d2s) and all(x>=0 for x in d3s)
            W=all(x>=0 for x in d2s+d3s)
            if S:
                sharp+=1
                assert all_ordinary(a)[0], (n,a)
            if W:
                weak+=1
                if not S:
                    WIT=exact_edge_witness(a)
                    assert WIT is not None
                    pf3,bad=all_ordinary(a)
                    assert not pf3, (n,a,bad)
                    weak_false+=1
            stream.update(f'{n}:{a}:{int(S)}:{int(W)};'.encode())
        counts.append({'n':n,'alphabet':[1,b],'sequences':b**(n+1),
                       'sharp_local_positive':sharp,'nonstrict_local_pass':weak,
                       'nonstrict_local_false_positive':weak_false})
    for n in (3,4,7):
        for q in (1,2,3):
            a=tuple(q**j for j in range(n+1))
            assert all(d2(a,j)>=0 and d3(a,j)>=0 for j in range(n+1))
            j,C,D=exact_edge_witness(a)
            assert (j,C,D)==(1,(1,2,n+1),-q**(n+1))
    obj={'schema':'R474_EXACT_INTEGER_VERIFICATION_V1',
         'scope':counts,'all_finite_input_classification_sha256':stream.hexdigest(),
         'geometric_family':'n>=3,q>0,a_j=q^j: weak local D2/D3 nonnegative but minor cols(1,2,n+1)=-q^(n+1)',
         'boundary_verification':{'n':[3,4,7],'q':[1,2,3],'all_pass':True},
         'status':'R474_EXACT_PASS'}
    print(json.dumps(obj,ensure_ascii=False,indent=2))
    return obj

if __name__=='__main__': run()
