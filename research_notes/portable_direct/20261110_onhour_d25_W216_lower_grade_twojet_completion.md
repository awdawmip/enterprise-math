# D25 — Original W216 lower-grade p-adic two-jet and signed LIFT certificate

Date: 2026-11-10. Status: **AUTHOR_SIDE / EXACT ALGEBRAIC PROOF / 13 EXACT CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0**.

Parent Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`. Publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research lane `chatgpt-research-onhour-enterprise-math-20260923` (separate from maintenance).

## Exact original observer and new result

For a prime `p=6m+1>3`, work in `Z_(p)`, define

\[
A_k=\frac{\binom{2k}{k}^2\binom{3k}{k}}{216^k}
=2^{-k}\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3},\qquad
W_p=\sum_{k=0}^{p-1}(6k+1)A_k.
\]

The target classes `p≡13,19 (mod24)` lie in this domain; the parity of `m` distinguishes them. For `0≤k<p`, the exact original coefficient valuations are

\[
v_p(A_k)=
\begin{cases}
0 &0\le k\le2m,\\
1 &2m<k\le3m,\\
2 &3m<k\le4m,\\
3 &4m<k<p.
\end{cases}
\]

The previously established grade-2 finite-field bridge [W-grade2](20261109_onhour_d25_W_grade2_finitefield_bridge.md) handles `3m<k≤4m`. The **new unit here** explicitly reconstructs the missing grade-0 **second p-adic jet** and grade-1 **first p-adic jet**, coefficient by coefficient modulo `p³`. This completes all original 216-model coefficient grades needed for the `(W_p-p)/p² modp` observer.

Write `H_n^{(r)}=∑_{j=1}^n j^{-r}` (with `H_0=0`), always as p-local rationals. For `0≤k≤2m`, define

\[
D_{n,k}^{(r)}=H_n^{(r)}-H_{n-k}^{(r)},\quad
\alpha_k=\tfrac13D_{2m,k}^{(1)}+\tfrac12D_{3m,k}^{(1)}+\tfrac23D_{4m,k}^{(1)},\quad
\beta_k=\tfrac19D_{2m,k}^{(2)}+\tfrac14D_{3m,k}^{(2)}+\tfrac49D_{4m,k}^{(2)},
\]
\[
B_k=(-1)^k 2^{-k}\binom{2m}{k}\binom{3m}{k}\binom{4m}{k}.
\]

**Theorem, grade 0, all `p=6m+1`:**

\[
\boxed{A_k\equiv B_k\left[1-p\alpha_k+\frac{p^2}{2}(\alpha_k^2-\beta_k)\right]\pmod{p^3}\qquad(0\le k\le2m).}\tag{1}
\]

For `2m<k≤3m`, set the p-integral unit

\[
T_k=\frac{(2m)!(k-2m-1)!(3m)!(4m)!}
{(3m-k)!(4m-k)!(k!)^3\,2^k},
\]
\[
\gamma_k=\frac{H_{k-2m-1}-H_{2m}}3
-\frac{H_{3m}-H_{3m-k}}2
-\frac{2(H_{4m}-H_{4m-k})}3.
\]

**Theorem, grade 1, all `p=6m+1`:**

\[
\boxed{A_k\equiv \frac p3 T_k(1+p\gamma_k)\pmod{p^3}\qquad(2m<k\le3m).}\tag{2}
\]

All denominator factors in (1)–(2) are p-units; every signed term retains its original index and coefficient. Define the explicit lower-grade certificate

\[
\mathscr L_p =
\sum_{k=0}^{2m}(6k+1)B_k
\left[1-p\alpha_k+\frac{p^2}{2}(\alpha_k^2-\beta_k)\right]
+\frac p3\sum_{k=2m+1}^{3m}(6k+1)T_k(1+p\gamma_k)
\quad\pmod{p^3}.\tag{3}
\]

Then `mathscr L_p ≡ W_(0,p)+W_(1,p) (mod p³)` **coefficientwise**, not merely after cancellation. Let `W_(2,p)=∑_(3m<k≤4m)(6k+1)A_k`. As `v_p(A_k)=3` above `4m`,

\[
\boxed{W_p\equiv\mathscr L_p+W_{(2,p)}\pmod{p^3}.}\tag{4}
\]

Consume the earlier proven grade-2 bridge `W_(2,p)/p²≡K_p\mathcal H_(m-1) (modp)`, where

\[
K_p=\frac{3m+2}{((3m+1)!)^4 216^{3m+1}},\quad
\mathcal H_{m-1}=
\left.(4+6z\partial_z)\sum_{j=0}^{m-1}
\frac{(-m+1)_j(m+1)_j(1)_j}{(3/2)_j^3}z^j\right|_{z=1/2}.
\]

**Correction:** the exact published grade-2 formula has numerator parameter `N+2=m+1` and `-N=1-m`; this notation uses both. The contribution is a finite length-`m` terminating sum.

Under the existing frozen first-digit input `W_p≡p (modp²)`, the lower-grade `mathscr L_p-p` is divisible by `p²`, and the original next-digit observer is now the **explicit smaller certificate**

\[
\boxed{\frac{W_p-p}{p^2}\equiv
\frac{\mathscr L_p-p}{p^2}+K_p\mathcal H_{m-1}\pmod p.}\tag{5}
\]

Equation (5) is a true equivalence at the original weighted W216 scalar observer, conditional only on the already stated frozen first-digit premise and existing grade-2 bridge. Its uniform zero remains the original LIFT scientific obligation (subject to the separately sourced W-to-Delta/R bridge); (1)–(4) are unconditional algebraic results.

## Proof

Use the exact parameter decompositions
\[
(1/3)_k=(-2m+p/3)_k,\quad
(1/2)_k=(-3m+p/2)_k,\quad
(2/3)_k=(-4m+2p/3)_k.
\]
For `k≤2m` no factor vanishes in the zero-order product. Divide by the signed falling factorials. The product consists of factors `1-p\lambda/(r-j)`. Expanding its product to second order gives `1-p\alpha_k+(p²/2)(\alpha_k²-\beta_k)`; the zero-order product is `B_k`, proving (1).

For `2m<k≤3m`, only the factor `j=2m` in `(-2m+p/3)_k` has positive p-valuation; it is exactly `p/3`. Remove this one factor before expansion. The remaining zero-order product is the positive p-unit `T_k`. Its first-order logarithmic correction is the signed sum `\gamma_k`, using `∑_{j\ne2m}(j-2m)^{-1}=H_{k-2m-1}-H_{2m}` and the two negative falling-factorial sums, proving (2).

For `3m<k≤4m`, both `j=2m` and `j=3m` are present and give exactly two p factors; after `4m`, a third factor `j=4m` appears. This proves the valuation partition and (4). The published grade-2 bridge supplies its leading unit and hence (5). All reductions take place after the explicit valuations certify integrality.

**BRC use:** carrier `(original k, valuation grade, signed 6k+1 weight, p-adic jet)`; operation = coefficientwise expansion followed by the weighted sum and division by `p²`. Observer preservation is verified at the declared mod-`p³` precision. Grade-0 and grade-1 lower digits, grade-2 positive/negative contributions, grade-3 omitted terms and the cross-grade carry are accounted for separately. The earlier 2304 and native H0/B0 branches are not identified with this arithmetic certificate.

## Executed exact checker

`research_notes/portable_direct/d25_w216_three_band_jet_20261110.py` implements (1)–(4) with integer modular arithmetic, and independently computes the **original** `(6k+1) binom(2k,k)^2 binom(3k,k)/216^k` for every `0≤k<p`. Verified all coefficients and weighted sums for `p=7,13,19,31,37,43,61,67,73,109,157,181,373`: **13/13 PASS** (no floats). At `p=373`, `m=62`, the original grade sums modulo `p³=51895117` are:

\[
W_0=28094360,\quad W_1=38687933,\quad W_2=37008314,\quad W_3=0.
\]

Therefore `mathscr L_373=14887176 (modp³)`; its normalized residue `(mathscr L_373-373)/373²=107 (mod373)`. The old grade-2 bridge independently gives `W_2/373²=266 (mod373)`. Their **signed** sum `107+266=373≡0` recovers the original numerical `W_373≡373 (mod373³)` without losing any valuation grade. Also `p=13`: lower 3, grade-2 10; `p=19`: lower 10, grade-2 9.

No full LIFT/JT2 uniform proof or formal Source admission is claimed. Native highest priority remains the **original-class** p=373 H0/B0 divided-power `[X]U mod139129`, rank, semilinear Frobenius direction, eta, signed kappa and Delta−R, under the existing support Issue #1559 (PENDING_OWNER). This new lower-grade proof does not execute that benchmark.

## Continuation and original Source request

Fresh Source continuation request `onhour11-20261110-0556-current-continuation` was QUEUED on last observation; reread its **same** target request for settlement, never resubmit. Own `recovery_status` was refused with `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`; a historical Source session registration is not an executable session key. No current winning CLAIM/run or native checkpoint is attested. The next proof step is a **finite WZ/Jacobi coupling** of the explicit lower-grade `mathscr L_p` with the previously proved grade-2 `K_p\mathcal H`, seeking the uniform cancellation in (5), while #1559 remains responsible for the native benchmark.
