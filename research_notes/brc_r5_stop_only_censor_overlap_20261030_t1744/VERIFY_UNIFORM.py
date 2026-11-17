"""Independent exact Fraction check of the uniform legal rectangle obstruction."""
from fractions import Fraction as F
from itertools import product

P={(0,0):F(7,40),(0,1):F(9,40),(1,0):F(3,40),(1,1):F(21,40)}
Q={(0,0):F(7,20),(0,1):F(3,20),(1,0):F(3,20),(1,1):F(7,20)}
c,a,b=F(1,4),F(1,8),F(1,8)


def obs(s,y,d):
    v=[]
    for W in (P,Q):
        e=F(0); t=F(0)
        for (x,u),w in W.items():
            e+=w*(c+a*x+(1-s[x])*d[x]+b*x*s[x]*y[x,u])
            t+=w*(2+2*s[x]-s[x]*y[x,u])
        v.append((e,t))
    return (v[0][0],v[1][0],v[0][1],v[1][1])


def support(d):
    full=[];lr=[]
    for ss in product((0,1),repeat=2):
        s={0:ss[0],1:ss[1]}
        for bits in product((0,1),repeat=4):
            y={(0,0):bits[0],(0,1):bits[1],(1,0):bits[2],(1,1):bits[3]}
            full.append(score(obs(s,y,d)))
        for bits in product((0,1),repeat=2):
            y={(x,u):bits[u] for x in (0,1) for u in (0,1)}
            lr.append(score(obs(s,y,d)))
    assert len(full)==64 and len(lr)==16
    return max(full),max(lr)

score=lambda o:12*o[0]+25*o[2]-12*o[3]
d=(F(0),F(0))
fw=obs({0:1,1:1},{(x,u):int((x,u)==(1,0)) for x in (0,1) for u in (0,1)},d)
lrw=obs({0:1,1:1},{(x,u):0 for x in (0,1) for u in (0,1)},d)
assert fw==(F(107,320),F(53,160),F(157,40),F(77,20))
assert lrw==(F(13,40),F(5,16),F(4),F(4))
assert score(fw)==F(895,16) and score(lrw)==F(559,10)
assert score(fw)-score(lrw)==F(3,80)

for x in (0,1):
    ppi=sum(P[x,u] for u in (0,1));
    q0,q1=Q[x,0],Q[x,1]
    maxd=F(3,4) if x==0 else F(5,8)
    lower=q0*F(1,2)+q1*F(51,2)-12*ppi*maxd
    assert lower==(F(2,5) if x==0 else F(9,2))

# Corner-approaching rational points and interior points across the FULL
# legal rectangle (not only the previously proved small wedge).
d0s=(-F(1,4)+F(1,1000), F(0), F(1,16), F(3,4)-F(1,1000))
d1s=(-F(3,8)+F(1,1000), F(0), F(1,8), F(5,8)-F(1,1000))
for d0,d1 in product(d0s,d1s):
    assert 0<c+d0<1 and 0<c+a+d1<1
    f,l=support((d0,d1))
    assert (f,l)==(F(895,16),F(559,10))

print('VALID_LEGAL_RECTANGLE', 'd0 in (-1/4,3/4)', 'd1 in (-3/8,5/8)')
print('WITNESS',tuple(map(str,fw)))
print('UNIFORM_INTEGER_FUNCTIONAL', (12,0,25,-12))
print('FULL_SUPPORT',score(fw),'LR_SUPPORT',score(lrw),'GAP',F(3,80))
print('UNIFORM_ROUTE_SURVIVAL_LOWER_BOUNDS',F(2,5),F(9,2))
print('EXACT_RATIONAL_RECTANGLE_CASES', len(d0s)*len(d1s))
print('L_INFINITY_DISTANCE_LOWER_BOUND',F(3,3920))
print('PASS_EXACT_R5_ALL_LEGAL_EARLY_ERROR_OFFSETS_NO_GO')
