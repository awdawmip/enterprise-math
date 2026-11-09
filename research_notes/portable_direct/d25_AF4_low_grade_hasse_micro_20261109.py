"""D25 AF4: exact original low-grade Hasse jets and X^2 boundary.
Author-side proof experiment; UNREVIEWED, NOT_ADMITTED, NOT_NATIVE.
"""
from math import comb, factorial, isqrt

def prime(p):
    return p > 1 and all(p % d for d in range(2, isqrt(p)+1))

def model(p, kind):
    M = p**4
    if kind == "W":
        m=(p-1)//6
        return [(-3*m,pow(2,-1,M)),(-2*m,pow(3,-1,M)),
                (-4*m,2*pow(3,-1,M)%M)], 2, 3*m, 6
    if p%4==1:
        t=(p-1)//4
        return [(-t,pow(4,-1,M)),(-2*t,pow(2,-1,M)),
                (-3*t,3*pow(4,-1,M)%M)],9,2*t,8
    t=(p-3)//4
    return [(-3*t-2,3*pow(4,-1,M)%M),(-2*t-1,pow(2,-1,M)),
            (-t,pow(4,-1,M))],9,2*t+1,8

def multiply_linear(a,constant,slope,M):
    return [(constant*a[k]+(slope*a[k-1] if k else 0))%M
            for k in range(4)]

def jets_and_terminal(p,kind):
    M=p**4
    params,z_inv,N,slope=model(p,kind)
    a=[1,0,0,0]
    sums=[0]*4
    for n in range(N+1):
        w=1+slope*n
        sums=[(sums[k]+w*a[k])%M for k in range(4)]
        if n==N:break
        for t,c in params:a=multiply_linear(a,n+t,c,M)
        d=pow(z_inv*(n+1)**3,-1,M)
        a=[v*d%M for v in a]
    low=sum(sums[k]*(p**k) for k in range(4))%M
    q=[1,0,0,0]
    for t,c in params:q=multiply_linear(q,N+t,c,M)
    zi=pow(z_inv,-1,M)
    boundary=[-zi*sum(a[k-j]*q[j] for j in range(k+1))%M
              for k in range(4)]
    assert boundary[0]==boundary[1]==0
    if kind=="W":
        m=(p-1)//6
        b2=m*factorial(2*m)*factorial(4*m)*pow(6*factorial(3*m)**2,-1,M)*pow(z_inv,-(3*m+1),M)%M
    elif p%4==1:
        t=(p-1)//4
        b2=(-1)**t*t*t*factorial(t-1)*factorial(3*t)*pow(8*factorial(2*t)**2,-1,M)*pow(z_inv,-(2*t+1),M)%M
    else:
        t=(p-3)//4
        b2=(-1)**t*(t+1)*factorial(t)*factorial(3*t+2)*pow(8*factorial(2*t+1)**2,-1,M)*pow(z_inv,-(2*t+2),M)%M
    assert boundary[2]==b2,(p,kind,boundary[2],b2)
    return sums,low,boundary

def original_low(p,kind):
    _,_,N,slope=model(p,kind)
    M=p**4
    result=0
    for n in range(N+1):
        if kind=="W":
            coeff=comb(2*n,n)**2*comb(3*n,n)
            denom=216
        else:
            coeff=comb(4*n,2*n)*comb(2*n,n)**2
            denom=2304
        result=(result+(1+slope*n)*coeff*pow(denom,-n,M))%M
    return result

def check(p):
    assert prime(p) and p%6==1
    jW,W,bW=jets_and_terminal(p,"W")
    jV,V,bV=jets_and_terminal(p,"V")
    if p<=373:
        assert W==original_low(p,"W")
        assert V==original_low(p,"V")
    L=(W-2*V+p)%(p**4)
    assert L%(p*p)==0
    return p,W,V,L//(p*p),bW[2]%p,bV[2]%p

if __name__=="__main__":
    expected={13:(24687,4407,94,2,6),19:(127091,20596,238,5,6),
              37:(428534,810485,498,18,14),43:(3274622,2862295,524,40,10),
              73:(19674741,12059600,4495,1,55),
              373:(7176413322,6953946051,90746,57,79)}
    for p,ans in expected.items():
        actual=check(p)
        assert actual[1:]==ans,(p,actual,ans)
        print(*actual)
    tested=0
    for p in range(7,1001):
        if prime(p) and p%6==1:
            check(p)
            tested+=1
    assert tested==80
    print("PASS",tested,"exact Hasse and quadratic boundary cases; direct binomial cases p<=373")
