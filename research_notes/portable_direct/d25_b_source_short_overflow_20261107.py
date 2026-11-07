#!/usr/bin/env python3
"""D25 B3/B5 exact Cartier-compatible short-overflow readout, standard-library finite fields.
Author-side portable mathematics, not native H0/B0 experiment.
"""

def primes(n):
    q=bytearray(b'\x01')*(n+1);q[:2]=b'\x00\x00'
    for i in range(2,int(n**0.5)+1):
        if q[i]:q[i*i:n+1:i]=b'\x00'*(((n-i*i)//i)+1)
    return [p for p in range(5,n+1) if q[p] and p%24 in (13,19)]

def data(p):
    assert p%8 in (3,5)
    k=(p-3)//8 if p%8==3 else (p-5)//8
    inv=lambda a:pow(a%p,-1,p)
    q=[1]
    for i in range(k):
        q.append(q[-1]*(k-i)*(3*k+1-i)*inv((i+1)**2)%p)
    r=[3*inv(64*(k+1)*(3*k+2))%p]
    J=5*k if p%8==3 else 5*k+2
    for j in range(J):
        r.append(r[-1]*(j+1)**2*inv((k+j+2)*(3*k+j+3))%p)
    return k,q,r

def direct_full_projection(p,q,r):
    x=pow(9,-1,p)
    e=0
    for i,qi in enumerate(q):
        for j,rj in enumerate(r):
            n=p-1+i-j
            if n<p:
                e=(e+2*qi*rj*pow(x,n,p)*(1+8*n))%p
            if p%8==5 and n+1<p:
                e=(e-2*qi*rj*pow(x,n+1,p)*(1+8*(n+1)))%p
    return e

def short_overflow(p,q,r):
    # Let C=1 for B3, 1-z for B5.  C Q R = Pi_<p(C Q R) + z^p H.
    # Only reflected-tail r_0..r_k enter H; coefficients are exact in F_p.
    k=len(q)-1
    H=[]
    for ell in range(k+1):
        h=sum(q[j+ell+1]*r[j] for j in range(k-ell)) if ell<k else 0
        if p%8==5:
            h-=sum(q[j+ell]*r[j] for j in range(k-ell+1))
        H.append(h%p)
    if p%8==3:assert H[-1]==0
    return H

def compact_readout(p,q,r,H):
    x=pow(9,-1,p)
    qx=sum(a*pow(x,i,p) for i,a in enumerate(q))%p
    dqx=sum(i*a*pow(x,i,p) for i,a in enumerate(q))%p
    Rx=sum(a*pow(x,p-1-j,p) for j,a in enumerate(r))%p
    hx=sum(a*pow(x,i,p) for i,a in enumerate(H))%p
    dhx=sum(i*a*pow(x,i,p) for i,a in enumerate(H))%p
    # If Q(x)=0, (1+8D)(CQR)(x)=8 C(x) (D Q)(x) R(x)
    assert qx==0,(p,'CM root prerequisite not met',qx)
    C=1-x if p%8==5 else 1
    E=(16*C*dqx*Rx-2*x*(hx+8*dhx))%p
    return E, (dqx*Rx)%p, hx, dhx

def main():
    P=primes(2500)
    vals={}
    for p in P:
        k,q,r=data(p)
        H=short_overflow(p,q,r)
        e0=direct_full_projection(p,q,r)
        e1,DQR,h,dh=compact_readout(p,q,r,H)
        assert e0==e1,(p,e0,e1)
        if p in (13,19,43,67,373):vals[p]=(e1,DQR,h,dh)
    assert {p:t[0] for p,t in vals.items()}=={13:0,19:8,43:33,67:46,373:220}
    print('PASS',len(P),'target primes p<2500: full projected Euler-Gauss convolution == short-overflow Cartier-compatible readout')
    print('p:(E_B, (D Q) R, H, D H) at x=1/9:',vals)

if __name__=='__main__':main()
