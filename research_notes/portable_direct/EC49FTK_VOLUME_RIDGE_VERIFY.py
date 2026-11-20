#!/usr/bin/env python3
"""EC49FTK exact rational consequences of EC49FTH PR #2774.

No original Bellman solver is run: this is independent postprocessing of
its published three affine D values and one affine S value.
"""
from fractions import Fraction as Q
from itertools import product

A0,A1=Q(3,4),Q(49,64)
B0,B1=Q(7,16),Q(57,128)
Z0,Z1=Q(11,16),Q(3,4)

def d_values(a,b,z):
    return (329-36*a-68*b-141*z,334-141*a-62*b-45*z,326-141*a-47*b-43*z)

def s_value(a,b,z):
    return 332-141*a-8*b-105*z

def delta(a,b,z):
    return min(d_values(a,b,z))-s_value(a,b,z)

def z23(b):
    return 4-Q(15,2)*b

def z12(a,b):
    return (105*a-6*b-5)/96

def acrit(b):
    return (77+6*b)/105

def predicted_phase(a,b,z):
    if z < z23(b): return 2 # 43 uses
    if z > z12(a,b): return 0 # 141 uses
    return 1 # 45 uses, including ties

def run():
    box=(A1-A0)*(B1-B0)*(Z1-Z0)
    bcut=Q(53,120)
    v43=(A1-A0)*(bcut-B0)*(z23(B0)-Z0)/2
    u0,u1=24*B0-7,24*B1-7
    vmid=(u1**3-u0**3)/Q(72*322560)
    v45=box-v43-vmid
    assert (box,v43,vmid,v45)==(Q(1,131072),Q(1,983040),Q(3307,10569646080),Q(66581,10569646080))
    assert (v43/box,vmid/box,v45/box)==(Q(2,15),Q(3307,80640),Q(66581,80640))

    baseline=2-54*(B0+B1)/2+60*(Z0+Z1)/2
    c43=-(A1-A0)*(bcut-B0)*(z23(B0)-Z0)**2/Q(3)
    cmid=-(u1**4-u0**4)/Q(96*3870720)
    mean=baseline+(c43+cmid)/box
    assert baseline==Q(2725,128)
    assert c43/box==-Q(1,360)
    assert cmid/box==-Q(152191,12386304)
    assert mean==Q(1317531013,61931520)

    for i,j,k in product(range(17),repeat=3):
        a=A0+(A1-A0)*Q(i,16)
        b=B0+(B1-B0)*Q(j,16)
        z=Z0+(Z1-Z0)*Q(k,16)
        candidates=d_values(a,b,z)
        assert candidates[predicted_phase(a,b,z)]==min(candidates), (i,j,k)
        assert z12(a,b)>z23(b)
        assert z12(a,b)>Z0
        assert z23(b)<Z1
        gaps=(-3+105*a-60*b-36*z,2-54*b+60*z,-6-39*b+62*z)
        assert delta(a,b,z)==min(gaps)

    for i,j in product(range(17),repeat=2):
        a=A0+(A1-A0)*Q(i,16)
        b=B0+(B1-B0)*Q(j,16)
        peak=min(Z1,z12(a,b))
        assert Z0<peak<=Z1
        predicted=((525*a-462*b-9)/8 if a<=acrit(b) else 47-54*b)
        assert delta(a,b,peak)==predicted
        for k in range(17):
            z=Z0+(Z1-Z0)*Q(k,16)
            assert delta(a,b,z)<=predicted
    assert 105*A0+714*B0-389==Q(17,8)
    print('EXACT_RATIONAL_REGRESSION_PASS')
    for title,val in [('box',box),('vol_D43',v43),('vol_D45',v45),('vol_Dmid',vmid),
                      ('fraction_D43',v43/box),('fraction_D45',v45/box),
                      ('fraction_Dmid',vmid/box),('mean_gap',mean),
                      ('base_mean',baseline),('D43_mean_correction',c43/box),
                      ('Dmid_mean_correction',cmid/box)]:
        print(title,str(val))
    print('rational_phase_grid_points',17**3)
    print('rational_ridge_grid_pairs',17**2)

if __name__=='__main__':
    run()
