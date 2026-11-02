"""Boundary, reuse and finite-domain checks for the cooperative guard."""
from __future__ import annotations
from dataclasses import replace
from pathlib import Path
from itertools import product
import argparse,json
import check_guard as g
p,m,e,r=g.p,g.m,g.e,g.r
ONE,ZERO=g.ONE,g.ZERO

def audit():
    G=g.Guard(slots=1,actors=2);count=0;examples=[]
    jobs=((('feedback',0),),(('present',0),))
    for table in g.base.domain(G.C):
        for actor in (0,1):
            # Three initial output states are actual register preparations.
            for previous in (None,0,1):
                J=G.C.encode(table,previous)
                extra=()
                for v in G.lanes:
                    if previous is not None:extra+=p.reg(v.admitted,previous)+p.reg(v.reply,1-previous)
                node=g.Node(m.canon(J+extra),(g.PC(),g.PC('busy')) if actor==0 else (g.PC('busy'),g.PC()))
                localjobs=(((('feedback',0),)),((('feedback',0),)))
                # Idle other lane is retained and not misreported as an attempt.
                while node.pcs[actor].phase not in ('done','busy'):
                    node,raw,_=G.next(node,actor,localjobs)
                wanted=g.base.expected(G.C,table,('execute',0))
                core=G.core(node.J)
                g.ck(G.C.decode(core)==wanted,'All 77 tables execute correctly inside admission')
                v=G.lanes[actor];other=G.lanes[1-actor]
                want=G.C.encode(*wanted)+p.reg(v.admitted,1)+p.reg(v.reply,int(wanted[1]))
                if previous is not None:want+=p.reg(other.admitted,previous)+p.reg(other.reply,1-previous)
                g.ck(node.J==m.canon(want),'Private old results clear only in owning lane; all work clean')
                count+=1
    for case,table in [('valid_A',((0,None,0),((0,0),)+(None,)*5)),
                       ('valid_B',((None,0,None),((1,0),)+(None,)*5)),
                       ('valid_C',((0,None,0),((2,0),)+(None,)*5)),
                       ('stale_B',((0,None,0),((1,0),)+(None,)*5))]:
        Q=g.Guard(slots=6,actors=2);tasks=((('feedback',0),),(('present',1),))
        node=g.Node(Q.C.encode(table),(g.PC(),g.PC('busy')));n=0
        while node.pcs[0].phase not in ('done','busy'):node,_,_=Q.next(node,0,tasks);n+=1
        g.ck(Q.C.decode(Q.core(node.J))==g.base.expected(Q.C,table,('execute',0)),'Six-slot interface result')
        examples.append(dict(case=case,raw_commands=n,body_commands=n-21,members=Q.members,
                             candidates=len(Q.H),kernel_calls=Q.calls,primitive_uses=Q.uses,result=g.bit(node.J,Q.lanes[0].reply)))
    return dict(mode='audit',cases=count,six_slot=examples,**G.stats())


def failures():
    G=g.Guard(slots=1,actors=2);C=G.C
    table=((0,None,0),((0,0),));J=C.encode(table);rows={}
    # A loser reads the shared gate instead of its own private ownership marker.
    J,_=G.runword(J,G.entry[0]);g.ck(g.bit(J,G.lanes[0].admitted),'Owner acquired')
    v=G.lanes[1]
    hh,reader,_=g.base.old.reader(G.g,v.admitted,v.work)
    wrong=tuple(p.clear_word(v.reply)+p.clear_word(v.admitted)+[p.add(G.lock(1))]+reader)
    H=G.H|frozenset(hh);K=J
    for raw in wrong:K,_,_=e.step(K,raw,H)
    g.ck(g.bit(K,v.admitted) and G.lock(1) not in K,'Reading shared gate yields false ownership')
    rows['shared_gate_is_not_ownership']=dict(owner_lock=G.lock(0),failed_lock=G.lock(1),wrong_result=True)
    # One omitted private probe similarly produces false success on contention.
    K=J
    omitted=5 # 0-based: four clears, reserve, then first reader probe
    for j,raw in enumerate(G.entry[1]):
        if j!=omitted:K,_=G._raw(K,raw)
    g.ck(g.bit(K,v.admitted) and G.lock(1) not in K,'Omitted private probe invalidates fault-free theorem')
    rows['omitted_probe']=dict(position=omitted+1,operation=G.entry[1][omitted],false_positive=True)
    # Late result copying: a safe body answer can be overwritten after unlocking.
    tab=((0,None,0),((1,0),));K=C.encode(tab)
    K,_=G.runword(K,G.entry[0]);K,_,_=C.runword(K,C.programs[('valid',0)])
    g.ck(not C.observe_result(K),'First operation result is false')
    K,_=G.runword(K,(p.one(G.lanes[0].a),))
    K,_=G.runword(K,G.entry[1]);K,_,_=C.runword(K,C.programs[('present',0)])
    g.ck(C.observe_result(K),'Second body changes shared result to true')
    K,_=G.runword(K,G.exit[1]);K,_=G.runword(K,G.exit[0][:-1])
    g.ck(g.bit(K,G.lanes[0].reply),'Late copy corrupts first caller answer')
    rows['copy_after_unlock']=dict(expected=False,actual=True)
    # Cooperative guard cannot fence a raw source release bypassing the guard.
    K=C.encode(table);K,_=G.runword(K,G.entry[0]);K,_,_=C.runword(K,C.programs[('match',0,0)])
    g.ck(C.observe_result(K),'Positive match really happened while guard held')
    K,_,_=C.runword(K,C.programs[('release',1)])
    K,_,_=C.runword(K,C.programs[('reserve',0)])
    g.ck(not g.base.expected(C,C.decode(G.core(K))[0],('valid',0))[1],'Old request stale after bypass recreation')
    K,_=G.runword(K,C.commit(0));g.ck(C.targets[0] not in K,'Guard cannot stop unregistered raw writers')
    rows['bypass']=dict(guard_still_present=G.lock(0) in K,new_A_deleted=True)
    # If the holder stalls, a finite failed attempt is safe; no crash recovery is claimed.
    K=C.encode(table);K,_=G.runword(K,G.entry[0]);hold=K
    failed=0
    for _ in range(20):
        K,_=G.runword(K,G.entry[1]);failed+=not g.bit(K,G.lanes[1].admitted)
    g.ck(failed==20 and G.lock(0) in K,'Stalled owner is not forcibly bypassed')
    rows['stalled_holder']=dict(failed_attempts=failed,owner_preserved=True)
    return dict(mode='failures',witnesses=rows,**G.stats())


def cycles(rounds=100):
    G=g.Guard(slots=6,actors=2)
    table=((0,None,0),((0,0),)+(None,)*5);J=G.C.encode(table)
    st=g.base.ref.old.seed(J);cname=st.names()[G.C.targets[2]]
    calls=steps=busy=0;log=[]
    def attempt_sequence(jobs,chooser):
        nonlocal J,st,calls,steps,busy,table
        node=g.Node(J,(g.PC(),g.PC()));initial=table
        while not G.done(node):
            i=chooser(node)
            node,raw,_=G.next(node,i,jobs)
            st,_,delta=g.base.ref.old.raw_step(st,raw,G.H)
            g.ck(st.matching==node.J,'Reuse schedule and original birth extension agree')
            g.ck(st.names().get(G.C.targets[2])==cname,'C original birth retained in every prefix')
            steps+=1
        answers=G.terminal(node,jobs,initial);J=node.J;table=G.C.decode(G.core(J))[0]
        calls+=2;busy+=sum(x[1]=='BUSY' for x in answers)
        return answers
    turn=[0]
    def alternate(node):
        wanted=turn[0];turn[0]=1-wanted
        return wanted if node.pcs[wanted].phase not in ('busy','done') else 1-wanted
    for k in range(rounds):
        # Parent source/references also go through the same gate.
        jobs=((('feedback',0),),(('release',1),('reserve',0),('bind',0,0)))
        a=attempt_sequence(jobs,alternate)
        jobs=((('reserve',0),('bind',0,0)),(('valid',0),))
        b=attempt_sequence(jobs,alternate)
        if k<3 or k==rounds-1:log.append(dict(round=k,first=a,second=b))
    # Construct a repeatable starvation cycle: both lanes get steps, only 0 holds.
    starve_J=J;cycles=[]
    for k in range(10):
        jobs=((('valid',0),),(('valid',0),))
        node=g.Node(starve_J,(g.PC(),g.PC()))
        for _ in range(11):node,_,_=G.next(node,0,jobs)
        for _ in range(11):node,_,_=G.next(node,1,jobs)
        while node.pcs[0].phase!='done':node,_,_=G.next(node,0,jobs)
        a=G.terminal(node,jobs,table)
        g.ck(a[1][1]=='BUSY','Scheduled competitor can be repeatedly overtaken')
        cycles.append(node.J);starve_J=node.J
    g.ck(all(K==cycles[0] for K in cycles[1:]),'Starvation example is an exact matching lasso')
    return dict(mode='cycles',rounds=rounds,attempts=calls,primitive_commands=steps,busy=busy,
                sample=log,named_kernel_calls=g.base.ref.old.KERNEL_CALLS,starvation_periodic_state=True,starvation_repeats=10,**G.stats())


def protected_entry():
    """Local omission checks only: competitor holds gate throughout this attempt."""
    G=g.Guard(slots=1,actors=2);tab=((0,None,0),((0,0),));rows=[]
    for held in (False,True):
        J=G.C.encode(tab)
        if held:J,_=G.runword(J,G.entry[0])
        i=1
        for f in (1,2):
            w=tuple(raw for raw in G.entry[i] for _ in range(f+1))
            D={(J,0):e.prep(J)}
            for raw in w:
                nxt={}
                for (K,used),mass in D.items():
                    G.uses+=1;L,_=G._raw(K,raw);key=L,used
                    nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
                    if used<f:
                        key=K,used+1;nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
                D=nxt
            counts={}
            for (K,used),mass in D.items():
                g.ck(g.bit(K,G.lanes[i].admitted)==(not held),'Protected entry local omission result')
                g.ck((G.lock(i) in K)==(not held),'Protected result agrees with physical owner')
                counts[used]=r.merge(counts.get(used,ZERO),mass)
            rows.append(dict(held=held,f=f,commands=len(w),mass={str(k):e.cw(v) for k,v in counts.items()}))
    return dict(mode='local_omissions',rows=rows,**G.stats())

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['audit','failures','cycles','omissions']);ap.add_argument('--out',required=True)
    a=ap.parse_args();ans={'audit':audit,'failures':failures,'cycles':cycles,'omissions':protected_entry}[a.mode]()
    Path(a.out).write_text(json.dumps(ans,ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps({k:v for k,v in ans.items() if k not in ('sample','witnesses')},ensure_ascii=False))
