from collections import defaultdict
from itertools import product
import json
OP={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]]
S=[0,0,4,1,16,32,8,2,0];A='acdefg'; I={c:j for j,c in enumerate(A)}
def native(w):return tuple(v for c in w for v in OP[c])
def sig(w):
 s=0
 for c in w:s=T[s][I[c]]
 return S[s]
def key(w):return tuple(sum(i==j for i in native(w)) for j in range(1,7))
def disp(w):return tuple(sum((i==j)-(i==-j) for i in native(w)) for j in range(1,7))
def words(h,k):
 x,y,z=k;d=dict(a=z-1,e=z,f=h+1-y-2*z,g=h+1-x,c=0,d=0);r=x+y-h-1
 if min(*d.values(),r)<0:return
 for nc in range(r+1):
  d['c'],d['d']=nc,r-nc
  def recurse(w):
   if len(w)==h:yield w;return
   for c in A:
    if d[c]:
     d[c]-=1;yield from recurse(w+c);d[c]+=1
  yield from recurse('')
def eligible(h,k):
 out={}
 for w in words(h,k):
  if sig(w):
   assert disp(w)==(2,0,0,0,0,0) and key(w)==(*k,0,0,0)
   out[w]=native(w)
 return out
assert len({OP[c][:2] for c in A})==6
assert all(T[s][I[c]]==s for s in range(2,8) for c in 'fg')
result={};loops=0
for L in ((4,3,1),(5,2,1)):
 E={h:eligible(h,L) for h in (4,5,6)};M={h:eligible(h,(8,2,1)) for h in (7,8,9)}
 pair={}
 for h in E:
  for k in M:
   prefixes=defaultdict(list)
   for v,t in M[k].items():prefixes[t[:2*(sum(L)-1)]].append(v)
   matches=[(u,v) for u,t in E[h].items() for v in prefixes.get(t,[])]
   expect=len(E[h]) if L==(5,2,1) and k==h+3 else 0
   assert len(matches)==expect
   assert all(v==u+'fff' and sig(v)==sig(u) for u,v in matches)
   pair[f'{h}->{k}']=len(matches)
 result[str(L)]={'early':[len(E[h]) for h in E], 'late':[len(M[h]) for h in M], 'pairs':pair}
 if L==(5,2,1):
  for h in E:
   for u in E[h]:
    for p,q in product(range(4),repeat=2):
     for tail in ('f'*p+'g'*q,'g'*q+'f'*p):
      w=u+tail
      assert sig(w)==sig(u) and disp(w)==(2,0,0,0,0,0)
      assert key(w)==(5+p,2+q,1,0,0,0) and native(w)[:14]==E[h][u]
      loops+=1
base=('fe','ge','feg','gef')
sel=[(4,'dedf',1),(4,'fedd',2),(4,'fecc',4),(4,'ecfc',8),
 (5,'geffd',1),(5,'fedgf',2),(5,'fecfg',4),(5,'ecffg',8),
 (6,'fegffg',16),(6,'geffgf',32)]
assert all(len(w)==h and sig(w)==s and key(w)==(5,2,1,0,0,0) for h,w,s in sel)
def edges(ws):return {t[:i] for w in ws for t in (native(w),) for i in range(1,len(t)+1)}
early=edges([*base,*(w for h,w,s in sel)])
whole=edges([*base,*(w for h,w,s in sel),*(w+'fff' for h,w,s in sel)])
assert len(early)==82 and len(whole)==142
report={'status':'PASS','native_prefix_pairs':result,'checked_lifts':loops,
        'early_edges':82,'lifted_nine_window_edges':142,'witness':sel,
        'frozen_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'}
print(json.dumps(report,indent=2))
