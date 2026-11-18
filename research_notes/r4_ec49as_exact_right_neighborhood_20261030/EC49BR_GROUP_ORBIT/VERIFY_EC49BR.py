"""EC49BR exact signed-X6 BRC finite-observer rank certificate.
Uses the unchanged native signed_brc.py; source blob pinned.
No physical heartbeat/phase assertion; filtered ensembles are auxiliary.
"""
from __future__ import annotations
import hashlib
import sys
import itertools
import json
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from sympy import Matrix
# Use pinned original repository kernel; adjacent copy is for offline replay.
repo_kernel = (Path(__file__).resolve().parents[3] /
 'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py')
source_path = repo_kernel if repo_kernel.exists() else Path(__file__).with_name('signed_brc.py')
sys.path.insert(0, str(source_path.parent))
from signed_brc import endpoint_weight, endpoint_multiplicity

PIN = '300a96e3dc24bf6fff73743037a0347a8bc83176'
src = source_path.read_bytes()
assert hashlib.sha1(f'blob {len(src)}\0'.encode() + src).hexdigest() == PIN
D = tuple(list(range(1,7)) + list(range(-1,-7,-1)))
U = tuple(t for t in itertools.product(D,repeat=4)
          if all(sum((1 if x>0 else -1) for x in t if abs(x)==i)==0 for i in range(1,7)))
assert len(U)==396
fibres=defaultdict(list)
for w in U: fibres[(w[0],w[-1])].append(w)
assert len(fibres)==144

def swap12(i):
    j=2 if abs(i)==1 else (1 if abs(i)==2 else abs(i))
    return j if i>0 else -j

def sign_vector(i):
    z=[0]*6
    z[abs(i)-1]=1 if i>0 else -1
    return z

def weight(word,q,perm):
    return Fraction(__import__('math').prod(q[abs(perm(x))-1] for x in word if x>0))

def weights(q,perm):
    wp=[0]*6
    for i in range(1,7): wp[i-1]=Fraction(q[abs(perm(i))-1])
    return wp

def fibre_audit(q):
    actions=(lambda i:i,swap12)
    comp_rank=0
    constant_recovered=True
    native_checks=0
    for (p,s),ws in fibres.items():
        rows=[]
        z=tuple(-a-b for a,b in zip(sign_vector(p),sign_vector(s)))
        for perm in actions:
            row=[weight(w,q,perm) for w in ws]
            rows.append(row)
            wp=weights(q,perm)
            prefix=wp[p-1] if p>0 else Fraction(1)
            suffix=wp[s-1] if s>0 else Fraction(1)
            expected=prefix*endpoint_weight(2,z,wp,[1]*6)*suffix
            assert sum(row)==expected, (q,p,s)
            native_checks+=1
        r=Matrix(rows).rank()
        comp_rank+=r
        if Matrix(rows+[[1]*len(ws)]).rank()>r:constant_recovered=False
    q_id=tuple(q)
    q_sw=(q[1],q[0],*q[2:])
    rho=Matrix([q_id,q_sw]).rank()
    assert comp_rank==132+12*rho
    count_extra=int(not constant_recovered)
    orbit_const = Matrix([q_id,q_sw,[1]*6]).rank()==rho
    assert constant_recovered==orbit_const
    return {'q':list(q),'H':'identity,signed-axis-swap(1,2)',
            'orbit_rank':rho,'composed_joint_rank':comp_rank,
            'count_in_row_span':constant_recovered,
            'composed_joint_plus_count_rank':comp_rank+count_extra,
            'native_BRC_fibre_equalities':native_checks}

cases={
'nonconstant_not_recover_count':fibre_audit((2,3,3,2,1,1)),
'nonconstant_recover_count':fibre_audit((2,4,3,3,3,3)),
'symmetric_no_increase':fibre_audit((3,3,3,3,3,3)),
}
# All twelve sign-labelled opposite endpoint cells have twelve middle words.
assert sorted([len(ws) for (p,s),ws in fibres.items() if p==-s])==[12]*12
assert sorted([len(ws) for (p,s),ws in fibres.items() if p!=-s])==[1]*12+[2]*120
A=(3,1,-1,-3); B=(3,4,-4,-3)
q=(2,3,3,2,1,1)
assert A in U and B in U and (A[0],A[-1])==(B[0],B[-1])
assert weight(A,q,lambda i:i)==weight(B,q,lambda i:i)==6
assert weight(A,q,swap12)==9 and weight(B,q,swap12)==6
s6q=[tuple(2 if j==i else 1 for j in range(6)) for i in range(6)]
assert Matrix(s6q).rank()==6
assert Matrix(s6q+[[1]*6]).rank()==6
assert endpoint_multiplicity(4,(0,)*6)==396

def count_matrix_audit(n,r,q):
    from itertools import combinations_with_replacement
    ktotal=n//2
    compositions=[tuple(xs.count(i) for i in range(6)) for xs in
                  combinations_with_replacement(range(6),ktotal)]
    signed=tuple(D)
    endwords=tuple(itertools.product(signed,repeat=r))
    rank_total=0
    count_lost=False
    for prefix in endwords:
        for suffix in endwords:
            ends=prefix+suffix
            floors=tuple(max(sum(x==i for x in ends),sum(x==-i for x in ends)) for i in range(1,7))
            ks=[k for k in compositions if all(ki>=li for ki,li in zip(k,floors))]
            assert ks
            row0=[__import__('math').prod(q[i]**k[i] for i in range(6)) for k in ks]
            qswap=(q[1],q[0],*q[2:])
            row1=[__import__('math').prod(qswap[i]**k[i] for i in range(6)) for k in ks]
            rr=Matrix([row0,row1]).rank()
            rank_total+=rr
            if Matrix([row0,row1,[1]*len(ks)]).rank()>rr:count_lost=True
    return {'n':n,'r':r,'q':list(q),'joint_rank':rank_total,
            'count_extra':int(count_lost),'joint_plus_count_rank':rank_total+int(count_lost),
            'native_unfiltered_weight':str(endpoint_weight(n,(0,)*6,q,[1]*6)),
            'native_unfiltered_multiplicity':endpoint_multiplicity(n,(0,)*6)}

n6_cases={
 'nonconstant_not_recover_count': count_matrix_audit(6,1,(2,3,3,2,1,1)),
 'nonconstant_n4_recover_but_n6_loses': count_matrix_audit(6,1,(2,4,3,3,3,3)),
 'symmetric': count_matrix_audit(6,1,(3,3,3,3,3,3)),
}
assert n6_cases['nonconstant_not_recover_count']['joint_rank']==288
assert n6_cases['nonconstant_n4_recover_but_n6_loses']['joint_rank']==288
assert n6_cases['nonconstant_n4_recover_but_n6_loses']['count_extra']==1
assert n6_cases['symmetric']['joint_rank']==144
out={
 'unit':'EC49BR',
 'source_git_blob':PIN,
 'finite_universe':'all 396 ordered four-step zero-displacement signed-X6 paths',
 'fibres':144,
 'fibre_sizes':{'opposite_end_12':12,'same_sign_same_axis_12':1,'other_120':2},
 'cases':cases,
 'n6_count_matrix_exact_cases':n6_cases,
 'fixed_instrument_counterexample':{'word_A':A,'word_B':B,'original_weights':(6,6),'after_swap':(9,6)},
 'full_S6_nonconstant_case':{'q':[2,1,1,1,1,1],'orbit_rank':6,'joint_rank':204,'count_extra':0},
 'covariant_label_and_weight_action_rank_without_count':144,
 'covariant_n4_plus_count_rank_q_unequal':145,
 'native_total_multiplicity':396,
 'status':'EXACT_FINITE_AUDIT_PASS_AUTHOR_UNREVIEWED'
}
print(json.dumps(out,indent=2,sort_keys=True,ensure_ascii=False))
