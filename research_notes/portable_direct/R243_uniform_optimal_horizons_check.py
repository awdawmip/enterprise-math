#!/usr/bin/env python3
"""R243 exact rational certificate for optimal parameter-uniform one-mode horizons.
PASS uses Fraction/integer only. Floating-point decimal output is diagnostic.
"""
from fractions import Fraction as Q
from hashlib import sha256
import json
import sys
sys.set_int_max_str_digits(100000)

L,U=Q(39,100),Q(41,100)
ETA=Q(1042768025600,8424836672439)  # R241
Q_BETA=Q(1641223,1651305)             # R241
R_LOWER=Q(990628,1000000)              # R242 left root, R236 r'>0
GAMMA=Q(977,1000)
DELTA=Q(973,1000)
SPLITS=4

def t(s):
    return (1691*s-2615)/(2615*s-3539)

def z(s):
    return 5*(4538*s-7153)/(16632*(s-1))

def static_term(j,x):
    alpha={0:Q(1,5),1:Q(1,4),2:Q(3,10),3:Q(9,20),5:Q(2,3)}[j]
    b=Q(13,60) if j==0 else Q(5,18)*abs(Q(1,2)-alpha)
    return b/(x-alpha)

def envelope_term(j,x,l,u):
    if j==4:  # source-4 secular term decreases in s for x>1/2
        return Q(5,18)*(Q(1,2)-l)/(x-l)
    if j==6:  # source-6 secular term increases in s for x>t(s)
        tt=t(u)
        return Q(5,18)*(tt-Q(1,2))/(x-tt)
    return static_term(j,x)

def source_set(mask):
    return [0]+[j for j in range(1,7) if mask & (1<<(j-1))]

def upper_secular(mask,x,l,u):
    return sum((envelope_term(j,x,l,u) for j in source_set(mask)),Q(0))-1

def main():
    assert t(L)>Q(1,2) and t(U)<Q(4,5) and t(U)>t(L)
    assert 0<R_LOWER<1 and R_LOWER>Q(99,100)
    gamma_secular=upper_secular(51,GAMMA,L,U)
    assert gamma_secular<0
    delta_parent_masks=[63-(1<<(j-1)) for j in (1,2,5,6)]
    signs=[]
    for k in range(SPLITS):
        l=L+(U-L)*k/SPLITS
        u=L+(U-L)*(k+1)/SPLITS
        for mask in delta_parent_masks:
            value=upper_secular(mask,DELTA,l,u)
            signs.append({'subinterval':k,'parent_mask':mask,
                          'strict_negative':value<0,
                          'numerator':str(value.numerator),
                          'denominator':str(value.denominator)})
            assert value<0,(k,mask,value)

    z3=Q(50,1089)
    z4_min=Q(5,18)*(Q(1,2)-U)/(1-U)**2
    z_upper=z(U)
    z_lower=z(L)
    assert z_upper>z_lower>z3+z4_min
    c_beta=Q(1681,1680)*(z_upper-z4_min)/(z_upper-z3)
    c_gamma=Q(1681,8400)
    c_rest=1/ETA
    assert 0<c_beta<1 and 0<Q_BETA<1
    assert GAMMA/R_LOWER<1 and DELTA/R_LOWER<1

    cases=[]
    for d,n in ((100,752),(1000,1128)):
        a=c_beta*Q_BETA**(n-1)
        b=c_gamma*(GAMMA/R_LOWER)**(n-1)
        c=c_rest*(DELTA/R_LOWER)**(n-1)
        full=a+b+c
        assert d*full<1
        margin=1-d*full
        cases.append({'target':f'1/{d}','uniform_first_horizon':n,
                      'upper_bound_less_target':True,
                      'upper_bound_decimal_diagnostic':format(float(full),'.14g'),
                      'positive_integer_margin':margin.numerator>0,
                      'margin_num_bits':margin.numerator.bit_length(),
                      'margin_den_bits':margin.denominator.bit_length(),
                      'margin_sha256':sha256((str(margin.numerator)+'/'+str(margin.denominator)).encode()).hexdigest(),
                      'lower_at_U_from_R242':n})

    result={'schema':'EM_R243_UNIFORM_FIRST_HORIZON_CERTIFICATE_V1',
            'status':'PASS','arithmetic':'exact Python Fraction integer cross-products',
            'domain':'39/100 < s < 41/100; boundary extension via continuity',
            'frozen_science':'awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34',
            'fixed_dependency_R242':'6427030e552a22824a5fc5a9608826890650039b',
            'gamma_upper':str(GAMMA),
            'gamma_secular_numerator':str(gamma_secular.numerator),
            'gamma_secular_denominator':str(gamma_secular.denominator),
            'delta_upper':str(DELTA),'subinterval_count':SPLITS,
            'delta_parent_signs':signs,'beta_mass_upper':str(c_beta),
            'gamma_mass_upper':str(c_gamma),'other_mass_upper':str(c_rest),
            'dominant_root_lower':str(R_LOWER),'beta_over_r_upper':str(Q_BETA),
            'cases':cases,'review':'NOT_REVIEWED','native_BRC':'NOT_EXECUTED'}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
