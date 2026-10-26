# D25/LIFT — Third p-adic digit of the exact oriented Green source kernel

Date: 2026-10-26. Research lane `chatgpt-research-hourly-enterprise-math-20260923`; parent Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` **unchanged**.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** This is a new third-digit extension of the author's existing two-digit factorial Ward source formula, not another credit for its previous modulo-p² theorem. No native original-class CM run, native checkpoint or reviewer acceptance is claimed.

## Input and exact coefficients

Use the source-faithful oriented Ward identity and the previous modulo `p²` coefficient factorization in `20261026_hourly_d25_ward_two_digit_lift_r11.md`. Put, for every prime `p=6m+1>=7`, `N=2m-1` and

\[
F_m=\frac{2^{4m-1}(2m-1)!(2m)!}{(4m)!},\qquad
C_t=\frac{4^t(t!)^2}{(2t)!},\qquad
E_t=\frac1{2N+1}-\frac1{2t+1}
+\sum_{r=t+1}^{N}\left(\frac1{2r-1}-\frac1{2r}\right).
\]

Keep the **exact** rational finite Green coefficients and left propagator

\[
D_h=\frac{1}{p-2h-1}\prod_{k=h+1}^{2m-1}\frac{p-2k}{p-2k-1},\qquad
P=\prod_{k=1-2m}^{2m-1}\frac{p-2k}{p-2k-1}.
\]

The unique `p` factor arises at `k=0`; `D_{-t-1}/p`, `P/p` and `F_m,C_t` are p-local units.

## New theorem: explicit three-digit coefficients

Define the (fully p-integral) second-order odd/even reciprocal contrast

\[
\Delta_a=\sum_{r=1}^{a}\left(\frac1{(2r-1)^2}-\frac1{(2r)^2}\right),\qquad \Delta_0=0,
\]
\[
H_t^{(2)}=\frac1{(2t+1)^2}+\frac1{(2N+1)^2}+\Delta_t+\Delta_N.
\]

Then for every `0<=t<N`:

\[
\boxed{\frac{D_{-t-1}}p
\equiv -\frac{F_mC_t}{2t+1}
\left[1+pE_t+\frac{p^2}{2}\left(E_t^2+H_t^{(2)}\right)\right]\pmod{p^3}.}\tag{A}
\]

For the true left-to-right terminal factor:

\[
\boxed{\frac Pp\equiv
-F_m C_N\left[1+\frac{p}{2N+1}
+p^2\left(\frac1{(2N+1)^2}+\Delta_N\right)\right]\pmod{p^3}.}\tag{B}
\]

**Proof.** The exact p-extracted negative kernel factors as
\[
\frac{D_{-t-1}}p=
\frac1{p+2t+1}\,\frac1{p-1}
\prod_{r=1}^t\frac{p+2r}{p+2r-1}
\prod_{k=1}^N\frac{p-2k}{p-2k-1}.
\]
Divide by the p-unit leading factor `-F_m C_t/(2t+1)`. The ratio becomes
\[
\frac1{1+p/(2t+1)}\frac1{1-p}
\prod_{r=1}^t\frac{1+p/(2r)}{1+p/(2r-1)}
\prod_{k=1}^N\frac{1-p/(2k)}{1-p/(2k+1)}.
\]
Expanding the **finite** p-adic logarithm modulo `p³`, with `log(1+x)=x-x²/2`, gives exactly
\[
\log\mathrm{ratio}=pE_t+\frac{p^2}{2}
\left(\frac1{(2t+1)^2}+\frac1{(2N+1)^2}+\Delta_t+\Delta_N\right)\pmod{p^3}.
\]
Exponentiating with `exp(y)=1+y+y²/2` establishes (A). These truncated formal operations need only division by 2, a unit for `p>=7`; all `2r±1` denominators here are also p-units. For `P/p`, drop the initial `(p+2t+1)^{-1}`, include all negative factors through `r=N`, and repeat. Its log's linear term is `p/(2N+1)`, and quadratic coefficient is `p²[2\Delta_N+1/(2N+1)^2]/2`. Exponentiation gives (B). QED.

## New source-faithful Ward law modulo p³

For the true channel-tagged sources `S_h^{ab}=J_h^{ab}+E_h^{ab}`, left edge `Y_{1-2m}^{ab}` and channels `(a,b)=(0,2),(1,2),(0,3)`, insert (A),(B) into the inherited **exact** Ward identity:

\[
\boxed{\begin{aligned}
\frac1{pF_m}\sum_{h=0}^{2m-1}D_h S_h^{ab}\equiv {}&
\sum_{t=0}^{N-1}\frac{C_t}{2t+1}
\left[1+pE_t+\frac{p^2}{2}\big(E_t^2+H_t^{(2)}\big)\right]S_{-t-1}^{ab}\\
&-C_N\left[1+\frac p{2N+1}
+p^2\left(\frac1{(2N+1)^2}+\Delta_N\right)\right]
Y_{1-2m}^{ab}\pmod{p^3}.
\end{aligned}}\tag{C}
\]

As before, the LHS is p-integral **before division**. The formula keeps negative-orientation `J+E`, left cutoff, the three Hasse channels and p-local valuations. It describes this Ward observable only; it does not by itself cancel the independently weighted original Clausen lower-triangle reflection nor the infinity port.

## Evidence and nontrivial example

Python stdlib exact-Fraction calculations checked each individual (A),(B) for **15 target primes** `p=7,13,19,31,37,43,61,67,73,79,97,103,109,127,139`, `330` coefficient assertions PASS. The same verifier independently constructed actual corrected Hasse jets and both `J+E` boundary terms for `p=7,13,19,31,37,43`, adding `18` channel-level checks of (C). **348 author assertions PASS**, not an independent mathematical review.

At `p=13`, `N=3`, the normalized negative-kernel ratios
`(D_{-t-1}/p)/[-F_mC_t/(2t+1)]` for `t=0,1,2` are respectively
`391,1717,898 mod 2197`.
Their exact `p²` correction coefficients modulo 13 are `7,4,5`, and the terminal ratio `(P/p)/[-F_m C_3]=1379 mod2197` has second correction coefficient `10 mod13`. These supply a sharper observer than the prior two-digit result.

## BRC reuse, status and next exact action

**BRC COMPOSE_APPLIED**: source carrier retains signed `(j,ell)` orientation, Hasse channel, two finite boundary faces, integer prime valuation and successive p-adic digits; future operation here is a Green linear functional, not general quadratic-rank compression. No auxiliary Laurent coordinate is equated with primitive six-dimensional P000 geometry.

Consume the just-derived lower-orientation unit-safe adjoint in `20261026_hourly_d25_negative_orientation_source_adjoint_r11.md`: next join the original `T02,U02,T12,T03` reflection observables with full corrected `k-1,k-2` coupling, the third-digit Ward kernel and distinct infinity ports. A mismatch must be reported as a source-labelled remainder, not an assertion of zero. Original same-class `H0/B0`, `[X]U mod p²`, Frobenius `eta`, `kappa`, `Delta_p-R_p`, native experiments and independent review still missing. Parent D25/LIFT/JT2 **OPEN**.

The native continuation read in this run verified the existing `SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED` checkpoint but `execution_authorized=false`; it did not issue CLAIM/OPEN/checkpoint. Portable GitHub storage does not change Source admission.
