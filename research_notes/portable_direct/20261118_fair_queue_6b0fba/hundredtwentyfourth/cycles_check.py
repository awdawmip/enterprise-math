"""Check stationary finite recorder resources and optimal cyclic calibration tapes."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import permutations, product
from math import factorial, gcd, prod
from pathlib import Path
import runpy
import json


def block_law(q, length):
    return {w: prod(q[i] for i in w) for w in product(range(len(q)), repeat=length)}


def euler_tape(adjacency, start):
    stack = [start]
    labels = []
    circuit = []
    while stack:
        vertex = stack[-1]
        if adjacency[vertex]:
            dest, letter = adjacency[vertex].pop()
            stack.append(dest)
            labels.append(letter)
        else:
            stack.pop()
            if labels:
                circuit.append(labels.pop())
    assert not any(adjacency.values())
    return tuple(reversed(circuit))


def window_frequencies(tape, length):
    period = len(tape)
    return Counter(tuple(tape[(i+j) % period] for j in range(length)) for i in range(period))


def rational_tape(a, n):
    alphabet = range(len(a))
    edges = defaultdict(list)
    for w in product(alphabet, repeat=n):
        edges[w[:-1]].extend([(w[1:], w[-1])] * prod(a[i] for i in w))
    tape = euler_tape(edges, (0,) * (n-1))
    assert len(tape) == sum(a) ** n
    assert {w: prod(a[i] for i in w) for w in product(alphabet, repeat=n)} == window_frequencies(tape, n)
    d = sum(a)
    nums = [prod(a[i] for i in v) * d for v in product(alphabet, repeat=n-1)]
    dens = [prod(a[i] for i in w) for w in product(alphabet, repeat=n)]
    necklace_count = F(prod(factorial(k) for k in nums), len(tape) * prod(factorial(k) for k in dens))
    assert necklace_count.denominator == 1
    return tape, necklace_count.numerator


def brute_necklaces(a, n):
    """Canonical cycles by literal word enumeration, with symbol totals fixed first."""
    expected = Counter({w: prod(a[i] for i in w) for w in product(range(len(a)), repeat=n)})
    tape, formula = rational_tape(a, n)
    counts = [x * sum(a) ** (n-1) for x in a]
    raw = 0
    necklaces = set()
    def visit(w):
        nonlocal raw
        if len(w) == len(tape):
            if window_frequencies(w, n) == expected:
                raw += 1
                necklaces.add(min(w[i:]+w[:i] for i in range(len(w))))
            return
        for j, remaining in enumerate(counts):
            if remaining:
                tail = w+(j,)
                if len(tail) < n or sum(tail[k:k+n] == tail[-n:] for k in range(len(tail)-n+1)) <= expected[tail[-n:]]:
                    counts[j] -= 1
                    visit(tail)
                    counts[j] += 1
    if a[0] == 1 and n > 1:
        # The all-zero N-word occurs exactly once, fixing the start of each necklace.
        counts[0] -= n
        visit((0,)*n)
        assert raw == len(necklaces)
        raw *= len(tape)
    else:
        visit(())
    assert len(necklaces) == formula and raw == len(tape) * formula
    return {'a': a, 'N': n, 'period': len(tape), 'raw_words': raw, 'necklaces': formula}


def endpoint_class(q, n):
    """All stationary state-minimal machines for these small instances."""
    s = len(q)
    words = tuple(product(range(s), repeat=n))
    suffixes = tuple(product(range(s), repeat=n-1))
    perms = [p for p in permutations(range(s)) if all(q[j] == q[p[j]] for j in range(s))]
    checked = 0
    tvs = {}
    orbit_counts = Counter()
    for choices in product(perms, repeat=len(suffixes)):
        rule = dict(zip(suffixes, choices))
        transition = {w: w[1:]+(rule[w[1:]][w[0]],) for w in words}
        assert len(set(transition.values())) == len(words)
        unseen = set(words)
        num_orbits = 0
        while unseen:
            curr = next(iter(unseen))
            while curr in unseen:
                unseen.remove(curr)
                curr = transition[curr]
            num_orbits += 1
        orbit_counts[num_orbits] += 1
        initial = block_law(q, n)
        assert all(initial[w] == initial[v] for w, v in transition.items())
        for extra in range(2*n+1):
            total = n+extra
            c, r = divmod(extra, n)
            observed = Counter()
            for w, mass in initial.items():
                curr, bits = w, []
                for _ in range(total):
                    bits.append(curr[0])
                    curr = transition[curr]
                observed[tuple(bits)] += mass
            target = block_law(q, total)
            tv = 1-sum(min(mass, target[w]) for w, mass in observed.items())
            exact = 1-sum(v**(c+2) for v in q)**r * sum(v**(c+1) for v in q)**(n-r)
            assert tv == exact
            tvs[total] = str(tv)
        checked += 1
    r = len(set(q))
    predicted_orbits = sum(r**gcd(j,n) for j in range(n)) // n
    assert min(orbit_counts) == predicted_orbits
    return {'minimum_number_of_orbits': predicted_orbits, 'orbit_count_histogram': dict(orbit_counts), 'q': list(map(str, q)), 'N': n, 'complete_tables': checked, 'TV_by_total_length': tvs}


def uniform_budget(s, n, k):
    if k == 1:
        tape, _ = rational_tape([1]*s, n)
    else:
        edges = defaultdict(list)
        for w in product(range(s), repeat=n):
            for shift in range(k):
                y = (w[0]+shift) % s
                edges[w].append((w[1:]+(y,), y))
        tape = euler_tape(edges, (0,)*n)
    assert len(tape) == k * s**n
    assert set(window_frequencies(tape, n).values()) == {k}
    for extra in range(1, 5):
        obs = window_frequencies(tape, n+extra)
        assert len(obs) == len(tape) and set(obs.values()) == {1}
        assert 1-F(len(obs),s**(n+extra)) == 1-F(k,s**extra)
    return {'s': s, 'N': n, 'k': k, 'period': len(tape), 'first_lost_TV': str(1-F(k,s))}


def native_records(repo):
    previous = Path(__file__).resolve().parents[1]/'fiftieth'/'calibration_check.py'
    adapter = runpy.run_path(str(previous))
    brc = adapter['load'](repo)
    name = 'research_tasks/RS-EULER-RR-05-REUSE-RESOURCE-20261011.md'
    data = (repo/name).read_bytes()
    blob = sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert blob == '3b1973cb0a22d10bf8e78b6e1459bf0ffbe99946'
    samples, costs = [], Counter()
    for n, a in [(2,(1,2,3)), (3,(1,1,1))]:
        tape, _ = rational_tape(a, n)
        for length in (n, n+1):
            freq = window_frequencies(tape,length)
            offsets = {(j,w): F(m,3*len(tape)) for j in range(3) for w,m in freq.items()}
            read = adapter['finite_kernel'](brc,costs,offsets)
            for j, row in enumerate(read['channel_by_source']):
                law = {tuple((y-j)%3 for y in w): F(p) for w,p in zip(read['record_words'],row) if F(p)}
                assert law == {w:F(m,len(tape)) for w,m in freq.items()}
            samples.append({'N':n,'a':a,'length':length,'observed_words':len(freq),
                            'conditional_table_sha256':sha256(json.dumps(read,sort_keys=True).encode()).hexdigest()})
    cleanup = Counter()
    for sheet in (-1,1):
        for a, receipt, new_source in product(range(3), repeat=3):
            r, log = receipt, a
            weight = brc.cwm_edge(F(1,27))
            for port in ('log','receiver'):
                delta = r-a if port == 'log' else a-log
                turns = (sheet*delta)%3
                for _ in range(turns or 1):
                    if port == 'log':
                        log = (log+sheet*bool(turns))%3
                    else:
                        r = (r+sheet*bool(turns))%3
                    cleanup['contact' if turns else 'hold'] += 1
                    weight = brc.cwm_propagate(weight,brc.CWM_ONE)
            assert (r,log,weight.total)==(a,receipt,F(1,27))
    return {'published_task_git_blob':blob, 'public_BRC_git_blobs':adapter['PINS'],
            'weighted_write_checks':samples,'actual_microsteps':dict(costs),'cleanup_microsteps':dict(cleanup)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo',required=True,type=Path)
    args = parser.parse_args()
    equality = [endpoint_class((F(1,2),F(1,2)),3), endpoint_class((F(1,2),F(1,4),F(1,4)),2),
                endpoint_class((F(1,2),F(1,3),F(1,6)),2)]
    rings = [brute_necklaces(a,n) for a,n in [((1,1),3), ((1,2),2),((1,1,1),2),((1,1,2),1),((1,1,2),2)]]
    budgets = [uniform_budget(s,n,k) for s in (2,3,4) for n in (1,2,3) for k in range(1,s+1)]
    out={'minimal_weighted_machines':equality,'independent_necklaces':rings,'uniform_budgets':budgets,
         'positive_record_replay':native_records(args.repo)}
    print(json.dumps(out,indent=2))


if __name__ == '__main__':
    main()
