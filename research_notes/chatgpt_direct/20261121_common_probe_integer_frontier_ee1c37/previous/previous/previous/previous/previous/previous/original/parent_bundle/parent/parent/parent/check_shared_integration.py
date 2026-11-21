"""Shared-key maintenance inside the inherited atomic-primitive cooperative ring."""
from __future__ import annotations
from dataclasses import replace
from functools import lru_cache
from pathlib import Path
import argparse,json,sys
import check_shared_key as s
sys.path.insert(0,str(Path(__file__).resolve().parent/'parent'))
import check_identity_integration as old
base,p,m,e,r=s.base,s.p,s.m,s.e,s.r
ONE,ZERO=s.ONE,s.ZERO
gate=old.gate
CHECKS=0

def ck(v,msg):
    global CHECKS
    CHECKS+=1
    if not v:raise AssertionError(msg)

class SharedRing(old.IdentityRing):
    def __init__(self,slots=1,actors=2,repeats=1):
        super().__init__(slots,actors,repeats)
        start=self.C.index[0][0][0]
        self.C=s.Compiler(slots=slots,index_start=start,policy='feedback')
        self.H=frozenset(set(self.H)|set(self.C.H))
        self.core_members=frozenset(x for h in self.C.H for x in h)
        self.members=len({x for h in self.H for x in h})
        self._raw=lru_cache(maxsize=500000)(self._uncached)
        self.calls=self.uses=self.omissions=0

    def begin(self,jobs,k,route):
        if k<len(jobs) and jobs[k][0] in ('bind','reserve'):
            return gate.PC('shared_base',k,route=route)
        return super().begin(jobs,k,route)

    def word(self,i,pc,jobs):
        if pc.phase=='shared_base':return self.C.base_programs[jobs[i][pc.job]]
        if pc.phase=='shared_tail':
            op=jobs[i][pc.job]
            if op[0]=='reserve':return self.C.refresh[op[1]]
            return self.C.bind_copy[op[1],op[2]] if pc.target else tuple(self.C.clear_index(op[1]))
        return super().word(i,pc,jobs)

    def invariant(self,node):
        super().invariant(node)
        for i,pc in enumerate(node.pcs):
            if pc.phase in ('shared_base','shared_tail'):
                ck(self.lock(i) in node.J,'source/cache binding and publication hold real token')
                nxt=(i+1)%self.actors
                banks=[b for b,h in enumerate(self.gate_pair[nxt]) if h in node.J]
                ck(len(banks)==1 and pc.route==(banks[0]^int(i==self.actors-1)),
                   'shared maintenance preserves the observed handoff bank')

    def next(self,node,i,jobs,omit=False,check=True):
        pc=node.pcs[i]
        if pc.phase not in ('shared_base','shared_tail'):
            return super().next(node,i,jobs,omit,check)
        word=self.word(i,pc,jobs);raw=word[pc.pos//self.repeats];self.uses+=1
        if omit:K=node.J;ok=None;self.omissions+=1
        else:K,ok=self._raw(node.J,raw)
        nxt=replace(pc,pos=pc.pos+1)
        if nxt.pos==len(word)*self.repeats:
            if pc.phase=='shared_base':
                answer=self.C.observe_result(K)
                op=jobs[i][pc.job]
                if op[0]=='reserve' and not answer:
                    nxt=self.begin(jobs[i],pc.job+1,pc.route)
                else:nxt=gate.PC('shared_tail',pc.job,int(answer),route=pc.route)
            else:nxt=self.begin(jobs[i],pc.job+1,pc.route)
        pcs=list(node.pcs);pcs[i]=nxt
        ans=gate.Node(K,tuple(pcs),node.turn)
        if check:self.invariant(ans)
        return ans,raw,ok,False

    def terminal(self,node,jobs,table,grants,phase=0):
        ck(all(pc.phase in ('done','busy') for pc in node.pcs),'completed finite attempts')
        ck(grants==tuple(range(len(grants))),'cyclic grant prefix')
        tab=table;cache=self.C.initial_cache(table);last=None;answers={}
        for i in grants:
            value=None
            for op in jobs[i]:
                logical=('execute',op[1]) if op[0]=='feedback' else op
                after,value=base.expected(self.C,tab,logical)
                cache=s.expected_cache(self.C,tab,cache,logical,after,value)
                tab=after
            answers[i]=value
            if jobs[i]:last=value
        want=self.C.encode(tab,last,cache)
        for i,v in enumerate(self.lanes):
            bank=phase^int(i in grants)
            want=m.canon(want+p.reg(v.admitted,int(i in grants)))
            if i in grants and jobs[i]:want=m.canon(want+p.reg(v.reply,int(answers[i])))
            if i!=node.turn:want=m.canon(want+(self.gate_pair[i][bank],))
            ck(node.pcs[i].route is None,'per-call route retired')
        ck(node.J==want,'entire source, reference snapshots, possibly stale cache, answers and gates')
        return answers


def costs():
    rows=[]
    for op in (('bind',0,0),('bind',0,1),('bind',0,2),('reserve',0),('feedback',0)):
        G=SharedRing(slots=6)
        table=((0,None,0),((0,0),)+(None,)*5)
        node=G.initial_node(table);jobs=((op,),())
        node,steps,grants=gate.complete(G,node,0,jobs)
        # The other actor remains at entry. Finish its single attempt so the
        # inherited ring terminal has a complete two-actor endpoint.
        node,steps2,grants2=gate.complete(G,node,1,jobs)
        G.terminal(node,jobs,table,grants+grants2)
        rows.append(dict(op=op,first_steps=steps,second_pass=steps2,members=G.members,candidates=len(G.H)))
    return dict(mode='ring_costs',rows=rows,assertions=CHECKS,inherited_gate_assertions=gate.CHECKS)


def graph(case='execute_bind',repeats=3,budget=2,limit=300000):
    G=SharedRing(1,2,repeats);table=((0,None,0),((0,0),))
    choices={
      'execute_bind':((('feedback',0),),(('bind',0,2),)),
      'execute_restart':((('feedback',0),),(('release',1),('reserve',0),('bind',0,0))),
      'retire_bind_absent':((('release',1),),(('bind',0,0),)),
      'copy_restart':((('bind',0,0),),(('release',1),('reserve',0))),
    }
    jobs=choices[case];front={(G.initial_node(table),0,()):ONE};terms={};states=edges=0
    while front:
        nxt={}
        for (node,used,order),mass in front.items():
            states+=1
            if states>limit:raise RuntimeError('Declared state limit reached')
            if all(pc.phase in ('done','busy') for pc in node.pcs):
                G.terminal(node,jobs,table,order)
                key=node,used,order;terms[key]=r.merge(terms.get(key,ZERO),mass);continue
            for i,pc in enumerate(node.pcs):
                if pc.phase in ('done','busy'):continue
                for skip in range(2 if used<budget else 1):
                    nn,_,_,grant=G.next(node,i,jobs,bool(skip));edges+=1
                    key=nn,used+skip,order+((i,) if grant else ())
                    nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
        front=nxt
    totals={}
    for (_,used,_),mass in terms.items():totals[used]=r.merge(totals.get(used,ZERO),mass)
    return dict(mode='ring_graph',case=case,repeats=repeats,budget=budget,
        states=states,edges=edges,terminal_classes=len(terms),
        CWM={str(k):e.cw(v) for k,v in totals.items()},assertions=CHECKS,
        inherited_gate_assertions=gate.CHECKS,kernel_cache_misses=G.calls,
        primitive_attempts=G.uses,omission_edges=G.omissions)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=('costs','graph'))
    ap.add_argument('--case',default='execute_bind');ap.add_argument('--repeats',type=int,default=3)
    ap.add_argument('--budget',type=int,default=2);ap.add_argument('--out');a=ap.parse_args()
    out=costs() if a.mode=='costs' else graph(a.case,a.repeats,a.budget)
    text=json.dumps(out,ensure_ascii=False,indent=2)+'\n'
    if a.out:Path(a.out).write_text(text)
    else:print(text)
