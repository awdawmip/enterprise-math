"""R503: independent Catalan/ballot 26x26 matrix, exact SymPy."""
from math import comb
from sympy import Matrix
def cat(k): return comb(2*k,k)//(k+1)
def H(k,t):
    r=2*k+1
    if t<2 or t>r: return 0
    return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*cat(k-q) for q in range(min((t-1)//2,k)+1))
for k in (1,5,6,7,8,10):
    mat=Matrix([[H(k,3+i-j) for j in range(26)] for i in range(26)])
    d=mat.det(method="domain-ge")
    got=1 if d>0 else -1 if d<0 else 0
    assert got==(1 if k<=6 else -1), (k,got)
    print("k=",k,"sign=",got)
print("R503_INDEPENDENT_PASS")
