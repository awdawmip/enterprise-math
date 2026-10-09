"""Paired positive-BRC response spectra and resource-valid three-event fan-out.

TEST_ONLY reservation semantics; six modules are NOT six spatial axes. Uses
unchanged pinned reserve/release and CWM primitives. A paired trace is two
counterfactual runs on one declared preparation/command seed, not two physical
copies and not a tensor-product probability. No old main suite is executed.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PRIOR = ROOT / 'prior/check_membership.py'
if not PRIOR.exists():
    PRIOR = ROOT.parent / '20261008_residual_membership_7c2e8a/check_membership.py'
raw = PRIOR.read_bytes()
assert hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == 'be1b60446e31c2c8489d1ce0db16cc1e952d11c8'
spec = importlib.util.spec_from_file_location('joint_response_pinned_membership', PRIOR)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)
r = m.r
CHECKS = 0
TARGETS = (7, 13, 19, 25, 31)
GATES = ((1, 7, 13), (2, 19, 25), (3, 31, 32))
BLOCKERS = ((7, 8, 9), (19, 20, 21), (31, 33, 34))


def ck(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(label)


def cw(w):
    return dict(C=w.count, W=str(w.total), M=str(w.dominant))


def put(out, key, w):
    out[key] = r.merge(out.get(key, r.brc.CWM_ZERO), w)


def occupancy(J):
    return tuple(int(b in m.used(J)) for b in TARGETS)


def module_state(J, g):
    lo, hi = 6*g+1, 6*g+6
    return tuple((b, tuple(h)) for h in J for b in h if lo <= b <= hi)


def valid(J):
    flat = tuple(b for h in J for b in h)
    return all(len(h) == 3 for h in J) and len(flat) == len(set(flat)) and set(flat) <= set(range(1, 37))


def trial(flags=(1, 1, 1), blocked=(0, 0, 0), order=(0, 1, 2), weight=Q(1)):
    """Fixed full preparation includes flags; the local intervention is release(1)."""
    if any(x not in (0, 1) for x in flags + blocked) or sorted(order) != [0, 1, 2]:
        raise ValueError('bad finite protocol input')
    start = m.canon([(1, 2, 3)] + [BLOCKERS[i] for i in range(3) if blocked[i]])
    w = m.active_monomial(start, weight)  # actual inherited compatible assembly
    ctl = start
    trt, released, ok = m.full_step(start, ('release', 1))
    w = r.serial(w, r.brc.CWM_ONE)
    ck(released == 1 and ok, 'source event genuinely released')
    ck(all(module_state(ctl, g) == module_state(trt, g) for g in range(1, 6)), 'initial intervention changes only source module')
    trace = [dict(stage='local_intervention', control=ctl, treated=trt,
                  target_control=occupancy(ctl), target_treated=occupancy(trt))]
    for gate_id in order:
        old = (ctl, trt)
        marks = ('skip', 'skip')
        if flags[gate_id]:
            ctl, _, c_ok = m.full_step(ctl, ('reserve', GATES[gate_id]))
            trt, _, t_ok = m.full_step(trt, ('reserve', GATES[gate_id]))
            marks = ('accepted' if c_ok else 'blocked', 'accepted' if t_ok else 'blocked')
        w = r.serial(w, r.brc.CWM_ONE)  # one seed weight; never square it
        ck(valid(ctl) and valid(trt), 'no occurrence duplicated, lost from inventory, or malformed event')
        support = {(b-1)//6 for b in GATES[gate_id]}
        for before, after in zip(old, (ctl, trt)):
            ck(all(module_state(before, g) == module_state(after, g) for g in range(6) if g not in support), 'complete state outside declared support unchanged')
        trace.append(dict(stage=gate_id, flag=flags[gate_id], proposal=GATES[gate_id],
                          outcomes=marks, control=ctl, treated=trt,
                          target_control=occupancy(ctl), target_treated=occupancy(trt)))
    a, b = occupancy(ctl), occupancy(trt)
    delta = tuple(y-x for x, y in zip(a, b))  # comparison, not negative mass
    mask = tuple(int(x != 0) for x in delta)
    enabled = [int(flags[i] and not blocked[i]) for i in range(3)]
    ck(mask == (enabled[0], enabled[0], enabled[1], enabled[1], enabled[2]), 'derived five-output mask')
    ck(w.total == weight, 'paired trajectories retain preparation weight once')
    return dict(flags=flags, blocked=blocked, order=order, initial=start, trace=trace,
                delta=delta, mask=mask, CWM=cw(w)), w


def statistics(hist):
    total = r.total(hist.values())
    ck(total.total == 1, 'normalized positive response-mask law')
    p = [r.total(w for mask, w in hist.items() if mask[j]).total for j in range(5)]
    theta = hist.get((1,)*5, r.brc.CWM_ZERO).total
    lower, upper = max(Q(), sum(p, Q())-4), min(p)
    ck(lower <= theta <= upper, 'intersection bounds')
    pairs = [str(r.total(w for mask, w in hist.items() if mask[i] and mask[j]).total)
             for i, j in combinations(range(5), 2)]
    return dict(marginals=list(map(str, p)), pair_success_weights=pairs,
                all_five=str(theta), lower=str(lower), upper=str(upper),
                spectrum=[dict(mask=k, CWM=cw(v)) for k, v in sorted(hist.items())])


def paired_examples():
    rows = []
    for flags in product((0, 1), repeat=3):
        for blocked in product((0, 1), repeat=3):
            for order in permutations(range(3)):
                row, _ = trial(flags, blocked, order)
                rows.append(row)
    certain, _ = trial()
    obstructed, _ = trial(blocked=(1, 0, 0))
    ck(certain['mask'] == (1,)*5 and obstructed['mask'] == (0, 0, 1, 1, 1), 'possible joint fanout and connected-but-blocked counterexample')
    # Same primitive rules; different explicit joint preparation of gate flags.
    parity_laws, parity_traces = [], []
    for parity in (0, 1):
        hist, paths = {}, []
        for flags in product((0, 1), repeat=3):
            if sum(flags) % 2 != parity:
                continue
            row, w = trial(flags=flags, weight=Q(1, 4))
            put(hist, row['mask'], w)
            paths.append(row)
        parity_laws.append(statistics(hist))
        parity_traces.append(paths)
    ck(parity_laws[0]['marginals'] == parity_laws[1]['marginals'] == ['1/2']*5, 'all five marginal responses identical')
    ck(parity_laws[0]['pair_success_weights'] == parity_laws[1]['pair_success_weights'], 'all pair response statistics identical')
    ck([x['all_five'] for x in parity_laws] == ['0', '1/4'], 'joint fanout differs despite identical marginal and pair profiles')
    # A common seed bit enables all or no commands: same five marginals, theta=1/2.
    hist = {}
    for flags in ((0, 0, 0), (1, 1, 1)):
        row, w = trial(flags=flags, weight=Q(1, 2)); put(hist, row['mask'], w)
    common = statistics(hist)
    ck(common['marginals'] == ['1/2']*5 and common['all_five'] == '1/2', 'marginal equality also permits half joint fanout')
    return dict(protocols=len(rows), full_protocol_traces=rows, deterministic=certain,
                blocked=obstructed, flag_parity_laws=parity_laws,
                parity_preparation_traces=parity_traces, common_flag_law=common)


def abstract_mask_bounds():
    """Declared BRC diagnostic mask populations, NOT physical preparations."""
    masks = list(product((0, 1), repeat=5))
    checked = 0
    h = hashlib.sha256()
    for a, b in combinations(masks, 2):
        for k in range(1, 8):
            row = statistics({a:r.edge(Q(k, 8)), b:r.edge(Q(8-k, 8))})
            h.update(json.dumps([a, b, k, row], sort_keys=True).encode()); checked += 1
    for a in masks:
        statistics({a:r.brc.CWM_ONE}); checked += 1
    # Both extremes at p_j=4/5, demonstrating sharpness at the zero lower bound.
    miss_one = {tuple(int(j != i) for j in range(5)):r.edge(Q(1, 5)) for i in range(5)}
    all_or_none = {(1,)*5:r.edge(Q(4, 5)), (0,)*5:r.edge(Q(1, 5))}
    lo, hi = statistics(miss_one), statistics(all_or_none)
    ck(lo['marginals'] == hi['marginals'] == ['4/5']*5, 'same large individual response probabilities')
    ck(lo['all_five'] == '0' and hi['all_five'] == '4/5', 'sharp endpoints for identical marginals')
    almost = {(1,)*5:r.edge(Q(1, 2))}
    for i in range(5):
        almost[tuple(int(j != i) for j in range(5))] = r.edge(Q(1, 10))
    pos = statistics(almost)
    ck(pos['marginals'] == ['9/10']*5 and pos['lower'] == pos['all_five'] == '1/2', 'positive lower endpoint attained')
    return dict(normalized_laws_checked=checked, certificate_sha256=h.hexdigest(),
                sharp_zero_lower=lo, sharp_upper=hi, sharp_positive_lower=pos)


def coupling_witness():
    """Identifiability witness only; alternative couplings are not same dynamics."""
    zero, one = (0,)*5, (1,)*5
    rows = []
    marginals = []
    for flip in (False, True):
        joint = [(zero, one if flip else zero), (one, zero if flip else one)]
        ctl, trt, masklaw = {}, {}, {}
        for a, b in joint:
            w = r.edge(Q(1, 2))
            put(ctl, a, w); put(trt, b, w)
            put(masklaw, tuple(int(x != y) for x, y in zip(a, b)), w)
        ck(ctl == trt, 'control and treatment complete output marginals equal')
        row = statistics(masklaw)
        row['paired_outputs'] = [dict(control=a, treated=b, W='1/2') for a, b in joint]
        rows.append(row); marginals.append((ctl, trt))
    ck(marginals[0] == marginals[1] and [x['all_five'] for x in rows] == ['0', '1'], 'unpaired outcome laws do not identify same-seed change')
    return dict(couplings=rows, structural_pairing_required=True, native_identification=False)


def support_certificate():
    """Pure support propagation; complete read/write locality is an extra premise."""
    supports = [{(b-1)//6 for b in D} for D in GATES]
    C = {0}; trace = [sorted(C)]
    for S in supports:
        if C & S:
            C |= S
        trace.append(sorted(C))
    ck([len(c) for c in trace] == [1, 3, 5, 6], 'resource witness saturates total event lower bound')
    triples = list(combinations(range(6), 3)); counts = []
    # All length<=2 support words; each branch has explicit unit count weight.
    for depth in (0, 1, 2):
        mass = r.brc.CWM_ZERO
        for word in product(triples, repeat=depth):
            C = {0}; w = r.brc.CWM_ONE
            for S in word:
                w = r.serial(w, r.brc.CWM_ONE)
                if C & set(S):C |= set(S)
            ck(len(C) <= 1+2*depth and len(C) < 6, 'at most two complete-support ternary events cannot reach all six modules')
            mass = r.merge(mass, w)
        counts.append(cw(mass))
    return dict(supports=[sorted(x) for x in supports], cone_trace=trace,
                lower_bound_total_cross_events=3, complete_short_support_word_counts=counts,
                physical_clock_bound=False, native_balance_arity_implies_locality=False)


def main():
    examples = paired_examples()
    bounds = abstract_mask_bounds()
    coupling = coupling_witness()
    cone = support_certificate()
    result = dict(schema='EM_PAIRED_JOINT_RESPONSE_V1',
      event_id='EM-20261009-RESIDUAL-JOINT-RESPONSE-7C2E8A',
      status='CONDITIONAL_EXECUTED_BRC_NOT_NATIVE_DYNAMICS_UNREVIEWED',
      global_read='9944ec5937a4024fbdad0c6de6d3f0bd6f33e5f0',
      source_read='2a563624c36515fdf38f93a7b78b62833c93ea6a',
      examples=examples, bounds=bounds, coupling=coupling, causal_support=cone,
      checks=CHECKS, inherited_helper_checks=m.CHECKS, BRC_calls=dict(r.CALLS),
      old_main_suites_executed=False, native_force=False, six_modules_are_six_axes=False,
      independent_review=False, positive_weights_squared_in_pairing=False)
    data=(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)+'\n').encode()
    (ROOT/'results.json').write_bytes(data)
    summary=dict(checks=CHECKS, inherited_helper_checks=m.CHECKS, BRC_calls=dict(r.CALLS),
                 protocols=examples['protocols'], mask_laws_checked=bounds['normalized_laws_checked'],
                 theta_parity=[x['all_five'] for x in examples['flag_parity_laws']],
                 deterministic_mask=examples['deterministic']['mask'],
                 output_bytes=len(data), output_sha256=hashlib.sha256(data).hexdigest())
    (ROOT/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary, indent=2))

if __name__=='__main__':main()
