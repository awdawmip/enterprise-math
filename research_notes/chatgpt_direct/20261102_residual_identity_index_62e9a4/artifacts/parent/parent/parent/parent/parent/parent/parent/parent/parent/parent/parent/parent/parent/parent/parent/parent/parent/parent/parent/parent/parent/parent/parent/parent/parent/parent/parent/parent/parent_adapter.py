"""Residual-preserving signed-tail adapters. Original typed positive BRC only.

No parent main is run. Matching changes go through the pinned e.step/m.full_step.
State alternatives use CWM. A separate Boolean-support observer is used only
for the finite shortest-word synthesis test; it makes no probability claim.
"""
from __future__ import annotations
from pathlib import Path
import hashlib,importlib.util,json,sys
from itertools import product
from collections import deque
ROOT=Path(__file__).resolve().parent
for rel,meta in json.loads((ROOT/'SOURCE_PINS.json').read_text()).items():
 b=(ROOT/'vendor'/rel).read_bytes()
 if hashlib.sha256(b).hexdigest()!=meta['sha256']:raise RuntimeError(rel)
 if hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()!=meta['git_blob']:raise RuntimeError(rel)
sp=importlib.util.spec_from_file_location('tail_primitive',ROOT/'vendor/prior_primitive.py')
p=importlib.util.module_from_spec(sp);sys.modules[sp.name]=p;sp.loader.exec_module(p)
e,m,r=p.e,p.m,p.r
ONE,ZERO=p.ONE,p.ZERO
E=(1,2,3);P=(2,6,10);A=(4,5,6);B=(4,5,7);HP=(6,8,9);HN=(7,8,9)
SOURCE_H={E,P,A,B,HP,HN}
CHECKS=CALLS=USES=0;CACHE={}
def ck(ok,label):
 global CHECKS
 CHECKS+=1
 if not ok:raise AssertionError(label)
def step(J,op,H):
 global CALLS,USES
 USES+=1;H=frozenset(H);key=(J,op,H)
 if key not in CACHE:
  K,delta,ok=e.step(J,op,H);CALLS+=1
  ck(all(h in H for h in K),'declared event library')
  ck(len(m.used(K))==3*len(K),'no repeated occurrence')
  CACHE[key]=K,ok
 return CACHE[key]
def put(d,k,w):d[k]=r.merge(d.get(k,ZERO),w)
def norm(J):return m.canon(h for h in J if h not in (A,B))
def source(J):return m.canon(h for h in J if h in SOURCE_H)
def signed(J):return 1 if HP in J else 0 if HN in J else -1
def reader(port,o,a,invert=False):
 # Output inversion is an address permutation, not an input-dependent branch.
 ht=p.reg(o,0 if invert else 1)[1];hf=p.reg(o,1 if invert else 0)[1]
 probe=tuple(sorted((port,ht[0],a)))
 word=[p.add(probe),p.add(ht),p.add(hf),p.one(a),
       p.add(p.reg(o,1 if invert else 0)[0]),p.add(p.reg(o,0 if invert else 1)[0])]
 return p.library(o)|{probe},word,probe
HA,wa,Q=reader(7,30,37,True);ADAPTER=[p.one(4)]+wa
HV,wv,QV=reader(8,40,47);HNread,wn,QN=reader(7,50,57)
PARTIAL=wv+[p.one(4)]+wn
HALF=p.reg(30,1)[1]
def rep(word,f):return [op for op in word for _ in range(f+1)]
def trace(J,word,H,omitted=()):
 initial=J;omitted=frozenset(omitted);mass=e.prep(J);rows=[]
 for j,op in enumerate(word):
  K,ok=(J,None) if j in omitted else step(J,op,H)
  mass=r.serial(mass,ONE)
  rows.append(dict(slot=j+1,op=op,invoked=j not in omitted,success=ok,before=J,after=K))
  J=K
 return dict(initial=initial,end=J,commands=len(word),omitted=[i+1 for i in sorted(omitted)],CWM=e.cw(mass),trace=rows)
def layers(L,f):
 d={0:ONE}
 for _ in range(L):
  q={}
  for j,w in d.items():
   put(q,j,r.serial(w,ONE))
   if j<f:put(q,j+1,r.serial(w,ONE))
  d=q
 return d

def static_suite():
 _,cat=e.catalog(SOURCE_H);dom=tuple(sorted(cat));valid=[J for J in dom if signed(J)>=0]
 out=[];noise=(81,82,83)
 for J in valid:
  H=SOURCE_H|HA|{noise};init=m.canon(J+(noise,));z=trace(init,ADAPTER,H)
  ck(z['end']==m.canon(norm(J)+p.reg(30,signed(J))+(noise,)),'seven-step exact postcondition')
  for row in z['trace']:
   K=row['after'];ck((HP in K)==(HP in J) and (HN in K)==(HN in J),'signed tail preserved at every prefix')
   ck((P in K)==(P in J),'old probe never released or invented')
   ck(noise in K and (E in K)==(E in J),'declared frame retained')
  if J in (p.reg(3,0),p.reg(3,1)):
   d=[len(set(range(4,10))-set(m.used(row['after']))) for row in z['trace']]
   ck(max(d)==3,'sharp three-original-member exposure from fully occupied register')
   z['source_idle_peak']=max(d)
   restored=trace(init,ADAPTER+[p.add(A),p.add(B)],H)
   ck(restored['end']==m.canon(J+p.reg(30,signed(J))+(noise,)),'full inputs admit exact source restoration with two further additions')
  out.append(z)
 partial=[]
 for J in dom:
  z=trace(J,PARTIAL,SOURCE_H|HV|HNread)
  v=int(HP in J or HN in J);n=int(HN in J)
  ck(z['end']==m.canon(norm(J)+p.reg(40,v)+p.reg(50,n)),'13-step complete two-bit certificate with UNKNOWN')
  ck((v,n) in ((0,0),(1,0),(1,1)),'no invalid 01 certificate')
  for row in z['trace']:
   ck((P in row['after'])==(P in J),'partial adapter preserves residual probe')
   ck(signed(row['after'])==signed(J),'partial adapter never changes evidence sign')
  partial.append(z)
 # Clean output may be fed to the old copier even while the ORIGINAL P remains.
 dirty=m.canon((P,HN));HC,WC=p.copy_program(30,60,67)
 z=trace(dirty,ADAPTER+WC,SOURCE_H|HA|HC)
 ck(z['end']==m.canon((P,HN)+p.reg(30,0)+p.reg(60,0)),'old copier now composes, original dirty residual retained')
 # A fresh target is an input condition, not a hidden assumption.
 _,tc=e.catalog(p.library(30));reuse=[]
 for J in valid:
  for T in tc:
   ini=m.canon(J+T);zz=trace(ini,p.clear_word(30)+ADAPTER,SOURCE_H|HA)
   ck(zz['end']==m.canon(norm(J)+p.reg(30,signed(J))),'9-step overwrite adapter')
   z2=trace(zz['end'],p.clear_word(30)+ADAPTER,SOURCE_H|HA)
   ck(z2['end']==zz['end'],'repeatable at macro endpoints on declared domain')
 return dict(source_states=len(dom),signed_source_states=len(valid),seven_step=out,
             thirteen_step=partial,composition=z,overwrite_cases=len(valid)*len(tc)),dom,valid

def omission_family(J,word,H,f,kind):
 d={(J,0):e.prep(J)}
 for op in word:
  nxt={}
  for (K,k),mass in d.items():
   L,_=step(K,op,H);put(nxt,(L,k),r.serial(mass,ONE))
   if k<f:put(nxt,(K,k+1),r.serial(mass,ONE))
  d=nxt
 target=m.canon(norm(J)+(p.reg(30,signed(J)) if kind=='total' else
                         p.reg(40,int(HP in J or HN in J))+p.reg(50,int(HN in J))))
 for (K,k),mass in d.items():ck(K==target,'complete adapter under global omission budget')
 sums={}
 for (K,k),mass in d.items():put(sums,k,mass)
 ck(sums==layers(len(word),f),'omission CWM equals independent position-only composition')
 return dict(kind=kind,f=f,start=J,commands=len(word),layers=[dict(omissions=k,CWM=e.cw(w)) for k,w in sorted(sums.items())])

def faults_suite(dom,valid):
 cases=[]
 for f in range(1,4):
  for J in valid:cases.append(omission_family(J,rep(ADAPTER,f),SOURCE_H|HA,f,'total'))
  for J in dom:cases.append(omission_family(J,rep(PARTIAL,f),SOURCE_H|HV|HNread,f,'partial'))
 # Same basic code, specific failures when preconditions are dropped.
 unknown=trace((),ADAPTER,SOURCE_H|HA)
 ck(p.restrict(unknown['end'],30)==p.reg(30,1),'seven-step program requires total evidence')
 miss_head=trace(p.reg(3,1),ADAPTER,SOURCE_H|HA,(0,))
 ck(p.restrict(miss_head['end'],30)==p.reg(30,0),'omitted header exposure can invert a positive')
 miss_probe=trace((HP,),ADAPTER,SOURCE_H|HA,(1,))
 ck(p.restrict(miss_probe['end'],30)==p.reg(30,0),'omitted adapted probe can invert a positive')
 alien=(7,81,82);alien_trace=trace(m.canon((HP,alien)),rep(ADAPTER,3),SOURCE_H|HA|{alien})
 ck(p.restrict(alien_trace['end'],30)==p.reg(30,0),'unmodelled occupied read port not fixed by repeats')
 fresh=trace(m.canon((HP,)+p.reg(30,0)),ADAPTER,SOURCE_H|HA)
 ck(p.restrict(fresh['end'],30)==p.reg(30,0),'nonempty target is not automatically overwritten')
 critical=[]
 for name,word,initials,H in [('total',ADAPTER,valid,SOURCE_H|HA),('partial',PARTIAL,dom,SOURCE_H|HV|HNread)]:
  for i in range(len(word)):
   witness=None
   for J in initials:
    z=trace(J,word,H,(i,))
    target=m.canon(norm(J)+(p.reg(30,signed(J)) if name=='total' else
                    p.reg(40,int(HP in J or HN in J))+p.reg(50,int(HN in J))))
    if z['end']!=target:witness=z;break
   ck(witness is not None,'each fixed position is necessary for the exact postcondition')
   critical.append(dict(kind=name,stage=i+1,witness=witness))
 return dict(families=cases,critical_positions=critical,unknown_misuse=unknown,omitted_header=miss_head,
             omitted_probe=miss_probe,foreign_port=alien_trace,dirty_target=fresh)

def reader_word(f,total=True):
 W=[p.add(P),p.add(HP),p.add(HN),p.one(10),p.add(A),p.add(B)]
 return [ (i,op) for i,op in enumerate(W) for _ in range(f+1 if i<(3 if total else 2) else 1)]

def end_to_end(present,f,budget,kind="total"):
 # The real source may change only during the reader. One GLOBAL omission budget
 # covers those source attempts, the reader, the adapter and the old copier.
 rd=reader_word(f,kind=='total');HC,WC=p.copy_program(30,60,67)
 word=ADAPTER+WC if kind=='total' else PARTIAL
 wd=[(3,op) for op in rep(word,f)]
 full=rd+wd;L=len(full);R=len(rd)
 H=SOURCE_H|HA|HC if kind=='total' else SOURCE_H|HV|HNread
 env=(p.add(E),p.one(3));start=(E,) if present else ()
 states={(0,0,0,start,0):e.prep(start)};done={}
 for depth in range(L+budget+1):
  nxt={}
  for (i,b,d,J,seen),mass in states.items():
   if i==L:
    if kind=='total':
     v=p.read(J,30);ck(v in (0,1),'complete extracted bit')
     ck(p.restrict(J,60)==p.reg(60,v),'legacy copier gets same witnessed bit')
     target_H=p.library(30)|p.library(60)
    else:
     valid=p.read(J,40);negative=p.read(J,50)
     ck((valid,negative) in ((0,0),(1,0),(1,1)),'complete partial-code outputs')
     v=1-negative if valid else -1;target_H=p.library(40)|p.library(50)
    if v>=0:ck(seen&(1<<v),'extracted output has its own real source-contact witness')
    ck(signed(J)==v,'original source tail retained through composition')
    ck(not any(h not in SOURCE_H|target_H for h in J),'only declared old residual may remain')
    put(done,(b,d,v),mass);continue
   stage,op=full[i];K,_=step(J,op,H)
   ns=seen|((1<<int(E in J)) if i<R and stage==0 else 0)
   put(nxt,(i+1,b,d,K,ns),r.serial(mass,ONE))
   if d<f:put(nxt,(i+1,b,d+1,J,seen),r.serial(mass,ONE))
   if i<R and b<budget:
    for ep in env:
     K,_=step(J,ep,H);put(nxt,(i,b+1,d,K,seen),r.serial(mass,ONE))
     if d<f:put(nxt,(i,b+1,d+1,J,seen),r.serial(mass,ONE))
  states=nxt
 ck(not states,'all bounded histories terminated')
 # Independently transport positions, with no matching data, same command labels.
 pos={(0,0,0):ONE};expected={}
 for depth in range(L+budget+1):
  nxt={}
  for (i,b,d),mass in pos.items():
   if i==L:put(expected,(b,d),mass);continue
   put(nxt,(i+1,b,d),r.serial(mass,ONE))
   if d<f:put(nxt,(i+1,b,d+1),r.serial(mass,ONE))
   if i<R and b<budget:
    for _ in env:
     put(nxt,(i,b+1,d),r.serial(mass,ONE))
     if d<f:put(nxt,(i,b+1,d+1),r.serial(mass,ONE))
  pos=nxt
 got={}
 for (b,d,v),mass in done.items():put(got,(b,d),mass)
 ck(got==expected,'all bounded dynamic source/omission histories preserve CWM')
 return dict(kind=kind,initial_source=present,f=f,source_budget=budget,reader_commands=R,
             fixed_commands=L,layers=[dict(source_attempts=b,omissions=d,value=v,CWM=e.cw(w)) for (b,d,v),w in sorted(done.items())])

def minimal_synthesis(valid):
 # Finite Boolean-support product automaton over all five evidence states, with
 # no real E (it is a frame). It searches words, not a new physical dynamics.
 V=tuple(J for J in valid if E not in J)
 H=(SOURCE_H-{E})|HA
 release_ids=(4,5,31,32,33,34,35,36,37)
 commands=tuple([p.one(i) for i in release_ids]+[p.add(h) for h in sorted(H)])
 target=tuple(m.canon(norm(J)+p.reg(30,signed(J))) for J in V)
 queue=deque([V]);dist={V:0};parent={};shortest=None;edge_uses=0
 while queue:
  S=queue.popleft()
  if S==target:
   word=[];t=S
   while t!=V:t,op=parent[t];word.append(op)
   shortest=list(reversed(word));break
  if dist[S]>=7:continue
  for op in commands:
   T=tuple(step(J,op,H)[0] for J in S);edge_uses+=1
   supported=r.brc.boolean_support(r.serial(ONE,ONE))
   if not supported:continue
   if any(signed(K)!=signed(J) or ((P in K)!=(P in J)) for J,K in zip(V,T)):continue
   if T not in dist:dist[T]=dist[S]+1;parent[T]=(S,op);queue.append(T)
 ck(shortest is not None and len(shortest)==7,'shortest word in declared finite library is 7')
 return dict(word=shortest,states_discovered=len(dist),edges=edge_uses,
             depth_counts={str(i):sum(v==i for v in dist.values()) for i in range(8)},
             scope='Boolean reachability of fixed programs preserving evidence tails and old probe at every prefix')

def main():
 static,dom,valid=static_suite()
 ans=dict(static=static,faults=faults_suite(dom,valid),
          end_to_end=[end_to_end(s,f,2,kind) for kind in ('total','partial') for f in range(3) for s in (0,1)],
          synthesis=minimal_synthesis(valid))
 ans['stats']=dict(assertions=CHECKS,uncached_kernel_calls=CALLS,transition_uses=USES,
                   inherited_p_checks=p.CHECKS,inherited_e_checks=e.CHECKS)
 (ROOT/'results.json').write_text(json.dumps(ans,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n')
 summary=dict(stats=ans['stats'],source_states=static['source_states'],signed_source_states=static['signed_source_states'],
              seven_step_commands=7,partial_commands=13,overwriting_commands=9,
              omission_families=len(ans['faults']['families']),end_to_end_families=len(ans['end_to_end']),
              shortest=ans['synthesis'])
 (ROOT/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
 print(json.dumps(summary,ensure_ascii=False,sort_keys=True))
if __name__=='__main__':main()
