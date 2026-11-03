"""Original-216 D25 high-strip p^4 endpoint/normal-form check; Python stdlib."""
from math import comb

def primes(n):
    return [p for p in range(7,n+1) if p%6==1 and all(p%d for d in range(2,int(p**.5)+1))]

def mul(a,b,m):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%m
    return out

def D(P,p,m):
    c=(p+1)//2; v=pow(36,-1,m)
    A=[(18*c**3+27*c*c+13*c+2)*v%m,(54*c*c+54*c+13)*v%m,(54*c+27)*v%m,18*v%m]
    B=[c**3%m,3*c*c%m,3*c%m,1]
    shift=[0]*(len(P)+1)
    for j,x in enumerate(P):
        for i in range(j+1):shift[i]=(shift[i]+x*comb(j,i))%m
    t=mul(A,shift,m);u=mul(B,P,m)
    for i,x in enumerate(u):t[i]=(t[i]-x)%m
    while len(t)>1 and t[-1]==0:t.pop()
    return t

def ev(a,s,m):
    z=0
    for x in a[::-1]:z=(z*s+x)%m
    return z

n=0
for p in primes(2000):
    r=(p-1)//6;a=3*r+1;b=4*r+1;m=p**4;n+=r
    f=[1]*(3*b+1)
    for j in range(1,len(f)):f[j]=f[j-1]*(j if j%p else j//p)%m
    Y=[]
    for k in range(a,b+1):
        v=2*k//p+3*k//p
        assert v== (3 if k==b else 2)
        Y.append(f[2*k]*f[3*k]*pow(f[k],-5,m)*pow(216,-k,m)*p**(v-2)%m)
    for j in range(r):
        k=a+j;assert ((k+1)**3*Y[j+1]-(2*k+1)*(3*k+1)*(3*k+2)*pow(36,-1,m)*Y[j])%m==0
    for P in ([1],[0,1],[0,0,1],[1,-pow(r,-1,m)],[0,pow(r,-1,m)]):
        lhs=sum(ev(D(P,p,m),j,m)*Y[j] for j in range(r))%m
        rhs=(b**3*ev(P,r,m)*Y[-1]-a**3*ev(P,0,m)*Y[0])%m
        assert lhs==rhs,(p,P)
    for degree in range(3,11):
        rem=[0]*degree+[1];Q=[0]*(degree-2)
        while len(rem)>3:
            j=len(rem)-4;v=(-2*rem[-1])%m;Q[j]=(Q[j]+v)%m
            t=D([0]*j+[v],p,m)
            for i,x in enumerate(t):rem[i]=(rem[i]-x)%m
            while len(rem)>1 and rem[-1]==0:rem.pop()
        lhs=sum(pow(j,degree,m)*Y[j] for j in range(r))%m
        rhs=(sum(sum(pow(j,i,m)*Y[j] for j in range(r))*x for i,x in enumerate(rem))
             +b**3*ev(Q,r,m)*Y[-1]-a**3*ev(Q,0,m)*Y[0])%m
        assert lhs==rhs,(p,degree)
    if p in (13,19,373):
        H=sum((6*(a+j)+1)*Y[j] for j in range(r))%m
        print(p,'r',r,'H2/p2 mod p',H%p,'in',(-a**3*Y[0])%m,'out',(b**3*Y[-1])%m)
print('PASS',len(primes(2000)),'primes',n,'high positions, mod p^4; degrees 3..10')
