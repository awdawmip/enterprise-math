"""Protected integration and validated hints for the triadic target directory."""
from __future__ import annotations
from dataclasses import replace
from functools import lru_cache
from pathlib import Path
import argparse,json
import check_route_index as ix
CType=ix.Compiler
base,p,m,e,r=ix.base,ix.p,ix.m,ix.e,ix.r
ONE,ZERO=ix.ONE,ix.ZERO
gate=ix.old.gate
CHECKS=0

def ck(v,message):
    global CHECKS
    CHECKS+=1
    if not v:raise AssertionError(message)

def hint_dispatch(C,J,i,trace=False):
    """Directory is only a suggestion. Failed check falls back to old scan.

    Index triples can encode any value independently of the request. Source,
    request and original current tables must still satisfy the original API.
    """
    code=0;word=[];mass=e.prep(J);logs=[];reads=0
    def do(w):
        nonlocal J,mass
        J,wm,log=C.runword(J,w,trace);mass=r.serial(mass,wm);word.extend(w);logs.extend(log)
    for b in range(C.bits):
        do(C.reads[i,b]);code|=int(C.observe_result(J))<<b;reads+=1
    hit=False
    if 1<=code<=C.d:
        do(C.programs['match',i,code-1]);reads+=1
        hit=C.observe_result(J)
        if hit:do(C.commit(code-1))
    if not hit:
        J,wm,data=ix.feedback.Compiler.feedback(C,J,i,trace)
        mass=r.serial(mass,wm);word.extend(data['word']);logs.extend(data['trace']);reads+=data['feedback_reads']
    return J,mass,dict(code=code,hit=hit,reads=reads,commands=len(word),word=tuple(word),trace=logs)

def hints():
    C=CType(slots=2);F=ix.feedback.Compiler(slots=2);count=0;mass=ZERO;hit=0
    for tab in base.domain(C):
        for i in range(C.slots):
            original=F.encode(tab);baseline,_,_=F.feedback(original,i)
            for code in range(1<<C.bits):
                J,_,_=C.runword(C.encode(tab),C.clear_index(i))
                J,_,_=C.runword(J,tuple(p.add(C.index[i][b]) for b in range(C.bits) if code>>b&1))
                tags=tuple(h for h in J if h not in C.strip_index(J))
                K,wm,data=hint_dispatch(C,J,i)
                ck(C.strip_index(K)==baseline,'arbitrary well-formed hint preserves exact original execute result')
                ck(tuple(h for h in K if h not in C.strip_index(K))==tags,'hint preserved even when outdated')
                q=tab[1][i];valid=q is not None and tab[0][q[0]]==q[1]
                ck(data['hit']==bool(valid and code==q[0]+1),'a hit always verified against original target and instance')
                hit+=int(data['hit']);count+=1;mass=r.merge(mass,wm)
    # A genuine out-of-range code is a miss rather than an interpretation.
    X=CType(H=((1,2,3),(4,5,6)),slots=1);tab=((0,0),((0,0),));J=X.encode(tab)
    J,_,_=X.runword(J,X.clear_index(0)+[p.add(h) for h in X.index[0]])
    K,_,data=hint_dispatch(X,J,0)
    target=base.expected(X,tab,('execute',0))
    ck(X.strip_index(K)==base.Compiler.encode(X,*target),'reserved code falls back correctly')
    return dict(mode='hints',full_domain=1900,cases=count,verified_hits=hit,CWM=e.cw(mass),
                out_of_range_case=data['code'],assertions=CHECKS,kernel_cache_misses=C.calls,primitive_uses=C.uses)

class IndexRing(gate.PhaseRing):
    def __init__(self,slots=1,actors=2,repeats=1):
        super().__init__(slots,actors,repeats)
        start=max(x for h in self.H for x in h)+1
        self.C=CType(slots=slots,index_start=start)
        self.H=frozenset(set(self.H)|set(self.C.H))
        self.core_members=frozenset(x for h in self.C.H for x in h)
        self.members=len({x for h in self.H for x in h})
        self._raw=lru_cache(maxsize=500000)(self._uncached)
        self.calls=self.uses=self.omissions=0
    def begin(self,jobs,k,route):
        if k==len(jobs):return gate.PC('publish',k,route=route) if jobs else gate.PC('handoff',route=route)
        return gate.PC('index' if jobs[k][0]=='feedback' else 'fixed',k,route=route)
    def word(self,i,pc,jobs):
        if pc.phase=='index':
            depth=(pc.target+1).bit_length()-1
            return self.C.reads[jobs[i][pc.job][1],self.C.bits-1-depth]
        return super().word(i,pc,jobs)
    def invariant(self,node):
        super().invariant(node)
        for i,pc in enumerate(node.pcs):
            if pc.phase=='index':
                ck(self.lock(i) in node.J,'directory reads hold actual shared token')
                j=(i+1)%self.actors
                banks=[b for b,h in enumerate(self.gate_pair[j]) if h in node.J]
                ck(len(banks)==1 and pc.route==(banks[0]^int(i==self.actors-1)), 'index read preserves phase relation')
    def next(self,node,i,jobs,omit=False,check=True):
        pc=node.pcs[i]
        if pc.phase not in ('index','match'):return super().next(node,i,jobs,omit,check)
        w=self.word(i,pc,jobs);raw=w[pc.pos//self.repeats];self.uses+=1
        if omit:K=node.J;ok=None;self.omissions+=1
        else:K,ok=self._raw(node.J,raw)
        nxt=replace(pc,pos=pc.pos+1)
        if nxt.pos==len(w)*self.repeats:
            bit=self.C.observe_result(K)
            if pc.phase=='index':
                child=2*pc.target+1+int(bit);depth=(child+1).bit_length()-1
                if depth==self.C.bits:
                    code=child-((1<<self.C.bits)-1)
                    if code>self.C.d:raise ValueError('Invalid exact route code')
                    nxt=gate.PC('match',pc.job,code-1,route=pc.route) if code else self.begin(jobs[i],pc.job+1,pc.route)
                else:nxt=gate.PC('index',pc.job,child,route=pc.route)
            else:nxt=gate.PC('commit',pc.job,pc.target,route=pc.route) if bit else self.begin(jobs[i],pc.job+1,pc.route)
        pcs=list(node.pcs);pcs[i]=nxt;out=gate.Node(K,tuple(pcs),node.turn)
        if check:self.invariant(out)
        return out,raw,ok,False

def ring_costs():
    rows=[]
    for phase in (0,1):
        for name,cur,q in [('A',(0,None,0),(0,0)),('B',(None,0,None),(1,0)),
                           ('C',(0,None,0),(2,0)),('stale',(1,None,0),(0,0)),('empty',(0,None,0),None)]:
            G=IndexRing(6,2);tab=cur,(q,)+(None,)*5;jobs=((('feedback',0),),())
            node=G.initial_node(tab,phase=phase);st=base.ref.old.seed(node.J)
            want=base.expected(G.C,tab,('execute',0));deleted=G.C.targets[q[0]] if want[1] else None
            protected={h:n for h,n in st.events if h in G.C.targets and h!=deleted}
            node,steps,order=gate.complete(G,node,0,jobs,ann=[st,protected])
            ck(G.C.decode(G.core(node.J))==want,'protected source and maintained directory')
            ck(gate.old.bit(node.J,G.lanes[0].reply)==want[1],'private complete response')
            ck(steps==31+8*G.C.bits+(4*G.C.colors+9 if q else 0)+(2 if want[1] else 0),'complete wrapper cost')
            rows.append(dict(name=name,phase=phase,steps=steps,members=G.members,candidates=len(G.H)))
    return dict(mode='ring_costs',rows=rows,assertions=CHECKS,gate_assertions=gate.CHECKS)

def ring_graph(repeats=3,budget=2,case='execute_bind'):
    G=IndexRing(1,2,repeats);tab=((0,None,0),((0,0),))
    choices={'execute_bind':((('feedback',0),),(('bind',0,2),)),
             'execute_restart':((('feedback',0),),(('release',1),('reserve',0))),
             'execute_execute':((('feedback',0),),(('feedback',0),))}
    jobs=choices[case];node=G.initial_node(tab);front={(node,0,()):ONE};terms={};states=edges=0
    while front:
        nxt={}
        for (state,used,order),mass in front.items():
            states+=1
            if states>350000:raise RuntimeError('Graph exceeds declared execution budget')
            if all(pc.phase in ('done','busy') for pc in state.pcs):
                G.terminal(state,jobs,tab,order)
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
                assertions=CHECKS,gate_assertions=gate.CHECKS,kernel_cache_misses=G.calls,
                transition_attempts=G.uses,omission_edges=G.omissions)

def workload():
    """Executed fresh bind-and-execute costs, plus full weighted query traces."""
    C=CType(slots=6);F=ix.old.Compiler(slots=6);L=ix.feedback.Compiler(slots=6)
    rows=[]
    for t in range(3):
        cur=(None,0,None) if t==1 else (0,None,0)
        table=cur,(None,)*6
        N,_,_=C.run(C.encode(table),('bind',0,t));N,_,data=C.dispatch(N,0)
        O,_,_=F.run(F.encode(table),('bind',0,t));O,_,pd=F.dispatch(O,0)
        Z,_,_=L.run(L.encode(table),('bind',0,t));Z,_,ld=L.feedback(Z,0)
        ck(C.strip_index(N)==O==Z,'same complete bind-and-execute endpoint')
        rows.append(dict(target=t,indexed=len(C.programs['bind',0,t])+data['commands'],
                         balanced=len(F.programs['bind',0,t])+pd['commands'],
                         linear=len(L.programs['bind',0,t])+ld['commands']))
    # Stable explicit prepared workload; mass is positive provenance, not an
    # estimate of a physical probability distribution.
    paths=[]
    for lab,cur,q in [('A',(0,None,0),(0,0)),('B',(None,0,None),(1,0)),
                      ('C',(0,None,0),(2,0)),('stale',(0,None,0),(1,0))]:
        tab=cur,(q,)+(None,)*5;_,wm,di=C.dispatch(C.encode(tab),0)
        paths.append((wm,di['commands']))
    groups=[]
    for weights in ((1,1,1,1),(80,10,5,5)):
        mass=ZERO;total=0
        for (wm,length),w in zip(paths,weights):
            for _ in range(w):mass=r.merge(mass,wm)
            total+=w*length
        groups.append(dict(weights=weights,commands=total,mean=total/sum(weights),CWM=e.cw(mass)))
    return dict(mode='workload',fresh_bind_execute=rows,prepared_workloads=groups,
                retrofit_commands_per_slot=86,assertions=CHECKS)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['hints','ring_costs','ring_graph','workload'])
    ap.add_argument('--case',default='execute_bind');ap.add_argument('--repeats',type=int,default=3)
    ap.add_argument('--budget',type=int,default=2);ap.add_argument('--out');a=ap.parse_args()
    ans=ring_graph(a.repeats,a.budget,a.case) if a.mode=='ring_graph' else globals()[a.mode]()
    text=json.dumps(ans,ensure_ascii=False,indent=2)+'\n'
    if a.out:Path(a.out).write_text(text)
    else:print(text)
