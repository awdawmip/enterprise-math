"""R529 independent exact Python/SymPy cross-check of signed BRC Toeplitz m=52."""
from functools import lru_cache
from math import comb
from pathlib import Path
from sympy import Matrix
import json
M=52
SAMPLES=list(range(1,17))+[20,26]
HIGH_SAMPLES=[305,306,307,308]
@lru_cache(None)
def choose(n,k):
    return comb(n,k) if n>=0 and 0<=k<=n else 0
@lru_cache(None)
def cat(k):
    if k==0: return 1
    return sum(cat(j)*cat(k-1-j) for j in range(k))
@lru_cache(None)
def raw(k,t):
    r=2*k+1
    if not 2<=t<=r: return 0
    return choose(r+t,2*t)*sum(choose(r-t,q)*(choose(2*t,r-2*q)-choose(2*t,r-2*q-1)) for q in range(r-t+1))
@lru_cache(None)
def ballot(k,t):
    r=2*k+1
    if not 2<=t<=r: return 0
    return choose(r+t,2*t)*sum(choose(t-1,2*q)*4**q*cat(k-q) for q in range(min((t-1)//2,k)+1))
def recurrence(k,coef):
    p=coef(k,2);d=[1]
    a=[coef(k,j+3) for j in range(M)]
    for n in range(1,M+1):
        d.append(sum((-1)**(h-1)*a[h-1]*p**(h-1)*d[n-h] for h in range(1,n+1)))
    return d[-1]
def newton_eval(delta,shift):
    return sum(int(d)*choose(shift,j) for j,d in enumerate(delta))
def sign(x):return '+' if x>0 else '-' if x<0 else '0'
cert=json.loads(Path(__file__).with_name('R529_EVIDENCE.json').read_text())
assert cert['identity_checks']==313 and cert['order']==M
assert cert['tail_shift_origin_k']==307 and len(cert['tail_newton'])==104
assert all(int(x)>0 for x in cert['tail_newton'])
assert len(cert['delta_at_k1'])==104
out={'status':'R529_INDEPENDENT_PASS','method':'raw signed convolution; independently computed Catalan recurrence; SymPy Berkowitz 52x52; high-k original-sign recurrence; Newton certificate audit','sample_ks':SAMPLES,'high_k_samples':HIGH_SAMPLES,'direct_determinants':0,'raw_ballot_checks':0,'original_recurrence_checks':0,'high_k_signs':{},'tail_newton_signs_audited':104,'interpolant_checks':0}
for k in SAMPLES:
    for t in range(2,M+2):
        assert raw(k,t)==ballot(k,t),(k,t)
        out['raw_ballot_checks']+=1
    d=Matrix([[raw(k,3+i-j) for j in range(M)] for i in range(M)]).berkowitz_det()
    assert int(d)==recurrence(k,ballot),('determinant',k)
    expected='+' if k<=11 else '-'
    assert sign(d)==expected,('sign',k,sign(d))
    out['direct_determinants']+=1
    assert int(d)*int(cert['L'])==cat(k)**M*(k*(k+1)*(2*k+1)*(2*k+3))**M*(k+2)*newton_eval(cert['delta_at_k1'],k-1)
    out['interpolant_checks']+=1
for k in HIGH_SAMPLES:
    for t in range(2,M+2):
        assert raw(k,t)==ballot(k,t),(k,t)
        out['raw_ballot_checks']+=1
    a=recurrence(k,raw)
    b=recurrence(k,ballot)
    assert a==b,('high k recurrence mismatch',k)
    expected='-' if k<=306 else '+'
    assert sign(a)==expected,('high sign',k,sign(a))
    assert a*int(cert['L'])==cat(k)**M*(k*(k+1)*(2*k+1)*(2*k+3))**M*(k+2)*newton_eval(cert['delta_at_k1'],k-1)
    out['original_recurrence_checks']+=1
    out['interpolant_checks']+=1
    out['high_k_signs'][str(k)]=expected
print(json.dumps(out,ensure_ascii=False,indent=2))
