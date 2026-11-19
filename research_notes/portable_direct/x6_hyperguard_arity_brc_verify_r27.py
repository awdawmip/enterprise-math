#!/usr/bin/env python3
"""Exact Boolean support / labeled successful-word language verification for X6 R27.

The tested controller is declared, conditional and deterministic, not asserted to
be an authenticated TRIADIC_CLOSURE_E update implementation.
"""
import itertools
import json
import math
import random
from functools import lru_cache
from pathlib import Path


def bitcount(x):
    return x.bit_count()


def edges_of_size(m, sizes):
    return [sum(1 << x for x in comb)
            for k in sizes for comb in itertools.combinations(range(m), k)]


def active_edges(mask, edges):
    return tuple(j for j,e in enumerate(edges) if e & mask == e)


def eligible_edges_for_h(edges, h):
    return tuple(e for e in edges if 2 * bitcount(e) + 1 <= h)


def canonical_support(mask, edges):
    w=0
    for e in edges:
        if (mask & e) == e:
            w |= e
    return w


def predicted_partition(mask, edges, h):
    return active_edges(mask, eligible_edges_for_h(edges, h))


def all_words_signature(m, edges, theta_mask, max_h, intern):
    """Signature interning of entire Boolean successful-word language, ≤h.

    Public dynamic state: signed-lane phase bits, first-return bits, used consumer bits.
    Hidden immutable theta controls conditional per-return Link flags.
    Each source i has a unique +Ei/-Ei port label, each consumer e has its own
    unique +Ei port label (its own geometrically disjoint lane).
    """
    ids=[]
    @lru_cache(None)
    def rec(phase, returned, used, h):
        if h==0: return 0
        edgesign=[]
        for i in range(m):
            p=1 << i
            if phase & p:
                nx=(phase ^ p, returned | p, used)
                lab=f'B{i}-'
            else:
                nx=(phase | p, returned, used)
                lab=f'B{i}+'
            edgesign.append((lab,rec(*nx,h-1)))
        for j,e in enumerate(edges):
            if not ((used>>j)&1) and (returned & e)==e and (theta_mask & e)==e:
                edgesign.append((f'A{j}+',rec(phase,returned,used |(1<<j),h-1)))
        z=tuple(sorted(edgesign))
        k=intern.get(z)
        if k is None:
            k=len(intern)
            intern[z]=k
        return k
    for h in range(max_h+1): ids.append(rec(0,0,0,h))
    return ids, rec.cache_info().currsize


def independent_residual_fiber(m, edges, w):
    # S=W ∪ I, I⊆V\W; no newly activated hyperedge.
    residual=[e & ~w for e in edges if e & w != e]
    complement=((1<<m)-1)&~w
    count=0
    i=complement
    while True:
        if not any(i & x == x for x in residual):count+=1
        if i==0: break
        i=(i-1)&complement
    return count


def inspect_graph(m, edges, max_h):
    signature_by_theta=[]
    memo_nodes=0
    intern={():0}
    for theta in range(1<<m):
        s,k=all_words_signature(m,edges,theta,max_h,intern)
        signature_by_theta.append(s)
        memo_nodes+=k
    pairchecks=0
    for h in range(max_h+1):
        pred=[predicted_partition(t,edges,h) for t in range(1<<m)]
        for t in range(1<<m):
            for u in range(t+1,1<<m):
                pairchecks+=1
                if (signature_by_theta[t][h]==signature_by_theta[u][h])!=(pred[t]==pred[u]):
                    raise AssertionError({'failure':'language partition', 'm':m,'edges':edges,'h':h,'t':t,'u':u})
        sig_classes=len(set(signature_by_theta[t][h] for t in range(1<<m)))
        ws={canonical_support(t,eligible_edges_for_h(edges,h)) for t in range(1<<m)}
        if len(ws)!=sig_classes:raise AssertionError(('count',m,edges,h))
        for w in ws:
            fiber=sum(canonical_support(t,eligible_edges_for_h(edges,h))==w for t in range(1<<m))
            formula=independent_residual_fiber(m,eligible_edges_for_h(edges,h),w)
            if fiber!=formula:raise AssertionError(('fiber',m,edges,h,w,fiber,formula))
    return pairchecks,memo_nodes


def main():
    corpus=[]
    # Exhaust all triple-guard hypergraphs on four labeled sources (16 graphs).
    for k in range(1,5):
        all_e=edges_of_size(k, [3])
        for bits in range(1<<len(all_e)):
            corpus.append((k,[e for j,e in enumerate(all_e) if (bits>>j)&1], 'all-triad'))
    # All mixed pair+triple hypergraphs up to 3 vertices.
    all_e=edges_of_size(3,[2,3])
    for bits in range(1<<len(all_e)):
        corpus.append((3,[e for j,e in enumerate(all_e) if (bits>>j)&1], 'all-mixed-3'))
    # Representative five-vertex triple/mixed configurations.
    rng=random.Random(270019)
    e5=edges_of_size(5,[2,3,4])
    for k in range(8):
        if k==0: sel=edges_of_size(5,[3])
        elif k==1:sel=edges_of_size(5,[2,3])
        elif k==2:sel=edges_of_size(5,[4])
        elif k==3:sel=edges_of_size(5,[2])
        else:sel=[e for e in e5 if rng.random()<(.15+.1*k)]
        corpus.append((5,sel,'sample-mixed-5'))
    # Finite h for m≤4: test every horizon 0..8, m=5: 0..7.
    details=[]
    totalpairs=0; totalmemo=0
    for m,edges,tag in corpus:
        h=8 if m<=4 else 7
        pairs,memos=inspect_graph(m,edges,h)
        totalpairs+=pairs;totalmemo+=memos
        details.append({'m':m,'edges':[''.join(str(i) for i in range(m) if (e>>i)&1) for e in edges],
                        'tag':tag,'max_h':h,'pair_checks':pairs,'signature_nodes':memos})
    profiles=[]
    for m in range(3,9):
        es=edges_of_size(m,[3]); ws={canonical_support(s,es) for s in range(1<<m)}
        exact=1+sum(math.comb(m,j) for j in range(3,m+1))
        assert len(ws)==exact
        profiles.append({'m':m,'complete_triad_classes':exact,'min_bits':(exact-1).bit_length()})
    result={
        'schema':'X6_R27_BOOLEAN_BRC_EXACT_CHECK_V1',
        'status':'PASS',
        'hypothesis':'Declared independent signed two-Cell triadic lanes, one-use conjunctive guarded consumers, labels for all successful source/signed-Port events',
        'scope':'Exhaust all three-uniform hypergraphs on m=1..4, all mixed (2,3) hypergraphs on m=3; 8 representative mixed/arbitrary hypergraphs on m=5',
        'hypergraphs_checked':len(corpus),
        'language_partition_pair_checks':totalpairs,
        'memo_states_computed':totalmemo,
        'horizon':'0..8 (m<=4); 0..7 (m=5)',
        'profiles_complete_3_uniform':profiles,
        'graphs':details,
        'proof_outside_finite_scope':'Uses symbolic length-minimal witness and labeled bisimulation; computer test not a universal proof',
        'native_TRIADIC_CLOSURE_E_admission':'NOT_ESTABLISHED'
    }
    path=Path(__file__).with_name('x6_hyperguard_arity_brc_results_r27.json')
    path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps({k:result[k] for k in ('status','hypergraphs_checked','language_partition_pair_checks','memo_states_computed','profiles_complete_3_uniform')},indent=2))

if __name__=='__main__':main()
