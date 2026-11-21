"""Exact raw joint moments for type (10,747) and reusable small-tail sumsets.

This expands the complete native orbit representatives and checks all 24,000
new classes with the original finite-menu checker. The older 49,500-class
centered-moment verification is not rerun.
"""
from pathlib import Path
from hashlib import sha256
from collections import Counter,defaultdict
from functools import lru_cache
from itertools import product,permutations
import argparse,importlib.util,json

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
P=list(product(range(5),repeat=3));PAIRS=((0,1),(0,2),(1,2));ZERO=(0,0,0)
FULL_Q=frozenset(P)
D=frozenset(tuple(a if i==j else 0 for i in range(3)) for j in range(3) for a in (1,4))
PLANES=[frozenset(q for q in P if q[2-i]==0) for i in range(3)]

def points(mask):
    while mask:
        b=mask&-mask;yield b.bit_length()-1;mask-=b

def orbit(ids):
    oriented={tuple(sorted(25*(P[i][perm[0]]*sign[0]*scale%5)+5*(P[i][perm[1]]*sign[1]*scale%5)
                                  +P[i][perm[2]]*sign[2]*scale%5 for i in ids))
              for perm in permutations(range(3)) for sign in product((1,-1),repeat=3) for scale in (1,2)}
    return {sum(1<<(25*((P[i][0]+a)%5)+5*((P[i][1]+b)%5)+(P[i][2]+c)%5) for i in row)
            for row in oriented for a,b,c in P}

def raw_moments(mask):
    ps=[P[i] for i in points(mask)]
    mu=tuple(sum(p[i] for p in ps)%5 for i in range(3))
    q=tuple(sum(p[i]*p[j] for p in ps)%5 for i,j in PAIRS)
    return mu,q

def add(u,v):return tuple((a+b)%5 for a,b in zip(u,v))

@lru_cache(maxsize=None)
def q_sum(a,b):return frozenset(add(u,v) for u in a for v in b)

def signature_sum(a,b):
    result=defaultdict(set)
    for mu,qa in a.items():
        for nu,qb in b.items():result[add(mu,nu)].update(q_sum(qa,qb))
    return {mu:frozenset(qs) for mu,qs in result.items()}

def predicted_two():
    result={}
    for mu in P:
        nz=[i for i,v in enumerate(mu) if v]
        if len(nz)==0:result[mu]=frozenset(q for q in P if 0 in q)
        elif len(nz)==1:result[mu]=PLANES[nz[0]]
        elif len(nz)==2:result[mu]=FULL_Q
    return result

def verify(previous,output):
    spec=importlib.util.spec_from_file_location('moment747_native_checker',previous/'fractional/proof/verify.py')
    native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
    bad,pair=native.observation_tables()
    source=json.loads((HERE/'class_representatives.json').read_text());family=set();orbits=[]
    for entry in source['representatives']:
        current=orbit(entry['points']);assert len(current)==entry['orbit_size'] and not current&family
        family|=current;orbits.append(len(current))
    assert len(family)==source['complete_class_count']==24000
    canonical=b''.join(m.to_bytes(16,'little') for m in sorted(family))
    assert sha256(canonical).hexdigest()==source['canonical_class_sha256']
    signatures=Counter();mu_counts=Counter();fiber_q_counts=Counter();shape_counts=[Counter() for i in range(3)]
    for mask in family:
        assert native.native_class(mask,bad,pair)==(10,747)
        mu,q=raw_moments(mask);nz=[i for i,a in enumerate(mu) if a];assert len(nz)==1
        axis=nz[0];assert q[2-axis]==0
        ps=[P[i] for i in points(mask)];hist=[tuple(sum(p[i]==a for p in ps) for a in range(5)) for i in range(3)]
        assert sorted(hist[axis])==[1,2,2,2,3]
        assert all(hist[j]==(2,2,2,2,2) for j in range(3) if j!=axis)
        deficit=hist[axis].index(1);surplus=hist[axis].index(3)
        assert mu[axis]==(surplus-deficit)%5
        signatures[mu,q]+=1;mu_counts[mu]+=1;fiber_q_counts[axis,deficit,surplus,q]+=1
        for j in range(3):shape_counts[j][tuple(sorted(hist[j]))]+=1
    target={}
    for axis in range(3):
        for a in range(1,5):
            mu=tuple(a if i==axis else 0 for i in range(3));target[mu]=PLANES[axis]
    assert set(signatures)=={(mu,q) for mu,qs in target.items() for q in qs}
    assert len(signatures)==300 and set(signatures.values())=={80}
    assert len(mu_counts)==12 and set(mu_counts.values())=={2000}
    assert len(fiber_q_counts)==1500 and set(fiber_q_counts.values())=={16}
    powers=[{ZERO:frozenset([ZERO])},target]
    for k in range(2,5):powers.append(signature_sum(powers[-1],target))
    assert powers[2]==predicted_two()
    predicted_three={mu:(frozenset(q for q in P if 0 in q) if mu==ZERO else FULL_Q) for mu in P}
    assert powers[3]==predicted_three
    assert powers[4]=={mu:FULL_Q for mu in P}
    expected=[[1,6,19],[300,900,1500],[6361,7017,7625],[15561,15617,15625],[15625,15625,15625]]
    rows=[]
    for k in range(5):
        values=powers[k]
        for m in range(3):
            n=sum(len(qs) for qs in values.values());assert n==expected[k][m]
            if k in [2,3] and m==0:assert values[ZERO]==frozenset(q for q in P if 0 in q)
            if k in [2,3] and m==1:assert values[ZERO]==frozenset(q for q in P if any(a in (0,1,4) for a in q))
            if k in [2,3] and m==2:assert values[ZERO]==FULL_Q
            rows.append({'ten747_classes':k,'balanced_ten_classes':m,'reachable_joint_signatures':n,
                         'mean_values':len(values),'q_values_at_zero_mean':len(values.get(ZERO,()))})
            values=signature_sum(values,{ZERO:D})
    result={'schema':'TEN747_RAW_JOINT_MOMENTS_AND_TAILS_V1','native_classes_checked':24000,'native_orbit_sizes':orbits,
            'signature_values':300,'classes_per_signature':80,'nonzero_axis_means':12,'classes_per_mean':2000,
            'marginal_and_q_values':1500,'classes_per_marginal_and_q':16,
            'canonical_class_sha256':source['canonical_class_sha256'],
            'coordinate_shapes':[{'axis':j,'shapes':[{'counts':list(s),'classes':n} for s,n in sorted(counter.items())]} for j,counter in enumerate(shape_counts)],
            'tail_sumsets':rows,
            'scope':'Complete raw (mu,Q) support for type (10,747) and necessary abstract signature-sum conditions. Balanced-ten D support is inherited from the already verified types (10,744)/(10,768); no disjoint geometric realization or global lower bound is asserted.'}
    output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--previous',type=Path,default=ROOT/'delivery');p.add_argument('--output',type=Path,default=HERE/'verification.json');a=p.parse_args();verify(a.previous,a.output)
