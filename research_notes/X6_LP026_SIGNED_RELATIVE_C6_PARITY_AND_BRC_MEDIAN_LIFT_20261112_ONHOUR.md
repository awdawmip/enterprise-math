# LP026 — signed X6 relative C6 grade, path parity and median-lift BRC theorem

Date: 2026-11-12. Scientific status: **AUTHOR_PROVED / INDEPENDENT EXACT INTEGER CHECK EXECUTED / NONBLIND / UNREVIEWED / NOT_ADMITTED**. Parent `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`, Driver `REQUEST_REVISION`. Frozen scientific pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical comparison pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.

## 1. A specific unresolved LP026 parity consumer

Old frozen `research_notes/X6_BRC_C6_GRADE_AND_EXACT_MULTINOMIAL_KERNEL_V9_20260905.md` (at `fd2bcff...`, observed Git blob `7eea4b5f9146090d16dfa6463087039666b50b3f`) §§1–5 defines on the *derived relative quotient* `G6_D=Z^6/Z·1`:

`rho([z])=sum_i z_i mod 6`, `chi2([z])=(-1)^(sum_i z_i)`.

For its explicitly **positive-axis-only** words of length `N` and normalized min-zero address `a`, the previously valid condition is `N>=sum a_i` and `N≡sum a_i (mod 6)`. It gives a single nonnegative count histogram `n_i=a_i+k`, `k=(N-sum a)/6`.

The current, frozen signed native X6 Cell model (`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`) has **twelve** free primitive coordinate labels `±e_1,...,±e_6`. The concrete LP026 question is: *what can the old C6 relative grade safely say about finite signed native word reachability, parity and BRC counts?* It must be answered without promoting the old positive-only reachability criterion to arbitrary signed words.

Reuse: current signed-BRC multinomial histogram law and its nonnegative thickness fibers (published `research_notes/X6_LP019_SIGNED_THICKNESS_NATIVE_BRC_CONSUMER_CROSSWALK_20261112_ONHOUR.md`) and the current relative quotient/min-zero carry. This note gives their **new median-lift composition at a fixed relative endpoint**.

## 2. Universal signed-relative median reachability theorem

Fix a chosen native Cell anchor and the free signed-step word alphabet `{±e_i : 1<=i<=6}`. For an ordered word `w` of length `N>=0`, let `z(w)∈Z^6` be its *true signed native displacement*. Let `a=can6(z)=z-min_i(z_i)·1`, so `a∈N_0^6` and `min a_i=0`.

Let `a_(1)<=...<=a_(6)` denote the sorted components of `a`. Define

`L_rel(a) = a_(4)+a_(5)+a_(6)-a_(1)-a_(2)-a_(3)`.

**Theorem LP026-P1 (all min-zero a and all N>=0):** At least one signed native word of length `N` has relative endpoint `a` **if and only if**

`N >= L_rel(a)` **and** `N ≡ sum_i a_i (mod 2)`.

In addition, `L_rel(a)=min_{h∈Z} sum_i |a_i+h|`, with the complete minimizing integer interval

`-a_(4) <= h <= -a_(3)`.

**Proof.** Every native displacement with min-zero class `a` is uniquely `z=a+h·1` for an integer `h`. Put `f(h)=sum_i |a_i+h|`. In the even six-coordinate case, the median property of the L1 objective makes `f` minimal precisely on the stated integer interval. There, the lower three and upper three terms have opposite signs and the `3h` contributions cancel, giving `L_rel` exactly. A signed native word reaching a fixed `z` has minimum length `sum|z_i|`; its other possible lengths are exactly that minimum plus `2k`, `k∈N_0`, by inserting immediate `(+e_i,-e_i)` pairs. Since `|z_i|≡z_i (mod 2)` and `sum z_i=sum a_i+6h`, every possible word satisfies the stated parity and lower bound. Conversely choose a minimizing `h`, take one shortest signed word of length `L_rel` to `z), and insert exactly `(N-L_rel)/2` canceling primitive-step pairs. QED.

**Exact parity-safe quotient:** for every such word,
`(-1)^N = chi2([z(w)]) = (-1)^(sum a_i)`.
But `rho([z(w)])≡ #positive_steps-#negative_steps (mod 6)` is the **signed event net**, not the total signed-word length modulo 6. Thus the C6 character retains the invariant parity `N mod 2`, while the stronger positive-only `N mod 6` rule is restricted to the positive subalphabet. Both statements are valid in their declared domains.

## 3. Exact signed-BRC multiplicity on one relative class

Write `z_i(h)=a_i+h`, `L_h=sum_i|z_i(h)|`, `K_h=(N-L_h)/2`, and `u^+=max(u,0)`, `u^-=max(-u,0)`. A signed endpoint `z(h)` contributes iff `L_h<=N` and `N-L_h` is even. In the contributing case, every letter histogram is uniquely

`p_i=z_i(h)^+ + k_i`, `m_i=z_i(h)^- + k_i`, where `k_i>=0`, `sum_i k_i=K_h`.

**Theorem LP026-P2 (exact nonnegative integer BRC mass):**

```text
B_rel(N,a) =
  sum_{h∈Z: L_h≤N, N-L_h even}
    sum_{k∈N_0^6: Σ k_i=(N-L_h)/2}
       N! / Π_{i=1}^6 [(z_i(h)^+ + k_i)! (z_i(h)^- + k_i)!].
```

**Proof.** Distinct `h` label different signed native endpoints even though they share the relative observer address. For each fixed `z(h)`, the displayed nonnegative histogram decomposition is unique, as in the existing signed-BRC kernel/LP019 proof. For fixed counts, multinomial permutations enumerate distinct ordered words exactly. The histogram and native-endpoint fibers are disjoint; summing them counts each concrete word exactly once. Each contributing term is a positive integer; there is no cancellation across opposite-sign endpoints. QED.

This formula is a precisely operation-typed way to compress ordered native words to an endpoint histogram and then to a relative observer without deleting BRC multiplicity. It is a direct composition of prior signed-BRC with the quotient; it does not alter P000, time/history decorations or restricted weighted channels.

## 4. Exact nontrivial witnesses

**Native zero vs relative zero at N=6.** Set `a=(0,0,0,0,0,0)`. The true native end displacements `z=-1·1,0,+1·1` all have the same relative address. Their exact free signed shortest/length-six BRC masses are respectively `720, 19920, 720`, giving

`B_rel(6,0)=21360`.

The historical positive-only C6 word model counts only the all-`+e_i` branch here (`720` words). At `N=2`, the signed-relative zero mass is `12` from primitive two-step returns, while positive-only relative zero is unreachable. The same relative coordinate is therefore compatible with a strictly richer signed event population; the original positive-only result remains exact in its own scope.

**Median example unavailable to the positive-only C6 rule.** For `a=(0,1,1,2,3,5)`, `sum a=12`, `L_rel(a)=8`. At length `N=8`, the two median lifts are:

- `h=-2`: `z=(-2,-1,-1,0,1,3)`, `L=8`, BRC `3360`;
- `h=-1`: `z=(-1,0,0,1,2,4)`, `L=8`, BRC `840`.

Hence `B_rel(8,a)=4200` even though `N=8` fails the *positive-only* condition `N>=12` and `N≡12 (mod 6)`. The median signed lift achieves a shorter legal native path **within the same relative quotient class**, not the same native endpoint.

## 5. Actually executed independent exact check

Published checker: `research_checks/X6_LP026_SIGNED_RELATIVE_C6_PARITY_BRC_20261112_ONHOUR.py`.

In this run, Python standard-library exact integer arithmetic independently compared (i) a twelve-letter signed-step dynamic program directly on min-zero relative classes and (ii) the nested integer histogram formula above. It covered **7,588 distinct (length,relative-state) pairs** for **all lengths 0 through 6**; all exact counts matched, with whole-state totals `12^N`. Numbers of relative states per length:

`N=0..6: [1, 12, 73, 284, 835, 2036, 4347]`.

Additional explicit assertions checked `B_rel(2,0)=12`, `B_rel(6,0)=21360`, and both separate lifts at the `(0,1,1,2,3,5),N=8` example (`3360+840=4200`). Observed terminal output:

```text
PASS X6_SIGNED_RELATIVE_PARITY_MEDIAN_BRC
independent_dp_vs_histogram_cases 7588
signed_relative_state_counts [(0, 1), (1, 12), (2, 73), (3, 284), (4, 835), (5, 2036), (6, 4347)]
r_zero_n6 21360 r_011235_n8 4200
```

The all-N result is proved algebraically above; the finite verification validates the independent implementation and worked witnesses. No numeric floating point, external geometry assumption or independent Driver review is used.

## 6. LP026 source-to-consumer disposition and continuation

Old C6 note §§1–2 and §§3–5 now have an exact split: `chi2` is an operation-safe signed-word **parity** observer under `G6_D`; its `N≡rho mod 6` path reachability is positive-word-specific, and its positive-only return formulas are **derived relative returns**, not automatically native signed Cell returns. Preserve historical formulas, attach this typed signed extension rather than editing their provenance. Related current `CQ=definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md` §7 already guards relative vs native endpoints.

This is an additional concrete **LP026 parity and BRC consumer** and direct source/evidence/action entry supplementing today's `research_notes/X6_LP28_SOURCE_CONSUMER_ACTION_CROSSWALK_20261112_ONHOUR_1400.md`. It does not complete the Driver's full 28-row historical/current repository-wide dependency census.

**Do not repeat:** historical72, native signed selected N25=30/846, carrier (1,1,1) and closed disk, LP011 signed chamber, LP019 signed thickness, LP026 norm resonance, R063 fixed-sector and all-pair N2500 capacities. **Next precise work:** attach this C6-grade source location and signed-path parity distinction to LP026's current consumer tests; continue remaining active executable signed-quotient callers, LP011/LP019 exact historical provenance, and the unclosed 28-row dependency matrix.

Source evidence is portable and author-only. Original Research lane `chatgpt-research-onhour-enterprise-math-20260923` has no verified winning current X6 CLAIM/open. Current typed continuation support: [Enterprise Math #2141](https://github.com/awdawmip/enterprise-math/issues/2141). This proof/checker publication neither claims an admitted Result nor initiates a new native task.
