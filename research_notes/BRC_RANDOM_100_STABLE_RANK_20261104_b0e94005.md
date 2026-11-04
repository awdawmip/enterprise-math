# BRC stable rank construction for 100 arbitrary numbers

Progress-Event-ID: brc-random-100-20261104-b0e94005
At: 2026-11-04T04:01:33.182Z
Status: AUTHOR_DERIVATION_AND_EXECUTED_FINITE_CHECKS
Scope: 100 arbitrary finite numeric inputs, including negative, fractional and repeated values; comparison defines a total order.
User correction: “不是 一百个随机数 不是1到一百” in the ongoing clarification; the operative meaning is 100 numbers with unrestricted values. The earlier 1..100-permutation assumption is retired for this task.
Normative global snapshot: 9568b9fadd3f096ba8f080c5af44b43e6e5acb75
Current project source read: 042f45ae0456b9c0ba49101c97e45d937fd8e321
Prior source modules reused in local execution: 01d7a2c0982291f7efec74931449e1ae0ac5e650
Contribution: current ChatGPT conversation and shared-context mathematical subagent; no independent-review claim.

## Construction and proof

Retain each original index i and define the stable key K_i=(a_i,i).
For each endpoint i begin with one unit-weight branch, CWM=(1,1,1).
For each unordered index pair i<j, make exactly one comparison a_i>a_j.
If true, recoalesce one unit branch into endpoint i; otherwise into j.
The false case includes equal values, so the later original index receives the increment.

The added branches reaching endpoint i are in bijection with tokens whose stable keys are smaller than K_i.
Writing r_i for the zero-based stable rank, the resulting state is

(C_i,W_i,M_i)=(r_i+1,r_i+1,1),
E_i=W_i/M_i=r_i+1,
Delta_i=ln(E_i).

The E_i form exactly a permutation of 1..n. Scatter the original token i to output address E_i-1.
This computes ranks from the unsorted input; it does not assume ranks.
All branch masses are positive 1. Numeric values or signed differences are comparison data, not branch weights.
Comparisons are evaluated directly, without subtracting floating inputs.
The original array and index labels are retained; the n accumulators are a sufficient observer for this fixed sorting output. An explicit log of every comparison is optional extra output.

The BRC operations are the existing cwm_recoalesce and effective_multiplicity laws.
This is a BRC expression of comparison/rank sorting, with explicitly charged input comparisons.
No method novelty or speed superiority is asserted.
Reference source:
https://github.com/awdawmip/enterprise-math/blob/042f45ae0456b9c0ba49101c97e45d937fd8e321/src/enterprise_math/brc_weighted.py

## Cost and example

Each unordered pair is visited once: n(n-1)/2 comparisons and the same number of unit-branch increments.
For n=100 this is exactly 4950 comparisons, followed by 100 output placements.
With unit-cost numeric comparisons the total time is O(n^2), auxiliary storage O(n).
For variable-precision numbers include the actual comparison cost.
No quadratic residual matrix or explicit 5050-branch graph is materialized.

Example input: [37.5,-8,102,37.5,0]
E: [3,1,5,4,2]
Stable output tokens: [(-8,1),(0,4),(37.5,0),(37.5,3),(102,2)].
The two equal 37.5 values retain original order.

The prior value-as-address permutation method handled an already known-rank special input.
Its O(n) bound is not the end-to-end cost for these arbitrary values.
After ranks are known, one may optionally define position displacement d_i=E_i-(i+1);
the present implementation uses a separate output array and writes every input token once.

## Executed verification on 2026-11-04

The local Python run completed with all assertions passing:
- Exhaustive 1093 arrays of lengths 0..6 over {-1,0,1}.
- 200 independently generated length-100 arrays from one Python Random(20261104) stream:
  first 100 use randint(-30,30); next 100 use uniform(-1e6,1e6), with injected repeats on even iterations.
- Eight special cases: empty, singleton, all equal, sorted, reversed, huge signed integers, extreme finite floats including signed zero, exact rational values.
- 29 selected cases executed the existing project CWM functions and agreed exactly with the unit-weight specialization.
- All cases checked stable token output against Python sorted indices, uniqueness/completeness of E, and exact comparison count.
- Demonstration result E=[3,1,5,4,2], 10 comparisons for five input values.

The earlier verification tool call was interrupted by the user before a receipt was delivered.
The retained local script was subsequently run successfully; the claims above use that successful new receipt.
Source reuse classification: REUSE_EXECUTED.

## Complete implementation and verification script

```python
from itertools import product
from random import Random
from fractions import Fraction
import json
from enterprise_math.brc_weighted import CWM_ONE, cwm_recoalesce, effective_multiplicity

def brc_rank_sort(values):
    """Totally ordered numeric values; returns stable tokens, E and pair count."""
    n = len(values)
    effective = [1] * n
    comparisons = 0
    for i in range(n):
        for j in range(i + 1, n):
            comparisons += 1
            if values[i] > values[j]:
                effective[i] += 1
            else:
                effective[j] += 1
    out = [None] * n
    for i, value in enumerate(values):
        out[effective[i] - 1] = (value, i)
    return out, effective, comparisons

def brc_rank_sort_native(values):
    n = len(values)
    states = [CWM_ONE] * n
    for i in range(n):
        for j in range(i + 1, n):
            target = i if values[i] > values[j] else j
            states[target] = cwm_recoalesce(states[target], CWM_ONE)
    effective = []
    for state in states:
        ratio = effective_multiplicity(state)
        assert ratio.denominator == 1
        assert state.count == state.total == ratio
        assert state.dominant == 1
        effective.append(ratio.numerator)
    out = [None] * n
    for i, value in enumerate(values):
        out[effective[i] - 1] = (value, i)
    return out, effective

def verify(values, native=False):
    tokens, effective, count = brc_rank_sort(values)
    expected = [(values[i], i) for i in sorted(range(len(values)), key=lambda i: (values[i], i))]
    assert tokens == expected
    assert sorted(effective) == list(range(1, len(values)+1))
    assert count == len(values)*(len(values)-1)//2
    if native:
        assert brc_rank_sort_native(values) == (tokens, effective)
    return tokens, effective, count

exhaustive = 0
for n in range(7):
    for a in product((-1, 0, 1), repeat=n):
        verify(list(a))
        exhaustive += 1

rng = Random(20261104)
random_tests = 0
native_tests = 0
for t in range(200):
    if t < 100:
        a = [rng.randint(-30,30) for _ in range(100)]
    else:
        a = [rng.uniform(-1e6,1e6) for _ in range(100)]
        if t % 2 == 0:
            a[50:55] = [a[0]] * 5
    use_native = (t % 10 == 0)
    verify(a, use_native)
    random_tests += 1
    native_tests += use_native

specials = [
    [],
    [7],
    [2] * 100,
    list(range(100)),
    list(range(99,-1,-1)),
    [10**400, -(10**400), 0, 10**400],
    [1e308, -1e308, 0.0, -0.0, 1e-308],
    [Fraction(1,3), Fraction(-2,7), Fraction(1,3), Fraction(4,5)],
]
for a in specials:
    verify(a, True)
    native_tests += 1

demo = [37.5, -8, 102, 37.5, 0]
tokens, effective, count = verify(demo, True)
native_tests += 1
report = {
    "source_scope": "reused unchanged project CWM functions",
    "exhaustive_cases": exhaustive,
    "exhaustive_domain": "lengths 0..6 over {-1,0,1}",
    "random_100_element_cases": random_tests,
    "rng": "Python Random(20261104), one sequential stream",
    "special_cases": len(specials),
    "native_CWM_cases": native_tests,
    "checks": ["stable sorted tokens equal oracle", "E is a permutation of 1..n", "pair count equals n*(n-1)/2", "native CWM agrees on selected cases"],
    "demo": {"input":demo, "E":effective, "tokens":tokens, "comparisons":count},
    "comparisons_for_n_100": 100*99//2
}
print(json.dumps(report, ensure_ascii=False, indent=2))


```

## Activity/publication state

Ordinary material preservation follows the current PORTABLE_RESEARCH_PROTOCOL.
No formal task, claim, Result, review or theorem acceptance is asserted.

Read-only bridge status:
https://github.com/awdawmip/kimi-query-bridge/issues/6651
It returned SUCCEEDED and a local session pointer MCP-ea7c68c59e1a4fbd97f89c2c65b2f67e
with original start_request_id brc-sort-20261103-b0e94005-session-bridge.
That original request had previously returned SOURCE_TREE_SIZE_LIMIT:
https://github.com/awdawmip/kimi-query-bridge/issues/6649

The exact expected session-record path at project source 042f45ae0456b9c0ba49101c97e45d937fd8e321 returned 404.
Thus local service session metadata is observed, while canonical research identity/activity publication remains unconfirmed.
Preserve these original request IDs for reconciliation; do not invent a Researcher-ID or duplicate the session.

## Optional next question

Study block aggregation during a stable merge:
s known smaller tokens contribute (s,s,1), representing s unit paths.
A single path of weight s would instead be (1,s,s) and would change E semantics.
Any claimed improvement must include construction, comparisons, aggregation and output recovery.
This is a prospective optimization; the implemented and verified method above performs all pair comparisons.
