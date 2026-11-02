#!/usr/bin/env python3
"""Exact p-local W216/Cauchy zeroth-jet transport, retaining upper-product boundary."""
import json, math

def run(p):
    assert p>3 and p%6==1
    M=p**3; m=(p-1)//6; N=p-1; x=pow(2,-1,M)
    # Unweighted source B_k=((1/2)_k(1/3)_k(2/3)_k)/(k!)^3
    # no 1/2^k here; W evaluation z=x supplies it
    b=[1]; efrac=[1]
    for k in range(1,p):
        b.append(b[-1]*(2*k-1)*(3*k-2)*(3*k-1)*pow(18*k**3,-1,M)%M)
        efrac.append(efrac[-1]*(2*k-1)*pow(2*k,-1,M)%M)
    ecoeff=[((-1)**j*math.comb(3*m,j))%M for j in range(3*m+1)]
    # Exact truncated rational convolution E*B and integer polynomial e*B
    c=[0]*p
    a_full=[0]*(p+3*m)
    for i,bi in enumerate(b):
        for j,ej in enumerate(efrac[:p-i]):
            c[i+j]=(c[i+j]+bi*ej)%M
        for j,ej in enumerate(ecoeff):
            a_full[i+j]=(a_full[i+j]+bi*ej)%M
    d=[(c[n]-a_full[n])%M for n in range(p)]
    assert all(v%p==0 for v in d)
    # independent log correction D using H_{j-1}
    logs=[0]*p
    harm=0
    for j in range(1,p):
        logs[j]=(p*pow(2*j,-1,M)+p*p*harm*pow(4*j,-1,M))%M
        harm=(harm+pow(j,-1,M))%M
    # check E-e = e*log within <p: independent of original B
    alt=[0]*p
    for i,ei in enumerate(ecoeff):
        for j in range(1,p-i):
            alt[i+j]=(alt[i+j]+ei*logs[j])%M
    assert all((efrac[i]-(ecoeff[i] if i<len(ecoeff) else 0)-alt[i])%M==0 for i in range(p))
    # D = truncated (eB)*log, not just e*log*B; same degree <p
    d2=[0]*p
    for i in range(p):
        for j in range(1,p-i):
            d2[i+j]=(d2[i+j]+a_full[i]*logs[j])%M
    assert d==d2
    def obs(coefs,shift=0):
        acc=0;xx=pow(x,shift,M)
        for n,v in enumerate(coefs,shift):
            acc=(acc+(3*n-1)*v*xx)%M
            xx=xx*x%M
        return acc
    w=sum((6*k+1)*bb*pow(x,k,M) for k,bb in enumerate(b))%M
    f=sum(bb*pow(x,k,M) for k,bb in enumerate(b))%M
    lam=obs(c)
    h=obs(a_full[p:],p)
    ds=obs(d)
    e0=pow(x,3*m,M)
    base=(2*pow(e0,-1,M)*(lam+h-ds)+3*p*f)%M
    assert w==base
    char=1 if p%3==1 else -1
    assert (w-p*char)%M==0
    return {
        'p':p,'modulus':M,'m':m,'original_W':w,'original_F':f,'e0':e0,
        'Cauchy_L':lam,'upper_boundary_H':h,'log_deformation_D':ds,
        'Cauchy_L_plus_H_mod_p':(lam+h)%p,
        'log_D_quot_p_mod_p2':(ds//p)%(p*p),
        'reconstructed_original_W':base,
        'source_split_RHS':{'cauchy_core':(2*pow(e0,-1,M)*lam)%M,'upper':(2*pow(e0,-1,M)*h)%M,'log':(-2*pow(e0,-1,M)*ds)%M,'scalar_3pF':(3*p*f)%M},
        'original_target_pass':(w-p*char)%M==0,
    }

def main():
    primes=[7,13,19,31,37,43,61,67,73,79,97,109,139,157,181,229,373,1171]
    rs=[run(p) for p in primes]
    print(json.dumps({'method':'exact p-local polynomial coefficient method with independent log correction','primes':len(primes),'checks':rs},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
