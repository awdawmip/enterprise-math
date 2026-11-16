"""R520 independent signed-BRC integer determinant / ballot-Catalan check.
Frozen scientific input: R462; auxiliary scalar model, s=3, m=43.
Author-side implementation using exact SymPy Berkowitz, separate from JS Bareiss.
"""
from math import comb
from sympy import Matrix
import json

R=43

def b(n,j):
    return comb(n,j) if 0 <= j <= n else 0

def cat(k):
    return b(2*k,k)//(k+1)

def raw(k,t):
    r=2*k+1
    if not 2 <= t <= r: return 0
    return b(r+t,2*t)*sum(b(r-t,q)*(b(2*t,r-2*q)-b(2*t,r-2*q-1)) for q in range(r-t+1))

def ballot(k,t):
    r=2*k+1
    if not 2 <= t <= r: return 0
    return b(r+t,2*t)*sum(b(t-1,2*q)*4**q*cat(k-q) for q in range(min((t-1)//2,k)+1))

def recurrence(k,m=R):
    h=[ballot(k,t) for t in range(2,m+3)]
    f=[1]
    for n in range(1,m+1):
        f.append(sum((-1)**(a-1)*h[a]*h[0]**(a-1)*f[n-a] for a in range(1,n+1)))
    return f[-1]

ks=[1,2,3,4,5,6,7,8,9,10,11,12,14,15,37,38,39,40]
results=[]
for k in ks:
    mat=Matrix(R,R,lambda i,j:raw(k,3+i-j))
    det=int(mat.det(method='berkowitz'))
    assert det == recurrence(k), (k,'det_recurrence_mismatch')
    results.append({'k':k,'sign':'+' if det>0 else '-' if det<0 else '0'})
checks=0
for k in range(1,21):
    for t in range(2,R+2):
        assert raw(k,t)==ballot(k,t),(k,t)
        checks+=1
expected=lambda k: '+' if k<=4 or 9<=k<=38 else '-'
assert all(x['sign']==expected(x['k']) for x in results)
print(json.dumps({'status':'R520_INDEPENDENT_PASS','date':'2026-11-04',
    'scientific_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f',
    'method':'direct original signed polynomial coefficients; SymPy Berkowitz 43x43 determinant and independent ballot recurrence',
    'arithmetic':'exact integer', 'matrix_checks':results,
    'coefficient_crosschecks':checks,'review':'author-side independent algorithm, not native Driver review'},indent=2))
