"""Exact rational verification for R5 conditional kernel strike tomography.

This is an external two-measure sequential-observation toy model, not
an execution of X6 heartbeat native evolution.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

S = lambda n,d=1: F(n,d)
Y=(S(1,2),S(1),S(3,2))
KA=(S(1,4),S(1,2),S(1,4))
KB=(S(1,8),S(3,4),S(1,8))
q1={'A':S(1,2),'B':S(1,2)}
r1={'A':S(1,2),'B':S(3,2)}
q2={'AU':S(1,6),'AV':S(1,3),'BU':S(1,4),'BV':S(1,4)}
r2={'AU':S(1),'AV':S(1,4),'BU':S(1),'BV':S(2)}
child={'AU':tuple(zip(Y,KA)), 'AV':((S(1,4),S(1)),),
       'BU':tuple(zip(Y,KB)), 'BV':((S(2),S(1)),)}

assert sum(q1.values())==1
assert sum(q1[z]*r1[z] for z in q1)==1
assert all(sum(p for _,p in v)==1 for v in child.values())
assert all(sum(p*y for y,p in v)==r2[h] for h,v in child.items())
assert q2['AU']+q2['AV']==q1['A']
assert q2['BU']+q2['BV']==q1['B']
assert sum(q2.values())==1
assert sum(q2[h]*r2[h] for h in q2)==1
leaves=[(h,j,q2[h]*p,q2[h]*p*y,y)
        for h,ys in child.items() for j,(y,p) in enumerate(ys)]
assert len(leaves)==8
assert all(q>0 and p>0 for _,_,q,p,_ in leaves)
assert sum(q for _,_,q,p,_ in leaves)==sum(p for _,_,q,p,_ in leaves)==1

# Stop-loss curve and discrete inversion.
def G(probs,k):
    r=sum(p*y for p,y in zip(probs,Y))
    return min(r,k)-sum(p*min(y,k) for p,y in zip(probs,Y))
assert sum(p*y for p,y in zip(KA,Y))==sum(p*y for p,y in zip(KB,Y))==1
assert [G(KA,y) for y in Y]==[S(0),S(1,8),S(0)]
assert [G(KB,y) for y in Y]==[S(0),S(1,16),S(0)]

def recover(p):
    r=sum(a*y for a,y in zip(p,Y))
    calls=[G(p,k)+max(r-k,0) for k in Y]
    tail=[-(calls[j+1]-calls[j])/(Y[j+1]-Y[j]) for j in range(len(Y)-1)]
    return tuple([1-tail[0]]+[tail[j-1]-tail[j] for j in range(1,len(tail))]+[tail[-1]])
assert recover(KA)==KA and recover(KB)==KB

k=S(9,10);s=S(7,100)
wA=q2['AU'];wB=q2['BU'];W=wA+wB
ga=G(KA,k);gb=G(KB,k)
assert (ga,gb)==(S(1,10),S(1,20))
assert s==(wA*ga+wB*gb)/W
conditional_full_gain=wA*max(ga-s,0)+wB*max(gb-s,0)
conditional_lr_gain=max(wA*(ga-s)+wB*(gb-s),0)
assert (conditional_full_gain,conditional_lr_gain)==(S(1,200),S(0))
assert conditional_full_gain-conditional_lr_gain == wA*wB/W*(ga-gb)

# Exhaust all pure full-history policies; prefix pruning avoids meaningless
# unreachable suffix choices. At t1 choose P/Q or continue with t2 policies.
# At t2 choose P/Q or continue with 2**(number of children) terminal declarations.
def hist_choices(h):
    return [('S','P'),('S','Q')]+[('C',d) for d in product('PQ',repeat=len(child[h]))]

def root_choices(root):
    h0=root+'U';h1=root+'V'
    return [('S','P'),('S','Q')]+[
        ('C', a,b) for a,b in product(hist_choices(h0),hist_choices(h1))]

zero=(S(0),)*4

def plus(a,b):return tuple(x+y for x,y in zip(a,b))

def stop(q,r,t,action):
    return (q*r*S(action=='Q'),q*S(action=='P'),q*r*t,q*t)

def follow_hist(h,twochoice):
    if twochoice[0]=='S':return stop(q2[h],r2[h],2,twochoice[1])
    acc=zero
    for (y,p),a in zip(child[h],twochoice[1]):acc=plus(acc,stop(q2[h]*p,y,3,a))
    return acc

def follow_root(root,choice):
    if choice[0]=='S':return stop(q1[root],r1[root],1,choice[1])
    return plus(follow_hist(root+'U',choice[1]),follow_hist(root+'V',choice[2]))

# Analyze full policy class exactly, enumerate all choices independently.
la=(S(1),k,S(0),s)
la_star=(S(406),S(489),S(35),S(-14))
def value(o):return sum(a*b for a,b in zip(la,o))
def value_star(o):return sum(a*b for a,b in zip(la_star,o))
rootA=[follow_root('A',a) for a in root_choices('A')]
rootB=[follow_root('B',b) for b in root_choices('B')]
full_vals=[value(plus(a,b)) for a,b in product(rootA,rootB)]
full_min=min(full_vals)
full_options=[(value_star(plus(a,b)),plus(a,b),ca,cb) for ca,a in zip(root_choices('A'),rootA) for cb,b in zip(root_choices('B'),rootB)]
full_star_min, full_star_vec, full_A_choice, full_B_choice = min(full_options,key=lambda x:x[0])

# LR policy shares the two AU/BU signatures. Terminal declaration is a
# function only of terminal (t=3,R), not of the full hidden path.
term_y=tuple(sorted(set(y for h,ys in child.items() for y,_ in ys)))
assert len(term_y)==5
stopcont='PQC'
min_lr=None
min_lr_star=None
lr_star_vec=None
lr_star_policy=None
checked=0
for terminal_actions in product('PQ',repeat=len(term_y)):
    d3=dict(zip(term_y,terminal_actions))
    for mid_actions in product(stopcont,repeat=3):
        d2={S(1):mid_actions[0],S(1,4):mid_actions[1],S(2):mid_actions[2]}
        for root_actions in product(stopcont,repeat=2):
            d1={'A':root_actions[0],'B':root_actions[1]}
            out=zero
            for root in 'AB':
                if d1[root]!='C':
                    out=plus(out,stop(q1[root],r1[root],1,d1[root]));continue
                for suffix in 'UV':
                    h=root+suffix
                    action=d2[r2[h]]
                    if action!='C':
                        out=plus(out,stop(q2[h],r2[h],2,action));continue
                    for y,p in child[h]:
                        out=plus(out,stop(q2[h]*p,y,3,d3[y]))
            checked+=1
            v=value(out)
            if min_lr is None or v<min_lr:min_lr=v
            vs=value_star(out)
            if min_lr_star is None or vs<min_lr_star:
                min_lr_star=vs;lr_star_vec=out;lr_star_policy=(d1.copy(),d2.copy(),d3.copy())

assert len(rootA)==42 and len(rootB)==42
assert len(full_vals)==1764 and checked==7776
assert full_min==min_lr==S(77,100)
assert full_star_min==S(364) and min_lr_star==S(731,2)
assert min_lr_star-full_star_min==S(3,2)
assert value_star(full_star_vec)==full_star_min
assert value_star(lr_star_vec)==min_lr_star
assert value(plus(stop(S(1,2),S(1,2),1,'Q'),
                  stop(S(1,2),S(3,2),1,'P')))==S(77,100)

print('FINITE_SUPPORT',tuple(map(str,Y)))
print('KERNEL_A',tuple(map(str,KA)))
print('KERNEL_B',tuple(map(str,KB)))
print('POSITIVE_LEAVES',len(leaves),'P_Q_TOTALS',1,1)
print('STOP_LOSS_AT_SUPPORT_A',tuple(str(G(KA,y)) for y in Y))
print('STOP_LOSS_AT_SUPPORT_B',tuple(str(G(KB,y)) for y in Y))
print('RECOVERY_EXACT',recover(KA)==KA and recover(KB)==KB)
print('TEST_STRIKE',k,'TEST_PRICE',s,'WEIGHTS',wA,wB)
print('GA_GB',ga,gb)
print('CONDITIONAL_FULL_IMPROVEMENT',conditional_full_gain)
print('CONDITIONAL_LR_IMPROVEMENT',conditional_lr_gain)
print('CONDITIONAL_GAP',conditional_full_gain-conditional_lr_gain)
print('UNRESTRICTED_FULL_PURE_STRATEGIES',len(full_vals))
print('UNRESTRICTED_LR_PURE_DESCRIPTIONS',checked)
print('GLOBAL_FULL_MIN',full_min)
print('GLOBAL_LR_MIN',min_lr)
print('GLOBAL_GAP',min_lr-full_min)
print('SIGNED_DIRECTION',tuple(map(str,la_star)))
print('SIGNED_FULL_MIN',full_star_min)
print('SIGNED_LR_MIN',min_lr_star)
print('SIGNED_GAP',min_lr_star-full_star_min)
print('FULL_WITNESS',tuple(map(str,full_star_vec)))
print('LR_WITNESS',tuple(map(str,lr_star_vec)))
print('FULL_WITNESS_ACTIONS',repr((full_A_choice,full_B_choice)))
print('LR_WITNESS_ACTIONS',repr(lr_star_policy))
print('ALL EXACT CHECKS PASSED')
