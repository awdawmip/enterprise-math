"""Focused domain, observer and failed-shortcut checks for physical gate phases."""
from __future__ import annotations
from dataclasses import replace
from pathlib import Path
import json
import check_gate_phase as x

def main():
    out={};G=x.PhaseRing(1,2)
    count=0
    for table in x.base.domain(G.C):
        for phase in (0,1):
            for schedule in ((0,1),(1,0)):
                node=G.initial_node(table,phase=phase)
                # Existing private complete outputs are overwritten by entry.
                J=node.J
                for i,v in enumerate(G.lanes):
                    J=x.m.canon(J+x.p.reg(v.admitted,(count+i)%2)+x.p.reg(v.reply,(count+i+1)%2))
                node=x.Node(J,node.pcs,node.turn)
                jobs=((('feedback',0),),(('feedback',0),));grants=()
                for i in schedule:
                    node,steps,gs=x.complete(G,node,i,jobs);grants+=gs
                G.terminal(node,jobs,table,grants,phase);count+=1
    x.ck(count==308,'77 preparations x 2 cycle phases x 2 attempt orders')
    out['endpoint_audit']=dict(cases=count,**G.stats())

    # Every possible ring position/phase has a physically readable successor.
    observations=[]
    for actors in range(2,7):
        T=x.PhaseRing(1,actors);empty=((None,)*3,(None,))
        for phase in (0,1):
            for i in range(actors):
                gates=tuple(T.gate_pair[j][phase^int(j<i)] for j in range(actors) if j!=i)
                J=x.m.canon(T.C.encode(empty)+gates+(T.lock(i),)+x.p.reg(T.lanes[i].admitted,1))
                initial=J
                J,_=T.runword(J,T.phase_reads[i]);b=int(x.old.bit(J,T.lanes[i].reply))
                route=b ^ int(i==actors-1)
                x.ck(route==phase,'actual local observation recovers correct current round phase')
                J,_=T.runword(J,T.phase_clears[i])
                x.ck(J==initial,'sampling and clearing exactly preserve all existing relations')
                observations.append(dict(actors=actors,actor=i,phase=phase,observed_successor_bank=b))
    x.ck(len(observations)==40,'all declared ring positions and phases')
    out['local_observers']=observations

    # Incorrect wrap convention: choose raw b, omitting the last actor correction.
    T=x.PhaseRing(1,2);jobs=((),());node=T.initial_node(empty);trace=[];grants=[]
    node,_,gs=x.complete(T,node,0,jobs,trace);grants+=list(gs)
    while node.pcs[1].phase!='phase_clear':
        before=node;node,raw,ok,got=T.next(node,1,jobs)
        if got:grants.append(1)
        trace.append(dict(actor=1,phase=before.pcs[1].phase,raw=raw))
    observed=int(x.old.bit(node.J,T.lanes[1].reply));pcs=list(node.pcs)
    pcs[1]=replace(pcs[1],route=observed) # Deliberate faulty controller alternative.
    node=x.Node(node.J,tuple(pcs),node.turn)
    node,_,gs=x.complete(T,node,1,jobs,trace,check=False)
    x.ck(all(any(h in node.J for h in pair) for pair in T.gate_pair),'missing wrap closes both gates')
    node=T.rearm(node,0);node,_,gs=x.complete(T,node,0,jobs,trace,check=False)
    x.ck(not gs,'wrong wrap prevents expected successor grant')
    out['missing_wrap']=dict(grants=grants,actor0_after='WAIT',trace=trace)

    # Keep the gate-phase sample in the result scratch: it contaminates delivery.
    T=x.PhaseRing(6,2);tab=((0,None,0),((0,0),)+(None,)*5)
    jobs=((('feedback',0),),());node=T.initial_node(tab);trace=[]
    while node.pcs[0].phase not in ('done','busy'):
        before=node;skip=before.pcs[0].phase=='phase_clear'
        node,raw,ok,got=T.next(node,0,jobs,omit=skip)
        trace.append(dict(actor=0,phase=before.pcs[0].phase,raw=raw,omitted=skip))
    x.ck(T.C.observe_result(node.J) is True,'shared business result true')
    x.ck(x.old.bit(node.J,T.lanes[0].reply) is False,'uncleared phase zero masks copied true result')
    out['missing_scratch_clear']=dict(shared=True,delivered=False,trace=trace)

    # A single omitted phase probe can select the wrong handoff without protection.
    T=x.PhaseRing(1,2);jobs=((),());node=T.initial_node(empty);trace=[]
    while node.pcs[0].phase not in ('done','busy'):
        pc=node.pcs[0];skip=pc.phase=='phase_read' and pc.pos==0
        node,raw,ok,got=T.next(node,0,jobs,omit=skip,check=False)
        trace.append(dict(phase=pc.phase,pos=pc.pos,raw=raw,omitted=skip))
    x.ck(all(any(h in node.J for h in pair) for pair in T.gate_pair),'unprotected phase-read omission loses turn')
    out['unprotected_probe_omission']=dict(closed_all=True,trace=trace)

    # Same omission, now protected, including physical observation and branch selection.
    T=x.PhaseRing(1,2,2);node=T.initial_node(empty);trace=[];grants=()
    while node.pcs[0].phase not in ('done','busy'):
        pc=node.pcs[0];skip=pc.phase=='phase_read' and pc.pos==0
        node,raw,ok,got=T.next(node,0,jobs,omit=skip)
        if got:grants+=(0,)
        trace.append(dict(phase=pc.phase,pos=pc.pos,raw=raw,omitted=skip))
    node,_,gs=x.complete(T,node,1,jobs);grants+=gs
    T.terminal(node,jobs,empty,grants)
    x.ck(grants==(0,1),'protected actual observation preserves order')
    out['protected_probe_omission']=dict(grants=grants,trace=trace)
    out['assertions']=x.CHECKS
    Path(__file__).with_name('gate_audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print('audit',x.CHECKS,'endpoint_cases',count,'observer_preparations',len(observations))

if __name__=='__main__':main()
