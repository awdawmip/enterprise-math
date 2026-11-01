#!/usr/bin/env python3
"""Independent Fraction check of the original complex five-Port matrix and
nonzero-width six-observation YES/NO certificates (no SymPy import)."""
from fractions import Fraction as F
import json


def C(a=0,b=0): return (F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def abs2(x): return x[0]**2+x[1]**2
def div(x,y):
    z=abs2(y)
    if not z: raise ZeroDivisionError()
    p=mul(x,conj(y))
    return (p[0]/z,p[1]/z)

Z=C()
A=[
    [C(4),C(4),Z],
    [Z,C(-4),C(4)],
    [C(-5,3),Z,C(-3,1)],
    [C(-2,-2),C(4,4),C(2,2)],
    [C(-2),Z,C(5,2)],
]
B=[
    [C(1),Z,Z],
    [Z,C(1),Z],
    [Z,Z,C(1)],
    [C(F(5,2),F(9,2)),C(F(3,2),F(7,2)),C(0,4)],
    [C(F(11,4),F(15,8)),C(F(11,4),F(15,8)),C(F(5,4),F(9,4))],
]


def dot(row,vec):
    out=Z
    for x,y in zip(row,vec): out=add(out,mul(x,y))
    return out


def solve3(mat,rhs):
    aug=[list(row)+[rhs[i]] for i,row in enumerate(mat)]
    for k in range(3):
        p=next(i for i in range(k,3) if aug[i][k]!=Z)
        aug[k],aug[p]=aug[p],aug[k]
        pivot=aug[k][k]
        aug[k]=[div(z,pivot) for z in aug[k]]
        for i in range(3):
            if i==k: continue
            coefficient=aug[i][k]
            aug[i]=[sub(aug[i][j],mul(coefficient,aug[k][j])) for j in range(4)]
    return [aug[i][3] for i in range(3)]


def original_observations(u,v):
    W=[C(1),u,v]
    Y=solve3(A[:3],W)
    P=[dot(row,Y) for row in A]
    O={'I2':abs2(P[1]),'Cu':abs2(add(C(1),u)),
       'I3':abs2(P[2]),'Cv':abs2(add(C(1),v)),
       'I4':abs2(P[3]),'I5':abs2(P[4])}
    return O,P,Y


def test():
    # Check B=A(A_first3)^(-1) as a full linear identity on the basis.
    for j in range(3):
        W=[C(int(i==j)) for i in range(3)]
        Y=solve3(A[:3],W)
        for i in range(5):
            assert dot(A[i],Y)==B[i][j],(i,j)
    assert abs2(B[3][0])==F(53,2)
    assert abs2(B[3][1])==F(29,2)
    assert abs2(B[4][0])==F(709,64)
    assert abs2(B[4][2])==F(53,8)
    o0,_,_=original_observations(Z,Z)
    assert o0=={'I2':F(0),'Cu':F(1),'I3':F(0),'Cv':F(1),
                'I4':F(53,2),'I5':F(709,64)}
    # Every source |u|,|v|<=1/1000 fits six strictly positive-width
    # bands: I2,I3 [0,10^-6]; Cu,Cv [.99,1.01]; I4 [26,27]; I5 [10,12].
    # Proof: perturbation at Port4 < 8/1000, Port5 < 7/1000.
    assert F(12)*F(8,1000)+F(8,1000)**2 < F(1,2)
    assert F(8)*F(7,1000)+F(7,1000)**2 < F(7,10)
    assert F(99,100) < (1-F(1,1000))**2
    assert (1+F(1,1000))**2 < F(101,100)
    assert F(10)<o0['I5']-F(7,10) and o0['I5']+F(7,10)<F(12)
    u=C(F(1,2000),F(1,2000))
    v=C(F(1,2500),-F(1,4000))
    assert abs2(u)<F(1,1000)**2 and abs2(v)<F(1,1000)**2
    obs,ports,Y=original_observations(u,v)
    bands={'I2':(F(0),F(1,1000000)),
           'Cu':(F(99,100),F(101,100)),
           'I3':(F(0),F(1,1000000)),
           'Cv':(F(99,100),F(101,100)),
           'I4':(F(26),F(27)),
           'I5':(F(10),F(12))}
    assert all(lo<=obs[key]<=hi for key,(lo,hi) in bands.items())
    # Robust NO record: keep the five other bands, set I4 to [0,1].
    # I2,I3 upper imply |u|,|v|<=1/1000; reverse triangle gives
    # |z4|>5-8/1000=624/125>1, contradicting I4<=1.
    assert F(53,2)>F(25) and F(29,2)<F(16)
    lower=F(5)-F(8,1000)
    assert lower==F(624,125) and lower>1 and lower*lower>1
    result={'matrix_identity_basis_checked':3,
            'full_noisy_yes_source':{'u':[str(x) for x in u], 'v':[str(x) for x in v]},
            'full_noisy_yes_measurements':{k:str(z) for k,z in obs.items()},
            'full_noisy_yes_bands':{k:[str(lo),str(hi)] for k,(lo,hi) in bands.items()},
            'full_noisy_no_i4_band':['0','1'],
            'reverse_triangle_port4_lower_amplitude':str(lower),
            'nontrivial_open_source_ball_radius':'1/1000'}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    print('PASS_PREFIX404_INDEPENDENT_FRACTION_ALL_NOISY_YES_NO_AND_ORIGINAL_MATRIX')

if __name__=='__main__': test()
