"""Independent spot checks of original signed-BRC Toeplitz D_32 (SymPy/Berkowitz)."""
import json
from math import comb
from sympy import Matrix, Integer
def cb(n,j):
    return comb(n,j) if 0<=j<=n else 0
def raw_h(k,t):
    r=2*k+1
    if t<2 or t>r:return 0
    coefficient=sum(cb(r-t,q)*(cb(2*t,r-2*q)-cb(2*t,r-2*q-1)) for q in range(r-t+1))
    return cb(r+t,2*t)*coefficient
def raw_det(k,m=32):
    mat=Matrix(m,m,lambda i,j: Integer(raw_h(k,3+i-j)))
    return int(mat.det(method="berkowitz"))
ks=[1,5,6,7,9,10,11,15,20]
signs={}
for k in ks:
    d=raw_det(k); signs[str(k)]="+" if d>0 else "-" if d<0 else "0"
    assert signs[str(k)]==("+" if k<=9 else "-"), (k,signs[str(k)])
print(json.dumps({"status":"R509_INDEPENDENT_PASS","method":"SymPy Berkowitz raw matrix determinant, exact signed-BRC coefficient extraction","m":32,"k_signs":signs,"scientific_pin":"18783e01e3646c72b7aab3b16d3f565e83e6446f"},indent=2))
