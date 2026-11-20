#!/usr/bin/env python3
"""R284BY: exhaustive 4x4 binary frozen-leaf star-Port code certificate."""
import bisect
import hashlib
import itertools
import json
import math
from pathlib import Path

P = 17179869143
D0, D3, Z1, Z2, Z3 = 1120822, 1651130, 390139, 394465, 1497642
EXPECTED_GAP = 41

def signature(c):
    a,b1,b2,b3,u1,a11,x,y,u2,w,a22,z,u3,g,h,r=c
    t,s=6-a11,13-a22
    U=t*s-x*w
    V=-r*U-z*(t*h+x*g)-y*(w*h+s*g)
    p1,p2=s*u1+x*u2,t*u2+w*u1
    q1=-r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
    q2=-r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3=U*u3+p1*g+p2*h
    J=-a*U-b1*p1-b2*p2
    K=-a*V-b1*q1-b2*q2-b3*q3
    return U,V,p1,p2,q1,q2,q3,J,K

def observation(c):
    U,V,p1,p2,q1,q2,q3,J,K=signature(c)
    return (D0*(U*D3+V)-Z1*(p1*D3+q1)-Z2*(p2*D3+q2)
            -Z3*q3+J*D3+K)%P

def reference_determinant(c):
    M=[[-c[4*i+j] for j in range(4)] for i in range(4)]
    for i,d in enumerate((D0,6,13,D3)): M[i][i]+=d
    for j,z in enumerate((Z1,Z2,Z3),1): M[0][j]-=z
    total=0
    for perm in itertools.permutations(range(4)):
        inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        total+=(-1 if inv%2 else 1)*math.prod(M[i][perm[i]] for i in range(4))
    return total%P

def primality_trial(n):
    return n>2 and n%2 and all(n%d for d in range(3,math.isqrt(n)+1,2))

def verify():
    assert P.bit_length()==34 and primality_trial(P)
    universe=list(itertools.product((1,2),repeat=16))
    readout=[observation(c) for c in universe]
    ordered=sorted((v,i) for i,v in enumerate(readout))
    vals=[v for v,_ in ordered]
    gaps=[vals[i+1]-vals[i] for i in range(65535)]+[P-vals[-1]+vals[0]]
    gap=min(gaps)
    assert gap==EXPECTED_GAP and len(set(vals))==65536
    w=gaps.index(gap)
    for k in range(0,65536,257):
        assert readout[k]==reference_determinant(universe[k])
    cross_checks=len(range(0,65536,257))
    for k,v in enumerate(readout):
        for e in (-20,0,20):
            r=(v+e)%P
            j=bisect.bisect_left(vals,r)
            nei=min((j%65536,(j-1)%65536),
                    key=lambda n:min((r-vals[n])%P,(vals[n]-r)%P))
            assert ordered[nei][1]==k
    sha=hashlib.sha256()
    for x in readout: sha.update(x.to_bytes(8,'big'))
    return {
      'schema':'EM_R284BY_34BIT_GAP41_EXACT_CERT_V1',
      'frozen_predecessor':'R284BX_EXACT_28_TO_34_BIT_STAR_PORT_CODE_FRONTIER_20261120.md',
      'matrix_dimensions':[4,4], 'alphabet':[1,2],
      'frozen_leaf_controls':[6,13], 'prime':P,
      'control_d0_d3_z1_z2_z3':[D0,D3,Z1,Z2,Z3],
      'candidate_count':65536, 'distinct_count':len(set(vals)),
      'exact_minimum_circular_gap':gap,
      'number_of_minimum_gaps':gaps.count(gap),
      'integer_noise_correctable':20,
      'real_noise_condition':'0 <= rho < 20.5',
      'independent_leibniz_checks':cross_checks,
      'decoder_checks':3*65536,
      'rowmajor_be64_sha256':sha.hexdigest(),
      'minimum_gap_pair':{
        'a_residue':int(ordered[w][0]),
        'a_matrix_row_major':list(universe[ordered[w][1]]),
        'b_residue':int(ordered[(w+1)%65536][0]),
        'b_matrix_row_major':list(universe[ordered[(w+1)%65536][1]])
      },
      'independent_review':'NOT_REVIEWED'
    }

if __name__=='__main__':
    result=verify()
    target=Path(__file__).with_name('R284BY_34bit_gap41_verification.json')
    target.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True,indent=2))
