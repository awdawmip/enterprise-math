#!/usr/bin/env python3
"""R749SRV: exact sharp cutoff for one-integer marked-count errors.

Only Python standard library. Count arithmetic is integer; decoding and
six-residue polynomial certificates use fractions.Fraction.
Frozen input: auxiliary Walsh labeled weights (1,1,2,3,6), source #1 marked.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
import json

WEIGHTS=(1,1,2,3,6)
OFFSETS=(0,1,5)
PHASE=tuple(F(x,36) for x in (455,-295,-25,185,-25,-295))
SIGNATURES=tuple(tuple(PHASE[(a+h)%6] for h in OFFSETS) for a in range(6))
SMOOTH=(F(1,6),F(1,2),-F(115,36),F(115,6),-F(16315,108))

def counts(length=600):
    coeff=[0]*length; marked=[0]*length; coeff[0]=1
    for i,w in enumerate(WEIGHTS):
        for v in range(w,length):
            marked[v]+=marked[v-w]+(coeff[v-w] if i==0 else 0)
            coeff[v]+=coeff[v-w]
    C=[0]; T=[0]
    for v in range(length):
        C.append(C[-1]+coeff[v]);T.append(T[-1]+marked[v])
    return C,T

def independent_enumeration(r):
    def rec(i,remaining,mark):
        if i==len(WEIGHTS):return (1,mark)
        c=t=0
        for k in range(remaining//WEIGHTS[i]+1):
            a,b=rec(i+1,remaining-k*WEIGHTS[i],mark+(k if i==0 else 0))
            c+=a;t+=b
        return c,t
    return rec(0,r-1,0)

def R(r,C,T,epsilon=0):
    return F(r**3*(T[r]+epsilon),C[r])-sum(a*r**(4-i) for i,a in enumerate(SMOOTH))

def polyadd(a,b):
    return [ (a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0))
             for i in range(max(len(a),len(b))) ]

def polymul(a,b):
    z=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):z[i+j]+=v*w
    return z

def polypow(a,k):
    z=[F(1)]
    for _ in range(k):z=polymul(z,a)
    return z

def polyscale(a,c):return [v*c for v in a]
def evalpoly(a,n):return sum(v*n**i for i,v in enumerate(a))

def interp(ys):
    dif=list(map(F,ys));out=[F(0)]
    for k in range(len(ys)):
        basis=[F(1)]
        for j in range(k):basis=polymul(basis,[-F(j),F(1)])
        out=polyadd(out,polyscale(basis,dif[0]/factorial(k)))
        dif=[dif[j+1]-dif[j] for j in range(len(dif)-1)]
    return out

def certify_tail(C,T):
    # Recreate the SRU exact 0 < R(r)-P(r mod 6) < 35/12 bound.
    # Rational GF pole orders at z=1 are 6 and 7 respectively; all other
    # roots of unity have period dividing 6 and smaller orders.
    rows=[]
    for a in range(6):
        start=next(r for r in range(512,518) if r%6==a)
        cp=interp([C[start+6*n] for n in range(6)])
        tp=interp([T[start+6*n] for n in range(7)])
        assert all(evalpoly(cp,n)==C[start+6*n] and
                   evalpoly(tp,n)==T[start+6*n] for n in range(8))
        rr=[F(start),F(6)];smooth=[PHASE[a]]
        for j,v in enumerate(SMOOTH):
            smooth=polyadd(smooth,polyscale(polypow(rr,4-j),v))
        num=polyadd(polymul(polypow(rr,3),tp),polyscale(polymul(cp,smooth),-1))
        upper=polyadd(polyscale(cp,F(35,12)),polyscale(num,-1))
        while num[-1]==0:num.pop()
        while upper[-1]==0:upper.pop()
        assert [len(cp),len(tp),len(num),len(upper)]==[6,7,5,6]
        assert all(v>0 for v in cp+num+upper)
        rows.append({'phase':a,'start':start,'C_degree':5,
                     'T_degree':6,'num_degree':4,'upper_degree':5,
                     'all_coefficients_positive':True})
    return rows

def decode(r,eps,C,T):
    y=tuple(R(r+h,C,T,eps[i]) for i,h in enumerate(OFFSETS))
    distances=tuple(max(abs(y[i]-SIGNATURES[b][i]) for i in range(3))
                    for b in range(6))
    smallest=min(distances)
    winners=[b for b,v in enumerate(distances) if v==smallest]
    return winners,distances,y

def main():
    C,T=counts()
    for r in range(1,25):assert (C[r],T[r])==independent_enumeration(r)
    tail=certify_tail(C,T)
    minsep=min(max(abs(x-z) for x,z in zip(SIGNATURES[a],SIGNATURES[b]))
               for a in range(6) for b in range(a+1,6))
    assert minsep==F(15,2)
    worst_gap=None; finite_checks=0
    for r in range(53,512):
        for eps in product((-1,0,1),repeat=3):
            winners,dists,_=decode(r,eps,C,T)
            assert winners==[r%6],(r,eps,winners)
            gap=min(dists[b] for b in range(6) if b!=r%6)-dists[r%6]
            if worst_gap is None or gap<worst_gap[0]:worst_gap=(gap,r,eps)
            finite_checks+=1
    assert finite_checks==(512-53)*27
    eps=(-1,1,-1)
    winners,d52,y52=decode(52,eps,C,T)
    assert winners==[3] and 52%6==4
    # Count-lattice lower bound: C_r > (r-1)^5/(5^5*prod WEIGHTS).
    # Thus |delta R_r| <= r^3/C_r < 112500*r^3/(r-1)^5.
    assert 5**5*factorial(1)*WEIGHTS[0]*WEIGHTS[1]*WEIGHTS[2]*WEIGHTS[3]*WEIGHTS[4]==112500
    bound=F(112500*512**3,511**5)
    assert bound<F(5,6)
    # The rational function 112500*r^3/(r-1)^5 is strictly decreasing for r>1.
    # On r>=512, exact residual error <35/12 and count error <5/6;
    # their sum is < minsep/2=15/4, proving unique decoding for all later r.
    return {'status':'PASS','research_unit':'R749SRV',
        'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'model_weights':list(WEIGHTS),'marked_source_index':0,
        'observer':'R(r)=r^3*T_r/C_r-r^4*H4(r)',
        'read_offsets':list(OFFSETS),
        'error_model':'C_r exact; independent integer errors epsilon_h in {-1,0,1} on T_{r+h}',
        'theorem':'For every integer r>=53 and all 27 errors, nearest ideal six-phase signature uniquely equals r mod 6. Cutoff 53 is least possible.',
        'finite_verified_range':[53,511], 'finite_cutoffs':459,
        'finite_error_vectors_per_cutoff':27,'finite_vectors_checked':finite_checks,
        'finite_competitor_distance_comparisons':finite_checks*6,
        'smallest_finite_gap':[str(worst_gap[0]),worst_gap[1],list(worst_gap[2])],
        'sharpness_counterexample':{'r':52,'true_phase':4,'error':list(eps),'decoded_phase':3,
             'true_distance':str(d52[4]),'rival_distance':str(d52[3]),
             'difference_rival_minus_true':str(d52[3]-d52[4]),
             'observed_scaled_residuals':[str(v) for v in y52]},
        'tail_range':'all integer r>=512',
        'minimum_ideal_signature_distance':str(minsep),
        'tail_exact_residual_bound':'0<R(r)-P(r mod 6)<35/12',
        'tail_raw_count_noise_bound_at_512':str(bound),
        'tail_count_noise_bound':'112500*r^3/(r-1)^5 decreasing for r>=512',
        'tail_sum_bound':'35/12 + 5/6 = 15/4 (strict inequality) ',
        'tail_positive_coefficient_certificates':tail,
        'independent_small_enumeration_cutoffs':24,
        'review':'AUTHOR_EXACT_NOT_REVIEWED'}

if __name__=='__main__':
    print(json.dumps(main(),indent=2,ensure_ascii=False))
