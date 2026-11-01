"""Verify original weighted 3F2 p^4 terminal source and seam; portable only."""
from math import prod

def ps(limit):
    for n in range(7, limit+1):
        if n % 6 != 1: continue
        if all(n % d for d in range(2, int(n**0.5)+1)):
            yield n

def val(a,p):
    return next((v for v in range(4) if a % p**(v+1)),4)

def direct_top(p):
    M=p**4; num=1
    for j in range(p-1):
        num=num*(2*j+1)*(3*j+1)*(3*j+2)%M
    den=pow(18,p-1,M)*pow(prod(range(1,p)),3,M)%M
    return num*pow(den,-1,M)%M

def check(p,independent=False):
    M=p**4; r=(p-1)//6
    cuts=((p-1)//3,(p-1)//2,2*(p-1)//3)
    zs=(pow(2,-1,M),pow(9,-1,M))
    sums=[0,0]; powers=[1,1]
    a=1; last=None; carry=None
    for n in range(p):
        w=(6*n+1)*a%M
        e=sum(n>j for j in cuts)
        assert val(a,p)==e and val(w,p)==e+(n==r), (p,n)
        if n==r: carry=w//p%p
        if n==r+1:
            assert w%p==36*pow(125,-1,p)*carry%p,(p,'seam')
        if n:
            c=18*(6*n-5)*n**3*w-(6*n+1)*(2*n-1)*(3*n-2)*(3*n-1)*last
            assert c%M==0,(p,n,'ODE internal')
        for i,z in enumerate(zs):
            v=18*(6*n-5)*n**3*w-(6*n+7)*(2*n+1)*(3*n+1)*(3*n+2)*w*z
            sums[i]=(sums[i]+v*powers[i])%M
            powers[i]=powers[i]*z%M
        if n<p-1:
            last=w
            a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(18*(n+1)**3,-1,M)%M
        else:
            assert a//p**3%p==p-1
            assert w//p**3%p==5%p
            assert (-(6*p+1)*(2*p-1)*(3*p-2)*(3*p-1)*w)%M==10*p**3%M
            if independent: assert a==direct_top(p)
    for s,z in zip(sums,zs):
        assert s==10*p**3*pow(z,p,M)%M,(p,'ODE point')
    return (p,r,carry,36*pow(125,-1,p)*carry%p,5*pow(9,-1,p)%p)

def main():
    count=0; classes={13:0,19:0,'other':0}
    selected={7,13,19,37,43,61,109,211,373}
    for p in ps(3000):
        result=check(p,p in selected); count+=1
        classes[p%24 if p%24 in (13,19) else 'other']+=1
        if p in selected: print('CERT',result)
    print('ALL_PASS',count,classes,'p4 coefficientwise and two evaluation points')
if __name__=='__main__': main()
