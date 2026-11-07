#!/usr/bin/env python3
"""Stage244: exact author-side ternary-IID N=14 all-real minimax certificate.
Standard library only; no native-X6 evolution or independent Source admission.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json

N=14
PN=(3,1,20); QN=(2,2,20)
LP=F(96950297784,1765157155)
LQ=F(104485552128,1765157155)
D=24**N
STATES=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
BASE=[24**(N-n) for n in range(N+1)]
def succ(s,j):return (s[0]+1,s[1]+(j==0),s[2]+(j==1))

@lru_cache(None)
def bell(s):
    n,a,b=s
    options={'P':LQ*F(2**(a+b),3**a),'Q':LP}
    if n<N:options['C']=F(1)+sum(F(PN[j],24)*bell(succ(s,j))[0] for j in range(3))
    best=min(options.values())
    choices=tuple(k for k in ('P','Q','C') if k in options and options[k]==best)
    return best,choices,options

H=bell((0,0,0))[0]
TIES=[(s,bell(s)[1]) for s in STATES if len(bell(s)[1])>1]
POS_GAPS=[v-bell(s)[0] for s in STATES for v in bell(s)[2].values() if v>bell(s)[0]]
assert len(STATES)==680 and len(TIES)==14 and len(POS_GAPS)==1226
assert min(POS_GAPS)==F(34069364,1765157155)
assert all(len(c)==2 for _,c in TIES)
assert [s for s,c in TIES]==[(1,1,0),(2,1,0),(2,1,1)]+[(n,1,0) for n in range(3,14)]
assert H==F(57363048204634793377,1152708874580404224)
TIE_INDEX={s:i for i,(s,_) in enumerate(TIES)}
FIXED={s:bell(s)[1][0] for s in STATES if s not in TIE_INDEX}
def act(s,mask):
    i=TIE_INDEX.get(s)
    return FIXED[s] if i is None else TIES[i][1][(mask>>i)&1]

points={}
nodes=0
for mask in range(1<<len(TIES)):
    @lru_cache(None)
    def suffix(s):
        n=s[0];a=act(s,mask)
        if a=='P':return (0,BASE[n],n*BASE[n],n*BASE[n])
        if a=='Q':return (BASE[n],0,n*BASE[n],n*BASE[n])
        child=[suffix(succ(s,j)) for j in range(3)]
        return tuple(sum((PN if i in (0,2) else QN)[j]*child[j][i] for j in range(3)) for i in range(4))
    ep,eq,tp,tq=suffix((0,0,0))
    assert F(tp,D)+LP*F(ep,D)+LQ*F(eq,D)==H
    points[mask]=(ep-eq,ep,tp,tq)
    # Independent full ordered-history DFS, no count-state merging.
    acc=[0,0,0,0];stack=[(0,0,0,1,1)]
    while stack:
        n,a,b,p,q=stack.pop();nodes+=1
        choice=act((n,a,b),mask)
        if choice=='C':
            for j in range(3):stack.append((n+1,a+(j==0),b+(j==1),p*PN[j],q*QN[j]))
        else:
            if choice=='Q':acc[0]+=p*BASE[n]
            if choice=='P':acc[1]+=q*BASE[n]
            acc[2]+=n*p*BASE[n];acc[3]+=n*q*BASE[n]
    assert tuple(acc)==(ep,eq,tp,tq),(mask,acc,(ep,eq,tp,tq))
assert nodes==1441798

seen={}
for mask,v in points.items():seen.setdefault(v[:2],mask)
xy=sorted(seen)
def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
lower=[]
for p in xy:
    while len(lower)>1 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
    lower.append(p)
upper=[]
for p in reversed(xy):
    while len(upper)>1 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
    upper.append(p)
hull=lower[:-1]+upper[:-1]
assert len(points)==16384 and len(seen)==12280 and len(hull)==4

def crossing(a,b):
    x1,y1=a;x2,y2=b
    if x1*x2>0 or x1==x2:return None
    if x1==0:return F(y1)
    if x2==0:return F(y2)
    return F(y1*(-x2)+y2*x1,x1-x2)
edges=[]
for a,b in zip(hull,hull[1:]+hull[:1]):
    z=crossing(a,b)
    if z is not None:edges.append((z,a,b))
assert len(edges)==2
edges.sort(key=lambda x:x[0])
(_,la,lb),(_,ua,ub)=edges
A,B=sorted((la,lb));C,E=sorted((ua,ub))
def margin(v,a,b):
    x,y=v;x1,y1=a;x2,y2=b
    return (y-y1)*(x2-x1)-(y2-y1)*(x-x1)
assert all(margin(v[:2],A,B)>=0 and margin(v[:2],C,E)<=0 for v in points.values())

def witness(a,b):
    m1,m2=seen[a],seen[b]
    x1,y1,tp1,tq1=points[m1]
    x2,y2,tp2,tq2=points[m2]
    w=F(-x2,x1-x2)
    assert 0<w<1 and w*x1+(1-w)*x2==0
    ep=(w*y1+(1-w)*y2)/D
    tp=(w*tp1+(1-w)*tp2)/D
    tq=(w*tq1+(1-w)*tq2)/D
    assert tp>tq and tp==H-(LP+LQ)*ep
    return {'masks':[m1,m2],'weights':[str(w),str(1-w)],'alpha':str(ep),'value':str(tp),
            'timeQ':str(tq),'time_advantage':str(tp-tq),'XY':[list(a),list(b)]}
left=witness(A,B);right=witness(C,E)
alpha243=F(4372969427965,11702381838336)
value243=F(10415008236599,1462797729792)
assert (F(left['alpha']),F(left['value']))==(alpha243,value243)
assert F(right['alpha'])==F(136710455785,365699432448)
assert F(right['value'])==F(324682148605,45712429056)
assert F(right['alpha'])-alpha243==F(1765157155,11702381838336)
assert LP+LQ<F(33611704152,292565255) # strict-right dual improvement

# Independent forward mass check for the four endpoint policies.
def forward(mask):
    inflow={(0,0,0):(F(D),F(D))};out=[F(0),F(0),F(0),F(0)]
    for s in STATES:
        p,q=inflow.get(s,(F(0),F(0)))
        if p==0 and q==0:continue
        n=s[0];choice=act(s,mask)
        if choice=='P':out[1]+=q;out[2]+=n*p;out[3]+=n*q
        elif choice=='Q':out[0]+=p;out[2]+=n*p;out[3]+=n*q
        else:
            for j in range(3):
                t=succ(s,j);u,v=inflow.get(t,(F(0),F(0)))
                inflow[t]=(u+p*PN[j]/24,v+q*QN[j]/24)
    return tuple(out)
for mask in set(left['masks']+right['masks']):
    ep,eq,tp,tq=forward(mask)
    assert (ep-eq,ep,tp,tq)==points[mask],mask

result={
 'stage':244,'classification':'AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED',
 'model':{'P_numerators':PN,'Q_numerators':QN,'denominator':24,'N':N},
 'LP':str(LP),'LQ':str(LQ),'H':str(H),'slope':str(-(LP+LQ)),
 'bellman_states':len(STATES),'ties':[{'state':list(s),'actions':list(c)} for s,c in TIES],
 'positive_gaps':len(POS_GAPS),'minimum_gap':str(min(POS_GAPS)),
 'policies':len(points),'distinct_XY':len(seen),'hull_vertices':len(hull),
 'full_ordered_DFS_nodes':nodes,'global_supports':{'lower':{'A':list(A),'B':list(B)},'upper':{'C':list(C),'D':list(E)}},
 'left':left,'right':right,'delta':str(F(right['alpha'])-alpha243),
 'strict_right_old_dual_slope_difference':str(F(33611704152,292565255)-(LP+LQ)),
 'forward_checked_masks':sorted(set(left['masks']+right['masks'])),
 'proof_scope':'Finite horizon N14 exact all-real full-history randomized policies, external IID only; no native X6 transfer.'
}
Path(__file__).with_name('CERT_STAGE244_EXACT.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('STAGE244_EXACT_AUTHOR_PASS',len(points),'ordered_nodes',nodes)
print('ALPHA',right['alpha'],'VALUE',right['value'],'WIDTH',result['delta'])
