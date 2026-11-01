#!/usr/bin/env python3
"""D25: independently check the Legendre-neighbor Frobenius first-digit law.
All arithmetic is exact modular integer arithmetic; no native H0/B0 experiment.
"""
def primes(n):
    sv=[True]*(n+1); sv[:2]=[False,False]
    for k in range(2,int(n**.5)+1):
        if sv[k]:
            for j in range(k*k,n+1,k):sv[j]=False
    return [p for p in range(5,n+1) if sv[p]]
def poly_eval(coeff,z,mod):
    v=0
    for c in reversed(coeff):v=(v*z+c)%mod
    return v
def original_coeffs(p,mod):
    out=[1]
    for k in range(1,p):
        out.append(out[-1]*(8*k-7)*(8*k-5)*pow(64*k*k,-1,mod)%mod)
    return out
def adjacent_legendre(p,n):
    # x=(2/3)s, s^2=2 in F_p[s]/(s^2-2)
    c=2*pow(3,-1,p)%p
    old=(1,0); now=(0,c)
    if n==0:return old
    for k in range(1,n):
        xc=(2*c*now[1]%p,c*now[0]%p)
        inv=pow(k+1,-1,p)
        nxt=(((2*k+1)*xc[0]-k*old[0])*inv%p,
             ((2*k+1)*xc[1]-k*old[1])*inv%p)
        old,now=now,nxt
    return now
def check(p):
    assert p%24==13
    n=(p-1)//4; mod=p*p
    xnear=adjacent_legendre(p,n-1)
    assert xnear[1]==0 and xnear[0]!=0
    near=xnear[0]
    fp1=original_coeffs(p,p)
    lam=pow(9,-1,p)
    derivative=sum(k*fp1[k]*pow(lam,k-1,p) for k in range(1,p))%p
    assert derivative==(-9*pow(8,-1,p)*near)%p
    orig=original_coeffs(p,mod)
    lam2=pow(9,-1,mod)
    rv=poly_eval(orig,lam2,mod)
    fv=poly_eval(orig,pow(lam2,p,mod),mod)
    assert rv%p==0 and fv%p==0
    q9=(pow(9,p-1,mod)-1)//p
    carry=q9*pow(8,-1,p)*near%p
    assert ((fv-rv)//p)%p==carry
    return p,near,derivative,q9,rv//p,fv//p,carry
def main():
    result=[check(p) for p in primes(3000) if p%24==13]
    assert len(result)==53
    print('PASS_N1_N2_ALL',len(result),'primes')
    print('FINITE_CONJECTURAL_P2_ZEROS',sum(x[4]==0 for x in result))
    for r in result:
        if r[0] in (13,37,61,109,373):print('CERTIFICATE',r)
if __name__=='__main__':main()
