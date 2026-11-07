"""R504 independent finite verification: exact ballot/Catalan integer SymPy Toeplitz determinants."""
import json
from math import comb
from sympy import Matrix

def cat(k): return comb(2*k,k)//(k+1)
def H2(k,t):
    r=2*k+1
    if t<2 or t>r: return 0
    return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*cat(k-q) for q in range(min((t-1)//2,k)+1))
def direct(k,m): return int(Matrix(m,m,lambda i,j:H2(k,3+i-j)).det(method="domain-ge"))
expected={1:1,5:1,6:-1,7:-1,10:-1,20:-1,25:-1,26:1,27:1,40:1}
checks={}
for k,s in expected.items():
    d=direct(k,27);sign=(d>0)-(d<0)
    assert sign==s,(k,sign,s)
    checks[str(k)]={"sign":"+" if sign>0 else "-" if sign<0 else "0","abs_digits":len(str(abs(d)))}
print(json.dumps({"status":"R504_INDEPENDENT_PASS","checks":checks,"arithmetic":"integer / SymPy exact domain determinant","scope":"ten independently evaluated finite k values"},ensure_ascii=False))
