#!/usr/bin/env python3
"""Author-side exact fourth-digit Wilson/harmonic jets for original W216 and V2304.
No native H0/B0, canonical claim, or formal admission is asserted.
"""
from math import isqrt

def primes_through(z):
    sieve = bytearray(b'\x01')*(z+1)
    sieve[:2] = b'\x00\x00'
    for q in range(2, isqrt(z)+1):
        if sieve[q]:
            sieve[q*q:z+1:q] = b'\x00'*((z-q*q)//q+1)
    return [p for p in range(5,z+1) if sieve[p]]

def direct(p):
    M=p**4
    a=b=1; wi=[0]*4; vi=[0]*4
    iw=pow(216,-1,M); iv=pow(2304,-1,M)
    for n in range(p):
        g=(2*n)//p+(3*n)//p
        wi[g]=(wi[g]+(6*n+1)*a)%M
        g=(4*n)//p
        vi[g]=(vi[g]+(8*n+1)*b)%M
        if n+1<p:
            inv=pow(n+1,-1,M)
            a=a*(2*n+1)*(2*n+2)*(3*n+1)*(3*n+2)*(3*n+3)*pow(inv,5,M)*iw%M
            b=b*(4*n+1)*(4*n+2)*(4*n+3)*(4*n+4)*pow(inv,4,M)*iv%M
    return wi,vi

def derived(p, suppress_wilson=False):
    M=p**4; Q=p**3
    f=[1]*p
    for i in range(1,p): f[i]=f[i-1]*i%M
    omega=((f[-1]%Q+1)%Q)//p
    actual_omega=omega
    if suppress_wilson: omega=0
    inv=[0]*p; h=[0]*p; e2=[0]*p
    for k in range(1,p):
        inv[k]=pow(k,-1,Q)
        h[k]=(h[k-1]+inv[k])%Q
        e2[k]=(e2[k-1]+inv[k]*h[k-1])%Q
    iw=pow(216,-1,M); iv=pow(2304,-1,M)
    wi=[0]*4; vi=[0]*4
    for n in range(p):
        if 3*n<p:
            base=(6*n+1)*f[2*n]*f[3*n]*pow(f[n],-5,M)*pow(iw,n,M)%M
            wi[0]=(wi[0]+base)%M
        elif 2*n<p:
            r=3*n-p
            base=-(6*n+1)*f[2*n]*f[r]*pow(f[n],-5,M)*pow(iw,n,M)%M
            L1=(h[r]-omega)%Q
            L2=(e2[r]-omega*h[r])%Q
            wi[1]=(wi[1]+p*base*(1+p*L1+p*p*L2))%M
        elif 3*n<2*p:
            r,s=2*n-p,3*n-p
            base=(6*n+1)*f[r]*f[s]*pow(f[n],-5,M)*pow(iw,n,M)%M
            wi[2]=(wi[2]+p*p*base*(1+p*(h[r]+h[s]-2*omega)))%M
        else:
            r=2*n-p;s=3*n-2*p
            base=-2*(6*n+1)*f[r]*f[s]*pow(f[n],-5,M)*pow(iw,n,M)%M
            wi[3]=(wi[3]+p**3*base)%M
        if 4*n<p:
            base=(8*n+1)*f[4*n]*pow(f[n],-4,M)*pow(iv,n,M)%M
            vi[0]=(vi[0]+base)%M
        elif 4*n<2*p:
            r=4*n-p
            base=-(8*n+1)*f[r]*pow(f[n],-4,M)*pow(iv,n,M)%M
            L1=(h[r]-omega)%Q
            L2=(e2[r]-omega*h[r])%Q
            vi[1]=(vi[1]+p*base*(1+p*L1+p*p*L2))%M
        elif 4*n<3*p:
            r=4*n-2*p
            base=2*(8*n+1)*f[r]*pow(f[n],-4,M)*pow(iv,n,M)%M
            vi[2]=(vi[2]+p*p*base*(1+2*p*(h[r]-omega)))%M
        else:
            r=4*n-3*p
            base=-6*(8*n+1)*f[r]*pow(f[n],-4,M)*pow(iv,n,M)%M
            vi[3]=(vi[3]+p**3*base)%M
    return wi,vi,actual_omega

def main():
    tested=primes_through(2000)
    for p in tested:
        w,v=direct(p)
        x,y,_=derived(p)
        assert (w,v)==(x,y), ('four-grade mismatch',p,w,v,x,y)
        chi=1 if p%3==1 else -1
        assert (sum(x)-2*sum(y)+p*chi)%p**4==0, ('C4 discrepancy',p)
    print('Exact four-grade match:',len(tested),'primes <=2000; 8 ports per prime.')
    for p in (13,19,373):
        w,v,omega=derived(p)
        x,y,_=derived(p,suppress_wilson=True)
        M=p**4
        chi=1 if p%3==1 else -1
        altered=(sum(x)-2*sum(y)+p*chi)%M
        print('p',p,'omega mod p^2',omega,'W grades',w,'V grades',v,
              'C4 residual', (sum(w)-2*sum(v)+p*chi)%M,
              'C4 residual if Wilson terms removed',altered)
        assert altered!=0
    print('All-prime jet formulas proved algebraically; universal C4 still open.')
if __name__ == '__main__':
    main()
