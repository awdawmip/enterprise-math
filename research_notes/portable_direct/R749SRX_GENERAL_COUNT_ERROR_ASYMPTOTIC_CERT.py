#!/usr/bin/env python3
"""R749SRX: exact rational certificates for six-phase large-M count-error asymptotics.

Finite checks certify the six quasi-polynomial coefficient identities and
selected finite error examples. The mathematical proof of the asymptotic
quantified-over-all-M theorem is in the accompanying research note.
"""
from fractions import Fraction as F
from math import factorial
import json

W=(1,1,2,3,6)
OFFSETS=(0,1,5)
P=tuple(F(x,36) for x in (455,-295,-25,185,-25,-295))
H=(F(1,6),F(1,2),-F(115,36),F(115,6),-F(16315,108))
S=tuple(tuple(P[(a+h)%6] for h in OFFSETS) for a in range(6))
GAMMA=(F(3335,3),F(13780,9),F(12845,9),F(3740,3),F(11485,9),F(12980,9))

def count(N):
    c=[0]*N; t=[0]*N; c[0]=1
    for i,w in enumerate(W):
        for j in range(w,N):
            t[j]+=t[j-w]+(c[j-w] if i==0 else 0)
            c[j]+=c[j-w]
    C=[0];T=[0]
    for v in range(N):
        C.append(C[-1]+c[v]);T.append(T[-1]+t[v])
    return C,T

def add(a,b):
    return [ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b))) ]
def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
def scale(a,x): return [x*v for v in a]
def pw(a,n):
    out=[F(1)]
    for _ in range(n):out=mul(out,a)
    return out
def interp(ys):
    dif=list(map(F,ys)); out=[F(0)]
    for k in range(len(ys)):
        basis=[F(1)]
        for j in range(k):basis=mul(basis,[-F(j),F(1)])
        out=add(out,scale(basis,dif[0]/factorial(k)))
        dif=[dif[j+1]-dif[j] for j in range(len(dif)-1)]
    return out
def evalp(poly,n):return sum(v*n**i for i,v in enumerate(poly))
def deg(poly):
    k=len(poly)-1
    while k>0 and poly[k]==0:k-=1
    return k

def main():
    C,T=count(720)
    for r in (36,37,60,72,128,500,703):
        assert C[r]>0
    sep=min(max(abs(x-y) for x,y in zip(S[a],S[b]))
            for a in range(6) for b in range(a+1,6))
    assert sep==F(15,2)
    assert max(abs(x-y) for x,y in zip(S[0],S[3]))==sep
    assert tuple(1 if y>x else -1 for x,y in zip(S[0],S[3]))==(-1,1,1)
    rows=[]
    for a in range(6):
        base=36+a
        cp=interp([C[base+6*j] for j in range(6)])
        tp=interp([T[base+6*j] for j in range(7)])
        for j in range(12):
            assert evalp(cp,j)==C[base+6*j]
            assert evalp(tp,j)==T[base+6*j]
        # Degree bounds are global for r>=30 from rational generating functions;
        # interpolate 6 (resp. 7) consecutive points to identify them exactly.
        rr=[F(base),F(6)]
        smooth=[P[a]]
        for j,v in enumerate(H):smooth=add(smooth,scale(pw(rr,4-j),v))
        numerator=add(mul(pw(rr,3),tp),scale(mul(cp,smooth),-1))
        assert (deg(cp),deg(tp),deg(numerator))==(5,6,4)
        assert cp[5]==F(9,5)
        gam=6*numerator[4]/cp[5]
        assert gam==GAMMA[a],(a,gam)
        rows.append({'phase':a,'C_degree':5,'T_degree':6,
          'residual_numerator_degree':4,'C_top_in_n':'9/5',
          'lim_r_times_R_minus_P':str(gam),
          'quasipolynomial_samples_checked':12})
    # Independent direct-DP checks at separate finite cutoffs.
    def R(r,eps=0):
        return F(r**3*(T[r]+eps),C[r])-sum(v*r**(4-i) for i,v in enumerate(H))
    def decode(r,eps):
        y=tuple(R(r+h,eps[i]) for i,h in enumerate(OFFSETS))
        distances=[max(abs(x-z) for x,z in zip(y,S[b])) for b in range(6)]
        return [i for i,d in enumerate(distances) if d==min(distances)]
    assert decode(52,(-1,1,-1))==[3]
    assert decode(64,(-2,2,-2))==[3]
    # All residue classes' leading coefficients independently confirm C_r~r^5/4320.
    # The rational generating functions have denominators whose roots divide 6;
    # for r>=30 the period-six sequence has polynomial degree <=5/6.
    result={'status':'PASS','unit':'R749SRX','review':'AUTHOR_EXACT_NOT_REVIEWED',
        'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'weights':list(W),'marked_source':0,'offsets':list(OFFSETS),
        'phase_signature_min_linf_separation':str(sep),
        'closest_pair':[0,3], 'closest_pair_signed_direction':[-1,1,1],
        'rational_gf_C':'z/((1-z)^3*(1-z^2)*(1-z^3)*(1-z^6))',
        'rational_gf_T':'z^2/((1-z)^4*(1-z^2)*(1-z^3)*(1-z^6))',
        'count_asymptotic':'C_r=r^5/4320+O(r^4)',
        'noise_asymptotic':'(r+h)^3/C_(r+h)=4320/r^2+O(r^-3), h=0,1,5',
        'sharp_threshold_asymptotic':'N(M)=24*sqrt(2*M)+O(1) as M tends to infinity',
        'residue_coefficients':rows,
        'finite_residue_positions_checked':72,
        'out_of_sample_C_checks':36,
        'out_of_sample_T_checks':30,
        'prior_known_exact_thresholds':{'M=0':35,'M=1':53,'M=2':65}}
    return result
if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2))
