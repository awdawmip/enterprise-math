"""R519: independent exact 42x42 determinant and signed-BRC/ballot checks.
External scope: frozen R462 auxiliary signed scalar model, not native-X6 dynamics.
Requires Python 3 with SymPy; all determinant arithmetic over ZZ, method Berkowitz.
"""
from math import comb
from sympy import Matrix
import json
R = 42

def b(n,j):
    return comb(n,j) if 0 <= j <= n else 0

def catalan(k):
    return b(2*k,k)//(k+1)

def direct_coefficient(k,t):
    r=2*k+1
    if not 2<=t<=r: return 0
    coeff=sum(b(r-t,q)*(b(2*t,r-2*q)-b(2*t,r-2*q-1)) for q in range(r-t+1))
    return b(r+t,2*t)*coeff

def ballot(k,t):
    r=2*k+1
    if not 2<=t<=r: return 0
    return b(r+t,2*t)*sum(b(t-1,2*j)*4**j*catalan(k-j)
                            for j in range(min((t-1)//2,k)+1))

def recurrence(k,n=R):
    h=[ballot(k,t) for t in range(2,n+3)]
    p=h[0]
    f=[1]
    for m in range(1,n+1):
        f.append(sum((-1)**(a-1)*h[a]*p**(a-1)*f[m-a] for a in range(1,m+1)))
    return f[-1]

ks=[1,2,3,4,5,6,7,8,9,10,11,12,14,15,28,29]
results=[]
for k in ks:
    matrix=Matrix(R,R,lambda i,j:direct_coefficient(k,3+i-j))
    det=int(matrix.det(method='berkowitz'))
    assert det==recurrence(k), (k,'det_recurrence_mismatch')
    results.append({'k':k,'sign':'+' if det>0 else '-' if det<0 else '0'})
count=0
for k in range(1,21):
    for t in range(2,R+2):
        assert direct_coefficient(k,t)==ballot(k,t),(k,t)
        count+=1
expected=lambda k:'+' if k<=5 or k>=11 else '-'
assert all(row['sign']==expected(row['k']) for row in results)
print(json.dumps({'status':'R519_INDEPENDENT_PASS',
                   'method':'independently constructed signed polynomial coefficients and SymPy Berkowitz 42x42 determinants; separate ballot recurrence',
                   'precision':'exact arbitrary-precision integer',
                   'matrix_checks':results,
                   'signed_coefficient_ballot_crosschecks':count,
                   'mathematical_review':'author-side cross-implementation, not Driver independent admission'},indent=2))
