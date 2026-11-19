#!/usr/bin/env python3
"""Exact native odd-core comparison. Python 3.10+. No precomputed modular order input."""
import argparse
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
from itertools import product
from math import lcm
import json
from pathlib import Path

HELPER_HASH = "b79a92b28b0528e7e8a3b026c9716e9379f1ef21f891ad8f4db36f6a384dc62e"
FIXTURES = (21, 35, 65, 33, 43)
A, T = 2, 4
NU = (1, 3, 5, 7)


def load_helper(path):
    if sha256(path.read_bytes()).hexdigest() != HELPER_HASH:
        raise ValueError("wave 18 native adapters differ from the specified revision")
    spec = importlib.util.spec_from_file_location("prior_defect", path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    return helper


def tree(p, depth):
    frontier = {(): p.initial()}
    levels = [frontier]
    for _ in range(depth):
        following = {}
        for h, (state, den) in frontier.items():
            plan = p.branch_plan(state, den, h)
            for b, mass in enumerate(plan.masses):
                if mass:
                    following[h+(b,)] = p.materialize(plan,b)
        frontier = following
        levels.append(frontier)
    return levels


def normrow(v):
    return sum(x*x for x in v.values())


def normrows(rows):
    return sum(map(normrow,rows.values()))


def weighted(op, vec, scale):
    return {k:op.obs("common_scale", ((x,scale),)) for k,x in vec.items() if x and scale}


def discover(p, helper, calls):
    L = 1 << T
    queries = []
    verified = []
    def probe(n, purpose):
        before = len(calls)
        accepted, steps = helper.certify(p,T,n)
        queries.append(dict(R=n, purpose=purpose, modular_columns=steps, source_calls=len(calls)-before,
                            outcome=accepted))
        return accepted
    for n in sorted({v*2**k for v in NU for k in range(T) if v*2**k < L}):
        if probe(n,"fixed-schedule"):
            verified.append(n)
    if not verified:
        return queries, verified, None
    # The largest verified value is a documented deterministic choice, and may be nonminimal.
    current = max(verified)
    while current % 2 == 0:
        if not probe(current//2,"strip-extra-twos"):
            break
        current //= 2
    g = current & -current
    return queries, verified, g


def charge(p, calls_used):
    return {"original_modular_arithmetic_calls":calls_used, "selected_child":dict(p.selected_metrics),
            "column_tables":[z.report_metrics() for z in p.lazy_factory.tables.values()]}


def record_kernel_cost(counters, peaks, label, metrics):
    for key in ("kernel_calls","expression_requests","unique_graphs_and_use_record_bytes"):
        counters[label+"_"+key] += metrics[key]
    for key in ("peak_numeric_bits","peak_graph_states","peak_graph_edges","peak_single_dense_graph_slots"):
        peaks[label+"_"+key] = max(peaks[label+"_"+key],metrics[key])


def fixture(N, lib, api):
    cls, _, calls, bank, rd, _ = api
    start = len(calls)
    sim = cls(N,A,T,bank,61)
    full_admit = len(calls)-start
    full_probes, full_returns, full_g = discover(sim,lib,calls)
    start = len(calls)
    levels = tree(sim,T)
    full_cost = charge(sim,len(calls)-start)
    start = len(calls)
    short = cls(N,A,T,bank,61)
    short_admit = len(calls)-start
    probes, returns, g = discover(short,lib,calls)
    assert ([(r["R"],r["outcome"],r["modular_columns"]) for r in full_probes],full_returns,full_g)==(
        [(r["R"],r["outcome"],r["modular_columns"]) for r in probes],returns,g)
    assert g and 1 < g < 1<<T
    j = g.bit_length()-1
    mid = T-j
    start = len(calls)
    reduced = tree(short,mid)[-1]
    reduced_cost = charge(short,len(calls)-start)
    # Only terminal (bit word, working label) masses. No feedback-word product is needed.
    all_certified = {r["R"]:r["outcome"] for r in probes}
    minimal = {R:all(all_certified.get(R//p) is False for p in range(2,R+1)
                       if R%p==0 and all(p%q for q in range(2,p))) for R in returns}
    shifts = {}
    classmap = {}
    lookup_count = 0
    begin_relabel = len(calls)
    for h,(state,den) in reduced.items():
        prefix = lib.raw_field(state,den)
        assert prefix == lib.raw_field(*levels[mid][h])
        qs = {}
        for w,row in prefix.items():
            if w not in shifts:
                labels = [w]
                for _ in range(g-1):
                    labels.append(short.tables[-1][labels[-1]])
                    lookup_count += 1
                shifts[w] = labels
            for label in shifts[w]:
                assert label not in qs
                qs[label] = normrow(row)/g**2
        for b in product((0,1),repeat=j):
            rows = lib.raw_field(*levels[T][h+b])
            assert qs == {label:normrow(v) for label,v in rows.items()}
            classmap[h+b] = qs
    relabel_brc_calls = len(calls)-begin_relabel
    scope_controls = {}
    if N == 35:
        raw = []
        for b in product((0,1),repeat=2):
            rows = lib.raw_field(*levels[T][(0,0)+b])
            mass = normrows(rows)
            raw.append({"suffix":"".join(map(str,b)), "mass":str(mass),
                        "conditional_internal_mode_zero":str(sum(v.get(0,0)**2 for v in rows.values())/mass),
                        "joint_work_two":str(normrow(rows[2])),
                        "mode_zero_given_history_and_work_two":str(rows[2].get(0,0)**2/normrow(rows[2]))})
        assert [r["conditional_internal_mode_zero"] for r in raw] == ["1","1","1/2","1/2"]
        scope_controls["native_internal_readout_after_prefix_00"] = raw
    word_cases = []
    counts = Counter()
    costs = Counter()
    peaks = Counter()
    for h,(base,den) in sorted(reduced.items()):
        cfield = lib.raw_field(base,den)
        op = rd.Ops()
        prefixword = lib.bind_word(rd,op,short,h)
        record_kernel_cost(costs,peaks,"core_word_binding",lib.cost(op))
        core_labels = lib.labels_for_validation(short,mid)
        cz = core_labels[:-1]
        calpha, qfield = lib.coeffs_and_rows(op,rd,prefixword,core_labels)
        assert qfield == cfield
        core_rows = {}
        for R in returns:
            D = R//g
            cset, ca, cb = lib.partition(1<<mid,D)
            co = rd.Ops()
            cj = rd.carry(co,prefixword,D,rd.eye())
            delta = 2*((1<<mid)-D+cj)
            assert delta == sum(normrow(op.vadd(calpha[i],calpha[i+D])) for i in range((1<<mid)-D))
            tw = lib.scale(op,lib.combine(op,*({cz[k]:calpha[k]} for k in range(ca,ca+cb))),F(1,1<<mid))
            pmax = max(Counter(cz[k] for k in cset).values(), default=0)
            mu = normrows(tw)
            witness = next((i for i in range(len(cz)-D) if op.vadd(calpha[i],calpha[i+D])), None)
            if delta:
                loc = rd.locate_defect(co,prefixword,D)
                assert loc and loc["f"] == witness
            else:
                assert witness is None
            accepted = bool(mu and pmax*delta <= F(1,4)*(1<<mid)**2*mu)
            core_rows[R]=(ca,cb,cj,delta,tw,mu,pmax,witness,cset)
            metrics = lib.cost(co)
            record_kernel_cost(costs,peaks,"core",metrics)
            word_cases.append(dict(prefix="".join(map(str,h)),R=R,core_R=D,core_J=str(cj),
                 full_J=str(g*cj),full_Delta=str(g*delta),full_tail=[g*ca,g*cb],full_mu=str(mu/g),
                 full_parent_mass=str(normrows(cfield)/g),Pmax=pmax,first_bad_full_pair=None if witness is None else g*witness,
                 square_test_at_epsilon_half=accepted,
                 decision="EXACT_BOUNDARY" if not delta else "NO_CERTIFIED_COMPRESSION" if not mu else
                 "CERTIFIED_TRUNCATION" if accepted else "RETAIN_RESIDUAL"))
            if mu:
                common = lcm(*(x.denominator for row in tw.values() for x in row.values()))
                tail_state = {(0,w,0):tuple(int(row.get(i,0)*common) for i in range(61))
                              for w,row in tw.items()}
                tail_plan = sim.branch_plan(tail_state,common,h)
                assert tail_plan.masses == (mu/2,mu/2)
                for bit in (0,1):
                    next_tail = lib.raw_field(*sim.materialize(tail_plan,bit))
                    assert normrows(next_tail) == mu/2
                    counts["native_next_arm_tail_states"] += 1
            if minimal[R] and 1<<T < 2*R:
                Tdelta = g*delta
                prob_removed = Tdelta/(2*R-(1<<T)+Tdelta)
                label_tv = sum(abs(normrow(cfield.get(w,{}))/normrows(cfield)
                                   -normrow(tw.get(w,{}))/mu) for w in set(cfield)|set(tw))/2
                inner = sum(op.dot(v,tw.get(w,{})) for w,v in cfield.items())
                pure_distance_sq = 1-inner**2/(mu*normrows(cfield))
                assert prob_removed==pure_distance_sq==label_tv
                word_cases[-1]["sharp_work_TV_and_pure_distance_squared"] = str(prob_removed)
        for b in product((0,1),repeat=j):
            fullh = h+b
            word_op = rd.Ops()
            words = lib.bind_word(rd,word_op,short,fullh)
            record_kernel_cost(costs,peaks,"full_word_binding",lib.cost(word_op))
            labels = lib.labels_for_validation(short,T)
            zs = labels[:-1]
            falpha, fullfield = lib.coeffs_and_rows(op,rd,words,labels)
            assert fullfield == lib.raw_field(*levels[T][fullh])
            assert classmap[fullh] == {w:normrow(row) for w,row in fullfield.items()}
            def lift(s,v):
                for bit in reversed(range(j)):
                    if s>>bit & 1:
                        v = op.apply(words[bit],v)
                return v
            for e,vec in enumerate(falpha):
                assert vec == lift(e%g,calpha[e//g])
                counts["ordered_word_address_rows"] += 1
            if N == 35 and not any(fullh):
                by_coset = {s:sum(normrow(falpha[e]) for e in range(s,5,g)) for s in range(g)}
                assert len(set(zs[:5])) == 5
                assert [by_coset[s]/sum(by_coset.values()) for s in range(g)] == [F(2,5),F(1,5),F(1,5),F(1,5)]
                scope_controls["unaligned_window_0_to_5_coset_law"] = ["2/5","1/5","1/5","1/5"]
            for R,(ca,cb,cj,delta,cwt,cmu,pmax,witness,cset) in core_rows.items():
                pairs, pos, length = lib.partition(1<<T,R)
                assert (pos,length) == (g*ca,g*cb)
                assert pairs == [g*k+s for k in cset for s in range(g)]
                ft = lib.scale(op,lib.combine(op,*({zs[e]:falpha[e]} for e in range(pos,pos+length))),F(1,1<<T))
                for k,w in enumerate(cz):
                    if k and w in cz[:k]:
                        continue
                    for s in range(g):
                        lw = zs[g*k+s]
                        assert ft.get(lw,{}) == weighted(op,lift(s,cwt.get(w,{})),F(1,g))
                        assert fullfield.get(lw,{}) == weighted(op,lift(s,cfield.get(w,{})),F(1,g))
                assert normrows(ft)==cmu/g
                assert max(Counter(zs[k] for k in pairs).values(),default=0)==pmax
                scalar = rd.Ops()
                assert rd.carry(scalar,words,R,rd.eye()) == g*cj
                y = [normrow(op.vadd(falpha[e],falpha[e+R])) for e in range(len(zs)-R)]
                assert sum(y)==g*delta
                assert next((e for e,x in enumerate(y) if x),None) == (None if witness is None else g*witness)
                if delta:
                    assert rd.locate_defect(scalar,words,R)["f"]==g*witness
                metrics = lib.cost(scalar)
                record_kernel_cost(costs,peaks,"full",metrics)
                counts["full_word_return_cases"] += 1
            counts["terminal_words"] += 1
            counts["terminal_nonzero_row_masses"] += len(fullfield)
    return dict(N=N,a=A,t=T,schedule=probes,verified=returns,certified_power_of_two=g,
           retained_depth=mid,certified_least_returns=minimal,scope_controls=scope_controls,cases_per_reduced_prefix=word_cases,terminal_and_address_counts=dict(counts),
           exact_costs=dict(full_admission_BRC=full_admit,reduced_admission_BRC=short_admit,
                            full_tree=full_cost,reduced_tree=reduced_cost,
                            extra_columns_for_reduced_joint_output=lookup_count,extra_native_BRC_for_these_columns=relabel_brc_calls,
                            unique_prefix_work_labels_to_lift=len(shifts),
                            operator_word_and_first_bad_pair=dict(costs),operator_peaks=dict(peaks)),
           terminal_distribution_sha256=sha256(lib.canonical({
              "".join(map(str,k)):{w:str(x) for w,x in sorted(v.items())} for k,v in sorted(classmap.items())})).hexdigest())


if __name__ == "__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--stage",type=Path,required=True)
    p.add_argument("--audit",type=Path,required=True)
    p.add_argument("--wave18",type=Path,default=Path(__file__).resolve().parents[1]/"eighteenth"/"return_defect_check.py")
    args=p.parse_args()
    lib=load_helper(args.wave18)
    api=lib.imports(args.repo.resolve(),args.stage.resolve(),args.audit.resolve())
    result=[fixture(n,lib,api) for n in FIXTURES]
    print(json.dumps(dict(conditions={"N":FIXTURES,"base":A,"program_width":T,"odd_scan":NU,"bank":lib.BANK,
                       "epsilon":"1/2","samples_pilot_or_production":0},fixtures=result),sort_keys=True,indent=2))
