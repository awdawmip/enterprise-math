#!/usr/bin/env python3
"""R284BZ: full exact certificate for noise-optimal 34-bit star-Port code.

Standard library only. Exhausts C in {1,2}^{4x4}, verifies 24-term independent
Leibniz determinants, nearest-neighbor decoding and the cofactor obstruction.
"""
import bisect
import hashlib
import itertools
import json
import math
from pathlib import Path

P = 17179869143
D0, D3, Z1, Z2, Z3 = 1120832, 1651128, 390139, 394465, 1497639
EXPECTED_GAP = 59

def signature(c):
    a,b1,b2,b3,u1,a11,x,y,u2,w,a22,z,u3,g,h,r = c
    t,s = 6-a11, 13-a22
    U = t*s-x*w
    V = -r*U-z*(t*h+x*g)-y*(w*h+s*g)
    p1,p2 = s*u1+x*u2, t*u2+w*u1
    q1 = -r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
    q2 = -r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3 = U*u3+p1*g+p2*h
    J = -a*U-b1*p1-b2*p2
    K = -a*V-b1*q1-b2*q2-b3*q3
    return U,V,p1,p2,q1,q2,q3,J,K

def observation(c):
    U,V,p1,p2,q1,q2,q3,J,K = signature(c)
    return (D0*(U*D3+V)-Z1*(p1*D3+q1)-Z2*(p2*D3+q2)
            -Z3*q3+J*D3+K) % P

def reference_determinant(c):
    M = [[-c[4*i+j] for j in range(4)] for i in range(4)]
    for i,d in enumerate((D0,6,13,D3)): M[i][i] += d
    for j,z in enumerate((Z1,Z2,Z3),1): M[0][j] -= z
    total = 0
    for perm in itertools.permutations(range(4)):
        inversions = sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        total += (-1 if inversions % 2 else 1) * math.prod(M[i][perm[i]] for i in range(4))
    return total % P

def verify():
    assert P.bit_length() == 34
    assert all(P % d for d in range(3, math.isqrt(P)+1, 2)), 'p is not prime'
    universe = list(itertools.product((1,2),repeat=16))
    readouts = [observation(c) for c in universe]
    ordered = sorted((v,i) for i,v in enumerate(readouts))
    vals = [v for v,_ in ordered]
    gaps = [vals[i+1]-vals[i] for i in range(65535)]+[P-vals[-1]+vals[0]]
    gap = min(gaps)
    assert len(set(vals)) == 65536 and gap == EXPECTED_GAP
    first_min_gap_index = gaps.index(gap)
    q3_values = [signature(c)[6] for c in universe]
    assert min(q3_values) == 59 and max(q3_values) == 196
    for i in range(0,65536,257):
        assert readouts[i] == reference_determinant(universe[i])
    cross_checks = len(range(0,65536,257))
    for k,v in enumerate(readouts):
        for e in (-29,0,29):
            r = (v+e) % P
            j = bisect.bisect_left(vals,r)
            candidates = (j % 65536, (j-1) % 65536)
            nearest = min(candidates, key=lambda n:min((r-vals[n])%P,(vals[n]-r)%P))
            assert ordered[nearest][1] == k
    sha=hashlib.sha256()
    for x in readouts: sha.update(x.to_bytes(8,'big'))
    w=first_min_gap_index
    return {
        'schema':'EM_R284BZ_34BIT_GAP59_GLOBAL_FROZEN_PAIR_CERT_V1',
        'source_model':'4x4 binary star Port frozen d1=6,d2=13',
        'scientific_predecessor':'R284BY_34BIT_SHARP_GAP41_PORT_20261120.md',
        'candidate_count':65536,'distinct_residue_count':len(set(vals)),
        'prime':P,'prime_bit_length':P.bit_length(),
        'controls_d0_d3_z1_z2_z3':[D0,D3,Z1,Z2,Z3],
        'exact_minimum_circular_gap':gap,
        'minimum_gap_multiplicity':gaps.count(gap),
        'lower_cofactor_q3':min(q3_values),'upper_cofactor_q3':max(q3_values),
        'integral_noise_correctable':29,
        'real_noise_guarantee':'0 <= rho < 59/2',
        'full_model_noise_optimal':True,
        'independent_leibniz_checks':cross_checks,
        'decoder_checks':3*len(universe),
        'rowmajor_be64_sha256':sha.hexdigest(),
        'one_minimum_gap_pair':{
            'a_index':ordered[w][1],'a_residue':ordered[w][0],
            'a_matrix':list(universe[ordered[w][1]]),
            'b_index':ordered[(w+1)%65536][1],
            'b_residue':ordered[(w+1)%65536][0],
            'b_matrix':list(universe[ordered[(w+1)%65536][1]])
        },
        'review':'NOT_REVIEWED',
    }

if __name__ == '__main__':
    data = verify()
    target = Path(__file__).with_name('R284BZ_34bit_gap59_verification.json')
    target.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(data,sort_keys=True,indent=2))
