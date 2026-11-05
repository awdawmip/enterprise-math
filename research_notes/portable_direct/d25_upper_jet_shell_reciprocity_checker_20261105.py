#!/usr/bin/env python3
"""Exact author-side check for D25 upper jet/shell; NOT native H0/B0."""
import json

def primes_below(n):
    sieve=bytearray(b'\x01')*(n+1); sieve[0:2]=b'\x00\x00'
    for d in range(2,int(n**0.5)+1):
        if sieve[d]: sieve[d*d:n+1:d]=b'\x00'*((n-d*d)//d+1)
    return [p for p in range(7,n+1) if sieve[p] and p%6==1]

def check(p):
    n=(p-1)//6; N=3*n; K=2*n
    iv=lambda x: pow(x%p,-1,p)
    inv2=iv(2); inv3=iv(3); inv18=iv(18)
    w=[1]; v=[0]; u=[0]
    for k in range(1,N+1):
        x=k-1
        P0=(x-N)*(x-K)*(x-4*n)%p
        P1=((x-K)*(x-4*n)*inv2+(x-N)*(x-4*n)*inv3+2*(x-N)*(x-K)*inv3)%p
        P2=(13*x*inv18-2*n)%p
        ik=iv(k)**3%p
        w.append(P0*w[-1]*ik%p)
        v.append((P0*v[-1]+P1*w[-2])*ik%p)
        u.append((P0*u[-1]+P1*v[-2]+P2*w[-2])*ik%p)
    assert all(w[k]==0 for k in range(K+1,N+1))
    assert all(v[k]!=0 for k in range(K+1,N+1))
    h=[(6*k+1)*pow(2,-k,p)%p for k in range(N+1)]
    s2=sum(h[k]*u[k] for k in range(N+1))%p
    upper=sum(h[k]*u[k] for k in range(K+1,N+1))%p
    U=n*n*v[N]*iv(2)**(N+2)*iv(N+1)**3%p
    g=1; H=0; B=0; T=0; rN=u[N]*iv(v[N])%p
    samples=[]
    for j in range(n):
        k=N-j; A=v[k]*iv(v[N])%p
        assert (A*g*(2*j+1)**3)%p==1, (p,j,'reciprocal')
        assert (u[k]*iv(v[k])-rN)%p==H, (p,j,'harmonic')
        B+=(6*k+1)*pow(2,j,p)*A*(rN+H)
        T+=(3*j+2)*pow(2,-j,p)*g
        if j in (0,1,n-1): samples.append((j,A,g,H))
        if j+1<n:
            H=(H+iv(2)*iv(j+1)+iv(3)*iv((6*j+7)*iv(6))+2*iv(3)*iv((6*j+5)*iv(6)))%p
            a=(j+5*iv(6))%p; b=(j+7*iv(6))%p; c=(j+3*iv(2))%p
            g=g*((j+1)*a*b%p)*iv(c)**3%p
    pred=v[N]*pow(2,-N,p)*B%p
    TA=-2*U*T%p
    both=v[N]*pow(2,-N,p)*(B-n*n*iv(2)*iv(N+1)**3*T)%p
    assert upper==pred and both==(upper+TA)%p
    return {'p':p,'vN':v[N],'uN':u[N],'rN':rN,
       'S2lower':(s2-upper)%p,'S2upper':upper,'S2':s2,'U':U,'TA':TA,
       'S2upper_plus_TA':both,'samples':samples}

if __name__=='__main__':
    ps=primes_below(10000)
    outputs=[check(p) for p in ps]
    result={'domain':'primes p=6n+1, 7<=p<=10000','checked':len(outputs),'failed':0,
      'anchors':[r for r in outputs if r['p'] in (7,13,19,139,373,9973)]}
    with open('d25_jet_shell_reciprocity_results_20261105.json','w') as f:
        json.dump(result,f,indent=2)
    print(json.dumps(result,indent=2))
