"""R531 independently recomputed signed BRC Toeplitz 54th minors and Newton certificate."""
from functools import lru_cache
from math import comb
from pathlib import Path
from sympy import Matrix
import json
M=54
SAMPLES=list(range(1,13))+[14,16,17,18,19,20,23,31]
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
cert=json.loads(Path(__file__).with_name('R531_EVIDENCE.json').read_text())
assert cert['identity_checks']==325 and cert['order']==M
assert cert['tail_shift_origin_k']==18 and len(cert['tail_newton'])==108
assert all(int(x)>0 for x in cert['tail_newton'])
assert len(cert['delta_at_k1'])==108
values=[newton_eval(cert['delta_at_k1'],17+i) for i in range(108)]
recalc=[]
while values:
    recalc.append(values[0]);values=[values[j+1]-values[j] for j in range(len(values)-1)]
assert recalc==list(map(int,cert['tail_newton']))
assert all(newton_eval(cert['delta_at_k1'],k-1)>0 for k in range(1,8))
assert all(newton_eval(cert['delta_at_k1'],k-1)<0 for k in range(8,18))
assert list(map(int,cert['finite_values_before_tail']))==[newton_eval(cert['delta_at_k1'],k-1) for k in range(1,18)]
out={'status':'R531_INDEPENDENT_PASS','method':'raw signed convolution, separate Catalan recurrence, SymPy Berkowitz 54x54, independent certificate shift audit','sample_ks':SAMPLES,'direct_determinants':0,'raw_ballot_checks':0,'original_recurrence_checks':0,'interpolant_checks':0,'shifted_newton_coefficients_recomputed':len(recalc),'boundary_pairs':[[7,8],[17,18]]}
for k in SAMPLES:
    for t in range(2,M+2):
        assert raw(k,t)==ballot(k,t),(k,t)
        out['raw_ballot_checks']+=1
    d=Matrix([[raw(k,3+i-j) for j in range(M)] for i in range(M)]).berkowitz_det()
    ref=recurrence(k,ballot)
    assert int(d)==ref,('determinant',k)
    expected='-' if 8<=k<=17 else '+'
    assert sign(d)==expected,('sign',k,sign(d))
    out['direct_determinants']+=1
    assert int(d)*int(cert['L'])==cat(k)**M*(k*(k+1)*(2*k+1)*(2*k+3))**M*(k+2)*newton_eval(cert['delta_at_k1'],k-1)
    out['interpolant_checks']+=1
for k in [16,17,18,19,55]:
    assert recurrence(k,raw)==recurrence(k,ballot)
    out['original_recurrence_checks']+=1
    out['interpolant_checks']+=1
print(json.dumps(out,ensure_ascii=False,indent=2))
