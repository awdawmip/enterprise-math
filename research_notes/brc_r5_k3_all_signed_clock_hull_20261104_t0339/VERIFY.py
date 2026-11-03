"""Exact, standalone Fraction regression: all-signed time hull and unique-C 4D fiber.

Finite witness suites check analytic theorems in accompanying RESEARCH.md.
No numerical tolerance, floating point, or external packages.
"""
from fractions import Fraction as F
from itertools import product, permutations, combinations

C=(F(1,8),F(1,6),F(1,16),F(3,32))
LAB=('C','I','BJ','IJ')
MASKS=(frozenset(),frozenset((0,)),frozenset((0,1)),frozenset((0,2)),frozenset(range(4)))
UP_FULL=((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0))
UP_LR=((0,0,0),(0,1,1),(1,0,0),(1,1,0))
STAGES=((0,0,0),(1,0,0),(1,1,0),(1,1,1))
CHECKS=0

def ck(cond,label):
    global CHECKS
    CHECKS+=1
    assert cond, f'assertion {CHECKS}: {label}'

def dot(n,p):return sum((x*y for x,y in zip(n,p)), F(0))

def observation(up,js,r,k,p,q):
    x,y,i=up
    w=(F(1,8),F(1-x,6),F(y,16),F(3*i,32))
    d=F(y,16)+F(3*i,32)
    m=tuple(w[j]*STAGES[js[j]][0] for j in range(4))
    s=tuple(F(2,3)*m[j]*STAGES[js[j]][1] for j in range(4))
    u=tuple(s[j]*STAGES[js[j]][2] for j in range(4))
    return (F(107,128)-F(21*x,128)+d/4-sum(s)/2+sum((p[j]*s[j]/8 for j in range(4)),F(0)),
      F(13,64)+F(3*x,64)-d/2+sum(s)/8+sum((q[j]*s[j]/32 for j in range(4)),F(0)),
      F(3)+sum(m)+F(3,2)*sum(s)+sum((r[j]*u[j] for j in range(4)),F(0)),
      F(3)+sum(m)/2+F(3,8)*sum(s)+sum((k*r[j]*u[j]/4 for j in range(4)),F(0)))

def support_formula(a,b,r,k):
    A=a+b/2
    B=2*a+F(3,4)*b
    T=F(2,3)*a+k*b/6
    if T<=0:
        v=max(F(0),A,B)
        return (3*(a+b)+sum(C)*v, 3*(a+b)+sum(C)*v)
    g=tuple(B+z*T for z in r)
    hf=3*(a+b)+sum((C[j]*max(F(0),g[j]) for j in range(4)),F(0))
    hl=3*(a+b)+max(sum((C[j]*g[j] for j in mask),F(0)) for mask in MASKS)
    return hf,hl

def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(points):
    p=sorted(set(points))
    if len(p)<3:return tuple(p)
    lo=[]
    for z in p:
        while len(lo)>=2 and cross(lo[-2],lo[-1],z)<=0:lo.pop()
        lo.append(z)
    hi=[]
    for z in reversed(p):
        while len(hi)>=2 and cross(hi[-2],hi[-1],z)<=0:hi.pop()
        hi.append(z)
    return tuple(lo[:-1]+hi[:-1])

def expected_survivor(r):
    levels=sorted(set(r),reverse=True)
    running=set()
    for value in levels[:-1]:
        running.update(j for j,z in enumerate(r) if z==value)
        if frozenset(running) not in MASKS:return False
    return True

P=(F(1,4),F(1,2),F(3,4),F(1,3))
Q=(F(3,4),F(1,2),F(1,4),F(2,3))
k=F(1,2)
# Check every exact finite deterministic hull (not just angular support sampling).
# Cases: 24 strict permutations, 14 proper two-level masks, 12 distinct three-level patterns, 1 constant.
case_rows=[]
for order in permutations((F(1,5),F(2,5),F(3,5),F(4,5))):case_rows.append(('strict',order))
for sz in (1,2,3):
    for high in combinations(range(4),sz):case_rows.append(('two',tuple(F(4,5) if j in high else F(1,5) for j in range(4))))
for bottom in combinations(range(4),2):
    top=[j for j in range(4) if j not in bottom]
    for lead in top:
        r=tuple(F(4,5) if j==lead else F(3,5) if j in top else F(1,5) for j in range(4))
        case_rows.append(('three',r))
case_rows.append(('uniform',(F(3,5),)*4))
ck(len(case_rows)==51,'test family cardinality 24+14+12+1')
counts={'strict':0,'two':0,'three':0,'uniform':0}
for cat,r in case_rows:
    full_clock=[];lr_clock=[]
    for up in UP_FULL:
        for js in product(range(4),repeat=4):
            z=observation(up,js,r,k,P,Q)
            full_clock.append(z[2:])
    for up in UP_LR:
        for j in range(4):
            z=observation(up,(j,)*4,r,k,P,Q)
            lr_clock.append(z[2:])
    ck(len(full_clock)==1536 and len(lr_clock)==16,cat+' enumeration coverage')
    HF=hull(full_clock);HL=hull(lr_clock)
    actual=HF==HL;expect=expected_survivor(r)
    ck(actual==expect,cat+' exact clock hull iff superlevel masks')
    counts[cat]+=int(actual)
    # All hull edges of BOTH convex sets provide all finite candidate support normals.
    # Testing their supporting normal values is an exact complete equality cross-check in R^2.
    normals=[]
    for H in (HF,HL):
        for m in range(len(H)):
            a,b=H[m],H[(m+1)%len(H)]
            normals.append((b[1]-a[1],a[0]-b[0]))
    for a,b in normals:
        f,l=support_formula(a,b,r,k)
        ck(f==max(a*z[0]+b*z[1] for z in HF),cat+' full analytic support on edge')
        ck(l==max(a*z[0]+b*z[1] for z in HL),cat+' LR analytic support on edge')
    if cat=='three' and expect:
        print('THREE_LEVEL_HULL_EQUAL',tuple(map(str,r)),'vertices',len(HF),'hull',tuple(tuple(map(str,z)) for z in HF))
print('COVERAGE',len(case_rows),'family_survivors',counts)

# Construct source-C exposed face and actual 4D separation with exact rational epsilon.
for which,r in (('CI_three',(F(4,5),F(3,5),F(1,5),F(1,5))),
                ('CB_three',(F(4,5),F(1,5),F(3,5),F(1,5)))):
    mu=lambda z:(9+2*k*z)/(8*(3+z))
    t=(mu(F(4,5))+mu(F(3,5)))/2
    g=tuple((2+F(2,3)*r[j])*t-F(3,4)-k*r[j]/6 for j in range(4))
    ck(0<t<F(3,8) and g[0]>0 and all(z<0 for z in g[1:]),which+' unique C time normal')
    up_full=(0,1,1);j_full=(3,0,0,0)
    W=observation(up_full,j_full,r,k,P,Q)
    H=observation((1,0,0),(3,)*4,r,k,P,Q)
    ck(W[2:]==H[2:],which+' same clock projection')
    ck(tuple(W[j]-H[j] for j in range(4))==(F(13,64),-F(1,8),0,0),which+' exact error fiber residual')
    all_lr=[observation(up,(j,)*4,r,k,P,Q) for up in UP_LR for j in range(4)]
    norm0=(F(0),F(0),t,F(-1))
    ck([z for z in all_lr if dot(norm0,z)==max(dot(norm0,u) for u in all_lr)]==[H],which+' unique clock exposed LR vertex')
    # Choose a positive epsilon below all other LR crossing ratios, without epsilon sampling.
    # H strictly wins the time face; difference in eP <=1, so eps=min positive time slack / 2.
    slacks=[dot(norm0,H)-dot(norm0,z) for z in all_lr if z!=H]
    ck(all(s>0 for s in slacks),which+' positive LR finite slack')
    eps=min(slacks)/2
    n=(eps,F(0),t,F(-1))
    hf=max(dot(n,observation(up,js,r,k,P,Q)) for up in UP_FULL for js in product(range(4),repeat=4))
    hl=max(dot(n,z) for z in all_lr)
    gap=hf-hl
    ck(dot(n,H)==hl and dot(n,W)>hl,which+' rational mixed-separation certificate')
    ck(gap>=eps*F(13,64) and gap>0,which+' certified gap at least witness score')
    inf_dist=(dot(n,W)-hl)/sum(abs(x) for x in n)
    ck(inf_dist>0,which+' positive L-infinity distance lower bound')
    print('FIBER',which,'r',tuple(map(str,r)),'t',t,'epsilon',eps,'time_scores',tuple(map(str,g)))
    print('H',tuple(map(str,H)),'W',tuple(map(str,W)),'mixed_normal',tuple(map(str,n)))
    print('h_FULL',hf,'h_LR',hl,'gap',gap,'witness_inf_distance>=',inf_dist)
print('ASSERTIONS_TOTAL',CHECKS)
print('PASS_EXACT_R5_K3_ALL_SIGNED_CLOCK_HULL_AND_C_FACE_FIBER')
