"""Exact finite certificates for the odd cyclotomic part of a fixed 2-Kummer tower."""
from collections import Counter
from itertools import product
from math import gcd,isqrt,prod
import json

A,B=233**2,119**2
H=(194089,69872040)
BAD=(3,7,11,17,19,233)
BASES=(2,3,2,3,2,3)
D=(2,2,2,16,2,8)
WITNESSES=[
    (4001,(420,2673),(3337,2698),(3310,1030)),
    (321553,(28827,10604),(180494,162797),(249914,249288)),
]


def add(P,Q,p):
    if P is None:return Q
    if Q is None:return P
    x,y=P; u,v=Q
    if x==u:
        if (y+v)%p==0:return None
        slope=(3*x*x-2*(A+B)*x+A*B)*pow(2*y,-1,p)%p
    else:
        slope=(v-y)*pow(u-x,-1,p)%p
    z=(slope*slope+A+B-x-u)%p
    return z,(slope*(x-z)-y)%p


def doubled(P,i,p):
    for _ in range(i):P=add(P,P,p)
    return P


def span(gens):
    H={tuple(0 for _ in D)}
    step=lambda v,w:tuple((a+b)%d for a,b,d in zip(v,w,D))
    for w in gens:
        g=w
        base=set(H)
        while g not in base:
            H.update(step(v,g) for v in base)
            g=step(g,w)
    return H


def log_tables():
    tables=[]
    for p,base,order in zip(BAD,BASES,D):
        table={pow(base,j,p):j%order for j in range(p-1)}
        assert len(table)==p-1
        tables.append(table)
    return tables


def period_polynomial(logs):
    m=17*233
    def orbit(x):
        x%=m
        if x==0:return 6
        if x%17==0:return 4
        if x%233==0:return 5
        return (logs[3][x%17]+logs[5][x%233])%4
    orbits=[[] for _ in range(7)]
    for x in range(m):orbits[orbit(x)].append(x)
    kernel=orbits[0]
    assert len(kernel)==928
    # The multiplier kernel projects surjectively to each prime, so all seven sets are its orbits.
    for group in orbits:
        assert {group[0]*u%m for u in kernel}==set(group)
    T=[Counter(orbit(group[0]-u) for u in kernel) for group in orbits]
    coeff=[0]*6+[1]
    traces=[]; polynomial=[1]
    for n in range(1,7):
        coeff=[sum(mult*coeff[j] for j,mult in row.items()) for row in T]
        rt=sum(len(g)*value*(16 if g[0]%17==0 else -1)*(232 if g[0]%233==0 else -1)
               for g,value in zip(orbits,coeff))
        trace,rem=divmod(rt,len(kernel))
        assert not rem
        traces.append(trace)
        if n<=4:
            c,rem=divmod(-sum(polynomial[n-j]*traces[j-1] for j in range(1,n+1)),n)
            assert not rem
            polynomial.append(c)
    # An irreducible reduction is a second certificate of a primitive element.
    f=[c%7 for c in reversed(polynomial)]
    for degree in (1,2):
        for lo in product(range(7),repeat=degree):
            divisor=list(lo)+[1]
            a=f.copy()
            for i in range(4,degree-1,-1):
                lead=a[i]
                for j,v in enumerate(divisor):
                    a[i-degree+j]=(a[i-degree+j]-lead*v)%7
            assert any(a[:degree])
    from itertools import permutations
    powers=[4]+traces
    disc=0
    for pi in permutations(range(4)):
        parity=sum(pi[i]>pi[j] for i in range(4) for j in range(i+1,4))
        disc+=(-1)**parity*prod(powers[i+pi[i]] for i in range(4))
    # Each of chi, chi^2, chi^3 is nontrivial at each of the two prime factors.
    assert all(any((j*power)%4 for j in table.values()) for table in (logs[3],logs[5]) for power in (1,2,3))
    assert disc==m**3*(2*11**3)**2
    return dict(traces=traces[:4],monic_descending=polynomial,order=len(kernel),
                irreducible_mod=7,field_discriminant=m**3,power_order_discriminant=disc,
                power_order_index=2*11**3)


def finite_two_adic_check():
    # Compose linear matrices modulo 8, translations modulo 4.
    identity=(1,0,0,1,0,0)
    def multiply(P,Q):
        a,b,c,d,x,y=P
        e,f,g,h,s,t=Q
        return ((a*e+b*g)%8,(a*f+b*h)%8,(c*e+d*g)%8,(c*f+d*h)%8,
                (a*s+b*t+x)%4,(c*s+d*t+y)%4)
    def inverse(P):
        a,b,c,d,x,y=P
        inv=pow(a*d-b*c,-1,8)
        e,f,g,h=(v*inv%8 for v in (d,-b,-c,a))
        return e,f,g,h,(-e*x-f*y)%4,(-g*x-h*y)%4
    def generate(gens):
        reached={identity}
        stack=[identity]
        while stack:
            z=stack.pop()
            for g in gens:
                m=multiply(z,g)
                if m not in reached:
                    reached.add(m)
                    stack.append(m)
        return reached
    gens=[
        (1,2,0,1,0,0),(1,0,4,1,0,0),(7,0,0,1,0,0),(5,0,0,1,0,0),
        (1,0,0,5,0,0),(1,0,0,1,1,0),(1,0,0,1,0,1),
    ]
    group=generate(gens)
    assert len(group)==1024
    def comm(z,w):
        return multiply(multiply(z,w),inverse(multiply(w,z)))
    comms={comm(g,h) for g in gens for h in gens}
    normal={multiply(multiply(v,c),inverse(v)) for v in group for c in comms}
    derived=generate(normal)
    def read(P):
        a,b,c,d,x,y=P
        return ((a*d-b*c)%8,(b//2)%2,(c//4)%2,((d-1)//4)%2,x%2,y%4)
    image=set(map(read,group))
    assert len(image)==256
    assert derived=={v for v in group if read(v)==read(identity)}
    # Squares of the subgroup of odd 2-adic units congruent to 1 mod 4 start at 1 mod 8.
    # Fourth powers start at 1 mod 16, including every such unit at each finite level.
    for modulus in (16,32,64,128,256,512):
        fourth_powers={pow(x,4,modulus) for x in range(1,modulus,2)}
        assert fourth_powers==set(range(1,modulus,16))
    return dict(raw_group=len(group),derived=len(derived),abelian_quotient=len(image),
                determinant_units=4,finite_part=64)


def main():
    logs=log_tables()
    rows=[]
    gens=[]
    for p,U,V,W in WITNESSES:
        assert p%16==1 and all(p%d for d in range(2,isqrt(p)+1))
        for x,y in (U,V,W):assert (y*y-x*(x-A)*(x-B))%p==0
        assert doubled(U,2,p)==(0,0)
        assert doubled(V,2,p)==(A%p,0)
        assert doubled(W,3,p)==(H[0]%p,H[1]%p)
        w=tuple(t[p%q] for t,q in zip(logs,BAD))
        gens.append(w)
        rows.append(dict(p=p,U=U,V=V,W=W,frobenius=w,generated=len(span(gens))))
    subgroup=span(gens)
    def image(x):
        a,b,c,d,e,f=x
        # -7, -19, 33, -51 and the quartic character.
        return b,e,(a+c)%2,(a+d)%2,(d+f)%4
    G=list(product(*(range(m) for m in D)))
    assert len(subgroup)==32 and set(v for v in G if not any(image(v)))==subgroup
    assert len(set(map(image,G)))==64
    both_plus=[(v[3]+v[5])%4 for v in gens]
    conjugate_at_one_prime=[(v[3]-v[5])%4 for v in gens]
    assert both_plus==[0,0] and conjugate_at_one_prime==[2,0]
    singles=[D[i]//len({v[i] for v in subgroup}) for i in range(len(D))]
    assert singles==[1,2,1,1,2,1]
    return dict(two_adic_audit=finite_two_adic_check(),single_prime_intersections=singles,
                quartic_exponents_at_witnesses=dict(plus=both_plus,single_factor_reversed=conjugate_at_one_prime),
                witnesses=rows,odd_primes=BAD,primitive_roots=BASES,
                cyclic_factors=D,odd_ground_size=prod(D),intersection_degree=64,
                period=period_polynomial(logs))


if __name__=='__main__':print(json.dumps(main(),sort_keys=True,indent=2))
