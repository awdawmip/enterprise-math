#!/usr/bin/env python3
"""R284EC: exact global bit-query decision-tree optimum for the R284EA
full 16-bit quotient-exception predicate. Independent of Port determinant code.
All original source inputs retained; the ignored B3 bit is provably irrelevant.
"""
from functools import lru_cache
from itertools import product
from hashlib import sha256
from pathlib import Path
import json

W = (13, 6, 28, 25, 11, 12, 26, 17, 6)
THRESHOLD = 77
ALL = (1 << 9) - 1
ORDER = (2, 6, 3, 7, 0, 5, 4, 1, 8)


def bounds(z, o):
    free = ALL ^ (z | o)
    lo = sum(W[j] for j in range(9) if o & (1 << j))
    hi = lo + sum(W[j] for j in range(9) if free & (1 << j))
    return free, lo, hi


@lru_cache(None)
def optimal(core_remaining, zero, one):
    """Lexicographic (min total queries, then worst depth, then action)."""
    free, lo, hi = bounds(zero, one)
    if hi < THRESHOLD or (core_remaining == 0 and lo >= THRESHOLD):
        return 0, 0, 'stop'
    n = core_remaining + free.bit_count()
    choices = []
    if core_remaining:
        passed = optimal(core_remaining - 1, zero, one)
        # A zero core bit is immediately terminal; only the one branch recurses.
        choices.append((2**n + passed[0], 1 + passed[1], 'core'))
    for j in range(9):
        if free & (1 << j):
            a = optimal(core_remaining, zero | (1 << j), one)
            b = optimal(core_remaining, zero, one | (1 << j))
            choices.append((2**n + a[0] + b[0], 1 + max(a[1], b[1]), j))
    return min(choices, key=lambda t: (t[0], t[1], -1 if t[2]=='core' else t[2]))


@lru_cache(None)
def minimax(core_remaining, zero, one):
    free, lo, hi = bounds(zero, one)
    if hi < THRESHOLD or (core_remaining == 0 and lo >= THRESHOLD):
        return 0, 0, 'stop'
    n = core_remaining + free.bit_count()
    choices = []
    if core_remaining:
        a = minimax(core_remaining - 1, zero, one)
        choices.append((1 + a[0], 2**n + a[1], 'core'))
    for j in range(9):
        if free & (1 << j):
            a = minimax(core_remaining, zero | (1 << j), one)
            b = minimax(core_remaining, zero, one | (1 << j))
            choices.append((1 + max(a[0], b[0]), 2**n + a[1] + b[1], j))
    return min(choices, key=lambda t: (t[0], t[1], -1 if t[2]=='core' else t[2]))


def fixed_threshold_depth(bits):
    z = o = depth = 0
    while True:
        free, lo, hi = bounds(z, o)
        if lo >= THRESHOLD or hi < THRESHOLD:
            assert (lo >= THRESHOLD) == (sum(w*b for w,b in zip(W,bits)) >= THRESHOLD)
            return depth
        j = next(j for j in ORDER if free & (1 << j))
        if bits[j]: o |= 1 << j
        else: z |= 1 << j
        depth += 1


def main():
    # All 7*3^9 DP states; two recurrences, including unreachable subcubes.
    table=[]
    for k in range(7):
        for z in range(512):
            for o in range(512):
                if z & o: continue
                a,b = optimal(k,z,o),minimax(k,z,o)
                # Store unambiguous action code 9=core, -1=terminal.
                qa = 9 if a[2]=='core' else (-1 if a[2]=='stop' else a[2])
                qb = 9 if b[2]=='core' else (-1 if b[2]=='stop' else b[2])
                table.append((k,z,o,a[0],a[1],qa,b[0],b[1],qb))
    assert len(table)==7*3**9==137781
    root, worst=optimal(6,0,0),minimax(6,0,0)
    assert root==(67246,15,'core')
    assert worst==(15,67246,'core')
    assert [optimal(k,0,0)[0] for k in range(7)] == [2734,3758,5806,9902,18094,34478,67246]
    hist={};total=0; yes=0
    for core in product((0,1),repeat=6):
        core_depth=next((j+1 for j,v in enumerate(core) if v==0),6)
        passes=all(core)
        for bits in product((0,1),repeat=9):
            f=passes and sum(w*b for w,b in zip(W,bits))>=THRESHOLD
            yes+=2*f   # both B3 values
            depth=core_depth+(fixed_threshold_depth(bits) if passes else 0)
            hist[depth]=hist.get(depth,0)+2
            total+=depth*2
    assert total==134492 and sum(hist.values())==65536
    assert yes==446 and max(hist)==15 and hist[15]==84
    result={
      'schema':'R284EC_FULL_PORT_EXCEPTION_GUARD_GLOBAL_BIT_PROBE_OPTIMUM_V1',
      'date':'2026-11-22',
      'scientific_status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
      'frozen_source_commit':'acba2d8667903434aaa2a10720f43637fcc2421b',
      'immediate_predecessors':['R284EA','R284EB'],
      'bit_count_relevant':15,
      'irrelevant_original_upper_bit':'B3',
      'cost_model':'Deterministic adaptive original-source-bit queries; independent uniform inputs; 1 unit each; exact Boolean computation free',
      'enumerated_dp_states':len(table),
      'dp_table_sha256':sha256(json.dumps(table,separators=(',',':')).encode()).hexdigest(),
      'root_optimal_total_queries_for_32768_relevant_inputs':root[0],
      'root_minimax_depth':worst[0],
      'optimal_total_queries_all_65536':total,
      'optimal_mean_queries':{'numerator':33623,'denominator':16384},
      'optimal_policy':'read six core bits until first zero, then U,B0,G,B1,Y,R,H,Z,B2 with threshold early stopping',
      'uniform_inputs_checked':65536,
      'positive_exception_states':yes,
      'optimal_fixed_policy_histogram':{str(k):v for k,v in sorted(hist.items())},
      'root_total_queries_for_k_0_through_6':[optimal(k,0,0)[0] for k in range(7)],
      'full_state_original_input_retained':True,
      'independent_review':'NOT_REVIEWED'
    }
    return result


if __name__ == '__main__':
    c=main()
    out=Path(__file__).with_name('R284EC_full_guard_optimality_certificate.json')
    out.write_text(json.dumps(c,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(c,indent=2,ensure_ascii=False))
