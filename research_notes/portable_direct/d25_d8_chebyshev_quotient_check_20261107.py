"""Exact D8-Chebyshev quotient check; standalone, stdlib only.
Native p=373 divided-power/Frobenius benchmark is NOT executed.
"""
from math import isqrt

def primes(n):
    a=bytearray(b'\1')*(n+1); a[:2]=b'\0\0'
    for i in range(2,isqrt(n)+1):
        if a[i]:
            a[i*i::i]=b'\0'*((n-i*i)//i+1)
    return [i for i in range(n+1) if a[i]]

def check(p):
    assert p%24 in (13,19)
    assert pow(2,(p-1)//2,p)==p-1
    m=(p-1)//6
    X=set(range(2,p-1))
    inv2=pow(2,-1,p)
    def T(y): return (y-1)*pow(y+1,-1,p)%p
    def R(y): return 2*y*pow(1-y*y,-1,p)%p
    def J(y):
        d=(y*y+1)%p
        return None if d==0 else 4*y*y*(y*y-1)**2*pow(d,-4,p)%p
    def P(j): return None if j is None else 4*j*(1-4*j)%p
    def v(y):
        x=(y-1)*inv2%p
        return pow(x**5*(x+1)**2*y,m,p)
    def chi(z):
        a=pow(z%p,(p-1)//2,p)
        assert a in (0,1,p-1)
        return 0 if a==0 else (1 if a==1 else -1)
    seen=set()
    orbits={}
    for first in sorted(X):
        if first in seen: continue
        O={first}; todo=[first]
        while todo:
            y=todo.pop()
            for z in (-y%p,T(y)):
                assert z in X
                if z not in O: O.add(z); todo.append(z)
        assert not O&seen
        seen|=O
        jset={J(y) for y in O}
        assert len(jset)==1
        j=jset.pop()
        assert j not in orbits
        assert (j is None and p%24==13 and len(O)==2) or (j is not None and len(O)==8)
        orbits[j]=O
    assert seen==X
    sums={j:sum(v(y) for y in O)%p for j,O in orbits.items()}
    # Fresh O(m) modular exact binomial sum, independent of old D8 checker.
    c1=c2=1
    S=0
    for k in range(m+1):
        S=(S+c1*c2)%p
        if k<m:
            ik=pow(k+1,-1,p)
            c1=c1*(m-k)*ik%p
            c2=c2*(2*m+k+1)*ik%p
    assert S==(-sum(sums.values()))%p
    samples=X if p in (19,43,61,373) else {min(O) for O in orbits.values()}
    for y in samples:
        j=J(y)
        assert R(y) in X and J(R(y))==P(j)
        if j is not None:
            r=(y*y-1)*pow(y*y+1,-1,p)%p
            w=2*y*pow(y*y+1,-1,p)%p
            assert (r*r+w*w)%p==1
            assert j==r*r*w*w%p
            assert J(T(y))==j
    assert {P(j) for j in orbits}==set(orbits)
    if p%24==13:
        for j, val in sums.items():
            if val:
                assert sums[P(j)]==0
                assert all(chi(y)==chi(y*y-1)==1 for y in orbits[j])
                assert all(chi(R(y))==-1 for y in orbits[j])
    visited=set(); cycles=[]
    for j in orbits:
        if j in visited: continue
        cycle=[]; z=j
        while z not in visited:
            visited.add(z); cycle.append(z); z=P(z)
        assert z==j
        cycles.append(cycle)
    assert len(visited)==len(orbits)
    return cycles,sums

if __name__=="__main__":
    ps=[p for p in primes(1999) if p%24 in (13,19)]
    assert len(ps)==77
    results={p:check(p) for p in ps}
    for p in (19,43,61,373):
        cycles,sums=results[p]
        print("p",p,"cycles",[(c,[sums[j] for j in c]) for c in cycles if any(sums[j] for j in c)])
    print("verified",len(ps),"primes; 13-branch",sum(p%24==13 for p in ps),
          "19-branch",sum(p%24==19 for p in ps),"failures=0")
