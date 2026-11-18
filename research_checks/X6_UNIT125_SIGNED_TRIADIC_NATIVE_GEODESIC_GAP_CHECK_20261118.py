#!/usr/bin/env python3
"""Independent exact source-typed census for signed three-distinct-axis macro blocks.
Original consumer: experiments/x6_triadic_decomposition_brc_v2_20260906/
check_triadic_decomposition_brc.py (Git blob 5d0f2cb88a0d4e437b5025e9050e3044f7831cd4).
P000 signed X6 source freeze: 59538f585d037d09ef687b28715c4bc1a3f9fe03.
Research unit: X6 Unit125; independent arithmetic, not a native benchmark.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial, prod
import hashlib
import json

AXES=range(6)
TRIPLES=tuple(combinations(AXES,3))
EVENTS=tuple(tuple((axis,sgn) for axis,sgn in zip(triple,signs))
    for triple in TRIPLES for signs in product((-1,1),repeat=3))

def need(condition,detail):
    if not condition:
        raise ArithmeticError(str(detail))

def sigma(ev):
    out=[0]*12
    for i,s in ev:out[2*i+(0 if s==1 else 1)]+=1
    return tuple(out)

@lru_cache(None)
def macro_count(D):
    D=tuple(D)
    if sum(D)%3:return 0
    state={(0,)*6:1}
    for _ in range(sum(D)//3):
        nxt={}
        for v,n in state.items():
            for triple in TRIPLES:
                vv=list(v)
                for j in triple:vv[j]+=1
                if all(vv[i]<=D[i] for i in AXES):
                    vv=tuple(vv);nxt[vv]=nxt.get(vv,0)+n
        state=nxt
    return state.get(D,0)

def signed_macro_formula(d):
    D=tuple(d[2*i]+d[2*i+1] for i in AXES)
    return macro_count(D)*prod(comb(D[i],d[2*i]) for i in AXES)

def native_geometry(d):
    m=sum(d)//3
    D=tuple(d[2*i]+d[2*i+1] for i in AXES)
    z=tuple(d[2*i]-d[2*i+1] for i in AXES)
    C=sum(min(d[2*i],d[2*i+1]) for i in AXES)
    native_length=sum(abs(x) for x in z)
    need(3*m-native_length==2*C,(d,m,C,native_length))
    B=factorial(native_length)//prod(factorial(abs(x)) for x in z)
    return m,D,z,C,native_length,B

def finite_census():
    need(len(TRIPLES)==20 and len(EVENTS)==160,'event alphabet size')
    for ev in EVENTS:need(signed_macro_formula(sigma(ev))==1,ev)
    hist=Counter()
    pairs_by_d=Counter()
    for e in EVENTS:
        a=sigma(e)
        for f in EVENTS:
            b=sigma(f)
            pairs_by_d[tuple(x+y for x,y in zip(a,b))]+=1
    # This is a complete census of 160^2 actually enumerated ordered macro-event histories.
    need(sum(pairs_by_d.values())==25600,'original two-event history count')
    exhaustive_native_shortest=0
    nongeodesic_words=0
    inflation_total=0
    coherent_words=0
    total_macro_types=0
    min_gap=None
    max_gap=None
    first_cancellation={}
    maximal_ratio=None
    length_deficit_counts=Counter()
    smallest_cancellation_weight=None
    for d,n in sorted(pairs_by_d.items()):
        need(n==signed_macro_formula(d),('formula differs',d,n))
        m,D,z,C,L,B=native_geometry(d)
        need(m==2,(d,m))
        W=(factorial(3)**m)*n
        deficit=3*m-L
        length_deficit_counts[deficit]+=1
        hist[C]+=1
        total_macro_types+=n
        if C==0:
            need(W<=B,(d,W,B))
            coherent_words+=W
            if W==B:exhaustive_native_shortest+=1
        else:
            need(deficit>=2,(d,deficit))
            nongeodesic_words+=W
            if smallest_cancellation_weight is None or W<smallest_cancellation_weight:
                smallest_cancellation_weight=W
            if str(C) not in first_cancellation:
                first_cancellation[str(C)]={'d':list(d),'z':list(z),'macro_count':n,'block_words':W,'native_length':L,'native_B':B,'length_excess':deficit}
            if maximal_ratio is None or W*maximal_ratio['native_B']>maximal_ratio['block_words']*B:
                maximal_ratio={'d':list(d),'z':list(z),'block_words':W,'native_B':B,'native_length':L,'C':C}
        min_gap=deficit if min_gap is None else min(min_gap,deficit)
        max_gap=deficit if max_gap is None else max(max_gap,deficit)
        inflation_total+=W
    need(inflation_total==25600*36,(inflation_total,25600*36))
    need(coherent_words+nongeodesic_words==inflation_total,'word partition')
    # Exact 2k-event all-cancellation family, every step on each of axes 0,1,2:
    family=[]
    for k in range(1,5):
        m=2*k
        d=tuple(([k,k] if i<3 else [0,0]) for i in AXES)
        d=tuple(x for pair in d for x in pair)
        M=signed_macro_formula(d)
        need(M==comb(2*k,k)**3,('family macro formula',k,M))
        W=(6**m)*M
        length=0
        family.append({'k':k,'macro_events':m,'macro_count':M,'block_words':W,
                       'native_endpoint':[0]*6,'native_shortest_length':length,'native_shortest_BRC':1,
                       'length_excess':3*m})
    output={
        'schema':'X6_UNIT125_SIGNED_TRIADIC_GEODESIC_GAP_CERTIFICATE_V1',
        'source_consumer':'experiments/x6_triadic_decomposition_brc_v2_20260906/check_triadic_decomposition_brc.py',
        'source_blob':'5d0f2cb88a0d4e437b5025e9050e3044f7831cd4',
        'frozen_science':'59538f585d037d09ef687b28715c4bc1a3f9fe03',
        'alphabet':{'unsigned_triads':len(TRIPLES),'signed_triads':len(EVENTS),'two_event_histories':25600},
        'two_event_census':{
          'distinct_signed_incidence_vectors':len(pairs_by_d),
          'C_histogram_by_signed_incidence':{str(k):hist[k] for k in sorted(hist)},
          'length_excess_histogram_by_signed_incidence':{str(k):length_deficit_counts[k] for k in sorted(length_deficit_counts)},
          'signed_macro_event_histories':total_macro_types,
          'free_block_words':inflation_total,
          'geodesic_block_words':coherent_words,
          'nongeodesic_block_words':nongeodesic_words,
          'coherent_incidence_vectors_where_all_native_shortest_words_covered':exhaustive_native_shortest,
          'first_cancellation_witnesses_by_C':first_cancellation,
          'maximal_W_over_native_B_in_two_event_census':maximal_ratio,
          'smallest_positive_W_in_nongeodesic_class':smallest_cancellation_weight,
          'min_length_excess':min_gap,'max_length_excess':max_gap},
        'all_cancellation_family_k_1_to_4':family,
        'theorem':'For any feasible d with 3m signed primitive steps and C=sum_i min(d_i+,d_i-), every free triadic-block word has native length excess exactly 2C; geodesic iff C=0. At C=0 W=6^m U(D) <=B(z), with equality iff max D_i<=1. At C>0 none of W words is native shortest, and W/B(z) has no universal finite bound.',
        'execution_scope':'Independent exact Python source-interface arithmetic; not original signed_brc or R063 six-file benchmark execution',
        'author_status':'UNREVIEWED_NOT_ADMITTED',
    }
    return output

if __name__=='__main__':
    result=finite_census()
    raw=json.dumps(result,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n'
    print(raw,end='')
