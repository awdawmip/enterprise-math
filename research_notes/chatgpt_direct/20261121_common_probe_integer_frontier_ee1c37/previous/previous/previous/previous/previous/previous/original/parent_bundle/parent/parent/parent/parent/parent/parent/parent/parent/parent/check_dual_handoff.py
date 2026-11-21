"""Two release ports per cyclic gate; finite local phase and original BRC steps.

Controller branches only on complete inherited result registers. Local phase
changes once, after the entire successful handoff call has returned. The turn
field below is a test-only monitor; production word selection never reads it.
Original reserve/release semantics and positive CWM operations are inherited.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from collections import deque
from functools import lru_cache
from pathlib import Path
import argparse, json, sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_fair_handoff as parent
old=parent.parent
base,p,m,e,r=parent.base,parent.p,parent.m,parent.e,parent.r
ONE,ZERO=parent.ONE,parent.ZERO
CHECKS=0

def ck(value, message):
    global CHECKS
    CHECKS+=1
    if not value: raise AssertionError(message)

@dataclass(frozen=True)
class PC:
    phase:str='entry'
    job:int=0
    target:int=0
    pos:int=0
    bank:int=0

@dataclass(frozen=True)
class Node:
    J:tuple
    pcs:tuple[PC,...]
    turn:int=0  # independent cyclic-order monitor, not an execution input

class DualRing(parent.FairGuard):
    def __init__(self,slots=1,actors=2,repeats=1):
        if not isinstance(repeats,int) or repeats<1: raise ValueError('positive repeats required')
        super().__init__(slots,actors)
        self.old_members=self.members
        self.old_candidates=len(self.H)
        self.repeats=repeats
        start=max(frozenset().union(*(frozenset(h) for h in self.H)))+1
        self.release_ports=tuple((self.gate_ports[i][0],start+i) for i in range(actors))
        self.gate_pair=tuple((self.gates[i],tuple(sorted((self.lanes[i].a,self.gate_ports[i][1],start+i))))
                             for i in range(actors))
        self.H=frozenset(set(self.H)|{x[1] for x in self.gate_pair})
        self.members=len(frozenset().union(*(frozenset(h) for h in self.H)))
        self.handoffs=tuple(tuple((p.one(self.lanes[i].a),p.add(self.gate_pair[i][1-b]),
                                     p.one(self.release_ports[(i+1)%actors][b ^ int(i==actors-1)]))
                                   for b in (0,1)) for i in range(actors))
        self.calls=self.uses=self.omissions=0
        self._raw=lru_cache(maxsize=500000)(self._uncached)

    def initial_node(self,table,turn=0,old_result=None):
        # Starting cyclic phase is defined for turn 0; arbitrary starts are rotations
        # of the participant labels, not a hidden reinitialization of private bits.
        if turn!=0: raise ValueError('canonical initial owner is 0')
        J=m.canon(self.C.encode(table,old_result)+tuple(self.gate_pair[i][0] for i in range(1,self.actors)))
        return Node(J,tuple(PC() for _ in range(self.actors)),0)

    def begin(self,jobs,k,bank):
        if k==len(jobs): return PC('publish',k,bank=bank) if jobs else PC('handoff',bank=bank)
        return PC('match' if jobs[k][0]=='feedback' else 'fixed',k,bank=bank)

    def word(self,i,pc,jobs):
        if pc.phase=='handoff':return self.handoffs[i][pc.bank]
        if pc.phase=='publish':return self.publish[i]
        return old.Guard.word(self,i,pc,jobs)

    def invariant(self,node):
        owners=[i for i in range(self.actors) if self.lock(i) in node.J]
        opened=[i for i,pair in enumerate(self.gate_pair) if not any(h in node.J for h in pair)]
        ck(len(owners)<=1,'shared token maintains mutual exclusion')
        ck(len(opened)<=1,'at most one physical turn gate is open')
        ck(all(i in opened for i in owners),'token holder is the physically open participant')
        for i,pair in enumerate(self.gate_pair):
            ck(sum(h in node.J for h in pair)<=1,'one of the two gate encodings, never both')
        active=[i for i,pc in enumerate(node.pcs) if pc.phase in ('fixed','match','commit','publish')]
        ck(len(active)<=1,'only one shared business/copy context')
        ck(all(self.lock(i) in node.J for i in active),'all business remains under its actual token')

    def next(self,node,i,jobs,omit=False,check=True):
        pc=node.pcs[i]
        if pc.phase in ('done','busy'): raise ValueError('caller must rearm completed attempt')
        word=self.word(i,pc,jobs)
        raw=word[pc.pos//self.repeats]
        self.uses+=1
        if omit:
            self.omissions+=1;K=node.J;ok=None
        else:K,ok=self._raw(node.J,raw)
        new=replace(pc,pos=pc.pos+1)
        grant=False;turn=node.turn
        if new.pos==self.repeats*len(word):
            if pc.phase=='entry':
                got=old.bit(K,self.lanes[i].admitted)
                if check:ck(got==(self.lock(i) in K),'complete entry evidence exactly identifies own token')
                new=self.begin(jobs[i],0,pc.bank) if got else PC('busy',bank=pc.bank)
                grant=got
                if got:
                    if check:ck(i==node.turn,'grant follows the specified cyclic order')
                    turn=(i+1)%self.actors
            elif pc.phase in ('fixed','commit'):
                new=self.begin(jobs[i],pc.job+1,pc.bank)
            elif pc.phase=='match':
                value=self.C.observe_result(K)
                if value:new=PC('commit',pc.job,pc.target,bank=pc.bank)
                elif pc.target+1<self.C.d:new=PC('match',pc.job,pc.target+1,bank=pc.bank)
                else:new=self.begin(jobs[i],pc.job+1,pc.bank)
            elif pc.phase=='publish':new=PC('handoff',pc.job,bank=pc.bank)
            elif pc.phase=='handoff':new=PC('done',pc.job,bank=1-pc.bank)
        pcs=list(node.pcs);pcs[i]=new
        ans=Node(K,tuple(pcs),turn)
        if check:self.invariant(ans)
        return ans,raw,ok,grant

    def rearm(self,node,i):
        ck(node.pcs[i].phase in ('done','busy'),'old call must drain before same participant reenters')
        pcs=list(node.pcs);pcs[i]=PC(bank=pcs[i].bank)
        return Node(node.J,tuple(pcs),node.turn)

    def terminal(self,node,jobs,table,grants):
        ck(all(pc.phase in ('done','busy') for pc in node.pcs),'finite attempts are complete')
        ck(grants==tuple(range(len(grants))),'finite grant history is a cyclic prefix from zero')
        tab=table;last=None;ans={}
        for i in grants:
            value=None
            for op in jobs[i]:tab,value=base.expected(self.C,tab,('execute',op[1]) if op[0]=='feedback' else op)
            ans[i]=value
            if jobs[i]:last=value
        want=self.C.encode(tab,last)
        for i,v in enumerate(self.lanes):
            want=m.canon(want+p.reg(v.admitted,int(i in grants)))
            if i in grants and jobs[i]:want=m.canon(want+p.reg(v.reply,int(ans[i])))
            if i!=node.turn:want=m.canon(want+(self.gate_pair[i][node.pcs[i].bank],))
        ck(node.J==want,'exact persistent source/table/results/gates with all private work cleared')
        return {str(i):('WAIT_TURN' if i not in grants else ('PASS' if not jobs[i] else ans[i])) for i in range(self.actors)}

    def stats(self):
        return dict(assertions=CHECKS,kernel_calls=self.calls,primitive_uses=self.uses,omission_edges=self.omissions,
                    slots=self.C.slots,actors=self.actors,repeats=self.repeats,members=self.members,
                    candidates=len(self.H),parent_members=self.old_members,parent_candidates=self.old_candidates,
                    local_phase_bits=self.actors)

def complete(G,node,i,jobs,trace=None,ann=None,omits=frozenset()):
    steps=0;grants=[]
    while node.pcs[i].phase not in ('done','busy'):
        before=node
        omission=steps in omits
        node,raw,ok,grant=G.next(node,i,jobs,omit=omission)
        if grant:grants.append(i)
        if ann is not None and not omission:
            ann[0],_,delta=base.ref.old.raw_step(ann[0],raw,G.H)
            ck(ann[0].matching==node.J,'creation annotations reuse exact same primitive transition')
            for h,identity in ann[1].items():ck(ann[0].names().get(h)==identity,'protected source event persists at every primitive')
        if trace is not None:trace.append(dict(actor=i,phase=before.pcs[i].phase,pos=before.pcs[i].pos,
          bank=before.pcs[i].bank,raw=raw,omitted=omission,grant=grant,next_phase=node.pcs[i].phase,
          gates=[[(list(h)) for h in pair if h in node.J] for pair in G.gate_pair]))
        steps+=1
    return node,steps,tuple(grants)

def costs():
    rows=[]
    G=DualRing(6,2)
    for name,cur,ref in [('A',(0,None,0),(0,0)),('B',(None,0,None),(1,0)),
                         ('C',(0,None,0),(2,0)),('stale',(0,None,0),(1,0))]:
        table=(cur,(ref,)+(None,)*5);jobs=((('feedback',0),),())
        node=G.initial_node(table);st=base.ref.old.seed(node.J)
        valid=base.expected(G.C,table,('execute',0))[1]
        delete=G.C.targets[ref[0]] if valid else None
        protected={h:n for h,n in st.events if h in G.C.targets and h!=delete}
        node,steps,grants=complete(G,node,0,jobs,ann=[st,protected])
        ck(G.C.decode(G.core(node.J))==base.expected(G.C,table,('execute',0)),'exact business result')
        rows.append(dict(name=name,steps=steps,response=old.bit(node.J,G.lanes[0].reply)))
    ck([x['steps'] for x in rows]==[62,99,136,134],'no extra unprotected primitive calls')
    return dict(mode='costs',paths=rows,**G.stats())

def delayed_suffix():
    """Receiver finishes a full round between two actual old opening calls."""
    G=DualRing(6,2,2);table=((0,None,0),((0,0),)+(None,)*5)
    jobs=((('feedback',0),),(('reserve',0),));node=G.initial_node(table);trace=[]
    st=base.ref.old.seed(node.J);ann=[st,{G.C.targets[2]:st.names()[G.C.targets[2]]}]
    grants=[];steps=0
    # Leave sender after first of its two opening releases, before the second.
    while not(node.pcs[0].phase=='handoff' and node.pcs[0].pos==5):
        before=node;node,raw,ok,g=G.next(node,0,jobs);steps+=1
        if g:grants.append(0)
        ann[0],_,_=base.ref.old.raw_step(ann[0],raw,G.H)
        ck(ann[0].matching==node.J,'annotated prefix agrees')
        ck(ann[0].names().get(G.C.targets[2])==ann[1][G.C.targets[2]],'C birth preserved')
        trace.append(dict(actor=0,phase=before.pcs[0].phase,pos=before.pcs[0].pos,raw=raw,grant=g))
    before_receiver=node
    node,s,gs=complete(G,node,1,jobs,trace,ann);steps+=s;grants+=list(gs)
    ck(G.gate_pair[1][1] in node.J,'receiver closes the other release bank')
    old_address=G.release_ports[1][0]
    ck(not any(old_address in h for h in node.J),'old opening address is now genuinely free')
    stable=node.J
    node,s,gs=complete(G,node,0,jobs,trace,ann);steps+=s;grants+=list(gs)
    ck(node.J==stable,'late old opening call is an exact identity on matching')
    node=G.rearm(node,1)
    node,s,gs=complete(G,node,1,jobs,trace,ann);steps+=s;grants+=list(gs)
    ck(node.pcs[1].phase=='busy','receiver cannot acquire two consecutive turns')
    node=G.rearm(node,0)
    node,s,gs=complete(G,node,0,jobs,trace,ann);steps+=s;grants+=list(gs)
    ck(grants==[0,1,0],'protected handoff retains cyclic succession')
    ck(old.bit(node.J,G.lanes[0].reply)==False,'old A request rejected after real recreation')
    return dict(mode='delayed_suffix',order=grants,steps=steps,trace=trace,**G.stats())

def finite_graph(repeats=1,omission_budget=0,case='pass',actors=2,max_states=700000):
    G=DualRing(1,actors,repeats)
    table=((0,None,0),((0,0),))
    cases={'pass':((),()),'execute_restart':((('feedback',0),),(('release',1),('reserve',0))),
           'execute_execute':((('feedback',0),),(('feedback',0),)),
           'execute_bind':((('feedback',0),),(('bind',0,2),))}
    jobs=tuple(() for _ in range(actors)) if case=='pass' else cases[case]
    start=G.initial_node(table)
    D={(start,(),0):e.prep(start.J)};states=edges=0;ends={}
    while D:
        states+=len(D)
        if states>max_states:raise RuntimeError('finite graph limit reached')
        nxt={}
        for (node,grants,used),mass in D.items():
            if all(pc.phase in ('done','busy') for pc in node.pcs):
                answers=G.terminal(node,jobs,table,grants)
                key=(node,grants,used)
                ends[key]=r.merge(ends.get(key,ZERO),mass)
                continue
            for i,pc in enumerate(node.pcs):
                if pc.phase in ('done','busy'):continue
                for skip in range(2 if used<omission_budget else 1):
                    q,_,_,got=G.next(node,i,jobs,omit=bool(skip))
                    key=(q,grants+((i,) if got else ()),used+skip)
                    nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE));edges+=1
        D=nxt
    totals={}
    for (_,__,k),mass in ends.items():totals[k]=r.merge(totals.get(k,ZERO),mass)
    return dict(mode='finite',case=case,states=states,edges=edges,classes=len(ends),
                weights_by_omissions={str(k):e.cw(v) for k,v in totals.items()},**G.stats())

def recurrent(repeats=2,actors=2,max_states=250000):
    import networkx as nx
    G=DualRing(1,actors,repeats);jobs=tuple(() for _ in range(actors))
    start=G.initial_node(((None,)*3,(None,)))
    nodes=[start];idx={start:0};queue=deque([0]);adj=[]
    while queue:
        key=queue.popleft();node=nodes[key];out=[]
        for i in range(actors):
            nxt,raw,ok,grant=G.next(node,i,jobs)
            if nxt.pcs[i].phase in ('done','busy'):nxt=G.rearm(nxt,i)
            if nxt not in idx:
                idx[nxt]=len(nodes);nodes.append(nxt);queue.append(idx[nxt])
                if len(nodes)>max_states:raise RuntimeError('recurrent graph limit reached')
            out.append((idx[nxt],i,grant))
        adj.append(out)
    analyses=[]
    for victim in range(actors):
        D=nx.DiGraph();D.add_nodes_from(range(len(nodes)))
        for u,out in enumerate(adj):
            for v,i,grant in out:
                if not(grant and i==victim):D.add_edge(u,v)
        bad=[];cyclic=0
        for comp in nx.strongly_connected_components(D):
            if len(comp)==1 and not D.has_edge(next(iter(comp)),next(iter(comp))):continue
            cyclic+=1;seen=set()
            for u in comp:
                for v,i,grant in adj[u]:
                    if v in comp and not(grant and i==victim):seen.add(i)
            if len(seen)==actors:bad.append(len(comp))
        ck(not bad,'no weakly fair recurrent component can omit this participant forever')
        analyses.append(dict(victim=victim,cyclic_components=cyclic,bad_components=bad))
    # Exact finite-prefix schedule multiplicities on the actual original-step graph.
    depth=18
    mass={0:e.prep(start.J)}
    for _ in range(depth):
        nxt={}
        for u,cwm in mass.items():
            for v,i,g in adj[u]:nxt[v]=r.merge(nxt.get(v,ZERO),r.serial(cwm,ONE))
        mass=nxt
    total=ZERO
    for w in mass.values():total=r.merge(total,w)
    return dict(mode='recurrent',states=len(nodes),edges=sum(map(len,adj)),analyses=analyses,
                depth=depth,classes=len(mass),prefix_CWM=e.cw(total),**G.stats())

def cycles(rounds=30,repeats=2):
    G=DualRing(6,6,repeats)
    table=((0,None,0),((0,0),)+(None,)*5)
    jobs=((('feedback',0),),(('reserve',0),),(('bind',0,0),),(('valid',0),),(),())
    node=G.initial_node(table);st=base.ref.old.seed(node.J)
    ann=[st,{G.C.targets[2]:st.names()[G.C.targets[2]]}]
    accepted=[];attempts=steps=0;logical=table
    for _ in range(rounds):
        for i in range(6):
            for j in range(6):
                if j==i:continue
                if node.pcs[j].phase in ('done','busy'):node=G.rearm(node,j)
                node,s,g=complete(G,node,j,jobs,ann=ann);steps+=s;attempts+=1
                ck(not g and node.pcs[j].phase=='busy','non-turn actors cannot barge')
            if node.pcs[i].phase in ('done','busy'):node=G.rearm(node,i)
            node,s,g=complete(G,node,i,jobs,ann=ann);steps+=s;attempts+=1
            ck(g==(i,),'next cooperative participant really acquires')
            accepted+=list(g)
            for op in jobs[i]:logical,value=base.expected(G.C,logical,('execute',op[1]) if op[0]=='feedback' else op)
            if jobs[i]:ck(G.C.decode(G.core(node.J))==(logical,value),'sequential business correspondence')
    return dict(mode='cycles',rounds=rounds,attempts=attempts,grants=len(accepted),steps=steps,
                prefix_order=accepted[:24],last_order=accepted[-12:],**G.stats())

def emit_programs():
    out=[]
    for slots,actors in ((1,2),(6,2),(6,6)):
        G=DualRing(slots,actors)
        out.append(dict(slots=slots,actors=actors,members=G.members,candidates=sorted(G.H),
            release_ports=G.release_ports,gates=G.gate_pair,
            entry=G.entry,publish=G.publish,handoff=G.handoffs,
            control='bank toggles only after completed successful handoff; WAIT leaves bank unchanged',
            initialization=[p.add(G.gate_pair[i][0]) for i in range(1,actors)]))
    return out

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['costs','suffix','finite','recurrent','cycles','programs'])
    ap.add_argument('--repeats',type=int,default=1);ap.add_argument('--actors',type=int,default=2)
    ap.add_argument('--omissions',type=int,default=0);ap.add_argument('--case',default='pass')
    ap.add_argument('--rounds',type=int,default=30);ap.add_argument('--out')
    args=ap.parse_args()
    if args.mode=='costs':result=costs()
    elif args.mode=='suffix':result=delayed_suffix()
    elif args.mode=='finite':result=finite_graph(args.repeats,args.omissions,args.case,args.actors)
    elif args.mode=='recurrent':result=recurrent(args.repeats,args.actors)
    elif args.mode=='cycles':result=cycles(args.rounds,args.repeats)
    else:result=emit_programs()
    text=json.dumps(result,ensure_ascii=False,indent=2)
    if args.out:Path(args.out).write_text(text+'\n')
    else:print(text)
