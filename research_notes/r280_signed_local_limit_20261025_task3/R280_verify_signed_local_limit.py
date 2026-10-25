#!/usr/bin/env python3
"""Exact BRC path histogram / rational generating-function cross-check.

Pure Python standard library; controls: q 0,1,2; clean source words only;
ordered right composition (e,k)*(eta,b)=(eta*e,eta*k+b).
No physical/P000 trajectory is being simulated.
"""
from collections import defaultdict
from math import sqrt, exp, pi
import json

TRANS={
    0:{0:(2,-1,-1),1:(2,+1,-1)},
    1:{0:(0,-1,-1),1:(0,+1,-1)},
    2:{0:(1,+1,+1),1:(2,+1,-1)},
}
PHI=(1+sqrt(5))/2
SIGMA2=(15+7*sqrt(5))/10
MU={+1:-(2+sqrt(5)),-1:-(5+sqrt(5))/2}


def add(d,k,v):
    d[k]=d.get(k,0)+v


def source_coeff(max_n):
    state={(0,False,+1,0):1}
    out=[]
    for n in range(max_n+1):
        bins={+1:{},-1:{}}
        for (q,last_zero,eps,k),amount in state.items():
            if q==0:
                add(bins[eps],k,amount)
        out.append(bins)
        if n==max_n: break
        nxt={}
        for (q,last_zero,eps,k),amount in state.items():
            for bit,(qn,eta,b) in TRANS[q].items():
                if last_zero and bit==0: continue
                neps=eta*eps; nk=eta*k+b
                add(nxt,(qn,bit==0,neps,nk),amount)
        state=nxt
    return out


def rational_coeff(max_n):
    # H=1+x²-x(z+z^-1)-x³(z+z^-1)+2x4+x6-x8
    # H*G+=1+x²+x4-xz^-1-xz-x³z
    # H*G-=x4z^-2-x5z^-1
    out=[]
    numer={+1:{(0,0):1,(2,0):1,(4,0):1,(1,-1):-1,(1,+1):-1,(3,+1):-1},
           -1:{(4,-2):1,(5,-1):-1}}
    for n in range(max_n+1):
        bins={+1:{},-1:{}}
        for eps in [+1,-1]:
            z={}
            # Generate contributions from previous coefficients
            if n>=1:
                for k,a in out[n-1][eps].items():
                    add(z,k-1,a);add(z,k+1,a)
            if n>=2:
                for k,a in out[n-2][eps].items():add(z,k,-a)
            if n>=3:
                for k,a in out[n-3][eps].items():
                    add(z,k-1,a);add(z,k+1,a)
            if n>=4:
                for k,a in out[n-4][eps].items():add(z,k,-2*a)
            if n>=6:
                for k,a in out[n-6][eps].items():add(z,k,-a)
            if n>=8:
                for k,a in out[n-8][eps].items():add(z,k,a)
            for (j,k),a in numer[eps].items():
                if n==j:add(z,k,a)
            bins[eps]={k:a for k,a in z.items() if a}
        out.append(bins)
    return out


def run():
    source=source_coeff(300)
    gf=rational_coeff(150)
    checked=0
    for n in range(151):
        for eps in [+1,-1]:
            assert source[n][eps]==gf[n][eps],(n,eps,'GF mismatch')
            checked+=len(source[n][eps])
    examples=[]
    for n in (40,80,120,200,300):
        data=source[n]
        peak=max([(v,e,k) for e in (+1,-1) for k,v in data[e].items()]); peak_count, peak_eps, peak_k=peak
        exact=float(peak_count/(10**(len(str(peak_count))-1)))*10**(len(str(peak_count))-1) if len(str(peak_count))<307 else float('nan')
        # Avoid exp overflow and preserve robust ratio by using logarithms of ints
        from math import log
        log_peak=log(peak_count)
        log_lead=n*log(PHI)-log(5)-.5*log(2*pi*SIGMA2*n)
        ratio=exp(log_peak-log_lead)
        max_near=[]
        for eps in (+1,-1):
            items=sorted([(v,k) for k,v in data[eps].items()], reverse=True)
            max_near.append({'eps':eps,'k':items[0][1], 'shift_from_mu':round(items[0][1]-MU[eps],8)})
        examples.append({'n':n,'peak_effect':[peak_eps,peak_k], 'peak_count_decimal':str(peak_count),
                         'ratio_to_LLT_lead':round(ratio,10),'per_sign_modes':max_near})
    for n in range(301):
        for eps in (+1,-1):
            assert all(k%2==n%2 and c>0 for k,c in source[n][eps].items()), ('bad support',n)
    output={'status':'PASS','model':'R279 clean q0 ordered-positive affine BRC',
            'source_dp_max_n':300,'independent_rational_GF_max_n':150,'nonzero_coeffs_checked':checked,
            'parity_layers_checked':301,'sigma2_double':SIGMA2,
            'means_double':MU,'peak_examples':examples,
            'proof_note':'Numeric ratios are illustrative; all-n local limit relies on analytic pole/spectral argument, not extrapolation.'}
    print(json.dumps(output,ensure_ascii=False,indent=2))
    return output

if __name__=='__main__':run()
