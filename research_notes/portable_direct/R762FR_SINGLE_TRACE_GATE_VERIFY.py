#!/usr/bin/env python3
"""R762FR fail-stop single-trace gate observation; stdlib, exact integers."""
from collections import Counter
from itertools import product, permutations
from pathlib import Path
import json

def outcome(state, order):
    row=list(state)
    for j,edge in enumerate(order,1):
        if row[edge]==1:
            return j  # BLOCK ends the entire trace
        row[edge]=2-row[edge]  # H0 <-> H2, enabled stays enabled
    return 0  # NONE

def check(m):
    states=list(product((0,1,2),repeat=m))
    assert len(states)==3**m
    policies=0
    checks=0
    for t in range(m+1):
        expected={j:2**(j-1)*3**(m-j) for j in range(1,t+1)}
        expected[0]=2**t*3**(m-t)
        for order in permutations(range(m),t):
            counts=Counter(outcome(state,order) for state in states)
            assert dict(counts)==expected
            assert len(counts)==t+1
            for state in states:
                predicted=next((j for j,e in enumerate(order,1) if state[e]==1),0)
                assert outcome(state,order)==predicted
                checks+=1
            policies+=1
    return {
        "m":m,"k":2*m+1,"histories":3**m,"orders_tested":policies,
        "history_policy_checks":checks,"maximum_one_trace_classes":m+1,
        "one_trace_bits":m.bit_length(),"resettable_probe_bits":m,
        "full_history_bits":(3**m-1).bit_length(),
        "full_horizon_class_fibers":{
            **{str(j):2**(j-1)*3**(m-j) for j in range(1,m+1)},
            "no_block":2**m
        }
    }

if __name__=="__main__":
    rows=[check(m) for m in range(1,7)]
    result={
        "schema":"R762FR_FAIL_STOP_SINGLE_TRACE_V1","status":"PASS",
        "semantic_assumptions":"one initial state, success changes H0/H2 only, first BLOCK terminates trace, deterministic known-edge policy, reset prohibited",
        "coverage":"m=1..6, all nonrepeating fixed-order policies, lengths 0..m, all 3^m states; no floating point",
        "rows":rows,"independent_review":"NOT_REVIEWED"
    }
    Path(__file__).with_name("R762FR_SINGLE_TRACE_GATE_EVIDENCE.json").write_text(
        json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))
