"""Protected full-key lookup, reusing the original fair triadic entry."""
from __future__ import annotations
from dataclasses import replace
from functools import lru_cache
from pathlib import Path
import argparse,json,sys
import check_identity_index as ix
sys.path.insert(0,str(Path(__file__).resolve().parent/'parent'))
import check_index_integration as parent_integration
base,p,m,e,r = ix.base,ix.p,ix.m,ix.e,ix.r
ONE,ZERO=ix.ONE,ix.ZERO
gate=parent_integration.gate
CHECKS=0

def ck(v,message):
    global CHECKS
    CHECKS+=1
    if not v:raise AssertionError(message)

class IdentityRing(gate.PhaseRing):
    def __init__(self,slots=1,actors=2,repeats=1):
        super().__init__(slots,actors,repeats)
        start=max(x for h in self.H for x in h)+1
        self.C=ix.Compiler(slots=slots,index_start=start)
        self.H=frozenset(set(self.H)|set(self.C.H))
        self.core_members=frozenset(x for h in self.C.H for x in h)
        self.members=len({x for h in self.H for x in h})
        self._raw=lru_cache(maxsize=500000)(self._uncached)
        self.calls=self.uses=self.omissions=0
    def begin(self,jobs,k,route):
        if k==len(jobs):return gate.PC('publish',k,route=route) if jobs else gate.PC('handoff',route=route)
        return gate.PC('key_index' if jobs[k][0]=='feedback' else 'fixed',k,route=route)
    def word(self,i,pc,jobs):
        if pc.phase=='key_index':
            depth=(pc.target+1).bit_length()-1
            return self.C.reads[jobs[i][pc.job][1],self.C.bits-1-depth]
        if pc.phase=='key_current':
            return self.C.current_reads[divmod(pc.target,self.C.colors)]
        return super().word(i,pc,jobs)
    def invariant(self,node):
        super().invariant(node)
        for i,pc in enumerate(node.pcs):
            if pc.phase in ('key_index','key_current'):
                ck(self.lock(i) in node.J,'key read/current verification holds real shared token')
                j=(i+1)%self.actors
                banks=[b for b,h in enumerate(self.gate_pair[j]) if h in node.J]
                ck(len(banks)==1 and pc.route==(banks[0]^int(i==self.actors-1)), 'key phases preserve phase handoff invariant')
    def next(self,node,i,jobs,omit=False,check=True):
        pc=node.pcs[i]
        if pc.phase not in ('key_index','key_current'):
            return super().next(node,i,jobs,omit,check)
        w=self.word(i,pc,jobs);raw=w[pc.pos//self.repeats];self.uses+=1
        if omit:K=node.J;ok=None;self.omissions+=1
        else:K,ok=self._raw(node.J,raw)
        nxt=replace(pc,pos=pc.pos+1)
        if nxt.pos==len(w)*self.repeats:
            bit=self.C.observe_result(K)
            if pc.phase=='key_index':
                child=2*pc.target+1+int(bit);depth=(child+1).bit_length()-1
                if depth==self.C.bits:
                    code=child-((1<<self.C.bits)-1)
                    if code>self.C.d*self.C.colors:raise ValueError('Invalid exact key')
                    nxt=gate.PC('key_current',pc.job,code-1,route=pc.route) if code else self.begin(jobs[i],pc.job+1,pc.route)
                else:nxt=gate.PC('key_index',pc.job,child,route=pc.route)
            else:
                target=pc.target//self.C.colors
                nxt=gate.PC('commit',pc.job,target,route=pc.route) if bit else self.begin(jobs[i],pc.job+1,pc.route)
        pcs=list(node.pcs);pcs[i]=nxt
        out=gate.Node(K,tuple(pcs),node.turn)
        if check:self.invariant(out)
        return out,raw,ok,False


def ring_costs():
    rows=[]
    for phase in (0,1):
        for name,cur,q in [('A',(0,None,0),(0,0)),('B',(None,0,None),(1,0)),
                           ('C',(0,None,0),(2,0)),('stale',(1,None,0),(0,0)),('empty',(0,None,0),None)]:
            G=IdentityRing(6,2);table=cur,(q,)+(None,)*5;jobs=((('feedback',0),),())
            node=G.initial_node(table,phase=phase);st=base.ref.old.seed(node.J)
            want=base.expected(G.C,table,('execute',0));deleted=G.C.targets[q[0]] if want[1] else None
            protected={h:n for h,n in st.events if h in G.C.targets and h!=deleted}
            node,steps,order=gate.complete(G,node,0,jobs,ann=[st,protected])
            ck(G.C.decode(G.core(node.J))==want,'protected maintained-key business endpoint')
            ck(gate.old.bit(node.J,G.lanes[0].reply)==want[1],'private complete business reply')
            ck(steps==31+8*G.C.bits+(8 if q else 0)+(2 if want[1] else 0),'protected path length')
            rows.append(dict(name=name,phase=phase,steps=steps,members=G.members,candidates=len(G.H)))
    return dict(mode='ring_costs',rows=rows,assertions=CHECKS,inherited_gate_assertions=gate.CHECKS)


def ring_graph(repeats=3,budget=2,case='execute_bind'):
    G=IdentityRing(1,2,repeats);table=((0,None,0),((0,0),))
    choices={'execute_bind':((('feedback',0),),(('bind',0,2),)),
             'execute_restart':((('feedback',0),),(('release',1),('reserve',0))),
             'execute_execute':((('feedback',0),),(('feedback',0),))}
    jobs=choices[case];node=G.initial_node(table)
    front={(node,0,()):ONE};terms={};states=edges=0
    while front:
        nxt={}
        for (state,used,order),mass in front.items():
            states+=1
            if states>300000:raise RuntimeError('Declared graph size budget exceeded')
            if all(pc.phase in ('done','busy') for pc in state.pcs):
                G.terminal(state,jobs,table,order)
                key=state,used,order;terms[key]=r.merge(terms.get(key,ZERO),mass);continue
            for i,pc in enumerate(state.pcs):
                if pc.phase in ('done','busy'):continue
                for omission in range(2 if used<budget else 1):
                    nn,raw,ok,grant=G.next(state,i,jobs,bool(omission));edges+=1
                    oo=order+((i,) if grant else ())
                    key=nn,used+omission,oo
                    nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
        front=nxt
    masses={}
    for (state,used,order),mass in terms.items():masses[used]=r.merge(masses.get(used,ZERO),mass)
    return dict(mode='ring_graph',case=case,repeats=repeats,budget=budget,states=states,edges=edges,
                terminal_classes=len(terms),CWM={str(k):e.cw(v) for k,v in masses.items()},
                assertions=CHECKS,inherited_gate_assertions=gate.CHECKS,
                kernel_cache_misses=G.calls,primitive_attempts=G.uses,omission_edges=G.omissions)


def empty_filter():
    C=ix.Compiler(slots=6);rows=[]
    for label,cur,q in [('A',(0,None,0),(0,0)),('stale',(1,None,0),(0,0)),('empty',(0,None,0),None)]:
        table=cur,(q,)+(None,)*5;J=C.encode(table)
        K,_,_=C.runword(J,C.programs['present',0]);cost=len(C.programs['present',0])
        if C.observe_result(K):K,_,data=C.dispatch(K,0);cost+=data['commands']
        ck(C.decode(K)==base.expected(C,table,('execute',0)),'early presence filter is semantics preserving')
        rows.append(dict(label=label,commands=cost))
    return dict(mode='empty_filter',rows=rows,empty_fraction_benefit='p_empty > 1/q, q=5 in this instance',assertions=CHECKS)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=('ring_costs','ring_graph','empty_filter'))
    ap.add_argument('--case',default='execute_bind');ap.add_argument('--out');a=ap.parse_args()
    result=ring_graph(case=a.case) if a.mode=='ring_graph' else globals()[a.mode]()
    text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if a.out:Path(a.out).write_text(text)
    else:print(text)
