"""R5 K3 exact four-source subdiagonal ratio dispersion certificate.

All arithmetic is fractions.Fraction; complete deterministic hull support enumeration.
The analytical all-real quantifier is proved in RESEARCH.md.
"""
from fractions import Fraction as Q
from itertools import product

C = (Q(1, 8), Q(1, 6), Q(1, 16), Q(3, 32))
UP_FULL = ((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0))
UP_LR = ((0,0,0),(0,1,1),(1,0,0),(1,1,0))
STAGES = ((0,0,0),(1,0,0),(1,1,0),(1,1,1))
ASSERTIONS = 0

def check(test, label):
    global ASSERTIONS
    ASSERTIONS += 1
    assert test, f"check {ASSERTIONS}: {label}"

def obs(up, stages, r, v, p, q):
    x,y,i = up
    w = (Q(1,8), Q(1-x,6), Q(y,16), Q(3*i,32))
    d = Q(y,16) + Q(3*i,32)
    m = [w[s]*STAGES[stages[s]][0] for s in range(4)]
    s = [Q(2,3)*m[j]*STAGES[stages[j]][1] for j in range(4)]
    u = [s[j]*STAGES[stages[j]][2] for j in range(4)]
    return (
        Q(107,128)-Q(21*x,128)+d/4-sum(s)/2+sum((p[j]*s[j]/8 for j in range(4)),Q(0)),
        Q(13,64)+Q(3*x,64)-d/2+sum(s)/8+sum((q[j]*s[j]/32 for j in range(4)),Q(0)),
        Q(3)+sum(m)+Q(3,2)*sum(s)+sum((r[j]*u[j] for j in range(4)),Q(0)),
        Q(3)+sum(m)/2+Q(3,8)*sum(s)+sum((v[j]*u[j]/4 for j in range(4)),Q(0)),
    )

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),Q(0))

def execute(label, r, v, p, q):
    check(all(Q(0)<v[j]<r[j]<Q(1) for j in range(4)), label+":subdiagonal")
    cr = sum((C[j]*r[j] for j in range(4)),Q(0))
    cv = sum((C[j]*v[j] for j in range(4)),Q(0))
    kappa = cv/cr
    t = kappa/4
    rho = [v[j]-kappa*r[j] for j in range(4)]
    gap = sum((C[j]*abs(rho[j]) for j in range(4)),Q(0))/12
    n=(Q(0),Q(0),-t,Q(1))
    check(Q(0)<t<Q(1,4), label+":t-range")
    check(sum((C[j]*rho[j] for j in range(4)),Q(0)) == 0, label+":balanced")
    for j in range(4):
        score1=Q(1,2)-t
        score2=Q(3,4)-2*t
        score3=score2+rho[j]/6
        check(score2>score1 and score2>0 and score3>0, label+f":stage-positive-{j}")
        check(score3-score2==rho[j]/6,label+f":stage-diff-{j}")
    # A single FULL policy realizes source-wise max, including every provenance cell.
    selection=tuple(3 if rho[j]>0 else 2 for j in range(4))
    full_w=obs((0,1,1),selection,r,v,p,q)
    fv=[obs(up,st,r,v,p,q) for up in UP_FULL for st in product(range(4), repeat=4)]
    lv=[obs(up,(stage,)*4,r,v,p,q) for up in UP_LR for stage in range(4)]
    check((len(fv),len(lv))==(1536,16),label+":coverage")
    hs_full=max(dot(n,z) for z in fv)
    hs_lr=max(dot(n,z) for z in lv)
    check(dot(n,full_w)==hs_full,label+":attained-full")
    check(hs_full-hs_lr==gap,label+":exact-gap")
    lr2=dot(n,obs((0,1,1),(2,2,2,2),r,v,p,q))
    lr3=dot(n,obs((0,1,1),(3,3,3,3),r,v,p,q))
    check(lr2==lr3==hs_lr,label+":lr-tie")
    check((gap>0)==(len(set(v[j]/r[j] for j in range(4)))>1),label+":strictness")
    # All wedge normals: exact closed form, not only the balanced canonical direction.
    wedge = (Q(1,20),Q(1,10),Q(1,8),Q(1,7),Q(1,6),Q(1,5),Q(6,25),t)
    for z in wedge:
        normal = (Q(0),Q(0),-z,Q(1))
        plus = sum((C[j]*max(Q(0),v[j]-4*r[j]*z) for j in range(4)),Q(0))
        minus = sum((C[j]*max(Q(0),4*r[j]*z-v[j]) for j in range(4)),Q(0))
        actual = max(dot(normal,f) for f in fv)-max(dot(normal,l) for l in lv)
        check(actual == min(plus,minus)/6,label+f":wedge-{z}")
        check(actual<=gap,label+f":maximum-{z}")
    dist_lower=gap/(1+t)
    print('CASE',label)
    print('r=',r,'v=',v)
    print('kappa=',kappa,'t=',t,'rho=',tuple(rho),'selected stages=',selection)
    print('W_FULL=',full_w,'signed normal=',n)
    print('h_FULL=',hs_full,'h_LR=',hs_lr,'GAP=',gap,'LINF_DISTANCE_LOWER=',dist_lower)
    print('DETERMINISTIC_POINTS',len(fv),len(lv),'ASSERTIONS_TO_NOW',ASSERTIONS)
    return {'kappa':kappa,'t':t,'gap':gap,'w':full_w,'lower':dist_lower}

h=Q(1,2)
# Source grouped, nonproportional and outside the previous V>R exposed-clock chamber.
grouped=execute('GROUPED_NONPROPORTIONAL',
    (Q(3,5),Q(3,5),Q(1,4),Q(1,4)),
    (Q(3,10),Q(3,10),Q(1,5),Q(1,5)),
    (Q(1,4),Q(1,2),Q(3,4),Q(1,3)),
    (Q(3,4),Q(1,2),Q(1,4),Q(2,3)))
check(grouped['t']==Q(19,137), 'grouped:t')
check(grouped['gap']==Q(7,4384), 'grouped:gap')
check(grouped['lower']==Q(7,4992), 'grouped:lower')
# Ungrouped inputs: all four source labels retained, no two-group cancellation assumption.
execute('UNGROUPED_NONPROPORTIONAL',
    (Q(3,5),Q(1,2),Q(2,5),Q(1,4)),
    (Q(3,10),Q(3,10),Q(1,5),Q(1,5)),
    (h,h,h,h),(h,h,h,h))
# Equal-ratio control: only the asserted *canonical direction* gap is zero.
control=execute('PROPORTIONAL_CONTROL',
    (Q(3,5),Q(3,5),Q(1,4),Q(1,4)),
    (Q(3,10),Q(3,10),Q(1,8),Q(1,8)),
    (h,h,h,h),(h,h,h,h))
check(control['gap']==0,'proportional-zero')
# Independent upstream-mask obstruction on the equal-ratio surface v=k*r.
r=(Q(3,5),Q(1,2),Q(2,5),Q(1,4)); k=Q(1,2)
v=tuple(k*z for z in r); p=q=(h,h,h,h)
mu=tuple((9+2*v[j])/(8*(3+r[j])) for j in range(4))
check(mu==(Q(1,3),Q(19,56),Q(47,136),Q(37,104)),"mask:mu")
check(mu[0]<mu[1]<mu[2]<mu[3]<Q(3,8),"mask:threshold-order")
B,J=Q(1,16),Q(3,32)
PB,PI=2+Q(2,3)*r[2],2+Q(2,3)*r[3]
t_opt=(B*PB*mu[2]+J*PI*mu[3])/(B*PB+J*PI)
check(t_opt==Q(931,2648),"mask:optimizer")
for t in (Q(7,20),t_opt):
    n=(Q(0),Q(0),t,-Q(1))
    a=tuple((2+Q(2,3)*r[j])*t-Q(3,4)-v[j]/6 for j in range(4))
    check(a[0]>=a[1]>=a[2]>0>a[3],"mask:stage-sign")
    predicted=min(B*a[2],-J*a[3])
    full_w=obs((0,1,1),(3,3,3,0),r,v,p,q)
    full_max=max(dot(n,obs(up,js,r,v,p,q)) for up in UP_FULL for js in product(range(4),repeat=4))
    lr_max=max(dot(n,obs(up,(js,)*4,r,v,p,q)) for up in UP_LR for js in range(4))
    check(dot(n,full_w)==full_max,"mask:full-optimizer")
    check(full_max-lr_max==predicted,"mask:gap")
    check(predicted>0,"mask:strict")
    print('MASK_COMMON_RATIO t=',t,'A=',a,'W_FULL=',full_w,'h_FULL=',full_max,
          'h_LR=',lr_max,'GAP=',predicted,'LINF_DISTANCE_LOWER=',predicted/(1+t))
check(min(B*((2+Q(2,3)*r[2])*Q(7,20)-Q(3,4)-v[2]/6),
          -J*((2+Q(2,3)*r[3])*Q(7,20)-Q(3,4)-v[3]/6))==Q(1,1600),"mask:simple-gap")
check(B*PB*(t_opt-mu[2])==Q(9,10592),"mask:optimal-gap")
check(Q(9,10592)/(1+t_opt)==Q(3,4772),"mask:distance")
print('ASSERTIONS_TOTAL',ASSERTIONS)
print('PASS_EXACT_R5_K3_SUBDIAGONAL_RATIO_DISPERSION')
