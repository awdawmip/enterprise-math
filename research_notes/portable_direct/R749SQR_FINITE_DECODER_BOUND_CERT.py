#!/usr/bin/env python3
"""R749SQR finite-r recovery theorem via rational quasipolynomials, standard library.
For r>=512 prove 0<r^4(E_1-H_4)-P(r)<35/12 on all residues.
"""
import json
from fractions import Fraction as F
from math import factorial
from R749SQR_SIMULTANEOUS_CYCLOTOMIC_CERT import prefix_counts, smooth_mean, phase

S=(1,1,2,3,6)

def padd(a,b):
    return [(a[k] if k<len(a) else F(0))+(b[k] if k<len(b) else F(0))
            for k in range(max(len(a),len(b)))]

def pscale(a,c):
    return [v*c for v in a]

def pmul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def ppow(a,k):
    out=[F(1)]
    for _ in range(k):out=pmul(out,a)
    return out

def ptrim(a):
    while len(a)>1 and not a[-1]:a.pop()
    return a

def binom_poly(k):
    a=[F(1)]
    for j in range(k):a=pmul(a,[-F(j),F(1)])
    return pscale(a,F(1,factorial(k)))

def interpolate_forward(vals):
    # Exact forward differences at n=0 times binom(n,k).
    diff=list(map(F,vals));out=[F(0)]
    for k in range(len(vals)):
        out=padd(out,pscale(binom_poly(k),diff[0]))
        diff=[diff[i+1]-diff[i] for i in range(len(diff)-1)]
    return ptrim(out)

def eval_poly(p,n):
    return sum(x*n**k for k,x in enumerate(p))

def start_for_residue(a):
    return next(v for v in range(512,518) if v%6==a)

def run():
    C,T=prefix_counts(S,600)
    H=smooth_mean(S,4,0)
    cases=[]
    for a in range(6):
        start=start_for_residue(a)
        Cp=interpolate_forward([C[start+6*k] for k in range(6)])
        Tp=interpolate_forward([T[0][start+6*k] for k in range(7)])
        assert all(eval_poly(Cp,k)==C[start+6*k] for k in range(9))
        assert all(eval_poly(Tp,k)==T[0][start+6*k] for k in range(9))
        rr=[F(start),F(6)]
        HplusP=[F(phase(a,1))]
        for j,h in enumerate(H):
            HplusP=padd(HplusP,pscale(ppow(rr,4-j),h))
        N=ptrim(padd(pmul(ppow(rr,3),Tp),pscale(pmul(Cp,HplusP),-1)))
        upper=ptrim(padd(pscale(Cp,F(35,12)),pscale(N,-1)))
        assert len(Cp)==6 and len(Tp)==7
        assert len(N)==5
        assert all(v>0 for v in N)
        assert all(v>0 for v in upper)
        assert all(v>0 for v in Cp)
        # Exact for all k>=0 because [z^r]F and [z^r]N are
        # quasipolynomials of degrees 5 and 6 and period dividing 6.
        cases.append({'residue_mod_6':a,'first_r':start,
                      'C_coefficients':[str(x) for x in Cp],
                      'N_coefficients':[str(x) for x in N],
                      'upper_35_over_12_coefficients':[str(x) for x in upper],
                      'all_coefficients_strictly_positive':True})
    fail=[]
    for r in range(1,512):
        scaled=F(r**3*T[0][r],C[r])-sum(h*r**(4-j) for j,h in enumerate(H))
        err=scaled-phase(r,1)
        if not (F(0)<err<F(35,12)):fail.append(r)
    assert fail and max(fail)==511
    return {'status':'PASS','finite_sufficient_threshold':512,
            'claim':'For all integer r>=512: 0 < r^4*(E_{1,r}-H_{1,4}(r))-P_1(r) < 35/12.',
            'consequence':'Two consecutive scaled residual reads identify r mod 6 by nearest exact phase pair for all integer r>=512.',
            'last_small_r_failing_sufficient_bound':max(fail),
            'number_small_r_failing_sufficient_bound':len(fail),
            'method':'exact rational quasipolynomial interpolation, degree bounds proven from generating-function poles; coefficientwise positive polynomials in n=(r-first_r)/6 for n>=0',
            'cases':cases,'math_review':'NOT_REVIEWED'}

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2))
