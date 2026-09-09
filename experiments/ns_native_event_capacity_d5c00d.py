#!/usr/bin/env python3
"""Finite capacity/provenance and autonomous routing audit on native X6.

An explicit reservation-and-routing interface, not primitive force dynamics or
Navier--Stokes. The four incidences are a supplied material template, not an
identification of the FCC observer with physical interaction. Integer and
Fraction arithmetic only. Run: python ns_native_event_capacity_d5c00d.py
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
import json
from math import factorial, prod
from pathlib import Path

EVENT = 'NS-NATIVE-EVENT-CAPACITY-20260909-D5C00D-13'
STARS = ((0, 2, 5), (0, 3, 4), (1, 2, 4), (1, 3, 5))
SIGNED = ((1,0,-1,0,0,-1), (1,0,0,-1,-1,0),
          (0,1,-1,0,1,0), (0,1,0,-1,0,1))
PAIR_TO_AXIS = {tuple(s for s in range(4) if i in STARS[s]): i
                for i in range(6)}
ZERO = (0,) * 6

def require_nats(x, size):
    if len(x) != size or any(type(v) is not int or v < 0 for v in x):
        raise ValueError('expected nonnegative integer tuple of declared size')

def demand(x):
    require_nats(x, 4)
    return tuple(sum(x[s] for s in range(4) if i in STARS[s])
                 for i in range(6))

def feasible(n, x):
    require_nats(n, 6)
    return all(a <= b for a, b in zip(demand(x), n))

def allocations(n):
    require_nats(n, 6)
    bounds = [min(n[i] for i in e) for e in STARS]
    return tuple(x for x in product(*(range(b + 1) for b in bounds))
                 if feasible(n, x))

def perfect(n):
    """Exact inverse of A*x=n on the nonnegative integer cone, or None."""
    require_nats(n, 6)
    a,b,c,d,e,f = n
    if a+b != c+d or a+b != e+f:
        return None
    numerators = (a+c-e, a+e-c, c+e-a, 2*b-c-e+a)
    if any(k < 0 or k % 2 for k in numerators):
        return None
    x = tuple(k//2 for k in numerators)
    if demand(x) != n:
        raise AssertionError('inverse formula failed')
    return x

def labelled_lifts(n, x):
    """Number of unordered, token-disjoint typed triple collections."""
    if not feasible(n, x):
        return 0
    numerator = prod(factorial(k)//factorial(k-d)
                     for k, d in zip(n, demand(x)))
    denominator = prod(factorial(k) for k in x)
    if numerator % denominator:
        raise AssertionError('noninteger labelled lift count')
    return numerator//denominator

def actual_token_batches(n, x):
    """Small exact enumeration independent of the counting formula."""
    if not feasible(n, x):
        return ()
    event_tokens = [tuple(product(*[tuple((i,a) for a in range(n[i]))
                                     for i in triad])) for triad in STARS]
    choices = [tuple(combinations(items, x[s]))
               for s,items in enumerate(event_tokens)]
    ans = []
    for by_type in product(*choices):
        used = [token for group in by_type for event in group for token in event]
        if len(used) == len(set(used)):
            ans.append(by_type)
    return tuple(ans)

def event_axis_permutation(p):
    return tuple(PAIR_TO_AXIS[tuple(sorted(p[s] for s in pair))]
                 for pair,axis in sorted(PAIR_TO_AXIS.items(), key=lambda kv:kv[1]))

def act_counts(x,p):
    ans=[0]*len(x)
    for i,v in enumerate(x): ans[p[i]]=v
    return tuple(ans)

def unit(i):
    return tuple(int(i==j) for j in range(6))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))

def readout(z):
    a,b,c,d,e,f=z
    return (a+b+c+d,a-b+e+f,c-d+e-f)

def frame_axes(frame, template=STARS):
    """Orient the current triple by the stored order of its three neighbors."""
    a,*others=frame
    ans=[]
    for b in others:
        shared=set(template[a]) & set(template[b])
        if len(shared)!=1:
            raise ValueError('template must have the stated pairwise intersections')
        ans.append(next(iter(shared)))
    return tuple(ans)

def macro_step(tokens, frame, template=STARS):
    if sorted(tokens)!=list(range(6)) or sorted(frame)!=list(range(4)):
        raise ValueError('distinct six tokens and four-event frame required')
    axes=frame_axes(frame,template)
    out=list(tokens)
    for k,i in enumerate(axes): out[axes[(k+1)%3]]=tokens[i]
    return tuple(out),frame[1:]+frame[:1]

def micro_path(tokens,frame,anchor=ZERO,template=STARS):
    """Return token-id indexed start/middle/end for a two-tick event.

    Frame and phase determine the entire next step; no external selector.
    At midpoint tokens carry the same current frame; commit rotates that frame.
    """
    axes=frame_axes(frame,template)
    start={tokens[i]:add(anchor,unit(i)) for i in range(6)}
    middle=dict(start);end=dict(start)
    for k,i in enumerate(axes):
        j=axes[(k+1)%3]
        middle[tokens[i]]=add(add(anchor,unit(i)),unit(j))
        end[tokens[i]]=add(anchor,unit(j))
    return start,middle,end

def permutation_order(p):
    out=tuple(range(len(p)));base=out
    for k in range(1,721):
        out=tuple(p[out[i]] for i in range(len(p)))
        if out==base: return k
    raise AssertionError('permutation order too large')

def run():
    report={'schema':'EM_NATIVE_EVENT_CAPACITY_RESULTS_V1','event_id':EVENT}
    # Perfect utilization: independent forward image and inverse formula.
    image={demand(x):x for x in product(range(5),repeat=4)
           if max(demand(x))<=4}
    for n in product(range(5),repeat=6):
        assert perfect(n)==image.get(n)
    report['perfect_utilization']={'capacities_checked':5**6,
                                    'exactly_decomposable':len(image)}
    profiles=[];total_allocations=0;covariance=0
    group=tuple(permutations(range(4)))
    for q in range(13):
        n=(q,)*6;family=allocations(n);total_allocations+=len(family)
        best=max(map(sum,family));maximizers=tuple(x for x in family if sum(x)==best)
        expected=2*q-(q%2)
        assert best==expected
        assert len(maximizers)==(4 if q%2 else 1)
        invariant=tuple(x for x in family if len(set(x))==1)
        assert max(map(sum,invariant))==4*(q//2)
        if q%2:
            r=q//2
            assert set(maximizers)=={tuple(r+int(i==j) for i in range(4)) for j in range(4)}
        profiles.append({'q':q,'fractional_max':2*q,'integer_max':best,
                         'maximizer_count':len(maximizers),
                         'max_invariant_events':4*(q//2)})
        # Check every allocation under generators, all 24 actions on optima.
        for x in family:
            for p in ((1,0,2,3),(0,2,1,3),(0,1,3,2)):
                ap=event_axis_permutation(p)
                assert demand(act_counts(x,p))==act_counts(demand(x),ap)
                covariance+=1
        for p in group:
            assert {act_counts(x,p) for x in maximizers}==set(maximizers)
    report['symmetric_capacity']={'profiles':profiles,'allocations_checked':total_allocations,
                                  'capacity_covariance_equalities':covariance}
    # Fractional optimum for q=1 is outside the integer-batch convex hull.
    f=(Fraction(1,2),)*4
    fractional_demand=tuple(sum(f[s] for s in range(4) if i in STARS[s]) for i in range(6))
    assert fractional_demand==(1,)*6 and sum(f)==2
    assert max(map(sum,allocations((1,)*6)))==1
    # Token provenance counts, independently enumerated.
    lifts=[]
    for n,x in (((2,)*6,(1,1,1,1)),((2,)*6,(2,0,0,0)),
                ((1,)*6,(1,0,0,0)),((3,)*6,(1,1,0,0))):
        actual=actual_token_batches(n,x)
        assert len(actual)==labelled_lifts(n,x)
        lifts.append({'n':n,'x':x,'labelled_batches':len(actual)})
    report['token_provenance']=lifts
    # Entire 20-triple palette, unit capacities: exact legal maximal batches.
    triples=tuple(combinations(range(6),3))
    full_batches=tuple((a,b) for a,b in combinations(triples,2) if set(a).isdisjoint(b))
    assert len(full_batches)==10
    full_cov=0
    for p in permutations(range(6)):
        def pt(t):return tuple(sorted(p[i] for i in t))
        transformed={tuple(sorted((pt(a),pt(b)))) for a,b in full_batches}
        assert transformed==set(full_batches)
        full_cov+=len(full_batches)
    assert len(set().union(*[set(x) for x in full_batches]))==20
    report['complete_palette']={'triples':20,'optimal_batches':10,
                                'S6_batch_covariance_equalities':full_cov,
                                'fixed_maximal_batches':0}
    # Signed spatial closure is separate from unsigned simultaneous capacity.
    relation=(1,-1,-1,1)
    closure=tuple(sum(relation[s]*SIGNED[s][i] for s in range(4)) for i in range(6))
    assert closure==ZERO and demand(tuple(map(abs,relation)))==(2,)*6
    assert all(readout(r)==(0,0,0) for r in SIGNED)
    # Relation equality iff lambda times (1,-1,-1,1), checked bounded lattice.
    closed=[]
    for x in product(range(-3,4),repeat=4):
        zero=all(sum(x[s]*SIGNED[s][i] for s in range(4))==0 for i in range(6))
        expected=x==tuple(x[0]*r for r in relation)
        assert zero==expected
        if zero:closed.append(x)
    report['signed_closure']={'coefficient_tuples_checked':7**4,'closed':closed,
                              'minimum_nonzero_net_block_resources_per_axis':2}
    # Autonomous 24-state frame: equivariance, fairness and exact recurrence.
    rotor_cov=0;micro_edges=0;macro_sequences=0
    base=tuple(range(6));orders=[]
    for frame0 in group:
        tokens=base;frame=frame0;seen=[]
        for t in range(20):
            start,middle,end=micro_path(tokens,frame)
            assert len(set(middle.values()))==6
            for token in range(6):
                for x,y in ((start[token],middle[token]),(middle[token],end[token])):
                    d=sub(y,x)
                    assert sum(abs(v) for v in d) in (0,1)
                    if d!=ZERO:micro_edges+=1
            # Same six cells restored after two native ticks, tokens retained.
            assert Counter(start.values())==Counter(end.values())
            midpoint_delta=tuple(sum(middle[a][i]-start[a][i] for a in range(6)) for i in range(6))
            assert midpoint_delta==tuple(int(i in frame_axes(frame)) for i in range(6))
            nxt,nframe=macro_step(tokens,frame)
            assert end=={nxt[i]:unit(i) for i in range(6)}
            seen.append(frame[0]);tokens,frame=nxt,nframe
            macro_sequences+=1
            if t==3:
                assert frame==frame0
                orders.append(permutation_order(tokens))
                assert sum(int(tokens[i]==i) for i in range(6))==1
        assert tokens==base and frame==frame0
        assert all(set(seen[i:i+4])==set(range(4)) for i in range(0,20,4))
        for p in group:
            ap=event_axis_permutation(p)
            transformed_frame=tuple(p[s] for s in frame0)
            assert frame_axes(transformed_frame)==tuple(ap[i] for i in frame_axes(frame0))
            transformed_tokens=act_counts(base,ap)
            left,lf=macro_step(transformed_tokens,transformed_frame)
            right,rf=macro_step(base,frame0)
            assert left==act_counts(right,ap) and lf==tuple(p[s] for s in rf)
            rotor_cov+=1
    assert set(orders)=={5}
    # Check all token relabelings; all 24 frame full-state macro orbits have length20.
    recurrence=0
    for frame0 in group:
        for tokens0 in permutations(range(6)):
            tokens,frame=tokens0,frame0
            for t in range(1,21):
                tokens,frame=macro_step(tokens,frame)
                assert (tokens,frame)!=(tokens0,frame0) or t==20
            assert (tokens,frame)==(tokens0,frame0)
            recurrence+=1
    # Arbitrary S6 relabeling transports the incidence template too.
    arbitrary_cov=0
    frame0=group[0]
    st,mi,en=micro_path(base,frame0)
    for ap in permutations(range(6)):
        template=tuple(tuple(ap[i] for i in e) for e in STARS)
        tokens=act_counts(base,ap)
        a,b,c=micro_path(tokens,frame0,template=template)
        trans=lambda z:act_counts(z,ap)
        assert a=={i:trans(z) for i,z in st.items()}
        assert b=={i:trans(z) for i,z in mi.items()}
        assert c=={i:trans(z) for i,z in en.items()}
        arbitrary_cov+=1
    for anchor in ((7,-2,1,0,3,-4),(-1,)*6,(1,2,3,4,5,6)):
        a,b,c=micro_path(base,frame0,anchor)
        assert all(v=={i:add(anchor,z) for i,z in w.items()}
                   for v,w in zip((a,b,c),(st,mi,en)))
    report['autonomous_router']={'internal_order_states':24,'order_phase_pairs':48,
         'rotor_covariance_equalities':rotor_cov,'macro_steps_checked':macro_sequences,
         'nonzero_native_microsteps_checked':micro_edges,
         'initial_frame_token_states_checked':recurrence,
         'macro_full_state_period':20,'native_tick_full_state_period':40,
         'S6_transported_template_checks':arbitrary_cov,'translation_checks':3,
         'four_event_particle_permutation_cycle_type':[5,1]}
    report['scope']=['Explicit reservation and packet-routing candidate, not a force law',
        'No local TRIADIC_CLOSURE_E admissibility inferred from resource arithmetic',
        'No viscosity, physical f=0, instability, or NS theorem',
        'No force or energy assigned to temporary position-sum changes',
        'Fractional allocation is a comparison, never an executable event',
        'No Lean or independent review; no historical novelty assertion']
    return report

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('results_13.json'))
    args=parser.parse_args()
    result=run()
    text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    args.output.write_text(text,encoding='utf-8')
    print(text)

if __name__=='__main__':main()
