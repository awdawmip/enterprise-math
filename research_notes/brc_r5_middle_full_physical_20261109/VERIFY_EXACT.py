#!/usr/bin/env python3
"""R5 exact proof-facing verifier for two full-real five-parameter prisms.
All 64 targets are in EXACT_SUPPORT_CERTS.txt in this same directory.
Frozen mass/time calibration is copied exactly from author-side PR #1827.
Use: python -S VERIFY_EXACT.py
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
R=tuple(map(F,('1/10','1/2','3/4','1','5/4','3/2','19/10')))
PSTAR=F(303,2450)
BOXES={
'A':((F(3,20),F(7,39)),(F(0),PSTAR),(F(0),F(1,2)),(F(0),F(1)),(F(0),F(1))),
'B':((F(3,20),F(7,39)),(F(0),PSTAR),(F(0),F(1)),(F(0),F(1)),(F(1,4),F(1)))
}
Y={}
for line in Path(__file__).with_name('EXACT_SUPPORT_CERTS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):continue
    name,bits,*coords=line.split()
    key=(name,tuple(map(int,bits)))
    assert name in BOXES and len(bits)==5 and len(coords)==7 and key not in Y
    Y[key]=tuple(map(F,coords))
assert len(Y)==64

def source(t,p,q,theta,kappa):
    return (F(1),t,F(1),(F(13,40)*t+F(1,80))*p,
            F(9,40)*kappa+t*theta/10,
            (F(3,40)*t+F(21,80))*q,t*theta/10)
def mass(f):
    g,a,b,u,v,w,z=f
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            F(13,40)*a+b/80-u,(g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def tp(f):
    g,a,b,u,v,w,z=f
    return 1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w
def tq(f):
    g,a,b,u,v,w,z=f
    return 1+g+(a+b)/2+u+v+w
def hinge(f,k):
    return sum(max(ri-k,F(0))*mi for ri,mi in zip(R,mass(f)))

def lawful(f):
    g,a,b,u,v,w,z=f
    assert 0<=a<=g<=1 and 0<=b<=g
    assert 0<=u<=F(13,40)*a+b/80
    assert 0<=w<=F(3,40)*a+F(21,80)*b
    assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
    m=mass(f)
    assert all(mi>=0 for mi in m)
    assert sum(m)==1 and sum(ri*mi for ri,mi in zip(R,m))==1

def verify(x,y):
    lawful(x); lawful(y)
    assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
    assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])
    assert tp(x)==tp(y) and tq(x)==tq(y)
    assert all(hinge(y,k)>=hinge(x,k) for k in R[1:-1])


def target(name,t,p,q,theta,kappa):
    ranges=BOXES[name]
    parameters=(t,p,q,theta,kappa)
    weights=[]
    for a,(lo,hi) in zip(parameters,ranges):
        assert lo<=a<=hi
        weights.append((a-lo)/(hi-lo))
    ans=[F(0)]*7
    for bits in product((0,1),repeat=5):
        w=F(1)
        for bit,z in zip(bits,weights):w*=z if bit else 1-z
        for i in range(7):ans[i]+=w*Y[(name,bits)][i]
    y=tuple(ans)
    verify(source(*parameters),y)
    return y

def main():
    minima=[None]*5
    for name,box in BOXES.items():
        count=0
        for bits in product((0,1),repeat=5):
            args=[pair[bit] for pair,bit in zip(box,bits)]
            x,y=source(*args),Y[(name,bits)]
            verify(x,y)
            margins=tuple(hinge(y,k)-hinge(x,k) for k in R[1:-1])
            minima=[v if old is None or v<old else old for old,v in zip(minima,margins)]
            count+=1
        print('PASS_EXACT_F_BOX_'+name+'_CORNERS',count)
    print('MIN_EXACT_HINGE_GAPS_ALL_CORNERS',','.join(map(str,minima)))
    for name,box in BOXES.items():
        for j in range(101):
            den=103
            num=[(13*j+7)%den,(17*j+11)%den,(19*j+13)%den,(23*j+17)%den,(29*j+19)%den]
            vals=tuple(lo+(hi-lo)*F(n,den) for (lo,hi),n in zip(box,num))
            target(name,*vals)
        print('PASS_EXACT_F_BOX_'+name+'_101_INTERIOR_REGRESSIONS')
    special_x=source(F(1,6),F(0),F(0),F(1),F(1,2))
    special_y=tuple(map(F,('403649/517950','462959/2071800',
        '403649/517950','455051/5524800','20479/103590',
        '279431/1841600','462959/20718000')))
    assert special_x==(F(1),F(1,6),F(1),F(0),F(31,240),F(0),F(1,60))
    verify(special_x,special_y)
    assert tuple(hinge(special_y,k)-hinge(special_x,k) for k in R[1:-1])==tuple(map(F,(
        '375781/12430800','3227713/99446400','0','94567/4143600','94567/2071800')))
    print('PASS_EXACT_SPECIAL_NON_SEEDLESS_SOURCE_T_1_6_P0_Q0_THETA1_KAPPA1_2')
    print('AUTHOR_THEOREM_R5_TWO_F_CHARTS_ALL_REAL_BY_MULTI_AFFINE_INTERPOLATION')
if __name__=='__main__': main()
