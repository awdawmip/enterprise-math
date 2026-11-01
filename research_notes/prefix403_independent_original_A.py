#!/usr/bin/env python3
"""PREFIX-403 independent original complex-matrix check.
Reconstruct A3 inverse from the unnormalized source matrix, then check
both branches and the formerly frozen-center false negative exactly.
"""
import sympy as s
R=s.Rational; i=s.I
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*i,0,-3+i],
            [-2-2*i,4+4*i,2+2*i],[-2,0,5+2*i]])
A3=A[:3,:]
assert s.simplify(A3.det()-(-32+32*i))==0
B=(A*A3.inv()).applyfunc(s.simplify)
expected=s.Matrix([[1,0,0],[0,1,0],[0,0,1],
            [R(5,2)+R(9,2)*i,R(3,2)+R(7,2)*i,4*i],
            [R(11,4)+R(15,8)*i,R(11,4)+R(15,8)*i,R(5,4)+R(9,4)*i]])
assert B==expected

def abs2(x): return s.simplify(s.expand_complex(x*s.conjugate(x)))

def obs(u,v):
    y=A3.inv()*s.Matrix([1,u,v]); z=A*y
    return [abs2(z[j]) for j in range(5)]+[abs2(1+u),abs2(1+v)]

u0=R(59,63)
up=u0+i/R(10000)
actual=obs(up,1+i)
base=obs(u0,1+i)
neg=obs(u0,1-i)
assert actual[0]==1 and actual[2]==2 and actual[-1]==5
assert actual[1]-base[1]==R(1,10**8)
assert actual[-2]-base[-2]==R(1,10**8)
assert s.simplify(actual[3]-base[3])==R(720029,200000000)
assert s.simplify(actual[3]-neg[3])==R(-262384879391,4200000000)
assert actual[4]!=base[4]
assert abs(actual[3]-base[3])<R(1,10)
assert abs(actual[4]-base[4])<R(1,10)
assert s.simplify(abs2(expected[3,1])-R(29,2))==0
assert s.simplify(abs2(expected[4,1])-R(709,64))==0
print('ORIGINAL_A_DET=',A3.det())
print('ACTUAL_I4=',actual[3])
print('ACTUAL_I5=',actual[4])
print('I4_FROZEN_BRANCH_DIFFERENCES=',actual[3]-base[3],actual[3]-neg[3])
print('PASS_PREFIX403_INDEPENDENT_ORIGINAL_A_NOISY_U_AND_TWO_V_BRANCHES')
