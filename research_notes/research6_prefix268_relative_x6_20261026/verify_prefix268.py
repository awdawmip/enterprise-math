#!/usr/bin/env python3
"""Exact independent enumerations of native X6 signed N-BRC endpoint fibers.
This is path-formal N-BRC combinatorics; never physical heartbeat or amplitude.
Method A: labeled signed-path recurrence, counting multiplicity.
Method B: translated-orbit class count by weakly ordered coordinate gaps.
"""
from collections import defaultdict
from math import factorial

M=6
E=tuple((i,sgn) for i in range(M) for sgn in (-1,1))

def relative(z):
    u=min(z)
    return tuple(t-u for t in z)

def compositions(total):
    if total==0:
        yield ()
    else:
        for first in range(1,total+1):
            for rest in compositions(total-first):
                yield (first,)+rest

def gap_spheres(K):
    """A_6(x): one tuple of 6 coordinate levels per orbit, ordered gaps positive."""
    counts=[0]*(K+1)
    for block_sizes in compositions(6):
        denom=1
        for b in block_sizes: denom*=factorial(b)
        multiplicity=factorial(6)//denom
        prefixes=[]
        acc=0
        for b in block_sizes[:-1]:
            acc+=b
            prefixes.append(min(acc,6-acc))
        # Each between-block gap >=1; exact polynomial product (x^d+x^2d+...)
        poly=[0]*(K+1); poly[0]=1
        for d in prefixes:
            next_poly=[0]*(K+1)
            for i,v in enumerate(poly):
                if v==0: continue
                for j in range(i+d,K+1,d): next_poly[j]+=v
            poly=next_poly
        for k,v in enumerate(poly):counts[k]+=multiplicity*v
    return counts

def supported_length_count(k, a):
    # Source-backed signed X6 path reachability, allowing inverse-step pairs.
    return sum(a[j] for j in range(k%2,k+1,2))

def actual_path_dp(K):
    # N-BRC: each distinct ordered signed primitive path is retained as one
    # branch, propagated by one ±Ei, and recoalesced at its exact endpoint.
    source_counts={(0,)*M:1}
    out=[]
    for n in range(K+1):
        relative_classes={relative(z) for z in source_counts}
        out.append(dict(n=n, full_cells=len(source_counts),
                        relative_classes=len(relative_classes),
                        path_mass=sum(source_counts.values()),
                        origin_mass=source_counts.get((0,)*M,0),
                        full_origin_lifts=sorted(x[0] for x in source_counts if len(set(x))==1)))
        if n==K: break
        nxt=defaultdict(int)
        for z,mass in source_counts.items():
            for i,sgn in E:
                nxt[z[:i]+(z[i]+sgn,)+z[i+1:]]+=mass
        source_counts=nxt
    return out

def prove_static_action_witness():
    # Quotient by diagonal is congruent under all spatial primitive translations
    # and axis permutations, but is NOT a full Cell identity quotient.
    D=(1,)*6
    z=(0,0,0,0,0,0)
    assert relative(z)==relative(D)
    for p in (z,D,(3,0,-2,5,1,4)):
        for i,sgn in E:
            t=p[:i]+(p[i]+sgn,)+p[i+1:]
            r=relative(p); u=r[:i]+(r[i]+sgn,)+r[i+1:]
            assert relative(t)==relative(u)
    assert len({relative(tuple(int(i==j) for i in range(6))) for j in range(6)})==6
    assert len({relative(tuple(int(i==j)*sgn for i in range(6))) for j in range(6) for sgn in(-1,1)})==12
    return True

def main():
    a=gap_spheres(12)
    d=actual_path_dp(12)
    assert prove_static_action_witness()
    for row in d:
        k=row['n']
        assert row['relative_classes']==supported_length_count(k,a),(row,a)
        assert row['path_mass']==12**k
        assert row['full_origin_lifts']==(list(range(-(k//6),k//6+1)) if k%2==0 else []) or k%2==1
        if k==0: assert row['relative_classes']==1
        print(f"k={k:2d} full={row['full_cells']:>8d} rel={row['relative_classes']:>8d} paths={row['path_mass']:>16d} r0_full_lifts={row['full_origin_lifts']}")
    print('relative spheres a6(0..12)=',a)
    for n,h in ((12,0),(12,1),(12,2),(12,3),(10,2)):
        Q=(12**h)*d[n-h]['relative_classes']
        print(f'Q_relative(n={n},h={h})={Q}')
    assert d[12]['full_cells']==227305
    assert d[10]['full_cells']==85305
    print('PREFIX268_FULL_BRC_DP_VS_INDEPENDENT_GAP_CERTIFICATE_PASS')

if __name__=='__main__': main()
