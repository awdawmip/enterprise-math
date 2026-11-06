"""R587: independent exact reciprocal Newton coefficients and mesoscopic moments.
All assertions use arbitrary-precision integers/Fraction; numerical ratios are
non-certifying displays and do not prove the asymptotic theorem.
"""
from fractions import Fraction as F
from math import comb


def catalan(n):
    return comb(2*n, n)//(n+1)


def H(k, s):
    return comb(2*k+1+s, 2*s)*sum(
        comb(s-1, 2*q)*4**q*catalan(k-q)
        for q in range(min(k, (s-1)//2)+1)
    )


def inverse_power_sums(k, M):
    d = 2*k-1
    a = [F(H(k, j+2), H(k, 2)) for j in range(d+1)]
    e = [F(1)] + [a[d-j]/a[d] for j in range(1, d+1)]
    p = [F(d)]
    for m in range(1, M+1):
        v = sum((-1)**(j-1)*e[j]*p[m-j]
                for j in range(1, min(d, m-1)+1))
        if m <= d:
            v += (-1)**(m-1)*m*e[m]
        p.append(v)
    assert p[1] == d
    assert p[2] == F(12*k*k-20*k+1, 4*k+1)
    return p


def correction(m):
    # Independent R583 finite-sum representation of b_m.
    return (F(comb(2*m-1, m-1), 2**m)
        + F(1, 2)*sum(F(comb(m+j-1, j), 2**j) for j in range(m))
        - 3*2**(m-1)*sum(F(comb(m+j-1, j), 4**j) for j in range(m)))


def moment(m):
    return F(comb(2*m, m), 2**m)

records=[]
for k in (3, 5, 8, 12, 20, 32, 48, 64):
    M=min(16, 2*k+4)
    p=inverse_power_sums(k,M)
    for m in range(1,M+1):
        delta=p[m]-F(2*k+1)*moment(m)-correction(m)
        records.append((k,m,delta))
    if k >= 12:
        print('RECIPROCAL_SAMPLE',k,
              'm2_correction', float(p[2]-(2*k+1)*moment(2)),
              'm4_rem_n', float((p[4]-(2*k+1)*moment(4)-correction(4))*(2*k+1)),
              'm8_rem_n', float((p[8]-(2*k+1)*moment(8)-correction(8))*(2*k+1)))

# Check first-order reciprocal asymptotic for fixed m numerically, exact inputs.
for m in (1,2,3,4,6,8,12):
    xs=[(k,float(delta*(2*k+1))) for k,j,delta in records if j==m]
    print('N_TIMES_REMAINDER',m,xs[-3:])
print('EXACT_NEWTON_MOMENT_RECORDS',len(records))
print('R587_RECIPROCAL_CROSSCHECK_PASS')

# R586 finite Bernstein-sum collapse used in the new W1 certificate.
a=F(3,7)
for N in range(1,25):
    nested=sum(F(comb(N,l),2**0)*2**l*sum(
        F(comb(l,m)*m,2**l)*a**m for m in range(1,l+1))
        for l in range(1,N+1))
    expected=a*N*(2+a)**(N-1)
    assert nested==expected,(N,nested,expected)
    second=sum(comb(N,l)*2**l*l*(l-1) for l in range(2,N+1))
    assert second==4*N*(N-1)*3**(N-2),(N,second)
print('R587_BERNSTEIN_BINOMIAL_SUMS_EXACT_24_PASS')
