#!/usr/bin/env python3
"""PREFIX-289: exact C4 sourced four-ordered-pair BRC checker; no float/trigonometry."""
from itertools import product

ZERO=(0,0)
ONE=(1,0)
I=(0,1)
Q=(ONE,I,(-1,0),(0,-1))

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def conj(a): return (a[0],-a[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def smul(n,a): return (n*a[0],n*a[1])
def norm(a): return a[0]*a[0]+a[1]*a[1]
def signed(a,s): return a if s==1 else neg(a)
def atom(a,j): return a[j] if 0<=j<len(a) else ZERO

def bin_arms(a,q,s,j):
    return (mul(q,atom(a,j)),signed(atom(a,j-1),s))

def brc_four_ordered_pair_mass(arms):
    total=ZERO
    for left in arms:
        for right in arms:
            total=add(total,mul(left,conj(right)))
    assert total[1]==0 and total[0]>=0
    return total[0]

def packet_test(a,q):
    z=sum(norm(x) for x in a)
    assert z>0
    output={(s,j):brc_four_ordered_pair_mass(bin_arms(a,q,s,j)) for s in (1,-1) for j in range(4)}
    assert sum(output.values())==4*z
    u=add(a[0],mul(q,a[1]))
    v=sub(mul(q,a[2]),a[1])
    e4=output[(1,1)]+output[(-1,2)]
    assert e4==norm(u)+norm(v)
    cq=conj(q)
    n=(u,sub(mul(cq,u),v),mul(cq,v)) # n = 4 (J* J) a
    s=add(sub(a[1],mul(cq,a[0])),mul(q,a[2])) # <a,Kq>, Kq=(-q,1,conj(q))
    defect16=3*z-norm(s)
    assert defect16>=0
    assert 4*e4-sum(norm(x) for x in n)==defect16 # 16 (M_E-||A a||^2)
    cn=tuple(sub(smul(4,x),y) for x,y in zip(a,n)) # 4(I-A)a
    assert 16*z-4*e4-sum(norm(x) for x in cn)==defect16
    assert 0<=e4<=3*z # P(E) <=3/4; P(E)=e4/(4*z)
    return {'input_mass':z,'E_mass_numerator_over_4':e4,
            'Ec_mass_numerator_over_4':4*z-e4,
            'kernel_inner_product':s,'defect_numerator_over_16':defect16,
            'recycled_E_mass_numerator_over_16':sum(norm(x) for x in n),
            'recycled_Ec_mass_numerator_over_16':sum(norm(x) for x in cn)}


def main():
    count=0
    pos=0
    high=0
    for a0,m1,k1,m2,k2,q in product(range(1,5),range(1,5),range(4),range(1,5),range(4),Q):
        a=(smul(a0,ONE),smul(m1,Q[k1]),smul(m2,Q[k2]))
        out=packet_test(a,q)
        count+=1
        if out['defect_numerator_over_16']>0: pos+=1
        if out['E_mass_numerator_over_4']==3*out['input_mass']: high+=1
    wa=(ONE,I,ONE)
    wb=(ONE,neg(I),ONE)
    qa=packet_test(wa,I)
    qb=packet_test(wb,I)
    assert qa['E_mass_numerator_over_4']==0
    assert qb['E_mass_numerator_over_4']==8 # P(E)=8/(4*3)=2/3
    assert qb['defect_numerator_over_16']==8 # D_E=D_Ec=8/16=1/2
    assert qb['recycled_E_mass_numerator_over_16']==24 # = 3/2
    assert qb['recycled_Ec_mass_numerator_over_16']==8 # = 1/2
    import json
    result={'scope':'FORMAL_C4_BRC_THREE_SOURCE_ONLY',
        'packets':1024,'phase_settings':4,'exact_packet_phase_cases':count,
        'direct_four_ordered_pair_brc_bins':8*count,
        'reset_loss_equalities_E_and_Ec':2*count,
        'positive_defect_cases':pos,'exact_upper_bound_cases':high,
        'witness_a':qa,'witness_b':qb,
        'formal_postmeasurement_support_ranks':{'E':2,'Ec':3,'minimal_orthogonal_outcome_carrier':5},
        'native_detector_executed':False,
        'not_admitted':True}
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
if __name__=='__main__':main()
