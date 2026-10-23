"""D25 author-side exact Fraction crosscheck, not native benchmark/admission.

Checks Morley p^2 normalization, coupled C+P parity, and full LOW/Beta
joint residual equivalence for the finite set p=6m+1 with 1<=m<18.
"""
from fractions import Fraction as Q
from math import comb, factorial, isqrt


def H(k, degree=1):
    return sum((Q(1, j ** degree) for j in range(1, k + 1)), Q(0))


def beta_half(m, r):
    return Q((-1)**m * factorial(m) * factorial(r-1), 2**(m+r) * factorial(m+r))


def beta_full(m, r):
    return sum((Q(comb(m, j) * (-1)**(m-j), 2**(m-j) * (r+j))
                for j in range(m+1)), Q(0))


def residuals(m):
    p=6*m+1
    H1=[H(i) for i in range(4*m+1)]
    Hs=[H(i,2) for i in range(4*m+1)]
    weights=[Q(1) if r<=m else Q(1,3) for r in range(1,3*m+1)]
    beta=[beta_half(m,r) for r in range(1,3*m+1)]
    V=sum((w*beta_full(m,r) for r,w in enumerate(weights,1)),Q(0))
    I=sum((w*(3*m*beta_full(m-1,r)+beta_full(m,r))
           for r,w in enumerate(weights,1)),Q(0))
    J1=sum((w*(3*r+Q(p-2,2))*beta[r-1]
            for r,w in enumerate(weights,1)),Q(0))
    Theta=Q(3*(-1)**m-2,2**m)+I+J1
    F0=sum((w*b for w,b in zip(weights,beta)),Q(0))
    F1=Q(0); F1prime=Q(0); J2=Q(0)
    for r,(w,b) in enumerate(zip(weights,beta),1):
        d=(m-r if r<=m else r-m-1)
        Jh=Q(1,2)*(H1[r-1]-H1[m])+Q(2,3)*(H1[2*m]-H1[d])+Q(1,3)*(H1[4*m]-H1[3*m-r])
        J2+=w*b*((3*r-1)*Jh+1)
        F1+=w*b*Jh
        F1prime+=2*(r-1)*w*b*Jh
    R=Q(1,4)*F1prime+(m+Q(1,2))*F1
    assert J2==F0+6*R-p*F1
    C=Q(1,2)*sum((Q((-1)**j,j) for j in range(1,m+1)),Q(0))+Q(2,3)*(H1[2*m]-H1[m])+Q(1,3)*(H1[4*m]-H1[m])
    MM=Q(0); PP=Q(0)
    for n in range(m+1):
        b=Q((-1)**n * comb(m,n), 2**n)
        w=6*n-1
        An=H1[m]-H1[m-n]
        Ln=-An/2+Q(2,3)*(H1[2*m]-H1[2*m-n])+Q(1,3)*(H1[4*m]-H1[4*m-n])
        Mn=Ln*Ln/2-Q(1,8)*(Hs[m]-Hs[m-n])+Q(4,9)*(Hs[2*m]-Hs[2*m-n])+Q(5,18)*(Hs[4*m]-Hs[4*m-n])
        MM+=b*w*Mn
        PP+=b*w*Q(1,8)*(An*An-(Hs[m]-Hs[m-n]))
    X1=Q(0); qm=Q(0); qp=Q(0)
    for j in range(m):
        aj=Q((-1)**j*comb(m-1,j),2**j)
        lam=2*(H1[2*m]-H1[2*m-j])-(H1[2*m+j]-H1[2*m]); an=H1[m]-H1[m-j]
        dj=Q(2,2*m-j)-Q(1,2*m+j+1); ej=Q(1,m-j)
        X1+=aj*((2*dj-3*ej)*lam-3*dj*an+dj*dj-3*dj*ej)/18
        qm+=aj/(2*m-j)**2
        qp+=aj/(2*m+j+1)**2
    combined=Q(1,2**m)*(H1[2*m]+Q(3*(-1)**m,2)*H1[m]-H1[m//2])
    rhs_M=PP+X1+Q(4,9)*qm+Q(5,18)*qp
    norm=Q(4**(p-1)*factorial(2*m)**3, factorial(p-1))
    normsharp=Q((-1)**m*factorial(2*m)**3, factorial(3*m)**2)
    A=Q(factorial(p-1),3**(p-1)*factorial(2*m)**3)
    chi=(Q(4,3)**(p-1)-1)/p
    orig=(A*Theta-1)/p+A*(Q(1,2**m)*C-2*V+MM+J2)-chi
    short=(Theta-normsharp)/p+combined-2*V+X1+Q(4,9)*qm+Q(5,18)*qp+F0+6*R
    return dict(p=p, m=m, Theta=Theta, norm=norm, normsharp=normsharp, original=orig, short=short, A=A,
                M=MM, Mshort=rhs_M, CplusP=Q(1,2**m)*C+PP,
                CplusPshort=combined, norm_quotient=(Theta-normsharp)/p,
                beta_left=F0, beta_full=V, R=R)


def mod(q,p):
    assert q.denominator % p
    return q.numerator * pow(q.denominator,-1,p) % p

if __name__=='__main__':
    checks=[]
    for m in range(1,18):
        p=6*m+1
        if any(p%d==0 for d in range(2,isqrt(p)+1)):continue
        a=residuals(m)
        assert mod(a['norm']-a['normsharp'],p*p)==0,(p,'Morley p^2')
        assert mod(a['Theta']-a['normsharp'],p)==0,(p,'normalization integrality')
        assert mod(a['M']-a['Mshort'],p)==0,(p,'M')
        assert mod(a['CplusP']-a['CplusPshort'],p)==0,(p,'C+P')
        assert mod(a['original']-a['A']*a['short'],p)==0,(p,'joint')
        assert mod(p*a['short'],p*p)==0,(p,'p^2 coupled certificate')
        assert mod(a['original'],p)==0,(p,'original finite witness')
        checks.append((p,mod(a['CplusP'],p),mod(a['norm_quotient'],p),mod(a['short'],p)))
    print('PASS original and coupled joint residuals, p-unit and exact first-jet checks',len(checks),'prime cases')
    print('p, C+P mod p, (Theta-G)/p mod p, full joint residual mod p')
    for row in checks:print(*row,sep=',')
