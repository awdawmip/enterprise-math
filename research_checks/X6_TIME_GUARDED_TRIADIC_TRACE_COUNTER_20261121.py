#!/usr/bin/env python3
"""Exact integers for conditional disjoint-source guarded triadic event model."""
from math import comb, factorial
from collections import defaultdict
import json

def coefficients(m):
    dp={(-1,)*m:1}
    configs=[1]; traces=[1]
    for k in range(m):
        nx=defaultdict(int)
        for state,ways in dp.items():
            for i,val in enumerate(state):
                if val!=-1: continue
                for port in range(3):
                    new=list(state);new[i]=port
                    nx[tuple(new)]+=ways
        dp=dict(nx)
        c=len(dp);h=sum(dp.values())
        assert c==comb(m,k+1)*3**(k+1)
        assert h==c*factorial(k+1)
        assert set(dp.values())=={factorial(k+1)}
        configs.append(c);traces.append(h)
    assert sum(configs)==4**m
    total=sum(traces)
    return {"m":m,"config_counts":configs,"trace_counts":traces,
            "total_configs":sum(configs),"total_traces":total,
            "future_state_classes":2**m,"future_bits":m,
            "current_port_classes":4**m,"port_bits":2*m,
            "history_bits":(total-1).bit_length()}

def brute(m):
    counts=[0]*(m+1)
    terminal=defaultdict(int)
    def visit(state,k):
        counts[k]+=1
        terminal[state]+=1
        for i,x in enumerate(state):
            if x==-1:
                for port in range(3):
                    u=list(state);u[i]=port
                    visit(tuple(u),k+1)
    visit((-1,)*m,0)
    predicted=[comb(m,k)*3**k*factorial(k) for k in range(m+1)]
    assert counts==predicted
    for state,ways in terminal.items():
        k=sum(x!=-1 for x in state)
        assert ways==factorial(k)
    assert len(terminal)==4**m
    states=list(terminal)
    signatures={tuple((i,port) for i in range(m) for port in range(3)
                      if st[i]==-1) for st in states}
    assert len(signatures)==2**m
    return {"m":m,"enumerated_ordered_prefixes":sum(counts),
            "distinct_configurations":len(terminal),
            "future_signatures":len(signatures)}

def main():
    rows=[coefficients(m) for m in range(1,9)]
    exp=[brute(m) for m in range(1,6)]
    seq1=((0,0),(1,1));seq2=((1,1),(0,0))
    def run(seq):
        q=[-1,-1]
        for i,p in seq:
            assert q[i]==-1
            q[i]=p
        return tuple(q)
    assert run(seq1)==run(seq2)==(0,1)
    out={"schema":"X6_TIME_DISJOINT_GUARDED_SOURCE_TRACE_CERT_V1",
         "model":"m disjoint independent one-shot sources, 3 labeled ports/source; q_i=-1 unused or 0,1,2 chosen port; no physical admissibility claim",
         "arithmetic":"exact Python integers; no floating-point tests",
         "formulae":{"configuration_layer":"binomial(m,k)*3^k",
                     "ordered_prefix_layer":"binomial(m,k)*3^k*k!",
                     "configuration_total":"4^m",
                     "future_equivalence_classes":"2^m",
                     "history_classes":"sum_{k=0}^m binomial(m,k)*3^k*k!"},
         "dp_rows":rows,"independent_DFS_rows":exp,
         "m2_witness":{"trace_A":seq1,"trace_B":seq2,
                       "same_configuration":[0,1],"different_order":True},
         "mismatch_count":0}
    print(json.dumps(out,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
