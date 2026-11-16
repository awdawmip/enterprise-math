"""Independent rank-29 direct matrix check via original convolution; finite samples only."""
from math import comb
from sympy import Matrix

def H(k,t):
    r=2*k+1
    if t<2 or t>r: return 0
    def B(j):
        return sum(comb(2*t,j-2*q)*comb(r-t,q)
                   for q in range(r-t+1) if 0<=j-2*q<=2*t)
    return comb(r+t,2*t)*(B(r)-B(r-1))

for k,expected in [(1,1),(5,1),(6,-1),(7,-1),(8,-1),(9,1),(10,1),(15,1)]:
    matrix=Matrix([[H(k,3+i-j) for j in range(29)] for i in range(29)])
    det=int(matrix.det(method='domain-ge'))
    actual=(det>0)-(det<0)
    assert actual==expected,(k,actual,expected)
    print(f"k={k}: sign={actual}, digits={len(str(abs(det)))}")
print("R506_INDEPENDENT_PASS")
