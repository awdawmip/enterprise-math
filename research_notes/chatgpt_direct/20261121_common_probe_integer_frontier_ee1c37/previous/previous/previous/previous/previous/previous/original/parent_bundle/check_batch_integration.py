"""Primitive-level protected batch with an invocation-local absence witness."""
from __future__ import annotations
from dataclasses import dataclass,replace
from functools import lru_cache
from pathlib import Path
import argparse,json,sys
import check_batch_vacancy as a
sys.path.insert(0,str(Path(__file__).resolve().parent/'parent'))
import check_vacancy_integration as prior
base,p,m,e,r=a.base,a.p,a.m,a.e,a.r
gate=prior.gate
ONE,ZERO=a.ONE,a.ZERO
CHECKS=0

def ck(value,msg):
 global CHECKS
 CHECKS+=1
 if not value:raise AssertionError(msg)

@dataclass(frozen=True)
class Cursor:
 at:int=0
 holes:tuple[int,...]|None=None
 search:a.Search|None=None
 color:int|None=None
 last:int=1

class BatchRing(prior.VacancyRing):
 PHASES_BATCH=('batch_free','batch_bit','batch_write')
 def __init__(self,slots=2,actors=2,repeats=1):
  super().__init__(slots,actors,repeats)
  self.C=a.Compiler(slots=slots,index_start=self.C.index[0][0][0])
  self.H=frozenset(set(self.H)|set(self.C.H));self.core_members=frozenset(x for h in self.C.H for x in h)
  self.members=len({x for h in self.H for x in h});self._raw=lru_cache(maxsize=500000)(self._uncached)
  self.calls=self.uses=self.omissions=0
 def begin(self,jobs,k,route):
  if k<len(jobs) and jobs[k][0]=='batch_reserve':return gate.PC('batch_free',k,Cursor(),route=route)
  return super().begin(jobs,k,route)
 def word(self,i,pc,jobs):
  if pc.phase not in self.PHASES_BATCH:return super().word(i,pc,jobs)
  c=pc.target;t=jobs[i][pc.job][1][c.at]
  if pc.phase=='batch_free':return self.C.free_reads[t]
  if pc.phase=='batch_bit':
   task=c.search.task
   return self.C.reads[task.active[c.search.at],task.level]
  return self.C.create_words[t,c.color,c.last]
 def invariant(self,node):
  super().invariant(node)
  for i,pc in enumerate(node.pcs):
   if pc.phase in self.PHASES_BATCH:
    ck(self.lock(i) in node.J,'certificate and all target commits share the actual protected interval')
    j=(i+1)%self.actors;banks=[b for b,h in enumerate(self.gate_pair[j]) if h in node.J]
    ck(len(banks)==1 and pc.route==(banks[0]^int(i==self.actors-1)),'batch preserves observed handoff bank')
 def next(self,node,i,jobs,omit=False,check=True):
  pc=node.pcs[i]
  if pc.phase not in self.PHASES_BATCH:return super().next(node,i,jobs,omit,check)
  word=self.word(i,pc,jobs);raw=word[pc.pos//self.repeats];self.uses+=1
  if omit:K=node.J;ok=None;self.omissions+=1
  else:K,ok=self._raw(node.J,raw)
  nxt=replace(pc,pos=pc.pos+1);c=pc.target;targets=jobs[i][pc.job][1];t=targets[c.at]
  def next_target():
   if c.at+1<len(targets):return gate.PC('batch_free',pc.job,Cursor(c.at+1,c.holes),route=pc.route)
   return self.begin(jobs[i],pc.job+1,pc.route)
  if nxt.pos==len(word)*self.repeats:
   if pc.phase=='batch_write':nxt=next_target()
   elif pc.phase=='batch_free':
    if not self.C.observe_result(K):nxt=next_target()
    elif c.holes is None:nxt=gate.PC('batch_bit',pc.job,replace(c,search=a.start_search(self.C.slots)),route=pc.route)
    else:nxt=gate.PC('batch_write',pc.job,replace(c,color=a.select_color(self.C,t,c.holes),last=1),route=pc.route)
   else:
    value=int(self.C.observe_result(K));s=a.accept_bit(c.search,value,self.C.color_bits)
    if s.task is not None:nxt=gate.PC('batch_bit',pc.job,replace(c,search=s),route=pc.route)
    else:nxt=gate.PC('batch_write',pc.job,Cursor(c.at,s.holes,None,a.select_color(self.C,t,s.holes),value),route=pc.route)
  pcs=list(node.pcs);pcs[i]=nxt;out=gate.Node(K,tuple(pcs),node.turn)
  if check:self.invariant(out)
  return out,raw,ok,False
 def terminal(self,node,jobs,table,grants,phase=0):
  ck(all(pc.phase in ('done','busy') for pc in node.pcs),'finite concurrent calls completed')
  ck(grants==tuple(range(len(grants))),'cyclic prefix of admitted calls')
  tab=table;cache=self.C.initial_cache(tab);last=None;answers={}
  for i in grants:
   value=None
   for op in jobs[i]:
    if op[0]=='batch_reserve':tab,cache,values=a.expected_batch(self.C,tab,cache,op[1]);value=values[-1]
    else:
     logical=('execute',op[1]) if op[0]=='feedback' else op
     tab,value,cache=a.parent.expected(self.C,tab,cache,logical)
   answers[i]=value
   if jobs[i]:last=value
  want=self.C.encode(tab,last,cache)
  for i,v in enumerate(self.lanes):
   bank=phase^int(i in grants);want=m.canon(want+p.reg(v.admitted,int(i in grants)))
   if i in grants and jobs[i]:want=m.canon(want+p.reg(v.reply,int(answers[i])))
   if i!=node.turn:want=m.canon(want+(self.gate_pair[i][bank],))
   ck(node.pcs[i].route is None,'invocation route discarded on completion')
  ck(node.J==want,'whole endpoint including caches gates responses and cleanup')
  return answers

def costs():
 rows=[]
 for phase in (0,1):
  G=BatchRing(slots=6);tab=((None,)*3,tuple((0,c) for c in range(6)));jobs=((('batch_reserve',(0,2)),),(('bind',0,0),))
  node=G.initial_node(tab,phase=phase);_,_,local=G.C.batch(G.C.encode(tab),(0,2))
  node,n,grants=gate.complete(G,node,0,jobs);node,n2,g2=gate.complete(G,node,1,jobs)
  G.terminal(node,jobs,tab,grants+g2,phase)
  ck(n==local['commands']+31,'batch wrapper paid once rather than once per target')
  rows.append(dict(phase=phase,batch_commands=n,next_bind_commands=n2,members=G.members,candidates=len(G.H)))
 return dict(mode='ring_costs',rows=rows,assertions=CHECKS,parent_gate_assertions=gate.CHECKS)

def graph(case='batch_bind',repeats=2,budget=1,limit=250000):
 G=BatchRing(slots=2,actors=2,repeats=repeats)
 if case=='batch_bind':tab=((None,)*3,((0,0),None));jobs=((('batch_reserve',(0,2)),),(('bind',1,0),))
 elif case=='batch_copy':tab=((None,)*3,((0,0),None));jobs=((('batch_reserve',(0,2)),),(('copy',1,0),))
 else:raise ValueError(case)
 front={(G.initial_node(tab),0,()):ONE};terminal={};states=edges=0
 while front:
  nxt={}
  for (node,used,order),mass in front.items():
   states+=1
   if states>limit:raise RuntimeError('Declared graph limit exceeded')
   if all(pc.phase in ('done','busy') for pc in node.pcs):
    G.terminal(node,jobs,tab,order);key=node,used,order;terminal[key]=r.merge(terminal.get(key,ZERO),mass);continue
   for i,pc in enumerate(node.pcs):
    if pc.phase in ('done','busy'):continue
    for skipped in range(2 if used<budget else 1):
     nn,_,_,grant=G.next(node,i,jobs,bool(skipped));edges+=1
     key=nn,used+skipped,order+((i,) if grant else ())
     nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
  front=nxt
 masses={}
 for (_,used,_),weight in terminal.items():masses[used]=r.merge(masses.get(used,ZERO),weight)
 return dict(mode='ring_graph',case=case,repeats=repeats,omission_budget=budget,states=states,edges=edges,
             terminal_classes=len(terminal),CWM={str(k):e.cw(v) for k,v in masses.items()},assertions=CHECKS,
             parent_gate_assertions=gate.CHECKS,kernel_cache_misses=G.calls,primitive_attempts=G.uses)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['costs','graph']);ap.add_argument('--case',default='batch_bind')
 ap.add_argument('--repeats',type=int,default=2);ap.add_argument('--budget',type=int,default=1);ap.add_argument('--out')
 args=ap.parse_args();data=costs() if args.mode=='costs' else graph(args.case,args.repeats,args.budget)
 text=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
 if args.out:Path(args.out).write_text(text)
 else:print(text)
