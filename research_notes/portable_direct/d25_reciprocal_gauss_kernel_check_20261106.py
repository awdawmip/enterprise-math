"""Verify finite reciprocal Gauss kernel for the D25 signed triangular boundary.
All arithmetic is exact in F_p, no native H0/B0 computation or admission.
"""
from math import comb


def inv(a,p):
    return pow(a%p,-1,p)

def verify(p):
    m=(p-1)//6
    assert p==6*m+1 and m>=1
    # Base finite Gauss solution and its reciprocal tail, in the field F_p.
    d=[comb(m,i)*comb(2*m,i)*inv(pow(2,i,p),p)%p for i in range(m+1)]
    e=[0]*(m+1)
    e[1]=inv(10,p)
    for r in range(1,m):
        e[r+1]=e[r]*36*r*r*inv((6*r+5)*(3*r+2),p)%p
    # New exact binomial reciprocity formula (for every 1<=r<=m)
    for r in range(1,m+1):
        br=pow(2,r,p)*inv(36*r*r*comb(m+r,r)*comb(2*m+r,r),p)%p
        assert e[r]==br,(p,r,e[r],br)
    # Complementary PF inhomogeneous operator: all coefficients 0..m+1.
    for r in range(0,m+2):
        coeff=(6*r-1)*(3*r-1)*(e[r] if r<=m else 0)-36*(r-1)**2*(e[r-1] if 1<=r<=m+1 else 0)
        expect= (1 if r==1 else -36*m*m*e[m] if r==m+1 else 0)
        assert (coeff-expect)%p==0,(p,r,coeff,expect)
    # Original finite Gauss ODE: homogeneous over F_p because 6m+1=p.
    for r in range(0,m+2):
        coeff=36*r*r*(d[r] if r<=m else 0)-(6*r-5)*(3*r-2)*(d[r-1] if 1<=r<=m+1 else 0)
        assert coeff%p==0,(p,r,coeff)
    # Original signed triangular boundary, two independent formulations.
    j_pair=sum((1+6*(i-r))*d[i]*e[r] for i in range(1,m+1) for r in range(1,i+1))%p
    j_prefix=0; er=0; rer=0
    for i in range(1,m+1):
        er=(er+e[i])%p;rer=(rer+i*e[i])%p
        j_prefix+=d[i]*((1+6*i)*er-6*rer)
    j_prefix%=p
    assert j_pair==j_prefix
    # Coefficient-extraction presentation, independent convolution.
    drev=[0]*m
    for r in range(1,m+1): drev[m-r]=e[r]
    c=[0]*(2*m)
    for i,di in enumerate(d):
        for j,ej in enumerate(drev):c[i+j]=(c[i+j]+di*ej)%p
    j_coeff=sum((1+6*n)*c[m+n] for n in range(m))%p
    assert j_pair==j_coeff,(p,j_pair,j_coeff)
    # Signed complement under CM vanishing, only when F_m(1/2)=0.
    D=sum(d)%p;T=sum(i*d[i] for i in range(m+1))%p
    if D==0:
        Jdual=(6*T*sum(e) - sum((1+6*(i-r))*d[i]*e[r]
                 for r in range(1,m+1) for i in range(r)))%p
        assert Jdual==j_pair,(p,j_pair,Jdual)
    return {'p':p,'m':m,'D_mod_p':D,'T_mod_p':T,'E_sum_mod_p':sum(e)%p,
            'J_mod_p':j_pair,'endpoint_mod_p':(-36*m*m*e[m])%p}


def primes(n):
    sieve=bytearray(b'\x01')*(n+1);sieve[0:2]=b'\x00\x00'
    for a in range(2,int(n**.5)+1):
        if sieve[a]:sieve[a*a::a]=b'\x00'*((n-a*a)//a+1)
    return [p for p in range(7,n+1) if sieve[p] and p%6==1]

if __name__=='__main__':
    vals=[verify(p) for p in primes(997)]
    print('ALL_CHECKS_PASS',len(vals),'primes p=1 mod6, p<=997')
    for v in vals:
        if v['p'] in (7,13,19,67,373):print(v)
