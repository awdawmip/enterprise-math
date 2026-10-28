from fractions import Fraction
from math import isqrt

def primes_till(N):
    s=[True]*(N+1)
    s[0]=s[1]=False
    for i in range(2,isqrt(N)+1):
        if s[i]: s[i*i::i]=[False]*len(s[i*i::i])
    return [i for i in range(7,N+1) if s[i] and i%4==3]
def modinv(a,m):
    return pow(a%m,-1,m)

def check_case(p,details=False):
    d=(p-3)//4;m=p*p
    be=[1];ga=[1]
    a=[1];c=[1]
    for r in range(d):
        be.append(be[-1]*16*(r+1)*(4*r+3)*modinv((8*r+13)**2,m)%m)
        ga.append(ga[-1]*4*(4*r+4-p)*(4*r+3-p)*modinv((8*r+13-2*p)**2,m)%m)
        a.append(a[-1]*(8*r+1)**2*modinv(16*(4*r+3)*(r+1),m)%m)
        c.append(c[-1]*(4*r+1)**3*modinv((4*r+2)*(4*r+3)*(4*r+4),m)%m)
    v=[];g=[]
    for n in range(2*d+1):
        bn=be[n] if n<=d else 0
        bm=be[n-d-1] if d+1<=n<=2*d+1 else 0
        vn1=v[-1] if n else 0
        rhs=(8*(n+1)*(2*n+1)*(4*n+3)*vn1+25*(6*n+5)*bn-
             16*p*(d+1)*be[d]*(6*n-4*d+1)*bm)%m
        v.append(rhs*modinv((4*n+5)**3,m)%m)
        gn1=g[-1] if n else 0
        gam=ga[n] if n<=d else 0
        rhs=(4*(2*n+2-p)*(2*n+1-p)*(4*n+3-2*p)*gn1+
             (5-2*p)**2*(6*n+5-2*p)*gam)%m
        g.append(rhs*modinv((4*n+5-2*p)**3,m)%m)
    v_ref=[0]*(2*d+1);g_ref=[0]*(2*d+1)
    for i in range(d+1):
        for j in range(d+1):
            v_ref[i+j]=(v_ref[i+j]+be[i]*be[j])%m
            g_ref[i+j]=(g_ref[i+j]+ga[i]*ga[j])%m
    assert v==v_ref,(p,"v", next((n for n in range(2*d+1) if v[n]!=v_ref[n]),None))
    assert g==g_ref,(p,"g", next((n for n in range(2*d+1) if g[n]!=g_ref[n]),None))
    assert all((g[n]-v[n])%p==0 for n in range(2*d+1))
    u=modinv(9,m)
    M=W=J=0
    for n in range(d):
        jn=((g[n]-v[n])%m)//p
        M=(M+v[n]*pow(u,n,m))%m
        W=(W+(8*n+11)*v[n]*pow(u,n,m))%m
        J=(J+(8*n+11)*jn*pow(u,n,p))%p
    # GH-42 eq: T=BQ+(a_d²/9)[W + p(qW-4M+J)].
    z=9
    B=sum(a[n]*pow(z,n,m) for n in range(d+1))%m
    Q=sum((16*n+1)*a[n]*pow(z,n,m) for n in range(d+1))%m
    T=sum((8*n+1)*c[n]*pow(z,n,m) for n in range(d+1))%m
    q=(pow(3,p-1,m)-1)%m//p  # 3^(p-1) == 1 + p*q (mod p²)
    predicted=(B*Q + a[d]*a[d]*modinv(9,m)*(W+p*(q*W-4*M+J)))%m
    assert predicted==T,(p,predicted,T,M,W,J,q)
    # reverse full upper half mod p (and p² with correction).
    for r in range(d+1):
        assert g[2*d-r] == c[r]*modinv(a[d]*a[d],m)%m, (p,r)
    # first-jet g-v matches pair source H
    H=[0]
    for j in range(d):
        Hj=(H[-1] +4*modinv(8*j+13,p)-modinv(4*j+4,p)-modinv(4*j+3,p))%p
        H.append(Hj)
    for n in range(2*d+1):
        j_ref=sum(be[i]*be[n-i]*(H[i]+H[n-i]) for i in range(max(0,n-d),min(d,n)+1))%p
        assert ((g[n]-v[n])%m)//p==j_ref,(p,n)
    if details:
        return {"p":p,"d":d,"M":M%p,"W":W%p,"J":J,"q":q,"T_p2":T,
                "upper_boundary_raw":(-16*p*(d+1)*be[d]*(6*(d+1)-4*d+1)*be[0])%m,
                "beta_d":be[d]%p,"gamma_d":ga[d]%p,
                "v_mid":v[d], "g_mid":g[d], "jmid":((g[d]-v[d])%m)//p}

def check_notch(p):
    d=(p-3)//4
    n0=(p-2)//3 if p%3==2 else None
    found=[]
    for n in range(d+1,2*d+2):
        factor=(6*n-4*d+1)%p
        if factor==0: found.append(n)
    expected=[n0] if p%12==11 else []
    assert found==expected,(p,found,expected)
    return found

from fractions import Fraction as F
def rational_checks(d):
 p=4*d+3
 b=[F(1)]; gam=[F(1)]
 for r in range(d):
  b.append(b[-1]*F(16*(r+1)*(4*r+3),(8*r+13)**2))
  gam.append(gam[-1]*F(4*(4*r+4-p)*(4*r+3-p),(8*r+13-2*p)**2))
 v=[sum(b[i]*b[n-i] for i in range(max(0,n-d),min(d,n)+1)) for n in range(2*d+1)]
 g=[sum(gam[i]*gam[n-i] for i in range(max(0,n-d),min(d,n)+1)) for n in range(2*d+1)]
 for n in range(2*d+2):
  vcurr=v[n] if n<=2*d else F(0)
  vprev=v[n-1] if n>0 else F(0)
  gcurr=g[n] if n<=2*d else F(0)
  gprev=g[n-1] if n>0 else F(0)
  betan=b[n] if n<=d else F(0)
  betanew=b[n-d-1] if d+1<=n<=2*d+1 else F(0)
  gamn=gam[n] if n<=d else F(0)
  rhs=8*(n+1)*(2*n+1)*(4*n+3)*vprev+25*(6*n+5)*betan-16*p*(d+1)*b[d]*(6*n-4*d+1)*betanew
  assert (4*n+5)**3*vcurr == rhs,("v",d,n)
  rhs2=4*(2*n+2-p)*(2*n+1-p)*(4*n+3-2*p)*gprev+(5-2*p)**2*(6*n+5-2*p)*gamn
  assert (4*n+5-2*p)**3*gcurr == rhs2,("g",d,n)

def main():
    for d in range(1,13): rational_checks(d)
    print("PASS_GH47_GH48_EXACT_RATIONAL 12 d=1..12")
    ps=primes_till(2000)
    for p in ps:
        check_case(p)
        check_notch(p)
    exceptions=sum(bool(check_notch(p)) for p in ps)
    print(f"PASS_GH47_GH48_LINEAR_PADIC_RECURRENCES {len(ps)} primes p<2000 p=3(mod4)")
    print(f"PASS_GH48_BOUNDARY_NOTCH {exceptions} p=11(mod12) among {len(ps)} cases")
    for p in (7,11,19,23,43,67):
        print("CASE",check_case(p,True),"notch=",check_notch(p))

if __name__=="__main__": main()
