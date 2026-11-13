"""R597 exact cubic coefficient independent series check and optional root diagnostics."""
from fractions import Fraction as Q
from math import comb, factorial

N=3
ONE=(Q(1),Q(0),Q(0),Q(0))

def mul(a,b):
    return tuple(sum((a[i]*b[n-i] for i in range(n+1)),Q(0)) for n in range(N+1))

def bj_series(j):
    p=ONE
    for h in range(1,j+1):
        p=mul(p,(Q(1),Q(h+3,2),Q(0),Q(0)))
        p=mul(p,(Q(1),Q(-h,2),Q(0),Q(0)))
    w=[Q(0)]*(N+1)
    r=ONE
    for q in range((j+1)//2+1):
        if q:
            t=q-1
            b=Q(2*t+1,2)
            factor=(Q(1),Q(3,2),Q(3,2)*b,Q(3,2)*b*b)
            r=mul(r,factor)
        weight=Q(comb(j+1,2*q),2**j)
        for n in range(N+1):w[n]+=weight*r[n]
    return mul(p,tuple(w))

def alpha(j): return Q(0) if j==0 else Q(15*j+3,8)

def beta(j):
    v=Q(-32*j**3+501*j*j-349*j-18,384)
    return v+(Q(3,64) if j==0 else Q(15,64) if j==1 else Q(0))

def gamma(j):
    v=Q(-160*j**4+359*j**3-1814*j*j+1159*j+36,1024)
    return v+(Q(-9,256) if j==0 else Q(105,256) if j==1 else Q(-105,512) if j==2 else Q(0))

for j in range(121):
    coeff=bj_series(j)
    assert coeff==(Q(1),alpha(j),beta(j),gamma(j)),(j,coeff)
print('R597_EXACT_CUBIC_FORMAL_COEFFICIENT_PASS',121)

def cat(n): return comb(2*n,n)//(n+1)
def raw_h(k,s):
    return comb(2*k+1+s,2*s)*sum(comb(s-1,2*q)*4**q*cat(k-q) for q in range(min(k,(s-1)//2)+1))
def ratio(k,j):
    if not j:return Q(1)
    p=Q(1)
    for h in range(1,j+1):p*=(1+Q(h+3,2*k))*(1-Q(h,2*k))
    w=Q(0);r=Q(1)
    for q in range((j+1)//2+1):
        if q:r*=1+Q(3,2*(k-q+1)-1)
        w+=comb(j+1,2*q)*r
    return p*w/2**j
n=0
for k in range(2,21):
    h2=raw_h(k,2)
    for j in range(2*k):
        raw=Q(raw_h(k,j+2),h2)*Q(factorial(2*j+4),24*8**j*k**(2*j))
        assert raw==ratio(k,j),(k,j)
        n+=1
print('R597_INDEPENDENT_CATALAN_COEFFICIENT_PASS',n)

for j in (1,2,3,6,10):
    values=[]
    for k in (64,256,1024):
        v=k**4*(ratio(k,j)-1-alpha(j)/k-beta(j)/k**2-gamma(j)/k**3)
        values.append(f'{float(v):.8f}')
    print('R597_CUBIC_REMAINDER',j,' '.join(values))

try:
    import mpmath as mp
except ImportError:
    print('R597_NUMERIC_ROOT_DIAGNOSTIC_SKIPPED_NO_MPMATH')
else:
    mp.mp.dps=70
    J=55
    a=[mp.mpf(24)*8**j/mp.factorial(2*j+4) for j in range(J+1)]
    cf=[(-1)**j*a[j] for j in range(J+1)]
    def deriv(z,level):
        return mp.fsum(cf[j]*mp.factorial(j)/mp.factorial(j-level)*z**(j-level)
                       for j in range(level,J+1))
    def corr(z,order,derivative=0):
        fun=(alpha,beta,gamma)[order-1]
        return mp.fsum(cf[j]*mp.mpf(fun(j).numerator)/fun(j).denominator*mp.factorial(j)/mp.factorial(j-derivative)*z**(j-derivative)
                       for j in range(derivative,J+1))
    z=mp.findroot(lambda z:deriv(z,0),(mp.mpc('6.3','9.4'),mp.mpc('6.4','9.5')),tol=mp.mpf('1e-65'))
    f1=deriv(z,1);f2=deriv(z,2);f3=deriv(z,3)
    ell=-corr(z,1)/f1
    m=-(corr(z,2)+corr(z,1,1)*ell+f2*ell**2/2)/f1
    nu=-(corr(z,3)+corr(z,2,1)*ell+corr(z,1,1)*m+corr(z,1,2)*ell**2/2+f2*ell*m+f3*ell**3/6)/f1
    b,u,v,w=[mp.im(e) for e in (z,ell,m,nu)]
    e8=b*b/8+b*u/2+u*u/2+b*v+2*b*w+2*u*v
    print('R597_LIMIT_ROOT',mp.nstr(z,38))
    print('R597_THIRD_ORDER_SHIFT',mp.nstr(nu,38))
    print('R597_PAIR_ENERGY_K_MINUS_8',mp.nstr(e8,35))
    for k in (128,256,512,1024):
        coeff=[cf[j] * (mp.mpf(ratio(k,j).numerator)/ratio(k,j).denominator) for j in range(J+1)]
        def fk(x): return mp.polyval(list(reversed(coeff)),x)
        zk=mp.findroot(fk,(z+ell/k+m/k**2+nu/k**3,z+ell/k+m/k**2+nu/k**3+mp.mpf('0.00001')),tol=mp.mpf('1e-58'))
        print('R597_NUMERIC_CUBIC_SHIFT',k,mp.nstr(k**3*(zk-z-ell/k-m/k**2),22), 'k4error',mp.nstr(k**4*abs(zk-z-ell/k-m/k**2-nu/k**3),18))
    print('R597_CUBIC_COEFFICIENT_AND_ROOT_DIAGNOSTIC_PASS')
