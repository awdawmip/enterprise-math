#!/usr/bin/env python3
"""Exact rational checks for the frozen R5 four-stage P/Q observer."""
from fractions import Fraction as F
R=(F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
B=F(3761,36000)
def calc(g,a,b,u,v,w,z,legal=True):
    c0=F(13,40)*a+b/80
    c1=a/10+F(9,40)*b
    c2=F(3,40)*a+F(21,80)*b
    tp=1+g+(3*a+5*b)/8+u/2+v+F(3,2)*w
    tq=1+g+(a+b)/2+u+v+w
    m0=F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100
    m6=u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w
    S=(g-a,g-b,c0-u,c1-v,c2-w,F(9,40)*b-v+z)
    D0=sum((p*q for p,q in zip((S[0],S[1],S[2],S[3],S[5]),(
        F(283,4800),F(3277,72000),F(6599,18000),F(5639,36000),F(247,1620)))),F(0))
    D=sum((p*q for p,q in zip(S,(
        F(147,2000),F(1219,9000),F(6599,18000),
        F(5639,18000),F(6599,18000),F(247,810)))),F(0))
    assert B*(tq-1)-F(3401,18000)*(tp-tq)-m0==D0
    assert 2*B*(tq-1)-m0-m6==D
    if legal:
        assert 0<=a<=g<=1 and 0<=b<=g
        assert 0<=u<=c0 and 0<=v<=c1 and 0<=w<=c2
        assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
        M=(m0,c0-u,(g-a)/2,
           1-g+c1-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
           (g-b)/2,c2-w,m6)
        assert all(m>=0 for m in M)
        assert sum(M)==1 and sum(R[i]*M[i] for i in range(7))==1
        assert m0+m6<=2*B*(tq-1)
    return tp,tq,m0,m6,S
for j in range(7):
    args=[F(0)]*7;args[j]=F(1)
    calc(*args,legal=False)
print('PASS_TWO_AFFINE_IDENTITIES_ALL_SEVEN_BASIS_COEFFICIENTS')
for s in (F(0),F(1,7),F(1,3),F(7,10),F(1)):
    tp,tq,m0,m6,S=calc(s,s,s,F(27,80)*s,F(13,40)*s,F(27,80)*s,s/10)
    assert tp==tq==1+3*s and m0==m6==F(3761,12000)*s
    assert all(x==0 for x in S)
    for l in (F(0),F(1,5),F(1,2),F(1)):
        for k in (F(0),F(2,7),F(3,4),F(1)):
            E0=l*m0;E6=k*m6
            eq=E0+E6; one_minus_ep=R[0]*E0+R[6]*E6
            assert eq<=2*B*(tq-1)
            assert one_minus_ep==F(1,10)*E0+F(19,10)*E6
print('PASS_SHARP_EQUALITY_FACE_5_TIMES_80_TWO_TAIL_DECLARATIONS')
count=0
for gg in (F(1,4),F(1,2),F(1)):
 for aa in (gg/2,gg):
  for bb in (gg/3,gg):
   A=(F(13,40)*aa,aa/10,F(3,40)*aa)
   C=(bb/80,F(9,40)*bb,F(21,80)*bb)
   for fa in (F(0),F(1,3),F(1)):
    for fb in (F(1,5),F(4,5)):
     xa=[fa*x for x in A];xb=[fb*x for x in C]
     calc(gg,aa,bb,xa[0]+xb[0],xa[1]+xb[1],xa[2]+xb[2],xa[1])
     count+=1
print('PASS_EXACT_FULL_HIST_INTERIOR_POLICIES',count)
s=F(7,10)
tp,tq,m0,m6,_=calc(s,s,s,F(27,80)*s,F(13,40)*s,F(27,80)*s,s/10)
assert (tp,tq,m0,m6)==(F(31,10),F(31,10),F(26327,120000),F(26327,120000))
print('SYMMETRIC_TIME_31_OVER_10',tp,tq,m0,m6)
print('PASS_EXACT_R5_GLOBAL_TWO_TAIL_CAPACITY_AND_COMMON_RECTANGLE')
