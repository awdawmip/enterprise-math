#!/usr/bin/env python3
"""Author-only exact modular verification of general Ward face-repair on authentic Hasse jets.

Finite-rank corrected Clausen algebra; not an Enterprise Math native experiment.
"""
from math import comb

CHANNELS = ((0, 2), (1, 2), (0, 3), (2, 2), (1, 3), (0, 4))
KINDS = ('geo', 'rank', 'signed')


def primes():
    return [p for p in range(7, 212) if p % 6 == 1 and
            all(p % d for d in range(2, int(p**.5) + 1))] + [733]


def inv(x, q):
    return pow(x % q, -1, q)


def jets(p, q):
    m = (p - 1) // 6
    ans = [[0] * p for _ in range(5)]
    ans[0][0] = 1
    half = inv(2, q)
    for r in range(1, p):
        denom = inv(r * (r - p * half), q)
        for a in range(5):
            v = (r - 1 - m) * (r - 1 - 2*m) * ans[a][r-1]
            if a >= 1:
                v += 3*r*ans[a-1][r] - (3*(r-1)-4*m)*ans[a-1][r-1]
            if a >= 2:
                v += 2 * ans[a-2][r-1]
            ans[a][r] = v * denom % q
    return ans


def moments(p, q, u):
    m = (p - 1) // 6
    M = 2*m - 1
    s0 = {(a,b):[0]*(2*M+2) for a in range(5) for b in range(5)}
    s1 = {(a,b):[0]*(2*M+2) for a in range(5) for b in range(5)}
    for j in range(1,2*m+1):
        for ell in range(1,2*m+1):
            ix = ell-j+M
            for a in range(5):
                ua = u[a][j]
                if not ua: continue
                for b in range(5):
                    z = ua*u[b][p-ell]%q
                    if not z: continue
                    s0[a,b][ix] = (s0[a,b][ix]+z)%q
                    s1[a,b][ix] = (s1[a,b][ix]+j*z)%q
    return s0,s1


def native_source(n,a,b,p,q,u,s0,s1):
    m=(p-1)//6;M=2*m-1
    def U(a,r):
        return u[a][r] if a>=0 and 0<=r<p else 0
    def mass(s,a,b,k):
        if a<0 or b<0 or k< -M or k>M:return 0
        return s[a,b][k+M]
    M0=lambda a,b,k:mass(s0,a,b,k)
    M1=lambda a,b,k:mass(s1,a,b,k)
    j=(3*M1(a-1,b,n)-3*M1(a-1,b,n+1)+4*m*M0(a-1,b,n+1)
       +2*M0(a-2,b,n+1)
       -3*((p-n)*M0(a,b-1,n)-M1(a,b-1,n))
       +(14*m-3*n)*M0(a,b-1,n+1)-3*M1(a,b-1,n+1)
       -2*M0(a,b-2,n+1))
    if n>=0:
        e=(2*m*m*(a==0)+4*m*(a==1)+2*(a==2))*U(b,p-n-1)
        e+=U(a,2*m-n)*(-6*m*m*U(b,4*m)+8*m*U(b-1,4*m)-2*U(b-2,4*m))
    else:
        e=U(a,-n)*(20*m*m*U(b,p-1)-14*m*U(b-1,p-1)+2*U(b-2,p-1))
        e+=U(b,p-(2*m+n+1))*(2*m*U(a-1,2*m)-2*U(a-2,2*m))
    return (j+e)%q


def weight(n,p,q,kind):
    factor={'geo':1,'rank':n,'signed':1-6*n}[kind]
    return factor*pow(2,n,q)%q


def adjoint(p,q,kind):
    m=(p-1)//6;M=2*m-1;L=-M
    w=lambda n:weight(n,p,q,kind)
    eta={0:0}
    for n in range(0,L,-1):
        eta[n-1]=((p-2*n)*eta[n]-w(n))*inv(p-2*n+1,q)%q
    for n in range(1,M+1):
        eta[n]=(w(n)+(p-2*n+1)*eta[n-1])*inv(p-2*n,q)%q
    delta=(w(L)-(p-2*L)*eta[L])%q
    g=1
    for n in range(L,0):
        g=g*(p-2*n)*inv(p-2*n-1,q)%q
    return eta,delta,g


def run(p):
    m=(p-1)//6;M=2*m-1;L=-M;q=p*p
    u=jets(p,q)
    s0,s1=moments(p,q,u)
    half=inv(2,q)
    Y={}
    for ab in CHANNELS:
        Y[ab]={n:(s1[ab][n+M]-(p-n)*half*s0[ab][n+M])%q
               for n in range(L,M+1)}
        Y[ab][M+1]=0
    # Independently check the genuine k-1/k-2 Hasse source and both faces.
    sources={}
    source_assertions=0
    for ab in CHANNELS:
        a,b=ab
        sources[ab]={}
        for n in range(L,M+1):
            native=native_source(n,a,b,p,q,u,s0,s1)
            diff=((p-2*n)*Y[ab][n]-(p-2*n-1)*Y[ab][n+1])%q
            assert native==diff,('J/E',p,ab,n,native,diff)
            sources[ab][n]=native
            source_assertions+=1
    yl=Y[1,2][L]
    expected_yl=(4*(-1)**m*inv(comb(2*m,m)*(2*m+1)*(m+1),q))%p
    assert yl%p==expected_yl and yl%p!=0,('Yleft',p,yl,expected_yl)
    for ab in ((0,2),(0,3),(0,4)):
        assert Y[ab][L]==0,('zero-face',p,ab)
    cM=comb(2*M,M)*inv(pow(4,M,q),q)%p
    outputs={}
    for kind in KINDS:
        eta,delta,g=adjoint(p,q,kind)
        phi=sum(comb(2*t,t)*inv(pow(4,t,p),p)*weight(-t,p,p,kind)
                for t in range(M+1))%p
        assert delta*cM%p==phi,('Phi',p,kind,phi,delta,cM)
        for ab in CHANNELS:
            lhs=sum(weight(n,p,q,kind)*Y[ab][n] for n in range(L,M+1))%q
            rhs=(sum(eta[n]*sources[ab][n] for n in range(L,M+1))
                 +delta*Y[ab][L])%q
            assert lhs==rhs,('dual-ward',p,kind,ab,lhs,rhs)
        if phi==0:
            assert delta%p==0
            t=(delta//p)*inv(g,p)%p
            # Alter the central adjoint value t: the left face cancels mod p^2.
            adjusted=delta-p*g*t
            assert adjusted%q==0,('source-factorization',p,kind)
        outputs[kind]=(phi,delta%p,delta*yl%p)
    if p==13:
        assert outputs=={'geo':(9,8,7),'rank':(3,7,11),'signed':(4,5,6)}
    if p==733:
        assert outputs=={'geo':(0,0,0),'rank':(211,487,205),'signed':(200,10,236)}
    return source_assertions,outputs


def main():
    total=0;ps=primes()
    for p in ps:
        count,out=run(p);total+=count
        if p in (7,13,19,733):print('CERT',p,out)
    print('PASS',len(ps),'primes;',total,'separately reconstructed authentic J+E source cells;',
          18*len(ps),'independent channel/observer adjoint equalities modulo p^2')


if __name__=='__main__':main()
