"""R516 independent 39th-order determinant checks using ballot–Catalan and SymPy Berkowitz."""
from math import comb
from sympy import Matrix
import json
M=39
POINTS=(1,2,5,6,7,8,9,10,11,12,22,23,39)
def b(n,r):return 0 if n<0 or r<0 or r>n else comb(n,r)
def C(k):return comb(2*k,k)//(k+1)
def H_ballot(k,t):
    r=2*k+1
    if t<2 or t>r:return 0
    return b(r+t,2*t)*sum(b(t-1,2*q)*4**q*C(k-q) for q in range(min((t-1)//2,k)+1))
def H_original(k,t):
    r=2*k+1
    if t<2 or t>r:return 0
    return b(r+t,2*t)*sum(b(r-t,q)*(b(2*t,r-2*q)-b(2*t,r-2*q-1)) for q in range(r-t+1))
def D(k):
    return int(Matrix([[H_ballot(k,3+i-j) for j in range(M)] for i in range(M)]).det(method='berkowitz'))
result=[]
for k in POINTS:
    d=D(k)
    result.append({'k':k,'r':2*k+1,'sign':'+' if d>0 else '-' if d<0 else '0','decimal_digits':len(str(abs(d)))})
comparisons=0
for k in range(1,21):
    for t in range(2,M+2):
        assert H_ballot(k,t)==H_original(k,t),(k,t)
        comparisons+=1
assert all(x['sign']==('+' if x['k']<=9 else '-') for x in result)
print(json.dumps({'status':'R516_INDEPENDENT_PASS','scientific_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f','method':'Python math.comb ballot-Catalan and 39x39 SymPy Berkowitz exact matrix determinant','points':result,'signed_original_vs_ballot_checks':comparisons,'floating_point':False},indent=2))
