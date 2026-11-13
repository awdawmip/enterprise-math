from fractions import Fraction as F
from itertools import product

C = (F(1,8),F(1,6),F(1,16),F(3,32))
S = ('C','I','BJ','IJ')
assert sum(C)==F(43,96)


def observer(x,y,i, stages,r,v,p,q):
    x,y,i=map(F,(x,y,i))
    d=y/16+3*i/32
    w=(F(1,8), (1-x)/6, y/16, 3*i/32)
    M=[]; SS=[]; U=[]
    for s,(ww,j) in enumerate(zip(w,stages)):
        if j==0: mm=ss=uu=F(0)
        elif j==1: mm=ww;ss=uu=F(0)
        elif j==2: mm=ww;ss=F(2,3)*ww;uu=F(0)
        elif j==3: mm=ww;ss=F(2,3)*ww;uu=ss
        M.append(mm);SS.append(ss);U.append(uu)
    ep=F(107,128)-F(21,128)*x+d/4-sum(SS)/2+sum(p[s]*SS[s]/8 for s in range(4))
    eq=F(13,64)+3*x/64-d/2+sum(SS)/8+sum(q[s]*SS[s]/32 for s in range(4))
    tp=3+sum(M)+F(3,2)*sum(SS)+sum(r[s]*U[s] for s in range(4))
    tq=3+sum(M)/2+F(3,8)*sum(SS)+sum(v[s]*U[s]/4 for s in range(4))
    return (ep,eq,tp,tq)

FULL_UP=[(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0)]
LR_UP=[(0,0,0),(0,1,1),(1,0,0),(1,1,0)]

def vectors(r,v,p,q):
    full=[(up,st,observer(*up,st,r,v,p,q)) for up in FULL_UP for st in product(range(4),repeat=4)]
    lr=[(up,(j,)*4,observer(*up,(j,)*4,r,v,p,q)) for up in LR_UP for j in range(4)]
    assert len(full)==1536 and len(lr)==16
    return full,lr

def dot(a,b):return sum(x*y for x,y in zip(a,b))

def examine(high_group, eps=F(1,4096)):
    high=set(high_group)
    r=tuple(F(4,5) if s in high else F(1,5) for s in S)
    v=tuple(t/2 for t in r)
    p=(F(1,4),F(1,2),F(3,4),F(1,3))
    q=(F(3,4),F(1,2),F(1,4),F(2,3))
    full,lr=vectors(r,v,p,q)
    a=(F(0),F(0),F(1,3),F(-1))
    hF=max(dot(a,z) for _,_,z in full)
    hL=max(dot(a,z) for _,_,z in lr)
    assert hF==hL
    lr_exposed=[(up,st,z) for up,st,z in lr if dot(a,z)==hL]
    assert len(lr_exposed)==1, lr_exposed
    H=lr_exposed[0][2]
    full_w=(0,1,1)
    st=tuple(3 if s in high else 0 for s in S)
    W=observer(*full_w,st,r,v,p,q)
    assert dot(a,W)==hL
    residual=tuple(W[j]-H[j] for j in range(4))
    expect= (F(5,128),-F(5,64),F(0),F(0)) if high=={'C','I'} else (F(3,16),-F(3,32),F(0),F(0))
    assert residual==expect,(residual,expect)
    n=(eps,F(0),F(1,3),F(-1))
    lr_scores=[dot(n,z) for _,_,z in lr]
    max_lr=max(lr_scores)
    assert dot(n,H)==max_lr
    max_full=max(dot(n,z) for _,_,z in full)
    W_score=dot(n,W)
    assert max_full>=W_score>max_lr
    gap_lower=W_score-max_lr
    assert gap_lower==eps*expect[0]
    true_gap=max_full-max_lr
    dist_lower=gap_lower/sum(abs(a) for a in n)
    assert dist_lower>0
    print('HIGH_GROUP',','.join(sorted(high)))
    print('LR exposed up, stages',lr_exposed[0][0],lr_exposed[0][1])
    print('H=',H)
    print('W=',W)
    print('W-H=',residual)
    print('clock_support=',hL)
    print('mixed_normal=',n)
    print('full_support=',max_full,'LR_support=',max_lr)
    print('W_score=',W_score,'witness_surplus=',gap_lower,'full_support_gap=',true_gap)
    print('distance_bound=',dist_lower)
    return true_gap,dist_lower

if __name__=='__main__':
    examine({'C','I'})
    examine({'C','BJ'})
    print('PASS_EXACT_R5_K3_TWO_LEVEL_HIGH_MASK_FIBERS')
