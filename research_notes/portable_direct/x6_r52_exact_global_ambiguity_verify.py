#!/usr/bin/env python3
"""R52: independent exact Fraction verification of the p=4 global ambiguity threshold.

Conditional R44/R47 positive BRC observer; no native P000 event admission assumed.
"""
from fractions import Fraction as Q
from itertools import product
import json


def masses(p, s, prod):
    assert p >= 1 and s > 0 and prod > 0 and 4 * prod <= s*s
    return (p*s, (p-1)*s, 2*(p*p-1)*prod, 2*p*prod)


def contrast_coefficients(q):
    c=q*q-q-1
    return (Q(-c*(q-1),q), Q(c), Q(1), Q(-1)-Q(c,q))


def contrast(q,v):
    return sum((u*x for u,x in zip(contrast_coefficients(q),v)),Q(0))


def ell1(q):
    return sum(map(abs,contrast_coefficients(q)))


def main():
    p=4; s=Q(1); prod=Q(99,10000)
    real=masses(p,s,prod)
    q=5; sr=Q(402921,500000); pr=Q(10841,1000000)
    rival=masses(q,sr,pr)
    bias=Q(-126289,1000000)
    observed=tuple((a+b+bias)/2 for a,b in zip(real,rival))
    eta=Q(97079,2000000)
    assert sr*sr-4*pr == Q(151504332241,250000000000) > 0
    assert tuple(z-a for z,a in zip(observed,real))==(-eta,eta,eta,-eta)
    assert tuple(z-a-bias for z,a in zip(observed,rival))==(eta,-eta,-eta,eta)
    assert contrast(q,rival)==0
    assert ell1(q)==Q(40)
    assert abs(contrast(q,real))==Q(97079,25000)
    assert abs(contrast(q,real))/(2*ell1(q)) == eta
    assert eta < Q(1,20) and eta > Q(1,8*(p+1))
    # Any two radius-eta observation boxes can meet only if the one
    # competitor's own contrast of the actual vector is <= 2eta*ell1.
    rivals=0
    for other in range(1,1001):
        if other in (p,q):
            continue
        if other==1:
            # q=1 has D-H=-2P'<0 while actual D-H positive.
            assert (real[2]-real[3])/4 > eta
        else:
            c=other*other-other-1
            assert ell1(other)==2*other*(other-1)
            exact=Q(abs(p-other),other)*(s*c+2*prod*(p*other+1))
            assert abs(contrast(other,real))==exact
            lower=Q(abs(p-other)*c,4*other*(c+1))
            assert lower>eta
            assert abs(contrast(other,real))/(2*ell1(other))>=lower
        rivals+=1
    # Closed-form infinite tail: monotone for q>=6 (two increasing factors).
    q6_lower=Q((6-p)*(6*6-6-1),4*6*(6*6-6))
    assert q6_lower==Q(29,360)>eta
    assert Q(5,72)>eta and Q(1,8)>eta
    assert (real[2]-real[3])/4 == Q(1089,20000)>eta
    return {
        'schema':'X6_R52_EXACT_GLOBAL_AMBIGUITY_CERTIFICATE_V1',
        'status':'PASS',
        'scope':'conditional R44 BRC rooted four-observation vector; p=4,S=1,P=99/10000; all positive competitor q and arbitrary common bias',
        'optimal_radius':str(eta),
        'uniqueness':'all errors eta<critical force p=4',
        'boundary':'at eta=critical, q=5 exact positive-weight ambiguity exists',
        'true':{'p':p,'S':str(s),'P':str(prod),'bias':'0','root':list(map(str,real))},
        'rival':{'q':q,'S':str(sr),'P':str(pr),'bias':str(bias),'root':list(map(str,rival)),'weight_discriminant':str(sr*sr-4*pr)},
        'shared_observation':list(map(str,observed)),
        'offset_robust_q5_lower':str(abs(contrast(q,real))/(2*ell1(q))),
        'all_other_ports_symbolic_certificate':{
            'q1_sign_threshold':str((real[2]-real[3])/4),
            'q2_lower':str(Q(1,8)),
            'q3_lower':str(Q(5,72)),
            'q_ge_6_monotone_lower':str(q6_lower)},
        'rival_port_instances_exact_checked':rivals,
        'rival_q_checked':'1..1000 excluding p=4,q=5',
        'universal_q_ge_6':'symbolic monotonicity proof; finite q scan is corroboration',
        'proof_status':'AUTHOR_PROOF_AND_EXACT_FRACTION_CHECK; NOT_INDEPENDENTLY_REVIEWED',
        'native_P000':'NO_NATIVE_R_T_ADMISSION_MAPPING_CLAIMED'
    }


if __name__ == '__main__':
    print(json.dumps(main(),indent=2,ensure_ascii=False,sort_keys=True))
