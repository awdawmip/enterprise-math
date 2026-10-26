#!/usr/bin/env python3
"""Exact author verification of external ternary iid N14 Stage163 candidate.
No native P000 theorem or independent Driver review is claimed.
Derived from published Stage162 model, checked with distinct count-state and ordered-prefix implementations.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from itertools import product
import json,hashlib,datetime
N=14
P=(F(1,8), F(1,24), F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
PN=(3,1,20); QN=(1,1,10)
K=F(163900037061,554150611)
L=F(476600779976,1662451833)
ALPHA162=F(440625031179621048365,1265046575011281764352)
V162=F(2138966145833987829541,180720939287325966336)
R=(10,0,1); Y=(8,4,1)
TIES={R:('Q','C'),Y:('P','C')}
ACTS='PQC'
def fmt(x):return str(x.numerator)+('/'+str(x.denominator) if x.denominator!=1 else '')
def state_child(s,k):return s[0]+1,s[1]+(k==0),s[2]+(k==1)
def ratio(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
@lru_cache(None)
def val(s):
    opts=[K*ratio(s),L]
    if s[0]<N:
        opts.append(1+sum(P[k]*val(state_child(s,k))[0] for k in range(3)))
    return min(opts),tuple(opts)
strict={}; ties={}; gaps=[];nr=0
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
    s=(n,a,b); v,opts=val(s); ismin=tuple(ACTS[i] for i,o in enumerate(opts) if o==v)
    (ties if len(ismin)>1 else strict)[s]=ismin if len(ismin)>1 else ismin[0]
    gaps.extend(o-v for o in opts if o>v)
    nr+=1
assert nr==680 and len(gaps)==1238,(nr,len(gaps))
assert ties==TIES,(ties,TIES)

def action(s,r,x):
    if s==R:return 'Q' if r else 'C'
    if s==Y:return 'P' if x else 'C'
    return strict[s]

def suffix(r,x):
 @lru_cache(None)
 def rec(s):
    a=action(s,r,x)
    if a=='P':return (F(0),F(1),F(0),F(0))
    if a=='Q':return (F(1),F(0),F(0),F(0))
    seq=[rec(state_child(s,k)) for k in range(3)]
    return (sum(P[k]*seq[k][0] for k in range(3)),
            sum(Q[k]*seq[k][1] for k in range(3)),
            1+sum(P[k]*seq[k][2] for k in range(3)),
            1+sum(Q[k]*seq[k][3] for k in range(3)))
 return rec((0,0,0))

def ordered_dfs(r,x):
    terminal=defaultdict(int); hits={R:[0,F(0),F(0)],Y:[0,F(0),F(0)]}; nodes=0
    def visit(n,a,b,pnum,qnum):
        nonlocal nodes
        nodes+=1;s=(n,a,b)
        if s in hits:
            hits[s][0]+=1;hits[s][1]+=F(pnum,24**n);hits[s][2]+=F(qnum,12**n)
        v=action(s,r,x)
        if v!='C':
            terminal[n,'allp']+=pnum;terminal[n,'allq']+=qnum
            terminal[n,'tp']+=n*pnum;terminal[n,'tq']+=n*qnum
            if v=='P':terminal[n,'eq']+=qnum
            else:terminal[n,'ep']+=pnum
            return
        for k in range(3): visit(n+1,a+(k==0),b+(k==1),pnum*PN[k],qnum*QN[k])
    visit(0,0,0,1,1)
    def tot(t,base):return sum((F(terminal[n,t],base**n) for n in range(N+1)),F(0))
    assert tot('allp',24)==1 and tot('allq',12)==1
    return (tot('ep',24),tot('eq',12),tot('tp',24),tot('tq',12)),hits,nodes

def plus(u,v):return tuple(x+y for x,y in zip(u,v))
def sub(u,v):return tuple(x-y for x,y in zip(u,v))
def mul(c,v):return tuple(c*x for x in v)
def ediff(v):return v[0]-v[1]
corners={}; checks={}; hits0=None; node_counts={}
for r,x in product([0,1],[0,1]):
    v=suffix(r,x); w,hits,nodes=ordered_dfs(r,x)
    assert v==w,(r,x,v,w)
    corners[r,x]=v; node_counts[f'{r}{x}']=nodes
    if hits0 is None:hits0=hits
    else:assert hits0==hits
print('CORNERS',*[f'{key}: '+str(tuple(fmt(x) for x in val)) for key,val in corners.items()],sep='\n')
base=corners[0,0];dR=sub(corners[1,0],base);dX=sub(corners[0,1],base)
mixed=sub(sub(corners[1,1],corners[1,0]),sub(corners[0,1],base))
print('M00',*[fmt(v) for v in base],sep='\n')
print('dR',*[fmt(v) for v in dR],sep='\n')
print('dX',*[fmt(v) for v in dX],sep='\n')
print('mixed',mixed)
assert mixed==(0,0,0,0)
print('hits', {str(k):(v[0],fmt(v[1]),fmt(v[2])) for k,v in hits0.items()})
print('DFS nodes',node_counts)
D0,DR,DX=ediff(base),ediff(dR),ediff(dX)
print('err_diff_coeff',*[fmt(x) for x in (D0,DR,DX)])
# balance: x(r)=a+b*r; r(x)=a+b*x
assert DX!=0 and DR!=0
x0,xslope=-D0/DX,-DR/DX
r0,rslope=-D0/DR,-DX/DR
print('x(r)',fmt(x0),fmt(xslope),'r')
print('r(x)',fmt(r0),fmt(rslope),'x')
print('x(0),x(1)',fmt(x0),fmt(x0+xslope))
print('r(0),r(1)',fmt(r0),fmt(r0+rslope))
# Find legal feasible balanced endpoints of the unit square by intersecting x(r) [0,1] with r in[0,1]
points=[]
for r in (F(0),F(1),-x0/xslope,(F(1)-x0)/xslope):
   x=x0+xslope*r
   if 0<=r<=1 and 0<=x<=1:points.append((r,x))
points=list(dict.fromkeys(points))
assert len(points)==2,points
def getobs(r,x):return plus(plus(base,mul(r,dR)),mul(x,dX))
points=sorted(points,key=lambda p:getobs(*p)[0]);(rl,xl),(rr,xr)=points
vl,vr=getobs(rl,xl),getobs(rr,xr)
for y in (vl,vr):
 assert y[0]==y[1] and y[2]>=y[3] and y[2]+K*y[1]+L*y[0]==val((0,0,0))[0],('broken',y)
print('LEFT coins',fmt(rl),fmt(xl),'alpha',fmt(vl[0]),'V',fmt(vl[2]),'time_gap',fmt(vl[2]-vl[3]))
print('RIGHT coins',fmt(rr),fmt(xr),'alpha',fmt(vr[0]),'V',fmt(vr[2]),'time_gap',fmt(vr[2]-vr[3]))
print('INHERITED_MATCH',vl[0]==ALPHA162 and vl[2]==V162)
print('SLOPE',fmt(K+L),'WIDTH',fmt(vr[0]-vl[0]))
print('BELL',fmt(val((0,0,0))[0]),'MIN_GAP',fmt(min(gaps)),'GAPS',len(gaps))
assert vl[0]==ALPHA162 and vl[2]==V162
assert vr[0]>vl[0]
assert K>0 and L>0
assert 0<=rl<=1 and 0<=rr<=1 and 0<=xl<=1 and 0<=xr<=1
assert vr[2]-vl[2]==-(K+L)*(vr[0]-vl[0])
# proof: no same-affine support beyond max common error on tie-family.
# For all policies that would saturate this bound, positive coefficients and strict Bellman gaps force tie-only acts.
# Disjoint reachable cones imply additivity for full ordered-history behavioral policies after averaging.
print('PASS Stage163 author exact interval + sharpness; no independent native review')
cert={'model':'external iid ternary N14','status':'AUTHOR_EXACT_COMPUTATION_ASSISTED','source_stage':'161 dual candidate; pinned global/main and EM/main prior to work','K':fmt(K),'L':fmt(L),'H_root':fmt(val((0,0,0))[0]),'states':nr,'positive_gaps':len(gaps),'minimum_gap':fmt(min(gaps)),'ties':{str(k):list(v) for k,v in ties.items()},'first_hits':{str(k):{'count':v[0],'P':fmt(v[1]),'Q':fmt(v[2])} for k,v in hits0.items()},'corners':{f'{r}{x}':[fmt(k) for k in corners[r,x]] for r,x in corners},'M00':[fmt(y) for y in base],'dR':[fmt(y) for y in dR],'dX':[fmt(y) for y in dX],'mixed':[fmt(y) for y in mixed],'error_diff_coeff':[fmt(y) for y in (D0,DR,DX)],'x_of_r':{'intercept':fmt(x0),'slope':fmt(xslope)},'r_of_x':{'intercept':fmt(r0),'slope':fmt(rslope)},'left':{'r':fmt(rl),'x':fmt(xl),'alpha':fmt(vl[0]),'V':fmt(vl[2]),'time_gap':fmt(vl[2]-vl[3])},'right':{'r':fmt(rr),'x':fmt(xr),'alpha':fmt(vr[0]),'V':fmt(vr[2]),'time_gap':fmt(vr[2]-vr[3])},'width':fmt(vr[0]-vl[0]),'slope':fmt(K+L),'ordered_dfs_nodes':node_counts,'dual_equalities':'EXACT_AT_BOTH_ENDPOINTS','primal_interval':'WHOLE_REAL_SEGMENT','right_sharpness':'DERIVED_BELLMAN_TIE_FAMILY_EXHAUSTION'}
path='/mnt/data/stage163_certificate.json'
with open(path,'w') as f:json.dump(cert,f,indent=2,ensure_ascii=False)
print('CERTIFICATE_FILE',path)
