from math import comb
from functools import lru_cache
from sympy import Matrix

@lru_cache(None)
def catalan(k):
    return comb(2*k,k)//(k+1)
def ballot_h(k,t):
    r=2*k+1
    if t<2 or t>r:
        return 0
    qmax=min((t-1)//2,k)
    return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*catalan(k-q) for q in range(qmax+1))
for k in (1,9,10,15):
    M=Matrix(25,25,lambda i,j:ballot_h(k,3+i-j))
    v=M.det(method="domain-ge")
    sign=(1 if v>0 else -1 if v<0 else 0)
    expected=1 if k<10 else -1
    assert sign==expected,(k,sign)
    print(k,sign)
print("R502_INDEPENDENT_PASS")
