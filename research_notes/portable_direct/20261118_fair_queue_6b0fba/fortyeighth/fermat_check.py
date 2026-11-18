"""Exact local checks for the shifted modular square test, using integer arithmetic."""
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod
import json


def prime(n):
    return n>1 and all(n%d for d in range(2,isqrt(n)+1))


def char(a,p):
    r=pow(a%p,(p-1)//2,p)
    return r if r<2 else -1


def truth(q,n):
    squares={i*i%q for i in range(q)}
    return [int((i*i-n)%q in squares) for i in range(q)]


def direct_counts(A, shifts):
    q=len(A);mask=sum(a<<i for i,a in enumerate(A));allbits=(1<<q)-1
    return [((mask & (((mask<<h)&allbits)|(mask>>(q-h))))).bit_count() for h in shifts]


def prime_formula(p,n,h):
    n%=p;h%=p
    if n==0:return p,None
    roots=[r for r in range(p) if r*r%p==n]
    if h==0:return (p+char(n,p))//2,None
    if (h*h-4*n)%p==0:
        value=p+2-char(-1,p)+2*char(2,p)
        assert value%4==0
        return value//4,None
    v=h*pow(2,-1,p)%p
    A=-2*(v*v+n);B=(v*v-n)**2
    trace=-sum(char(x*(x*x+A*x+B),p) for x in range(p))
    extra=sum(char(h*(h+2*r),p) for r in roots)
    value=p-3+2*len(roots)-trace+2*extra
    assert value%4==0 and trace**2<=4*p
    return value//4,trace


def valuation(a,p,k):
    j=0
    while j<k and a%p==0:
        j+=1;a//=p
    return j


def root_lifts(p,k,n):
    q=p
    roots=[r for r in range(p) if (r*r-n)%p==0]
    for _ in range(1,k):
        roots=[r+q*((n-r*r)//q*pow(2*r,-1,p)%p) for r in roots]
        q*=p
    return roots


def overlap_disk(p,k,r,s,h):
    eps,eta=char(2*r,p),char(2*s,p)
    d=r+h-s;l=valuation(d,p,k)
    restricted=lambda lo,hi: (p-1)//2*sum(p**(k-j-1) for j in range(lo,hi) if j%2==0)
    before=restricted(1,l) if eps==eta else 0
    if l==k:return before+1
    if l%2:return before
    u=d//(p**l)
    after=1+restricted(l+1,k)
    middle=p-2-eps*char(-u,p)-eta*char(u,p)-eps*eta
    assert middle%4==0
    return before+after*(int(char(u,p)==eta)+int(char(-u,p)==eps))+middle//4*p**(k-l-1)


def unit_count(p,k,n,h):
    q=p**k
    cp,_=prime_formula(p,n,h)
    if char(n,p)<0:return p**(k-1)*cp
    roots=root_lifts(p,k,n)
    local=1+(p-1)//2*sum(p**(k-j-1) for j in range(2,k,2))
    single=2*sum(char(h*(h+2*r),p)==1 for r in roots)
    pairs=[(r,s) for r in roots for s in roots if (r+h-s)%p==0]
    return ((cp-single-len(pairs))*p**(k-1)+single*local+
            sum(overlap_disk(p,k,r,s,h) for r,s in pairs))


def odd_count(p,k,n,h):
    q=p**k;v=valuation(n,p,k)
    if v==k:return q
    t=v//2
    if v%2:
        m=p**(t+1)
        return q-(2-int(h%m==0))*(q//m)
    if t==0:return unit_count(p,k,n,h)
    t0=p**t;k0=k-2*t;n0=n//(t0*t0);q0=p**k0
    size=unit_count(p,k0,n0,0)
    failures=t0*(q0-size)
    if h%t0:return q-2*failures
    return q-2*failures+t0*(q0-2*size+unit_count(p,k0,n0,h//t0))


def two_cylinders(k,n):
    # Each (r,j) represents x == r mod 2^j; disjoint square-valuation layers.
    def roots2(a,j):
        roots=[0];m=1
        for _ in range(j):
            roots=[x for r in roots for x in (r,r+m) if (x*x-a)%(2*m)==0]
            m*=2
        return roots
    out=[(r,k) for r in roots2(n,k)]
    for v in range(0,k,2):
        j=min(v+3,k)
        out.extend((r,j) for r in roots2(n+2**v,j))
    return out


def two_count(k,n,h):
    rows=two_cylinders(k,n)
    return sum(1<<(k-max(j,e)) for r,j in rows for s,e in rows if (r+h-s)%(1<<min(j,e))==0)


def active_conductors(A,p,k):
    # Phi_{p^j} divides the folded polynomial exactly when each set of p siblings has equal coefficients.
    active=[0] if sum(A) else []
    for j in range(1,k+1):
        m=p**j
        B=[sum(A[x::m]) for x in range(m)]
        if any(B[x]!=B[x%(m//p)] for x in range(m)):
            active.append(j)
    return active


def effective_odd_exponent(p,k,n):
    v=valuation(n,p,k)
    if v==k:return 0
    t=v//2
    if v%2:return t+1
    return k-t if char(n//p**(2*t),p)==1 else t+1


def binary_rank_and_size(n,k):
    if k==1:
        return 2,[0]
    if k==2:
        return 2,[0,1]
    h=n%8
    if h in (3,7):
        return 1<<(k-2),[0,1,2]
    if k==3:
        return 4,[0,1]
    if h==5:
        s=min(k,5)
        return 1<<(k-s+2),[0,1]+list(range(3,s))
    m=k-4
    r=1 if m==0 else ((1<<m)+8+2*(m%2))//6
    orders=[0,1,3]+([4] if k==7 or k>=9 else [])+list(range(5,k))
    return 4*r,orders


def fine_cyclotomic_test(p,k,n,A):
    q=p**k
    l=q//p
    roots=root_lifts(p,k,n)
    coeffs=A[:]
    for r in roots:
        coeffs[r]-=1
        if k%2:
            for u in {x*x%p for x in range(1,p)}:
                coeffs[(r+l*u*pow(2*r,-1,p))%q]-=1
    assert all(c==coeffs[j%l] for j,c in enumerate(coeffs))


def main():
    parts={};count=0;trac=0;powrows=0;ranks=0;energies=0;tworows=0;fine_checks=0
    for p in range(3,44,2):
        if not prime(p):continue
        for n in range(p):
            A=truth(p,n); ks=direct_counts(A,range(p))
            for h in range(p):
                val,tr=prime_formula(p,n,h)
                assert val==ks[h]
                count+=1;trac+=int(tr is not None)
    for p,maxk in [(3,5),(5,4),(7,3),(11,2)]:
        for k in range(1,maxk+1):
            q=p**k
            for n in sorted(set(range(min(20,q)))|{u%q for u in (15,21,35,45,63,77,105,9*11,125,189,225,375)}):
                A=truth(q,n)
                assert active_conductors(A,p,k)==list(range(effective_odd_exponent(p,k,n)+1))
                ranks+=1
                hs=list(range(q))
                counts=direct_counts(A,hs)
                assert all(odd_count(p,k,n,h)==v for h,v in zip(hs,counts))
                powrows+=len(hs)
                if k>=2 and n%p:
                    fine_cyclotomic_test(p,k,n,A);fine_checks+=1
                if k>=2 and char(n,p)==1:
                    roots=root_lifts(p,k,n);q0=q//p
                    fine=[p*v-sum(counts[h%q0::q0]) for h,v in enumerate(counts)]
                    exceptional={0,2*roots[0]%q0,-2*roots[0]%q0}
                    assert all(not v or h%q0 in exceptional for h,v in enumerate(fine))
                    factor=Fraction(6) if k%2==0 else Fraction(3,8)*((p+1)**2+2*p*(1+char(-1,p)))
                    assert Fraction(sum(v*v for v in fine),p*p)==Fraction(p-1,p)*factor
                    energies+=1
    for k in range(1,10):
        q=2**k
        for n in sorted({n%q for n in (1,3,5,7,9,11,13,15,17,33,73,105,9917459,9917461)}):
            A=truth(q,n);rows=two_cylinders(k,n)
            assert all(sum((x-r)%(1<<j)==0 for r,j in rows)==v for x,v in enumerate(A))
            good=direct_counts(A,range(q))
            assert all(two_count(k,n,h)==v for h,v in enumerate(good))
            tworows+=q
    binary=0
    for k in range(1,17):
        q=1<<k
        candidates=range(1,q,2) if k<=10 else (1,3,5,7)
        squares={i*i%q for i in range(q)}
        for n in candidates:
            A=[int((x*x-n)%q in squares) for x in range(q)]
            size,orders=binary_rank_and_size(n,k)
            assert sum(A)==size and active_conductors(A,2,k)==orders
            binary+=1
    sample=[]
    for n,p in product((9917459,9917461),(997,1009,4093)):
        A=truth(p,n);cs=direct_counts(A,range(p));M=sum(A)
        if n%p:
            shifted=[(v,h) for h,v in enumerate(cs) if 0<h<=p//2 and (h*h-4*n)%p]
            low=min(shifted)
            high_value=max(v for v,h in shifted)
            high=next(z for z in shifted if z[0]==high_value)
            cases=[]
            for val,h in (low,high):
                got,trace=prime_formula(p,n,h);assert got==val
                cases.append(dict(h=h,intersection=val,trace=trace))
        else:cases=[dict(h=1,intersection=p,trace=None)]
        sample.append(dict(N=n,p=p,single=M,independent_level=str(Fraction(M*M,p)),selected=cases))
    M=6720;CRT=[]
    for n in (15,105,9917459,9917461):
        A=truth(M,n)
        for h,expected in zip((0,1,2,7,48,63,240,3360),direct_counts(A,(0,1,2,7,48,63,240,3360))):
            got=two_count(6,n,h)*prod(odd_count(p,1,n,h) for p in (3,5,7))
            assert expected==got
            CRT.append([n,h,got])
    parts.update(prime_pairs=count,good_elliptic_trace_pairs=trac,odd_power_pairs=powrows,odd_rank_models=ranks,
                 exact_fine_energy_models=energies,cyclotomic_fine_spectrum_models=fine_checks,binary_rank_models=binary,two_power_pairs=tworows,arithmetic_examples=sample,
                 original_modulus_6720=CRT)
    print(json.dumps(parts,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
