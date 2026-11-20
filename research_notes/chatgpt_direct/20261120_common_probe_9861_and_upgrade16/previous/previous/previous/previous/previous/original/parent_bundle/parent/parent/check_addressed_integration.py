"""Primitive-granularity integration of context-addressed updates with the parent ring."""
from __future__ import annotations
from dataclasses import replace
from functools import lru_cache
from pathlib import Path
import argparse,json,sys
import check_addressed as a
sys.path.insert(0,str(Path(__file__).resolve().parent/'parent'))
import check_shared_integration as parent
base,p,m,e,r=a.base,a.p,a.m,a.e,a.r
ONE,ZERO=a.ONE,a.ZERO
gate=parent.gate
CHECKS=0

def ck(ok,msg):
    global CHECKS
    CHECKS+=1
    if not ok:raise AssertionError(msg)


def depth(node):
    return (node+1).bit_length()-1


def lsb_observations(node):
    """Decode the finite control node: no inspection of matching or request rows."""
    n=depth(node);prefix=node-((1<<n)-1);out=0
    for j in range(n):
        out |= ((prefix>>(n-1-j))&1)<<j
    return out


class AddressedRing(parent.SharedRing):
    PHASES=('address_present','address_low','address_full','address_write')
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
        if k<len(jobs):
            op=jobs[k]
            if op[0]=='bind':return gate.PC('address_present',k,route=route)
            if op[0]=='copy' and op[1]!=op[2]:return gate.PC('address_full',k,route=route)
        return super().begin(jobs,k,route)

    def word(self,i,pc,jobs):
        if pc.phase in self.PHASES:
            op=jobs[i][pc.job]
            if pc.phase=='address_present':return self.C.presence_reads[op[2]]
            if pc.phase=='address_low':return self.C.cache_reads[op[2],depth(pc.target)]
            if pc.phase=='address_full':return self.C.reads[op[2],depth(pc.target)]
            return self.C.address_writes[op[1],pc.target//2,pc.target%2]
        return super().word(i,pc,jobs)

    def invariant(self,node):
        super().invariant(node)
        for i,pc in enumerate(node.pcs):
            if pc.phase in self.PHASES:
                ck(self.lock(i) in node.J,'context reads and address writes hold the real token')
                nxt=(i+1)%self.actors
                banks=[b for b,h in enumerate(self.gate_pair[nxt]) if h in node.J]
                ck(len(banks)==1 and pc.route==(banks[0]^int(i==self.actors-1)),
                   'observed handoff bank remains valid throughout address update')

    def next(self,node,i,jobs,omit=False,check=True):
        pc=node.pcs[i]
        if pc.phase not in self.PHASES:return super().next(node,i,jobs,omit,check)
        w=self.word(i,pc,jobs);raw=w[pc.pos//self.repeats];self.uses+=1
        if omit:K=node.J;ok=None;self.omissions+=1
        else:K,ok=self._raw(node.J,raw)
        nxt=replace(pc,pos=pc.pos+1)
        if nxt.pos==len(w)*self.repeats:
            op=jobs[i][pc.job]
            if pc.phase=='address_write':
                nxt=self.begin(jobs[i],pc.job+1,pc.route)
            else:
                bit=int(self.C.observe_result(K))
                if pc.phase=='address_present':
                    nxt=(gate.PC('address_low',pc.job,route=pc.route) if bit else
                         gate.PC('address_write',pc.job,0,route=pc.route))
                else:
                    child=pc.target*2+1+bit
                    wanted=self.C.color_bits if pc.phase=='address_low' else self.C.bits
                    if depth(child)<wanted:nxt=gate.PC(pc.phase,pc.job,child,route=pc.route)
                    else:
                        code=lsb_observations(child)
                        if pc.phase=='address_low':
                            t=op[2]
                            code=self.C.key(t,self.C.decode_low[t][code])
                        if code>self.C.d*self.C.colors:raise ValueError('Out-of-domain exact key')
                        nxt=gate.PC('address_write',pc.job,2*code+bit,route=pc.route)
        pcs=list(node.pcs);pcs[i]=nxt
        out=gate.Node(K,tuple(pcs),node.turn)
        if check:self.invariant(out)
        return out,raw,ok,False


def costs():
    rows=[]
    for phase in (0,1):
        for op in (('bind',0,0),('bind',0,1),('bind',0,2),('copy',1,0),('copy',0,0)):
            G=AddressedRing(slots=6);table=((0,None,0),((0,0),)+(None,)*5)
            node=G.initial_node(table,phase=phase);jobs=((op,),())
            initial=base.ref.old.seed(node.J)
            protected={h:n for h,n in initial.events if h in G.C.targets}
            node,n,order=gate.complete(G,node,0,jobs,ann=[initial,protected])
            ck(n==a.expected_word_length(G.C,op,table)+31,'wrapper cost is 31 unchanged')
            ck(G.C.decode(G.core(node.J))==base.expected(G.C,table,op),'protected update exact semantic endpoint')
            firstn=n
            node,n2,order2=gate.complete(G,node,1,jobs)
            G.terminal(node,jobs,table,order+order2,phase)
            rows.append(dict(phase=phase,op=op,commands=firstn,second_pass=n2,members=G.members,candidates=len(G.H)))
    return dict(mode='ring_costs',rows=rows,assertions=CHECKS,inherited_gate_assertions=gate.CHECKS)


def graph(case='bind_restart',repeats=3,budget=2,limit=200000):
    slots=2 if case=='copy_rebind' else 1
    G=AddressedRing(slots,2,repeats)
    table=((0,None,0),((0,0),)+(None,)*(slots-1))
    cases={
      'bind_restart':((('bind',0,0),),(('release',1),('reserve',0))),
      'copy_rebind':((('copy',1,0),),(('bind',0,2),)),
      'execute_bind':((('feedback',0),),(('bind',0,2),)),
      'retire_absent':((('release',1),),(('bind',0,0),)),
    }
    jobs=cases[case]
    front={(G.initial_node(table),0,()):ONE};terms={};states=edges=0
    while front:
        nxt={}
        for (node,used,order),mass in front.items():
            states+=1
            if states>limit:raise RuntimeError('Declared graph limit reached')
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
    for (_,used,_),v in terms.items():masses[used]=r.merge(masses.get(used,ZERO),v)
    return dict(mode='ring_graph',case=case,slots=slots,repeats=repeats,budget=budget,
                states=states,edges=edges,terminal_classes=len(terms),
                CWM={str(k):e.cw(v) for k,v in masses.items()},
                assertions=CHECKS,parent_wrapper_assertions=parent.CHECKS,inherited_gate_assertions=gate.CHECKS,
                kernel_cache_misses=G.calls,primitive_attempts=G.uses,omission_edges=G.omissions)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=('costs','graph'))
    ap.add_argument('--case',default='bind_restart');ap.add_argument('--repeats',type=int,default=3)
    ap.add_argument('--budget',type=int,default=2);ap.add_argument('--out');a0=ap.parse_args()
    ans=costs() if a0.mode=='costs' else graph(a0.case,a0.repeats,a0.budget)
    text=json.dumps(ans,ensure_ascii=False,indent=2)+'\n'
    if a0.out:Path(a0.out).write_text(text)
    else:print(text)
