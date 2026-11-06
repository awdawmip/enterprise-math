"""Exact D25 coefficient-by-coefficient fourth-jet and reflection checks.
Portable author-side experiment; not a native CM experiment.
"""
from math import isqrt
N=4
def primes_through(x):
    isprime=[True]*(x+1)
    isprime[0:2]=[False,False]
    for d in range(2,isqrt(x)+1):
        if isprime[d]:
            for k in range(d*d,x+1,d): isprime[k]=False
    return [p for p in range(5,x+1) if isprime[p]]
def mul(x,y,p):
    z=[0]*(N+1)
    for i,a in enumerate(x):
        if a:
            for j,b in enumerate(y[:N+1-i]): z[i+j]=(z[i+j]+a*b)%p
    return z
def reciprocal_linear(denom,slope,p):
    inv=pow(denom%p,-1,p);x=[0]*(N+1);v=inv
    for i in range(N+1):
        x[i]=v
        v=-v*slope*inv%p
    return x
def run_prime(p):
    eps=1 if p%6==1 else -1
    m=(p-eps)//6;delta=(1-eps)//2
    a,b,c=2*m-delta,3*m-delta,4*m-delta
    assert 0<=a<b<c<p
    inv2=pow(2,-1,p)
    C=[1,0,0,0,0];M=[1,0,0,0,0]
    H2=H3=H4=0;samples={};Rcoeff=[]
    for j in range(p):
        Rcoeff.append([1,0,(2*H2)%p,(6*H3)%p,(16*H4+2*H2*H2)%p])
        ell=sum(j>s for s in (a,b,c))
        assert all(M[k]==C[k]==0 for k in range(ell))
        assert M[ell]==C[ell] and M[ell]!=0
        defect=[(M[k]-C[k])%p for k in range(N+1)]
        rhs2=2*H2*C[0]%p
        rhs3=(2*H2*C[1]+6*H3*C[0])%p
        rhs4=(2*H2*C[2]+6*H3*C[1]+(16*H4+2*H2*H2)*C[0])%p
        assert defect[0]==defect[1]==0
        assert (defect[2],defect[3],defect[4])==(rhs2,rhs3,rhs4),(p,j,defect,(rhs2,rhs3,rhs4))
        assert all(defect[k]==0 for k in range(min(N+1,ell+2)))
        if j==(p-1)//6 and p%6==1: samples['exceptional']=(j,M[0],H2,defect[2],defect[4])
        if j in (a,b,c,p-1): samples[f'j{j}']=(ell,defect[2],defect[3],defect[4])
        if j==p-1: break
        num=[1,0,0,0,0]
        for s in (a,b,c):num=mul(num,[(s-j)%p,1,0,0,0],p)
        fac=(-inv2)%p; num=[z*fac%p for z in num]
        h=j+1;invh=pow(h,-1,p)
        cfac=mul(reciprocal_linear(h,-1,p),reciprocal_linear(h,-2,p),p)
        cfac=[z*invh%p for z in cfac]
        mfac=[z*invh*invh%p for z in reciprocal_linear(h,-3,p)]
        C=mul(C,mul(num,cfac,p),p)
        M=mul(M,mul(num,mfac,p),p)
        H2=(H2+invh**2)%p;H3=(H3+invh**3)%p;H4=(H4+invh**4)%p
    for j in range(p):
        neg=[x*((-1)**i)%p for i,x in enumerate(Rcoeff[p-1-j])]
        got=mul(Rcoeff[j],neg,p)
        expected=[1,0,0,0,0]
        if p==5:expected[4]=p-1
        assert got==expected,(p,j,got,expected)
    return samples
if __name__=='__main__':
    pp=sorted(set(primes_through(421)+[1009]))
    for p in pp:run_prime(p)
    print(f'PASS {len(pp)} primes: all j<p through fourth jet and complementary reflection.')
    for p in [5,7,13,19,373,1009]:
        s=run_prime(p)
        print(p,s.get('exceptional'),s[f'j{p-1}'])
