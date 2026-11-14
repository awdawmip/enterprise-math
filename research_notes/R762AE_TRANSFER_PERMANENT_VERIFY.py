#!/usr/bin/env python3
"""R762AE: exact source-blind chronological TRANSFER-fiber census.
Python >=3.8, standard library only. No randomness or floating point.
Physical labeled-token enumeration and binary-permanent DP are independent.
"""
import json
import math
from collections import defaultdict, Counter
from functools import lru_cache
from pathlib import Path

def enumerate_physical(n):
    obs = defaultdict(set)
    def rec(entered, departed, hub, trace, dest):
        if departed.bit_count() == n:
            assert not hub and entered.bit_count() == n
            assert sorted(dest) == list(range(n))
            obs[trace].add(tuple(dest))
            return
        if len(hub) < 2:
            for i in range(n):
                if not (entered & (1 << i)):
                    rec(entered | (1 << i), departed, hub + (i,),
                        trace + (("I",i),), dest)
        for p in range(n):
            if (entered & (1 << p)) and not (departed & (1 << p)):
                for source in hub:
                    if source != p:
                        nd = list(dest)
                        assert nd[source] == -1
                        nd[source] = p
                        rec(entered, departed | (1 << p),
                            tuple(x for x in hub if x != source),
                            trace + (("O",p),), tuple(nd))
    rec(0, 0, (), (), (-1,)*n)
    return obs

def temporal_permanent(trace,n):
    ins = {i:t for t,(kind,i) in enumerate(trace) if kind == "I"}
    outs = {i:t for t,(kind,i) in enumerate(trace) if kind == "O"}
    assert len(ins) == len(outs) == n
    mat = [[i!=j and ins[i]<outs[j] for j in range(n)]
           for i in range(n)]
    @lru_cache(None)
    def dp(i,mask):
        if i==n:
            return int(mask==(1<<n)-1)
        return sum(dp(i+1,mask | (1<<j))
                   for j in range(n) if mat[i][j] and not mask & (1<<j))
    return dp(0,0)

def canonical_trace(n):
    assert n>=2
    return (("I",0),("I",1),("O",0)) + tuple(
        step for i in range(2,n)
        for step in (("I",i),("O",i-1))
    ) + (("O",n-1),)

def fib(k):
    a,b=0,1
    for _ in range(k):
        a,b=b,a+b
    return a

def main():
    census,examples={},{}
    for n in range(2,7):
        obs=enumerate_physical(n)
        hist=Counter(map(len,obs.values()))
        for trace,maps in obs.items():
            assert len(trace)==2*n
            assert temporal_permanent(trace,n)==len(maps)
        total=sum(k*v for k,v in hist.items())
        expected=math.factorial(n)*2**(n-1)*fib(n-1)
        assert total==expected
        assert len(obs[canonical_trace(n)])==temporal_permanent(canonical_trace(n),n)==fib(n-1)
        census[str(n)]={
            "number_of_source_blind_transcripts":len(obs),
            "transcript_fiber_size_histogram":{str(k):hist[k] for k in sorted(hist)},
            "total_labelled_shortest_histories":total,
            "R762AD_mass":expected,
            "maximum_observed_fiber":max(hist),
            "canonical_fiber":fib(n-1)
        }
        maxf=max(hist)
        witness=next(t for t,v in obs.items() if len(v)==maxf)
        examples[str(n)]={
            "transcript":[kind+str(p) for kind,p in witness],
            "source_to_destination_maps":[list(x) for x in sorted(obs[witness])]
        }
    canonical={}
    for n in range(2,16):
        x=temporal_permanent(canonical_trace(n),n)
        assert x==fib(n-1)
        canonical[str(n)]=x
    evidence={
        "schema":"R762AE_SOURCE_BLIND_TRANSFER_FIBERS_V1",
        "scope":"conditional_two_slot_star_shortest_transfers_only",
        "algorithm":"independent_labeled_physical_DFS_and_binary_permanent_DP",
        "exactness":"integer_only_exhaustive_n_2_to_6; canonical_n_2_to_15",
        "claims":{
            "general_exact_fiber":"per(M_tau), M_ij=[i!=j and time(I_i)<time(O_j)]",
            "canonical_schedule_exact_fiber":"F_(n-1) for n>=2",
            "repair_bits_per_transcript":"ceil(log2(per(M_tau))) for nonempty fiber",
            "worst_case_general_max":"NOT_PROVED; n<=6 finite census only"
        },
        "census":census,
        "canonical_fibonacci_checks":canonical,
        "representative_maximal_fibers":examples,
        "provenance":{
            "task_id":"RS-X6-TRIADIC-CLOSURE-DYNAMICS",
            "publication_id":"TP2-8B7E13C5904A2D6F1142",
            "frozen_science_commit":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
            "parents":["R762AC","R762AD"],
            "status":"AUTHOR_SIDE_NOT_REVIEWED_NOT_NATIVE_ADMITTED"
        }
    }
    output=Path(__file__).with_name("R762AE_TRANSFER_PERMANENT_EVIDENCE.json")
    output.write_text(json.dumps(evidence,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"verified":True,"census":census,"canonical":canonical},indent=2))

if __name__=="__main__":
    main()
