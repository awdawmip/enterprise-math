from fractions import Fraction as F
r=(F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
def calc(g,a,b,u,v,w,z):
    tq=1+g+(a+b)/2+u+v+w
    tp=1+g+(3*a+5*b)/8+u/2+v+F(3,2)*w
    m=u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w
    slack=(g-a,g-b,a/10+F(9,40)*b-v,F(3,40)*a+F(21,80)*b-w,F(9,40)*b-v+z)
    rhs=sum((x*y for x,y in zip(slack,(F(349,24000),F(259,2880),F(5639,36000),F(6599,18000),F(247,1620)))),F(0))
    return tp,tq,m,F(3401,18000)*(tp-1)-F(3041,36000)*(tq-1)-m-rhs,slack
for j in range(7):
    V=[F(0)]*7;V[j]=F(1)
    assert calc(*V)[3]==0
print('PASS_DUAL_AFFINE_IDENTITY_7_COEFFICIENTS')
for s in (F(0),F(1,7),F(7,10),F(1)):
    for k in (F(0),F(1,2),F(1)):
        q=F(27,80)*s*k
        tp,tq,m,zero,slacks=calc(s,s,s,q,F(13,40)*s,F(27,80)*s,s/10)
        assert zero==0 and all(v==0 for v in slacks)
        assert tq==1+F(213,80)*s+q and tp==1+F(453,160)*s+q/2
        assert m==F(7441,24000)*s+q/100
        c0=q/(F(27,80)*s) if s else F(0)
        xa=(F(13,40)*s*c0,s/10,F(3,40)*s)
        xb=(s*c0/80,F(9,40)*s,F(21,80)*s)
        assert all(F(0)<=xa[i]<=(F(13,40),F(1,10),F(3,40))[i]*s for i in range(3))
        assert all(F(0)<=xb[i]<=(F(1,80),F(9,40),F(21,80))[i]*s for i in range(3))
        M=(F(509,900)*q+F(47,180)*xa[1]+F(67,162)*xb[1]+F(27,80)*s/100,
           F(27,80)*s-q,F(0),
           1-s+F(191,450)*(q+F(27,80)*s)+F(43,90)*xa[1]+F(14,81)*xb[1],
           F(0),F(0),m)
        assert all(t>=0 for t in M) and sum(M)==1 and sum(R*t for R,t in zip(r,M))==1
print('PASS_LR_FACE_AND_QP_MOMENTS_12_RATIONAL_CASES')
for t in (F(1),F(9,5),F(31,10),F(4)):
    s=(t-1)/3
    tp,tq,m,zero,_=calc(s,s,s,F(27,80)*s,F(13,40)*s,F(27,80)*s,s/10)
    assert tp==tq==t and m==F(3761,36000)*(t-1) and zero==0
    print('DIAGONAL',t,m)
print('PASS_SHARP_SYMMETRIC_RAY_ALL_REAL_THEOREM_HAS_EXACT_CERTIFICATE')
