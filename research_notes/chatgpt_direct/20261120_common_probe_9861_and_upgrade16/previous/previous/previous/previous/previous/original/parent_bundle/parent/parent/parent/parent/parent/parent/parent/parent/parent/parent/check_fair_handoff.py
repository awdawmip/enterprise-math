"""Round-robin turn gates around the inherited cooperative triadic guard.

Production feedback reads only complete six-member result registers. Turn is
represented by real gate occupancy; no decoded owner index selects a winner.
Tests use the unchanged inherited BRC transition and positive CWM composition.
Contract: atomic exact primitives, closed cooperative accesses, non-reentrant
lanes, initialized gates, finite bodies; every lane services idle passes for
liveness. Weak fairness concerns scheduling, not an assumed fair try-lock.
"""
from __future__ import annotations
from dataclasses import replace
from collections import deque
from functools import lru_cache
from pathlib import Path
import argparse,json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_guard as parent
PC,Node=parent.PC,parent.Node
base,p,m,e,r=parent.base,parent.p,parent.m,parent.e,parent.r
ONE,ZERO=parent.ONE,parent.ZERO
CHECKS=0

def ck(test,description):
    global CHECKS
    CHECKS+=1
    if not test: raise AssertionError(description)

class FairGuard(parent.Guard):
    def __init__(self,slots=1,actors=2):
        if actors<2: raise ValueError('This ring contract requires at least two lanes')
        super().__init__(slots,actors)
        self.parent_members=self.members
        self.parent_candidates=len(self.H)
        start=max(frozenset().union(*(frozenset(h) for h in self.H)))+1
        self.gate_ports=tuple((start+2*i,start+2*i+1) for i in range(actors))
        self.gates=tuple(tuple(sorted((self.lanes[i].a,*self.gate_ports[i]))) for i in range(actors))
        self.H=frozenset(set(self.H)|set(self.gates))
        self.handoff=tuple((p.one(self.lanes[i].a),p.add(self.gates[i]),
                            p.one(self.gate_ports[(i+1)%actors][0])) for i in range(actors))
        # Copy the completed business answer while the inherited lock is held.
        self.publish=tuple(word[:-1] for word in self.exit)
        self.members=len(frozenset().union(*(frozenset(h) for h in self.H)))
    def initial(self,table,turn=0,old_result=None):
        return m.canon(self.C.encode(table,old_result)+tuple(h for i,h in enumerate(self.gates) if i!=turn))
    def start_pc(self,jobs,k):
        if k==len(jobs): return PC('publish',k) if jobs else PC('handoff')
        return PC('match' if jobs[k][0]=='feedback' else 'fixed',k)
    def word(self,i,pc,jobs):
        if pc.phase=='handoff':return self.handoff[i]
        if pc.phase=='publish':return self.publish[i]
        return super().word(i,pc,jobs)
    def invariant(self,node):
        owners=[i for i in range(self.actors) if self.lock(i) in node.J]
        open_gates=[i for i,h in enumerate(self.gates) if h not in node.J]
        ck(len(owners)<=1,'Inherited shared g maintains mutual exclusion')
        ck(len(open_gates)<=1,'At most one turn gate is open')
        ck(all(i in open_gates for i in owners),'An owner always holds the open-gate turn')
        shared=[]
        for i,pc in enumerate(node.pcs):
            if pc.phase in ('fixed','match','commit','publish'):
                shared.append(i)
                ck(self.lock(i) in node.J,'Shared use and result copy retain own token')
            if pc.phase=='handoff':
                ck((self.lock(i) in node.J)==(pc.pos==0),'Token retirement occurs at handoff first step')
                ck((self.gates[i] in node.J)==(pc.pos>=2),'Own gate closes before successor opens')
        ck(len(shared)<=1,'At most one shared body/copy runs')
        if not open_gates:
            ck(any(pc.phase=='handoff' and pc.pos==2 for pc in node.pcs),
               'All gates closed only during an identified pending handoff')
    def next(self,node,i,jobs,check=True):
        pc=node.pcs[i];word=self.word(i,pc,jobs);raw=word[pc.pos]
        self.uses+=1;K,ok=self._raw(node.J,raw)
        new=replace(pc,pos=pc.pos+1);order=node.order
        if new.pos==len(word):
            if pc.phase=='entry':
                acquired=parent.bit(K,self.lanes[i].admitted)
                if check:ck(acquired==(self.lock(i) in K),'Entry evidence equals own stable token')
                new=self.start_pc(jobs[i],0) if acquired else PC('busy')
                if acquired:order=order+(i,)
            elif pc.phase in ('fixed','commit'):
                new=self.start_pc(jobs[i],pc.job+1)
            elif pc.phase=='match':
                if self.C.observe_result(K):new=PC('commit',pc.job,pc.target)
                elif pc.target+1<self.C.d:new=PC('match',pc.job,pc.target+1)
                else:new=self.start_pc(jobs[i],pc.job+1)
            elif pc.phase=='publish':new=PC('handoff',pc.job)
            elif pc.phase=='handoff':new=PC('done',pc.job)
        pcs=list(node.pcs);pcs[i]=new;ans=Node(K,tuple(pcs),order)
        if check:self.invariant(ans)
        return ans,raw,ok
    def terminal(self,node,jobs,initial_table,turn=0,initial_result=None):
        ck(self.done(node),'Only complete finite attempts are terminal')
        ck(node.order==tuple((turn+k)%self.actors for k in range(len(node.order))),
           'Accepted attempts are a cyclic prefix, never a race-dependent permutation')
        tab=initial_table;last=initial_result;answers={}
        for i in node.order:
            value=None
            for op in jobs[i]:
                tab,value=base.expected(self.C,tab,('execute',op[1]) if op[0]=='feedback' else op)
            answers[i]='PASS' if not jobs[i] else value
            if jobs[i]:last=value
        want=self.initial(tab,(turn+len(node.order))%self.actors,last)
        for i,v in enumerate(self.lanes):
            accepted=i in node.order
            want=m.canon(want+p.reg(v.admitted,int(accepted)))
            if accepted and jobs[i]:want=m.canon(want+p.reg(v.reply,int(answers[i])))
        ck(node.J==want,'Exact source/table/private outputs/gates, all temporary state cleared')
        return tuple((i,answers.get(i,'WAIT_TURN')) for i in range(self.actors))
    def stats(self):
        return dict(assertions=CHECKS,kernel_calls=self.calls,primitive_uses=self.uses,
                    actors=self.actors,slots=self.C.slots,members=self.members,
                    candidates=len(self.H),parent_guard_members=self.parent_members,
                    parent_guard_candidates=self.parent_candidates,
                    entry_length=len(self.entry[0]),publish_length=len(self.publish[0]),
                    handoff_length=len(self.handoff[0]))


def finite_explore(G,table,jobs,turn=0,limit=500000):
    init=Node(G.initial(table,turn),tuple(PC() for _ in jobs))
    D={init:e.prep(init.J)};ends={};states=edges=0;layers=[]
    while D:
        states+=len(D)
        if states>limit:raise RuntimeError('Finite-state exploration budget reached')
        nxt={}
        for node,mass in D.items():
            if G.done(node):
                ans=G.terminal(node,jobs,table,turn)
                key=(node,ans);ends[key]=r.merge(ends.get(key,ZERO),mass);continue
            for i,pc in enumerate(node.pcs):
                if pc.phase in ('busy','done'):continue
                v,_,_=G.next(node,i,jobs);edges+=1
                nxt[v]=r.merge(nxt.get(v,ZERO),r.serial(mass,ONE))
        layers.append(len(D));D=nxt
    total=ZERO;out=[]
    for (node,ans),mass in ends.items():
        total=r.merge(total,mass);out.append(dict(order=node.order,answers=ans,CWM=e.cw(mass)))
    return dict(states=states,edges=edges,layers=layers,classes=len(ends),CWM=e.cw(total),outcomes=out)


def complete_actor(G,node,i,jobs,trace=None,annotated=None):
    steps=0
    while node.pcs[i].phase not in ('busy','done'):
        old=node;node,raw,ok=G.next(node,i,jobs);steps+=1
        if annotated is not None:
            annotated[0],_,delta=base.ref.old.raw_step(annotated[0],raw,G.H)
            ck(annotated[0].matching==node.J,'Creation annotations use identical raw transitions')
            names=annotated[0].names()
            for h,name in annotated[1].items():ck(names.get(h)==name,'Protected source creation persists in every prefix')
        if trace is not None:trace.append(dict(actor=i,phase=old.pcs[i].phase,pos=old.pcs[i].pos,
                                               raw=raw,next=node.pcs[i].phase,order=node.order))
    return node,steps


def fresh_attempt(node,i):
    ck(node.pcs[i].phase in ('done','busy'),'Rearm only after finite attempt returns')
    pcs=list(node.pcs);pcs[i]=PC()
    return Node(node.J,tuple(pcs),node.order)


def examples():
    G=FairGuard(6,3);table=((0,None,0),((0,0),)+(None,)*5)
    jobs=((('feedback',0),),(('reserve',0),),())
    node=Node(G.initial(table),tuple(PC() for _ in jobs));trace=[]
    names=base.ref.old.seed(node.J);C=G.C.targets[2]
    annotated=[names,{C:names.names()[C]}]
    # First actor completes. Aggressive reacquisition must now fail until 1 and 2 pass.
    node,l0=complete_actor(G,node,0,jobs,trace,annotated)
    for _ in range(8):
        node=fresh_attempt(node,0);node,ln=complete_actor(G,node,0,jobs,trace,annotated)
        ck(node.pcs[0].phase=='busy' and ln==11,'Fast predecessor cannot immediately retake turn')
    node,l1=complete_actor(G,node,1,jobs,trace,annotated)
    node,l2=complete_actor(G,node,2,jobs,trace,annotated)
    node=fresh_attempt(node,0);node,l3=complete_actor(G,node,0,jobs,trace,annotated)
    ck(node.order==(0,1,2,0),'Actual order includes idle pass and prevents barging')
    ck(parent.bit(node.J,G.lanes[0].reply)==False,'Old request rejected after protected recreation')
    ck(parent.bit(node.J,G.lanes[2].admitted) and not p.restrict(node.J,G.lanes[2].reply),
       'Idle pass leaves no fabricated business response')
    return dict(mode='examples',order=node.order,lengths=[l0,l1,l2,l3],trace=trace,**G.stats())


def costs():
    G=FairGuard(6,2);rows=[]
    for name,cur,ref in [('valid_A',(0,None,0),(0,0)),('valid_B',(None,0,None),(1,0)),
                         ('valid_C',(0,None,0),(2,0)),('stale_B',(0,None,0),(1,0)),
                         ('empty',(0,None,0),None)]:
        table=(cur,(ref,)+(None,)*5);jobs=((('feedback',0),),())
        node=Node(G.initial(table),tuple(PC() for _ in jobs))
        st=base.ref.old.seed(node.J);valid=base.expected(G.C,table,('execute',0))[1]
        deleted=G.C.targets[ref[0]] if valid else None
        protected={h:n for h,n in st.events if h in G.C.targets and h!=deleted}
        node,num=complete_actor(G,node,0,jobs,annotated=[st,protected])
        target=base.expected(G.C,table,('execute',0))
        ck(G.C.decode(G.core(node.J))==target,'Cost example exact business source/table/result')
        rows.append(dict(name=name,commands=num,value=parent.bit(node.J,G.lanes[0].reply)))
    ck([v['commands'] for v in rows]==[62,99,136,134,134],'Business wrapper adds exactly 23 commands')
    tab=((None,)*3,(None,)*6);node=Node(G.initial(tab),tuple(PC() for _ in range(2)))
    jobs=((),());node,ps=complete_actor(G,node,0,jobs)
    ck(ps==14,'Idle pass 11 acquisition + 3 handoff')
    return dict(mode='costs',paths=rows,idle_pass=ps,**G.stats())


def recurrent_graph(actors):
    """Enumerate real primitive states with endless idle service, then check fair lassos."""
    import networkx as nx
    G=FairGuard(1,actors);jobs=tuple(() for _ in range(actors))
    table=((None,)*3,(None,));start=Node(G.initial(table),tuple(PC() for _ in range(actors)))
    nodes=[start];index={start:0};adj=[];queue=deque([0]);edges=0
    while queue:
        k=queue.popleft();node=nodes[k];out=[]
        for i in range(actors):
            nxt,raw,ok=G.next(node,i,jobs)
            grant=nxt.order==(i,)
            pcs=list(nxt.pcs)
            if pcs[i].phase in ('done','busy'):pcs[i]=PC()
            nxt=Node(nxt.J,tuple(pcs))
            if nxt not in index:
                index[nxt]=len(nodes);nodes.append(nxt);queue.append(len(nodes)-1)
                if len(nodes)>250000:raise RuntimeError('Declared graph bound exceeded')
            out.append((index[nxt],i,grant));edges+=1
        adj.append(out)
    analyses=[]
    for victim in range(actors):
        D=nx.DiGraph();D.add_nodes_from(range(len(nodes)))
        for u,out in enumerate(adj):
            for v,i,grant in out:
                if not(grant and i==victim):D.add_edge(u,v)
        bad=[];cyclic=0;actor_sets={}
        for comp in nx.strongly_connected_components(D):
            if len(comp)==1:
                u=next(iter(comp))
                if not D.has_edge(u,u):continue
            cyclic+=1;seen=set()
            for u in comp:
                for v,i,grant in adj[u]:
                    if v in comp and not(grant and i==victim):seen.add(i)
            sig=','.join(map(str,sorted(seen)));actor_sets[sig]=actor_sets.get(sig,0)+1
            if len(seen)==actors:bad.append(len(comp))
        ck(not bad,'No strongly connected starvation region supports a weakly fair schedule')
        analyses.append(dict(victim=victim,cyclic_components=cyclic,actor_supports=actor_sets,
                             weakly_fair_starvation_components=bad))
    # Finite original positive-CWM traversal on exactly the graph edges, not probabilities.
    D={0:ONE};mass_layers=[]
    depth=30 if actors==2 else 24
    for level in range(depth):
        nxt={}
        for u,mass in D.items():
            for v,i,grant in adj[u]:nxt[v]=r.merge(nxt.get(v,ZERO),r.serial(mass,ONE))
        D=nxt
        if level in (depth-1,10):
            total=ZERO
            for mass in D.values():total=r.merge(total,mass)
            ck(total.count==actors**(level+1),'CWM keeps every finite scheduler word')
            mass_layers.append(dict(depth=level+1,states=len(D),CWM=e.cw(total)))
    return dict(mode='recurrent',states=len(nodes),edges=edges,analyses=analyses,
                finite_prefix_cwm=mass_layers,**G.stats())


def interleavings(case,turn=0):
    G=FairGuard(1,2);table=((0,None,0),((0,0),))
    cases={
      'execute_restart':((('feedback',0),),(('release',1),('reserve',0))),
      'execute_execute':((('feedback',0),),(('feedback',0),)),
      'execute_bind':((('feedback',0),),(('bind',0,2),)),
      'release_create':((('release',1),),(('reserve',1),)),
      'pass_execute':((),(('feedback',0),)),
    }
    return dict(mode='interleavings',case=case,initial_turn=turn,
                result=finite_explore(G,table,cases[case],turn),**G.stats())


def failures():
    G=FairGuard(1,2);table=((0,None,0),((0,0),));jobs=((),())
    node=Node(G.initial(table),tuple(PC() for _ in jobs));node,_=complete_actor(G,node,0,jobs)
    # Lane 1 owns the turn but stops: repeated lane-0 attempts do not advance it.
    for _ in range(12):
        node=fresh_attempt(node,0);node,k=complete_actor(G,node,0,jobs)
        ck(node.pcs[0].phase=='busy' and k==11,'Stopped idle successor blocks progress without breaking mutex')
    stopped=dict(order=node.order,attempts=12)
    # Two planned adjacent opens can straddle a complete successor visit.
    node=Node(G.initial(table),tuple(PC() for _ in jobs));trace=[]
    original=G.handoff
    G.handoff=(original[0]+(original[0][-1],),)+original[1:]
    while not (node.pcs[0].phase=='handoff' and node.pcs[0].pos==3):
        before=node;node,raw,_=G.next(node,0,jobs,check=False)
        trace.append(dict(actor=0,phase=before.pcs[0].phase,raw=raw))
    ck(node.pcs[0].phase=='handoff','Old opening still has one scheduled retry pending')
    while node.pcs[1].phase not in ('busy','done'):
        before=node;node,raw,_=G.next(node,1,jobs,check=False)
        trace.append(dict(actor=1,phase=before.pcs[1].phase,raw=raw))
    ck(G.gates[1] in node.J and G.gates[0] not in node.J,'Successor finished and reclosed its gate')
    node,late,_=G.next(node,0,jobs,check=False)
    trace.append(dict(actor=0,phase='handoff_retry',raw=late))
    ck(all(h not in node.J for h in G.gates),'Late old open deletes reclosed next-generation gate')
    G.handoff=original;node=fresh_attempt(node,1);words=[]
    while node.pcs[1].phase not in ('busy','done'):
        node,raw,_=G.next(node,1,jobs,check=False);words.append(raw)
    ck(node.order==(0,1,1),'A delayed adjacent retry breaks cyclic order without omissions')
    ck(sum(G.lock(i) in node.J for i in range(2))<=1,'Original mutex stays separate from cyclic order')
    retry=dict(late_release=late,order=node.order,extra_words=words,prior_trace=trace)
    # Opening successor before closing self permits a stale close to erase its returned turn.
    J=G.initial(table);J,_=G.runword(J,G.entry[0])
    J,_=G.runword(J,(original[0][0],original[0][2]))
    J,_=G.runword(J,G.entry[1]);ck(parent.bit(J,G.lanes[1].admitted),'Successor entered early-open variant')
    J,_=G.runword(J,original[1]);J,_=G.runword(J,(original[0][1],))
    ck(all(h in J for h in G.gates),'Closing self after opening successor can lose the returned turn')
    # Omitted turn closing step: opening successor leaves two eligible lanes.
    J=G.initial(table);J,_=G.runword(J,G.entry[0]);
    bad=(G.handoff[0][0],G.handoff[0][2]);J,_=G.runword(J,bad)
    ck(all(h not in J for h in G.gates),'Omitting own-gate closure destroys unique eligibility')
    # Omitted last handoff: all gates remain closed.
    J=G.initial(table);J,_=G.runword(J,G.entry[0]);J,_=G.runword(J,G.handoff[0][:2])
    ck(all(h in J for h in G.gates),'Omitted successor opening deadlocks admission')
    for i in range(2):
        J,_=G.runword(J,G.entry[i]);ck(not parent.bit(J,G.lanes[i].admitted),'All closed gates reject entry')
    # Safe source count/readout does not specify future turn: two equal business projections.
    J0,J1=G.initial(table,0),G.initial(table,1)
    ck(G.core(J0)==G.core(J1),'Business state is identical under different turn relations')
    K0,_=G.runword(J0,G.entry[0]);K1,_=G.runword(J1,G.entry[0])
    ck(parent.bit(K0,G.lanes[0].admitted) and not parent.bit(K1,G.lanes[0].admitted),
       'Same business readout has different future admission behavior')
    return dict(mode='failures',stopped_successor=stopped,late_retry=retry,
                gate_omissions=['missing_close_two_open','missing_open_all_closed'],
                same_business_different_turn=True,open_before_close_all_closed=True,**G.stats())


def cycles(rounds=30,actors=6):
    G=FairGuard(6,actors);table=((0,None,0),((0,0),)+(None,)*5)
    node=Node(G.initial(table),tuple(PC() for _ in range(actors)))
    cur=table;st=base.ref.old.seed(node.J);C=G.C.targets[2]
    annotated=[st,{C:st.names()[C]}];hist=[];attempts=steps=0
    for roundno in range(rounds):
        for owner in range(actors):
            # Each queued operation is fixed before its successful turn. Idle lanes relay.
            if owner==0:work=(('feedback',0),)
            elif owner==1:work=(('reserve',0),('bind',0,0))
            elif owner==2:work=(('valid',0),)
            elif owner==3:work=(('same',0,0),)
            else:work=()
            jobs=[() for _ in range(actors)];jobs[owner]=work;jobs=tuple(jobs)
            # Give every other lane a completed attempt first: speed cannot steal this turn.
            for j in range(actors):
                if j==owner:continue
                if node.pcs[j].phase in ('done','busy'):node=fresh_attempt(node,j)
                node,num=complete_actor(G,node,j,jobs,annotated=annotated)
                attempts+=1;steps+=num
                ck(node.pcs[j].phase=='busy','All out-of-turn attempts remain waiting')
            if node.pcs[owner].phase in ('done','busy'):node=fresh_attempt(node,owner)
            before=len(node.order);node,num=complete_actor(G,node,owner,jobs,annotated=annotated)
            attempts+=1;steps+=num
            ck(node.pcs[owner].phase=='done' and len(node.order)==before+1,'Designated turn progresses')
            answer=None
            for op in work:cur,answer=base.expected(G.C,cur,('execute',op[1]) if op[0]=='feedback' else op)
            actual=G.C.decode(G.core(node.J))
            ck(actual[0]==cur,'Cyclic service composes with exact logical reference model')
            if work:ck(parent.bit(node.J,G.lanes[owner].reply)==answer,'Private reply belongs to this completed operation')
            hist.append(dict(round=roundno,owner=owner,commands=num,job=work,reply=answer))
    ck(node.order==tuple(k%actors for k in range(rounds*actors)),'Entire admission trace is exactly cyclic')
    return dict(mode='cycles',rounds=rounds,admitted=rounds*actors,attempts=attempts,
                actual_commands=steps,history=hist,protected_source=list(C),**G.stats())


def audit():
    G=FairGuard(1,2);dom=base.domain(G.C);count=0;total=ZERO
    for table in dom:
        for actor in range(2):
            jobs=((('feedback',0),),(('feedback',0),))
            # Both turn values and old private-result patterns are genuine source preparations.
            for turn in range(2):
                J=G.initial(table,turn)
                for i,l in enumerate(G.lanes):J=m.canon(J+p.reg(l.admitted,(i+actor)%2)+p.reg(l.reply,(i+turn)%2))
                node=Node(J,tuple(PC() for _ in range(2)))
                node,num=complete_actor(G,node,actor,jobs)
                accepted=actor==turn
                ck(parent.bit(node.J,G.lanes[actor].admitted)==accepted,'Old admission record overwritten correctly')
                if accepted:
                    expected=base.expected(G.C,table,('execute',0))
                    ck(G.C.decode(G.core(node.J))==expected,'All finite source inputs preserve business specification')
                    ck(parent.bit(node.J,G.lanes[actor].reply)==expected[1],'Fresh private response is exact')
                else:
                    ck(G.core(node.J)==G.C.encode(table),'Out-of-turn attempt has no business effect')
                    ck(not p.restrict(node.J,G.lanes[actor].reply),'Waiting discards previous reply rather than faking zero')
                count+=1;total=r.merge(total,ONE)
    return dict(mode='audit',source_preparations=len(dom),cases=count,CWM=e.cw(total),**G.stats())


def programs():
    allrows=[]
    for slots,actors in [(1,2),(6,2),(6,3),(6,6)]:
        G=FairGuard(slots,actors)
        allrows.append(dict(slots=slots,actors=actors,members=G.members,candidates=sorted(G.H),
                            gates=G.gates,locks=[G.lock(i) for i in range(actors)],
                            entry=G.entry,publish=G.publish,handoff=G.handoff,
                            controller='Actual full entry bit; fixed/feedback parent body; copy; release-own, close-own, open-successor'))
    return dict(layouts=allrows)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode');ap.add_argument('--case',default='execute_restart')
    ap.add_argument('--actors',type=int,default=2);ap.add_argument('--turn',type=int,default=0)
    ap.add_argument('--rounds',type=int,default=30);ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if a.mode=='examples':ans=examples()
    elif a.mode=='costs':ans=costs()
    elif a.mode=='recurrent':ans=recurrent_graph(a.actors)
    elif a.mode=='interleavings':ans=interleavings(a.case,a.turn)
    elif a.mode=='cycles':ans=cycles(a.rounds,a.actors)
    elif a.mode=='failures':ans=failures()
    elif a.mode=='audit':ans=audit()
    elif a.mode=='programs':ans=programs()
    else:raise ValueError(a.mode)
    Path(a.out).write_text(json.dumps(ans,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in ans.items() if k not in ('trace','history','layouts','late_retry','result')},ensure_ascii=False))
