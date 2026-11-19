#!/usr/bin/env python3
"""Exact positive-world register tests and independent subgroup/fibre enumeration."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha1
from itertools import product
import json
from math import gcd, prod
from pathlib import Path
import sys


PINS = {
    "research_tasks/RS-EULER-RECORDER-A04-RETENTION-RESET-20261012.md": "8c3c0a5e8f9f600969536be06591a3366e2cd37e",
    "research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING.md": "03cfdf23f8f1a6208b4ac4eb862a1b7ad3811d8b",
    "src/enterprise_math/brc_weighted.py": "3f205696709e847909958a153f8fe10d3f6b70f0",
    "src/enterprise_math/brc_logarithm.py": "4732e5fc381ce613d240c4381ccbef03c27a69c7",
    "src/enterprise_math/exact_arithmetic.py": "35ea95b0916494b83a92386e3e313928362dd79e",
}


def source(root):
    if root is None:
        root = next((p for p in (Path.cwd(), *Path(__file__).resolve().parents)
                     if (p / next(iter(PINS))).is_file()), None)
    if root is None:
        raise SystemExit("Pass --repo PATH to a checkout containing the pinned public files")
    for name, expected in PINS.items():
        raw = (root / name).read_bytes()
        assert sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest() == expected
    sys.path.insert(0, str(root / "src"))
    from enterprise_math import brc_weighted
    return brc_weighted


def write(j, a, r):
    return (r + j - a) % 3


def inverse(j, a, r):
    return (r - j + a) % 3


def registers(brc):
    for j, a, r in product(range(3), repeat=3):
        assert inverse(j, a, write(j, a, r)) == r
        assert write(j, a, write(j, a, write(j, a, r))) == r
    for a, x, y in product(range(3), repeat=3):
        r = write(x, a, a)
        c = write(r, a, a)
        assert inverse(c, a, r) == a and c == x
        assert inverse(y, a, r) == (a + x - y) % 3
    detached_histories = 0
    for L in range(5):
        for a, x in product(range(3), repeat=2):
            for path in product(range(3), repeat=L):
                state = (x, a, write(x, a, a))
                for next_source in path:
                    state = (next_source, state[1], state[2])
                    assert state == (next_source, a, x)
                detached_histories += 1
    sequences = 0
    first_terminal_blind = None
    for N in range(1, 6):
        for deltas in product(range(3), repeat=N):
            a, r = 2, 2
            errors = []
            previous = 0
            for t, delta in enumerate(deltas):
                x = (t + 1) % 3
                r = write(x, a, r)
                c = write(r, a, (a + delta) % 3)
                r = inverse(c, a, r)
                errors.append((c - x) % 3)
                assert (r - a) % 3 == -delta % 3
                assert errors[-1] == (delta - previous) % 3
                previous = delta
            assert sum(errors) % 3 == deltas[-1]
            if any(errors) and r == a and first_terminal_blind is None:
                first_terminal_blind = (deltas, errors)
            sequences += 1
    assert first_terminal_blind == ((1, 0), [1, 2])
    # Full histories receive one shared positive mass, with no independence needed.
    keys = list(product(range(3), repeat=5))   # a, x, next source, receiver error, copy-port error
    total_weight = sum(range(1, len(keys) + 1))
    pool = defaultdict(lambda: brc.CWM_ZERO)
    unit = brc.cwm_edge(1)
    for index, (a, x, z, eps, delta) in enumerate(keys, 1):
        r = write(x, a, (a + eps) % 3)
        c = write(r, a, (a + delta) % 3)
        r = inverse(c, a, r)
        next_record = write(z, a, r)
        passed = (c == x, next_record == z)
        assert passed == ((eps + delta) % 3 == 0, delta == 0)
        w = brc.cwm_edge(Fraction(index, total_weight))
        for _ in range(4):
            w = brc.cwm_propagate(w, unit)
        pool[passed] = brc.cwm_recoalesce(pool[passed], w)
    assert sum(v.total for v in pool.values()) == 1
    assert sum(v.count for v in pool.values()) == 243
    return {"original_E_inputs": 27, "prepared_old_new_reference_triples": 27,
            "detached_label_histories_lengths_zero_to_four": detached_histories,
            "copy_port_error_words_lengths_one_to_five": sequences,
            "minimal_hidden_faults_then_correct_final_preparation": first_terminal_blind,
            "symbolic_fault_worlds": len(keys), "frozen_positive_weight_core_only": True,
            "old_and_next_correct_counts_and_masses":
            {str(k): [v.count, str(v.total)] for k, v in sorted(pool.items())},
            "minimal_extra_enabled_write": [0, 1, 2],
            "stale_inverse_source_example_relative_ready_error": inverse(1, 0, 0)}


def cyclic_tables():
    checked = 0
    hidden_checks = 0
    samples = []
    for m in range(2, 17):
        for h in range(1, m + 1):
            if m % h:
                continue
            for u in range(m):
                arrivals = Counter({x: 1 for x in range(m)})
                rows = []
                permitted = set(range(0, m, h))
                for i in range(1, 5):
                    old_states = set(arrivals)
                    next_counts = Counter()
                    preds = defaultdict(set)
                    for x, multiplicity in arrivals.items():
                        for eta in permitted:
                            y = (u * x + eta) % m
                            next_counts[y] += multiplicity
                            preds[y].add(x)
                    K = gcd(h, u**i) * (m // h)**i
                    assert set(next_counts.values()) == {K}
                    assert len(next_counts) * K == m * len(permitted)**i
                    undetected = {e for e in old_states if u * e % m in permitted}
                    for y, choices in preds.items():
                        base = min(choices)
                        assert {(x - base) % m for x in choices} == undetected
                    hidden_checks += len(preds)
                    rows.append([len(next_counts), len(undetected), K])
                    arrivals = next_counts
                    checked += 1
                if (m, h, u) in ((3, 1, 1), (3, 3, 1), (9, 9, 3), (12, 4, 2)):
                    samples.append({"m": m, "h": h, "u": u, "image_predecessors_history": rows})
    return {"m_range": [2, 16], "depth_range": [1, 4], "all_divisors_h_all_u": True,
            "parameter_layers": checked, "endpoint_cosets_checked": hidden_checks, "examples": samples}


def codec(states, innovation, step, N):
    # Explicit histories are state paths; the innovation is uniquely found from adjacent states.
    paths = {(x,): 0 for x in states}
    old_size = 1
    rows = []
    for i in range(1, N + 1):
        S = {history[-1] for history in paths}
        pre = defaultdict(set)
        for x in S:
            for eta in innovation:
                pre[step(x, eta)].add(x)
        preds = {y: sorted(xs) for y, xs in pre.items()}
        slots = {y: {x: j for j, x in enumerate(xs)} for y, xs in preds.items()}
        next_paths = {}
        for history, code in paths.items():
            x = history[-1]
            for eta in innovation:
                y = step(x, eta)
                word = history + (y,)
                assert word not in next_paths
                next_paths[word] = code + old_size * slots[y][x]
        groups = defaultdict(dict)
        for history, code in next_paths.items():
            y = history[-1]
            assert code not in groups[y]
            groups[y][code] = history
            quotient, prior = divmod(code, old_size)
            assert preds[y][quotient] == history[-2] and paths[history[:-1]] == prior
        new_size = len(next(iter(groups.values())))
        assert all(set(codes) == set(range(new_size)) for codes in groups.values())
        assert len(next_paths) == len(states) * len(innovation)**i
        for budget in {1, max(1, new_size // 3), new_size, new_size + 1}:
            correct = sum(len({c % budget for c in codes}) for codes in groups.values())
            assert correct == len(pre) * min(budget, new_size)
        rows.append({"i": i, "reachable_endpoints": len(pre),
                     "indices_per_endpoint": new_size, "histories": len(next_paths)})
        paths, old_size = next_paths, new_size
    return rows


def multiples(x, c, moduli):
    return tuple(c * a % m for a, m in zip(x, moduli))


def elements(moduli):
    return list(product(*(range(m) for m in moduli)))


def subgroups(moduli):
    all_elements = elements(moduli)
    zero = (0,) * len(moduli)
    base = frozenset([zero])
    result = {base}
    frontier = [base]
    while frontier:
        H = frontier.pop()
        for x in all_elements:
            if x in H:
                continue
            union = set(H)
            y = x
            while y not in H:
                union.update(tuple((i + j) % m for i, j, m in zip(y, v, moduli)) for v in H)
                y = tuple((i + j) % m for i, j, m in zip(y, x, moduli))
            new = frozenset(union)
            if new not in result:
                frontier.append(new)
                result.add(new)
    return sorted(result, key=lambda H: (len(H), sorted(H)))


def primes(n):
    return [p for p in range(2, n + 1) if n % p == 0 and all(p % q for q in range(2, p))]


def additive_bound(moduli, K):
    A = set(elements(moduli))
    zero = (0,) * len(moduli)
    value = 1
    for p in primes(prod(moduli)):
        S = {v for v in K if multiples(v, p, moduli) == zero}
        layer = A
        while True:
            value *= len(S & layer)
            next_layer = {multiples(v, p, moduli) for v in layer}
            if next_layer == layer:
                break
            layer = next_layer
    return value


def additive_audit():
    rows = []
    for moduli in [(3, 3), (9,), (9, 3), (8, 4), (4, 4, 2), (6, 6)]:
        groups = subgroups(moduli)
        A_size = prod(moduli)
        strict = []
        for K in groups:
            optimum = min(A_size // len(L) for L in groups if len(K & L) == 1)
            assert optimum == additive_bound(moduli, K)
            if optimum > len(K):
                strict.append((len(K), optimum))
        rows.append({"A_moduli": moduli, "subgroups_checked": len(groups),
                     "strict_kernel_size_additive_size_multiplicity":
                     [[k, m, n] for (k, m), n in sorted(Counter(strict).items())]})
    counts = 0
    for m in range(2, 41):
        for u in range(m):
            for N in (1, 2, 3):
                g = gcd(m, u**N)
                choices = [b for b in range(1, m + 1) if m % b == 0 and
                           len({(pow(u, N, m) * j % m, j % b) for j in range(m)}) == m]
                exact = 1
                for p in primes(g):
                    q = m
                    while q % p == 0:
                        exact *= p
                        q //= p
                assert min(choices) == exact
                counts += 1
    return {"all_subgroups": rows, "cyclic_deterministic_parameters": counts}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path)
    brc = source(parser.parse_args().repo)
    noninvariant = codec(range(8), [0, 2], lambda x, eta: (x >> 1) ^ eta, 6)
    assert all(r["indices_per_endpoint"] == 2**(r["i"] + 1) for r in noninvariant)
    output = {"public_git_blobs": PINS, "registers": registers(brc), "cyclic_source": cyclic_tables(),
              "online_codec_Z12_u2_H4": codec(range(12), range(0, 12, 4),
                                                lambda x, eta: (2*x + eta) % 12, 5),
              "online_codec_F2_cubed_shift_H_middle": noninvariant,
              "additive": additive_audit()}
    print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
