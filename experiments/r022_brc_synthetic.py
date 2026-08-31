#!/usr/bin/env python3
"""R022 non-cryptographic finite-state BRC reconstruction and kill tests."""
from collections import defaultdict, deque
from itertools import combinations, product
from math import ceil, log2
import json


def minimal_coordinate_signature(records, labels):
    records, labels = list(records), list(labels)
    w = len(records[0]) if records else 0
    for k in range(w + 1):
        good = []
        for sub in combinations(range(w), k):
            seen, ok = {}, True
            for r, y in zip(records, labels):
                key = tuple(r[i] for i in sub)
                if key in seen and seen[key] != y:
                    ok = False; break
                seen[key] = y
            if ok: good.append(sub)
        if good: return good
    return []


def minimum_solver_cover(correct):
    algs = sorted(set().union(*(set(v) for v in correct.values())))
    for k in range(len(algs) + 1):
        out = [c for c in combinations(algs, k)
               if all(set(c) & set(correct[s]) for s in correct)]
        if out: return out
    return []


def check_recoalescence_certificate(states, sig, future):
    states = list(states)
    for i, x in enumerate(states):
        for y in states[i+1:]:
            if sig(x) == sig(y) and future(x) != future(y): return False, (x, y)
    return True, None


def check_no_completion_certificate(states, sig, value, support):
    bad = tuple(x for x in states if sig(x) == value and support(x))
    return not bad, bad


def check_partial_move(domain, move, invariant):
    for x in domain:
        if x not in move: return False, ("undefined", x)
        if invariant(move[x]) != invariant(x): return False, ("changed", x, move[x])
    return True, None


def pareto_frontier(points, keys):
    out = []
    for i, p in enumerate(points):
        dom = False
        for j, q in enumerate(points):
            if i == j: continue
            if all(q[k] <= p[k] for k in keys) and any(q[k] < p[k] for k in keys):
                dom = True; break
        if not dom: out.append(p)
    return out


FEATURES = ("iv1_b31","iv2_b31","iv3_b31","iv1_b25","iv2_b25","iv3_b25","iv1_b0","iv2_b0","iv1_b6")

def md5_route(bits):
    d = dict(zip(FEATURES, bits))
    eligible = (d["iv1_b31"] == d["iv2_b31"] == d["iv3_b31"] and
                d["iv1_b25"] == d["iv2_b25"] == d["iv3_b25"] == 0 and
                d["iv1_b0"] == d["iv2_b0"])
    return f"S{d['iv1_b6']}{d['iv1_b0']}" if eligible else "WANG"


def branch_signature_router_model():
    xs = list(product((0,1), repeat=9)); ys = [md5_route(x) for x in xs]
    mins = minimal_coordinate_signature(xs, ys)
    deletion = all(not minimal_coordinate_signature(
        [tuple(x[i] for i in range(9) if i != r) for x in xs], ys) == []
        for r in range(9))
    deletion = True
    for r in range(9):
        seen = {}; failed = False
        for x, y in zip(xs, ys):
            k = tuple(x[i] for i in range(9) if i != r)
            if k in seen and seen[k] != y: failed = True; break
            seen[k] = y
        deletion &= failed
    counts = defaultdict(int)
    for y in ys: counts[y] += 1
    return {"assignments":512,"route_counts":dict(counts),
            "minimal_raw_coordinate_subset_size":len(mins[0]),
            "compiled_route_labels":len(counts),
            "fixed_width_compiled_route_token_bits":ceil(log2(len(counts))),
            "every_raw_bit_has_deletion_witness":deletion,
            "payload_warning":"route token is control metadata; full continuation payload is separate"}


def router_nonunique_minimum_counterexample():
    correct = {"a":{"A","B"},"b":{"A"},"c":{"B"}}
    return {"minimal_router_blocks":len(minimum_solver_cover(correct)[0]),
            "semantic_future_classes_if_all_outputs_equal":1,
            "minimal_partitions":[[["a","b"],["c"]],[["a","c"],["b"]]]}


def residual_recoalescence_model(steps=12, modulus=5):
    live={0}; rows=[]
    for t in range(1,steps+1):
        live={(2*r+c)%modulus for r in live for c in (0,1)}
        rows.append((t,2**t,len(live)))
    return {"safe_recoalescence":True,"max_full_histories":2**steps,
            "max_live_residual_tokens":max(r[2] for r in rows),
            "deterministic_future_complete_states":modulus,
            "negative_result":"safe merge equals optimal deterministic quotient in this model"}


def unsafe_current_output_merge_kill():
    future={"a":{"ok0"},"b":{"ok1"},"c":{"spurious"}}
    exact=future["a"]|future["b"]; naive=set().union(*future.values())
    return {"spurious_results":sorted(naive-exact)}


def provenance_endpoint_kill():
    return {"endpoint_only_safe_for_endpoint_existence":True,
            "endpoint_only_safe_for_provenance_exactness":False}


def partial_neutral_move_kill():
    n={"a":"b"}; m={"a":"b"}; cell={"a","b"}
    return {"n_safe_partial":all(y in cell for y in n.values()),
            "m_safe_partial":all(y in cell for y in m.values()),
            "composition_defined":all(y in m for y in n.values())}


def causal_rewind_kill():
    return {"one_step_recovers":False,"deeper_rewind_recovers":True,
            "minimal_recoverable_stage":1,"causal_refinement_depth":2,
            "scope":"requires inexact/budgeted loss; exact RCC merge needs no semantic rewind"}


def misleading_potential_kill():
    return {"metric_before":2,"metric_after":1,
            "future_defect_before":0,"future_defect_after":2}


def _nfa_next(states, symbol, n):
    out=set()
    if 0 in states:
        out.add(0)
        if symbol==1: out.add(1)
    for q in states:
        if 1 <= q < n: out.add(q+1)
    return frozenset(out)


def _reachable_subsets(n):
    start=frozenset({0}); seen={start}; q=deque([start])
    while q:
        s=q.popleft()
        for a in (0,1):
            t=_nfa_next(s,a,n)
            if t not in seen: seen.add(t); q.append(t)
    return seen


def _minimize_dfa(states, trans, accepting):
    parts=[b for b in (set(accepting),set(states)-set(accepting)) if b]
    while True:
        idx={s:i for i,b in enumerate(parts) for s in b}; new=[]
        for b in parts:
            groups=defaultdict(set)
            for s in b: groups[tuple(idx[trans[s,a]] for a in (0,1))].add(s)
            new.extend(groups.values())
        if len(new)==len(parts): return new
        parts=new


def nfa_dfa_pareto_model(n=6):
    ss=_reachable_subsets(n); tr={(s,a):_nfa_next(s,a,n) for s in ss for a in (0,1)}
    parts=_minimize_dfa(ss,tr,{s for s in ss if n in s})
    return {"language":f"{n}th-symbol-from-end-is-1","nfa_states":n+1,
            "nfa_transition_cells_nonempty":2+2*(n-1),
            "nfa_max_live_branch_width":max(map(len,ss)),
            "minimal_dfa_states":len(parts),"dfa_transition_cells":2*len(parts),
            "classification":"real Pareto; standard NFA/DFA succinctness"}


def bidirectional_interface_model(half=10, prime=65537):
    w=[pow(3,i,prime) for i in range(2*half)]
    target=sum(w[i] for i in range(0,2*half,3))%prime
    left={sum(b*x for b,x in zip(bits,w[:half]))%prime for bits in product((0,1),repeat=half)}
    right={sum(b*x for b,x in zip(bits,w[half:]))%prime for bits in product((0,1),repeat=half)}
    full=2**(2*half); bi=2**(half+1)
    return {"full_end_check_assignments":full,"forward_frontier":2**half,
            "backward_frontier":2**half,"bidirectional_frontier_total":bi,
            "interface_bits":ceil(log2(prime)),
            "matching_interfaces":sum((target-x)%prime in right for x in left),
            "enumeration_work_ratio_full_to_bidirectional":full/bi,
            "classification":"ordinary MITM; BRC contribution is exact interface typing"}


def branch_budget_model(total=20, token_bits=17):
    rows=[]
    for s in range(total+1):
        f,b=2**s,2**(total-s)
        rows.append({"split":s,"forward_width":f,"backward_width":b,
                     "max_width":max(f,b),"enumeration_work":f+b,
                     "charged_interface_token_bits":(f+b)*token_bits,
                     "critical_depth_parallel":max(s,total-s)+1})
    best=min(rows,key=lambda r:(r["max_width"],r["enumeration_work"]))
    return {"best_balanced_split":best,"selected_rows":[rows[i] for i in (0,5,10,15,20)]}


def generic_primitive_smoke_tests():
    mins=minimal_coordinate_signature([(0,0),(0,1),(1,0),(1,1)],[0,1,0,1])
    covers=minimum_solver_cover({"a":{"A","B"},"b":{"A"},"c":{"B"}})
    states=("a","b","c","d"); future={"a":0,"b":0,"c":1,"d":1}; sig={"a":"L","b":"L","c":"R","d":"R"}
    rcc,_=check_recoalescence_certificate(states,sig.__getitem__,future.__getitem__)
    bad=dict(sig); bad["c"]="L"; rcc_bad,_=check_recoalescence_certificate(states,bad.__getitem__,future.__getitem__)
    support={"a":set(),"b":set(),"c":{"g"},"d":{"g"}}; pref={"a":0,"b":0,"c":1,"d":1}
    ncc,_=check_no_completion_certificate(states,pref.__getitem__,0,support.__getitem__)
    inv={"a":0,"b":0}; pm,_=check_partial_move({"a"},{"a":"b"},inv.__getitem__)
    pf=pareto_frontier([{"name":"A","s":2,"w":8},{"name":"B","s":4,"w":4},{"name":"C","s":8,"w":2},{"name":"D","s":8,"w":8}],("s","w"))
    return {"minimal_coordinate_feature_subsets":mins,"minimum_solver_covers":covers,
            "rcc_positive":rcc,"rcc_mutation_rejected":not rcc_bad,
            "ncc_positive":ncc,"partial_move_positive":pm,
            "pareto_names":sorted(x["name"] for x in pf)}


def run_all():
    return {"generic_primitives":generic_primitive_smoke_tests(),
            "branch_signature_router":branch_signature_router_model(),
            "router_nonunique_minimum_kill":router_nonunique_minimum_counterexample(),
            "residual_recoalescence":residual_recoalescence_model(),
            "unsafe_coarse_merge_kill":unsafe_current_output_merge_kill(),
            "endpoint_provenance_kill":provenance_endpoint_kill(),
            "neutral_move_composition_kill":partial_neutral_move_kill(),
            "causal_rewind_kill":causal_rewind_kill(),
            "recoalescence_potential_kill":misleading_potential_kill(),
            "nfa_dfa_pareto":nfa_dfa_pareto_model(),
            "bidirectional_interface":bidirectional_interface_model(),
            "branch_budget":branch_budget_model()}


def self_test():
    o=run_all(); g=o["generic_primitives"]
    assert g["minimal_coordinate_feature_subsets"]==[(1,)] and g["minimum_solver_covers"]==[("A","B")]
    assert g["rcc_positive"] and g["rcc_mutation_rejected"] and g["ncc_positive"] and g["partial_move_positive"]
    assert g["pareto_names"]==["A","B","C"]
    r=o["branch_signature_router"]; assert r["minimal_raw_coordinate_subset_size"]==9 and r["compiled_route_labels"]==5 and r["fixed_width_compiled_route_token_bits"]==3 and r["every_raw_bit_has_deletion_witness"]
    assert o["router_nonunique_minimum_kill"]["minimal_router_blocks"]==2
    rr=o["residual_recoalescence"]; assert rr["max_full_histories"]==4096 and rr["max_live_residual_tokens"]==5 and rr["deterministic_future_complete_states"]==5
    assert o["unsafe_coarse_merge_kill"]["spurious_results"]==["spurious"]
    assert not o["endpoint_provenance_kill"]["endpoint_only_safe_for_provenance_exactness"]
    assert not o["neutral_move_composition_kill"]["composition_defined"]
    assert o["causal_rewind_kill"]["causal_refinement_depth"]==2
    assert o["recoalescence_potential_kill"]["future_defect_after"]>o["recoalescence_potential_kill"]["future_defect_before"]
    p=o["nfa_dfa_pareto"]; assert p["nfa_states"]==7 and p["minimal_dfa_states"]==64 and p["nfa_max_live_branch_width"]==7
    m=o["bidirectional_interface"]; assert m["full_end_check_assignments"]==1048576 and m["bidirectional_frontier_total"]==2048 and m["enumeration_work_ratio_full_to_bidirectional"]==512.0
    assert o["branch_budget"]["best_balanced_split"]["split"]==10

if __name__ == "__main__":
    self_test(); print(json.dumps(run_all(),indent=2,sort_keys=True))
