"""D25 R41/R42 p-free factorial, exact transport and first jets (author-side)."""
from math import isqrt

def primes(n=997):
    for p in range(7,n+1):
        if p%6==1 and all(p%d for d in range(2,isqrt(p)+1)):
            yield p

def fact_units(p,q):
    f=[1]*(4*p)
    for i in range(1,4*p):
        a=i
        while a%p==0:a//=p
        f[i]=f[i-1]*a%q
    return f

def prod(p,q,t,n):
    z=1
    for i in range(1,n+1):z=z*(1+t*p*pow(i,-1,q))%q
    return z

def run():
    counters={'primes':0,'R41':0,'R42':0,'S2_sum':0,'weight_exception':0}
    for p in primes():
        m=(p-1)//6;H=(3*p-1)//4;q=p**3;f=fact_units(p,q)
        inv=lambda x:pow(x%q,-1,q)
        h=[0]*p
        for i in range(1,p):h[i]=(h[i-1]+inv(i))%q
        def pf_tau(k):return f[k]*f[4*k]*inv(f[2*k]*f[3*k])*pow(3*inv(32),k,q)%q
        def wsu(k):
            ew=6*k+1;es=8*k+1
            vw=2*k//p+3*k//p;vs=4*k//p
            while ew%p==0:ew//=p;vw+=1
            while es%p==0:es//=p;vs+=1
            w=ew*f[2*k]*f[3*k]*inv(f[k]**5*pow(216,k,q))%q
            s=es*f[4*k]*inv(f[k]**4*pow(2304,k,q))%q
            return vw,vs,w,s
        for k in range(4*m+1,p):
            a=2*k-p;b=3*k-2*p;t=pf_tau(k)
            vw,vs,w,s=wsu(k)
            assert vw==3
            if k<=H:
                r=4*k-2*p;c=3*p-1-4*k
                z=(-1)**c*f[k]*inv(f[a]*f[b]*f[c])*pow(3*inv(32),k,q)%q
                t0=z*prod(p,q,2,r)*inv(prod(p,q,1,a)*prod(p,q,2,b)*prod(p,q,-1,c))%q
                jet=2*h[r]-h[a]-2*h[b]+h[c]
                assert vs==2 and t==t0 and t%p**2==z*(1+p*jet)%p**2
                assert s==w*(8*k+1)*inv(6*k+1)*t%q
                counters['R41']+=1
            else:
                r=4*k-3*p
                z=3*f[k]*f[r]*inv(f[a]*f[b])*pow(3*inv(32),k,q)%q
                t0=z*prod(p,q,2,p-1)*prod(p,q,3,r)*inv(prod(p,q,1,a)*prod(p,q,2,b))%q
                jet=3*h[r]-h[a]-2*h[b]
                assert t==t0 and t%p**2==z*(1+p*jet)%p**2
                e=8*k+1
                while e%p==0:e//=p
                if e!=8*k+1:counters['weight_exception']+=1
                assert vs==3+(0 if e==8*k+1 else (2 if p==7 else 1))
                assert s==w*e*inv(6*k+1)*t%q
                counters['R42']+=1
        # S2 aggregate cancellation: finite independent readback of R23 input
        su=0
        for k in range(3*m+1,H+1):
            vw,vs,w,s=wsu(k)
            if vs==2:su=(su+s)%p
        assert su==0,(p,su)
        counters['primes']+=1;counters['S2_sum']+=1
    print('R41/R42 exact p-free factorial PASS',counters)
if __name__=='__main__':run()
