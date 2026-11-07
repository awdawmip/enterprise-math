"""R513 independent exact ballot/Catalan raw-matrix checks, Python >=3.11, SymPy."""
from math import comb
from sympy import Matrix
from json import dump
from pathlib import Path
import sys
sys.set_int_max_str_digits(0)
R=36
def catalan(k):
    return 0 if k<0 else comb(2*k,k)//(k+1)
def h_ballot(k,t):
    r=2*k+1
    if not (2<=t<=r): return 0
    return comb(r+t,2*t)*sum(comb(t-1,2*q)*(4**q)*catalan(k-q) for q in range(min((t-1)//2,k)+1))
def d_ballot_recurrence(k):
    p=h_ballot(k,2)
    D=[1]
    for m in range(1,R+1):
        s=0
        pp=1
        for e in range(1,m+1):
            s+=(1 if e%2 else -1)*h_ballot(k,e+2)*pp*D[m-e]
            pp*=p
        D.append(s)
    return D[-1]
points=[1,5,6,8,9,12,18,207,208]
expected={1:'+',5:'+',6:'-',8:'-',9:'+',12:'+',18:'+',207:'+',208:'-'}
records=[]
for k in points:
    d=d_ballot_recurrence(k)
    if k<=18:
        A=Matrix([[h_ballot(k,3+i-j) for j in range(R)] for i in range(R)])
        assert A.det(method='berkowitz')==d, k
    sign='+' if d>0 else '-' if d<0 else '0'
    assert sign==expected[k], (k, sign)
    records.append({'k':k,'sign':sign,'digit_count':len(str(abs(d))),'independent_matrix':k<=18})
result={'status':'R513_INDEPENDENT_PASS','matrix_method':'SymPy Berkowitz for k<=18','boundary_method':'independent ballot/Catalan Hessenberg recurrence at k=207,208','points':records,'exact_arithmetic':'Python integers/SymPy exact integers'}
with Path(__file__).with_name('R513_INDEPENDENT_EVIDENCE.json').open('w') as f: dump(result,f,indent=2)
print(result['status'],records)
