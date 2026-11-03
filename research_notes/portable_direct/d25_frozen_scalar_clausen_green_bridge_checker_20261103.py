"""Exact D25 frozen scalar / finite Clausen Green binding regression."""
from math import comb, isqrt

def primes(lim):
    s=bytearray(b'\x01')*(lim+1)
    s[:2]=b'\x00\x00'
    for d in range(2,isqrt(lim)+1):
        if s[d]: s[d*d:lim+1:d]=b'\x00'*((lim-d*d)//d+1)
    return [p for p in range(13,lim+1) if s[p] and p%24 in (13,19)]

def trial(p):
    M=p**3
    b=a=1
    g=h=W=0
    for k in range(p):
        g=(g+b)%M
        h=(h+(12*k+1)*b)%M
        W=(W+(6*k+1)*a)%M
        if k+1<p:
            b=b*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,M)%M
            a=a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,M)%M
    assert g%p==0
    G=g//p
    assert (G*h-1)%p==0
    Delta=((G*h-1)%p**2)//p
    assert (g*h-W)%(p*p)==0
    Rtail=((g*h-W)%M)//(p*p)
    Eorig=((W-g*h)%M)//(p*p)

    r=(p-1)//6
    coeff=1; C=pow(10,-1,p); A=T=R=0
    cs=[]; bs=[]
    for i in range(1,r+1):
        coeff=coeff*(6*i-5)*(3*i-2)*pow(36*i*i,-1,p)%p
        if i>1:
            j=i-1
            C=C*36*j*j*pow((6*j+5)*(3*j+2),-1,p)%p
        T=(T+6*A+C)%p
        A=(A+C)%p
        R=(R+2*coeff*T)%p
        cs.append(C);bs.append(coeff)
    assert R==Rtail and (R+Eorig)%p==0

    K=[0]*(r+1)
    for t in range(r,0,-1):
        Q=(2*t-1)*(3*t-2)*(3*t-1)*pow(18,-1,p)%p
        ell=comb(r,t)*comb(2*r,t)%p
        K[t-1]=(t**3*K[t]-t*pow(3,-1,p)*ell)*pow(Q,-1,p)%p
    z=pow(2,-1,p)
    Kv=sum(x*pow(z,t,p) for t,x in enumerate(K[:-1]))%p
    Kth=sum(t*x*pow(z,t,p) for t,x in enumerate(K[:-1]))%p
    Egreen=z*(Kv+6*Kth)%p
    assert Egreen==Eorig and R==(-Egreen)%p
    assert ((W-p)%M)//p**2==(Delta-R)%p
    if p in (13,19,37,43,373):
        Woriginal=sum((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,M) for k in range(p))%M
        assert Woriginal==W
        Roriginal=2*sum(bs[i-1]*sum((1+6*(i-j))*cs[j-1] for j in range(1,i+1)) for i in range(1,r+1))%p
        assert Roriginal==R
    return p,Delta,R,Kv,Kth,Egreen,W

if __name__=="__main__":
    ps=primes(2000)
    rows=[trial(p) for p in ps]
    assert len(rows)==77
    print("PASS 77/77 original 216, frozen R, finite Green K, LIFT bridge")
    for row in rows:
        if row[0] in (13,19,37,43,373): print(row)
