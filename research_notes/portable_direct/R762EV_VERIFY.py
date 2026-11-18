#!/usr/bin/env python3
"""R762EV: exact integer cubic BRC second-trit repair and q=27 finite proof checks."""
import hashlib
import json
B=((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))
Q=27
SIZE=Q**3

def idx(x,y,z):
    return (x*Q+y)*Q+z

def permutations(scale):
    return [[idx((x-dx*scale)%Q,(y-dy*scale)%Q,(z-dz*scale)%Q)
        for x in range(Q) for y in range(Q) for z in range(Q)] for dx,dy,dz in B]

def step(v,perms,mod):
    return [sum(v[p[i]] for p in perms)%mod for i in range(SIZE)]

U=permutations(1)
W=permutations(3)
e0=[0]*SIZE
e0[0]=1
powers=[e0]
for n in range(26):
    powers.append(step(powers[-1],U,9))

A=[0]*SIZE
for dx,dy,dz in B:
    A[idx(3*dx,3*dy,3*dz)]+=1

P3_exact=[0]*SIZE
for dx1,dy1,dz1 in B:
    for dx2,dy2,dz2 in B:
        for dx3,dy3,dz3 in B:
            P3_exact[idx(dx1+dx2+dx3,dy1+dy2+dy3,dz1+dz2+dz3)]+=1

assert all((x-y)%3==0 for x,y in zip(P3_exact,A))
D=[(x-y)//3 for x,y in zip(P3_exact,A)]
assert sum(D)==70 and D[idx(1,0,0)]==1

As=[e0]
for m in range(8):
    As.append(step(As[-1],W,9))
Dm=[None,[d%3 for d in D]]
for m in range(2,9):
    Dm.append(step(Dm[-1],W,3))

for m in range(9):
    pred=[(As[m][i]+(3*m*Dm[m][i] if m else 0))%9 for i in range(SIZE)]
    assert pred==powers[3*m],('repair',m)
    if m>0:
        assert powers[3*m][idx(1,0,0)]==(3*m)%9
        assert As[m][idx(1,0,0)]==0
        assert (As[m]==powers[3*m])==(m%3==0)
    for r in range(3):
        evolved=pred
        for _ in range(r):
            evolved=step(evolved,U,9)
        assert evolved==powers[3*m+r],('remainder',m,r)

result={
    'schema':'R762EV_SECOND_TRIT_CUBIC_REPAIR_CERTIFICATE_V1',
    'model':'P=1+X+Z+XY+YZ+XYZ in Z[(Z/27)^3]',
    'exact_cubic_branch_triples':216,
    'D_augmentation':sum(D),
    'D_coefficient_at_X':D[idx(1,0,0)],
    'D_nonzero_mod3_cells':sum(v%3!=0 for v in D),
    'D_mod3_sha256':hashlib.sha256(bytes(v%3 for v in D)).hexdigest(),
    'Q':Q,'m_tested':[0,8],
    'vector_cells':SIZE,
    'full_Q27_mod9_cubic_corrected_vector_comparisons':9*SIZE,
    'full_Q27_mod9_r_0_1_2_comparisons':27*SIZE,
    'exact_mod9_equality iff 3 divides m, for m1..8':True,
    'witness':'coefficient at (1,0,0) of P^3m is 3m (mod 9); iota(P_q^m) coefficient is 0',
    'arithmetic':'exact integer cube + 6 named cyclic shifts mod 9 and mod 3, no floats',
    'result':'PASS','independent_review':'NOT_REVIEWED'
}
print(json.dumps(result,indent=2))
