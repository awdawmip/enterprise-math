# PREFIX-619-R2 — Exact 14-phase active support and full-output cost of the X6-BRC four-point probe

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR-SIDE EXACT THEOREM + EXECUTED EXACT FRACTION CHECKER; independent Driver review pending.
Frozen science: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Predecessors: PREFIX-617 full48 positive eight-state intertwiner, commit `00cdf3bcbea94aaa623e8b3e969f2354a5bfd21e`; PREFIX-618 four-terminal-phase-sensor theorem, commit `a546f6402d43d772975cf8adec4eee01f06d8c9e`.
Current P000, ACTIVE X6 worldview and joint-observer-preservation and BRC-only science-method rules apply separately. We study the original **48-phase positive branch-sum** quotient, not the tagged 96-port path state.

## Precise question and inputs

For `d=e4+e11+e14+e32`, calibrated nonnegative initial gates `a,b`, `lambda>0`, and any subsequent nonnegative gate word `q1,...,qt`, determine (1) exact terminal nonzero phase support and (2) verified full-output computational costs of native 48D, positive 8D, and four-residue scalar accumulator implementations, counting input preparation and output recovery.

The frozen STAR source gives 48 zero-based `(a,p,c)` phases. Each live phase row (axis `|c| in {1,2,3,4}`) has three original tagged successors; the other rows vanish for weights `(1,1,1,1,0,0)`. The positive phase-sum matrix `Q(g)` has **96 structurally nonzero entries** (32 live rows times three). These 96 entries are a matrix sparse count and are not an identification of the separately defined 96-port carrier or its 576 tagged actions.

## Exact theorem 619.1: fourteen active phases at every time

Use the explicit PREFIX-617 nonnegative embedding `H=[H_C H_B]` (48 by 8), whose columns are:

```
C0: (2,3,15); C1: (5,28,29); C2: (27,38,39); C3: (16,17,41) all coefficient 1.
B0: (3,14,15) coefficient 1
B1: (17,40,41) coefficient 2
B2: (26,27,39) coefficient 4
B3: phase 4 coefficient 4; phases 5,29 coefficient 8
```

Under the native exact intertwiner `Q(g) H = H diag(C,B(g))`, `C=2P` for the forward four-cycle and `B(g)` is the forward four-cycle with wrap weight `4(g+3)`. The calibrated lift after the two initial BRC operations is
```
c0 = lambda*(0,0,4,4)
w0 = lambda*(b+3,a+3,1,1/2).
```
For all nonnegative gates, `w_t` has all four coordinates strictly positive. `c_t` has exactly two positive coordinates, namely `(t+2) mod4` and `(t+3) mod4`. Write
```
S_B = {3,4,5,14,15,17,26,27,29,39,40,41}
S_C(0) = {27,38,39,16,17,41}
S_C(1) = {16,17,41,2,3,15}
S_C(2) = {2,3,15,5,28,29}
S_C(3) = {5,28,29,27,38,39}.
```
Since all contributions to `H(c,w)` are nonnegative, there is no cancellation. Direct exact set intersection yields `|S_B|=12`, `|S_C(t)|=6`, and `|S_B ∩ S_C(t)|=4` for each residue. Thus
```
support(x_t) = S_B union S_C(t mod4);
|support(x_t)| = 14 (all t>=0).
```
The union of supports across times has 16 phase rows. This is a dynamic support certificate for this fixed probe and observer; it is **not** a license to erase native port/provenance residuals.

## Exact algorithm 619.2: three end-to-end equivalent BRC sum implementations

(A) `native48`: `x0=lambda*Q(b)Q(a)d`, then repeated original `Q(q)` applied to 48 exact rational coordinates, 96 sparse candidate edges per gate.
(B) `positive8`: use the same two-step native preparation, then `c'=2Pc`, `w'=B(q)w` with 8 nonzero scalar transition entries; at the endpoint reconstruct all 48 coordinates from the 24 nonzero coefficients of `H`.
(C) `four_products`: use the same exact source lift; maintain four factors
`F_r(t)=prod_{1<=s<=t, s mod4=r}4(q_s+3)`,
updating only one factor per gate. Recover
```
c_t[j] = 2^t * c0[(j-t) mod4]
w_t[j] = w0[(j-t) mod4] * F_((t-j) mod4)(t)
x_t = H_C c_t + H_B w_t.
```
These identities follow by induction on the proved BRC four-cycle, retaining all original 48 phase-sum output entries. Scalar update counts are O(t), O(1) scalar registers for (C); rational bit width and source/port preparation remain separately charged.

**Bit-growth witness:** if `q_s=1` for `t=4k`, each four-residue factor is `16^k=2^t`, of exact binary width `t+1` bits. This proves linear bit growth for explicit integers in this valid input family. It does not imply universal O(1) bit memory or an optimal bit-operation algorithm.

## Executed exact evidence

The standalone Python 3 script `PREFIX619_R2_exact_cost_benchmark.py` rebuilds the original STAR successor incidence and native Q, and compares 48 exact `fractions.Fraction` outputs from all three paths. Calibrated `a=1,b=2,lambda=3/2`. Test gates: `((13j²+7j+3) mod11)`; nonnegative rationals `((11j²+5j+1) mod7)/(((3j+1) mod5)+1)`; and all-zero gates. Lengths: `0,4,16,64,256,1024` (rational length 1024 omitted). **17 exact cases, 17 complete 48-vector equalities passed**. Every tested output has 14 nonzero phase coordinates.

Observed wall-clock medians (nanoseconds; full input setup and all 48-value output reconstruction included, three or five repetitions):

| integer-word length | original Q 48D | positive 8D | four products | output max numerator/denominator bits |
|---:|---:|---:|---:|---:|
|16|2,265,005|359,339|329,624|25|
|64|7,835,283|649,253|423,195|84|
|256|28,784,389|1,649,402|806,078|313|
|1024|121,340,996|6,775,495|2,627,758|1240|

At length 1024, this measured workload gives a 17.9-fold native48/positive8 and 46.2-fold native48/four_products elapsed-time ratio. Timings are local interpreter, machine, representation and workload-specific **engineering measurements**, not asymptotic speedup proofs. The full case inventory and execution parameters appear in the companion results JSON; mathematical validity comes from the BRC intertwiner and exact cycle proof, not finite tests.

## Frontier and evidence boundary

(1) Build a genuinely native 96-port **typed tagged-path** observer and test precise future operations for descent through the phase-sum map, producing a two-history separation witness or a scoped fiber-constancy certificate. (2) Compare true 96-port source setup, provenance transport, exact big-integer bit operations and output cost for eligible downstream workloads. (3) Optimize terminal observation for unknown `a,b,lambda`.

Original frozen science, P000 and the tagged-action substrate are unchanged. Author-side mathematics and measured exact BRC computation are not an independent Driver acceptance, shared task completion, or full native 96-port equivalence claim.
