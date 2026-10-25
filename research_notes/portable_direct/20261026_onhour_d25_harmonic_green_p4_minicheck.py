#!/usr/bin/env python3
"""Author exact modular cross-check of D25 harmonic-reduced p^4 corner.
Portable only: not original-class CM, independent review or native Source run.
"""

def primes(limit):
    for p in range(7, limit+1, 6):
        if all(p%d for d in range(2,int(p**.5)+1)):
            yield p

def check(p):
    m=(p-1)//6; q=p*p; q4=p**4; ph=p*pow(2,-1,q)%q
    fact=[1]*p; den=[1]*p; H=[0]*p; D=[0]*p
    for i in range(1,p):
        fact[i]=fact[i-1]*i%q
        den[i]=den[i-1]*(i-ph)%q
        H[i]=(H[i-1]+pow(i,-1,q))%q
        D[i]=(D[i-1]+pow((i-ph)%q,-1,q))%q
    F=[pow(t,-1,q) for t in fact]
    E=[pow(t,-1,q) for t in den]
    inv2=pow(2,-1,q); inv6=pow(6,-1,q)
    P=J=Z=V=low=mid=0
    for j in range(1,2*m+1):
        r=p-j
        u2=2*(-1 if m%2 else 1)*fact[m]*fact[2*m]*fact[r-1-m]*fact[r-1-2*m]*F[r]*E[r]%q
        h=(H[m]+2*H[2*m]-H[r-1-m]-2*H[r-1-2*m]+3*D[r])%q
        g=pow(2,j,q)*u2%q
        P=(P+g)%q; J=(J+j*g)%q
        Z=(Z+g*h)%q; V=(V+j*g*h)%q
        C=((6*j+1)*P-6*J)%q
        Ch=((6*j+1)*Z-6*V)%q
        if j<=m:
            u0=fact[m]*fact[2*m]*F[m-j]*F[2*m-j]*F[j]*E[j]%q
            a=(H[m]-H[m-j]+2*(H[2*m]-H[2*m-j])+3*D[j])%q
            low=(low+pow(inv2,j,q)*u0*(C+p*(6*P-(a*C+Ch)*inv6)))%q
        else:
            u1=(-1 if (m+j)%2==0 else 1)*fact[m]*fact[j-1-m]*fact[2*m]*F[2*m-j]*F[j]*E[j]%q
            mid=(mid+pow(inv2,j,q)*u1*C)%q
    expected=pow(2,-p,q)*pow(18,-1,q)*(low-p*inv6*mid)%q
    r=[1]
    for j in range(p-1):
        r.append(r[-1]*(6*j+1)*(3*j+1)*pow(36*(j+1)**2,-1,q4)%q4)
    mass=[0]*(p+1); moment=[0]*(p+1)
    for j in range(p-1,-1,-1):
        mass[j]=(mass[j+1]+r[j])%q4
        moment[j]=(moment[j+1]+j*r[j])%q4
    raw=sum(r[j]*((6*j+1)*mass[p-j]+6*moment[p-j]) for j in range(p))%q4
    assert raw%(p*p)==0
    assert expected==raw//(p*p),(p,expected,raw//(p*p))
    return expected

if __name__=='__main__':
    checked=[(p,check(p)) for p in primes(997)]
    print('PASS',len(checked),'primes: original ordered Q/p^2 mod p^2 vs harmonic formula')
    print('witnesses',[(p,v) for p,v in checked if p in (7,13,19,31,37,43,211)])
