#!/usr/bin/env python3
"""Stage248 exact horizon classification for separate caps; stdlib only."""
from fractions import Fraction as F
from itertools import product
from math import factorial

P=(F(3,24),F(1,24),F(20,24))
Q=(F(2,24),F(2,24),F(20,24))
a,b=F(3,10),F(19,40)

def mult(n,x,y):
    return factorial(n)//(factorial(x)*factorial(y)*factorial(n-x-y))

def mass_count(n,x,y,R):
    return mult(n,x,y)*R[0]**x*R[1]**y*R[2]**(n-x-y)

def tv_counts(n):
    return sum((abs(mass_count(n,x,y,P)-mass_count(n,x,y,Q))/2
                for x in range(n+1) for y in range(n+1-x)),F(0))

def tv_ordered(n):
    return sum((abs(_weight(xs,P)-_weight(xs,Q))/2
                for xs in product(range(3),repeat=n)),F(0))

def _weight(xs,R):
    t=F(1)
    for x in xs:t*=R[x]
    return t

def coin(p,q):
    return F(1) if p>q else (F(3,4) if p==q else F(0))

def n9_counts():
    ep=eq=F(0)
    for x in range(10):
        for y in range(10-x):
            pp=mass_count(9,x,y,P);qq=mass_count(9,x,y,Q)
            c=coin(pp,qq)
            ep+=pp*(1-c)
            eq+=qq*c
    return ep,eq

def n9_full_ordered():
    ep=eq=F(0)
    for xs in product(range(3),repeat=9):
        pp=_weight(xs,P);qq=_weight(xs,Q)
        c=coin(pp,qq)
        ep+=pp*(1-c)
        eq+=qq*c
    return ep,eq

TV8=tv_counts(8)
assert TV8==tv_ordered(8)==F(24591244757,110075314176)
assert F(9,40)-TV8==F(878504663,550376570880)>0
E9=n9_counts()
assert E9==n9_full_ordered()==(F(16038379873,55037657088),F(604628965,1289945088))
assert a-E9[0]==F(2364586267,275188285440)>0
assert b-E9[1]==F(40474759,6449725440)>0

# N=13 TV-sharp construction: first non-2, time-zero activation w,
# and no-signal Q-guess probability q=3/4. Analytical and ordered
# positive-branch DFS observers agree with Stage247's exact formulas.
n=13;s=4*(1-a-b);w=s/(1-F(5,6)**n);q=F(3,4)
assert w==F(58773123072,59199954455)
leaves=[('time0',0,'P',(1-w)*(1-q),(1-w)*(1-q)),
        ('time0',0,'Q',(1-w)*q,(1-w)*q)]
def visit(prefix,depth,pp,qq):
    if depth==n:
        leaves.append((prefix,depth,'P',pp*(1-q),qq*(1-q)))
        leaves.append((prefix,depth,'Q',pp*q,qq*q))
        return
    for x in range(3):
        p2=pp*P[x];q2=qq*Q[x];h=prefix+str(x)
        if x==0:leaves.append((h,depth+1,'P',p2,q2))
        elif x==1:leaves.append((h,depth+1,'Q',p2,q2))
        else:visit(h,depth+1,p2,q2)
visit('',0,w,w)
assert len(leaves)==2*n+4==30
assert sum((v[3] for v in leaves),F(0))==sum((v[4] for v in leaves),F(0))==1
obs=(sum((pp for h,t,d,pp,qq in leaves if d=='Q'),F(0)),
     sum((qq for h,t,d,pp,qq in leaves if d=='P'),F(0)),
     sum((t*pp for h,t,d,pp,qq in leaves),F(0)),
     sum((t*qq for h,t,d,pp,qq in leaves),F(0)))
assert obs==(a,b,F(27,5),F(27,5))
assert 1-F(5,6)**12-s==-F(132311957,10883911680)
assert 1-F(5,6)**13-s==F(426831383,65303470080)>0
print('STAGE248_MIN_HORIZON_EXACT_PASS')
print('TV_8=',TV8,'cap_signal_requirement=',F(9,40),'strict_deficit=',F(9,40)-TV8,'ordered_8=',3**8)
print('N9 terminal-LR rule: eP,eQ=',E9,'P_margin=',a-E9[0],'Q_margin=',b-E9[1],'ordered_9=',3**9)
print('N13 first-non2: w=',w,'q=',q,'eP,eQ,tP,tQ=',obs,'source_leaves=',len(leaves))
print('N12 sharpness_obstruction=',s-(1-F(5,6)**12))
print('horizon_classification: N<=8 INFEASIBLE; N=9..12 FEASIBLE_NONSHARP; N>=13 SHARP_V=27/5')
