"""R595 author-side reproducible verification for first-order auxiliary root drift.

Exact Fraction coefficients and independent Catalan source cross-check;
complex root diagnostics use IEEE-754 floats and are not a zero certificate.
"""
from fractions import Fraction as Q
from math import comb, factorial


def catalan(n):
    return comb(2*n, n) // (n+1)


def H(k, s):
    return comb(2*k+1+s, 2*s) * sum(
        comb(s-1, 2*q)*4**q*catalan(k-q)
        for q in range(min(k,(s-1)//2)+1)
    )


def ratio(k,j):
    P=Q(1)
    for h in range(1,j+1):
        P *= (1+Q(h+3,2*k))*(1-Q(h,2*k))
    W=Q(0); Rq=Q(1)
    for q in range((j+1)//2+1):
        if q:
            Rq *= 1+Q(3,2*(k-q+1)-1)
        W += comb(j+1,2*q)*Rq
    return P * W / 2**j


def alpha(j):
    return Q(0) if j==0 else Q(15*j+3,8)


# First-order coefficient is an exact identity of finite binomial sums.
for j in range(0,101):
    n=j+1
    S=sum(Q(comb(n,2*q),2**j) for q in range((j+1)//2+1))
    moment=sum(Q(q*comb(n,2*q),2**j) for q in range((j+1)//2+1))
    assert S==1
    assert Q(3*j,2)+Q(3*moment,2)==alpha(j)
print('R595_EXACT_FIRST_ORDER_BINOMIAL_MOMENTS_PASS',101,'degrees')

# Compare with the independent original H_k construction.
count=0
for k in range(2,19):
    H2=H(k,2)
    for j in range(2*k):
        ar=Q(H(k,j+2),H2)
        rr=ar*Q(factorial(2*j+4),24*8**j*k**(2*j))
        assert rr == ratio(k,j)
        count+=1
print('R595_INDEPENDENT_CATALAN_COEFFICIENT_PASS',count,'pairs')

# The actual fixed-degree correction k*(r-1) -> alpha_j.
# Report the rescaled second-order remainder over small finite domains.
for k in (64,256,1024,4096):
    rems=[]
    for j in range(1,11):
        r=ratio(k,j)
        rem=k*k*(r-1-alpha(j)/k)
        rems.append(float(rem))
    print('R595_FINITE_SECOND_ORDER_DIAGNOSTIC', 'k=',k,
          'min=',round(min(rems),8), 'max=',round(max(rems),8))


def a(j):
    return 24.0*8.0**j/factorial(2*j+4)


def eval_fd(z,k=None,J=32):
    # Simultaneously evaluate F (or F_k) and its derivative via Horner.
    f=0j; fp=0j
    for j in range(J,-1,-1):
        coeff=(-1)**j*a(j)*(float(ratio(k,j)) if k is not None else 1)
        fp=fp*z+f
        f=f*z+coeff
    return f,fp


def newton(k=None):
    z=6.339+9.481j
    for _ in range(25):
        f,fp=eval_fd(z,k)
        dz=f/fp
        z-=dz
        if abs(dz)<2e-12:
            break
    assert abs(eval_fd(z,k)[0])<2e-12
    return z

z0=newton()
Fz, Fp=eval_fd(z0)
G=15*z0*Fp/8+3*(Fz-1)/8
L=-G/Fp
assert abs(Fz)<2e-12
print('R595_NUMERIC_LIMIT_ROOT',format(z0.real,'.12f'),format(z0.imag,'.12f'))
print('R595_NUMERIC_PREDICTED_K_SHIFT',format(L.real,'.10f'),format(L.imag,'.10f'))
for k in (128,256,512,1024,4096):
    zk=newton(k)
    scaled=k*(zk-z0)
    print('R595_NUMERIC_ROOT_DRIFT',k,
          format(zk.real,'.12f'),format(zk.imag,'.12f'),
          format(scaled.real,'.8f'),format(scaled.imag,'.8f'),
          'residual_to_L=',round(abs(scaled-L),9))
print('R595_EXACT_COEFFICIENT_AND_NUMERIC_DRIFT_CHECK_PASS')
