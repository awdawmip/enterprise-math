from fractions import Fraction as Q

G=Q(1)
u0=Q(1)
u1=Q(12,13)
X0=Q(81,520)
X1=Q(4,13)
X2=Q(0)
alpha=Q(47,180)
beta=Q(67,162)
A=u0/Q(10)
B=Q(9,40)*u1
V0=Q(13,40)*u0+u1/Q(80)
V1=A+B
V2=Q(3,40)*u0+Q(21,80)*u1
z0,z1,z2=X0/V0,X1/V1,X2/V2
assert (z0,z1,z2)==(Q(81,175),Q(1),Q(0))
assert all(Q(0)<=z<=Q(1) for z in (z0,z1,z2))
TQ=1+G+(u0+u1)/2+X0+X1+X2
TP=1+G+(3*u0+5*u1)/8+X0/2+X1+3*X2/2
assert (TP,TQ)==(Q(267,80),Q(137,40))
J=X1*(alpha*A+beta*B)/(A+B)
M={
Q(1,10):(509*X0+9*X2)/900+J,
Q(1,2):V0-X0,
Q(3,4):(G-u0)/2,
Q(1):1-G+V1+Q(382,900)*(X0+X2)-2*J,
Q(5,4):(G-u1)/2,
Q(3,2):V2-X2,
Q(19,10):(9*X0+509*X2)/900+J,
}
assert all(m>=0 for m in M.values())
assert sum(M.values())==1
assert sum(r*m for r,m in M.items())==1
ell01=Q(1787,9000)
ell05=Q(13,80)
p01=ell01/M[Q(1,10)]
p05=ell05/M[Q(1,2)]
assert (M[Q(1,10)],M[Q(1,2)],M[Q(3,2)])==(Q(93649,468000),Q(47,260),Q(33,104))
assert (p01,p05)==(Q(92924,93649),Q(169,188))
assert 0<=p01<=1 and 0<=p05<=1
eQ=ell01+ell05
eP=1-Q(1,10)*ell01-Q(1,2)*ell05
assert (eP,eQ,TP,TQ)==(Q(161801,180000),Q(6499,18000),Q(267,80),Q(137,40))
assert Q(27,80)-M[Q(3,2)]==Q(21,1040)
print('LR_SHARED_Z=',tuple(map(str,(z0,z1,z2))))
print('LR_DECLARATION_PROBS=',str(p01),str(p05))
print('LR_W=',tuple(map(str,(eP,eQ,TP,TQ))))
print('FULL_EXTRA_M_3_OVER_2=',Q(27,80),'LR_EXTRA_M_3_OVER_2=',M[Q(3,2)])
print('EXTRA_MASS_GAP=',Q(21,1040))
print('PASS_EXACT_R5_FOUR_OBSERVER_LR_RECONSTRUCTION')
