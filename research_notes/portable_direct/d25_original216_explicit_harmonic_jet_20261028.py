"""D25 author-side explicit harmonic jet; exact modular integers; no native experiment."""
from math import comb, factorial
def harmonic_ports(p, log=False):
    assert p > 3 and p%6==1
    m=(p-1)//6; M=p**3
    f=[1]*p
    for i in range(1,p): f[i]=f[i-1]*i%M
    ifact=[pow(z,-1,M) for z in f]
    H=[0]*p
    H2=[0]*p
    for i in range(1,p):
        t=pow(i,-1,M)
        H[i]=(H[i-1]+t)%M
        H2[i]=(H2[i-1]+t*t)%M
    def termprod(fs,ds,sgn=1):
        a=sgn
        for k in fs: a=a*f[k]%M
        for k in ds: a=a*ifact[k]%M
        return a
    inv2=pow(2,-1,M); inv3=pow(3,-1,M);inv4=inv2**2%M;inv9=inv3**2%M
    I2=inv2; I3=inv3; I6=I2*I3%M
    A0=A1=A2=C1=C2=D2=0
    for n in range(2*m+1):
        a=(6*n+1)*(-1)**n*termprod([3*m,2*m,4*m],[3*m-n,2*m-n,4*m-n,n,n,n]) *pow(inv2,n,M)%M
        h3=(H[3*m]-H[3*m-n])%M
        h2=(H[2*m]-H[2*m-n])%M
        h4=(H[4*m]-H[4*m-n])%M
        l=-(I2*h3 +I3*h2+2*I3*h4)%M
        e=(inv4*(H2[3*m]-H2[3*m-n])+inv9*(H2[2*m]-H2[2*m-n]) +4*inv9*(H2[4*m]-H2[4*m-n]))%M
        A0=(A0+a)%M
        A1=(A1+a*l)%M
        A2=(A2+a*(l*l-e)*inv2)%M
    for n in range(2*m+1,3*m+1):
        c=(6*n+1)*termprod([3*m,4*m,2*m,n-2*m-1], [3*m-n,4*m-n,n,n,n]) *pow(inv2,n,M)*I3%M
        h3=(H[3*m]-H[3*m-n])%M
        h4=(H[4*m]-H[4*m-n])%M
        v=(-I2*h3-2*I3*h4+I3*(H[n-2*m-1]-H[2*m]))%M
        C1=(C1+c)%M
        C2=(C2+c*v)%M
    for n in range(3*m+1,4*m+1):
        d=(6*n+1)*(-1)**(m+n)*termprod([3*m,2*m,4*m,n-3*m-1,n-2*m-1],[4*m-n,n,n,n])*pow(inv2,n,M)*I6%M
        D2=(D2+d)%M
    j0=A0
    j1=(A1+C1)%p**2
    j2=(A2+C2+D2)%p
    direct=0
    for n in range(p):
        w=(6*n+1)*comb(2*n,n)**2 * comb(3*n,n)*pow(216,-n,M) % M
        direct=(direct+w)%M
    if log: print("p",p,"m",m,"J0",j0,"J1",j1,"J2",j2,"parts", A1%p**2,C1%p**2, A2%p,C2%p,D2%p,"W",direct,"same",(j0+p*j1+p*p*j2)%M==direct)
    return j0,j1,j2,(A1%p**2,C1%p**2,A2%p,C2%p,D2%p),direct
if __name__=="__main__":
    cases=[7,13,19,31,37,43,61,67,73,211,373]
    for p in cases:
        j0,j1,j2,part,w=harmonic_ports(p)
        assert (j0+p*j1+p*p*j2)%p**3==w, (p,"reconstruct")
    assert harmonic_ports(373)[0:3]==(15521276,47909,133)
    assert harmonic_ports(373)[3]==(3122,44787,82,158,266)
    print("PASS_D25_ORIGINAL216_HARMONIC_JET_EXPLICIT_PORTS",len(cases),"primes; p373 fixture matched")
