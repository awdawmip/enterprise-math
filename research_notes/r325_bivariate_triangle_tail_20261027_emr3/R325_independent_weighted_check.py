#!/usr/bin/env python3
"""Independent original-M recurrence and exact weighted-grading proof witness.
Usage: python R325_independent_weighted_check.py --max 192
Requires sympy; the original-polynomial comparison is integral.
"""
import argparse, json
from math import comb
from sympy import symbols, Poly, expand, cancel
import R325_scan_triangle_1024 as transfer

def C(n,k): return comb(n,k) if 0<=k<=n else 0

def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def mul(a,b):
    o=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: o[i+j]+=x*y
    return trim(o)

def sub(a,b):
    o=a+[0]*max(0,len(b)-len(a))
    for j,v in enumerate(b): o[j]-=v
    return trim(o)

def minus_power(k): return [(-1)**i*C(k,i) for i in range(k+1)]

def delta(i):
    return [0,-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),
            C(7,i-2),-C(9,i-3)]

def direct(n):
    factors=[None]+[mul(delta(i),minus_power(i-1)) for i in range(1,13)]
    M={0:[1]}; B={0:[1,1]}
    checked=0
    for s in range(n+1):
        if s>0:
            ms=mul([0,-C(3,s-1),-C(6,s-1),C(8,s-2)],
                   minus_power(s)) if s<=10 else [0]
            for i in range(1,min(s,12)+1):
                ms=sub(ms,mul(factors[i],M[s-i]))
            M[s]=ms
            assert len(ms)<=2*s+2
            b=transfer.source(s)
            b.extend([0]*(2*s+2-len(b)))
            for i in range(1,min(s,12)+1):
                for j,c in enumerate(transfer.K[i]):
                    if c:
                        for q,a in enumerate(B[s-i]): b[q+j]+=c*a
            B[s]=trim(b)
        expected=[0]*(2*s+2)
        for j,c in enumerate(M[s]):
            if c:
                for q in range(2*s+2-j):expected[q]+=c*C(2*s+1-j,q)
        expected=trim(expected)
        assert expected==B[s],(s,expected[:8],B[s][:8])
        checked+=len(B[s])
        if s>=12: del M[s-12];del B[s-12]
    return {"status":"PASS","max_s":n,"independent_full_row_coefficients":checked}

def grade(expr,w,z,g):
    return expand(sum(c*w**i*z**j for (i,j),c in
        Poly(expr,w,z).terms() if i-4*j==g))

def symbolic():
    w,z=symbols("w z")
    N=1-z*w*(1+w)**3-z**2*w*(1+w)**6+z**3*w**2*(1+w)**8
    D=-z*((1+w)**4-1)+z*w*(1+w)**2+z**2*w*(1-w)*(1+w)**5+z**3*w**2*(1+w)**7-z**4*w**3*(1+w)**9
    nsum=1+sum((-C(3,i-1)*z-C(6,i-1)*z*z+
                    C(8,i-2)*z**3)*w**i for i in range(1,11))
    dsum=sum(((-C(4,i)+C(2,i-1))*z+
              (C(5,i-1)-C(5,i-2))*z*z+
              C(7,i-2)*z**3-C(9,i-3)*z**4)*w**i
              for i in range(1,13))
    assert expand(N-nsum)==0 and expand(D-dsum)==0
    Q=expand(1-z+D)
    H=expand((1-z)*(N-1)-D)
    T=z*w**4
    assert expand(grade(Q,w,z,0)-(1-T))==0
    assert expand(grade(Q,w,z,-1)+z*w**3*(3+T))==0
    assert expand(grade(H,w,z,-2)-z*w**2*(1-T)**2)==0
    assert expand(grade(H,w,z,-3)-z*w*(2-10*T+7*T*T))==0
    assert max(i-4*j for (i,j),c in Poly(Q,w,z).terms())==0
    assert max(i-4*j for (i,j),c in Poly(H,w,z).terms())==-2
    g2=z*w**2*(1-T)
    g3=z*w*(2-5*T-T**3/(1-T))
    assert cancel(g2-z*w**2*(1-T)**2/(1-T))==0
    assert cancel(g3-(z*w*(2-10*T+7*T*T)/(1-T)
        -z*w**2*(1-T)**2*(-z*w**3*(3+T))/(1-T)**2))==0
    # Formal expansion -T^3/(1-T) has coefficient -1 at T^(r-1), r>=4.
    return {"status":"PASS","grade_rule":"deg_w - 4 deg_z",
      "Q0":"1-T","Q_minus1":"-z*w^3*(3+T)",
      "H_minus2":"z*w^2*(1-T)^2",
      "H_minus3":"z*w*(2-10*T+7*T^2)",
      "Uminus1_grade_minus2":"z*w^2*(1-T)",
      "Uminus1_grade_minus3":"z*w*(2-5*T-T^3/(1-T))",
      "infinite_negative_tail_coeff":-1}

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--max",type=int,default=192)
    ap.add_argument("--json",default=None)
    args=ap.parse_args()
    out={"direct_original_M_comparison":direct(args.max),
         "formal_weighted_certificate":symbolic()}
    print(json.dumps(out,ensure_ascii=False,indent=2))
    if args.json:
        with open(args.json,"w",encoding="utf-8") as f:
            json.dump(out,f,indent=2,ensure_ascii=False)
            f.write("\n")
