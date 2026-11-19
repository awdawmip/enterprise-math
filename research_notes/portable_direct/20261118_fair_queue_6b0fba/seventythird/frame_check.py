"""Exhaustive finite-source comparison, independent of the closed formula."""
from collections import Counter
import importlib.util
from itertools import permutations, product, combinations_with_replacement
from math import gcd
import json
from pathlib import Path
from hashlib import sha256
import argparse

P = list(permutations(range(4)))
sign = [(-1)**sum(a>b for i,a in enumerate(p) for b in p[i+1:]) for p in P]


def stab(x,q):
    return tuple(j for j,p in enumerate(P)
        if all((sign[j]*x[p[i]]-x[i])%q==0 for i in range(4)))


def free_count(q):
    h,g = gcd(2,q),gcd(4,q)
    return q**3-(4+9*h)*q+6*(g+h*h)


def primitive_count(r):
    ans=r*r
    for p in range(2,r+1):
        if r%p==0 and all(p%i for i in range(2,p)):
            ans=ans//p**2*(p**2-1)
    return 16*ans -16*(r==1)-8*(r==3)


def ordinary_free(x):
    return sum(all(sign[j]*x[p[i]]==x[i] for i in range(4)) for j,p in enumerate(P)) == 1


def bind(repo):
    path=repo/"scripts/check_a3_recursive_shell_alignment_tomography.py"
    digest=sha256(path.read_bytes()).hexdigest()
    assert digest=="28f3000ea052b78b7b7ec3ba34c3d880ed98666b61eef2888d1890cd11e61b04"
    spec=importlib.util.spec_from_file_location("a3_frozen_source",path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert tuple(P)==module.G
    return module,digest


def measure(repo):
    m,digest=bind(repo)
    mods={}
    for q in range(1,26):
        h=Counter(); reg_primitive=0
        # Enumerate every scalar multiplicity type; each permutation has the same stabilizer order.
        from math import factorial,prod
        for x in combinations_with_replacement(range(q),4):
            if sum(x)%q: continue
            mult=24//prod(factorial(v) for v in Counter(x).values())
            integral=x[:3]+(x[3]-sum(x),)
            source_stab=tuple(j for j,g in enumerate(m.G) if all((a-b)%q==0 for a,b in zip(integral,m.r_act(g,integral))))
            assert source_stab == stab(x,q)
            s=len(source_stab);h[s]+=mult
            reg_primitive += mult*(s==1)*(gcd(q,*x)==1)
        assert sum(h.values())==q**3 and h[1]==free_count(q)
        mods[q]={"fiber":dict(sorted(h.items())),"regular_primitive":reg_primitive}
    shells={}
    for r in range(1,16):
        possible=0;regular=0;allpoints=0
        for x in combinations_with_replacement(range(-r,r+1),4):
            if sum(x) or max(map(abs,x))!=r: continue
            mult=24//prod(factorial(v) for v in Counter(x).values())
            allpoints+=mult
            if gcd(*x)!=1:continue
            possible+=mult
            regular+=mult*ordinary_free(x)
        assert allpoints==16*r*r+2 and regular==primitive_count(r)
        shells[r]=[possible,regular]
    cross=(0,1,1,-2)
    small={q:stab(cross,q) for q in (2,3,4,6)}
    assert set(small[2])&set(small[3])=={0} and len(small[6])==1
    for q in range(2,45):
        k=q//2
        x=(k,-k,1,-1) if q%2==0 and k>=2 else (k+1,-k,-k-1,k)
        if q==2:x=cross
        assert gcd(*x)==1 and ordinary_free(x) and len(stab(x,q))>1
    witness=(0,1,1,-2)
    y1={m.prefix_move(4,2,g,witness) for g in m.G}
    y2={m.prefix_move(3,2,g,witness) for g in m.G}
    assert y1=={witness} and len(y2)==24
    quotient_classes=[len({tuple(z%q for z in y) for y in y2}) for q in range(1,26)]
    assert quotient_classes[:3]==[1,6,8] and quotient_classes[3:]==[24]*22
    def mod4(x):return tuple(v%4 for v in x)
    x=(1,-1,0,0); y=(-3,3,0,0)
    dx=m.prefix_move(3,1,m.SWAP23,x); dy=m.prefix_move(3,1,m.SWAP23,y)
    assert mod4(x)==mod4(y) and mod4(dy) not in {mod4(dx),mod4(m.r_act(m.SWAP12,dx))}
    return dict(frozen_source_sha256=digest,modulus_histograms=mods,primitive_shells=shells,
           native_scale_square={"n":3,"d":2,"point":witness,"upper_endpoints":len(y1),"lower_endpoints":len(y2),
                                "lower_endpoint_counts_moduli_1_to_25":quotient_classes},
           failure_without_shell={"input":[x,y],"outputs":[dx,dy],"outputs_mod_four":[mod4(dx),mod4(dy)]},
           CRT_witness=list(cross),stabilizing_pullback_permutations={q:[P[j] for j in s] for q,s in small.items()},
           universal_ball_bad_witness_checked_q_2_through=44)
if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    print(json.dumps(measure(parser.parse_args().repo),sort_keys=True,indent=2))
