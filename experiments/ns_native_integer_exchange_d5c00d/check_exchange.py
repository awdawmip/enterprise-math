#!/usr/bin/env python3
"""Exact integer exchange / native transport test interface, not a force solver.

Run: python check_exchange.py --output results_15.json
No network, floating point, third-party dependency, or native-ontology change.
"""
from __future__ import annotations
import argparse
from collections import Counter
from dataclasses import dataclass
from itertools import combinations, permutations, product
import hashlib
import json
from pathlib import Path
import random
import sys
from typing import Sequence

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'deps'))
import native_router_source_extract as core

EVENT = 'NS-NATIVE-INTEGER-EXCHANGE-20260910-D5C00D-15'
D = 6
R0 = (1, 2, 3, 0)
R1 = (2, 0, 3, 1)
PAIRS = frozenset(combinations(range(6), 2))
ZERO = (0,) * D


def ints(v: Sequence[int], length: int | None = None) -> tuple[int, ...]:
    v = tuple(v)
    if (length is not None and len(v) != length) or any(type(x) is not int for x in v):
        raise ValueError('Expected a tuple of integers of the declared length')
    return v


def square(q):
    return sum(x*x for x in q)


def minimum_square(total: int, count: int) -> int:
    if type(total) is not int or type(count) is not int or count <= 0:
        raise ValueError('Integer total and positive integer population required')
    a, r = divmod(total, count)
    return count*a*a + 2*a*r + r


def balance3(q):
    q = ints(q, 3)
    if max(q) - min(q) <= 1:
        return q
    a, r = divmod(sum(q), 3)
    return tuple(a + int(i < r) for i in range(3))


def reflect3(q):
    """Comparison control: a residue-gated integer energy-preserving involution."""
    q = ints(q, 3)
    total = sum(q)
    if total % 3:
        return q
    return tuple(2*(total//3)-x for x in q)


def controller_step(tokens, frame, bit, rules=(R0, R1), template=core.STARS):
    new_tokens, _ = core.macro_step(tokens, frame, template)
    rule = rules[bit]
    return new_tokens, tuple(frame[i] for i in rule), 1-bit


def itinerary(rules=(R0, R1), frame=(0,1,2,3), bit=0, tokens=tuple(range(6))):
    initial = (tokens, frame, bit)
    state = initial
    rows = []
    for t in range(3000):
        tokens, frame, bit = state
        rows.append((tuple(tokens[i] for i in core.frame_axes(frame)), frame, bit))
        state = controller_step(*state, rules=rules)
        if state == initial:
            return rows
    raise AssertionError('Finite test itinerary exceeded its explicit bound')


def covered(rows):
    return frozenset(p for tri, _, _ in rows for p in combinations(sorted(tri), 2))


def window_width(rows):
    for width in range(1, len(rows)+1):
        if all(covered([rows[(t+i) % len(rows)] for i in range(width)]) == PAIRS
               for t in range(len(rows))):
            return width
    return None


def fair_four_cycles():
    result = []
    for r in permutations(range(4)):
        seen = set()
        x = 0
        while x not in seen:
            seen.add(x)
            x = r[x]
        if len(seen) == 4:
            result.append(r)
    return tuple(result)


def exchange_scalar(q, tri):
    result = list(q)
    new = balance3(tuple(q[i] for i in tri))
    for i, value in zip(tri, new):
        result[i] = value
    return tuple(result)


@dataclass(frozen=True)
class State:
    tokens: tuple[int, ...]  # retained source-slot -> token id during flight
    frame: tuple[int, ...]
    bit: int
    flight: int
    charges: tuple[tuple[int, ...], ...]  # indexed by immutable token id


class GatherExchangeRouter:
    """A local common-Cell exchange with retained source-slot provenance."""
    def __init__(self, anchor=ZERO, template=core.STARS):
        self.anchor = ints(anchor, 6)
        self.template = tuple(tuple(t) for t in template)
        for h in permutations(range(4)):
            if len(set(core.frame_axes(h, self.template))) != 3:
                raise ValueError('Illegal incidence template')

    def initial(self, charges, frame=(0,1,2,3), bit=0, tokens=tuple(range(6))):
        s = State(tuple(tokens), tuple(frame), bit, 0, tuple(ints(q,6) for q in charges))
        self.validate(s)
        return s

    def validate(self, s):
        if (sorted(s.tokens) != list(range(6)) or sorted(s.frame) != list(range(4))
                or type(s.bit) is not int or s.bit not in (0,1)
                or type(s.flight) is not int or s.flight not in (0,1)
                or len(s.charges) != 6):
            raise ValueError('Invalid controller or labelled participant state')
        for q in s.charges:
            ints(q, 6)

    def participants(self, s):
        return tuple(s.tokens[i] for i in core.frame_axes(s.frame, self.template))

    def positions(self, s):
        self.validate(s)
        active = set(self.participants(s))
        pos = [None]*6
        for slot, token in enumerate(s.tokens):
            pos[token] = (self.anchor if s.flight and token in active
                          else core.add(self.anchor, core.unit(slot)))
        return tuple(pos)

    def step(self, s):
        self.validate(s)
        if s.flight == 0:
            return State(s.tokens, s.frame, s.bit, 1, s.charges), 0
        tri = self.participants(s)
        charges = [list(q) for q in s.charges]
        for a in range(6):
            new = balance3(tuple(s.charges[i][a] for i in tri))
            for i, value in zip(tri, new):
                charges[i][a] = value
        charges = tuple(tuple(q) for q in charges)
        newtokens, newframe, newbit = controller_step(s.tokens, s.frame, s.bit,
                                                    template=self.template)
        drop = sum(square(q) for q in s.charges) - sum(square(q) for q in charges)
        out = State(newtokens, newframe, newbit, 0, charges)
        self.validate(out)
        return out, drop


def local_density(pos, charges, quadratic=False):
    d = Counter()
    for z, q in zip(pos, charges):
        if quadratic:
            d[z] += square(q)
        else:
            for a, val in enumerate(q):
                d[(z,a)] += val
    return d


def cleaned(c):
    return {k:v for k,v in c.items() if v}


def difference(a, b):
    c = Counter(a)
    c.subtract(b)
    return c


def check_microstep(router, s):
    out, drop = router.step(s)
    before, after = router.positions(s), router.positions(out)
    assert len(before) == len(after) == 6
    assert tuple(map(sum, zip(*s.charges))) == tuple(map(sum, zip(*out.charges)))
    phi0, phi1 = sum(map(square,s.charges)), sum(map(square,out.charges))
    assert phi0-phi1 == drop and drop >= 0 and drop % 2 == 0
    # Exchange occurs at the common Cell BEFORE the second movement.
    # Its local carried-quantity source is exactly zero.
    intermediate = local_density(before, out.charges)
    assert cleaned(intermediate) == cleaned(local_density(before, s.charges))
    divergence, ediv = Counter(), Counter()
    moving = 0
    for alpha, (z,w) in enumerate(zip(before,after)):
        delta = core.sub(w,z)
        length = sum(abs(v) for v in delta)
        assert length in (0,1)
        if not length:
            continue
        moving += 1
        for a, val in enumerate(out.charges[alpha]):
            divergence[(z,a)] -= val
            divergence[(w,a)] += val
        e = square(out.charges[alpha])
        ediv[z] -= e
        ediv[w] += e
    assert moving == 3
    assert cleaned(difference(local_density(after,out.charges),
                              local_density(before,s.charges))) == cleaned(divergence)
    if drop:
        ediv[router.anchor] -= drop
    assert cleaned(difference(local_density(after,out.charges,True),
                              local_density(before,s.charges,True))) == cleaned(ediv)
    return out, drop, moving


def transform_vector(v,p):
    w=[0]*6
    for i,x in enumerate(v): w[p[i]]=x
    return tuple(w)


def run():
    extract = HERE/'deps/native_router_source_extract.py'
    digest = hashlib.sha256(extract.read_bytes()).hexdigest()
    assert digest == 'a06546610f5e8b2679cc426007c54a6458e6874197a45d436606b981e8a9ab34'
    result={'schema':'EM_NATIVE_INTEGER_EXCHANGE_RESULTS_V1','event_id':EVENT,
            'status':'EXECUTED_EXACT_CHECKS_WITH_ORDINARY_PROOFS_NOT_PHYSICAL_FORCE',
            'source_extract_sha256':digest}
    # Independent enumeration of scalar integer minima.
    minima={}
    triples=tuple(product(range(-6,7),repeat=3))
    for q in triples:
        minima[sum(q)]=min(minima.get(sum(q),10**9),square(q))
    for q in triples:
        b=balance3(q)
        assert sum(b)==sum(q) and square(b)==minimum_square(sum(q),3)==minima[sum(q)]
        assert all(min(q)<=v<=max(q) for v in b)
        loss=square(q)-square(b)
        assert loss%2==0 and ((loss==0)==(max(q)-min(q)<=1))
        if loss==0: assert b==q
        a,r=divmod(sum(q),3)
        assert 3*minimum_square(sum(q),3)-sum(q)**2==r*(3-r)
        reflected=reflect3(q)
        assert sum(reflected)==sum(q) and square(reflected)==square(q)
        assert reflect3(reflected)==q
    result['integer_triples_checked']=len(triples)
    result['reflection_control']={'input':[0,3,3],'output':reflect3((0,3,3)),
                                  'sum':6,'quadratic_before_and_after':18}
    # Integer column/sum/contraction theorem small exact check without floats.
    passed=[];tested=0
    for off in product(range(-1,2),repeat=6):
        a,b,c,d,e,f=off
        T=((1-c-e,a,b),(c,1-a-f,d),(e,f,1-b-d))
        if any(abs(x)>2 for row in T for x in row):continue
        tested+=1
        # Unit-column tests and pair sums prove the classification here too.
        cols=tuple(zip(*T))
        if any(square(v)>1 for v in cols):continue
        if any(square(tuple(x+y for x,y in zip(cols[i],cols[j])))>2
               for i,j in combinations(range(3),2)):continue
        assert sorted(cols)==sorted(((1,0,0),(0,1,0),(0,0,1)))
        passed.append(T)
    result['linear_integer_checks']={'matrices_tested':tested,'passing_permutations':len(passed)}
    assert len(passed)==6
    # Six, and only six, fair equivariant right updates on a 24-frame carrier.
    fairs=fair_four_cycles();assert len(fairs)==6
    table=[]
    for r in fairs:
        rows=itinerary((r,r))
        table.append({'r':r,'macro_period':len(rows),'pair_count':len(covered(rows)),
                      'distinct_participant_triples':len({frozenset(q) for q,_,_ in rows})})
        assert len(covered(rows)) in (9,10) and len(covered(rows))<15
    result['frame24_fair_controller_classification']=table
    # Explicit, disclosed finite search for a two-fiber controller.
    good=[]
    for r0,r1 in product(fairs,repeat=2):
        rows=itinerary((r0,r1))
        if covered(rows)==PAIRS and {h[0] for _,h,_ in rows}==set(range(4)):
            good.append({'r0':r0,'r1':r1,'period':len(rows),'window':window_width(rows)})
    assert len(good)==6 and all(r['period']==30 and r['window']==8 for r in good)
    result['frame48_search']={'tested_pairs':36,'full_pair_mixers':good}
    rows=itinerary()
    assert len(rows)==30 and window_width(rows)==8
    triads=[tuple(sorted(q)) for q,_,_ in rows]
    assert all(triads[t]==triads[t%10] for t in range(30))
    paircounts=Counter(p for q in triads[:10] for p in combinations(q,2))
    assert set(paircounts)==set(PAIRS) and set(paircounts.values())=={2}
    result['selected_participant_triples_one_based']=[[i+1 for i in q] for q in triads[:10]]
    coverage_cases=0
    for frame in permutations(range(4)):
        for bit in (0,1):
            rotation=itinerary(frame=frame,bit=bit)
            assert len(rotation)==30 and window_width(rotation)==8
            assert {h[0] for _,h,_ in rotation}==set(range(4))
            coverage_cases+=1
    result['all_order_frame_bit_coverage_cases']=coverage_cases
    result['pair_occurrences_in_ten_events']=[{'pair':[i+1 for i in p],'events':[t for t,q in enumerate(triads[:10]) if set(p)<=set(q)]} for p in sorted(PAIRS)]
    # Original wheel restriction gives an explicit stationary nonoptimal load.
    stalled=(0,1,1,2,1,1);q=stalled
    for tri,_,_ in itinerary((R0,R0)):
        q=exchange_scalar(q,tri)
        assert q==stalled
    q=stalled;relax=[]
    for t,(tri,_,_) in enumerate(rows):
        q=exchange_scalar(q,tri)
        relax.append({'event':t+1,'q':q,'phi':square(q)})
        if max(q)-min(q)<=1:break
    assert len(relax)==5 and q==(1,)*6
    result['stalled_and_repaired']={'q0':stalled,'phi0':8,'minimum':6,
                                   'old_router_stationary':True,'new_router_trajectory':relax}
    # Exhaust a signed six-token box for exact convergence and the proved bound.
    maxsteps=0;totalsteps=0;loss_events=0
    for q0 in product(range(-2,3),repeat=6):
        q=q0;debt=square(q)-minimum_square(sum(q),6)
        assert debt>=0 and debt%2==0
        bound=4*debt
        t=0
        while max(q)-min(q)>1:
            tri=rows[t%len(rows)][0]
            new=exchange_scalar(q,tri)
            drop=square(q)-square(new)
            assert drop>=0 and drop%2==0 and sum(q)==sum(new)
            if new!=q: assert drop>=2;loss_events+=1
            q=new;t+=1
            assert t<=bound
        assert square(q)==minimum_square(sum(q),6)
        maxsteps=max(maxsteps,t);totalsteps+=t
    result['six_token_scalar_box']={'cases':5**6,'largest_events_to_equilibrium':maxsteps,
                                    'total_events':totalsteps,'positive_loss_events':loss_events}
    # Microstep executions with vector charges; bit/order/flight all current state.
    rng=random.Random(20260910)
    router=GatherExchangeRouter()
    micro=0;edges=0;max_tick=0;tested_paths=0
    for h in permutations(range(4)):
        for bit in (0,1):
            charges=tuple(tuple(rng.randrange(-9,10) for _ in range(6)) for _ in range(6))
            s=router.initial(charges,h,bit)
            for t in range(120):
                s,drop,e=check_microstep(router,s);micro+=1;edges+=e
                if all(max(q[a] for q in s.charges)-min(q[a] for q in s.charges)<=1 for a in range(6)):
                    max_tick=max(max_tick,t+1);break
            else:raise AssertionError('Chosen vector test did not settle in its bound')
            assert sum(map(square,s.charges))==sum(minimum_square(sum(q[a] for q in charges),6) for a in range(6))
            tested_paths+=1
    result['vector_microstep_runs']={'initial_controllers':tested_paths,'checked_ticks':micro,
                                    'moving_native_edges':edges,'largest_settling_tick':max_tick}
    # Every ordering/frame/phase coverage and label provenance; no new vertex identity.
    cov=0
    charges=tuple(tuple(3*i-a for a in range(6)) for i in range(6))
    base=router.initial(charges);middle,_=router.step(base);end,_=router.step(middle)
    for p in permutations(range(6)):
        template=tuple(tuple(p[i] for i in tri) for tri in core.STARS)
        tr=GatherExchangeRouter(template=template)
        tokens=[None]*6
        for slot,token in enumerate(base.tokens):tokens[p[slot]]=token
        tq=tuple(transform_vector(v,p) for v in charges)
        state=tr.initial(tq,tokens=tuple(tokens))
        for ref in (base,middle,end):
            assert tr.positions(state)==tuple(transform_vector(z,p) for z in router.positions(ref))
            assert state.charges==tuple(transform_vector(v,p) for v in ref.charges)
            state,_=tr.step(state);cov+=1
    result['S6_transported_covariance_checks']=cov
    # Individual source-slot memory is necessary at the gathering Cell.
    a=router.initial(tuple((i,0,0,0,0,0) for i in range(6)))
    amid,_=router.step(a)
    p=list(a.tokens);p[0],p[2]=p[2],p[0]
    b=router.initial(a.charges,tokens=tuple(p));bmid,_=router.step(b)
    assert router.positions(amid)==router.positions(bmid)
    # Identical complete identity-position and identity-charge views at midpoint.
    assert amid.charges==bmid.charges
    aend,_=router.step(amid);bend,_=router.step(bmid)
    assert router.positions(aend)!=router.positions(bend)
    result['midpoint_role_erasure_failure']=True
    # Closed-source-free quantity transport versus explicit quadratic loss.
    zcharges=tuple((stalled[i],0,0,0,0,0) for i in range(6))
    s=router.initial(zcharges);lossledger=[]
    for t in range(10):
        s,drop,_=check_microstep(router,s)
        if drop: lossledger.append({'tick':t+1,'location':ZERO,'loss':drop})
    assert lossledger==[{'tick':10,'location':ZERO,'loss':2}]
    result['example_quadratic_loss_ledger']=lossledger
    result['scope_limits']=[
        'Source slots/ordered participants are retained; role erasure is not safe.',
        '48 minimality is only for charge-blind equivariant extensions of this fixed frame-to-route interface.',
        'Integer load equalization is a declared dissipative algorithm, not a derived physical force law.',
        'Quadratic loss is not silently identified with total physical energy or heat.',
        'No viscosity calibration, continuum limit, NS proof, Lean build, or independent review.']
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=HERE/'results_15.json')
    a=p.parse_args()
    data=run()
    text=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
    a.output.write_text(text,encoding='utf-8')
    print(json.dumps({k:data[k] for k in ('integer_triples_checked','linear_integer_checks',
                         'six_token_scalar_box','vector_microstep_runs','example_quadratic_loss_ledger')},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
