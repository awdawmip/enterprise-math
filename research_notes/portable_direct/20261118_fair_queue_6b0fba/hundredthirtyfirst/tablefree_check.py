"""Exact fixed-degree gate for chains of the pinned BRC table-free transport."""
import argparse
from collections import Counter
from dataclasses import dataclass
from hashlib import sha1
from importlib import import_module
from itertools import combinations_with_replacement, product
import json
from math import comb, gcd, isqrt
from pathlib import Path
import sys
from types import FunctionType


SOURCE_BLOB = "aaef03c9d8e68de5ace75b6736d1169faa4b2918"
SOURCE_PATH = Path("src/enterprise_math/brc_table_free_tail.py")


def source_module(repo):
    raw = (repo / SOURCE_PATH).read_bytes()
    blob = sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    if blob != SOURCE_BLOB:
        raise ValueError(f"Expected {SOURCE_BLOB}; read {blob} from {repo / SOURCE_PATH}")
    sys.path.insert(0, str((repo / "src").resolve()))
    module = import_module("enterprise_math.brc_table_free_tail")
    if Path(module.__file__).resolve() != (repo / SOURCE_PATH).resolve():
        raise RuntimeError("The imported source differs from the checked file")
    return module


@dataclass(frozen=True)
class State:
    n: int
    multiplier: int
    root: int
    remainder: int


def true_state(n, m):
    j = isqrt(m * n)
    return State(n, m, j, m * n - j * j)


def power_for_setup(base, exponent, ledger):
    value = pow(base, exponent)
    ledger["setup_integer_powers"] += 1
    ledger["largest_setup_power_bits"] = max(ledger["largest_setup_power_bits"], value.bit_length())
    return value


def integer_root(value, degree, ledger):
    lo, hi = 0, 1 << ((value.bit_length() + degree - 1) // degree)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if power_for_setup(mid, degree, ledger) <= value:
            lo = mid
        else:
            hi = mid
    return lo


@dataclass(frozen=True)
class Gate:
    n: int
    step: int
    degree: int
    candidate: int
    first: int

    def lane(self, residue):
        return self.first + (residue - self.first) % self.step


def chain_gate(n, h, k, ledger):
    if n < 1 or h not in (1, 2) or k < 2 or k % 2:
        raise ValueError("Invalid integer, step or even order")
    catalan = comb(2 * k, k) // (k + 1)
    p = 2 * power_for_setup(4, k, ledger)
    q = catalan * power_for_setup(h, k + 1, ledger)
    a = gcd(p, q)
    p, q = p // a, q // a
    b = integer_root((n * q * q) // (p * p), 2 * k + 1, ledger)
    m = max(h, b + 1)
    numerator = p * power_for_setup(m, k, ledger) * (2 * m - h)
    endpoint = numerator // (2 * q)
    tested = m * n < (endpoint + 1) ** 2
    ledger["setup_catalans"] += 1
    ledger["setup_endpoint_tests"] += 1
    return Gate(n, h, k, m, m if tested else m + 1)


def instrumented_transport(module, gate, ledger, use_gate):
    """Retain the pinned transport bytecode and all source-state and output checks."""
    original = module.transport_certified_tail
    env = original.__globals__.copy()

    def certificate(j, m, h, k):
        if (h, k) != (gate.step, gate.degree):
            raise ValueError("This gate belongs to another fixed step or degree")
        if use_gate:
            ledger["threshold_comparisons"] += 1
            return m >= gate.first
        ledger["source_certificate_calls"] += 1
        return module.two_correction_certificate(j, m, h, k)

    def increment(j, m, h, k):
        ledger["source_horner_calls"] += 1
        return module.lower_increment(j, m, h, k)

    env.update(two_correction_certificate=certificate, lower_increment=increment)
    fn = FunctionType(original.__code__, env, original.__name__, original.__defaults__)
    fn.__kwdefaults__ = original.__kwdefaults__

    def advance(state):
        if state.n != gate.n:
            raise ValueError("This threshold belongs to a different N")
        target = fn(state, state.multiplier + gate.step, degree=gate.degree)
        ledger["odd_width_corrections"] += target.correction_steps
        return target

    return advance


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def small_exhaustion(module):
    primes = [p for p in range(3, 192, 2) if prime(p)]
    checked, chains, decisions, shifted_early = 0, 0, Counter(), Counter()
    for p, q in combinations_with_replacement(primes, 2):
        n = p * q
        for h, k in product((1, 2), (2, 4, 6, 8, 12, 16)):
            gate = chain_gate(n, h, k, Counter())
            decisions[gate.first - gate.candidate] += 1
            d = 2*k+1
            a, b = 2*4**k, (comb(2*k,k)//(k+1))*h**(k+1)
            m = gate.candidate
            first_shift = m if a*a*(d*m-h)**d > n*b*b*d**d else m+1
            assert gate.first-first_shift in (0,1)
            shifted_early[f"k{k}_h{h}"] += gate.first-first_shift
            for m in range(h, gate.first + 6):
                j = isqrt(m * n)
                assert module.two_correction_certificate(j, m, h, k) == (m >= gate.first)
                checked += 1
            chains += 1
    return dict(odd_primes=len(primes),semiprimes=len(primes)*(len(primes)+1)//2,
                parameter_triples=chains,native_certificates=checked,integer_skips=dict(decisions),
                shifted_guess_early_by_parameter=dict(shifted_early))


def production_case(module, p, q, h, k, steps):
    assert prime(p) and prime(q)
    setup = Counter()
    n = p * q
    gate = chain_gate(n, h, k, setup)
    original, optimized = Counter(), Counter()
    reference = instrumented_transport(module, gate, original, False)
    candidate = instrumented_transport(module, gate, optimized, True)
    past_setup = []
    for residue in range(h):
        first = gate.lane(residue)
        if first - h >= h:
            before = true_state(n, first - h)
            for advance in (reference, candidate):
                try:
                    advance(before)
                except ValueError as e:
                    assert str(e) == "declared degree does not certify the two-correction tail at this state"
                else:
                    raise AssertionError("Failed to reject the last uncertified state")
        a = b = true_state(n, first)
        for _ in range(steps):
            a, b = reference(a), candidate(b)
            assert a == b
            truth = true_state(n, a.multiplier)
            assert (a.root, a.remainder) == (truth.root, truth.remainder)
        past_setup.append(dict(residue=residue,first=first,stop=a.multiplier,
                               final_root=a.root,final_remainder=a.remainder))
    assert original["source_horner_calls"] == optimized["source_horner_calls"] == h*steps
    assert original["odd_width_corrections"] == optimized["odd_width_corrections"]
    return dict(factors=[p,q], n=n, step=h, degree=k, initial_integer_candidate=gate.candidate,
                first_integer=gate.first, original=dict(original),optimized=dict(optimized),
                setup=dict(setup),lanes=past_setup)


def rare_witnesses(module):
    rows = []
    for p, q, h, m in [(5,941,1,2),(7,67,2,3)]:
        assert prime(p) and prime(q)
        k, d = 2, 5
        a, b = 16,h**3   # A=16/h^3 at k=2
        floor_d = a*m**k*(2*m-h)//(2*b)
        true_num, true_den = (floor_d+1)**2,m
        approx_num, approx_den = a*a*(d*m-h)**d, b*b*d**d
        first = (true_num+true_den-1)//true_den
        last = (approx_num-1)//approx_den
        n = p*q
        assert first <= n <= last
        assert not module.two_correction_certificate(isqrt(n*m),m,h,k)
        assert chain_gate(n,h,k,Counter()).first == m+1
        rows.append(dict(factors=[p,q],step=h,degree=k,integer_interval=[first,last],
                         shifted_first=m,certified_first=m+1))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, help="checkout containing the pinned source")
    args = parser.parse_args()
    repo = args.repo
    if repo is None:
        candidates = [Path.cwd(), *Path(__file__).resolve().parents, Path("/workspace/enterprise-math")]
        repo = next((root for root in candidates if (root / SOURCE_PATH).is_file()), None)
    if repo is None:
        parser.error("Use --repo to point at a checkout containing the source")
    module = source_module(repo)
    small = small_exhaustion(module)
    witnesses = []
    for q in (22433, 20743, 78737, 67057):
        assert prime(q)
        gates = [chain_gate(3*q,h,2,Counter()) for h in (1,2)]
        witnesses.append(dict(factors=[3,q],candidate_and_first=[[g.candidate,g.first] for g in gates]))
    assert {tuple(b-a for a,b in row["candidate_and_first"]) for row in witnesses} == set(product((0,1),repeat=2))
    # Compare both paths on each predeclared source program and charge gate setup once per (N,h,k).
    cases = [production_case(module,p,q,h,k,128)
             for p,q in [(3,67057),(1009,10007),(1000003,1000033),(2147483629,2147483647)]
             for h,k in product((1,2),(2,4,8,16))]
    totals={key:dict(sum((Counter(v[key]) for v in cases),Counter())) for key in ('original','optimized')}
    setup=Counter()
    for v in cases:
        for key,count in v['setup'].items():
            if key=='largest_setup_power_bits':
                setup[key]=max(setup[key],count)
            else:
                setup[key]+=count
    print(json.dumps(dict(source_git_blob=SOURCE_BLOB,census=small,two_step_examples=witnesses,
                          production_cases=cases,shift_misses=rare_witnesses(module),
                          source_path=str(SOURCE_PATH),production_totals=totals,
                          setup_totals=dict(setup)),sort_keys=True,indent=2))


if __name__ == "__main__":
    main()
