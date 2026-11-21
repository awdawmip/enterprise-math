"""Creation-aware continuation of the pinned incidence/restoration model.

Matching transitions call the unchanged parent kernel.  Fresh occurrence names
and occurrence-bound requests are an explicit observer/carrier extension, not
newly compiled triadic operations or an asserted physical implementation.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'parent'))
import check_incidence as prior
p, m, e, r = prior.p, prior.m, prior.e, prior.r
ONE, ZERO = prior.ONE, prior.ZERO

Triple = tuple[int, int, int]
Ticket = tuple[Triple, int]
CHECKS = 0
KERNEL_CALLS = 0
STEPS = 0


def check(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


@dataclass(frozen=True)
class NamedState:
    events: tuple[tuple[Triple, int], ...]
    next_name: int

    @property
    def matching(self):
        return tuple(h for h, _ in self.events)

    def names(self):
        return dict(self.events)


def seed(J, first=1):
    J = m.canon(J)
    return NamedState(tuple((h, first+i) for i, h in enumerate(J)), first+len(J))


def source(state, U):
    U = frozenset(U)
    return tuple((h, name) for h, name in state.events if set(h) <= U)


def project(state, U):
    return tuple(h for h, _ in source(state, U))


def raw_step(state, op, H):
    """Use inherited matching kernel, then annotate actual births/deletions."""
    global STEPS, KERNEL_CALLS
    STEPS += 1
    KERNEL_CALLS += 1
    J, _, ok = e.step(state.matching, op, H)
    old = state.names()
    retired = tuple((h, old[h]) for h in state.matching if h not in J)
    born = tuple(h for h in J if h not in old)
    names = {h: old[h] for h in J if h in old}
    nxt = state.next_name
    creations = []
    for h in born:
        names[h] = nxt
        creations.append((h, nxt))
        nxt += 1
    new = NamedState(tuple(sorted(names.items())), nxt)
    return new, bool(ok), dict(created=creations, retired=retired)


def bound_step(state, ticket, H):
    """Semantic extension: consume only the named occurrence, not its successor."""
    global STEPS
    h, name = ticket
    if state.names().get(h) == name:
        new, _, delta = raw_step(state, p.one(min(h)), H)
        return new, True, delta
    STEPS += 1
    return state, False, dict(created=[], retired=[])


def execute(state, word, H, keep=False):
    weight = e.prep(state.matching)
    log = []
    for i, op in enumerate(word):
        old = state
        state, ok, delta = raw_step(state, op, H)
        weight = r.serial(weight, ONE)
        if keep:
            log.append(dict(index=i, operation=op, success=ok,
                            before=old.events, after=state.events, **delta))
    return state, weight, log


def mask(state, tickets):
    names = state.names()
    return tuple(names.get(h) == eta for h, eta in tickets)


def quotient_key(state, tickets):
    return state.matching, mask(state, tickets)


def abstract_step(key, op, H, tickets):
    """Exact finite-ticket quotient; labels outside tickets are not observed."""
    J, bits = key
    if op[0] == 'bound':
        i = op[1]
        if not bits[i]:
            return key, False
        old_h = tickets[i][0]
        J2, _, _ = e.step(J, p.one(min(old_h)), H)
        bits2 = tuple(v and h != old_h for v, (h, _) in zip(bits, tickets))
        return (J2, bits2), True
    J2, _, ok = e.step(J, op, H)
    removed = set(J) - set(J2)
    bits2 = tuple(v and h not in removed for v, (h, _) in zip(bits, tickets))
    # Newly created occurrences are fresh w.r.t. every fixed ticket name.
    return (J2, bits2), bool(ok)


def operational_step(state, op, H, tickets):
    if op[0] == 'bound':
        return bound_step(state, tickets[op[1]], H)
    return raw_step(state, op, H)


def quotient_catalog(U, tickets):
    """Declared finite admissible states: each edge has at most one live ticket."""
    by_edge = {}
    for i, (h, _) in enumerate(tickets):
        by_edge.setdefault(h, []).append(i)
    result = []
    for J in prior.catalog(tuple(U)):
        choices = [(-1,) + tuple(by_edge.get(h, ())) for h in J]
        for assignment in product(*choices):
            bits = [False]*len(tickets)
            for i in assignment:
                if i >= 0:
                    bits[i] = True
            result.append((J, tuple(bits)))
    return tuple(result)


def concretize(key, tickets, first):
    J, bits = key
    selected = {h: eta for on, (h, eta) in zip(bits, tickets) if on}
    events = []
    nxt = first
    for h in J:
        if h in selected:
            events.append((h, selected[h]))
        else:
            events.append((h, nxt)); nxt += 1
    return NamedState(tuple(events), nxt)


def cases():
    U=tuple(range(1,7)); C=prior.edge_test(U,1,(1,2,3)); H=C['H']
    J=m.canon(((1,2,3),(4,5,6)))
    s0=seed(J); s1,w,trace=execute(s0,C['word'],H,True)
    q=((1,2,3),s0.names()[(1,2,3)])
    before,before_ok,_=bound_step(s0,q,H)
    after,after_ok,_=bound_step(s1,q,H)
    check(before_ok and not after_ok, 'matching-restoring probe invalidates an old occurrence-bound request')
    check(project(s0,U)==project(s1,U), 'source matching is exactly restored')
    check(s0.names()[(4,5,6)]==s1.names()[(4,5,6)], 'untouched source occurrence preserved')
    raw0,_,_=raw_step(s0,p.one(1),H); raw1,_,_=raw_step(s1,p.one(1),H)
    check(project(raw0,U)==project(raw1,U), 'current-member release sees the restored matching')
    # Naive rebinding activates a stale request that already failed before the probe.
    h=(1,2,3); old=seed((h,)); stale=(h,old.names()[h])
    recreated,_,_=raw_step(old,p.one(1),H)
    recreated,_,_=raw_step(recreated,p.add(h),H)
    current=(h,recreated.names()[h])
    z,_,_=execute(recreated,C['word'],H)
    a,ok_stale,_=bound_step(z,stale,H)
    naive=(h,z.names()[h]); b,ok_naive,_=bound_step(z,naive,H)
    check(not ok_stale and ok_naive, 'shape-only rebinding resurrects a previously stale request')
    # Consistent ticket transport is an explicitly separate semantic transformation.
    transported=(h,z.names()[h])
    check(bound_step(z,transported,H)[1], 'transported live reference matches recreated source')
    return dict(program_length=len(C['word']),source=s0.events,restored_source=source(s1,U),
                original_ticket=q,bound_before=before_ok,bound_after=after_ok,
                before_bound_source=project(before,U),after_bound_source=project(after,U),
                raw_before=project(raw0,U),raw_after=project(raw1,U),
                CWM=e.cw(w),trace=trace,
                stale_rebinding=dict(stale=stale,current_before_probe=current,
                                     restored=source(z,U),naive=naive,unchanged_ticket_result=ok_stale,
                                     naive_result=ok_naive,naive_source=project(b,U)))


def restoration_domain():
    U=tuple(range(1,7)); C=prior.edge_test(U,1,(1,2,3)); P=prior.pool_test(U,U)
    rows=[]; edge_births=pool_births=0; mass=ZERO
    for J in prior.catalog(U):
        s0=seed(J); target=next((h for h in J if 1 in h),None)
        s1,w,trace=execute(s0,C['word'],C['H'],True)
        check(project(s1,U)==J, 'edge probe matching postcondition')
        check(p.read(s1.matching,C['status'])==int((1,2,3) in J), 'edge probe verdict unchanged')
        changed=tuple(h for h in J if s0.names()[h]!=s1.names()[h])
        check(changed==(() if target is None else (target,)), 'exact single-query identity disturbance set')
        births=sum(len([h for h,n in t['created'] if set(h)<=set(U)]) for t in trace)
        check(births==int(target is not None), 'one fresh source occurrence if pivot occupied')
        edge_births+=births
        for h,name in s0.events:
            check(bound_step(s1,(h,name),C['H'])[1]==(h!=target), 'pending requests preserved exactly off the disturbed event')
        s2,w2,log=execute(s0,P['word'],P['H'],True)
        check(project(s2,U)==J, 'four-pivot predicate restores matching')
        expected=sum(sum(a in h for h in J) for a in P['pivots'])
        actual=sum(len([h for h,n in t['created'] if set(h)<=set(U)]) for t in log)
        check(actual==expected, 'source recreation count equals occupied pivot incidences')
        check(all(s0.names()[h]!=s2.names()[h] for h in J), 'four pivots refresh every nonempty six-source event')
        pool_births+=actual
        mass=r.merge(mass,r.serial(w,w2))
        rows.append(dict(source=J,pivot_event=target,edge_refreshed=changed,
                         edge_births=births,pool_births=actual,pool_source=source(s2,U)))
    return dict(states=len(rows),edge_program=len(C['word']),pool_program=len(P['word']),
                edge_source_births=edge_births,pool_source_births=pool_births,
                CWM=e.cw(mass),rows=rows)


def quotient():
    U=tuple(range(1,7)); H=set(combinations(U,3))
    tickets=(((1,2,3),1),((1,2,3),2),((4,5,6),3),((1,2,4),4))
    D=quotient_catalog(U,tickets)
    ops=tuple(p.add(h) for h in sorted(H))+tuple(p.one(a) for a in U)+tuple(('bound',i) for i in range(len(tickets)))
    transitions=0; mass=ZERO; label_pairs=[]
    for key in D:
        A=concretize(key,tickets,100)
        B=concretize(key,tickets,1000)
        check(quotient_key(A,tickets)==key==quotient_key(B,tickets), 'different anonymous names share quotient')
        for op in ops:
            AA,oka,_=operational_step(A,op,H,tickets)
            BB,okb,_=operational_step(B,op,H,tickets)
            abstract,ok=abstract_step(key,op,H,tickets)
            check(quotient_key(AA,tickets)==abstract==quotient_key(BB,tickets) and oka==ok==okb,
                  'one-step exact commuting law for finite-ticket quotient')
            transitions+=1
            mass=r.merge(mass,ONE)
    # Distinct masks on same matching are separated by one actual bound operation.
    distinguish=0
    for i,key in enumerate(D):
        for other in D[i+1:]:
            if key[0]!=other[0] or key[1]==other[1]:continue
            j=next(j for j,(a,b) in enumerate(zip(key[1],other[1])) if a!=b)
            A=concretize(key,tickets,100);B=concretize(other,tickets,1000)
            AA,oa,_=bound_step(A,tickets[j],H);BB,ob,_=bound_step(B,tickets[j],H)
            check(oa!=ob and AA.matching!=BB.matching,'different live-binding masks have a distinguishing one-step future')
            distinguish+=1
    # New named queries require refinement; the empty fixed ticket context can collapse them.
    h=(1,2,3); A=seed((h,),100);B=seed((h,),1000)
    check(quotient_key(A,())==quotient_key(B,()), 'zero-ticket quotient forgets all names')
    check(bound_step(A,(h,100),H)[1] != bound_step(B,(h,100),H)[1], 'adding an external old name refines the observer')
    return dict(states=len(D),operations=len(ops),transition_pairs=transitions,
                same_matching_distinguishing_pairs=distinguish,CWM=e.cw(mass),
                tickets=tickets,scope='fixed tickets; fresh names never reuse any fixed ticket; no numeric-name or history observer')


def transport():
    """Explicit rebind of all live ticket references; stale references are retained.

This finite observer-layer transformation is not a compiled triadic instruction.
It assumes a trusted exclusive migration boundary and the complete ticket set.
"""
    U=tuple(range(1,7)); C=prior.edge_test(U,1,(1,2,3)); H=C['H']; rows=[]; mass=ZERO
    for J in prior.catalog(U):
        s0=seed(J,first=100)
        old=tuple(s0.events)
        stale=tuple((h,1+i) for i,h in enumerate(J))
        tickets=old+stale
        z,w,_=execute(s0,C['word'],H)
        # All stale names precede the initial allocation frontier and are never reused.
        transported=tuple((h,z.names()[h]) if s0.names().get(h)==eta else (h,eta) for h,eta in tickets)
        check(mask(s0,tickets)==mask(z,transported), 'transport preserves live and stale statuses')
        for q0,q1 in zip(tickets,transported):
            a,oa,_=bound_step(s0,q0,H);b,ob,_=bound_step(z,q1,H)
            check(oa==ob and project(a,U)==project(b,U), 'bound operations commute after complete valid ticket transport')
        # Test all original-source primitive one-steps after migration as well.
        for op in tuple(p.add(h) for h in combinations(U,3))+tuple(p.one(a) for a in U):
            a,oa,_=raw_step(s0,op,H);b,ob,_=raw_step(z,op,H)
            check(oa==ob and project(a,U)==project(b,U) and mask(a,tickets)==mask(b,transported),
                  'source operation plus future mask preserved after transport')
        mass=r.merge(mass,w)
        rows.append(dict(source=J,before=tickets,after=transported,mask=mask(s0,tickets)))
    # Partial migration: two aliases used to denote the same live occurrence.
    h=(1,2,3);s0=seed((h,));z,_,_=execute(s0,C['word'],H)
    aliases=((h,1),(h,1)); half=((h,z.names()[h]),aliases[1])
    check(mask(s0,aliases)==(True,True) and mask(z,half)==(True,False), 'one forgotten alias breaks transport')
    return dict(states=len(rows),rows=rows,CWM=e.cw(mass),partial_alias_failure=half,
                implementation='observer-layer rebind; explicit stronger operation, not an original reserve/release word')


def lower_bound():
    rows=[];mass=ZERO; pairs=0
    for k in range(1,7):
        edges=tuple(tuple(3*i+j for j in (1,2,3)) for i in range(k));H=set(edges)
        base=seed(edges);tickets=base.events;states=[]
        for recreate in product((False,True),repeat=k):
            z=base;w=e.prep(z.matching)
            for h,yes in zip(edges,recreate):
                if yes:
                    z,_,_=raw_step(z,p.one(h[0]),H);w=r.serial(w,ONE)
                    z,_,_=raw_step(z,p.add(h),H);w=r.serial(w,ONE)
            check(z.matching==base.matching and mask(z,tickets)==tuple(not v for v in recreate),
                  'actual deletion/recreation realizes every independent identity residual')
            states.append(z);mass=r.merge(mass,w)
        for i,a in enumerate(states):
            for b in states[i+1:]:
                j=next(j for j,(x,y) in enumerate(zip(mask(a,tickets),mask(b,tickets))) if x!=y)
                aa,oa,_=bound_step(a,tickets[j],H);bb,ob,_=bound_step(b,tickets[j],H)
                check(oa!=ob and aa.matching!=bb.matching, 'one bound request distinguishes every different mask')
                pairs+=1
        rows.append(dict(k=k,realized_states=len(states),logical_fixed_bits_required=k,
                         same_matching=base.matching))
    return dict(rows=rows,total_distinguishing_pairs=pairs,CWM=e.cw(mass))


def continuations():
    """Execute every length-three word over a ten-command continuation alphabet."""
    U=tuple(range(1,7)); H=set(combinations(U,3))
    tickets=(((1,2,3),1),((1,2,3),2),((4,5,6),3),((1,2,4),4))
    J=m.canon(((1,2,3),(4,5,6)))
    # Same retained relation graph: first event is bound, second is anonymous.
    key=(J,(True,False,False,False))
    A=concretize(key,tickets,100); B=concretize(key,tickets,1000)
    ops=(p.add((1,2,3)),p.add((4,5,6)),p.add((1,2,4)),p.add((3,5,6)),
         p.one(1),p.one(4))+tuple(('bound',i) for i in range(4))
    left={};right={};words=0
    for word in product(ops,repeat=3):
        a,b=A,B;wa=wb=ONE;ra=[];rb=[]
        for op in word:
            a,oa,_=operational_step(a,op,H,tickets)
            b,ob,_=operational_step(b,op,H,tickets)
            wa=r.serial(wa,ONE);wb=r.serial(wb,ONE)
            ra.append(oa);rb.append(ob)
            check(quotient_key(a,tickets)==quotient_key(b,tickets) and oa==ob,
                  'every actual continuation prefix has matching source and bound response')
        ka=(quotient_key(a,tickets),tuple(ra));kb=(quotient_key(b,tickets),tuple(rb))
        left[ka]=r.merge(left.get(ka,ZERO),wa)
        right[kb]=r.merge(right.get(kb,ZERO),wb)
        words+=1
    check(left==right,'CWM aggregate counts, total mass and dominant mass preserved by quotient')
    total=ZERO
    for w in left.values():total=r.merge(total,w)
    check(total.count==words,'all unit histories retained')
    return dict(word_length=3,alphabet=len(ops),words_per_realization=words,
                output_classes=len(left),CWM=e.cw(total),
                two_realizations=[A.events,B.events])


def main():
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=('cases','domain','quotient','transport','lower','continuations'))
    ap.add_argument('--out',required=True);args=ap.parse_args()
    funcs={'cases':cases,'domain':restoration_domain,'quotient':quotient,'transport':transport,'lower':lower_bound,'continuations':continuations}
    data=funcs[args.mode]()
    data['mode']=args.mode
    data['stats']=dict(assertions=CHECKS,annotated_steps=STEPS,concrete_kernel_calls=KERNEL_CALLS)
    Path(args.out).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(mode=args.mode,**data['stats']),ensure_ascii=False))

if __name__=='__main__': main()
