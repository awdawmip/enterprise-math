#!/usr/bin/env python3
"""Exact author checks for Galois descent of two-cycle full-gauge classes.

The universal descent argument is mathematical (connected stabilizers + Lang).
This standard-library script checks finite examples, including exhaustive GL2
similarity in the invertible-X two-cycle sector, plus integer orbit arithmetic.
It does not simulate the original H0/B0 divided-power CM experiment.
"""
from collections import Counter, deque
from itertools import product
import json


class FiniteField:
    def __init__(self, p, poly):
        self.p = p
        self.poly = tuple(poly)   # monic irreducible polynomial low->high
        self.e = len(poly) - 1
        self.q = p ** self.e
        self.powers = tuple(p ** i for i in range(self.e))
        assert poly[-1] == 1

    def digits(self, a):
        return [(a // x) % self.p for x in self.powers]

    def pack(self, c):
        return sum((v % self.p) * self.powers[i] for i, v in enumerate(c[:self.e]))

    def add(self, a, b):
        x, y = self.digits(a), self.digits(b)
        return self.pack([(u + v) % self.p for u, v in zip(x, y)])

    def neg(self, a):
        return self.pack([(-v) % self.p for v in self.digits(a)])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        x, y = self.digits(a), self.digits(b)
        z = [0] * (2 * self.e - 1)
        for i, u in enumerate(x):
            for j, v in enumerate(y):
                z[i+j] = (z[i+j] + u * v) % self.p
        for j in range(len(z)-1, self.e-1, -1):
            u = z[j]
            if u:
                for i in range(self.e):
                    z[j-self.e+i] = (z[j-self.e+i]-u*self.poly[i]) % self.p
        return self.pack(z)

    def pow(self, a, n):
        v = 1
        while n:
            if n & 1:
                v = self.mul(v, a)
            a = self.mul(a, a)
            n >>= 1
        return v

    def inv(self, a):
        if a == 0:
            raise ZeroDivisionError
        return self.pow(a, self.q - 2)

    def frob(self, a):
        return self.pow(a, self.p)


def matmul(F, A, B):
    a, b, c, d = A
    e, f, g, h = B
    return (F.add(F.mul(a,e),F.mul(b,g)),
            F.add(F.mul(a,f),F.mul(b,h)),
            F.add(F.mul(c,e),F.mul(d,g)),
            F.add(F.mul(c,f),F.mul(d,h)))


def det(F, A):
    return F.sub(F.mul(A[0],A[3]),F.mul(A[1],A[2]))


def invmat(F, A):
    z = F.inv(det(F,A))
    return tuple(F.mul(z,x) for x in (A[3],F.neg(A[1]),F.neg(A[2]),A[0]))


def generators(F):
    # Elementary shears from the additive F_p basis, the exchange matrix,
    # and every diagonal unit. These generate GL2(F_q).
    gs = []
    for b in F.powers:
        gs.append((1,b,0,1))
    gs.append((0,1,1,0))
    gs.extend((u,0,0,1) for u in range(1,F.q))
    return tuple(gs)


def gl2_size_check(F, gens):
    eye=(1,0,0,1)
    seen={eye}
    queue=deque([eye])
    while queue:
        a=queue.popleft()
        for g in gens:
            b=matmul(F,a,g)
            if b not in seen:
                seen.add(b)
                queue.append(b)
    target=(F.q**2-1)*(F.q**2-F.q)
    assert len(seen)==target,(F.q,len(seen),target)
    return len(seen)


def similarity_certificate(F):
    assert all(F.mul(a,F.inv(a))==1 for a in range(1,F.q))
    assert all(F.frob(F.mul(a,b))==F.mul(F.frob(a),F.frob(b))
               for a in range(F.q) for b in range(F.q))
    gen=generators(F)
    group=gl2_size_check(F,gen)
    transforms=[(g,invmat(F,g)) for g in gen]
    mats=set(product(range(F.q), repeat=4))
    orbit_id={}
    orbit_sizes=[]
    reprs=[]
    generator_edges=0
    for a in sorted(mats):
        if a in orbit_id:
            continue
        cid=len(reprs)
        reprs.append(a)
        queue=deque([a])
        orbit_id[a]=cid
        size=0
        while queue:
            x=queue.popleft()
            size+=1
            for g,gi in transforms:
                y=matmul(F,matmul(F,g,x),gi)
                generator_edges+=1
                if y not in orbit_id:
                    orbit_id[y]=cid
                    queue.append(y)
                else:
                    assert orbit_id[y]==cid
        orbit_sizes.append(size)
    assert len(orbit_id)==F.q**4
    assert len(reprs)==F.q*F.q+F.q
    mapping=[orbit_id[tuple(map(F.frob,a))] for a in reprs]
    cur=list(range(len(reprs)))
    for i in range(F.e):
        assert all(cur[j]==j for j in range(len(cur))) if i==0 else True
        cur=[mapping[j] for j in cur]
    assert cur==list(range(len(reprs)))
    visited=set()
    period_counts=Counter()
    for i in range(len(reprs)):
        if i in visited:
            continue
        cyc=[]
        j=i
        while j not in visited:
            visited.add(j)
            cyc.append(j)
            j=mapping[j]
        assert j==i
        period_counts[len(cyc)]+=1
    fixed=sum(i==j for i,j in enumerate(mapping))
    assert fixed==F.p**2+F.p
    semilinear=sum(period_counts.values())
    predicted=(sum(F.p**(2*__import__('math').gcd(F.e,j))+
                   F.p**__import__('math').gcd(F.e,j) for j in range(F.e))//F.e)
    assert semilinear==predicted
    return {
        "field":f"F_{F.q}/F_{F.p}",
        "irreducible_polynomial_low_high":list(F.poly),
        "GL2_order":group,
        "matrix_states":len(mats),
        "generated_conjugacy_edges":generator_edges,
        "linear_similarity_orbits":len(reprs),
        "Frobenius_fixed_similarity_orbits":fixed,
        "Galois_similarity_orbits":semilinear,
        "Galois_cycles_by_length":dict(sorted(period_counts.items())),
        "expected_semilinear_similarity_orbits":predicted,
    }


def mobius(n):
    primes=[]
    t=n
    d=2
    while d*d<=t:
        if t%d==0:
            t//=d
            if t%d==0:return 0
            primes.append(d)
        d+=1
    if t>1:primes.append(t)
    return (-1)**len(primes)


def divs(n):
    return [d for d in range(1,n+1) if n%d==0]


def linear_n2(q,m):
    if m==0:return 1
    if m==1:return q+3
    if m==2:return q*q+3*q+6
    if m==3:return q*q+4*q+8
    return q*q+4*q+9


def semilinear_n2(p,e,m):
    g=__import__('math').gcd
    b=sum(linear_n2(p**g(e,j),m) for j in range(e))
    assert b%e==0
    return b//e


def period_certificate(p,e,m):
    exact={}
    for d in divs(e):
        exact[d]=sum(mobius(d//a)*linear_n2(p**a,m) for a in divs(d))
        assert exact[d]>=0 and exact[d]%d==0
    count=sum(v//d for d,v in exact.items())
    assert count==semilinear_n2(p,e,m)
    return {"p":p,"e":e,"m":m,"n":2,"linear_classes":linear_n2(p**e,m),
            "semilinear_classes":count,"classes_of_exact_period":exact,
            "semilinear_orbits_by_period":{d:v//d for d,v in exact.items()}}


def main():
    exact=[similarity_certificate(FiniteField(2,[1,1,1])),
           similarity_certificate(FiniteField(2,[1,1,0,1])),
           similarity_certificate(FiniteField(3,[1,0,1]))]
    examples=[period_certificate(p,e,m) for p,e in ((2,2),(2,3),(2,4),(3,2),(5,2),(373,2))
              for m in range(5)]
    assert semilinear_n2(2,2,4)==31
    assert semilinear_n2(2,3,4)==49
    assert semilinear_n2(2,4,4)==103
    assert semilinear_n2(3,2,4)==78
    # Check the known exact F4 triple-core count distribution without rerunning it.
    assert [semilinear_n2(2,2,m) for m in range(5)]==[1,6,25,30,31]
    q=373**2
    assert examples[-1]["linear_classes"]==q*q+4*q+9
    out={"schema":"EM_AUTHOR_TWO_CYCLE_GALOIS_DESCENT_CHECK_V1",
         "proof_method":"connected representation automorphism groups plus Lang descent; computation is finite sanity check",
         "finite_similarity_full_enumeration":exact,
         "closed_n2_examples":examples,
         "f4_full_triple_prior_checksum":"previous author-side exhaustive 529-triple case: 41 linear, 21 fixed, 31 semilinear; not rerun",
         "scope":"AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE",
         "status":"PASS"}
    return out


if __name__=="__main__":
    print(json.dumps(main(),ensure_ascii=False,indent=2,sort_keys=True))
