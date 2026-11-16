"""R528 independent exact cross-check using original signed coefficient and SymPy Berkowitz."""
from functools import lru_cache
from math import comb
from sympy import Matrix
import json
M=51
SAMPLES=[1,2,3,4,5,6,7,8,9,14,15,16,17,18,23,24,25,26]
@lru_cache(None)
def choose(n,k):
    return comb(n,k) if n>=0 and 0<=k<=n else 0
@lru_cache(None)
def raw(k,t):
    r=2*k+1
    if not 2<=t<=r: return 0
    return choose(r+t,2*t)*sum(choose(r-t,q)*(choose(2*t,r-2*q)-choose(2*t,r-2*q-1)) for q in range(r-t+1))
@lru_cache(None)
def ballot(k,t):
    r=2*k+1
    if not 2<=t<=r: return 0
    catalan=[1]
    for n in range(1,k+1): catalan.append(sum(catalan[j]*catalan[n-1-j] for j in range(n)))
    return choose(r+t,2*t)*sum(choose(t-1,2*q)*4**q*catalan[k-q] for q in range(min((t-1)//2,k)+1))
def recurrence(k):
    p=ballot(k,2);d=[1]
    a=[ballot(k,j+3) for j in range(M)]
    for n in range(1,M+1):
        d.append(sum((-1)**(h-1)*a[h-1]*p**(h-1)*d[n-h] for h in range(1,n+1)))
    return d[-1]
out={"status":"R528_INDEPENDENT_PASS","method":"raw signed convolution H, SymPy Berkowitz 51x51 determinant, separate Catalan recurrence","sample_ks":SAMPLES,"signs":{},"raw_ballot_checks":0,"direct_determinants":0}
for k in SAMPLES:
    for t in range(2,M+2):
        assert raw(k,t)==ballot(k,t),(k,t)
        out["raw_ballot_checks"]+=1
    d=Matrix([[raw(k,3+i-j) for j in range(M)] for i in range(M)]).berkowitz_det()
    assert int(d)==recurrence(k),("determinant",k)
    sign="+" if d>0 else "-" if d<0 else "0"
    expected="+" if k<=4 or 7<=k<=15 else "-"
    assert sign==expected,("sign",k,sign)
    out["signs"][str(k)]=sign
    out["direct_determinants"]+=1
print(json.dumps(out,ensure_ascii=False,separators=(",",":")))
