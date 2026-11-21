"""Primitive-granularity integration of vacancy allocation with the inherited ring."""
from __future__ import annotations
from dataclasses import replace
from functools import lru_cache
from pathlib import Path
import argparse,json,sys
import check_vacancy as a
sys.path.insert(0,str(Path(__file__).resolve().parent/'parent'))
import check_addressed_integration as parent
base,p,m,e,r=a.base,a.p,a.m,a.e,a.r
ONE,ZERO=a.ONE,a.ZERO
gate=parent.gate
CHECKS=0

def ck(ok,msg):
    global CHECKS
    CHECKS+=1
    if not ok:raise AssertionError(msg)

class VacancyRing(parent.AddressedRing):
    PHASES_ALLOC=('vacancy_free','vacancy_bit','vacancy_write')
    def __init__(self,slots=1,actors=2,repeats=1):
        super().__init__(slots,actors,repeats)
        start=self.C.index[0][0][0]
        self.C=a.Compiler(slots=slots,index_start=start)
        self.H=frozenset(set(self.H)|set(self.C.H))
        self.core_members=frozenset(x for h in self.C.H for x in h)
        self.members=len({x for h in self.H for x in h})
        self._raw=lru_cache(maxsize=500000)(self._uncached)
        self.calls=self.uses=self.omissions=0

    def begin(self,jobs,k,route):
        if k<len(jobs) and jobs[k][0]=='reserve':
            return gate.PC('vacancy_free',k,route=route)
        return super().begin(jobs,k,route)

    def word(self,i,pc,jobs):
        if pc.phase=='vacancy_free':return self.C.free_reads[jobs[i][pc.job][1]]
        if pc.phase=='vacancy_bit':
            k,prefix,active,at,zeros,ones=pc.target
            return self.C.reads[active[at],k]
        if pc.phase=='vacancy_write':
            color,last=pc.target
            return self.C.create_words[jobs[i][pc.job][1],color,last]
        return super().word(i,pc,jobs)

    def invariant(self,node):
        super().invariant(node)
        for i,pc in enumerate(node.pcs):
            if pc.phase in self.PHASES_ALLOC:
                ck(self.lock(i) in node.J,'allocation evidence and commit protected by actual shared token')
                nxt=(i+1)%self.actors
                banks=[b for b,h in enumerate(self.gate_pair[nxt]) if h in node.J]
                ck(len(banks)==1 and pc.route==(banks[0]^int(i==self.actors-1)),
                   'allocation preserves the observed handoff bank')

    def next(self,node,i,jobs,omit=False,check=True):
        pc=node.pcs[i]
        if pc.phase not in self.PHASES_ALLOC:return super().next(node,i,jobs,omit,check)
        w=self.word(i,pc,jobs);raw=w[pc.pos//self.repeats];self.uses+=1
        if omit:K=node.J;ok=None;self.omissions+=1
        else:K,ok=self._raw(node.J,raw)
        nxt=replace(pc,pos=pc.pos+1)
        if nxt.pos==len(w)*self.repeats:
            t=jobs[i][pc.job][1]
            if pc.phase=='vacancy_write':nxt=self.begin(jobs[i],pc.job+1,pc.route)
            elif pc.phase=='vacancy_free':
                if self.C.observe_result(K):
                    payload=(0,0,tuple(range(self.C.slots)),0,(),())
                    nxt=gate.PC('vacancy_bit',pc.job,payload,route=pc.route)
                else:nxt=self.begin(jobs[i],pc.job+1,pc.route)
            else:
                bit=int(self.C.observe_result(K))
                k,prefix,active,at,zeros,ones=pc.target
                if bit:ones=ones+(active[at],)
                else:zeros=zeros+(active[at],)
                if at+1<len(active):
                    nxt=gate.PC('vacancy_bit',pc.job,(k,prefix,active,at+1,zeros,ones),route=pc.route)
                else:
                    selected,remaining,_=self.C.branch(t,k,prefix,(zeros,ones))
                    prefix|=selected<<k;k+=1
                    if remaining:
                        nxt=gate.PC('vacancy_bit',pc.job,(k,prefix,remaining,0,(),()),route=pc.route)
                    else:
                        c=self.C.leaf_color[t,k,prefix]
                        nxt=gate.PC('vacancy_write',pc.job,(c,bit),route=pc.route)
        pcs=list(node.pcs);pcs[i]=nxt
        out=gate.Node(K,tuple(pcs),node.turn)
        if check:self.invariant(out)
        return out,raw,ok,False

    def terminal(self,node,jobs,table,grants,phase=0):
        ck(all(pc.phase in ('done','busy') for pc in node.pcs),'finite attempts complete')
        ck(grants==tuple(range(len(grants))),'grants are the cyclic prefix')
        tab=table;cache=self.C.initial_cache(tab);last=None;answers={}
        for i in grants:
            value=None
            for op in jobs[i]:
                logical=('execute',op[1]) if op[0]=='feedback' else op
                tab,value,cache=a.expected(self.C,tab,cache,logical)
            answers[i]=value
            if jobs[i]:last=value
        want=self.C.encode(tab,last,cache)
        for i,v in enumerate(self.lanes):
            bank=phase^int(i in grants)
            want=m.canon(want+p.reg(v.admitted,int(i in grants)))
            if i in grants and jobs[i]:want=m.canon(want+p.reg(v.reply,int(answers[i])))
            if i!=node.turn:want=m.canon(want+(self.gate_pair[i][bank],))
            ck(node.pcs[i].route is None,'temporary route retired')
        ck(node.J==want,'exact source/current/ref/cache/gate/private-result endpoint')
        return answers


def costs():
    rows=[]
    for phase in (0,1):
        for t in range(3):
            G=VacancyRing(slots=6)
            # Empty target and all six historical labels except last retained.
            table=((None,)*3,tuple((t,c) for c in range(6)))
            node=G.initial_node(table,phase=phase);jobs=((('reserve',t),),())
            _,_,local=G.C.allocate(G.C.encode(table),t)
            node,n,grants=gate.complete(G,node,0,jobs)
            ck(n==local['commands']+31,'inherited wrapper adds 31 commands')
            first=n
            node,n2,gg=gate.complete(G,node,1,jobs)
            G.terminal(node,jobs,table,grants+gg,phase)
            rows.append(dict(phase=phase,target=t,commands=first,pass_commands=n2,members=G.members,candidates=len(G.H)))
    return dict(mode='ring_costs',rows=rows,assertions=CHECKS,inherited_gate_assertions=gate.CHECKS)


def graph(case='create_bind',repeats=3,budget=2,limit=200000):
    slots=1 if case!='create_copy' else 2
    G=VacancyRing(slots,2,repeats)
    if case=='create_bind':
        table=((None,None,0),((0,0),));jobs=((('reserve',0),),(('bind',0,0),))
    elif case=='create_create':
        table=((None,)*3,((0,0),));jobs=((('reserve',0),),(('reserve',0),))
    elif case=='create_copy':
        table=((None,None,0),((0,0),None));jobs=((('reserve',0),),(('copy',1,0),))
    else:raise ValueError(case)
    front={(G.initial_node(table),0,()):ONE};terms={};states=edges=0
    while front:
        nxt={}
        for (node,used,order),mass in front.items():
            states+=1
            if states>limit:raise RuntimeError('Declared graph limit exceeded')
            if all(pc.phase in ('done','busy') for pc in node.pcs):
                G.terminal(node,jobs,table,order)
                key=node,used,order;terms[key]=r.merge(terms.get(key,ZERO),mass);continue
            for i,pc in enumerate(node.pcs):
                if pc.phase in ('done','busy'):continue
                for skipped in range(2 if used<budget else 1):
                    nn,_,_,grant=G.next(node,i,jobs,bool(skipped));edges+=1
                    key=nn,used+skipped,order+((i,) if grant else ())
                    nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
        front=nxt
    masses={}
    for (_,used,_),value in terms.items():masses[used]=r.merge(masses.get(used,ZERO),value)
    return dict(mode='ring_graph',case=case,slots=slots,repeats=repeats,budget=budget,
                states=states,edges=edges,terminal_classes=len(terms),
                CWM={str(k):e.cw(v) for k,v in masses.items()},assertions=CHECKS,
                inherited_gate_assertions=gate.CHECKS,kernel_cache_misses=G.calls,
                primitive_attempts=G.uses,omission_edges=G.omissions)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['costs','graph']);ap.add_argument('--case',default='create_bind')
    ap.add_argument('--repeats',type=int,default=3);ap.add_argument('--budget',type=int,default=2);ap.add_argument('--out')
    x=ap.parse_args();ans=costs() if x.mode=='costs' else graph(x.case,x.repeats,x.budget)
    text=json.dumps(ans,ensure_ascii=False,indent=2)+'\n'
    if x.out:Path(x.out).write_text(text)
    else:print(text)
