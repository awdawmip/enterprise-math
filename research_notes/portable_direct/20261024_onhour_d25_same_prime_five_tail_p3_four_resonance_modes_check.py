"""Author-side exact D25 five-port p^3 check. Not a native benchmark."""
from math import isqrt


def primes(n):
    return (p for p in range(7,n+1) if p%6==1 and all(p%d for d in range(2,isqrt(p)+1)))


def unit_table(p):
    q=p*p;f=[1]*p;h=[0]*p
    for j in range(1,p):
        f[j]=f[j-1]*j%q
        h[j]=(h[j-1]+pow(j,-1,q))%q
    def uf(t):
        assert 0<=t<2*p
        return f[t] if t<p else f[p-1]*f[t-p]*(1+p*h[t-p])%q
    def ar(r,n):
        a=f[6*r]*uf(4*r+2*n)*uf(3*n)%q
        b=pow(3,6*r,q)*f[2*r]*pow(216,n,q)*f[n]**2*f[2*r+n]**2*uf(4*r+n)%q
        return a*pow(b,-1,q)%q
    return ar


def predicted(p,k,ar):
    m=(p-1)//6;q=p*p;N=4*k+1;L=6*m-8*k
    Q=360*k*k+274*k+49
    b=ar(k,N)*2*(3*k+1)*Q*pow(3*(2*k+1),-1,q)%q
    e0=(b*pow(8*k+3,-1,q) if L<=0 else b if L==2 else p*b*pow(8*k+3,-1,q))%q
    es=[e0]
    for j in range(1,5):
        es.append((p if L>j+3 else 1)*ar(k+1,4*k+j)*(36*k+6*j+13)%q)
    return es


def strip(a,p):
    v=0
    while a%p==0: a//=p;v+=1
    return v,a


def stream(r,N,p):
    M=p**3;A=1;D=pow(3,6*r,M)
    for j in range(1,6*r+1):A=A*j%M
    for j in range(1,2*r+1):D=D*j**3%M
    A=A*pow(D,-1,M)%M
    v=0;u=1;out=[]
    for n in range(N+1):
        w,W=strip(6*n+12*r+1,p)
        out.append((v+w,A*u*W%M))
        if n==N:break
        na=(4*r+2*n+1)*(3*n+1)*(3*n+2)
        da=36*(n+1)*(2*r+n+1)*(4*r+n+1)
        nv,a=strip(na,p);dv,b=strip(da,p)
        v+=nv-dv;u=u*a*pow(b,-1,M)%M
        assert v>=0
    return out


def P(k,n):
    return (27*n**4+(324*k+180)*n**3+(1836*k*k+1746*k+429)*n*n
            +(4320*k**3+5940*k*k+2706*k+412)*n+3456*k**4
            +6336*k**3+4128*k*k+1184*k+128)


def independent(p,k):
    M=p**3;N=4*k+1
    old=stream(k,N,p);new=stream(k+1,N+3,p)
    a,b=strip(4*N*P(k,N),p)
    c,d=strip(9*(N+2*k+1)*(N+4*k+1)*(N+4*k+2)*(N+4*k+3)*(6*N+12*k+1),p)
    v,u=old[N]
    five=[(v+a-c,u*b*pow(d,-1,M)%M)]+new[N:N+4]
    assert all(v>=1 for v,u in five)
    x=[u*p**(v-1)%(p*p) for v,u in five]
    delta=(sum(u*p**v%M for v,u in new[:N+4])-sum(u*p**v%M for v,u in old[:N]))%M
    assert delta%p==0 and delta//p==sum(x)%(p*p)
    return x


def main():
    count=0;critical=[0]*4
    for p in primes(1000):
        m=(p-1)//6
        if m<2:continue
        ar=unit_table(p)
        kstar=(3*m-4)//4+1
        assert 6*m-8*kstar==[0,6,4,2][m%4]
        for k in range((m+1)//2,m):
            a=predicted(p,k,ar);b=independent(p,k)
            assert a==b,(p,k,a,b)
            if k==kstar:critical[m%4]+=1
            count+=1
    assert (count,critical)==(3027,[14,20,22,23])
    print('PASS 3027 exact p^3 five-port checks; critical classes',critical)
    p=211;m=35;ar=unit_table(p);k=26
    assert predicted(p,k,ar)==[37325,26960,2188,10171,3019]
    assert sum(sum(predicted(p,k,ar)) for k in range(18,35))%(p*p)==28274
    print('PASS p=211 critical ports and full upper-half transport')

if __name__=='__main__':main()
