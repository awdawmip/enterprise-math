"""Typed triadic-assembly INTERFACE TEST, not native force dynamics.

Run python check_triad.py. Only pinned BRC operations accumulate branch data.
The synthetic certificate libraries below are TEST_ONLY: no native closure
oracle, primitive force realization, timing, or physical occupancy law is given.
A one-shot occurrence may be allocated to at most one selected event. This is
explicit assembly semantics, not a universal prohibition on later interactions.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
import sys
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load(name, path, blob):
    raw = path.read_bytes()
    actual = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if actual != blob:
        raise RuntimeError(f'pin mismatch for {path}')
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

rpath = ROOT / 'packet_router.py'
if not rpath.exists():
    rpath = ROOT.parent / '20261007_cell_closure_u2_7f21d8/packet_router.py'
ppath = ROOT / 'prior/BRC_PATCH.py'
if not ppath.exists():
    ppath = ROOT.parent / '20261007_residual_algebra_patch_7c2e8a/BRC_PATCH.py'
r = load('triad_brc_router', rpath, '7465f5aa16cbb8fba61ba4be80f8a6884b879c53')
s = load('triad_path_readout', ppath, 'e3397722b0ee88dc9810cb872a14e7889403eee5')
CHECKS = 0

def ck(ok, msg):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(msg)

@dataclass(frozen=True)
class TestEvent:
    key: str
    occurrences: frozenset[int]
    weight: object
    scope: str = 'TEST_ONLY_NOT_NATIVE_CERTIFICATE'

    def __post_init__(self):
        if len(self.occurrences) != 3:
            raise ValueError('a test event uses exactly three distinct occurrences')
        if self.scope != 'TEST_ONLY_NOT_NATIVE_CERTIFICATE':
            raise ValueError('this prototype does not validate native certificates')

# A basis term retains selected event identity AND assigned occurrence identity.
# Scalar zero is absence of a compatible certificate family, not annihilation
# of any physical input. The inventory is always retained separately.
Basis = tuple[frozenset[str], frozenset[int]]
EMPTY: Basis = (frozenset(), frozenset())

def combine_basis(a: Basis, b: Basis):
    if a[0] & b[0] or a[1] & b[1]:
        return None
    return (a[0] | b[0], a[1] | b[1])


def plus(a, b):
    out = dict(a)
    for key, val in b.items():
        out[key] = r.merge(out.get(key, r.brc.CWM_ZERO), val)
    return out


def times(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            key = combine_basis(ka, kb)
            if key is not None:
                out[key] = r.merge(out.get(key, r.brc.CWM_ZERO), r.serial(va, vb))
    return out


def factor(event):
    return {EMPTY: r.brc.CWM_ONE,
            (frozenset([event.key]), event.occurrences): event.weight}


def assemble(events, inventory):
    # Conditional input validation: accepted tests are NOT native certificates.
    if len({e.key for e in events}) != len(events):
        raise ValueError('duplicate event identity')
    if any(not e.occurrences <= inventory for e in events):
        raise ValueError('event names an unavailable occurrence')
    out = {EMPTY: r.brc.CWM_ONE}
    for event in events:
        out = times(out, factor(event))
    return out


def row(key, value, inventory):
    return dict(events=sorted(key[0]), assigned=sorted(key[1]),
                unassigned=sorted(inventory-key[1]),
                C=value.count, W=str(value.total), M=str(value.dominant))


def maximal_keys(poly):
    return [k for k in poly if not any(k[0] < j[0] for j in poly)]


def future_add(poly, event, inventory):
    # Retain the alternative that does nothing as well as every compatible use.
    return times(poly, factor(event))


def main():
    # All signed three-distinct-axis words (NOT declared native-stable triads).
    # The inherited BRC coefficient/readout implementation supplies endpoints.
    projection = []
    for axes in combinations(range(1, 7), 3):
        for signs in product((-1, 1), repeat=3):
            letters = tuple(a * b for a, b in zip(axes, signs))
            for word in permutations(letters):
                z, omega = s.readout(s.signature(word, 2))
                ck(sum(v != 0 for v in z) == 3, 'three independent supports')
                ck(any(z), 'not identity under any endpoint-faithful extension')
                projection.append(dict(word=word, z=z, omega=omega))
    # Explicit finite positive provenance preserves alternatives and choices.
    I = frozenset(range(1, 7))
    events = [TestEvent('A123', frozenset((1,2,3)), r.edge(1)),
              TestEvent('B145', frozenset((1,4,5)), r.edge(1)),
              TestEvent('C456', frozenset((4,5,6)), r.edge(1))]
    poly = assemble(events, I)
    ck(len(poly) == 5, 'empty, three singletons, and AC')
    expected = {frozenset(), frozenset(['A123']), frozenset(['B145']),
                frozenset(['C456']), frozenset(['A123','C456'])}
    ck({k[0] for k in poly} == expected, 'exact assembly support')
    for ordering in permutations(events):
        ck(assemble(ordering, I) == poly, 'parallel factor order irrelevant')
    maxima = maximal_keys(poly)
    ck({k[0] for k in maxima} == {frozenset(['B145']),frozenset(['A123','C456'])},
       'maximal and maximum are different')
    ck({I-k[1] for k in maxima} == {frozenset((2,3,6)),frozenset()},
       'distinct unassigned normal forms')
    for k in poly:
        ck(k[1] | (I-k[1]) == I and not k[1] & (I-k[1]), 'inventory preserved')
        ck(len(k[1]) == 3*len(k[0]), 'no repeated occurrence in selected events')
    # Inspect all eight proposals separately, including incompatible ones.
    proposal_rows = []
    for bits in product((False,True), repeat=len(events)):
        chosen = [e for e,bit in zip(events,bits) if bit]
        used = frozenset().union(*(e.occurrences for e in chosen))
        ok = len(used) == 3*len(chosen)
        key = (frozenset(e.key for e in chosen), used)
        ck((key in poly) == ok, 'all proposals classified, none hidden')
        proposal_rows.append(dict(events=sorted(key[0]),compatible=ok,
                                  inventory=sorted(I),used=sorted(used)))
    # Conditional polynomial law is a genuine semiring: tested on full finite
    # 6-occurrence positive-triple library plus nontrivial CWM mixtures.
    all_events = [TestEvent('H'+''.join(map(str,h)),frozenset(h),r.edge(1))
                  for h in combinations(range(1,7),3)]
    all_poly = assemble(all_events, I)
    ck(len(all_poly) == 31, 'empty + 20 single events + 10 disjoint pairs')
    bases = list(all_poly)
    for a,b,c in product(bases,repeat=3):
        ab,bc=combine_basis(a,b),combine_basis(b,c)
        left = None if ab is None else combine_basis(ab,c)
        right= None if bc is None else combine_basis(a,bc)
        ck(left==right,'partial disjoint union associative including incompatibility')
    samples=[{}, {EMPTY:r.brc.CWM_ONE}]
    samples += [factor(e) for e in events]
    samples += [poly, plus(factor(events[0]),factor(events[1]))]
    for a,b,c in product(samples,repeat=3):
        ck(times(times(a,b),c)==times(a,times(b,c)), 'CWM convolution associativity')
        ck(times(a,plus(b,c))==plus(times(a,b),times(a,c)), 'left distributivity')
        ck(times(plus(a,b),c)==plus(times(a,c),times(b,c)), 'right distributivity')
    # Clearing all unassigned occurrences is not the empty event history.
    ac=next(k for k in poly if k[0]==frozenset(['A123','C456']))
    ck(not I-ac[1] and ac[0], 'closed record nonempty despite zero unassigned')
    # Resource budget is a declared combinatorial cost, not energy or force.
    weighted=[TestEvent(e.key,e.occurrences,r.edge(w)) for e,w in zip(events,(2,3,5))]
    wpoly=assemble(weighted,I)
    ck(r.total(wpoly.values()).total==21,'un-normalized weighted enumerator')
    # Missing native evidence is not repaired by arithmetic, counts or labels.
    rejected=False
    try:
        TestEvent('bad',frozenset((1,2,3)),r.edge(1),scope='NATIVE_VALIDATED')
    except ValueError:
        rejected=True
    ck(rejected,'native authority cannot be set by caller in this prototype')
    results={
      'schema':'EM_TRIADIC_ASSEMBLY_INTERFACE_TEST_V1',
      'status':'CONDITIONAL_TEST_ONLY_NOT_NATIVE_FORCE_LIFT',
      'global_snapshot':'4ae8956b65ced23a31929c866a9d78495f7526b2',
      'source_snapshot':'00cba08eaccae50fe4b7511abf880f39935cbdba',
      'projection_word_count':len(projection),'projection_words':projection,
      'assembly_branches':[row(k,v,I) for k,v in sorted(poly.items(),key=lambda kv:sorted(kv[0][0]))],
      'maximal_branches':[row(k,poly[k],I) for k in maxima],
      'proposals_including_incompatible':proposal_rows,
      'full_positive_triple_test_library_branches':len(all_poly),
      'basis_associativity_triples':len(bases)**3,
      'CWM_polynomial_test_triples':len(samples)**3,
      'assertions':CHECKS,'inherited_readout_assertions':s.CHECKS,
      'BRC_calls':dict(r.CALLS),'path_BRC_calls':dict(s.CALLS),
      'native_certificate_library_supplied':False,
      'force_to_coordinate_law_supplied':False,
      'physical_minimum_perturbation_proved':False,
      'previous_full_suites_reexecuted':False}
    data=(json.dumps(results,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    (ROOT/'results.json').write_bytes(data)
    print(json.dumps({k:v for k,v in results.items() if k not in ('projection_words','assembly_branches','maximal_branches','proposals_including_incompatible')},indent=2))
    print('results_sha256',hashlib.sha256(data).hexdigest())
    print('bytes',len(data))

if __name__=='__main__':
    main()
