"""Focused multi-round omission graphs and failure boundaries for the two-port ring."""
from __future__ import annotations
from collections import deque
from dataclasses import replace
from pathlib import Path
import argparse,json
import check_dual_handoff as x
GClass=x.DualRing

def recurrent_faults(repeats=3,budget=2,actors=2):
    import networkx as nx
    G=GClass(1,actors,repeats);jobs=tuple(() for _ in range(actors))
    node=G.initial_node(((None,)*3,(None,)))
    start=(node,0);nodes=[start];idx={start:0};queue=deque([0]);adj=[]
    while queue:
        key=queue.popleft();node,used=nodes[key];out=[]
        for i in range(actors):
            for omission in range(2 if used<budget else 1):
                nxt,raw,ok,grant=G.next(node,i,jobs,omit=bool(omission))
                if nxt.pcs[i].phase in ('done','busy'):nxt=G.rearm(nxt,i)
                pair=(nxt,used+omission)
                if pair not in idx:
                    idx[pair]=len(nodes);nodes.append(pair);queue.append(idx[pair])
                    if len(nodes)>250000:raise RuntimeError('state bound reached')
                out.append((idx[pair],i,grant,omission))
        adj.append(out)
    checks=[]
    for victim in range(actors):
        graph=nx.DiGraph();graph.add_nodes_from(range(len(nodes)))
        for u,out in enumerate(adj):
            for v,i,grant,omit in out:
                if not(i==victim and grant):graph.add_edge(u,v)
        bad=[];cyclic=0
        for comp in nx.strongly_connected_components(graph):
            if len(comp)==1 and not graph.has_edge(next(iter(comp)),next(iter(comp))):continue
            cyclic+=1;seen=set()
            for u in comp:
                for v,i,grant,omit in adj[u]:
                    if v in comp and not(i==victim and grant):seen.add(i)
            if len(seen)==actors:bad.append(len(comp))
        x.ck(not bad,'no fair starvation component even after any budgeted omission prefix')
        checks.append(dict(victim=victim,cyclic_components=cyclic,bad=bad))
    # Preserve schedule/omission provenance with the inherited exact positive CWM.
    depth=22;mass={0:x.e.prep(start[0].J)}
    for _ in range(depth):
        nxt={}
        for u,w in mass.items():
            for v,i,grant,omit in adj[u]:
                nxt[v]=x.r.merge(nxt.get(v,x.ZERO),x.r.serial(w,x.ONE))
        mass=nxt
    totals={}
    for u,w in mass.items():
        used=nodes[u][1];totals[used]=x.r.merge(totals.get(used,x.ZERO),w)
    counts={str(i):sum(used==i for _,used in nodes) for i in range(budget+1)}
    return dict(mode='fault_graph',budget=budget,states=len(nodes),edges=sum(map(len,adj)),
                states_by_omissions=counts,analyses=checks,depth=depth,
                CWM_by_omissions={str(k):x.e.cw(v) for k,v in totals.items()},**G.stats())

def failures():
    # Reproduce the parent one-port bug with its original operations and pending call.
    P=x.parent.FairGuard(1,2);table=((0,None,0),((0,0),));jobs=((),())
    N=x.parent.Node(P.initial(table),tuple(x.parent.PC() for _ in jobs))
    original=P.handoff;P.handoff=(original[0]+(original[0][-1],),original[1])
    oldtrace=[]
    while not(N.pcs[0].phase=='handoff' and N.pcs[0].pos==3):
        N,raw,_=P.next(N,0,jobs,check=False);oldtrace.append(dict(actor=0,raw=raw))
    while N.pcs[1].phase not in ('done','busy'):
        N,raw,_=P.next(N,1,jobs,check=False);oldtrace.append(dict(actor=1,raw=raw))
    N,raw,_=P.next(N,0,jobs,check=False);oldtrace.append(dict(actor=0,late=True,raw=raw))
    P.handoff=original;N=x.parent.fresh_attempt(N,1)
    while N.pcs[1].phase not in ('done','busy'):
        N,raw,_=P.next(N,1,jobs,check=False);oldtrace.append(dict(actor=1,raw=raw))
    x.ck(N.order==(0,1,1),'one release port allows actual pending suffix to reopen the next visit')
    # Two banks are safe for still-pending non-reentrant calls, not detached forever-delayed packets.
    G=GClass(1,2);node=G.initial_node(table);order=[];trace=[]
    for i in (0,1,0,1):
        if node.pcs[i].phase in ('done','busy'):node=G.rearm(node,i)
        node,steps,grants=x.complete(G,node,i,jobs,trace);order+=list(grants)
    x.ck(G.gate_pair[1][0] in node.J,'old address is reused only after two legitimate receiver visits')
    raw=x.p.one(G.release_ports[1][0]);K,_=G._raw(node.J,raw);node=x.Node(K,node.pcs,node.turn)
    node=G.rearm(node,1)
    while node.pcs[1].phase not in ('done','busy'):
        node,_,_,got=G.next(node,1,jobs,check=False)
        if got:order.append(1)
    x.ck(order==[0,1,0,1,1],'detached replay after return defeats finite bank reuse')
    # Each group needs a real execution; exceeding the omission budget can lose all eligibility.
    G2=GClass(1,2,2);N2=G2.initial_node(table)
    while not(N2.pcs[0].phase=='handoff' and N2.pcs[0].pos==4):N2,_,_,_=G2.next(N2,0,jobs)
    N2,_,_,_=G2.next(N2,0,jobs,omit=True)
    N2,_,_,_=G2.next(N2,0,jobs,omit=True)
    x.ck(all(any(h in N2.J for h in pair) for pair in G2.gate_pair),'omitting all opening repetitions leaves both gates closed')
    # Pausing a predecessor in its old suffix is safe: successor can finish, then ring waits.
    G3=GClass(1,2,2);N3=G3.initial_node(table);grants=[]
    while not(N3.pcs[0].phase=='handoff' and N3.pcs[0].pos==5):
        N3,_,_,got=G3.next(N3,0,jobs)
        if got:grants.append(0)
    N3,_,gs=x.complete(G3,N3,1,jobs);grants+=list(gs)
    for _ in range(8):
        N3=G3.rearm(N3,1);N3,_,gs=x.complete(G3,N3,1,jobs)
        x.ck(not gs,'a stopped sender cannot be skipped by repeatedly reentering successor')
    x.ck(grants==[0,1],'safety persists while the non-reentrant sender is paused')
    return dict(mode='failures',one_port_order=list(N.order),one_port_trace=oldtrace,
                detached_replay_order=order,detached_release=raw,
                opening_group_entirely_omitted='both_closed',stopped_sender_order=grants,
                new_ring=G.stats(),omission_ring=G2.stats(),stopped_ring=G3.stats(),assertions=x.CHECKS)

def audit():
    G=GClass(1,2,2);tables=x.base.domain(G.C);cases=0
    # All 77 inherited source/table inputs, both actual cyclic phase parities, both actor positions.
    for table in tables:
        for bank in (0,1):
            for turn in (0,1):
                jobs=((('feedback',0),),(('feedback',0),))
                initial=G.C.encode(table)
                phases=(bank,bank) if turn==0 else (1-bank,bank)
                pcs=tuple(x.PC(bank=b) for b in phases)
                J=x.m.canon(initial+tuple(G.gate_pair[i][phases[i]] for i in range(2) if i!=turn))
                for i,v in enumerate(G.lanes):J=x.m.canon(J+x.p.reg(v.admitted,i)+x.p.reg(v.reply,1-i))
                node=x.Node(J,pcs,turn)
                node,steps,grants=x.complete(G,node,turn,jobs)
                expected=x.base.expected(G.C,table,('execute',0))
                x.ck(grants==(turn,) and G.C.decode(G.core(node.J))==expected,'all endpoint parities keep exact business interface')
                x.ck(x.old.bit(node.J,G.lanes[turn].reply)==expected[1],'old private output is replaced with this call result')
                x.ck(G.gate_pair[turn][1-phases[turn]] in node.J,'successful lane alternates actual gate bank')
                cases+=1
    return dict(mode='audit',source_preparations=len(tables),cases=cases,**G.stats())

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['fault_graph','failures','audit'])
    ap.add_argument('--repeats',type=int,default=3);ap.add_argument('--budget',type=int,default=2)
    ap.add_argument('--actors',type=int,default=2);ap.add_argument('--out',required=True);args=ap.parse_args()
    if args.mode=='fault_graph':ans=recurrent_faults(args.repeats,args.budget,args.actors)
    elif args.mode=='failures':ans=failures()
    else:ans=audit()
    Path(args.out).write_text(json.dumps(ans,ensure_ascii=False,indent=2)+'\n')
