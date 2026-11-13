#!/usr/bin/env python3
"""Stage245 exact 2D Bellman-optimal error polytope without 2^27 corner enumeration.
Positive integer branch weights retain P/Q distinction; 4-observation witnesses
are separately preserved. External ternary IID only. Standard library only.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json

N=14;PN=(3,1,20);QN=(2,2,20);LP=F(40);LQ=F(48);D=24**N
S=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
BASE=[24**(N-n) for n in range(N+1)]
def succ(s,j):return s[0]+1,s[1]+(j==0),s[2]+(j==1)

@lru_cache(None)
def bell(s):
    n,a,b=s
    opt={'P':LQ*F(2**(a+b),3**a),'Q':LP}
    if n<N:opt['C']=F(1)+sum(F(PN[j],24)*bell(succ(s,j))[0] for j in range(3))
    m=min(opt.values())
    return m,tuple(k for k in ('P','Q','C') if k in opt and opt[k]==m),opt

H=bell((0,0,0))[0]
ties=[(s,bell(s)[1]) for s in S if len(bell(s)[1])>1]
gaps=[v-bell(s)[0] for s in S for v in bell(s)[2].values() if v>bell(s)[0]]
assert len(S)==680 and H==40 and len(ties)==27 and len(gaps)==1213
assert min(gaps)==F(296,6561)
assert all(len(c)==2 for s,c in ties)
assert [s for s,c in ties]==[(0,0,0)]+[z for n in range(1,14) for z in ((n,0,0),(n,1,0))]

@dataclass(frozen=True)
class Point:
    ep:int;eq:int;tp:int;tq:int;trace:object=None

def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def coords_hull(points):
    """Exact ordinary 2D convex hull. Duplicate XY stores one valid lower-tQ witness."""
    unique={}
    for p in points:
        old=unique.get((p.ep,p.eq))
        if old is None or p.tq<old.tq:unique[(p.ep,p.eq)]=p
    xy=sorted(unique)
    if len(xy)<=2:return [unique[z] for z in xy]
    lower=[]
    for z in xy:
        while len(lower)>1 and cross(lower[-2],lower[-1],z)<=0:lower.pop()
        lower.append(z)
    upper=[]
    for z in reversed(xy):
        while len(upper)>1 and cross(upper[-2],upper[-1],z)<=0:upper.pop()
        upper.append(z)
    return [unique[z] for z in lower[:-1]+upper[:-1]]

# Exact convex-polytopal induction: local stop vertices and continuation
# Minkowski sums. All history-dependent policies are included; the 2D
# projection is safe only for (eP,eQ), not an unchecked 4D quotient.
polys={};tested=0
for s in reversed(S):
    n=s[0];choices=bell(s)[1];out=[]
    if 'P' in choices:out.append(Point(0,BASE[n],0,0,('P',)))
    if 'Q' in choices:out.append(Point(BASE[n],0,0,0,('Q',)))
    if 'C' in choices:
        partial=[Point(0,0,0,0,())]
        for j in range(3):
            candidates=[]
            for a in partial:
                for b in polys[succ(s,j)]:
                    candidates.append(Point(a.ep+PN[j]*b.ep,a.eq+QN[j]*b.eq,
                                            a.tp+PN[j]*b.tp,a.tq+QN[j]*b.tq,
                                            a.trace+(b,)))
            tested+=len(candidates)
            partial=coords_hull(candidates)
        for a in partial:
            out.append(Point(a.ep,a.eq,BASE[n]+a.tp,BASE[n]+a.tq,('C',a.trace)))
    polys[s]=coords_hull(out)
root=polys[(0,0,0)]
assert len(root)==16
assert all(F(p.tp,D)+LP*F(p.ep,D)+LQ*F(p.eq,D)==H for p in root)
xy_to_p={(p.ep-p.eq,p.ep):p for p in root}
xy=sorted(xy_to_p)
low=[]
for z in xy:
    while len(low)>1 and cross(low[-2],low[-1],z)<=0:low.pop()
    low.append(z)
up=[]
for z in reversed(xy):
    while len(up)>1 and cross(up[-2],up[-1],z)<=0:up.pop()
    up.append(z)
hull=low[:-1]+up[:-1]
assert len(hull)==16

def vertical_section(a,b):
    x1,y1=a;x2,y2=b
    if x1*x2>0 or x1==x2:return None
    if x1==0:return F(y1)
    if x2==0:return F(y2)
    return F(y1*(-x2)+y2*x1,x1-x2)

edges=[]
for a,b in zip(hull,hull[1:]+hull[:1]):
    y=vertical_section(a,b)
    if y is not None:edges.append((y,a,b))
assert len(edges)==2
edges.sort(key=lambda x:x[0])
(_,la,lb),(_,ua,ub)=edges
A,B=sorted((la,lb));C,E=sorted((ua,ub))
def margin(p,a,b):
    x,y=p;x1,y1=a;x2,y2=b
    return (y-y1)*(x2-x1)-(y2-y1)*(x-x1)
assert all(margin(v,A,B)>=0 and margin(v,C,E)<=0 for v in hull)

# A different independent full-history DFS traverses each origin tree,
# without Bellman states, dynamic-programming caches or count merging.
def history_dfs(p):
    stack=[(0,1,1,p)];obs=[0,0,0,0];nodes=0
    while stack:
        n,pp,qq,pnt=stack.pop();nodes+=1
        choice=pnt.trace[0]
        if choice=='C':
            for j,ch in enumerate(pnt.trace[1]):
                stack.append((n+1,pp*PN[j],qq*QN[j],ch))
        else:
            if choice=='Q':obs[0]+=pp*BASE[n]
            if choice=='P':obs[1]+=qq*BASE[n]
            obs[2]+=n*pp*BASE[n];obs[3]+=n*qq*BASE[n]
    assert tuple(obs)==(p.ep,p.eq,p.tp,p.tq)
    return nodes

def witness(a,b):
    p=xy_to_p[a];q=xy_to_p[b]
    w=F(-b[0],a[0]-b[0]);assert 0<w<1
    alpha=(w*p.ep+(1-w)*q.ep)/D
    errq=(w*p.eq+(1-w)*q.eq)/D
    tP=(w*p.tp+(1-w)*q.tp)/D
    tQ=(w*p.tq+(1-w)*q.tq)/D
    assert errq==alpha and tP>=tQ and tP==H-(LP+LQ)*alpha
    return dict(alpha=str(alpha),value=str(tP),timeQ=str(tQ),time_advantage=str(tP-tQ),
                weights=[str(w),str(1-w)],XY=[list(a),list(b)],
                origin_nodes=[history_dfs(p),history_dfs(q)])
left=witness(A,B);right=witness(C,E)
assert (F(left['alpha']),F(left['value']))==(F(136710455785,365699432448),F(324682148605,45712429056))
assert (F(right['alpha']),F(right['value']))==(F(2,5),F(24,5))
assert F(left['time_advantage'])>0 and F(right['time_advantage'])==0
assert F(right['alpha'])>F(left['alpha'])
# New support is strictly above the Stage244 affine extension on the right.
assert F(88)<F(201435849912,1765157155)

cert={
  'stage':245,'classification':'AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED',
  'model':{'P_numerators':PN,'Q_numerators':QN,'denominator':24,'N':N},
  'LP':str(LP),'LQ':str(LQ),'H':str(H),'slope':str(-(LP+LQ)),
  'bellman_states':len(S),'tie_states':[{'s':list(s),'actions':list(c)} for s,c in ties],
  'positive_action_gaps':len(gaps),'minimum_action_gap':str(min(gaps)),
  'root_error_polytope_vertex_count':len(root),'max_intermediate_hull_vertices':max(len(p) for p in polys.values()),
  'tested_minkowski_candidates':tested,
  'root_XY_vertices':[list(p) for p in hull],
  'global_support_edges':{'lower':[list(A),list(B)],'upper':[list(C),list(E)]},
  'left':left,'right':right,'delta':str(F(right['alpha'])-F(left['alpha'])),
  'witness_tree_DFS_nodes':sum(left['origin_nodes']+right['origin_nodes']),
  'method':'Bellman optimal actions + exact 2D convex hull of error expectations via recursive Minkowski sums; witnesses retain full 4-observation integer measures and ordered tree origin; no enumeration of 2^27 count-state corners.',
  'scope':'All real alpha in endpoint interval; all full-history randomized policies; only external IID N14, not native X6 or Source admission.'
}
Path(__file__).with_name('CERT_STAGE245_EXACT.json').write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('STAGE245_EXACT_POLYTOPE_PASS',len(root),'ties',len(ties),'candidates',tested,'DFS_nodes',cert['witness_tree_DFS_nodes'])
print('ALPHA',right['alpha'],'VALUE',right['value'],'WIDTH',cert['delta'])
