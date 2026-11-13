# A3 quotient descent: one fixed binary singleton probe detects every forbidden aligner

**Date:** 2026-11-13. **Status:** self-contained additional mathematical Driver check; **not** an immutable Native Review or a frozen-Result replacement.

**Provenance and scope.** Original A3 Result: `RR-9FF7F84F01C577774649`, Task `RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION`, publication `TP2-D2D715EB36415B0CA0C5`, researcher `EM-A3SCR-7A41D2`; original science and PR #1491 are retained. This note strengthens the previous Driver quotient-normalizer and alphabet/faithfulness audits by finding a **single fixed carrier site** that detects all noncentralizing aligners. It is an extension of those prior analyses, not an independent second reviewer.

## 1. Model and exact statement

Let `G=S4` act on the A3 lattice by `R_g=sgn(g) P_g` (where `P_g` permutes four coordinates), and let `h=(12)`, `H={e,h}`, `B_n={x in Z^4:sum_i x_i=0, max_i |x_i|<=n}`, `S_r=B_r\B_{r-1}`. A radial partial move `D_{n,d}(g)`, `1<=d<=n`, acts by `R_g` on shells `r>=n-d+1` and by identity below. Global `H` acts by `R_h` on all shells, and `X_n=A^{B_n}` has at least two available labels. Write `delta_x` for the binary coloring with the second label only at site `x`, and `pi:X_n -> X_n/H` for the global orbit projection.

**Uniform singleton-probe theorem.** Fix *any* active shell radius `r in {n-d+1,...,n}` and the **same predetermined root direction**
```text
x_r = r(e_3-e_4) = (0,0,r,-r).
```
For *each* `g in S4`, the following are equivalent:

1. `D_{n,d}(g)` defines an operator `X_n/H -> X_n/H`;
2. `pi(D_* delta_{x_r}) = pi(D_* delta_{R_h x_r})` for this one fixed pair of equivalent binary singleton states;
3. `g` stabilizes the unordered pair `{3,4}`;
4. `g in C_{S4}((12))={e,(12),(34),(12)(34)}`.

Thus, unlike a scan of all state labels or carriers, **one predetermined binary probe on one active shell**, evaluated on its two representatives, is necessary and sufficient to determine whether *that* aligner descends to the global residual-H quotient. The exact support position must be active; if the move fixes the probe shell, the test is not discriminating. The theorem does not claim all two-path squares commute, and does not change the previously established additional support-transition conditions for a naturality square.

## 2. Proof

Since `h=(12)` is odd and `P_h` fixes the third and fourth coordinates, `R_h x_r=-x_r`. The two singleton states `delta_{x_r}` and `delta_{-x_r}` are therefore in the same global `H` orbit.

Because `r` is active, let `y=D_{n,d}(g)x_r=R_g x_r`. Linear permutation actions give `D_{n,d}(g)(-x_r)=-y`, and `y` is a nonzero signed root of the form `+/-r(e_{g(3)}-e_{g(4)})`.

The images of our two equivalent input singleton states have the same `H` orbit exactly when `-y=y` or `-y=R_h y`. The former is impossible because `y!=0`. For the latter, `R_h=-P_h`, so it is exactly the condition `P_h y=y`. A signed root `y=+/-r(e_i-e_j)`, `i!=j`, is fixed by swapping coordinates 1 and 2 precisely when neither of its nonzero entries occupies either coordinate 1 or 2; equivalently `{i,j}={3,4}`. Therefore the **single-probe orbit equality** holds iff `{g(3),g(4)}={3,4}`.

That stabilizer is `S_{\{1,2\}} x S_{\{3,4\}}`, exactly the centralizer of `(12)` in `S4`. If `g` is in this centralizer, `R_g` commutes with `R_h` on every active shell and the identity does so on every inactive shell. Hence the whole partial action commutes with global `R_h`, and defines a quotient-state operator. Conversely, any well-defined quotient operator must preserve the orbit equivalence of the chosen two singleton inputs, which by the argument forces `g` into the same centralizer. QED.

The assumption `|A|>=2` is essential: when `|A|=1`, all states are identical and every `g` induces the one-point quotient map, so the asserted biconditional fails.

## 3. General finite order-two sharpening

For any involution `h` acting on a finite carrier `Y`, let `P` be a carrier bijection and `k=PhP^{-1}`. With at least two labels, if the pair of singleton indicator states at `x` and `h x` stays in one `H` orbit for **every** `x`, then `k(z) in {z,hz}` for every `z`. Thus `k` preserves each one- or two-point `h` orbit and on a two-point orbit is either the identity or the swap. But `k` is conjugate to `h`, hence has the same number of two-cycles; every two-point orbit must be swapped. Therefore `k=h`, i.e. `PhP^{-1}=h`. Conversely centralization gives quotient descent immediately.

Consequently for order-two residual actions, **singleton binary orbit pairs already characterize the normalizer**, without requiring any two-marked-point subsets. The special A3 root geometry strengthens this from 'all singleton probes' to **one fixed singleton probe for every `g`**.

## 4. Independent exact finite regression

A separate direct Python permutation enumeration (no floating-point arithmetic or assumed theorem checker) used the literal signed action `R_g`, all 24 permutations `g in S4`, and `x_r=(0,0,r,-r)` for each `r=1,2,3,4`. On each shell, the test was whether `R_g R_h x_r` equals `R_g x_r` or `R_h R_g x_r`. There were **96 exact group/probe evaluations**. For each radius exactly 4 elements passed, namely coordinate permutations `[0123]`, `[0132]`, `[1023]`, `[1032]` in zero-based tuple notation: precisely `{e,(34),(12),(12)(34)}`. All other 20 failed on the same predetermined site. This regression confirms the formula for these finite cases; the proof above, not the finite enumeration, establishes the all-`n,d,r` statement.

A concrete `g=(23)`, `r=2` witness has `x=(0,0,2,-2)`, `R_h x=-x`, `R_g x=(0,-2,0,2)` and `R_g(-x)=(0,2,0,-2)`. Since `R_h R_g x=(2,0,0,-2)` is different from both, the two input singleton labels are equivalent while their images are not. (All coordinates follow directly from the signed action.)

## 5. Review/admission boundary

This is a new simplification of the A3 quotient-descent witness, **not** a replacement for the original exact radial-defect classification. It does not establish Native Review admission, formal Result acceptance, Task DONE, or closure of the parent A3 Objective. Original frozen Result, author contributions, H4 regression, radial formula, and previous audit findings remain preserved. A future Native Review should explicitly distinguish output-orbit comparison `X_{n+1} -> X_n/H` from an intrinsic square on quotient-state spaces, and carry the nontrivial-alphabet hypothesis.
