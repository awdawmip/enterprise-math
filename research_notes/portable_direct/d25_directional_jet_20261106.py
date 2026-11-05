"""D25 exact directional jet / independent 4-jet and W_q check; author-side only."""
from math import isqrt
def primes(n):
    z=bytearray(b'\x01')*(n+1); z[:2]=b'\0\0'
    for i in range(2,isqrt(n)+1):
        if z[i]:z[i*i:n+1:i]=b'\0'*(((n-i*i)//i)+1)
    return [i for i in range(5,n+1) if z[i]]
def data(p):
    r=((p*p-1)//6)%p
    return tuple((i*r)%p for i in (2,3,4))
def invs(p):
    v=[0]*p;v[1]=1
    for j in range(2,p):v[j]=(-(p//j)*v[p%j])%p
    return v
def scalar(p,s,v):
    a=-v[2]%p;u,e=1,0;Z=L=S=0
    for j in range(p):
        w=(6*j+1)%p;Z=(Z+u)%p;L=(L+w*u)%p;S=(S+w*e)%p
        if j==p-1:break
        t=[(x-j)%p for x in s];P=t[0]*t[1]*t[2]%p
        Q=(t[0]*t[1]+t[0]*t[2]+t[1]*t[2])%p
        ij=v[j+1];c=a*P*pow(ij,3,p)%p
        d=a*(Q+3*P*ij)*pow(ij,3,p)%p
        u,e=c*u%p,(c*e+d*u)%p
    H=[0]*p
    for j in range(1,p):H[j]=(H[j-1]+v[j])%p
    phi=(pow(2,p-1,p*p)-1)//p
    B=(6*Z+(sum(H[x] for x in s)-phi)*L-S)%p
    return Z,L,S,B
def fulljet(p,s,v):
    a=-v[2]%p;u=1;dx=[0,0,0];da=0
    Z=L=Dalpha=0;D=[0,0,0]
    for j in range(p):
        w=(6*j+1)%p;Z=(Z+u)%p;L=(L+w*u)%p
        for i in range(3):D[i]=(D[i]+w*dx[i])%p
        Dalpha=(Dalpha+w*da)%p
        if j==p-1:break
        t=[(x-j)%p for x in s];ij=v[j+1]
        C=a*t[0]*t[1]*t[2]*pow(ij,3,p)%p
        E=[a*t[(i+1)%3]*t[(i+2)%3]*pow(ij,3,p)%p for i in range(3)]
        newd=[(C*dx[i]+E[i]*u)%p for i in range(3)]
        newa=C*(da-u*ij)%p
        u,dx,da=C*u%p,newd,newa
    return Z,L,D,Dalpha
def original_W(p):
    m=p*p;term=total=1
    for k in range(1,p):
        term=term*(2*k-1)*(3*k-2)*(3*k-1)*pow(36*k**3,-1,m)%m
        total=(total+(6*k+1)*term)%m
    return total
def test(n=3000):
    count=nonzero=0
    for p in primes(n):
        s=data(p);v=invs(p)
        Z,L,S,B=scalar(p,s,v)
        Z2,L2,D,Da=fulljet(p,s,v)
        assert (Z,L)==(Z2,L2),(p,"base")
        assert S==(sum(D)-3*Da)%p,(p,"direction")
        H=[0]*p
        for j in range(1,p):H[j]=(H[j-1]+v[j])%p
        phi=(pow(2,p-1,p*p)-1)//p
        assert B==(6*Z+(sum(H[x] for x in s)-phi)*L-sum(D)+3*Da)%p,(p,"B")
        if L==0:
            w=original_W(p)
            assert w%p==0,(p,"W")
            assert (w//p-Z+S*pow(6,-1,p))%p==0,(p,"Theta")
        count+=1;nonzero+=int(Z!=0)
    print("PASS",count,"primes <=",n,"Z_nonzero",nonzero,"Z_zero",count-nonzero)
if __name__=="__main__":
    import sys
    test(int(sys.argv[1]) if len(sys.argv)>1 else 3000)
