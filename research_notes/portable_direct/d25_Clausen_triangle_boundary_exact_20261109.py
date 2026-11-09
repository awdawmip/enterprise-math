"""Author-side exact regression: original signed 216/2304 Clausen triangular boundary.
No external dependencies, floats, or native H0/B0 claim. 2026-11-09.
"""
from math import comb, factorial

def prime(p):
    return p > 1 and all(p % d for d in range(2, int(p**0.5) + 1))

def coeffs(p, tag):
    mod = p**3
    v = [1]
    for k in range(p-1):
        if tag == 'A':
            num, den = (6*k+1)*(3*k+1), 36*(k+1)**2
        else:
            num, den = (8*k+1)*(8*k+3), 576*(k+1)**2
        v.append(v[-1] * num * pow(den, -1, mod) % mod)
    return v

def poch(n,d,j,p):
    out = 1
    for i in range(j):
        out = out*(n+d*i)*pow(d,-1,p)%p
    return out

def reflected(j,p,tag):
    fact=pow(factorial(j-1),2,p)
    if tag=='A':
        denominator=18*poch(5,6,j,p)*poch(2,3,j,p)
        numerator=pow(2,j-1,p)*fact
    else:
        denominator=64*poch(7,8,j,p)*poch(5,8,j,p)
        numerator=3*pow(9,j-1,p)*fact
    return numerator*pow(denominator,-1,p)%p

def check(p,tag):
    mod=p**3
    f=coeffs(p,tag)
    weight,den = (6,216) if tag=='A' else (8,2304)
    S=sum(f)%mod
    D=sum(j*f[j] for j in range(p))%mod
    square=(S*S+2*weight*S*D)%mod
    cut=0
    for n in range(p):
        c=sum(f[j]*f[n-j] for j in range(n+1))%mod
        cut=(cut+(weight*n+1)*c)%mod
    original=0
    for n in range(p):
        c=(comb(2*n,n)**2*comb(3*n,n)) if tag=='A' else (comb(4*n,2*n)*comb(2*n,n)**2)
        original=(original+(weight*n+1)*c*pow(den,-n,mod))%mod
    assert cut==original,(p,tag,'Clausen')
    tail=(square-cut)%mod
    eligible=(tag=='A' and p%6==1) or (tag=='C' and p%8 in (1,3))
    if not eligible:
        return (p,tag,'other-class',tail)
    limit=(p-1)//6 if tag=='A' else (p-1)//8
    assert tail%p**2==0,(p,tag,'valuation')
    val=0
    for j in range(1,limit+1):
        r=reflected(j,p,tag)
        assert f[p-j]%p**2==0
        assert f[p-j]//p**2%p==r,(p,tag,j,'reflection')
        for k in range(j,limit+1):
            val+=2*(weight*(k-j)+1)*f[k]*r
    assert tail//p**2%p==val%p,(p,tag,'triangular residue')
    return (p,tag,'PASS',val%p)

if __name__=='__main__':
    counts={'clausen':0,'boundary':0}
    for p in range(5,374):
        if not prime(p):
            continue
        for tag in ('A','C'):
            out=check(p,tag)
            counts['clausen']+=1
            if out[2]=='PASS':
                counts['boundary']+=1
            if p in (13,19,37,43,73,373):
                print(out)
    assert counts=={'clausen':144,'boundary':68},counts
    print('PASS',counts)
