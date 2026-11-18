"""Exact modular and cyclotomic checks for a conditional cyclic propagation model."""
import json
from collections import Counter
from functools import cache
from itertools import combinations, product
from math import gcd, lcm


def join(r, m, s, n):
    """Intersect x=r mod m and x=s mod n."""
    h = gcd(m, n)
    if (r-s) % h:
        return None
    n1 = n // h
    k = (s-r) // h * pow(m//h, -1, n1) % n1
    return (r+m*k) % lcm(m,n), lcm(m,n)


def linear(a, b, m):
    g = gcd(a,m)
    if b % g:
        return None
    m1 = m//g
    return b//g * pow(a//g,-1,m1) % m1, m1


def time_space(q, K, v, b):
    k = K[0]
    rows = [(q//gcd(q,i-k), v+b*(i+k)) for i in K[1:]]
    T = 1
    for (m,s),(n,z) in combinations(rows, 2):
        g = gcd(m,n)
        T = lcm(T, g//gcd(g,s-z))
    r, L = 0, 1
    for m,s in rows:
        r,L = join(r,L,s*T,m)
    return T,r,L


def earliest(T, r, L, x):
    cls = linear(r,x,L)
    if cls is None:
        return None
    j,M = cls
    return T*j,T*M


def direct_focus(q, K, v, b, x, t):
    return len({(i*x-t*(v*i+b*i*i))%q for i in K}) == 1


def verify_focus():
    trials = 0
    for q in (3,5,9):
        spectra = [K for m in range(1,4) for K in combinations(range(q),m)]
        for K,(v,b) in product(spectra, product(range(q),repeat=2)):
            T,r,L = time_space(q,K,v,b)
            for x in range(q):
                times = [t for t in range(q) if direct_focus(q,K,v,b,x,t)]
                rule = earliest(T,r,L,x)
                assert times == ([] if rule is None else list(range(rule[0],q,rule[1])))
            trials += 1
    examples = []
    for q,K,v,b in [(45,(0,3,8),1,1),(315,(1,10,16,22),5,1),(15,(0,5),1,1)]:
        T,r,L = time_space(q,K,v,b)
        foci = [x for x in range(q) if direct_focus(q,K,v,b,x,T)]
        assert foci == list(range(r,q,L))
        assert all(not any(direct_focus(q,K,v,b,x,t) for x in range(q)) for t in range(1,T))
        examples.append({"q":q,"K":K,"v":v,"b":b,"first_positive_time_anywhere":T,
                         "spatial_modulus":L,"first_positions":foci})
    return {"models_with_all_sites_and_times_compared":trials,"examples":examples}


def rem(p,f):
    p = list(p)
    for i in range(len(p)-1,len(f)-2,-1):
        a=p[i]
        for j,x in enumerate(f):
            p[i-len(f)+1+j] -= a*x
    return tuple(p[:len(f)-1])


@cache
def cyclotomic(q):
    u=[-1]+[0]*(q-1)+[1]
    for d in range(1,q):
        if q%d==0:
            f=cyclotomic(d)
            quotient=[0]*(len(u)-len(f)+1)
            for i in reversed(range(len(quotient))):
                quotient[i]=u[i+len(f)-1]
                for j,c in enumerate(f):
                    u[i+j]-=quotient[i]*c
            assert not any(u)
            u=quotient
    return tuple(u)


def intens_numerator(q, v, b, t, x, amplitudes):
    coeff=[0]*q
    phases=[(k*x-t*(v*k+b*k*k))%q for k in range(len(amplitudes))]
    for i,a in enumerate(amplitudes):
        for j,z in enumerate(amplitudes):
            coeff[(phases[i]-phases[j])%q]+=a*z
    return rem(coeff,cyclotomic(q))


def point_rows(q):
    arows={}
    for a,x in product(range(q),repeat=2):
        d=gcd(q,a)
        n=intens_numerator(q,0,a,1,x,[1]*q)
        assert n == (d*q if x%d==0 else 0,)+(0,)*(len(cyclotomic(q))-2)
        arows[a,x]=n[0]
    return arows


def point_and_readout():
    point_verified=[]
    for q in (3,5,7,9,11,15,21,25,27):
        rows=point_rows(q)
        point_verified.append(q)
        if q!=15:
            continue
        classes={}
        frames={}
        for v,b in product(range(q),repeat=2):
            movie=tuple(rows[b*t%q,(x-v*t)%q] for t in range(q) for x in range(q))
            frame=movie[q:2*q]
            label=gcd(b,q),v%gcd(b,q)
            assert classes.setdefault(label,movie)==movie
            assert frames.setdefault(frame,label)==label
        assert len(set(classes.values()))==len(classes)==len(frames)==24
    result={}
    for q,weights in [(3,(1,2,4)),(5,(1,1,2)),(15,(1,1,2)),(15,(1,2,1))]:
        groups={}
        for v,b in product(range(q),repeat=2):
            frame=tuple(intens_numerator(q,v,b,1,x,weights) for x in range(q))
            groups.setdefault(frame,[]).append((v,b))
        if weights[0]!=weights[2]:
            assert len(groups)==q*q
        else:
            for pts in groups.values():
                v,b=pts[0]
                assert set(pts)=={(v,b),((v+4*b)%q,(-b)%q)}
        result[f"{q}_{weights}"]={"class_count":len(groups),"size_histogram":dict(Counter(map(len,groups.values())))}
    return {"exact_point_moduli":point_verified,"point_movie_and_single_frame_classes_at_15":24,
            "single_probe_intensity_classes":result}


def probe_index(q, probes):
    rows=[(q//gcd(q,i-j),i+j) for i,j in probes]
    L=lcm(*(m for m,_ in rows))
    T=1
    for (m,c),(n,d) in combinations(rows,2):
        h=gcd(m,n)
        T=lcm(T,h//gcd(h,c-d))
    groups=Counter(tuple((v+c*b)%m for m,c in rows) for v,b in product(range(q),repeat=2))
    assert set(groups.values())=={q*q//(L*T)}
    return {"probes":probes,"classes":len(groups),"fiber_size":q*q//(L*T)}


if __name__ == "__main__":
    print(json.dumps({"focus":verify_focus(),"gauss_and_tomography":point_and_readout(),
                      "two_mode_probe_sets_mod_15":[probe_index(15,p) for p in
                         [[(0,1)],[(0,1),(0,2)],[(0,3),(0,5)],[(0,1),(3,4)]]]},
                     indent=2,sort_keys=True))
