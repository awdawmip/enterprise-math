#!/usr/bin/env python3
"""R407 exact rational-polynomial certificates: s=6..16, all integer r>s.
Requires Python>=3.10 and sympy.  No floating-point sign tests.
"""
import argparse
import hashlib
import json
from math import comb
from pathlib import Path
import sympy as S

m, x = S.symbols('m x', integer=True)

def cat_shift(h, parity):
    """Cat_{m-h}/Cat_{m-1} (even r), or Cat_{m-h}/Cat_m (odd r)."""
    y = S.Integer(1)
    for j in range(1 if parity == 0 else 0, h):
        z = m-j
        y *= (z+1)/(2*(2*z-1))
    return S.cancel(y)

def delta_ratio(s, parity):
    """delta_{r,s}/C, C=Cat_{m-1} if r=2m, else Cat_m."""
    y = S.Integer(0)
    for j in range(s):
        h = s-j if parity == 0 else s-1-j
        if h % 2 == 0:
            y += S.binomial(s-1,j)*2**(s-1-j)*cat_shift(h//2,parity)
    return S.cancel(y)

def ratio_turan(s,parity):
    r = 2*m+parity
    Bfactor = S.Rational(2*s*(2*s-1),(2*s+2)*(2*s+1)) * (r+s+1)*(r-s)/((r+s)*(r-s+1))
    a=delta_ratio(s,parity)
    b=delta_ratio(s-1,parity)
    c=delta_ratio(s+1,parity)
    return S.factor(S.cancel(a*a - Bfactor*b*c))

def direct_delta(r,s):
    return sum(comb(r-s,j)*(comb(2*s,r-2*j) if 0<=r-2*j<=2*s else 0)
               -comb(r-s,j)*(comb(2*s,r-2*j-1) if 0<=r-2*j-1<=2*s else 0)
               for j in range(r-s+1))

def catalan(n):
    return comb(2*n,n)//(n+1)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--min-s',type=int,default=6)
    ap.add_argument('--max-s',type=int,default=16)
    ap.add_argument('--max-r',type=int,default=96)
    ap.add_argument('--out',default='R407_EVIDENCE.json')
    args=ap.parse_args()
    assert 6<=args.min_s<=args.max_s<=16
    assert args.max_r >= args.max_s+1
    out=[]
    models={}
    pos_num=pos_den=0
    for s in range(args.min_s,args.max_s+1):
        for parity in (0,1):
            f=ratio_turan(s,parity)
            numer,denom=S.fraction(f)

            # r=2m+parity >= s+1
            m0=(s+2-parity)//2
            assert 2*m0+parity >= s+1
            numerator_poly=S.Poly(S.expand(numer.subs(m,x+m0)),x,domain='ZZ')
            denominator_poly=S.Poly(S.expand(denom.subs(m,x+m0)),x,domain='ZZ')
            nc=[int(v) for v in numerator_poly.all_coeffs()]
            dc=[int(v) for v in denominator_poly.all_coeffs()]
            assert min(nc)>0 and min(dc)>0, (s,parity)
            assert numerator_poly.degree()==s-1+parity
            assert denominator_poly.degree()==s-1+parity
            pos_num+=len(nc);pos_den+=len(dc)
            models[(s,parity)]=(nc,dc,m0)
            data={'s':s,'parity':parity,'m0':m0,
                  'numerator_coefficients_desc':nc,'denominator_coefficients_desc':dc}
            canon=json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
            data['sha256']=hashlib.sha256(canon).hexdigest()
            out.append(data)
    checks=0
    # Entire tested rectangle, independent raw binomial coefficient extraction.
    for r in range(args.min_s+1,args.max_r+1):
        for s in range(args.min_s,min(args.max_s,r-1)+1):
            C=catalan(r//2-1 if r%2==0 else r//2)
            B=comb(r+s,2*s)
            values=[comb(r+t,2*t)*direct_delta(r,t) for t in (s-1,s,s+1)]
            direct=values[1]**2-values[0]*values[2]
            assert direct>0, (r,s)
            nc,dc,m0=models[(s,r%2)]
            xx=r//2-m0
            def horner(cs):
                y=0
                for q in cs:y=y*xx+q
                return y
            assert direct*horner(dc)==(B*C)**2*horner(nc), (r,s)
            checks+=1
    evidence={'schema':'R407_EXACT_POSITIVITY_CERTIFICATE_V1',
              'scope':{'s_min':args.min_s,'s_max':args.max_s,'r_rule':'all integers r>=s+1',
                       'numerical_crosscheck_r_min':args.min_s+1,'numerical_crosscheck_r_max':args.max_r},
              'certificate_count':len(out),'positive_numerator_coefficients':pos_num,
              'positive_denominator_coefficients':pos_den,'independent_direct_checks':checks,
              'rational_polynomials':out}
    target=Path(args.out)
    payload=(json.dumps(evidence,sort_keys=True,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    target.write_bytes(payload)
    print('R407_EXACT_PASS', 's='+str(args.min_s)+'..'+str(args.max_s), 'certificates='+str(len(out)),
          'positive_num='+str(pos_num),'positive_den='+str(pos_den),
          'direct_checks='+str(checks),'bytes='+str(len(payload)),
          'sha256='+hashlib.sha256(payload).hexdigest())

if __name__ == '__main__':
    main()
