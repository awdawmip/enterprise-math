"""R596 author-side independent exact Catalan/second-order check plus numeric root diagnostics."""
from fractions import Fraction as Q
from math import comb, factorial

def catalan(n):
    return comb(2*n,n)//(n+1)

def raw_H(k,s):
    return comb(2*k+1+s,2*s)*sum(comb(s-1,2*q)*4**q*catalan(k-q) for q in range(min(k,(s-1)//2)+1))

def ratio(k,j):
    if j==0: return Q(1)
    product=Q(1)
    for h in range(1,j+1):
        product *= (1+Q(h+3,2*k))*(1-Q(h,2*k))
    weighted=Q(0);cq=Q(1)
    for q in range((j+1)//2+1):
        if q: cq *= 1+Q(3,2*(k-q+1)-1)
        weighted += comb(j+1,2*q)*cq
    return product*weighted/2**j

def alpha(j):
    return Q(0) if j==0 else Q(15*j+3,8)

def beta_poly(j):
    return Q(-32*j**3+501*j*j-349*j-18,384)

def beta(j):
    return beta_poly(j)+(Q(3,64) if j==0 else Q(15,64) if j==1 else Q(0))

for j in range(101):
    n=j+1
    moments=[sum(Q(comb(n,2*q)*q**e,2**j) for q in range(n//2+1)) for e in (0,1,2)]
    assert moments[0]==1
    assert moments[1]==(Q(n,4) if j>=1 else 0)
    assert moments[2]==(Q(n*(n+1),16) if j>=2 else Q(1,2) if j==1 else 0)
    p2=sum(Q(-h*(h+3),4) for h in range(1,j+1))+Q(9,4)*comb(j,2)
    p1=Q(3*j,2)
    w1=Q(3,2)*moments[1]
    w2=(15*moments[2]-9*moments[1])/8
    assert p2+p1*w1+w2==beta(j)
print('R596_EXACT_TWO_MOMENTS_AND_SECOND_COEFFICIENT_PASS',101)
num=0
for k in range(2,19):
    h2=raw_H(k,2)
    for j in range(2*k):
        original=Q(raw_H(k,j+2),h2)*Q(factorial(2*j+4),24*8**j*k**(2*j))
        assert original==ratio(k,j)
        num+=1
print('R596_CATALAN_SOURCE_INDEPENDENT_RECONSTRUCTION_PASS',num)
for k in (64,256,1024,4096):
    vals=[k**3*(ratio(k,j)-1-alpha(j)/k-beta(j)/k**2) for j in range(1,11)]
    print('R596_EXACT_CUBIC_RESIDUAL k',k,'j=1..10',
          'first=',format(float(vals[0]),'.9f'),'last=',format(float(vals[-1]),'.9f'))

try:
    import mpmath as mp
except ImportError:
    print('R596_NUMERIC_ROOT_DIAGNOSTIC_NOT_RUN_NO_MPMATH')
else:
    mp.mp.dps=65
    J=54
    a=[mp.mpf(24)*8**j/mp.factorial(2*j+4) for j in range(J+1)]
    def evaluate(z,k=None):
        f=fp=fpp=g=gp=h=mp.mpc(0)
        power=mp.mpc(1)
        for j in range(J+1):
            c=(-1)**j*a[j]
            B=mp.mpf(1)
            if k is not None and j<=2*k-1:
                r=ratio(k,j); B=mp.mpf(r.numerator)/r.denominator
            elif k is not None: B=mp.mpf(0)
            f+=c*B*power
            if j: fp+=j*c*B*power/z
            if j>=2: fpp+=j*(j-1)*c*B*power/(z*z)
            if k is None:
                g+=c*mp.mpf(alpha(j).numerator)/alpha(j).denominator*power
                gp+=j*c*mp.mpf(alpha(j).numerator)/alpha(j).denominator*power/z if j else 0
                h+=c*mp.mpf(beta(j).numerator)/beta(j).denominator*power
            power*=z
        return f,fp,fpp,g,gp,h
    z0=mp.findroot(lambda z:evaluate(z)[0],
                   (mp.mpc('6.3','9.4'),mp.mpc('6.4','9.5')),tol=mp.mpf('1e-57'))
    f,fp,fpp,g,gp,h=evaluate(z0)
    L=-g/fp
    M=-(fpp*L**2/2+gp*L+h)/fp
    b=mp.im(z0); li=mp.im(L); mi=mp.im(M)
    A5=b**2; A6=b**2/2+2*b*li; A7=b**2/4+b*li+li**2+2*b*mi
    print('R596_LIMIT_ROOT_65DIG',mp.nstr(z0,50))
    print('R596_FIRST_SHIFT',mp.nstr(L,40))
    print('R596_SECOND_SHIFT',mp.nstr(M,40))
    print('R596_PAIR_V_COEFFS',*[mp.nstr(x,25) for x in (A5,A6,A7)])
    for k in (128,256,512,1024,4096):
        zk=mp.findroot(lambda z:evaluate(z,k)[0],
                       (z0+L/k+M/k**2,z0+L/k+M/k**2+mp.mpf('0.0001')),
                       tol=mp.mpf('1e-57'),maxsteps=40)
        err=abs(zk-z0-L/k-M/k**2)
        print('R596_NUMERIC_SECOND_DRIFT','k',k,
              'k2diff=',mp.nstr(k**2*(zk-z0-L/k),18),
              'k3_error_abs=',mp.nstr(k**3*err,14),
              'F_k_root_residual=',mp.nstr(abs(evaluate(zk,k)[0]),8))
    assert abs(f)<mp.mpf('1e-54')
    assert abs(fp)>mp.mpf('1e-2')
    print('R596_EXACT_AND_NUMERIC_SECOND_ORDER_DRIFT_PASS')
