"""Author exact checks for D25/LIFT diagonal moment closure (portable only).

Two parameter-Hasse constructions (rational recurrence and polynomial product),
then mass-only reconstruction of first/second labelled ranks. No native CM
experiment, independent review, or formal admission is claimed.
"""
from fractions import Fraction
from math import isqrt

CHANNELS = ((0, 2), (1, 2), (0, 3))


def target_primes(limit=211):
    out = []
    for p in range(7, limit + 1):
        if p % 6 != 1:
            continue
        if all(p % q for q in range(2, isqrt(p) + 1)):
            out.append(p)
    return out


def make_jets(m, modulus=None, method="recurrence"):
    p = 6*m+1
    R = (lambda x: x % modulus) if modulus is not None else (lambda x: x)
    half = (p*pow(2, -1, modulus)) % modulus if modulus else Fraction(p, 2)
    div = (lambda a,b: (a*pow(b % modulus,-1,modulus))%modulus) if modulus else (lambda a,b: a/b)
    coef = [[R(int(a==0)) for a in range(4)]]
    for r in range(1,p):
        A = R(r * R(r-half))
        B = R((r-1-m)*(r-1-2*m))
        D = R(3*(r-1)-4*m)
        row=[R(0)]*4
        if method=="recurrence":
            for a in range(4):
                right=B*coef[-1][a]
                if a>=1: right+=3*r*row[a-1]-D*coef[-1][a-1]
                if a>=2: right+=2*coef[-1][a-2]
                row[a]=R(div(R(right),A))
        elif method=="product":
            # Multiply by [(r-1-m-t)(r-1-2m-2t)]/[r(r-p/2-3t)].
            num=[B,R(-D),R(2)]
            inv=[R(0)]*4
            inv[0]=R(div(R(1),A))
            for k in range(1,4): inv[k]=R(div(R(3*r*inv[k-1]),A))
            ratio=[R(sum(num[i]*inv[k-i] for i in range(min(k,2)+1))) for k in range(4)]
            row=[R(sum(coef[-1][i]*ratio[k-i] for i in range(k+1))) for k in range(4)]
        else: raise ValueError(method)
        coef.append(row)
    return coef


def moment(coef,m,a,b,n,s,modulus=None):
    if a<0 or b<0: return 0
    p=6*m+1
    x=sum((j**s*coef[j][a]*coef[p-(j+n)][b]
         for j in range(1,2*m+1) if 1<=j+n<=2*m),0)
    return x%modulus if modulus else x


def endpoint(coef,m,a,b,n,modulus=None):
    p=6*m+1
    u=lambda aa,r: coef[r][aa] if 0<=aa<=3 and 0<=r<p else 0
    if n>=0:
        x=( (2*m*m*(a==0)+4*m*(a==1)+2*(a==2))*u(b,p-n-1)
           +u(a,2*m-n)*(-6*m*m*u(b,4*m)+8*m*u(b-1,4*m)-2*u(b-2,4*m)) )
    else:
        x=(u(a,-n)*(20*m*m*u(b,p-1)-14*m*u(b-1,p-1)+2*u(b-2,p-1))
           +u(b,p-(2*m+n+1))*(2*m*u(a-1,2*m)-2*u(a-2,2*m)))
    return x % modulus if modulus else x


def recover(coef,m,modulus=None):
    p=6*m+1
    low=1-2*m; high=2*m-1
    reduce = (lambda x: x%modulus) if modulus else (lambda x:x)
    half = p*pow(2,-1,modulus)%modulus if modulus else Fraction(p,2)
    divide = (lambda x,d:(x*pow(d%modulus,-1,modulus))%modulus) if modulus else (lambda x,d:x/d)
    masses={}; first={}; second={}
    def get(arr,a,b,n):return arr.get((a,b,n),0)
    for a,b in CHANNELS:
        for n in range(low,high+2):masses[a,b,n]=moment(coef,m,a,b,n,0,modulus)
        first[a,b,low]=reduce(2*m*masses[a,b,low])
        for n in range(low,high+1):
            A=6*m-2*n;B=-18*m*m+9*m*n-n*n;C=(p-n)*(half-n)
            lower=(3*get(first,a-1,b,n)-3*get(first,a-1,b,n+1)+4*m*get(masses,a-1,b,n+1)
                +2*get(masses,a-2,b,n+1)
                -3*((p-n)*get(masses,a,b-1,n)-get(first,a,b-1,n))
                +(14*m-3*n)*get(masses,a,b-1,n+1)-3*get(first,a,b-1,n+1)
                -2*get(masses,a,b-2,n+1))
            numerator=(p-2*n)*first[a,b,n]-C*masses[a,b,n]-B*masses[a,b,n+1]-lower-endpoint(coef,m,a,b,n,modulus)
            first[a,b,n+1]=reduce(divide(reduce(numerator),A))
        assert first[a,b,high+1]==0,(m,a,b,"terminal first")
        second[a,b,high+1]=0
        for n in range(high,low-1,-1):
            boundary=((2*m*m*(a==0)+4*m*(a==1)+2*(a==2))*coef[p-n-1][b] if n>=0 else 0)
            if n<0:
                r=p-(2*m+n+1)
                boundary+=(2*m*(coef[2*m][a-1] if a>=1 else 0)
                           -2*(coef[2*m][a-2] if a>=2 else 0))*coef[r][b]
            v=(second[a,b,n+1]+half*first[a,b,n]-3*m*first[a,b,n+1]
               +2*m*m*masses[a,b,n+1]+3*get(first,a-1,b,n)-3*get(first,a-1,b,n+1)
               +4*m*get(masses,a-1,b,n+1)+2*get(masses,a-2,b,n+1)+boundary)
            second[a,b,n]=reduce(v)
    return masses,first,second


def test():
    exact_count=0
    for m in range(1,6):
        C=make_jets(m,method="recurrence"); D=make_jets(m,method="product")
        assert C==D,(m,"direct Taylor")
        masses,first,second=recover(C,m)
        for a,b in CHANNELS:
            for n in range(1-2*m,2*m):
                assert first[a,b,n]==moment(C,m,a,b,n,1),(m,a,b,n,"first")
                assert second[a,b,n]==moment(C,m,a,b,n,2),(m,a,b,n,"second")
                exact_count+=2
    prime_count=0; checked=0
    for p in target_primes():
        m=(p-1)//6;mod=p*p
        C=make_jets(m,mod,"recurrence"); D=make_jets(m,mod,"product")
        assert C==D,(p,"modular direct Taylor")
        masses,first,second=recover(C,m,mod)
        for a,b in CHANNELS:
            for n in range(1-2*m,2*m):
                assert first[a,b,n]==moment(D,m,a,b,n,1,mod),(p,a,b,n,"first")
                assert second[a,b,n]==moment(D,m,a,b,n,2,mod),(p,a,b,n,"second")
                checked+=2
        prime_count+=1
    print(f"PASS: {exact_count} exact-rational moments (m=1..5); {prime_count} p=6m+1 primes <=211; {checked} modular moments mod p^2; 2 independent jet algorithms")


if __name__=="__main__":test()
