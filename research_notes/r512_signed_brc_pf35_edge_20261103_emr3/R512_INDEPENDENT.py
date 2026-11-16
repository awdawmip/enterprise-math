"""Independent raw signed BRC Toeplitz determinant spot checks for R512.
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

points=[1,4,5,6,7,10,11,12,13,18]
records=[]
for k in points:
    a=Matrix([[h_ballot(k,3+i-j) for j in range(35)] for i in range(35)])
    d=a.det(method='berkowitz')
    records.append({'k':k,'sign':'+' if d>0 else '-' if d<0 else '0', 'absolute_digits':len(str(abs(d)))})
assert [r['sign'] for r in records]==['+','+','+','-','-','-','-','+','+','+']
result={'status':'R512_INDEPENDENT_PASS','model':'ballot/Catalan coefficient expansion, 35x35 exact SymPy Berkowitz determinant','parameters':records,'arithmetic':'exact integers'}
with open('R512_INDEPENDENT_EVIDENCE.json','w') as f: dump(result,f,ensure_ascii=False,indent=2)
print(result['status'],records)
