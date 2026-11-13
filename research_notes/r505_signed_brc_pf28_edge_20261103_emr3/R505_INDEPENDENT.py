"""Independent SymPy matrix determinant check using ballot-Catalan H2; signed BRC auxiliary scalar."""
from math import comb
import sympy as sp
R=28

def C(k): return comb(2*k,k)//(k+1)
def b(n,k): return comb(n,k) if 0<=k<=n else 0

def h2(k,t):
    r=2*k+1
    if t<2 or t>r:return 0
    return b(r+t,2*t)*sum(b(t-1,2*q)*(4**q)*C(k-q) for q in range(min((t-1)//2,k)+1))

results={}
for k in (1,5,6,7,12,13,14,20):
    m=sp.Matrix([[h2(k,3+i-j) for j in range(R)] for i in range(R)])
    v=int(m.det(method='domain-ge'))
    results[k]=('+' if v>0 else '-' if v<0 else '0',len(str(abs(v))))
    assert (v>0) == (k<=5 or k>=13)
print('R505_INDEPENDENT_PASS',results)
