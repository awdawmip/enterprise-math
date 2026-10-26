#!/usr/bin/env python3
"""Exact author check: corrected Clausen scalar/left-face/infinity filtration.

Only integer modular arithmetic in Z/(p^2), Z/(p^4) with unit inverses.
No original-class CM/Frobenius, native Gateway run or independent review.
"""
from collections import defaultdict

CHANNELS=((0,2),(1,2),(0,3))

def prime_targets(bound):
    return [p for p in range(7,bound+1,6)
            if all(p%d for d in range(2,int(p**.5)+1))]

def jets(p):
    q=p*p;m=(p-1)//6;half=p*pow(2,-1,q)%q
    u=[[0]*p for _ in range(4)]
    u[0][0]=1
    for a in range(4):
        for r in range(1,p):
            def v(b,s):return u[b][s] if b>=0 and s>=0 else 0
            num=((r-1-m)*(r-1-2*m)*v(a,r-1)
                 +3*r*v(a-1,r)-(3*(r-1)-4*m)*v(a-1,r-1)
                 +2*v(a-2,r-1))
            u[a][r]=num*pow(r*(r-half)%q,-1,q)%q
    return u

def moments(p,u,a,b):
    q=p*p;m=(p-1)//6;H=2*m
    pp=[1]*(H+1);nn=[1]*(H+1)
    inv2=pow(2,-1,q)
    for i in range(1,H+1):pp[i]=pp[i-1]*2%q;nn[i]=nn[i-1]*inv2%q
    c=defaultdict(int);k=0
    I0p=I1p=P=J=0
    for ell in range(1,H+1):
        g=pp[ell]*u[b][p-ell]%q
        I0p+=g*P
        I1p+=g*((6*ell-1)*P-6*J)
        P+=nn[ell]*u[a][ell];J+=ell*nn[ell]*u[a][ell]
    for j in range(1,H+1):
        x=nn[j]*u[a][j]%q
        for ell in range(1,H+1):
            n=ell-j
            y=pp[ell]*u[b][p-ell]%q
            z=x*y%q
            c[n]=(c[n]+z)%q
            if n<=0:k+=j*z
    A=sum(c.values())%q
    B=sum(n*mass for n,mass in c.items())%q
    I0=sum(mass for n,mass in c.items() if n>0)%q
    I1=sum((6*n-1)*mass for n,mass in c.items() if n>0)%q
    U=sum(mass for n,mass in c.items() if n<=0)%q
    T=sum((1-6*n)*mass for n,mass in c.items() if n<=0)%q
    K=k%q
    R=(K-pow(2,-1,q)*sum((p-n)*mass for n,mass in c.items() if n<=0))%q
    L=1-H
    yl=(-2*m*u[a][2*m]*u[b][p-1])%q
    assert c[L]*pow(2,-L,q)%q==u[a][2*m]*u[b][p-1]%q
    assert U==(A-I0)%q and T==(A-6*B+I1)%q
    assert (I0,I1)==(I0p%q,I1p%q)
    assert T==((1-6*p)*U+12*K-12*R)%q
    return dict(A=A,B=B,I0=I0,I1=I1,U=U,T=T,K=K,R=R,YL=yl)

def adjoint_delta(p):
    q=p*p;N=(p-1)//3-1
    la=0
    for t in range(1,N+1):
        la=((p+2*t-2)*la-pow(2,1-t,q))*pow(p+2*t-1,-1,q)%q
    return (pow(2,-N,q)-(p+2*N)*la)%q

def original_Q_over_p2(p):
    q4=p**4;r=[1]
    for n in range(p-1):
        r.append(r[-1]*(6*n+1)*(3*n+1)*pow(36*(n+1)**2,-1,q4)%q4)
    Q=sum((6*(a+b)+1)*r[a]*r[b]
          for a in range(p) for b in range(p-a,p))%q4
    assert Q%(p*p)==0
    return Q//(p*p)

def check(p):
    q=p*p;m=(p-1)//6
    u=jets(p)
    d={ab:moments(p,u,*ab) for ab in CHANNELS}
    z02,z12,z03=[d[ab] for ab in CHANNELS]
    gamma=pow(2,-p,q)*pow(18,-1,q)%q
    inv6=pow(6,-1,q)
    bracket=(z02['T']+p*(6*z02['U']-(z12['T']+z03['T'])*inv6))%q
    endpoint=(z02['A']-6*z02['B']+p*(6*z02['A']
              -(z12['A']-6*z12['B']+z03['A']-6*z03['B'])*inv6))%q
    infinity=(z02['I1']+p*(-6*z02['I0']
              -(z12['I1']+z03['I1'])*inv6))%q
    assert bracket==(endpoint+infinity)%q
    Q=original_Q_over_p2(p)
    assert Q==gamma*bracket%q
    delta=adjoint_delta(p)
    C={ab:delta*d[ab]['YL']%q for ab in CHANNELS}
    assert C[(0,2)]==C[(0,3)]==0
    assert C[(1,2)]==(-2*m*delta*u[1][2*m]*u[2][p-1])%q
    assert bracket==(
        z02['U']+12*(z02['K']-z02['R'])
        -p*inv6*(z12['U']+z03['U'])
        -2*p*(z12['K']+z03['K']-z12['R']-z03['R'])
    )%q
    edge_scalar=2*p*C[(1,2)]%q
    assert edge_scalar==(-4*m*p*delta*u[1][2*m]*u[2][p-1])%q
    output=dict(p=p,delta=delta,C12=C[(1,2)],edge_scalar=edge_scalar,
                gamma=gamma,bracket=bracket,Q=Q,
                endpoint=endpoint,infinity=infinity,
                endpoint_Q=gamma*endpoint%q,infinity_Q=gamma*infinity%q)
    if p==13:
        assert Q==104 and C[(1,2)]==72 and edge_scalar==13
        assert (gamma*edge_scalar)%q==52
        assert (z02['I0'],z02['I1'],z12['I1'],z03['I1'])==(71,140,96,66)
    if p==733:
        assert Q==133477 and bracket==468744 and gamma==377719
        assert delta==176653 and C[(1,2)]==300530
        assert z02['T']==14284 and z12['T']==108012 and z03['T']==526050
        assert endpoint==251948 and infinity==216796
        assert (gamma*endpoint%q,gamma*infinity%q)==(381643,289123)
        assert edge_scalar==0 and (gamma*infinity)%p!=0
    return output

if __name__=='__main__':
    tests=[check(p) for p in prime_targets(211)]
    extra=check(733)
    print('PASS',len(tests)+1,'primes; exact original Q, corrected channels, Ward/infinity')
    for obj in [next(d for d in tests if d['p']==13),extra]:
        print(obj)
