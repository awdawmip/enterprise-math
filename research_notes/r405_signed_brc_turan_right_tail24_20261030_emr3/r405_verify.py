#!/usr/bin/env python3
"""R405 exact finite-family Turan certificate for the signed BRC auxiliary model.

Pure Python 3 standard library; integer polynomial arithmetic only.
The proof verifies that N_k(k+3+x) has strictly positive integer
coefficients for 1 <= k <= 24, ensuring strict Turan positivity
for all integers r >= k+3 in these 24 unbounded bands.

This verifies a finite *collection of polynomial identities* valid
for every r, not merely sample values of r.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

# Polynomials stored as ascending integer coefficients.
def trim(v):
    while len(v)>1 and v[-1]==0: v.pop()
    return v

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return trim(c)

def scale(a,c):
    return trim([c*x for x in a])

def sub(a,b):
    return add(a,scale(b,-1))

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)

def falling_linear(mult, start, degree):
    """(mult*r-start)_(degree) = prod_{i=0}^{degree-1}(mult*r-start-i)."""
    out=[1]
    for i in range(degree): out=mul(out,[-start-i,mult])
    return out

def compose_shift(a, c):
    """Return exact polynomial a(x+c) by Horner; variable is x."""
    res=[0]
    for v in reversed(a): res=add(mul(res,[c,1]),[v])
    return res

def eval_poly(a, x):
    val=0
    for v in reversed(a): val=val*x+v
    return val

def catalan(r):
    return math.comb(2*r,r)//(r+1)

def delta_direct(r,k):
    # s=r-k; 0 <= k < r
    n=2*r-2*k
    def choose(n,m): return math.comb(n,m) if 0<=m<=n else 0
    return sum(math.comb(k,j)*(choose(n,r-2*j)-choose(n,r-2*j-1)) for j in range(k+1))

def Q(k):
    """Polynomial Q_k(r) using only integer polynomial operations.

    (r+1) sum_{j=0}^{k-1} binom(k,j)(4j-2k+1)
      (r)_(2j) (r)_(2k-2j-1) + (2k+1)(r)_(2k).
    """
    total=[0]
    for j in range(k):
        term=mul(falling_linear(1,0,2*j),falling_linear(1,0,2*k-2*j-1))
        total=add(total,scale(term,math.comb(k,j)*(4*j-2*k+1)))
    return add(mul([1,1],total),scale(falling_linear(1,0,2*k),2*k+1))

def cert(N):
    q=[Q(k) for k in range(N+2)]
    rows=[]
    # Exact independent numeric checks are only secondary validation;
    # positivity certificate is polynomial in x for all r in domain.
    checks=0
    for k in range(N+1):
        for r in [k+3,k+4,k+6,k+13,k+50]:
            lhs=eval_poly(q[k],r)*catalan(r)
            rhs=math.factorial(k)*math.prod(2*r-i for i in range(k))*delta_direct(r,k)*math.comb(2*r-k,k)
            assert lhs==rhs, (k,r,'Q/H numeric identity mismatch')
            checks+=1
    for k in range(1,N+1):
        # N_k(r) = (k+1)(2r-k) Q_k(r)^2
        #          - k(2r-k+1) Q_{k-1}(r) Q_{k+1}(r).
        first=scale(mul([-k,2],mul(q[k],q[k])),k+1)
        second=scale(mul([1-k,2],mul(q[k-1],q[k+1])),k)
        nk=sub(first,second)
        shifted=compose_shift(nk,k+3)
        assert all(x>0 for x in shifted), (k,'negative/nonpositive coefficient')
        assert eval_poly(shifted,2)==eval_poly(nk,k+5)
        # Direct comparison for the finite point checks, independent of Q symbolic algebra.
        for r in [k+3,k+4,k+7,k+50]:
            s=r-k
            def H(t): return math.comb(r+t,2*t)*delta_direct(r,r-t)
            D=H(s)**2-H(s-1)*H(s+1)
            assert D>0
            den=(k+1)*(2*r-k)*math.factorial(k)**2*math.prod(2*r-i for i in range(k))**2
            assert D*den==catalan(r)**2*eval_poly(nk,r)
            checks+=1
        raw=json.dumps(shifted,separators=(',',':'))
        rows.append({
            'k':k,'r_min':k+3,'s_min':3,
            'shifted_degree':len(shifted)-1,
            'shifted_coefficients_count':len(shifted),
            'shifted_leading_coefficient':shifted[-1],
            'shifted_constant_term':shifted[0],
            'shifted_coefficients_sha256':hashlib.sha256(raw.encode('ascii')).hexdigest(),
            'all_coefficients_strictly_positive':True,
            'shifted_coefficients_ascending':shifted
        })
    return {'schema':'R405_TURAN_TAIL_POLYNOMIAL_CERT_V1',
            'model':'original signed 12-branch BRC K/J->B->D, K3[t^2]=-8(1+theta)',
            'scope':'integer r>=k+3, 1<=k<=N, s=r-k; all r unbounded',
            'N':N, 'exact_integer_crosschecks':checks,
            'positive_polynomial_coefficients_total':sum(a['shifted_coefficients_count'] for a in rows),
            'rows':rows,'status':'R405_EXACT_PASS'}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--max-k',type=int,default=24)
    p.add_argument('--out',default='R405_EVIDENCE.json')
    args=p.parse_args()
    assert 1<=args.max_k<=64
    result=cert(args.max_k)
    path=Path(args.out)
    path.write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    print(result['status'], 'k=1..'+str(args.max_k),'coefficient_count',result['positive_polynomial_coefficients_total'],'crosschecks',result['exact_integer_crosschecks'])
    print('evidence_sha256',digest,'evidence_bytes',path.stat().st_size)

if __name__=='__main__': main()
