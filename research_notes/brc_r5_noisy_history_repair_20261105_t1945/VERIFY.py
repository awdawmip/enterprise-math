"""R5 tagged-history gate; Python 3, stdlib Fraction, exact 128-pattern sweep."""
from fractions import Fraction as F
from itertools import product
R2=(F(3,4),F(5,4)); R3=(F(1,2),F(1),F(3,2)); R4=(F(1,10),F(1),F(19,10))
q2=(F(1,2),F(1,2))
q3=((F(13,20),F(1,5),F(3,20)),(F(1,40),F(9,20),F(21,40)))
q4_common={R3[0]:(F(509,900),F(382,900),F(9,900)),R3[2]:(F(9,900),F(382,900),F(509,900))}
q4_merge={R2[0]:(F(1,90),F(44,45),F(1,90)),R2[1]:(F(67,162),F(14,81),F(67,162))}
N=(-F(1),-F(1),-F(3,25),F(1,50))
C=-F(43,40)
A=(F(1,200),-F(47,400)); U=(-F(9,500),F(49,400)); W=(F(1,2),F(1,2))
def pos(x):return max(F(0),x)
def reduced(eta):
    vals=[]
    for z0,z1 in product((0,1),repeat=2):
        t0=(1-eta)*z0+eta*z1
        t1=eta*z0+(1-eta)*z1
        vals.append(W[0]*pos(A[0]+U[0]*t0)+W[1]*pos(A[1]+U[1]*t1))
    return C+max(vals),vals
def exact_formula(eta):return C+F(1,400)+pos(F(1,400)-F(281,4000)*eta)
def obs(eta,a1,a2,a3):
    ep=eq=F(0)
    def declare(r,m):
        nonlocal ep,eq
        if r<=1:ep+=r*m
        else:eq+=m
    if not a1:
        declare(F(1),F(1));return ep,eq,F(1),F(1)
    tp=tq=F(2)
    for i,r2 in enumerate(R2):
        m2=q2[i]
        if not a2[i]:declare(r2,m2);continue
        tp+=r2*m2;tq+=m2
        for j,r3 in enumerate(R3):
            m3=m2*q3[i][j]
            tags=((F(1),-1),) if j!=1 else (((1-eta if i==0 else eta),0),((eta if i==0 else 1-eta),1))
            for pt,tag in tags:
                mm=m3*pt
                gate=a3[0 if j==0 else 3 if j==2 else 1+tag]
                if not gate:declare(r3,mm);continue
                tp+=r3*mm;tq+=mm
                row=q4_merge[r2] if j==1 else q4_common[r3]
                for r4,p in zip(R4,row):declare(r4,mm*p)
    return ep,eq,tp,tq
def score(v):return sum(n*x for n,x in zip(N,v))
def assert_rows():
    assert sum(q2)==1 and sum(x*y for x,y in zip(q2,R2))==1
    for i,r in enumerate(R2):
        assert sum(q3[i])==1 and all(p>0 for p in q3[i])
        assert sum(p*s for p,s in zip(q3[i],R3))==r
    for r,row in list(q4_common.items())+[(F(1),v) for v in q4_merge.values()]:
        assert sum(row)==1 and all(p>0 for p in row)
        assert sum(p*s for p,s in zip(row,R4))==r
    assert all(x>0 for x in q2)
assert_rows()
parameters=(F(0),F(1,1000),F(1,50),F(10,281),F(1,20),F(1,4),F(1,2))
for eta in parameters:
    assert 0<=eta<=F(1,2)
    predicted,choices=reduced(eta)
    assert predicted==exact_formula(eta)
    maximum=max(score(obs(eta,a1,a2,a3))
                for a1 in (0,1) for a2 in product((0,1),repeat=2)
                for a3 in product((0,1),repeat=4))
    assert maximum==predicted,(eta,maximum,predicted)
    assert max(choices)==max(choices[0],choices[3],choices[1],choices[2])
    gap_to_lr=predicted-(C+F(1,400))
    gap_to_full=(C+F(1,200))-predicted
    assert gap_to_lr==pos(F(1,400)-F(281,4000)*eta)
    assert gap_to_full==min(F(281,4000)*eta,F(1,400))
    print('eta=',eta,'tag_support=',predicted,'benefit_vs_LR=',gap_to_lr,
          'remaining_FULL_gap=',gap_to_full,'bayes_reduced_policies=',128)
print('EXHAUSTIVE_BAYES_REDUCED_POLICIES=',len(parameters)*128)
print('PASS_EXACT_R5_NOISY_HISTORY_REPAIR_THRESHOLD')
