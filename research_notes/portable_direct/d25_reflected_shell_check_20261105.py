from math import comb, factorial, isqrt

def primes(n):
    s=bytearray(b'\x01')*(n+1);s[:2]=b'\x00\x00'
    for x in range(2,isqrt(n)+1):
        if s[x]:s[x*x::x]=b'\x00'*(((n-x*x)//x)+1)
    return [i for i in range(5,n+1) if s[i]]

def calc(p):
    m=p**3; k0=(p+1)//2; h=(p-1)//2
    kA=(2*p-1)//3; kB=(3*p-1)//4
    ia=pow(216,-1,m);ib=pow(2304,-1,m)
    a=[];b=[]
    for k in range(k0,max(kA,kB)+1):
        if k<=kA:
            v=(comb(2*k,k)**2*comb(3*k,k)*pow(ia,k,m))%m
            assert v%p**2==0
            a.append((v//p**2)%p)
        if k<=kB:
            v=(comb(2*k,k)**2*comb(4*k,2*k)*pow(ib,k,m))%m
            assert v%p**2==0
            b.append((v//p**2)%p)
    t=factorial(k0)%p
    a0= (k0+1)*pow(216,-k0,p)*pow(t,-4,p)%p
    b0=4*pow(2304,-k0,p)*pow(t,-4,p)%p
    assert a[0]==a0,(p,a[0],a0)
    assert b[0]==b0,(p,b[0],b0)
    leg=pow(6,(p-1)//2,p)
    leg=-1 if leg==p-1 else 1
    ratio=a0*pow(b0,-1,p)%p
    assert ratio==(4*leg)%p,(p,ratio,leg)
    if p%24 in (13,19):
        assert leg == (-1 if p%24 == 13 else 1)
    G=1
    for j,v in enumerate(a):
        assert v == a0*G%p,(p,'A',j,v,a0*G%p)
        if j<len(a)-1:
            num=(6*j+5)*(6*j+7)*(j+1)
            den=9*(2*j+3)**3
            G=G*num*pow(den,-1,p)%p
    G=1
    for j,v in enumerate(b):
        assert v==b0*G%p,(p,'B',j,v,b0*G%p)
        if j<len(b)-1:
            num=(4*j+3)*(4*j+5)*(j+1)
            den=18*(2*j+3)**3
            G=G*num*pow(den,-1,p)%p
    sa=sum((6*j+4)*v for j,v in enumerate(a))%p
    sb=sum((8*j+5)*v for j,v in enumerate(b))%p
    assert sb==0,(p,'Bweighted',sb)
    m3=p**3
    AA=BB=1
    WA=WB=HA=HB=0
    for k in range(p):
        WA=(WA+(6*k+1)*AA)%m3
        WB=(WB+(8*k+1)*BB)%m3
        if k<=h:
            HA=(HA+(6*k+1)*AA)%m3
            HB=(HB+(8*k+1)*BB)%m3
        if k<p-1:
            d=pow(k+1,-1,m3)
            AA=AA*(((2*k+1)*(2*k+2)*(3*k+1)*(3*k+2)*(3*k+3))%m3)*pow(d,5,m3)*pow(216,-1,m3)%m3
            BB=BB*(4*k+1)*(4*k+2)*(4*k+3)*(4*k+4)*pow(d,4,m3)*pow(2304,-1,m3)%m3
    assert (WA-HA-p*p*sa)%m3==0,(p,'A full-half')
    assert (WB-HB-p*p*sb)%m3==0,(p,'B full-half')
    GA=sa*pow(a0,-1,p)%p
    GB=sb*pow(b0,-1,p)%p
    assert (WA-WB-(HA-HB)-p*p*b0*((4*leg*GA-GB)%p))%m3==0,(p,'balanced',WA,WB)
    return {'p':p,'k0':k0,'n_A':len(a),'n_B':len(b),'a0':a0,'b0':b0,'ratio':ratio,'leg6':leg,'signed_A_shell':sa,'signed_B_shell':sb,'normalized_A_kernel':GA,'normalized_B_kernel':GB}

if __name__=='__main__':
    ps=primes(997)
    ans=[calc(p) for p in ps]
    import json
    print(json.dumps({'count':len(ans),'frozen':sum(x['p']%24 in(13,19) for x in ans),'examples':[x for x in ans if x['p'] in(7,13,19,139,373)],'failures':0},ensure_ascii=False))
