from fractions import Fraction
from math import factorial, comb, isqrt

def modq(x,p,k=2):
    q=p**k
    assert x.denominator % p, (x,p)
    return (x.numerator % q)*pow(x.denominator,-1,q)%q

def r_ratio(m,n):
    return Fraction((4*m+1+2*n)*(3*n+1)*(3*n+2),36*(n+1)*(2*m+n+1)*(4*m+n+1))

def R(m,n):
    r=Fraction(1)
    for j in range(n):
        r*=r_ratio(m,j)
    return r

def derived(p,T2,T4, exact_ratio=False):
    m=(p-1)//6
    q=(pow(6,p-1,p*p)-1)//p
    H=sum((Fraction(1,j) for j in range(1,2*m+1)),Fraction(0))
    C=Fraction(factorial(2*m-1)*factorial(2*m),factorial(4*m))
    alpha=Fraction((p+2)*(4*p+1),3*(2*p+1))
    beta=Fraction(-8*p*p+14*p-3,4*p-1)
    seam=alpha*T2+beta*T4
    r=T4/T2
    if exact_ratio:
        assert r==Fraction(comb(12*m,4*m)**2,216**(2*m)*comb(6*m,2*m)**2)
    r_pred=Fraction(1,9)*(1-p*(2*H+4+q))
    t2_pred=C*(1-p*(Fraction(1,2*m)+q))
    seam_pred=C*(1+Fraction(p,9)*(28-6*H-12*q))
    sigma_pred=1+Fraction(p,9)*(1-6*H-3*q)
    return dict(p=p, ratio=modq(r,p), ratio_pred=modq(r_pred,p),
                t2=modq(T2,p),t2_pred=modq(t2_pred,p),
                seam=modq(seam,p),seam_pred=modq(seam_pred,p),
                seam_mult=modq(seam/T2,p), seam_mult_pred=modq(sigma_pred,p),
                h=modq(H,p,1),q=q)

# independent exact rational path
for m in range(1,11):
    p=6*m+1
    R2=R(m,2*m)
    R4=R(m,4*m)
    assert R2==Fraction(comb(8*m,4*m),216**(2*m))
    assert R4/R2 == Fraction(comb(12*m,4*m)**2,216**(2*m)*comb(6*m,2*m)**2)
    if all(p%d for d in range(2,isqrt(p)+1)):
        row=derived(p,R2/p,R4/p,exact_ratio=True)
        assert row['ratio']==row['ratio_pred'],row
        assert row['t2']==row['t2_pred'],row
        assert row['seam']==row['seam_pred'],row
        assert row['seam_mult']==row['seam_mult_pred'],row
        print('exact',row)

# independent p-adic valuation-unit recurrence, no Fraction products
primes=[]
for p in range(7,1001,6):
    if any(p%d==0 for d in range(2,isqrt(p)+1)):
        continue
    m=(p-1)//6
    M=p**3
    v=0;u=1; T2=T4=None; regular=0;low=0;high=0
    for n in range(4*m+1):
        if n==2*m:
            assert v==1
            T2=u%(p*p)
        if n==4*m:
            assert v==1
            T4=u%(p*p)
        if n!=2*m and n<4*m:
            den=(3*n+p+2)*(3*n+2*p+1)
            assert den%p
            num_k=(2*p+1-3*n)*(6*n+2*p+3)
            kr=(num_k*pow(den,-1,p*p)*u*pow(p,v,p*p))%(p*p)
            regular=(regular+kr)%(p*p)
            if n<=m: low=(low+kr)%(p*p)
            else: high=(high+kr)%(p*p)
        if n==4*m: break
        num=(4*m+1+2*n)*(3*n+1)*(3*n+2)
        den=36*(n+1)*(2*m+n+1)*(4*m+n+1)
        while num%p==0: num//=p;v+=1
        while den%p==0: den//=p;v-=1
        u=(u*num*pow(den,-1,M))%M
    assert T2 is not None and T4 is not None
    row=derived(p,Fraction(T2),Fraction(T4))
    G=(-1)**m*factorial(2*m)**3*pow(factorial(3*m)**2,-1,p*p)%(p*p)
    C=Fraction(factorial(2*m-1)*factorial(2*m),factorial(4*m))
    assert (regular+row['seam'])%(p*p)==G
    assert (regular+row['seam_pred'])%(p*p)==G
    assert high%p==0
    row['regular']=regular;row['low']=low;row['high']=high;row['G']=G

    # Here T4/T2 is only known modulo p^2, not exact Q; remove exact-ratio assertion above for modular surrogate
    assert all(row[a]==row[b] for a,b in [('ratio','ratio_pred'),('t2','t2_pred'),('seam','seam_pred'),('seam_mult','seam_mult_pred')]),row
    primes.append(row)
print('checked',len(primes),'primes p<=1000 p=1 mod6 (including both target classes)')
for r in primes:
    if r['p'] in (13,19,31,37,61): print('combined', {k:r[k] for k in ('p','regular','low','high','seam','seam_pred','G')})
