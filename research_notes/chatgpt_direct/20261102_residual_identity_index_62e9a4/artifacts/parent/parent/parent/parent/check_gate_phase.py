"""Recover handoff phase from the successor's existing dual gate.

No persistent per-participant phase field and no additional phase storage.
The controller samples only complete private output, then selects one of two
fixed handoff words using a fixed wrap-around convention. It forgets that
selection on return. Original kernel/CWM are inherited unchanged.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from collections import deque
from functools import lru_cache
from pathlib import Path
import argparse, json, sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_dual_handoff as parent
old,base,p,m,e,r=parent.old,parent.base,parent.p,parent.m,parent.e,parent.r
ONE,ZERO=parent.ONE,parent.ZERO
CHECKS=0

def ck(value:bool, description:str)->None:
    global CHECKS
    CHECKS+=1
    if not value: raise AssertionError(description)

@dataclass(frozen=True)
class PC:
    phase:str='entry'
    job:int=0
    target:int=0
    pos:int=0
    route:int|None=None  # Temporary instruction path, forgotten on return.

@dataclass(frozen=True)
class Node:
    J:tuple
    pcs:tuple[PC,...]
    turn:int=0  # Test-only monitor; never read by word selection.

class PhaseRing(parent.DualRing):
    """Observe the successor's existing closed gate; no additional phase carrier."""
    def __init__(self, slots=1, actors=2, repeats=1):
        super().__init__(slots,actors,repeats)
        self.dual_members,self.dual_candidates=self.members,len(self.H)
        H=set(self.H);reads=[]
        for i in range(actors):
            v=self.lanes[i];successor=(i+1)%actors
            hh,word,_=base.old.reader(self.release_ports[successor][1],v.reply,v.work)
            H.update(hh);reads.append(tuple(word))
        self.phase_reads=tuple(reads)
        self.phase_clears=tuple(tuple(p.clear_word(v.reply)) for v in self.lanes)
        self.H=frozenset(H)
        self.members=len(frozenset().union(*(frozenset(h) for h in self.H)))
        self._raw=lru_cache(maxsize=500000)(self._uncached)
        self.calls=self.uses=self.omissions=0

    def initial_node(self, table, turn=0, old_result=None, phase=0):
        if turn!=0 or phase not in (0,1):raise ValueError('initial owner=0 and phase in {0,1}')
        J=m.canon(self.C.encode(table,old_result)+tuple(self.gate_pair[i][phase] for i in range(1,self.actors)))
        return Node(J,tuple(PC() for _ in range(self.actors)),0)

    def begin(self,jobs,k,route):
        if k==len(jobs):return PC('publish',k,route=route) if jobs else PC('handoff',route=route)
        return PC('match' if jobs[k][0]=='feedback' else 'fixed',k,route=route)

    def word(self,i,pc,jobs):
        if pc.phase=='entry':return self.entry[i]
        if pc.phase=='phase_read':return self.phase_reads[i]
        if pc.phase=='phase_clear':return self.phase_clears[i]
        if pc.phase=='handoff':
            if pc.route is None:raise ValueError('complete successor-gate observation required')
            return self.handoffs[i][pc.route]
        if pc.phase=='publish':return self.publish[i]
        return old.Guard.word(self,i,pc,jobs)

    def invariant(self,node):
        owners=[i for i in range(self.actors) if self.lock(i) in node.J]
        opened=[i for i,pair in enumerate(self.gate_pair) if not any(h in node.J for h in pair)]
        ck(len(owners)<=1,'one actual holder')
        ck(len(opened)<=1,'at most one open gate')
        ck(all(i in opened for i in owners),'holders own the open gate')
        active=[]
        for i,pc in enumerate(node.pcs):
            ck(sum(h in node.J for h in self.gate_pair[i])<=1,'one physical bank per closed gate')
            if pc.phase in ('entry','phase_read','done','busy'):
                ck(pc.route is None,'no phase memory between calls or before complete observation')
            if pc.phase in ('phase_read','phase_clear','fixed','match','commit','publish'):
                ck(self.lock(i) in node.J,'sampling/business/result copy hold actual token')
                active.append(i)
                j=(i+1)%self.actors
                banks=[b for b,h in enumerate(self.gate_pair[j]) if h in node.J]
                ck(len(banks)==1,'successor gate is closed during protected observation')
                if pc.route is not None:
                    ck(pc.route==(banks[0]^int(i==self.actors-1)), 'local route recovered from successor bank')
        ck(len(active)<=1,'one protected operation')

    def next(self,node,i,jobs,omit=False,check=True):
        pc=node.pcs[i]
        if pc.phase in ('done','busy'):raise ValueError('previous attempt must finish before rearming')
        word=self.word(i,pc,jobs);raw=word[pc.pos//self.repeats];self.uses+=1
        if omit:self.omissions+=1;K=node.J;ok=None
        else:K,ok=self._raw(node.J,raw)
        new=replace(pc,pos=pc.pos+1);grant=False;turn=node.turn
        if new.pos==len(word)*self.repeats:
            if pc.phase=='entry':
                got=old.bit(K,self.lanes[i].admitted)
                if check:ck(got==(self.lock(i) in K),'entry evidence identifies actual holder')
                new=PC('phase_read') if got else PC('busy');grant=got
                if got:
                    if check:ck(i==turn,'cyclic-order observer')
                    turn=(i+1)%self.actors
            elif pc.phase=='phase_read':
                observed=int(old.bit(K,self.lanes[i].reply))
                # Fixed participant label only; no source/gate-table decoding.
                route=observed ^ int(i==self.actors-1)
                new=PC('phase_clear',route=route)
            elif pc.phase=='phase_clear':new=self.begin(jobs[i],0,pc.route)
            elif pc.phase in ('fixed','commit'):new=self.begin(jobs[i],pc.job+1,pc.route)
            elif pc.phase=='match':
                if self.C.observe_result(K):new=PC('commit',pc.job,pc.target,route=pc.route)
                elif pc.target+1<self.C.d:new=PC('match',pc.job,pc.target+1,route=pc.route)
                else:new=self.begin(jobs[i],pc.job+1,pc.route)
            elif pc.phase=='publish':new=PC('handoff',pc.job,route=pc.route)
            elif pc.phase=='handoff':new=PC('done',pc.job)
        pcs=list(node.pcs);pcs[i]=new;ans=Node(K,tuple(pcs),turn)
        if check:self.invariant(ans)
        return ans,raw,ok,grant

    def rearm(self,node,i):
        ck(node.pcs[i].phase in ('done','busy'),'all planned repetitions finish before reentry')
        pcs=list(node.pcs);pcs[i]=PC()
        return Node(node.J,tuple(pcs),node.turn)

    def terminal(self,node,jobs,table,grants,phase=0):
        ck(all(pc.phase in ('done','busy') for pc in node.pcs),'finite attempts completed')
        ck(grants==tuple(range(len(grants))),'grants are initial cyclic prefix')
        tab=table;last=None;answers={}
        for i in grants:
            value=None
            for op in jobs[i]:tab,value=base.expected(self.C,tab,('execute',op[1]) if op[0]=='feedback' else op)
            answers[i]=value
            if jobs[i]:last=value
        want=self.C.encode(tab,last)
        for i,v in enumerate(self.lanes):
            q=phase^int(i in grants)
            want=m.canon(want+p.reg(v.admitted,int(i in grants)))
            if i in grants and jobs[i]:want=m.canon(want+p.reg(v.reply,int(answers[i])))
            if i!=node.turn:want=m.canon(want+(self.gate_pair[i][q],))
            ck(node.pcs[i].route is None,'completed caller discards phase selection')
        ck(node.J==want,'exact parent endpoint including source/table/results/gates and clear work')
        return {str(i):('WAIT' if i not in grants else ('PASS' if not jobs[i] else answers[i])) for i in range(self.actors)}

    def stats(self):
        return dict(assertions=CHECKS,kernel_calls=self.calls,primitive_uses=self.uses,omission_edges=self.omissions,
          slots=self.C.slots,actors=self.actors,repeats=self.repeats,members=self.members,candidates=len(self.H),
          parent_members=self.dual_members,parent_candidates=self.dual_candidates,
          persistent_controller_phase_bits=0,additional_phase_carrier_members=0)

def complete(G,node,i,jobs,trace=None,ann=None,omits=frozenset(),check=True):
    steps=0;grants=[]
    while node.pcs[i].phase not in ('done','busy'):
        before=node;omission=steps in omits
        node,raw,ok,grant=G.next(node,i,jobs,omit=omission,check=check)
        if grant:grants.append(i)
        if ann is not None and not omission:
            ann[0],_,_=base.ref.old.raw_step(ann[0],raw,G.H)
            ck(ann[0].matching==node.J,'same original kernel in creation annotation')
            for h,identity in ann[1].items():ck(ann[0].names().get(h)==identity,'protected source birth in every prefix')
        if trace is not None:
            trace.append(dict(actor=i,phase=before.pcs[i].phase,pos=before.pcs[i].pos,route=before.pcs[i].route,
              raw=raw,omitted=omission,grant=grant,next_phase=node.pcs[i].phase,
              closed_gates=[[list(h) for h in pair if h in node.J] for pair in G.gate_pair]))
        steps+=1
    return node,steps,tuple(grants)

def costs():
    rows=[];G=PhaseRing(6,2)
    for phase in (0,1):
        for name,cur,ref in [('A',(0,None,0),(0,0)),('B',(None,0,None),(1,0)),
                             ('C',(0,None,0),(2,0)),('stale',(0,None,0),(1,0))]:
            table=(cur,(ref,)+(None,)*5);jobs=((('feedback',0),),())
            node=G.initial_node(table,phase=phase);st=base.ref.old.seed(node.J)
            valid=base.expected(G.C,table,('execute',0))[1];target=G.C.targets[ref[0]] if valid else None
            ann=[st,{h:n for h,n in st.events if h in G.C.targets and h!=target}]
            node,steps,grants=complete(G,node,0,jobs,ann=ann)
            ck(G.C.decode(G.core(node.J))==base.expected(G.C,table,('execute',0)),'business result retained')
            ck(G.gate_pair[0][1-phase] in node.J,'closed own gate carries the new phase')
            rows.append(dict(name=name,phase=phase,steps=steps,response=old.bit(node.J,G.lanes[0].reply)))
    ck([x['steps'] for x in rows]==[70,107,144,142]*2,'six-slot execution cost = parent plus eight')
    J=G.initial_node(table);_,pas,gr=complete(G,J,0,((),()))
    ck(pas==22,'PASS includes actual gate read and scratch clearing')
    # Wrong-turn attempts never sample/write phase and still cost eleven.
    _,wait,gr=complete(G,J,1,((),()))
    ck(wait==11 and not gr,'WAIT unchanged')
    return dict(mode='costs',paths=rows,pass_steps=pas,wait_steps=wait,**G.stats())

def finite_graph(repeats=1,budget=0,case='execute_restart',actors=2,initial_phase=0,limit=350000):
    G=PhaseRing(1,actors,repeats);table=((0,None,0),((0,0),))
    cases={'execute_restart':((('feedback',0),),(('release',1),('reserve',0))),
           'execute_execute':((('feedback',0),),(('feedback',0),)),
           'execute_bind':((('feedback',0),),(('bind',0,2),))}
    jobs=tuple(() for _ in range(actors)) if case=='pass' else cases[case]
    node=G.initial_node(table,phase=initial_phase)
    D={(node,(),0):e.prep(node.J)};states=edges=0;ends={}
    while D:
        states+=len(D)
        if states>limit:raise RuntimeError('finite graph budget reached')
        nxt={}
        for (node,grants,used),mass in D.items():
            if all(pc.phase in ('done','busy') for pc in node.pcs):
                G.terminal(node,jobs,table,grants,initial_phase)
                ends[(node,grants,used)]=r.merge(ends.get((node,grants,used),ZERO),mass)
                continue
            for i,pc in enumerate(node.pcs):
                if pc.phase in ('done','busy'):continue
                for skip in range(2 if used<budget else 1):
                    q,_,_,got=G.next(node,i,jobs,omit=bool(skip))
                    key=(q,grants+((i,) if got else ()),used+skip)
                    nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE));edges+=1
        D=nxt
    totals={}
    for (_,__,used),mass in ends.items():totals[used]=r.merge(totals.get(used,ZERO),mass)
    return dict(mode='finite',case=case,budget=budget,initial_phase=initial_phase,states=states,edges=edges,
      classes=len(ends),CWM_by_omissions={str(k):e.cw(v) for k,v in totals.items()},**G.stats())

def recurrent(repeats=1,budget=0,actors=2,limit=300000):
    import networkx as nx
    G=PhaseRing(1,actors,repeats);jobs=tuple(() for _ in range(actors))
    start=(G.initial_node(((None,)*3,(None,))),0)
    nodes=[start];index={start:0};queue=deque([0]);adj=[]
    while queue:
        u=queue.popleft();node,used=nodes[u];out=[]
        for i in range(actors):
            for skip in range(2 if used<budget else 1):
                q,raw,ok,got=G.next(node,i,jobs,omit=bool(skip))
                if q.pcs[i].phase in ('done','busy'):q=G.rearm(q,i)
                key=(q,used+skip)
                if key not in index:
                    index[key]=len(nodes);nodes.append(key);queue.append(index[key])
                    if len(nodes)>limit:raise RuntimeError('recurrent graph budget reached')
                out.append((index[key],i,got,skip))
        adj.append(out)
    fairness=[]
    for victim in range(actors):
        dg=nx.DiGraph();dg.add_nodes_from(range(len(nodes)))
        for u,outs in enumerate(adj):
            for v,i,got,skip in outs:
                if not(i==victim and got):dg.add_edge(u,v)
        cyclic=0;bad=[]
        for scc in nx.strongly_connected_components(dg):
            if len(scc)==1 and not dg.has_edge(next(iter(scc)),next(iter(scc))):continue
            cyclic+=1;seen=set()
            for u in scc:
                for v,i,got,skip in adj[u]:
                    if v in scc and not(i==victim and got):seen.add(i)
            if len(seen)==actors:bad.append(len(scc))
        ck(not bad,'no weakly fair cycle permanently denies participant')
        fairness.append(dict(victim=victim,cyclic_components=cyclic,bad_components=bad))
    depth=20;D={0:e.prep(start[0].J)}
    for _ in range(depth):
        nxt={}
        for u,mass in D.items():
            for v,i,got,skip in adj[u]:nxt[v]=r.merge(nxt.get(v,ZERO),r.serial(mass,ONE))
        D=nxt
    total={}
    for u,mass in D.items():
        used=nodes[u][1];total[used]=r.merge(total.get(used,ZERO),mass)
    return dict(mode='recurrent',budget=budget,states=len(nodes),edges=sum(map(len,adj)),fairness=fairness,
      depth=depth,CWM_by_omissions={str(k):e.cw(v) for k,v in total.items()},**G.stats())

def cycles(rounds=12,repeats=3):
    G=PhaseRing(6,6,repeats);table=((0,None,0),((0,0),)+(None,)*5)
    jobs=((('feedback',0),),(('reserve',0),),(('bind',0,0),),(('valid',0),),(),())
    node=G.initial_node(table);st=base.ref.old.seed(node.J)
    ann=[st,{G.C.targets[2]:st.names()[G.C.targets[2]]}]
    order=[];steps=attempts=0;logical=table
    for cycle in range(rounds):
        for i in range(6):
            for j in range(6):
                if j==i:continue
                if node.pcs[j].phase in ('done','busy'):node=G.rearm(node,j)
                node,s,gs=complete(G,node,j,jobs,ann=ann);steps+=s;attempts+=1
                ck(not gs,'out-of-turn attempt never consumes opportunity')
            if node.pcs[i].phase in ('done','busy'):node=G.rearm(node,i)
            ck(node.pcs[i].route is None,'new invocation has no stored controller phase')
            node,s,gs=complete(G,node,i,jobs,ann=ann);steps+=s;attempts+=1
            ck(gs==(i,),'ring order');order+=list(gs)
            ck(G.gate_pair[i][(cycle+1)%2] in node.J,'next phase encoded by the closed gate')
            for op in jobs[i]:logical,value=base.expected(G.C,logical,('execute',op[1]) if op[0]=='feedback' else op)
            if jobs[i]:ck(G.C.decode(G.core(node.J))==(logical,value),'business simulation')
    return dict(mode='cycles',rounds=rounds,attempts=attempts,grants=len(order),steps=steps,
      prefix_order=order[:24],last_order=order[-12:],**G.stats())

def suffix():
    G=PhaseRing(6,2,2);table=((0,None,0),((0,0),)+(None,)*5)
    jobs=((('feedback',0),),(('reserve',0),));node=G.initial_node(table);trace=[];order=[];steps=0
    st=base.ref.old.seed(node.J);ann=[st,{G.C.targets[2]:st.names()[G.C.targets[2]]}]
    while not(node.pcs[0].phase=='handoff' and node.pcs[0].pos==5):
        before=node;node,raw,ok,got=G.next(node,0,jobs);steps+=1
        if got:order.append(0)
        ann[0],_,_=base.ref.old.raw_step(ann[0],raw,G.H)
        ck(ann[0].matching==node.J,'same source trace')
        ck(ann[0].names().get(G.C.targets[2])==ann[1][G.C.targets[2]],'C unchanged')
        trace.append(dict(actor=0,phase=before.pcs[0].phase,pos=before.pcs[0].pos,raw=raw))
    node,s,gs=complete(G,node,1,jobs,trace,ann);steps+=s;order+=list(gs)
    ck(G.gate_pair[1][1] in node.J,'receiver closes other bank')
    stable=node.J
    node,raw,ok,got=G.next(node,0,jobs);steps+=1
    ann[0],_,_=base.ref.old.raw_step(ann[0],raw,G.H)
    ck(node.J==stable,'old second release is exactly inert')
    node,s,gs=complete(G,node,0,jobs,trace,ann);steps+=s;order+=list(gs)
    ck(node.pcs[0].route is None,'temporary selector erased on return')
    node=G.rearm(node,1);node,s,gs=complete(G,node,1,jobs,trace,ann);steps+=s;order+=list(gs)
    ck(not gs,'receiver cannot take next round early')
    node=G.rearm(node,0);node,s,gs=complete(G,node,0,jobs,trace,ann);steps+=s;order+=list(gs)
    ck(order==[0,1,0],'ring order under late retry')
    ck(not old.bit(node.J,G.lanes[0].reply),'old reference returns false after recreation')
    return dict(mode='suffix',steps=steps,order=order,trace=trace,**G.stats())

def emit_programs():
    rows=[]
    for slots,actors in ((1,2),(6,2),(6,6)):
        G=PhaseRing(slots,actors)
        rows.append(dict(slots=slots,actors=actors,members=G.members,candidates=sorted(G.H),phase_source='successor closed dual gate',
          entry=G.entry,phase_reads=G.phase_reads,phase_clear=G.phase_clears,handoff=G.handoffs,
          publish=G.publish,
          control='entry -> read successor port -> route=reply XOR wrap -> clear reply -> body -> publish -> selected handoff -> return with route=None',
          initial_gates=[p.add(G.gate_pair[i][0]) for i in range(1,actors)]))
    return rows

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['costs','finite','recurrent','cycles','suffix','programs'])
    ap.add_argument('--repeats',type=int,default=1);ap.add_argument('--budget',type=int,default=0)
    ap.add_argument('--actors',type=int,default=2);ap.add_argument('--case',default='execute_restart')
    ap.add_argument('--phase',type=int,default=0);ap.add_argument('--rounds',type=int,default=12);ap.add_argument('--out')
    a=ap.parse_args()
    if a.mode=='costs':result=costs()
    elif a.mode=='finite':result=finite_graph(a.repeats,a.budget,a.case,a.actors,a.phase)
    elif a.mode=='recurrent':result=recurrent(a.repeats,a.budget,a.actors)
    elif a.mode=='cycles':result=cycles(a.rounds,a.repeats)
    elif a.mode=='suffix':result=suffix()
    else:result=emit_programs()
    text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if a.out:Path(a.out).write_text(text)
    else:print(text)
