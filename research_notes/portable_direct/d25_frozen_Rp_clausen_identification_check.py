"""Author-side exact D24/LIFT R_p-to-Clausen crosscheck.

Source R_p: frozen 2026-08-27 reflected derivative-product return.
Source C_p: 2026-10-25 exact cutoff bridge.
No Source CLAIM, native Result, or independent Driver review.
"""
from math import comb, isqrt, factorial
from fractions import Fraction


def candidate_primes(limit):
    for p in range(7, limit):
        if p % 6 == 1 and all(p % d for d in range(2, isqrt(p)+1)):
            yield p


def source_R(p):
    # Parent C_r (called K_r in note) computed by Pochhammer products.
    m = (p-1)//6
    Cs = [0]*(m+1)
    numerator = 1
    prod5 = prod2 = 1
    for r in range(1, m+1):
        prod5 = prod5*(6*r-1) % p
        prod2 = prod2*(3*r-1) % p
        if r > 1:
            numerator = numerator*36*(r-1)**2 % p
        Cs[r] = numerator*pow(prod5*prod2 % p, -1, p) % p
    total = 0
    for i in range(1,m+1):
        B = comb(m,i)*comb(2*m,i)*pow(2,-i,p)%p
        inner = sum((6*(i-r)+1)*Cs[r] for r in range(1,i+1))%p
        total = (total+2*B*inner)%p
    return total,Cs


def cutoff_C(p):
    m=(p-1)//6
    B=e=1
    e0=e1=ans=0
    es=[0]*(m+1)
    for i in range(1,m+1):
        B=B*(m-i+1)*(2*m-i+1)*pow(2*i*i,-1,p)%p
        if i>1:
            e=e*36*(i-1)**2*pow((6*i-1)*(3*i-1),-1,p)%p
        es[i]=e
        e0=(e0+e)%p
        e1=(e1+i*e)%p
        ans=(ans+B*((6*i+1)*e0-6*e1))%p
    return ans*pow(5,-1,p)%p,es


def weighted_W(p):
    M=p**3
    term=W=1
    for k in range(p-1):
        term=term*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,M)%M
        W=(W+(6*(k+1)+1)*term)%M
    return W


def gh_residue(p):
    M=p**3
    b=g=h=1
    for k in range(p-1):
        b=b*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,M)%M
        g=(g+b)%M
        h=(h+(12*(k+1)+1)*b)%M
    return g,(g*h)%M


def exact_base_checks():
    for r in range(1,8):
        numerator=Fraction(2**(r-1)*factorial(r-1)**2,18)
        denom=Fraction(1,1)
        for j in range(r):
            denom*=Fraction(6*j+5,6)*Fraction(3*j+2,3)
        K=numerator/denom
        e=Fraction(1,1)
        for j in range(2,r+1):
            e*=Fraction(36*(j-1)**2,(6*j-1)*(3*j-1))
        assert 10*K==e,(r,K,e)


def main():
    exact_base_checks()
    n=target=split=w3=0
    samples=[]
    for p in candidate_primes(5000):
        R,K=source_R(p)
        C,es=cutoff_C(p)
        assert R==C,(p,R,C)
        assert all(10*K[i]%p==es[i] for i in range(1,(p-1)//6+1)),p
        g,gh=gh_residue(p)
        W=weighted_W(p)
        M=p**3
        assert (gh-W)%p**2==0,p
        assert ((gh-W)%M)//p**2==R,(p,gh,W,R)
        if p%24 in (13,19):
            assert g%p==0
            assert (gh-p)%p**2==0,p
            assert (W-p)%p**2==0,p
            delta=((gh-p)%M)//p**2
            wdigit=((W-p)%M)//p**2
            assert (delta-R)%p==wdigit,(p,delta,R,wdigit)
            target+=1
            w3+=(wdigit==0)
            if p in (13,19,37,43,61,67,109):
                samples.append((p,delta,R,C,wdigit))
        else:
            split+=1
        n+=1
    print("Exact rational 10K_r=e_r spot checks r=1..7: passed")
    print("All primes 7<=p<5000, p=1 mod6: tail+R*=C",n,"/",n)
    print("Inert target LIFT residual checks:",target,"/",target)
    print("Other 1 mod6 tail-only checks:",split,"/",split)
    print("FINITE observation W=p mod p^3:",w3,"/",target)
    print("Samples p,Delta,R,C,(W-p)/p^2:",samples)


if __name__=="__main__":
    main()
