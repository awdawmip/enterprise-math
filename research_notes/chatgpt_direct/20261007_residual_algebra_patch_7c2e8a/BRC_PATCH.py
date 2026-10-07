"""Verbatim CWM function/class source slices fetched via GitHub.fetch_file.
Source: awdawmip/enterprise-math@a1033e7057c7ebed3ef221d60935e9dadb9eea86
Path: src/enterprise_math/brc_weighted.py
Returned source Git blob: 3f205696709e847909958a153f8fe10d3f6b70f0
Only required definitions are loaded; this is not a full-package import/test.
Relative logarithm/exact-arithmetic dependencies are unused and not loaded.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
RationalInput = int | Fraction


def _fraction(value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("weight must be an int or Fraction")
    return Fraction(value)


def _positive_fraction(name: str, value: RationalInput) -> Fraction:
    result = _fraction(value)
    if result <= 0:
        raise ValueError(f"{name} must be positive")
    return result


@dataclass(frozen=True)
class CWMState:
    """Count / total-mass / dominant-mass state for positive weighted paths.

    ``count`` records supported path multiplicity. ``total`` is the sum of path
    weights and ``dominant`` is the largest individual path weight.

    The constructor accepts the closed algebraic CWM envelope.  Use
    :func:`is_positive_path_realizable` when exact finite positive-path
    realizability is required.
    """

    count: int
    total: Fraction
    dominant: Fraction

    def __post_init__(self) -> None:
        if isinstance(self.count, bool) or not isinstance(self.count, int) or self.count < 0:
            raise ValueError("count must be a non-negative integer")
        if not isinstance(self.total, Fraction) or not isinstance(self.dominant, Fraction):
            raise TypeError("total and dominant must be Fraction values")
        if self.count == 0:
            if self.total != 0 or self.dominant != 0:
                raise ValueError("zero count requires zero total and dominant mass")
            return
        if self.total <= 0 or self.dominant <= 0:
            raise ValueError("live CWM state requires positive total and dominant mass")
        if self.dominant > self.total:
            raise ValueError("dominant path mass cannot exceed total path mass")
        if self.total > self.count * self.dominant:
            raise ValueError("total path mass cannot exceed count times dominant mass")

    @property
    def live(self) -> bool:
        return self.count > 0


CWM_ZERO = CWMState(0, Fraction(0, 1), Fraction(0, 1))
CWM_ONE = CWMState(1, Fraction(1, 1), Fraction(1, 1))


def cwm_edge(weight: RationalInput) -> CWMState:
    """Lift one positive edge/path weight to ``(1,a,a)``."""
    value = _positive_fraction("weight", weight)
    return CWMState(1, value, value)


def cwm_recoalesce(left: CWMState, right: CWMState) -> CWMState:
    """Alternative-branch recoalescence: ``(+,+,max)``."""
    if not left.live:
        return right
    if not right.live:
        return left
    return CWMState(
        left.count + right.count,
        left.total + right.total,
        max(left.dominant, right.dominant),
    )


def cwm_propagate(left: CWMState, right: CWMState) -> CWMState:
    """Serial path propagation: componentwise multiplication."""
    if not left.live or not right.live:
        return CWM_ZERO
    return CWMState(
        left.count * right.count,
        left.total * right.total,
        left.dominant * right.dominant,
    )


"""Typed positive-BRC chronological-subsequence observer; no physical dynamics.

Population: ordered selections of 0..d occurrence indices of a declared native
signed-axis word. Each index-selection branch has weight exactly 1. Ports carry
signed-axis LABELS, never negative branch mass. Full words remain evidence.
Future language for the quotient: word concatenation and these bounded-degree
count/endpoint/antisymmetric-order observers only. No force law is inferred.
"""
import hashlib
import json
from itertools import combinations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CALLS = dict(edge=0, propagate=0, recoalesce=0)
CHECKS = 0
PAIRS = tuple(combinations(range(6), 2))
PORTS = tuple(range(1, 7)) + tuple(range(-1, -7, -1))

def check(ok):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(f'check {CHECKS} failed')

def edge():
    CALLS['edge'] += 1
    return cwm_edge(1)

def add(a, b):
    CALLS['recoalesce'] += 1
    return cwm_recoalesce(a, b)

def mul(a, b):
    CALLS['propagate'] += 1
    return cwm_propagate(a, b)

def concat(a, b, degree=2):
    """Truncated CWM-coefficient noncommutative convolution."""
    out = {}
    for u, cu in a.items():
        for v, cv in b.items():
            if len(u) + len(v) <= degree:
                key = u + v
                out[key] = add(out.get(key, CWM_ZERO), mul(cu, cv))
    return out

def signature(word, degree=2):
    out = {(): CWM_ONE}
    for letter in word:
        if letter not in PORTS:
            raise ValueError('expected a signed native-axis port')
        out = concat(out, {(): CWM_ONE, (letter,): edge()}, degree)
    return out

def signed_sectors(sig):
    """Positive and negative occurrence counts stay separately available."""
    zplus, zminus = [0] * 6, [0] * 6
    op, om = [0] * 15, [0] * 15
    pair_index = {pair: k for k, pair in enumerate(PAIRS)}
    for letters, value in sig.items():
        count = value.count
        check(value.total == count and value.dominant == 1)
        if len(letters) == 1:
            x = letters[0]
            (zplus if x > 0 else zminus)[abs(x)-1] += count
        elif len(letters) == 2:
            x, y = letters
            i, j = abs(x)-1, abs(y)-1
            if i != j:
                sign = (1 if x*y > 0 else -1) * (1 if i < j else -1)
                k = pair_index[tuple(sorted((i, j)))]
                (op if sign > 0 else om)[k] += count
    return zplus, zminus, op, om

def readout(sig):
    zp, zm, op, om = signed_sectors(sig)
    return tuple(a-b for a, b in zip(zp, zm)), tuple(a-b for a, b in zip(op, om))

def wedge(z, w):
    """Signed observer law proved from the preserved occurrence departments."""
    return tuple(z[i]*w[j]-z[j]*w[i] for i, j in PAIRS)

def lifted(a, b):
    z, omega = a
    w, eta = b
    return tuple(x+y for x, y in zip(z, w)), tuple(x+y+c for x, y, c in zip(omega, eta, wedge(z, w)))

def evidence(word, degree=2):
    sig = signature(word, degree)
    z, om = readout(sig)
    return {
        'word': list(word), 'z': list(z), 'omega': list(om),
        'signed_sectors': signed_sectors(sig),
        'coefficients': [{'letters': list(k), 'C': v.count, 'W': str(v.total), 'M': str(v.dominant)} for k, v in sorted(sig.items())],
    }

def main():
    # Complete enumeration of signed-axis words of length <=3, with all cuts.
    # This is finite combinatorics, not full-X6 or physical validation.
    enumerated = cuts = 0
    for n in range(4):
        for word in product(PORTS, repeat=n):
            full = signature(word)
            obs = readout(full)
            enumerated += 1
            z, om = obs
            check(all((om[t]-z[i]*z[j]) % 2 == 0 for t, (i,j) in enumerate(PAIRS)))
            for k in range(n+1):
                left, right = signature(word[:k]), signature(word[k:])
                check(concat(left, right) == full)
                check(lifted(readout(left), readout(right)) == obs)
                cuts += 1
    units = [signature((p,)) for p in PORTS]
    assoc = 0
    for a, b, c in product(units, repeat=3):
        check(concat(concat(a, b), c) == concat(a, concat(b, c)))
        aa, bb, cc = readout(a), readout(b), readout(c)
        check(lifted(lifted(aa, bb), cc) == lifted(aa, lifted(bb, cc)))
        assoc += 1
    examples = {name: evidence(word) for name, word in {
        'i_then_j': (1, 2), 'j_then_i': (2, 1),
        'loop': (1, 2, -1, -2), 'idle': (),
        '1122': (1, 1, 2, 2), '1212': (1, 2, 1, 2),
        'backtrack': (1, -1),
    }.items()}
    a, b = examples['i_then_j'], examples['j_then_i']
    check(a['z'] == b['z'] and a['omega'][0] == 1 and b['omega'][0] == -1)
    check(examples['loop']['z'] == [0]*6 and examples['loop']['omega'][0] == 2)
    check(examples['1122']['omega'][0] == 4 and examples['1212']['omega'][0] == 2)
    # Coarsening Omega alone is not closed: append the SAME axis to equal Omega.
    p, q, r = (), (1,), (2,)
    check(readout(signature(p))[1] == readout(signature(q))[1])
    check(readout(signature(p+r))[1] != readout(signature(q+r))[1])
    # Even full (z,Omega) is not safe for an observer that sees path length.
    check(readout(signature(())) == readout(signature((1,-1))))
    # For degree-three observer, even all exact degree<=2 port counts can fail.
    # 1221 and 2112 have identical single and pair counts but distinct triple counts.
    p, q = (1,2,2,1), (2,1,1,2)
    check(signature(p, 2) == signature(q, 2))
    check(signature(p, 3) != signature(q, 3))
    examples['same_degree2_a'] = evidence(p, 3)
    examples['same_degree2_b'] = evidence(q, 3)
    # Actual step-norm counts are not executed: q is unchanged definitionally.
    results = dict(
        status='FINITE_TYPED_BRC_INTERFACE_CHECK_NOT_NATIVE_DYNAMICS',
        kernel_source=dict(repository='awdawmip/enterprise-math', ref='a1033e7057c7ebed3ef221d60935e9dadb9eea86', path='src/enterprise_math/brc_weighted.py', git_blob='3f205696709e847909958a153f8fe10d3f6b70f0', load='VERBATIM_FUNCTION_CLASS_SLICES_NOT_FULL_PACKAGE'),
        observer='order<=2 signed-port subsequence CWM, z, Omega',
        future_scope='concatenation; no hidden-state/force/physical response',
        words_enumerated=enumerated, all_cuts=cuts, unit_triples=assoc,
        assertions=CHECKS, brc_calls=CALLS, examples=examples,
        no_physical_five_axis_coupling_proved=True,
        no_minimal_perturbation_principle_proved=True,
        no_foundation_or_worldview_changed=True,
    )
    data = (json.dumps(results, ensure_ascii=False, sort_keys=True, indent=2)+'\n').encode()
    (ROOT/'results.json').write_bytes(data)
    print(json.dumps({k: results[k] for k in ['status','words_enumerated','all_cuts','unit_triples','assertions','brc_calls']},indent=2))
    print('results_sha256', hashlib.sha256(data).hexdigest())

if __name__ == '__main__':
    main()
