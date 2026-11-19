"""Exact conditional recording and retention on the public RR-06 channel model."""
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import permutations, product
import json
from math import comb, factorial
from pathlib import Path
import sys


SIBLINGS = Path(__file__).resolve().parents[1]
HELPERS = {
    'eightyfifth/euler_check.py': 'ec8986d8329ebaf390a05b9e376142d4fd35ae1fdfd6f7649ea9328982ed0082',
    'ninetieth/recorders_check.py': 'f1af1e08c97d50ca1996796774fc6f1693fcc4ace1d9453837345a46a9d49f31',
}
PINS = {
    'research_tasks/RS-EULER-RR-06-AUTONOMOUS-LATCH-20261011.md': 'd9d34c751abd8dc2bb3fb814220d028ea2fe1057',
    'research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING.md': '03cfdf23f8f1a6208b4ac4eb862a1b7ad3811d8b',
    'research_notes/chatgpt_direct/20261010_EULER_CONTROLLER_RELATIONAL_MEMORY.md': '22a7d072e54f40c52a94e91dac7f68f63371436c',
    'research_notes/chatgpt_direct/20261011_EULER_READOUT_BACKACTION.md': '5e00414f752d97d69cee9bf602fd6b5e50da4b05',
    'src/enterprise_math/brc_weighted.py': '3f205696709e847909958a153f8fe10d3f6b70f0',
    'src/enterprise_math/brc_logarithm.py': '4732e5fc381ce613d240c4381ccbef03c27a69c7',
    'src/enterprise_math/exact_arithmetic.py': '35ea95b0916494b83a92386e3e313928362dd79e',
}


def load(repo):
    for name, digest in HELPERS.items():
        path = SIBLINGS / name
        assert sha256(path.read_bytes()).hexdigest() == digest
        sys.path.insert(0, str(path.parent))
    for name, digest in PINS.items():
        raw = (repo / name).read_bytes()
        assert sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == digest
    sys.path.insert(0, str(repo / 'src'))
    from enterprise_math import brc_weighted
    from euler_check import cycle, gate
    from recorders_check import signed_unit_contact
    return brc_weighted, cycle, gate, signed_unit_contact


def profile(perm, size):
    """Start in receiver label 0 and count the consecutive first outputs of label 1."""
    counts = []
    for c in range(size):
        point = perm[c]
        held = 0
        while size <= point < 2 * size:
            held += 1
            point = perm[point]
        counts.append(held)
    return tuple(counts)


def construct(lengths):
    size = len(lengths)
    free = iter(i for i, n in enumerate(lengths) if n == 0)
    successor = list(range(size))
    for start, n in enumerate(lengths):
        if n:
            route = [start] + [next(free) for _ in range(n - 1)]
            for left, right in zip(route, route[1:] + route[:1]):
                successor[left] = right
    return tuple(((r + int(lengths[c] > 0)) % 3) * size + successor[c]
                 for r, c in product(range(3), range(size)))


def profiles():
    report = []
    for size in range(1, 4):
        feasible = {x for x in product(range(size + 1), repeat=size) if sum(x) <= size}
        observed = Counter(profile(p, size) for p in permutations(range(3 * size)))
        assert set(observed) == feasible and len(feasible) == comb(2 * size, size)
        for x in feasible:
            perm = construct(x)
            assert len(set(perm)) == 3 * size and profile(perm, size) == x
        report.append(dict(states=size, permutations=factorial(3 * size), profiles=len(feasible),
                           mass_by_total_retention={h:sum(n for x,n in observed.items() if sum(x)==h)
                                                    for h in range(size + 1)}))
    return report


def step(state, difference, H, M):
    r, c, z = state
    if difference:
        return (r + (difference if c == 0 else 0)) % 3, (c + 1) % H, z
    return r, c, (z + int(c == 0)) % M


def counter_tests():
    checked = schedules = 0
    for H, M in product(range(1, 10), range(1, 7)):
        states = set(product(range(3),range(H),range(M)))
        for delta in range(3):
            assert {step(x, delta, H, M) for x in states} == states
            checked += len(states)
        for a, delta, delay in product(range(3),(1,2),range(M)):
            x = (a, 0, 0)
            for _ in range(delay):
                x = step(x, 0, H, M)
            for _ in range(H):
                x = step(x, delta, H, M)
                assert (x[0],x[2]) == ((a + delta) % 3,delay)
            assert step(x, delta, H, M)[0] != (a + delta) % 3
            schedules += 1
    return dict(H_range=[1,9], M_range=[1,6], permutation_rows=checked, fixed_source_schedules=schedules)


def sources(kernel, cycle, gate, contact, H=5):
    domain = list(product(range(3),range(2),range(8),range(4),range(2)))
    assert len(set(map(cycle,domain))) == len(domain)
    jumps = Counter((cycle(s)[0]-s[0])%3 for s in domain)
    assert set(jumps) == {1,2}
    total = kernel.CWM_ZERO
    costs, times, correct = Counter(), Counter(), Counter()
    named_trace = []
    branches = len(domain)*3*3*2
    for src, a, error, sheet in product(domain,range(3),range(3),(-1,1)):
        origin = src
        intended_source = origin
        receiver, c, z = (a+error)%3, 0, 0
        capture = int(src[0] == a)
        target = (cycle(src) if capture else src)[0]
        w = kernel.cwm_edge(Fraction(1,branches))
        for tick in range(capture + H):
            j = src[0]
            delta = (j-a)%3
            active = bool(delta and c == 0)
            held_receiver, c, z = step((receiver,c,z),delta,H,2)
            ports = [j,a,receiver]
            w = contact(ports,2,delta if active else 0,(1,sheet),w,kernel,costs)
            receiver = ports[2]
            assert receiver == held_receiver and w.total == Fraction(1,branches)
            if tick >= capture:
                assert (receiver,z) == ((target+error)%3,capture)
            if origin == (0,0,2,0,0) and (a,error,sheet)==(0,0,1):
                named_trace.append([tick,j,active,c,z,receiver])
            for cmd in 'HUC':
                src = gate(src,cmd)
                w = kernel.cwm_propagate(w,kernel.CWM_ONE)
                costs['old_source_commands'] += 1
            intended_source = cycle(intended_source)
            assert src == intended_source
        times[capture] += 1
        correct[error] += int(receiver==target)
        total = kernel.cwm_recoalesce(total,w)
    assert (total.count,total.total,total.dominant)==(branches,1,Fraction(1,branches))
    return dict(public_core_modes=len(domain),single_round_jumps=dict(jumps),H=H,M=2,
                ready_and_biased_branches=branches,branches_by_capture_time=dict(times),
                exact_agreement_by_calibration_offset=dict(correct),costs=dict(costs),
                final_mass=[total.count,str(total.total),str(total.dominant)],
                example_columns=['tick','source_before_T','write','clock_after','time_tag','receiver'],
                example=named_trace)


def periodic_example(cycle):
    src = (0,0,2,0,0)
    orbit = [src]
    for _ in range(11):
        orbit.append(cycle(orbit[-1]))
    assert cycle(orbit[-1]) == src and len(set(orbit)) == 12
    sample = orbit[5]
    hits = [i for i, x in enumerate(orbit) if x[0] == 2]
    assert hits == [5,11]
    rows = []
    for label, predicate, stride in [('oriented_difference_2', lambda v:v[0]==2, 6),
                                     ('specified_whole_mode', lambda v:v==sample, 12)]:
        for H in (1,5,12,13,37):
            size = (H + stride - 1) // stride
            r = c = 0
            src = sample
            for k in range(size * stride + 1):
                if predicate(src):
                    if c == 0:
                        r = (r + src[0]) % 3
                    c = (c + 1) % size
                assert r == (2 if k < size * stride else 1)
                src = cycle(src)
            rows.append([label,H,size,size*stride])
    return dict(channel_word=[x[0] for x in orbit],hits=hits,
                columns=['phase_test','required_H','controller_states','actual_window'],rows=rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True,help='enterprise-math checkout with the pinned source files')
    args = parser.parse_args()
    modules = load(args.repo)
    print(json.dumps(dict(contract='RS-EULER-RR-06-AUTONOMOUS-LATCH-20261011',
                          source_kind='pinned public boundary reconstruction, no private ZIP replay',
                          arbitrary_permutations=profiles(), tagged_counter=counter_tests(),
                          old_source_and_contacts=sources(*modules),
                          periodic_comparison=periodic_example(modules[1])),ensure_ascii=False,indent=2))
