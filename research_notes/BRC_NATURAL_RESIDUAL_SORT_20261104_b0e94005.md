# 自然数上的 BRC 算术残差与排序：保序分解和稳定逐层分桶

Progress-Event-ID: `brc-natural-residual-sort-20261104-b0e94005`
At: `2026-11-04T11:01:43Z`
Status: research note; derivation and executed prototype; no formal theorem admission or novelty claim.
Conversation: `chat-brc-sort-b0e94005ad9c-20261103`
Researcher-ID: unconfirmed. Research-Activity-ID: unconfirmed.
Scientific source: `awdawmip/enterprise-math@82205c53d6ae2c00213796b7c138d398b198e51a`.
Global read snapshot: `2827dbd8bdd216a1135fade833ca64144cd0c526`, verified 2026-11-04 10:58 UTC.

## 1. Current scope

The user's latest instruction is “不对 先研究自然数”. The continuing question is whether BRC residual sorting can be implemented. This note studies a finite list of arbitrary natural numbers, with 100 entries as the requested instance. Values need not be consecutive, bounded by 100, or distinct. We use natural numbers including zero; the positive-natural restriction is an immediate subcase.

This is a proposed concrete interpretation of “residual”: the existing arithmetic collapse remainder. It is not an assumption that all BRC residual notions are interchangeable. Earlier comparison-rank/CWM constructions are not used to obtain the order here.

## 2. Reused sources and semantic scope

The following existing implementation is reused without functional changes:

- [core.py](https://github.com/awdawmip/enterprise-math/blob/82205c53d6ae2c00213796b7c138d398b198e51a/src/enterprise_math/core.py): integer_nth_root and perfect-power collapse.
- [division.py](https://github.com/awdawmip/enterprise-math/blob/82205c53d6ae2c00213796b7c138d398b198e51a/src/enterprise_math/division.py): Euclidean state and same-space multiple collapse.
- [exact_arithmetic.py](https://github.com/awdawmip/enterprise-math/blob/82205c53d6ae2c00213796b7c138d398b198e51a/src/enterprise_math/exact_arithmetic.py): BRCDivisionTrace, BRCRootTrace, brc_evaluate_division and brc_evaluate_root.

Runtime reuse state: REUSE_EXECUTED. The local copies equal the current source except for an extra trailing newline. The facade calls the repository's integer arithmetic primitives and retains its defined exact traces. This is not a claim of an independent native-X6 realization or of a new BRC theorem. CWM weighted multiplicity surplus is a different typed quantity and is not used.

## 3. First mathematical result: residual plus collapse coordinate preserves order

### Fixed-divisor case

Fix a common integer b >= 2. Every natural x has the unique state

    x = b*q(x) + r(x),    0 <= r(x) < b.

Its same-space collapse is C_b(x)=b*q(x), and the remainder is r(x)=x-C_b(x). These are precisely the fields retained by the existing division trace.

For natural x,y:

    x < y iff q(x) < q(y)
               or [q(x) = q(y) and r(x) < r(y)].

Proof: if q(x)<q(y), then
x <= b*q(x)+b-1 < b*(q(x)+1) <= b*q(y) <= y.
For equal quotients the common term cancels. Conversely q(x)>q(y) implies x>y by the same argument, and equal quotients reduce to residual comparison.

Thus the pair (q,r), with lexicographic order, is an order embedding. Residual alone is only a within-basin coordinate: for b=2, 5 has remainder 1 and 6 remainder 0. Equal values retain multiplicity and can be distinguished by original token index for stability.

### Square-collapse case

The existing root trace gives

    k(x)^2 <= x < (k(x)+1)^2,
    x = k(x)^2 + r_square(x),    0 <= r_square(x) <= 2*k(x).

Then x<y iff (k(x),r_square(x)) is lexicographically smaller than the corresponding pair for y. Different k identify disjoint ordered intervals; within one interval the common square cancels.

Example: 15 -> (3,6), 16 -> (4,0). This specifically refutes sorting arbitrary naturals by square residual alone. It does not rule out sorting with the retained basin coordinate or a different residual construction. The proof is a direct elementary consequence of the source definitions, not a claim of novelty.

## 4. Executable construction: stable binary residual passes

For each token keep its original index i and its current natural state q_i^(0)=a_i. At pass t, call the existing BRC division facade:

    q_i^(t) = 2*q_i^(t+1) + r_i^(t),    r_i^(t) in {0,1}.

Append tokens to residual-0 and residual-1 buckets in their current order; concatenate bucket 0 then bucket 1. Continue until all current quotients are zero. The original input values are retained for output.

After t passes, tokens are ordered by their original values modulo 2^t, with ties in their original input order. Induction: the next residual is the new more significant digit, and stable bucketing preserves the already ordered lower t digits within equal new residuals. At L=max_i bit_length(a_i), every a_i<2^L, so residue order is full numerical order. Empty/all-zero lists require zero passes and already satisfy the output condition.

This is the classical stable LSD binary radix construction executed through the existing arithmetic BRC facade. It does not compare pairs of input values to determine their rank. Its applicability follows from natural numbers having a finite binary expansion; no distribution assumption is needed.

Let m be input length and L=bit_length(max input), taking L=0 for empty/all-zero input. The program executes exactly m*L facade division calls; there are O(m*L) token/bucket operations under a unit-cost arithmetic model, and O(m) auxiliary token records. For arbitrary-size Python integers, division, arithmetic and the retained integer payloads have size-dependent cost, so these are not bounds independent of input bit length. No speed superiority over built-in comparison sorting is established.

## 5. Complete prototype

Save this block as natural_residual_sort.py with the Enterprise Math package available.

```python
"""Natural-number residual sorting through the existing BRC division facade.

Research prototype. No claim of a new sorting family or native X6 semantics.
"""
from enterprise_math.exact_arithmetic import division, brc_evaluate_division


def natural_residual_order(values):
    """Return stable source indices and the executed division-call count."""
    values = list(values)
    if any(isinstance(x, bool) or not isinstance(x, int) or x < 0
           for x in values):
        raise ValueError("values must be non-negative integers")

    states = [(i, x) for i, x in enumerate(values)]
    calls = 0
    while any(q != 0 for _, q in states):
        buckets = [[], []]
        for i, q in states:
            trace = brc_evaluate_division(division(q, 2))
            calls += 1
            buckets[trace.remainder].append((i, trace.quotient))
        states = buckets[0] + buckets[1]
    return [i for i, _ in states], calls


def natural_residual_sort(values):
    values = list(values)
    order, _ = natural_residual_order(values)
    return [values[i] for i in order]
```

## 6. Executed validation

Executed in the local Python runtime on 2026-11-04 using the canonical modules identified above. Exit code 0.

- 1,093 exhaustive arrays over {0,1,2}, of lengths 0 through 6.
- 100 generated arrays of exactly 100 naturals, cycling 4,12,64,128-bit ranges; seed 20261104; intentional duplicates and zeros.
- Seven edge cases, including empty/all-zero/all-equal/sorted/reversed lists, 512-bit values, and square-boundary values.
- Expected stable token order checked against a separate sorting oracle; exact division-call count checked.
- Negative, floating-point and Boolean input rejection checked.
- Fifteen root-boundary values checked for exact reconstruction, residual range and pair order; the 15/16 reversal of residual-only order checked.

Actual receipt:

```json
{
  "exhaustive_natural_arrays": 1093,
  "random_arrays_of_100": 100,
  "edge_cases": 7,
  "total_stable_sort_checks": 1200,
  "invalid_input_checks": 3,
  "root_boundary_states": 15,
  "example": [
    42,
    7,
    103,
    42,
    18,
    0
  ],
  "stable_order": [
    5,
    1,
    4,
    0,
    3,
    2
  ],
  "sorted": [
    0,
    7,
    18,
    42,
    42,
    103
  ],
  "division_calls": 42,
  "result": "PASS"
}
```

Reproducible validation script, saved beside the prototype:

```python
from itertools import product
from random import Random
from enterprise_math.exact_arithmetic import root, brc_evaluate_root
from natural_residual_sort import natural_residual_order, natural_residual_sort

checked = 0
def check(a):
    global checked
    order, calls = natural_residual_order(a)
    expected = sorted(range(len(a)), key=lambda i: (a[i], i))
    assert order == expected, (a, order, expected)
    levels = max(a, default=0).bit_length()
    assert calls == len(a) * levels
    checked += 1

exhaustive = 0
for length in range(7):
    for a in product((0, 1, 2), repeat=length):
        check(a)
        exhaustive += 1

rng = Random(20261104)
for t in range(100):
    bits = (4, 12, 64, 128)[t % 4]
    a = [rng.getrandbits(bits) for _ in range(100)]
    a[20] = a[5]
    a[40] = 0
    check(a)

edges = [
    [], [0] * 100, [1] * 100,
    list(range(100)), list(range(99, -1, -1)),
    [2**512, 2**512 - 1, 0, 2**512, 1],
    [16, 15, 25, 24, 81, 80, 1001, 1000, 0, 16],
]
for a in edges:
    check(a)

for bad in ([-1], [1.0], [True]):
    try:
        natural_residual_sort(bad)
    except ValueError:
        pass
    else:
        raise AssertionError(("invalid input accepted", bad))

root_values = (0, 1, 2, 3, 4, 8, 9, 15, 16, 24, 25, 80, 81, 1000, 1001)
root_states = []
for x in root_values:
    trace = brc_evaluate_root(root(x, 2))
    k, r = trace.root_index, trace.remainder
    assert x == k*k+r and 0 <= r <= 2*k
    root_states.append((k,r))
assert root_states == sorted(root_states)
assert brc_evaluate_root(root(15, 2)).remainder == 6
assert brc_evaluate_root(root(16, 2)).remainder == 0

example = [42, 7, 103, 42, 18, 0]
order, calls = natural_residual_order(example)
print({
    "exhaustive_natural_arrays": exhaustive,
    "random_arrays_of_100": 100,
    "edge_cases": len(edges),
    "total_stable_sort_checks": checked,
    "invalid_input_checks": 3,
    "root_boundary_states": len(root_values),
    "example": example,
    "stable_order": order,
    "sorted": natural_residual_sort(example),
    "division_calls": calls,
    "result": "PASS",
})
```

The sorting oracle is an independent validation reference, not the algorithm implementation. Finite tests support implementation behavior on the stated inputs; the order and termination arguments above establish the all-natural mathematical construction.

## 7. Registration state and remaining research

Ordinary research reporting and draft preservation follow docs/PORTABLE_RESEARCH_PROTOCOL.md. No shared task CLAIM, Result, Review, admission, or formal completion is asserted.

The original session-start request was not successfully published to Source. The exact canonical session-record path remains 404 at this read snapshot. An attempted reconciliation on [bridge issue #6652](https://github.com/awdawmip/kimi-query-bridge/issues/6652#issuecomment-6628983408), request brc-natural-sort-20261104-b0e94005-reconcile, returned matched terminal FAILED / NOT_RECONCILABLE. The service session pointer previously seen is insufficient to assert a canonical Researcher-ID or activity. Registration remains unconfirmed; source note persistence is a separate fact.

The current step establishes a concrete natural-number residual representation and working sort. Further research can compare alternative basin choices, including square-collapse grouping, against the binary baseline under an explicitly fixed magnitude/distribution/cost model. No performance gain, optimality, or universal impossibility is claimed.
