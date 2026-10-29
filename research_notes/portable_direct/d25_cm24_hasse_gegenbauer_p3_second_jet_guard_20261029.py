"""Finite p^3 CM Hasse/Gegenbauer second-parameter-jet modular checker; not native H0/B0."""
from math import comb

def check(p):
    m=p**3
    q=8*pow(9,-1,m)%m
    def sc(a,z):return (a[0]*z%m,a[1]*z%m)
    def add(a,b):return ((a[0]+b[0])%m,(a[1]+b[1])%m)
    def neg(a):return ((-a[0])%m,(-a[1])%m)
    def sub(a,b):return add(a,neg(b))
    def mul(a,b):return ((a[0]*b[0]+q*a[1]*b[1])%m,(a[0]*b[1]+a[1]*b[0])%m)
    one=(1,0);x=(0,1);zero=(0,0)
    e=(p-1)//4;k=(p-1)//2
    I=[0]+[pow(i,-1,m) for i in range(1,2*e+2)]
    u=sc(sub(x,one),I[2]);v=sc(add(x,one),I[2])
    s=sc(add(x,one),pow(8,-1,m))
    h=zero;power=one
    for j in range(e+1):
        h=add(h,sc(power,comb(k,2*j)*comb(2*j,j)))
        power=mul(power,s)
    b0=one;b1=sc(x,-2*k)
    if e==0:B=one
    elif e==1:B=b1
    else:
        for n in range(1,e):
            b2=sc(add(sc(mul(x,b1),2*(n-k)),sc(b0,2*k-n+1)),I[n+1])
            b0,b1=b1,b2
        B=b1
    H=[0]*(e+1);H2=[0]*(e+1)
    for i in range(1,e+1):
        H[i]=(H[i-1]+I[i])%m
        H2[i]=(H2[i-1]+I[i]*I[i])%m
    P=zero;Ja=zero;Jb=zero;Jab=zero;Jbb=zero
    uu=[one];vv=[one]
    for i in range(e):
        uu.append(mul(uu[-1],u))
        vv.append(mul(vv[-1],v))
    for j in range(e+1):
        c=sc(mul(uu[j],vv[e-j]),comb(e,j)**2)
        aa=(H[e]-H[j])%m
        bb=(H[e]-H[e-j])%m
        dbb=(H2[e]-H2[e-j])%m
        P=add(P,c)
        Ja=add(Ja,sc(c,aa))
        Jb=add(Jb,sc(c,bb))
        Jab=add(Jab,sc(c,aa*bb))
        Jbb=add(Jbb,sc(c,bb*bb-dbb))
    D1=add(sc(P,H[e]),Jb)
    D2=add(sc(P,H[e]*H[e]-3*H2[e]),add(sc(add(Ja,Jb),2*H[e]),add(sc(Jab,2),Jbb)))
    lhs=sub(B,sc(h,(-1)**e))
    first=sc(D1,-p*I[2]);second=sc(D2,p*p*pow(8,-1,m))
    assert lhs==add(first,second),(p,lhs,add(first,second))
    assert all((lhs[j]-first[j])%(p*p)==0 for j in (0,1))
    return (p,e,lhs,first,second,tuple(z%p for z in D2))

if __name__=='__main__':
    ps=[p for p in range(5,300) if all(p%d for d in range(2,int(p**0.5)+1))]
    for p in ps:check(p)
    print('PASS_D25_CM24_SECOND_JET_BRIDGE_P3',len(ps),'primes below 300')
    for p in (13,17,19,23,37,61,373):
        print(check(p))
