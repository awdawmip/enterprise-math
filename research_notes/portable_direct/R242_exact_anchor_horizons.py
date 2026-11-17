#!/usr/bin/env python3
"""R242: exact fixed-parameter one-mode horizon certificates.

Only stdlib. Uses rational killed-Markov propagation and a rational
secular-root/amplitude enclosure. No floating point affects PASS.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import lcm
import json
import sys
sys.set_int_max_str_digits(100000)

WEIGHTS = (144, 576, 1440, 4320, 17280, 86400, 518400)
CASES = (
    (F(39, 100), (513, 768)),
    (F(2, 5), (608, 912)),
    (F(41, 100), (752, 1128)),
)
ROOT_DENOMINATOR = 10**30


def parameters(s):
    alpha = (F(1,5), F(1,4), F(3,10), F(9,20), s, F(2,3),
             (1691*s-2615)/(2615*s-3539))
    b = (F(13,60),) + tuple(F(5,18)*abs(F(1,2)-a) for a in alpha[1:])
    pi = tuple(bb/(1-a) for bb,a in zip(b,alpha))
    z = sum((bb/(1-a)**2 for a,bb in zip(alpha,b)), F(0))
    rho = tuple(bb/((1-a)**2*z) for a,bb in zip(alpha,b))
    p = tuple(tuple(alpha[i]*(i==j)+(1-alpha[i])*pi[j]
                    for j in range(7)) for i in range(7))
    assert sum(pi)==sum(rho)==1
    assert all(sum(row)==1 for row in p)
    assert len(set(alpha))==7 and all(0<a<1 for a in alpha)
    return alpha,b,z,rho,p


def exact_moments(p,rho,ns):
    """For each proper nonneutral mask, sum W_u rho_D^T P_D^(n-1) 1."""
    scale_p = lcm(*(v.denominator for row in p for v in row))
    scale_rho = lcm(*(v.denominator for v in rho))
    h = tuple(tuple(int(scale_p*v) for v in row) for row in p)
    states=[]
    for mask in range(63):
        d=(0,)+tuple(j for j in range(1,7) if mask & (1 << (j-1)))
        h_d=tuple(tuple(h[i][j] for j in d) for i in d)
        state=tuple(int(scale_rho*rho[i]) for i in d)
        states.append((len(d)-1,h_d,state))
    denominator_power=1
    results={}
    for n in range(1,max(ns)+1):
        if n in ns:
            integer_total=sum(WEIGHTS[u]*sum(v) for u,_,v in states)
            results[n]=F(integer_total, scale_rho*denominator_power)
        if n==max(ns): break
        states=[(u,h_d,tuple(sum(vec[i]*h_d[i][j]
                                 for i in range(len(vec)))
                              for j in range(len(vec))))
                for u,h_d,vec in states]
        denominator_power*=scale_p
    return results,scale_p


def leading_root_and_amplitude_bounds(alpha,b,z):
    retained=(0,1,2,4,5,6)
    def secular(x):
        return sum((b[j]/(x-alpha[j]) for j in retained),F(0))-1
    q=ROOT_DENOMINATOR
    lo=99*q//100
    hi=991*q//1000
    assert secular(F(lo,q))>0 and secular(F(hi,q))<0
    while hi-lo>1:
        mid=(lo+hi)//2
        if secular(F(mid,q))>0: lo=mid
        else: hi=mid
    lower,upper=F(lo,q),F(hi,q)
    assert secular(lower)>0 and secular(upper)<0
    def sfun(x):
        return sum((b[j]/((1-alpha[j])*(x-alpha[j]))
                    for j in retained),F(0))
    def qfun(x):
        return sum((b[j]/(x-alpha[j])**2 for j in retained),F(0))
    amplitude_lower=WEIGHTS[5]*sfun(upper)**2/(z*qfun(lower))
    amplitude_upper=WEIGHTS[5]*sfun(lower)**2/(z*qfun(upper))
    assert 0<amplitude_lower<amplitude_upper
    return lower,upper,amplitude_lower,amplitude_upper,lo,hi


def ratio_digest(x):
    return sha256((str(x.numerator)+'/'+str(x.denominator)).encode()).hexdigest()


def certify(s, horizons):
    alpha,b,z,rho,p=parameters(s)
    n1,n2=horizons
    to_check=(n1-1,n1,n2-1,n2)
    moments,den=exact_moments(p,rho,to_check)
    lower,upper,alow,aup,lo,hi=leading_root_and_amplitude_bounds(alpha,b,z)
    certificates=[]
    for d,n in ((100,n1),(1000,n2)):
        # E_n < 1/d iff d*Phi_n < (d+1)*A*r^(n-1).
        # Lower/upper for A*r^(n-1) ensure strict signs.
        below = d*moments[n] < (d+1)*alow*lower**(n-1)
        before = d*moments[n-1] > (d+1)*aup*upper**(n-2)
        assert below and before, (s,n,d,below,before)
        certificates.append({
            'target_relative_error':f'1/{d}',
            'first_integer_n':n,
            'n_minus_1_rigorous_gt_target':before,
            'n_rigorous_lt_target':below,
            'moment_n_sha256':ratio_digest(moments[n]),
            'moment_predecessor_sha256':ratio_digest(moments[n-1]),
            'moment_n_bits':[moments[n].numerator.bit_length(),
                             moments[n].denominator.bit_length()],
        })
    return {
        's':f'{s.numerator}/{s.denominator}',
        'open_interval_status':'boundary_extension' if s!=F(2,5) else 'interior',
        'matrix_denominator':den,
        'root_lower_numerator_per_10pow30':str(lo),
        'root_upper_numerator_per_10pow30':str(hi),
        'root_signs':'f(lower)>0>f(upper)',
        'verified_first_horizons':certificates,
    }


def main():
    certs=[certify(s,h) for s,h in CASES]
    result={
        'schema':'EM_R242_EXACT_ANCHOR_HORIZONS_V1',
        'result':'PASS',
        'arithmetic':'Python Fraction and integer arithmetic only',
        'scope':'three rational s values in closure of (39/100,41/100)',
        'spectral_monotonicity':'positive subleading modes imply E_(n+1)<E_n for all n>=2',
        'root_interval_scale':str(ROOT_DENOMINATOR),
        'cases':certs,
        'independent_review':'NOT_REVIEWED',
        'native_BRC':'NOT_EXECUTED',
    }
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))


if __name__=='__main__': main()
