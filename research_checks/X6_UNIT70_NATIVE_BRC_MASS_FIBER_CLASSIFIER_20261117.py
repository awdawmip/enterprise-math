"""Unit70: signed Z3 can3/G/T fiber classifies exact N-BRC ambiguity.
Frozen native science pin 59538f585d037d09ef687b28715c4bc1a3f9fe03.
"""
from math import factorial, isqrt, prod
from collections import Counter
import json

def require(condition, reason):
    if not condition:
        raise ValueError(reason)

def observe(z):
    h = min(z)
    r = tuple(x-h for x in z)
    return r, sum(x*x for x in z), sum(abs(x) for x in z)

def recover(r, g, t):
    R, Q = sum(r), sum(x*x for x in r)
    D = R*R + 3*(g-Q)
    if D < 0 or isqrt(D)**2 != D:
        return ()
    roots = []
    for n in (-R-isqrt(D), -R+isqrt(D)):
        if n%3:
            continue
        h = n//3
        z = tuple(x+h for x in r)
        if sum(abs(x) for x in z)==t and sum(x*x for x in z)==g and z not in roots:
            roots.append(z)
    return tuple(sorted(roots))

def n_brc(z):
    return factorial(sum(map(abs,z)))//prod(factorial(abs(x)) for x in z)

def classify(r,g,t):
    zs = recover(r,g,t)
    if len(zs)==0: return 'empty',zs
    if len(zs)==1: return 'unique',zs
    R=sum(r)
    require(R%3==0, "two roots must have integer mean depth")
    v=tuple(x-R//3 for x in r)
    s=abs(zs[0][0]-zs[1][0])//2
    require(s>=1 and abs(zs[0][0]-zs[1][0])%2==0, "invalid distinct-depth parity")
    balanced = sorted(v)==[-max(map(abs,v)),0,max(map(abs,v))]
    if not balanced:
        require(s >= max(map(abs,v)), "unbalanced doubleton violates orthant condition")
    counts=[n_brc(z) for z in zs]
    require((counts[0]==counts[1]) == balanced, "N_BRC equal-fiber criterion violated")
    return 'two_equal' if balanced else 'two_distinct',zs

def main():
    stats=Counter()
    unique_obs=set()
    witnesses={}
    for a in range(-15,16):
        for b in range(-15,16):
            for c in range(-15,16):
                z=(a,b,c); key=observe(z)
                typ, zs=classify(*key)
                require(z in zs, "missing source displacement")
                stats['raw_input']+=1
                if key not in unique_obs:
                    unique_obs.add(key)
                    stats[typ]+=1
                    if typ not in witnesses or sum(abs(x) for x in z)<witnesses[typ]['T']:
                        witnesses[typ]={'r':key[0],'G':key[1],'T':key[2], 'endpoints':zs,'N_BRC':tuple(map(n_brc,zs))}
    require(stats['raw_input']==31**3, 'incorrect raw domain cardinality')
    require(sum(stats[k] for k in ('unique','two_equal','two_distinct'))==len(unique_obs), 'incorrect fiber accounting')
    print(json.dumps({'scope':'signed native selected Z3 slice; raw triples [-15,15]^3', 'stats':stats,'witnesses':witnesses,'checks':'all exact integers, independent of optimization assert','status':'AUTHOR_SCOPED_FINITE_EXECUTED_UNREVIEWED_NOT_ADMITTED'},indent=2))

if __name__=='__main__': main()
