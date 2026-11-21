# R762HJ — Retained-axis alternating certificate and one-interval BRC repair

**Status:** AUTHOR-PROVED HJ1–HJ2; EXACT FINITE CHECK for all named closed Port walks at m=2,4,6,8; explicit length-18 limitation witness; NOT_REVIEWED.

**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Historical research line EM-X6-3050F6; existing RA-6068F717D991DF54FBBDDEED is provenance only, and this GitHub artifact does not claim a fresh native Activity/PROGRESS receipt. **Frozen scientific input:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`, P000 V5 definitions and joint-relation preservation. The Port step and three-support displacement below remain a declared **composite candidate**; they are not a primitive force event admitted under TRIADIC_CLOSURE_E.

**Predecessors:** R762HE (retained-axis parity), R762HG (half-path counts), R762HI (exact two-colour half-degree graph factor) at PR #2865, #2869 and #2875 respectively. This work retains all path order, labelled Port transitions and signed BRC source multiplicity when testing a fixed unsigned history.

## Model

Let X={0,1,2,3,4,5}; P_t are named 2-subsets, P_m=P_0={0,1}, and |P_{t-1}∩P_t|=1. Each event is individually identified by its time index t=0,...,m−1. Set

- `h_t = 1_{P_t ∪ P_{t+1}} ∈ {0,1}^6` (three supported native axes);
- `a_t` = the unique retained axis in `P_t ∩ P_{t+1}`;
- a signed completion chooses independently `ε_t ∈ {−1,+1}` and the resulting chart-relative signed Cell displacement is `ΔC=Σ ε_t h_t`.

These are composite chart increments, not a statement of primitive straight-line force balance.

## HJ1. Retained-axis alternating identity (all even lengths)

Let m be even, and use the fixed alternating event signs `α_t=(-1)^t`. Then

```text
Σ_{t=0}^{m−1} α_t h_t = − Σ_{t=0}^{m−1} α_t e_{a_t}.   (HJ1)
```

Consequently a *particular* signed zero-Cell completion is certified in O(m) integer operations if, and only if, each of the six axes is retained equally often at even-indexed and odd-indexed event occurrences.

**Proof.** As incidence vectors, `h_t=1_{P_t}+1_{P_{t+1}}−e_{a_t}`. In the alternating weighted sum, the two Port-incidence terms cancel by a cyclic index shift, using `m` even and `P_m=P_0`. The remaining term is the displayed retained-axis vector. Each coordinate vanishes precisely when the signed retained occurrence count vanishes. QED.

**BRC interpretation.** The alternating completion and its simultaneous sign reversal give two distinct positive-weight signed source branches for every nonempty unsigned history passing HJ1. The retention histogram alone is a sound existence certificate only for these chosen signs, not a sufficient quotient for all possible future event permissions, source multiplicities, or intermediate Cells.

## HJ2. One contiguous interval flip and exact prefix criterion (all even lengths)

Define the full six-component integer prefix sequence

```text
V_0 = 0,   V_j = Σ_{t=0}^{j−1} (-1)^t h_t,   j=1,...,m.
```

Fix any nonempty contiguous index interval `[a,b)` with `0≤a<b≤m`, and flip the alternating signs exactly on it: `ε_t=−α_t` inside, `ε_t=α_t` outside. This produces zero displacement **if and only if**

```text
2 (V_b−V_a) = V_m.                            (HJ2)
```

**Proof.** The interval contributes `V_b−V_a` before flipping. Negating its sign changes the total from `V_m` to `V_m−2(V_b−V_a)`; setting it to zero proves both directions. QED.

The criterion is testable in expected O(6m) time with a hash map of the six-dimensional exact prefix vectors: if `V_m` has any odd coordinate, no interval exists; otherwise seek an earlier `V_a=V_b−V_m/2`, for any `b>a`. A deterministic O(m log m) dictionary implementation is also immediate. This is a **constructive signing**: return `(a,b)` and the full ordered sign word. It is stronger than the unflipped alternating certificate HJ1, but remains a sufficient family for the unrestricted signability question.

## Exact finite census, all named Port walks from 01

The accompanying C++17 checker exhaustively enumerates 8 choices at each Port transition, retaining duplicate supports and distinct temporal source occurrences. It reports:

| m | closed unsigned histories | parity-even histories | HJ1 alternating | prior HI2 two-layer Euler | HJ1 ∩ HI2 | HJ1 ∪ HI2 | HJ2 one-interval |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| 4 | 288 | 168 | 168 | 168 | 168 | 168 | 168 |
| 6 | 17,536 | 4,960 | 4,960 | 4,864 | 4,864 | 4,960 | 4,960 |
| 8 | 1,118,720 | 177,536 | 176,264 | 162,368 | 161,288 | 177,344 | 177,536 |

Thus for every named closed Port history of lengths 2,4,6,8 that satisfies the six parity incidences, HJ2 constructs a zero-Cell signing by at most **one contiguous sign-block flip** of the alternating assignment. The exact HJ1 test covers 14,976 m=8 histories outside HI2, and HI2∪HJ1 leaves 192 parity-valid histories not directly certified; HJ2 covers those as well. At length 6, HJ1 adds 96 histories to HI2.

This is a finite, exhaustive *construction theorem* at these four lengths; it is stronger than the earlier finite existence check because it bounds the sign-pattern edit complexity by one interval. Source-labelled BRC multiplicity is preserved by the enumerator. The cited prior values of complete signed BRC mass remain separate and are not recomputed here.

## Strict limitation witness at length 18

The following **legal candidate Port walk** is closed and each consecutive pair shares one axis:

```text
01 → 15 → 12 → 25 → 24 → 14 → 45 → 04 → 05 → 03 →
05 → 03 → 04 → 24 → 23 → 25 → 35 → 05 → 01.
```

Its 18 ordered supports are:

```text
015 125 125 245 124 145 045 045 035
035 035 034 024 234 235 235 035 015
```

Six-axis incidence counts are `(10,6,8,8,8,14)`: all even. The alternating signs give `V_18=(2,0,0,0,−2,0)`. A one-block repair would require a pair of strict prefix positions `a<b` with `V_b−V_a=(1,0,0,0,−1,0)`. Exact evaluation of all `18·19/2=171` possible nonempty intervals finds **zero** such pairs.

Nevertheless the source history has **652 distinct full signed zero-Cell completions** (exact 2^18 bitmask census); one explicit solution is the alternating pattern with the two *disjoint singleton* intervals `[0,1)` and `[5,6)` flipped:

```text
ε = (−,−,+,−,+,+,+,−,+,−,+,−,+,−,+,−,+,−).
```

Direct six-coordinate integer summation gives zero for this assignment. Thus the one-interval *constructive scheme* is not globally complete, while parity sufficiency for **all** legal closed Port histories remains an open question. No minimality of length 18 is claimed (lengths 10–16 have not been fully enumerated for one-block failure).

The accompanying C++17 program also validates the interval obstruction and counts the 652 exact completions independently of the interval formula. The finite checker does **not** certify native TRIADIC_CLOSURE_E legality, full historical time dynamics, or mathematical acceptance.

## Continuation

A useful next unit is to classify the minimum number of disjoint alternating-sign flip blocks needed to complete a parity-even closed Port history, derive an exact positive-BRC transfer for its block complexity, and search for an actual parity-even **unsignable** legal Port history—or prove that no such history exists. In parallel, recover native typed force/Cell/Link/Port/time and rotation permission at frozen P000, retaining the actual source histories and distinct observer interfaces. Preserve the original Researcher/CLAIM and pending Activity/PROGRESS linkage as separate control state, and retain NOT_REVIEWED until independent review.
