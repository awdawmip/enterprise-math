from math import factorial,gcd,lcm

def carrier(d,q):
    u=q+d;n=2*q+d
    def S(v):
        tail=[1]*(d+1)
        for k in range(d-1,-1,-1):tail[k]=tail[k+1]*(v+k+3)
        pre=1
        for k in range(d+1):
            tail[k]*=pre;pre*=v-k
        return tail
    U,N=S(u),S(n);v=b=a=0
    for k in range(d+1):
        l=d-k;A=(k+1)*(l+1)*U[k]*N[l];B=(k+1)*l*U[k]*N[l-1] if l else 0
        v+=A;b+=B;a+=(u-k)*(u+k+2)*(A+B)
    J=2*u*(2*u+1);L=4*n+2;W=L*a+u*U[d]*N[0]*q*(2*d+3)*(n+2);Q=J*L*b;Z=L*(q*a+J*(b+v));return 3*q*(4*q+3*d+1)**2*W*Q-32*(3*q+d+1)*Z**2

def val(x,p):
    if not x:return 999999
    k=0
    while x%p==0:x//=p;k+=1
    return k

def fixed(d):
    B=(factorial(d+2)//lcm(*range(1,d+3)))**4
    D=0; n=4*d+9
    for q in range(n+1):
        P=carrier(d,q);a,r=divmod(P,B);assert r==0
        D=gcd(D,a)
        if D==1:break
    return D

if __name__=='__main__':
    for d in range(81,121):
        f=fixed(d);print(d, f, *(val(f,p) for p in [2,3,5,7,11]),flush=True)
