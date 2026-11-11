#!/usr/bin/env python3
"""PREFIX-696-R6: exact rational extension from the pinned BRC 189-row jets.

Scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
The integer jet floors are independently recomputed by PREFIX-695; the sixth
order global envelopes are from PREFIX-693. This checks deductions from those
inputs, not the underlying 189-row recurrence or native heartbeat dynamics.
"""
from fractions import Fraction as F
from math import factorial
import json

A_JET_FLOORS = (44000296, -168056589514, -6667624082229,
                39352687679231, 3189837819999830, -36266294695911132)
B_JET_FLOORS = (789752024, 12845959424, -99127959112,
                -1326952329685, -14895243921676, -1960958310350017)
A6 = 201273663850076722544640
B6 = 17896441402901698560
BASE = F(53, 1000)
H = F(1, 6250)
LEFT, RIGHT = BASE-H, BASE+H
assert LEFT == F(1321,25000) and RIGHT == F(1329,25000)


def radius_bound(floors, m6, derivative):
    """Enclose derivative of order 0,1,2 for all |z-BASE|<=H."""
    k=derivative
    rem=F(0)
    for j in range(k+1,6):
        rem += F(max(abs(floors[j]), abs(floors[j]+1)),10**8)*H**(j-k)/factorial(j-k)
    rem += F(m6)*H**(6-k)/factorial(6-k)
    return F(floors[k],10**8)-rem, F(floors[k]+1,10**8)+rem


def endpoint_bound(floors, m6, t):
    """Enclose value at BASE+t, respecting signs of coefficient intervals."""
    low=F(0); high=F(0)
    for j, floor in enumerate(floors):
        term=t**j/F(factorial(j))
        if term>=0:
            low += F(floor,10**8)*term
            high+= F(floor+1,10**8)*term
        else:
            low += F(floor+1,10**8)*term
            high+= F(floor,10**8)*term
    err=F(m6)*abs(t)**6/factorial(6)
    return low-err, high+err


A=[radius_bound(A_JET_FLOORS,A6,j) for j in range(3)]
B=[radius_bound(B_JET_FLOORS,B6,j) for j in range(3)]
# All inequalities below are exact Fraction comparisons, not float tests.
assert F('0.16')<A[0][0]<A[0][1]<F('0.72')
assert -1870<A[1][0]<A[1][1]<-1490
assert -5600000<A[2][0]<A[2][1]<5600000
assert F('7.87')<B[0][0]<B[0][1]<F('7.92')
assert 128<B[1][0]<B[1][1]<129
assert -1500<B[2][0]<B[2][1]<1500

# Q''=(B''A^2 -BAA'' -2B'AA' +2B(A')^2)/A^3.
# Since A>0, B'>0 and A'<0, the third numerator term is positive.
numerator_lower = (2*F('7.87')*1490**2
                   -F('7.92')*F('0.72')*5600000
                   -1500*F('0.72')**2)
assert numerator_lower == F(15050782,5)
assert numerator_lower>3000000
assert numerator_lower/F('0.72')**3 > 8000000

al, bl = endpoint_bound(A_JET_FLOORS,A6,-H), endpoint_bound(B_JET_FLOORS,B6,-H)
ar, br = endpoint_bound(A_JET_FLOORS,A6,H), endpoint_bound(B_JET_FLOORS,B6,H)
left_sign_lower = 12*al[0]-bl[1]
right_sign_upper = 45*ar[1]-br[0]
assert left_sign_lower > F('0.56')
assert right_sign_upper < -F('0.045')
assert al[0]>0 and ar[0]>0
# For every real q in [12,45], F_q(left)>0>F_q(right) and F'_q<0.
# Thus the root is unique, Q=B/A strictly convex and z(q)=Q^-1(q)
# strictly increasing and strictly concave throughout (12,45).

out={
 'id':'PREFIX-696-R6',
 'status':'ALL_CHECKS_PASS PREFIX696-R6',
 'frozen_scientific_input':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'predecessor_jets':'PREFIX-695', 'sixth_derivative_bound':'PREFIX-693',
 'center':str(BASE),'radius':str(H),
 'new_z_interval':[str(LEFT),str(RIGHT)],
 'q_closed_interval':['12','45'],
 'a_b_a1_b1_a2_b2_exact_enclosures': {
  name: [str(v[0]),str(v[1])] for name,v in [('A',A[0]),('B',B[0]),('A1',A[1]),('B1',B[1]),('A2',A[2]),('B2',B[2])]
 },
 'N_lower':str(numerator_lower),
 'Q2_lower':'8000000 (strict)',
 'F12_left_lower':str(left_sign_lower),
 'F45_right_upper':str(right_sign_upper),
 'checks':[
   'strict sign A>0,B>0,A1<0,B1>0 on whole J',
   'strict convexity Q2>8000000 on whole J',
   'F12(left)>0.56 and F45(right)<-0.045',
   'unique root for every real q in [12,45]',
   'strictly increasing and concave inverse on (12,45)'
 ],
 'limitations':'Author-side implication check; predecessor exact jets and global sixth-derivative envelopes are trusted inputs. No independent formal review or native physics inference.'
}
if __name__=='__main__':
    print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
