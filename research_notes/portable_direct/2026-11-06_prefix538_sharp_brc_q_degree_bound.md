# PREFIX-538 — Sharp first-axis BRC degree and exact support-cap reduction

Date: 2026-11-06 (Asia/Shanghai). Parent line: `RS-X6-NATIVE-ROTATION-DYNAMICS`; predecessor: PREFIX-537 at `enterprise-math/main@c9f20aa52a0f55441e0c94bf4b4ce9b1ef6ba44a`. Immutable scientific reference: `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Work mode: independent author mathematics, no native CLAIM. Status: **AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Precise statement

Consider the frozen four-STAR native X6 candidate, with STAR triples `(1,3,6),(1,4,5),(2,3,5),(2,4,6)`, 48 directed phases, three legal successors per phase, and two separately labeled INNER/OUTER microstep choices at each macro transition. For a fixed initial phase `s` let
```text
P_s(d;q,z) = SUM_{w: |w|=d, w_0=s} q^{p_1(w)} z^{H(w)}
```
where `p_1` is signed first-axis BRC cancellation count and `H` is the consecutive-INNER `aAc` gate count. Then for **every** root `s` and integer `d >= 0`:
```text
deg_q P_s(d;q,z) <= floor((d+1)/3).                         (1)
```
The bound is **globally sharp for every depth**. In fact one and the same root, `(A,-L6,+L3)`, has a legal periodically continued path attaining equality in (1) for each `d`. This is a stronger exact bound than PREFIX-537's `p_1 <= d`. No equation for full native history or future Cell semantics is collapsed.

## Proof: two-step exclusion and endpoint correction

Represent a path of length `d` by phases `i_0,...,i_d`; write `sigma_j` for `+1` or `-1` when current phase direction is the first signed axis and 0 otherwise, and `eps_j=|sigma_j|`. The primitive directed rule is `(a,p,c)->(a,c,k)` for the allowed same-STAR continuation and `(a,p,c)->(b,c,k)` for the other STAR containing `|c|`. The two STARs containing first axis are `(1,3,6)` and `(1,4,5)`, whose intersection is exactly that axis. Consequently, if `eps_j=1` then `eps_{j+1}=eps_{j+2}=0`: immediate return is excluded by the previous-axis restriction, and a two-step return would require switching between the two first-axis STARs through a non-first common axis. The finite 48-phase successor table independently verifies this fact.

Let `m=sum eps_j` count first-axis phase visits. Every two visits are at least 3 phase indices apart, so `m <= floor(d/3)+1`. The endpoint BRC identity from the frozen phase observer is
```text
2*p_1 = K - |sigma_d - sigma_0|;
K = SUM_{j=0}^{d-1}(epsilon_j+epsilon_{j+1}) = 2*m-epsilon_0-epsilon_d.
```
Thus
```text
p_1 = m - (epsilon_0+epsilon_d+|sigma_d-sigma_0|)/2.        (2)
```
For `d=3k+2`, `m<=k+1`, proving (1). For `d=3k`, the only way to have `k+1` visits is to occupy both endpoints, so the last term of (2) is at least 1 and `p_1<=k`. For `d=3k+1`, having `k+1` visits forces at least one endpoint to be a visit. If exactly one is a visit then the endpoint difference is 1; if both are visits their endpoint contribution is 2. Hence again `p_1<=k`. This proves (1) for all roots and all lengths, including `d=0,1`.

For equality, repeat the following legal directed six-phase cycle, starting at its first entry:
```text
(A,-L6,+L3) -> (A,+L3,-L1) -> (A,-L1,+L6) ->
(A,+L6,-L3) -> (A,-L3,+L1) -> (A,+L1,-L6) -> start
```
Its first-axis signed incidence is periodically `0,-1,0,0,+1,0`. Taking all Cell labels OUTER is legal. Directly applying (2) to the prefix of length `d` yields `p_1=floor((d+1)/3)`: for residues `d=3k,3k+1,3k+2`, the counts are `k,k,k+1` respectively. This proves sharpness uniformly in `d`.

## New joint support certificate

Reuse the established gate constraints `0<=h<=H_d=floor((d+2)/4)` and `h<=p_1`. Put `M_d=floor((d+1)/3)`. Every nonzero monomial `q^p z^h` obeys
```text
0 <= h <= H_d, h <= p <= M_d.
```
Thus each rooted polynomial has at most
```text
C_d = (H_d+1)(M_d+1)-H_d(H_d+1)/2.                          (3)
```
possible nonzero monomials. In particular, at `d=24`, the previous cap was `154`, while (3) gives `42`, a reduction by `154/42≈3.667` in candidate coefficient slots. This reduces the domain of exact sparse and dense implementations without asserting a measured runtime speedup. The asymptotic coefficient of `d^2` decreases from `7/32` to `5/96`, a ratio `21/5=4.2`. The earlier `O(N^3)` number-of-slots and `O(N^4)` bit-size upper-order estimates for complete rooted outputs still hold, with improved leading candidate-slot constants.

## Reproducible check and sources

Run `python PREFIX538_degree_certificate_compact.py` with Python standard library, from its own directory. It reconstructs the 48 phases and transitions, verifies the local two-step exclusion for all phases, verifies the period-six witness for lengths `0..240`, and independently calculates all 48 rooted exact `Z[q,z]` histograms for every depth `0..24` (1200 full root-depth cases) using INNER/OUTER-labeled forward states. Output: `ALL_CHECKS_PASS`. At depth 24: `max_p=8`, `max_h=6`, `max_terms=41`, `total_terms=1876`, `distinct_root_polynomials=26`, `new_cap=42`, `old_cap=154`. Those observations agree with PREFIX-537's independent three-seed symbolic calculation. Exact finite enumeration corroborates the unbounded proof; the proof itself uses the graph rule, endpoint formula and periodic witness.

Dependencies: PREFIX-537 `2026-11-06_prefix537_symbolic_brc_gate_48root.md`; PREFIX-533 observation-class result; frozen four-STAR source pin above. This result belongs to the declared observer, not to all X6 dynamic and Cell/provenance operations.

## Next discriminating work

PREFIX-539: implement a dense joint histogram bounded by (3), compare controlled wall time and memory against sparse three-seed lift and independent raw branching at identical depths, verify full coefficient equality and initialization/output costs. Examine when a 26-class extraction map beats the three-seed computation, preserving all native branch/Cell data when later operations require it.
