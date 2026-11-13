"""R508 independent original 31x31 Toeplitz determinants using SymPy Berkowitz.
Run: python R508_INDEPENDENT.py > R508_INDEPENDENT_EVIDENCE.json.
"""
from math import comb
from sympy import Matrix
import json

def choose(n,j):
    return comb(n,j) if n>=0 and 0<=j<=n else 0

def H(k,t):
    r=2*k+1
    if t<2 or t>r: return 0
    a=sum(choose(r-t,q)*(choose(2*t,r-2*q)-choose(2*t,r-2*q-1)) for q in range(r-t+1))
    return choose(r+t,2*t)*a

rows=[]
for k in (1,5,6,7,10,13,14,15,16,20):
    M=Matrix([[H(k,3+i-j) for j in range(31)] for i in range(31)])
    d=M.det(method="berkowitz")
    rows.append({"k":k,"sign":"+" if d>0 else "-" if d<0 else "0","decimal_digits":len(str(abs(d)))})
assert [x["sign"] for x in rows] == ["+"]*7 + ["-"]*3
print(json.dumps({"status":"R508_INDEPENDENT_PASS","method":"SymPy Matrix.det(method=berkowitz) on exact original H matrix; no Hessenberg recurrence","rows":rows},indent=2))
