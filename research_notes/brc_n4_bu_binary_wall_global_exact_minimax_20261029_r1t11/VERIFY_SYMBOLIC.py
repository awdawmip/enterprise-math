from sympy import symbols,Rational,factor
A,B,c,U,V=symbols('A B c U V')
s=(A-1+B-Rational(1,20))/2
t=(A-1+3*(B-Rational(1,20)))/4
H=B*c/4
rQ=Rational(1,6)-A*c/6-U/3-V/4
rP=Rational(1,6)-A*c/6-U/12-V/2
w=(7*(1-c)/20,(7*c-3)/20,(3*c+1)/10,(7-3*c)/10)
lhs=w[0]*(H-s-rQ)+w[1]*(H-rQ)+w[2]*rP+w[3]*(t+rP)+Rational(7,20)*(V-B)
assert factor(lhs-(33-39*c)/400)==0
assert factor(2*A*c+7*B+16*rP-4*rQ-(2+7*(B-V)))==0
print('PASS_SYMBOLIC_N4_BU_DUAL_IDENTITY')
