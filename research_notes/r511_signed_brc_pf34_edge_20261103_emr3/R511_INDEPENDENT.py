"""Independent raw signed BRC Toeplitz determinant spot checks for R511.
Build matrix entries via ballot/Catalan expansion, no call to JS H or recurrence.
"""
from math import comb
from sympy import Matrix
from json import dump

def catalan(k):
    if k < 0: return 0
    return comb(2*k,k)//(k+1)

def h_ballot(k,t):
    r=2*k+1
    if not (2<=t<=r): return 0
    return comb(r+t,2*t)*sum(comb(t-1,2*q)*(4**q)*catalan(k-q) for q in range(min((t-1)//2,k)+1))

points=[1,4,5,6,7,9,10,14,16,17,18,19,25]
records=[]
for k in points:
    a=Matrix([[h_ballot(k,3+i-j) for j in range(34)] for i in range(34)])
    d=a.det(method='berkowitz')
    records.append({'k':k,'sign':'+' if d>0 else '-' if d<0 else '0', 'absolute_digits':len(str(abs(d)))})
assert [r['sign'] for r in records]==['+','+','+','-','-','-','-','-','-','-','+','+','+']
result={'status':'R511_INDEPENDENT_PASS','model':'ballot/Catalan coefficient expansion, 34x34 exact SymPy Berkowitz determinant','parameters':records,'arithmetic':'exact integers'}
with open('R511_INDEPENDENT_EVIDENCE.json','w') as f: dump(result,f,ensure_ascii=False,indent=2)
print(result['status'],records)
