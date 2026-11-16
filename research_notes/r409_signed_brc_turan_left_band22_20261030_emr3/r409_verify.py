#!/usr/bin/env python3
"""R409: exact positive-coefficient certificates for s=22, all r>s.
Source basis: R404 Catalan kernel, R407 normalized Turan identity.
Requires Python 3.10+ and SymPy. No floating-point sign tests.
Each parity is processed in a separate child to avoid SymPy expression-cache
pressure; universal claim comes from exact rational identities and coefficient
positivity, not from the independent bounded integer-grid tests.
"""
import argparse
import hashlib
import json
import subprocess
import sys
from math import comb
from pathlib import Path
import sympy as sp
m,x=sp.symbols('m x',integer=True)

def catalan(n):
    assert n>=0
    return comb(2*n,n)//(n+1)

def cat_shift(h,parity):
    y=sp.Integer(1)
    for j in range(1 if parity==0 else 0,h):
        z=m-j
        y*=(z+1)/(2*(2*z-1))
    return sp.cancel(y)

def delta_ratio(s,parity):
    y=sp.Integer(0)
    for j in range(s):
        h=s-j if parity==0 else s-1-j
        if h%2==0:
            y+=sp.binomial(s-1,j)*2**(s-1-j)*cat_shift(h//2,parity)
    return sp.cancel(y)

def normalized_turan(s,parity):
    r=2*m+parity
    lam=(sp.Rational(2*s*(2*s-1),(2*s+2)*(2*s+1))
         *(r+s+1)*(r-s)/((r+s)*(r-s+1)))
    a,b,c=(delta_ratio(q,parity) for q in (s,s-1,s+1))
    return sp.factor(sp.cancel(a*a-lam*b*c))

def direct_delta(r,s):
    total=0
    for j in range(r-s+1):
        q=r-2*j
        pos=comb(2*s,q) if 0<=q<=2*s else 0
        neg=comb(2*s,q-1) if 0<=q-1<=2*s else 0
        total+=comb(r-s,j)*(pos-neg)
    return total

def kernel_delta(r,s):
    return sum(comb(s-1,j)*2**(s-1-j)*catalan((r-s+j)//2)
               for j in range(s) if (r-s+j)%2==0)

def integer_h(r,s):
    return comb(r+s,2*s)*direct_delta(r,s)

def build_single(s,parity):
    f=normalized_turan(s,parity)
    num,den=sp.fraction(f)
    m0=(s+2-parity)//2
    assert 2*m0+parity>=s+1
    N=sp.Poly(sp.expand(num.subs(m,x+m0)),x,domain='ZZ')
    Q=sp.Poly(sp.expand(den.subs(m,x+m0)),x,domain='ZZ')
    assert N.degree()==s-1+parity and Q.degree()==s-1+parity
    nc=[int(c) for c in N.all_coeffs()]
    dc=[int(c) for c in Q.all_coeffs()]
    assert min(nc)>0 and min(dc)>0,(s,parity)
    # Entire rational identity: num/den is extracted by SymPy exact arithmetic,
    # then x=m-m0 is a bijective polynomial change of variable.
    count=cross=0
    for r in range(2*m0+parity,121,2):
        for a in (s-1,s,s+1):
            assert direct_delta(r,a)==kernel_delta(r,a),(r,a)
            count+=1
        B=comb(r+s,2*s)
        C=catalan((r//2-1) if parity==0 else r//2)
        D=integer_h(r,s)**2-integer_h(r,s-1)*integer_h(r,s+1)
        xx=(r-parity)//2-m0
        assert int(Q.eval(xx))*D==int(N.eval(xx))*(B*C)**2,(r,s)
        assert D>0
        cross+=1
    cert={'s':s,'parity':parity,'m0':m0,'numerator_coefficients_desc':nc,
          'denominator_coefficients_desc':dc,
          'independent_delta_checks':count,'turan_cross_multiplication_checks':cross}
    payload=json.dumps(cert,sort_keys=True,separators=(',',':')).encode()
    cert['sha256']=hashlib.sha256(payload).hexdigest()
    return cert

def aggregate():
    certs=[]
    for s in range(22,23):
        for p in (0,1):
            cached=Path(__file__).with_name(f'cert_{s}_{p}.json')
            if cached.exists() and cached.stat().st_size>0:
                cert=json.loads(cached.read_text(encoding='utf-8'))
            else:
                output=subprocess.run([sys.executable,__file__,'--single-s',str(s),'--single-parity',str(p)],
                    text=True,capture_output=True,check=True,timeout=150)
                cert=json.loads(output.stdout)
            assert cert['s']==s and cert['parity']==p
            digest=cert['sha256']
            signed={k:v for k,v in cert.items() if k!='sha256'}
            assert digest==hashlib.sha256(json.dumps(signed,sort_keys=True,separators=(',',':')).encode()).hexdigest()
            assert min(cert['numerator_coefficients_desc'])>0 and min(cert['denominator_coefficients_desc'])>0
            assert len(cert['numerator_coefficients_desc'])==s+p
            assert len(cert['denominator_coefficients_desc'])==s+p
            certs.append(cert)
            print('verified',s,p,'coeffs',len(cert['numerator_coefficients_desc']),flush=True)
    data={'schema':'ENTERPRISE_MATH_R409_TURAN_FIXED_S22_ONLY_V1',
        'model':'original signed 12-branch BRC auxiliary, via R404/R407',
        'theorem':'For every integer s=22 and every integer r>=s+1, D_(r,s)>0',
        'certificates':certs,
        'certificate_count':len(certs),
        'strictly_positive_num_coefficients':sum(len(z['numerator_coefficients_desc']) for z in certs),
        'strictly_positive_den_coefficients':sum(len(z['denominator_coefficients_desc']) for z in certs),
        'independent_delta_checks':sum(z['independent_delta_checks'] for z in certs),
        'turan_cross_multiplication_checks':sum(z['turan_cross_multiplication_checks'] for z in certs),
        'status':'AUTHOR_SIDE_EXACT_UNREVIEWED_NOT_ADMITTED'}
    out=Path(__file__).with_name('R409_EVIDENCE.json')
    out.write_text(json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print('R409_EXACT_PASS',data['certificate_count'],data['strictly_positive_num_coefficients'],
        data['strictly_positive_den_coefficients'],data['turan_cross_multiplication_checks'],
        data['independent_delta_checks'])
    print('EVIDENCE_SHA256',hashlib.sha256(out.read_bytes()).hexdigest())

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--single-s',type=int)
    ap.add_argument('--single-parity',type=int,choices=(0,1))
    args=ap.parse_args()
    if args.single_s is not None:
        assert args.single_s==22 and args.single_parity is not None
        print(json.dumps(build_single(args.single_s,args.single_parity),sort_keys=True,separators=(',',':')))
    else:
        aggregate()
