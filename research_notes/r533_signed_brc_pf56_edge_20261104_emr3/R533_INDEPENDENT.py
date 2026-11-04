"""Independent exact check of R533 (Python/SymPy v1.14+).
Run with R533_EVIDENCE.json next to this file; no floating arithmetic.
"""
from __future__ import annotations
import json, math
from functools import lru_cache
from pathlib import Path
from sympy import Matrix

M = 56
BIN = lambda a,b: math.comb(a,b) if a>=0 and 0<=b<=a else 0
CAT = lambda k: BIN(2*k,k)//(k+1)

@lru_cache(maxsize=None)
def H(k,t):
    r = 2*k+1
    if not 2<=t<=r: return 0
    s = sum(BIN(r-t,q)*(BIN(2*t,r-2*q)-BIN(2*t,r-2*q-1)) for q in range(r-t+1))
    return BIN(r+t,2*t)*s

@lru_cache(maxsize=None)
def B(k,t):
    r=2*k+1
    if not 2<=t<=r: return 0
    qmax=min((t-1)//2,k)
    s=sum(BIN(t-1,2*q)*4**q*CAT(k-q) for q in range(qmax+1))
    return BIN(r+t,2*t)*s

def coeff(k):
    p=B(k,2); a=[B(k,t) for t in range(3,M+3)]; f=[1]
    for n in range(1,M+1):
        f.append(sum((-1)**(j-1)*a[j-1]*p**(j-1)*f[n-j] for j in range(1,n+1)))
    return f[-1]

def sgn(v): return '+' if v>0 else '-' if v<0 else '0'

def check():
    p=Path(__file__).with_name('R533_EVIDENCE.json')
    C=json.loads(p.read_text())
    assert C['order']==M and C['identity_checks']==337
    d=list(map(int,C['delta_at_k1'])); assert len(d)==112
    L=int(C['L'])
    def S(k):return sum(x*BIN(k-1,j) for j,x in enumerate(d))
    def G(k):return (k*(k+1)*(2*k+1)*(2*k+3))**M*(k+2)
    chosen=(1,4,5,6,8,9,10,11,37,38,39,40)
    verified=[]
    for k in chosen:
        raw=Matrix([[H(k,3+i-j) for j in range(M)] for i in range(M)]).berkowitz_det()
        rec=coeff(k)
        assert raw==rec, f'raw determinant mismatch k={k}'
        assert L*rec==CAT(k)**M*G(k)*S(k), f'certificate mismatch k={k}'
        verified.append({'k':k,'sign':sgn(raw),'digits':len(str(abs(int(raw))))})
    original=0
    for k in (1,5,9,10,38,39,40):
        for t in range(2,59):
            assert H(k,t)==B(k,t),(k,t)
            original+=1
    shift=C['tail_shift_origin_k']; es=[]
    for j in range(112):
        v=sum((-1)**(j-a)*BIN(j,a)*S(shift+a) for a in range(j+1))
        assert str(v)==C['tail_newton'][j]
        es.append(sgn(v))
    assert len(es)==112 and set(es)=={'-'}
    assert [sgn(S(k)) for k in range(1,shift)]==['+']*5+['-']*4+['+']*(shift-10)
    return {'status':'R533_INDEPENDENT_PASS','method':'Python math.comb + SymPy Matrix.berkowitz_det; exact integer arithmetic', 'boundary_checks':verified,'raw_determinants':len(verified),'H_B_crosschecks':original,'tail_newton_coefficients':len(es),'tail_shift':shift, 'sign_blocks':C['sign_blocks']}

if __name__=='__main__':print(json.dumps(check(),ensure_ascii=False,indent=2))
