#!/usr/bin/env python3
"""Exact unbounded-r right-tail certificate for signed-BRC auxiliary Catalan kernel.

Computation is over Z[x] only. All-k theorem not asserted: each computed k
is a separate infinite-in-r polynomial positivity certificate.
"""
import math, hashlib, json, argparse
from pathlib import Path

def trim(p):
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def mul(a,b):
    p=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b):
                if bj: p[i+j]+=ai*bj
    return trim(p)

def scale(a,c):return trim([x*c for x in a])
def add(a,b):
    p=[0]*max(len(a),len(b))
    for i,x in enumerate(a):p[i]+=x
    for i,x in enumerate(b):p[i]+=x
    return trim(p)
def sub(a,b):return add(a,scale(b,-1))
def linprod(n):
    p=[1]
    for j in range(n):p=mul(p,[-j,1])
    return p

def shift(p,z):
    q=[0]
    for a in p[::-1]:q=add(mul(q,[z,1]),[a])
    return q

def horner(p,z):
    t=0
    for v in p[::-1]:t=t*z+v
    return t

def cat(r):return math.comb(2*r,r)//(r+1)

def delta_kernel(r,k):
    """R404 Catalan positive kernel, independent of the alternating binomial path."""
    s=r-k
    return sum(math.comb(s-1,j)*2**(s-1-j)*cat((k+j)//2)
               for j in range(s) if (k+j)%2==0)

def delta_raw(r,k):
    n=2*r-2*k
    def choose(m):return math.comb(n,m) if 0<=m<=n else 0
    return sum(math.comb(k,j)*(choose(r-2*j)-choose(r-2*j-1)) for j in range(k+1))

def Q(k,fall):
    a=[0]
    for j in range(k):
        a=add(a,scale(mul(fall[2*j],fall[2*k-2*j-1]),math.comb(k,j)*(4*j-2*k+1)))
    return add(mul([1,1],a),scale(fall[2*k],2*k+1))

def run(limit):
    # Shared integer falling polynomials, no float approximation.
    fall=[linprod(i) for i in range(2*limit+3)]
    qs=[Q(k,fall) for k in range(limit+2)]
    rows=[]; point_checks=0; poly_count=0
    # Two independent delta representations and exact rational-identity spot checks.
    for k in range(limit+1):
        for r in (k+3,k+5,k+11):
            assert delta_raw(r,k)==delta_kernel(r,k),(k,r,'delta kernels disagree')
            # Check R405.2 independently at each integer point.
            lhs=math.comb(2*r-k,k)*delta_raw(r,k)*math.factorial(k)*math.prod(2*r-i for i in range(k))
            rhs=cat(r)*horner(qs[k],r)
            if lhs!=rhs:raise AssertionError(('Q_raw',k,r,lhs,rhs))
            point_checks+=1
    for k,q in enumerate(qs):
        assert q[-1]==2**k,(k,'Q leading coefficient')
        if k>=1:assert q[-2]==-2**k*k*(k+1),(k,'Q subleading coefficient')
    for k in range(1,limit+1):
        N=sub(scale(mul([-k,2],mul(qs[k],qs[k])),k+1),scale(mul([1-k,2],mul(qs[k-1],qs[k+1])),k))
        p=shift(N,k+3)
        bad=[i for i,a in enumerate(p) if a<=0]
        if bad:raise AssertionError(('nonpositive_shift_coefficient',k,bad[:3],p[bad[0]]))
        for r in (k+3,k+8,k+15):
            s=r-k
            def H(t):return math.comb(r+t,2*t)*delta_raw(r,r-t)
            D=H(s)**2-H(s-1)*H(s+1)
            den=(k+1)*(2*r-k)*math.factorial(k)**2*math.prod(2*r-i for i in range(k))**2
            if D*den!=cat(r)**2*horner(N,r):raise AssertionError(('N_raw',k,r))
            point_checks+=1
        assert len(p)==4*k+2 and p[-1]==2**(2*k+1), (k,len(p),p[-1])
        assert N[-2]==-2**(2*k+1)*k*(2*k+1),(k,'N subleading coefficient')
        b=json.dumps(p,separators=(',',':')).encode()
        rows.append({'k':k,'min_r':k+3,'min_s':3,'degree':len(p)-1,'positive_coefficient_count':len(p),'positive':True,'constant_term':str(p[0]),'leading_coefficient':str(p[-1]),'coefficients_sha256':hashlib.sha256(b).hexdigest(),'coefficients_decimal':[str(v) for v in p]})
        poly_count+=len(p)
    return {'schema':'R406_TURAN_RIGHT_BAND_EXACT_CERT_V1','source':'R405 Eq.(R405.1)-(R405.4), signed BRC auxiliary model only','k_range':[1,limit],'domain':'all integer k in range, r>=k+3, s=r-k, infinite r','arithmetic':'exact integers Z[x]','strictly_positive_shift_coefficients':poly_count,'point_crosschecks':point_checks,'rows':rows,'status':'R406_EXACT_PASS'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--max-k',type=int,default=32);ap.add_argument('--out',default='R406_EVIDENCE.json');args=ap.parse_args()
    data=run(args.max_k)
    out=Path(args.out);out.write_text(json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n',encoding='utf8')
    print(data['status'],'k=',args.max_k,'positive_coefficients=',data['strictly_positive_shift_coefficients'],'point_checks=',data['point_crosschecks'])
    print('SHA256',hashlib.sha256(out.read_bytes()).hexdigest(),'bytes',out.stat().st_size)