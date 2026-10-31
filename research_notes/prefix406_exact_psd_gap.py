#!/usr/bin/env python3
"""PREFIX-406: exact certificate for a robust rank-one/PSD gap.

Only the external normalized static five-Port complex-amplitude model.
This is not a P000-native or typed-BRC calculation.
"""
from fractions import Fraction as Q
import json
import sympy as sp

i = sp.I
A = sp.Matrix([
    [4, 4, 0],
    [0, -4, 4],
    [-5+3*i, 0, -3+i],
    [-2-2*i, 4+4*i, 2+2*i],
    [-2, 0, 5+2*i],
])
A3 = A[:3, :]
assert sp.simplify(A3.det() - (-32+32*i)) == 0
T = sp.simplify(A*A3.inv())
a, b, c = T[3, 0], T[3, 1], T[3, 2]
a5, b5, c5 = T[4, 0], T[4, 1], T[4, 2]
assert (a,b,c)==(sp.Rational(5,2)+sp.Rational(9,2)*i,
                 sp.Rational(3,2)+sp.Rational(7,2)*i,4*i)
assert (a5,b5,c5)==(sp.Rational(11,4)+sp.Rational(15,8)*i,
                   sp.Rational(11,4)+sp.Rational(15,8)*i,
                   sp.Rational(5,4)+sp.Rational(9,4)*i)
alpha=sp.expand(a*sp.conjugate(b))
beta=sp.expand(a*sp.conjugate(c))
gamma=sp.expand(b*sp.conjugate(c))
assert (alpha,beta,gamma)==(sp.Rational(39,2)-2*i,18-10*i,14-6*i)
assert (sp.expand(beta*sp.conjugate(beta)),sp.expand(gamma*sp.conjugate(gamma)))==(424,232)

def readouts(H):
    def obs(row):
        row=sp.Matrix([list(row)])
        return sp.simplify((row*H*row.conjugate().T)[0])
    return {
        'I2': obs([0,1,0]),'Cu': obs([1,1,0]),
        'I3': obs([0,0,1]),'Cv': obs([1,0,1]),
        'I4': obs(T.row(3)),'I5': obs(T.row(4))
    }
H0=sp.diag(1,1,0)
read=readouts(H0)
assert read=={'I2':1,'Cu':2,'I3':0,'Cv':1,'I4':41,'I5':sp.Rational(709,32)}
assert H0.rank()==2
Wp=sp.Matrix([1,i,0]);Wm=sp.Matrix([1,-i,0])
Hp=Wp*Wp.conjugate().T;Hm=Wm*Wm.conjugate().T
assert (Hp+Hm)/2==H0
assert readouts(Hp)=={'I2':1,'Cu':2,'I3':0,'Cv':1,'I4':37,'I5':sp.Rational(709,32)}
assert readouts(Hm)=={'I2':1,'Cu':2,'I3':0,'Cv':1,'I4':45,'I5':sp.Rational(709,32)}

eps=Q(1,10000)
# For any feasible PSD H, F4=41+4t+error, t=Im H12.
# From Cu, |Re H12|<=eps. PSD gives |H13|<=1/100,
# |H23|<1001/100000; |a*conj(c)|<21, |b*conj(c)|<16.
err=Q(29,2)*eps+16*eps+39*eps+2*21*Q(1,100)+2*16*Q(1001,100000)
assert err==Q(74727,100000) and err<Q(3,4)
assert Q(424)<21**2 and Q(232)<16**2
assert Q(1)+eps < Q(1001,1000)**2
# If 40<=I4<=42, then |t|<7/16.
threshold=Q(9,16)-2*eps
assert threshold==Q(5623,10000)
# Any PSD H has lambda_2(H)>=lambda_min(its first 2x2 block).
# Gershgorin + |H12|<=|ImH12|+|ReH12| gives >threshold.
# Independently check rank-one exclusion with original amplitude norms.
delta=Q(459,10000)
Eplus=14*delta+delta*delta
Eminus=18*delta+delta*delta
margin=min(Q(40)-Q(37)-Eplus,Q(45)-Eminus-Q(42))
assert Eplus==Q(64470681,100000000)
assert Eminus==Q(82830681,100000000)
assert margin==Q(217169319,100000000)>0
assert Q(1)-eps-eps*eps>Q(999,1000)**2
assert Q(1)+eps<Q(1001,1000)**2
out={
    'status':'PASS_PREFIX406_ROBUST_PSD_RANK_GAP',
    'A3_determinant':'-32+32i',
    'H0_readouts':{k:str(v) for k,v in read.items()},
    'H0_rank':2,
    'error_bound_strict_below':str(err),
    'spectral_lambda2_strict_lower_bound':str(threshold),
    'rank_one_infeasibility_margin':str(margin),
    'I4_endpoint_bounds':[str(Eplus),str(Eminus)],
    'mathematical_scope':'normalized I1=1 external static complex five-Port; six positive-width rational bands',
    'admission':'author-side exact verification only',
}
print(json.dumps(out,sort_keys=True,ensure_ascii=False,indent=2))
