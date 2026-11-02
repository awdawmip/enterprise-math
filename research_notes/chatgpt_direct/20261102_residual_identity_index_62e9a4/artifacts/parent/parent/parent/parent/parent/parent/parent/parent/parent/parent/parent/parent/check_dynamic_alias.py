"""Dynamic handles over the pinned triadic matching kernel.

Fresh names, handle-table actions, equality and registered migration are explicit
observer/executor extensions. Matching changes use the unchanged inherited BRC
kernel; no claim of compiling these metadata operations into reserve/release.
"""
from __future__ import annotations
from dataclasses import dataclass
from collections import deque
from itertools import combinations, product
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'parent'))
import check_identity as old
p, m, e, r = old.p, old.m, old.e, old.r
ONE, ZERO = old.ONE, old.ZERO
Triple = tuple[int, int, int]
Ticket = tuple[Triple, int]
CHECKS = 0
CALLS = 0
ABSTRACT_KERNEL_CALLS = 0
EXTENSION_STEPS = 0


def check(value, message):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(message)


@dataclass(frozen=True)
class Machine:
    state: old.NamedState
    refs: tuple[Ticket | None, ...]


def empty(k):
    return Machine(old.seed(()), (None,) * k)


def normalize_parts(events, refs):
    """Canonical equality classes; allocator cursor/retired unused names erased."""
    classes = {}
    def name(a):
        if a not in classes:
            classes[a] = len(classes)
        return classes[a]
    ev = tuple((h, name(a)) for h, a in sorted(events))
    rr = tuple(None if q is None else (q[0], name(q[1])) for q in refs)
    return ev, rr


def key(machine):
    return normalize_parts(machine.state.events, machine.refs)


def weak_key(machine):
    ns = machine.state.names()
    return machine.state.matching, tuple(None if q is None else (q[0], ns.get(q[0]) == q[1]) for q in machine.refs)


def represent(k, offset=0, reverse=False):
    events, refs = k
    labels = sorted({a for _, a in events} | {q[1] for q in refs if q is not None})
    images = [offset + 7*i + 3 for i in range(len(labels))]
    if reverse:
        images.reverse()
    ren = dict(zip(labels, images))
    ev = tuple((h, ren[a]) for h, a in events)
    rr = tuple(None if q is None else (q[0], ren[q[1]]) for q in refs)
    return Machine(old.NamedState(ev, max(images, default=offset) + 11), rr)


def palette_represent(k):
    events, refs = k
    return Machine(old.NamedState(tuple((h, a+1) for h, a in events), 100),
                   tuple(None if q is None else (q[0], q[1]+1) for q in refs))


def matching_step(machine, op, H, palette=None):
    """Actual original matching operation, then declared occurrence annotation."""
    global CALLS
    state, ok, delta = old.raw_step(machine.state, op, H)
    CALLS += 1
    if palette is not None and delta['created']:
        used = {a for _, a in machine.state.events} | {q[1] for q in machine.refs if q is not None}
        choices = [a for a in range(1, palette+1) if a not in used]
        if len(choices) < len(delta['created']):
            raise RuntimeError('Palette exhausted: live classes and registered references cover all colors')
        mapping = {a: choices[i] for i, (_, a) in enumerate(delta['created'])}
        state = old.NamedState(tuple((h, mapping.get(a, a)) for h, a in state.events), state.next_name)
    return Machine(state, machine.refs), bool(ok)


def step(machine, op, H, palette=None):
    """Sequential atomic table actions; no unregistered references can re-enter."""
    global EXTENSION_STEPS
    kind = op[0]
    if kind in ('reserve', 'release'):
        return matching_step(machine, p.add(op[1]) if kind == 'reserve' else p.one(op[1]), H, palette)
    EXTENSION_STEPS += 1
    rr = list(machine.refs)
    ns = machine.state.names()
    i = op[1]
    if kind == 'bind':
        h = op[2]
        rr[i] = (h, ns[h]) if h in ns else None
        response = rr[i] is not None
    elif kind == 'copy':
        rr[i] = rr[op[2]]
        response = rr[i] is not None
    elif kind == 'drop':
        response = rr[i] is not None
        rr[i] = None
    elif kind == 'valid':
        q = rr[i]
        return machine, q is not None and ns.get(q[0]) == q[1]
    elif kind == 'target':
        return machine, None if rr[i] is None else rr[i][0]
    elif kind == 'same':
        return machine, rr[i] is not None and rr[i] == rr[op[2]]
    elif kind == 'execute':
        q = rr[i]
        if q is None or ns.get(q[0]) != q[1]:
            return machine, False
        # Executing a handle does not erase its stored historical name.
        return matching_step(machine, p.one(min(q[0])), H, palette)
    else:
        raise ValueError(f'Unknown operation: {op}')
    return Machine(machine.state, tuple(rr)), response


def reduced_step(k, op, H):
    """Reducer on finite equality classes, separate from concrete allocator."""
    global ABSTRACT_KERNEL_CALLS
    ev, refs = k
    ns = dict(ev)
    rr = list(refs)
    kind = op[0]
    if kind in ('reserve', 'release', 'execute'):
        if kind == 'execute':
            q = rr[op[1]]
            if q is None or ns.get(q[0]) != q[1]:
                return k, False
            raw = p.one(min(q[0]))
        else:
            raw = p.add(op[1]) if kind == 'reserve' else p.one(op[1])
        J2, _, ok = e.step(tuple(h for h, _ in ev), raw, H)
        ABSTRACT_KERNEL_CALLS += 1
        labels = {a for _, a in ev} | {q[1] for q in rr if q is not None}
        fresh = max(labels, default=-1) + 1
        next_ev = []
        for h in J2:
            if h in ns:
                next_ev.append((h, ns[h]))
            else:
                next_ev.append((h, fresh)); fresh += 1
        return normalize_parts(next_ev, rr), bool(ok)
    i = op[1]
    if kind == 'bind':
        h = op[2]; rr[i] = (h, ns[h]) if h in ns else None
        response = rr[i] is not None
    elif kind == 'copy':
        rr[i] = rr[op[2]]; response = rr[i] is not None
    elif kind == 'drop':
        response = rr[i] is not None; rr[i] = None
    elif kind == 'valid':
        q = rr[i]
        return k, q is not None and ns.get(q[0]) == q[1]
    elif kind == 'target':
        return k, None if rr[i] is None else rr[i][0]
    elif kind == 'same':
        return k, rr[i] is not None and rr[i] == rr[op[2]]
    else:
        raise ValueError(kind)
    return normalize_parts(ev, rr), response


def weak_step(k, op, H):
    """Exact dynamic-target quotient when handle equality is not an observer."""
    global ABSTRACT_KERNEL_CALLS
    J, refs = k
    rr = list(refs)
    kind = op[0]
    if kind == 'same':
        raise ValueError('same is outside the weak language')
    if kind in ('reserve', 'release', 'execute'):
        if kind == 'execute':
            q = rr[op[1]]
            if q is None or not q[1]:
                return k, False
            raw = p.one(min(q[0]))
        else:
            raw = p.add(op[1]) if kind == 'reserve' else p.one(op[1])
        J2, _, ok = e.step(J, raw, H); ABSTRACT_KERNEL_CALLS += 1
        removed = set(J) - set(J2)
        rr = [None if q is None else (q[0], q[1] and q[0] not in removed) for q in rr]
        return (J2, tuple(rr)), bool(ok)
    i = op[1]
    if kind == 'bind':
        h = op[2]; rr[i] = (h, True) if h in J else None; response = rr[i] is not None
    elif kind == 'copy':
        rr[i] = rr[op[2]]; response = rr[i] is not None
    elif kind == 'drop':
        response = rr[i] is not None; rr[i] = None
    elif kind == 'valid':
        return k, rr[i] is not None and rr[i][1]
    elif kind == 'target':
        return k, None if rr[i] is None else rr[i][0]
    else:
        raise ValueError(kind)
    return (J, tuple(rr)), response


def alphabet(H, slots):
    U = sorted(set().union(*H))
    return (tuple(('reserve', h) for h in sorted(H)) + tuple(('release', a) for a in U)
            + tuple(('bind', i, h) for i in range(slots) for h in sorted(H))
            + tuple((t, i) for t in ('drop', 'valid', 'target', 'execute') for i in range(slots))
            + tuple((t, i, j) for t in ('copy', 'same') for i in range(slots) for j in range(slots)))


def reachable(H, slots):
    ops = alphabet(H, slots)
    initial = key(empty(slots))
    seen = {initial}; queue = deque([initial])
    while queue:
        k = queue.popleft()
        for op in ops:
            k2, _ = reduced_step(k, op, H)
            if k2 not in seen:
                seen.add(k2); queue.append(k2)
    return tuple(sorted(seen, key=repr)), ops


def run(machine, ops, H, palette=None, trace=False):
    rows = []; weight = ONE
    for op in ops:
        before = key(machine)
        machine, result = step(machine, op, H, palette)
        weight = r.serial(weight, ONE)
        if trace:
            rows.append(dict(operation=op, response=result, before=before, after=key(machine), concrete=machine.state.events, refs=machine.refs))
    return machine, rows, weight


def cases():
    h=(1,2,3); H={h}
    # Same current shape, same targets, same (false,false) validity, distinct aliasing.
    common=[('reserve',h),('bind',0,h)]
    a,ta,_=run(empty(2),common+[('copy',1,0),('release',1),('reserve',h)],H,trace=True)
    b,tb,_=run(empty(2),common+[('release',1),('reserve',h),('bind',1,h),('release',1),('reserve',h)],H,trace=True)
    check(weak_key(a)==weak_key(b), 'identical dynamic validity summary')
    check(step(a,('same',0,1),H)[1] and not step(b,('same',0,1),H)[1], 'stale alias is observable')
    check(key(a)!=key(b), 'partition repair distinguishes the preparations')
    # Losing a registered old handle to an untracked external party defeats recycling.
    z,_,_=run(empty(1),[('reserve',h),('bind',0,h)],H,palette=2)
    leaked=z.refs[0]
    z,_,_=run(z,[('release',1),('drop',0),('reserve',h)],H,palette=2)
    leaked_machine=Machine(z.state,(leaked,))
    _, accepted=step(leaked_machine,('execute',0),H,palette=2)
    check(accepted, 'unregistered escaped old color aliases reused event')
    # Resetting all stale names destroys their equality relation.
    stale_merged=Machine(a.state, tuple((h,100+i) for i in range(2)))
    check(not step(stale_merged,('same',0,1),H)[1], 'replacing each stale handle by a fresh color loses equality')
    return dict(alias_examples=[dict(trace=ta,final=key(a)),dict(trace=tb,final=key(b))],
                escaped_reference=dict(leaked=leaked,after_reuse=z.state.events,unexpected_acceptance=accepted))


def quotient(slots, multiple=False):
    H={(1,2,3)} if not multiple else {(1,2,3),(4,5,6),(1,2,4)}
    capacity=1 if not multiple else 2
    D, ops=reachable(H,slots)
    mass=ZERO; transitions=0; max_classes=0
    for k in D:
        A=represent(k,10); B=represent(k,10000,True); C=palette_represent(k)
        check(key(A)==key(B)==key(C)==k, 'class representation')
        max_classes=max(max_classes,len({x for _,x in k[0]} | {q[1] for q in k[1] if q is not None}))
        for op in ops:
            target,resp=reduced_step(k,op,H)
            aa,ra=step(A,op,H); bb,rb=step(B,op,H); cc,rc=step(C,op,H,capacity+slots)
            check(key(aa)==key(bb)==key(cc)==target and ra==rb==rc==resp, 'strong exact quotient and bounded palette')
            if op[0]!='same':
                wk,wr=weak_step(weak_key(A),op,H)
                check(weak_key(aa)==wk and ra==wr, 'weak dynamic quotient')
            transitions+=1; mass=r.merge(mass,ONE)
    return dict(slots=slots,candidates=sorted(H),states=len(D),operations=len(ops),
                transition_pairs=transitions,palette_size=capacity+slots,max_retained_classes=max_classes,
                CWM=e.cw(mass),keys=D)


def partitions(n):
    if n==0:
        yield ()
        return
    def visit(prefix,maximum):
        if len(prefix)==n:
            yield tuple(prefix);return
        for a in range(maximum+2):
            yield from visit(prefix+[a],max(maximum,a))
    yield from visit([0],0)


def partition_preparation(partition):
    h=(1,2,3); H={h}; machine=empty(len(partition)); word=[]
    for block in range(max(partition, default=-1)+1):
        word.append(('reserve',h))
        word.extend(('bind',i,h) for i,v in enumerate(partition) if v==block)
        word.append(('release',1))
    word.append(('reserve',h))
    machine,_,w=run(machine,word,H)
    return machine,word,w


def lower():
    h=(1,2,3);H={h};rows=[]
    for n in range(1,7):
        P=tuple(partitions(n));states=[];mass=ZERO
        for part in P:
            z,word,w=partition_preparation(part)
            check(all(not step(z,('valid',i),H)[1] for i in range(n)), 'all references stale')
            check(z.state.matching==(h,), 'common current matching')
            states.append(z);mass=r.merge(mass,w)
        pairs=0
        for i in range(len(P)):
            for j in range(i):
                u,v=next((u,v) for u in range(n) for v in range(u+1,n) if (P[i][u]==P[i][v])!=(P[j][u]==P[j][v]))
                check(step(states[i],('same',u,v),H)[1]!=step(states[j],('same',u,v),H)[1], 'common equality query distinguishes partitions')
                pairs+=1
        check(len({key(z) for z in states})==len(P), 'all alias partitions represented')
        rows.append(dict(handles=n,partitions=len(P),distinguishing_pairs=pairs,CWM=e.cw(mass)))
    return dict(rows=rows)


def cycles():
    h=(1,2,3);H={h};n=6
    ops=[]
    # Reach six distinct retired names and one current name simultaneously.
    for i in range(n):
        ops += [('reserve',h),('bind',i,h),('release',1)]
    ops += [('reserve',h)]
    for t in range(1000):
        i=t%n
        ops += [('bind',i,h),('release',1),('valid',i),('reserve',h),('valid',i),('same',i,(i+1)%n)]
        if t%7==0:
            ops += [('copy',(i+1)%n,i),('drop',(i+2)%n),('bind',(i+2)%n,h)]
    A=empty(n);B=empty(n);maximum=0;colors=set();mass=ONE
    for idx,op in enumerate(ops):
        A,ra=step(A,op,H)
        B,rb=step(B,op,H,n+1)
        check(key(A)==key(B) and ra==rb, 'bounded palette preserves full dynamic observations')
        retained={a for _,a in B.state.events}|{q[1] for q in B.refs if q is not None}
        maximum=max(maximum,len(retained));colors|=retained
        check(len(retained)<=n+1, 'palette bound')
        mass=r.serial(mass,ONE)
    check(maximum==7 and len(colors)==7, 'tight seven-color execution')
    return dict(handles=n,cycles=1000,steps=len(ops),palette=7,max_simultaneously_retained=maximum,
                colors=sorted(colors),fresh_allocator_cursor=A.state.next_name,final=key(A),CWM=e.cw(mass))


def migrate_probe(machine, C, inject_copy=None, partial=False, retarget_all=False):
    """Registered exclusive migration around the actual inherited probe.

Ref writes and capture are metadata operations. Only the probe is a compiled
150-call triadic word. inject_copy deliberately violates exclusive-table scope.
"""
    before=machine.state.names()
    live=[q is not None and before.get(q[0])==q[1] for q in machine.refs]
    original=list(machine.refs)
    state,weight,_=old.execute(machine.state,C['word'],C['H'])
    refs=list(original)
    if inject_copy is not None:
        dst,src=inject_copy
        refs[dst]=refs[src]
    after=state.names()
    selected=range(1) if partial else range(len(refs))
    for i in selected:
        q=refs[i]
        if q is not None and (retarget_all or (live[i] and q==original[i])):
            refs[i]=(q[0],after[q[0]])
    # Statement concerns the source projection; the private answer is separately retained.
    src=old.NamedState(old.source(state,C['U']),state.next_name)
    return Machine(src,tuple(refs)),dict(probe_calls=len(C['word']),source_before=machine.state.events,
              source_after=src.events,refs_before=machine.refs,refs_after=refs,live_before=live,
              private_verdict=p.read(state.matching,C['status']),CWM=e.cw(weight))


def migration():
    h=(1,2,3);H={h};C=old.prior.edge_test(tuple(range(1,7)),1,h)
    D,ops=reachable(H,4);mass=ZERO;transitions=0
    for k in D:
        A=represent(k,10);B,receipt=migrate_probe(A,C)
        check(key(A)==key(B), 'complete live-only migration preserves dynamic partition')
        for op in ops:
            aa,ra=step(A,op,H);bb,rb=step(B,op,H)
            check(key(aa)==key(bb) and ra==rb, 'migration preserves dynamic successor')
            transitions+=1
        mass=r.merge(mass,ONE)
    a,_,_=run(empty(3),[('reserve',h),('bind',0,h),('copy',1,0),('bind',2,h)],H)
    partial,pr=migrate_probe(a,C,partial=True)
    check(step(partial,('same',0,1),H)[1] is False, 'partial update splits alias class')
    check(weak_key(partial)!=weak_key(a), 'partial update invalidates an alias')
    # Stale and current reference, with one spare slot at capture time.
    b,_,_=run(empty(3),[('reserve',h),('bind',0,h),('release',1),('reserve',h),('bind',1,h)],H)
    proper,good=migrate_probe(b,C)
    naive,bad=migrate_probe(b,C,retarget_all=True)
    check(not step(proper,('valid',0),H)[1] and step(naive,('valid',0),H)[1], 'all-by-shape update revives stale reference')
    race,rr=migrate_probe(b,C,inject_copy=(2,1))
    check(step(race,('valid',1),H)[1] and not step(race,('valid',2),H)[1], 'late copy escapes precomputed migration set')
    return dict(states=len(D),successor_checks=transitions,probe_calls=len(C['word']),CWM=e.cw(mass),
                partial_alias=pr,correct=good,stale_resurrection=bad,late_copy=rr)


def histories():
    h=(1,2,3);H={h}
    ops=(('reserve',h),('release',1),('bind',0,h),('bind',1,h),('copy',1,0),('drop',0),('execute',0),('same',0,1))
    # Retain exact operational responses and accumulate positive history mass per quotient.
    start=key(empty(2));dp={(start,()):ONE}
    widths=[1]
    for depth in range(5):
        nd={}
        for (k,out),weight in dp.items():
            A=represent(k,100+depth*1000);B=palette_represent(k)
            for op in ops:
                aa,ra=step(A,op,H);bb,rb=step(B,op,H,3)
                check(key(aa)==key(bb) and ra==rb, 'all generated history prefixes preserve responses')
                dest=(key(aa),out+(ra,))
                w=r.serial(weight,ONE)
                nd[dest]=r.merge(nd.get(dest,ZERO),w)
        dp=nd;widths.append(len(dp))
    mass=ZERO
    for w in dp.values():mass=r.merge(mass,w)
    # Independent positive-CWM position-only recurrence, with no state pruning.
    position=ONE
    for _ in range(5):
        one_step=ZERO
        for _ in ops:one_step=r.merge(one_step,ONE)
        position=r.serial(position,one_step)
    check(e.cw(mass)==e.cw(position), 'history mass equals unpruned alphabet power')
    return dict(alphabet=ops,word_length=5,prefix_widths=widths,final_state_response_classes=len(dp),CWM=e.cw(mass))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['cases','quotient','multi','lower','cycles','migration','histories']);ap.add_argument('--out',required=True)
    args=ap.parse_args()
    fn={'cases':cases,'quotient':lambda:quotient(4),'multi':lambda:quotient(2,True),'lower':lower,'cycles':cycles,'migration':migration,'histories':histories}[args.mode]
    result=fn()
    result.update(mode=args.mode,assertions=CHECKS,concrete_original_kernel_calls=CALLS,
                  inherited_named_kernel_calls=old.KERNEL_CALLS,abstract_original_kernel_calls=ABSTRACT_KERNEL_CALLS,
                  metadata_steps=EXTENSION_STEPS)
    Path(args.out).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['keys','rows','alias_examples','partial_alias','correct','stale_resurrection','late_copy']},ensure_ascii=False)[:2400])

if __name__=='__main__':main()
