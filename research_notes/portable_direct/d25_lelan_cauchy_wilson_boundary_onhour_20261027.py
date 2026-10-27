"""Author-only exact Cauchy-to-weighted216/Wilson-boundary checker.
NOT native H0/B0, Source checkpoint, formal Result, or all-prime LIFT proof.
"""
import math

def check(p):
    assert p > 3 and p % 6 == 1
    m, N = (p-1)//6, p**3
    inv = lambda a: pow(a,-1,N)
    a=[1]
    for k in range(p-1):
        a.append(a[-1]*(2*k+1)*(3*k+1)*(3*k+2)*inv(36*(k+1)**3)%N)
    for k in range(p):
        rhs=math.comb(2*k,k)**2*math.comb(3*k,k)*pow(inv(216),k,N)%N
        assert a[k]==rhs,(p,k)
    t=[math.comb(2*j,j)*pow(inv(8),j,N)%N for j in range(p)]
    T,J=sum(t)%N,sum(j*v for j,v in enumerate(t))%N
    A,W=sum(a)%N,sum((6*k+1)*v for k,v in enumerate(a))%N
    x,y=[1],[1]
    for k in range(p-1):
        x.append(x[-1]*(3*k+1)*(6*k+1)*inv(36*(k+1)**2)%N)
        y.append(y[-1]*(3*k+2)*(6*k+5)*inv(36*(k+1)**2)%N)
    c=[sum(x[k]*y[n-k] for k in range(n+1))%N for n in range(p)]
    assert all(c[n]==sum(t[j]*a[n-j] for j in range(n+1))%N for n in range(p))
    S=sum((3*n-1)*v for n,v in enumerate(c))%N
    E=sum((3*(j+k)-1)*t[j]*a[k] for j in range(p) for k in range(p-j,p))%N
    assert (2*S-T*W-3*(2*J-T)*A+2*E)%N==0
    assert T%p==pow(2,(p-1)//2,p)
    assert (2*J-T)%p==0 and E%p==0
    if p%24 in (13,19):
        assert A%(p*p)==0 and W%p==0
        assert (2*(S+E)-T*W)%N==0
    wedge=sum((3*(j+k)-1)*t[j]*a[k]
              for j in range(4*m+1,p) for k in range(p-j,2*m+1))%N
    assert (E-wedge)%(p*p)==0
    h=0
    for r in range(1,2*m+1):
        j=p-r
        assert t[j]%p==0
        mu=(-2*pow(8,r-1,p)*pow(r*math.comb(2*r,r),-1,p))%p
        assert t[j]//p%p==mu
        h+=mu*sum((3*(k-r)-1)*a[k] for k in range(r,2*m+1))
    h%=p
    assert E%(p*p)==(p*h)%(p*p)
    if p==373:
        assert (W,S,E,T%(p*p),J%(p*p),A%(p*p))==(373,8487242,1042908,51100,94928,0)
        assert (S-W)%(p**3)==61*(p*p)
    return dict(p=p,S=S,W=W,E=E,T_modp2=T%(p*p),
                E_divp_modp=h,minus_3_over_2=(-3*pow(2,-1,p))%p)

if __name__=='__main__':
    for p in (7,13,19,31,37,43,61,67,73,211,373):
        print('PASS',check(p))
