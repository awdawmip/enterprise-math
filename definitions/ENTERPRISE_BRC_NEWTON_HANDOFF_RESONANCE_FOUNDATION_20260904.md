# Enterprise BRC Newton Handoff / Resonance Foundation Addendum

**Effective:** 2026-09-04  
**Status:** CANDIDATE FOUNDATION BACKFLOW pending dedicated CI  
**Parent:** `ENTERPRISE_BRC_NEWTON_RECURSION_FOUNDATION_20260904.md` (`WBRC-T52/T53`)

This addendum transports the main-backed results of PR #1191 and PR #1193 into the all-research Weighted-BRC foundation.  It does not change the Boolean R023 base, does not replace the critical smallest-positive-root selector of WBRC-T41, and does not introduce a generic algebraic-number field or complete Puiseux engine.

## WBRC-T54 — single-generator irrational translated-root handoff and absorption

Let a finite Newton jet have rational polynomial coefficients

\[
J_s(y)=\sum_\sigma \sigma^s P_\sigma(y),\qquad P_\sigma\in\mathbb Q[y],
\]

with finite Newton-scale support in

\[
\mathcal S_{\rm rad}=\mathbb Q_{>0}^{\times}\otimes_{\mathbb Z}\mathbb Q.
\]

Suppose the scale-one edge polynomial has an exactly isolated selected real root \(\beta\), possibly irrational.  Define the single-root evaluation carrier

\[
\mathcal A_\beta=\{[g]_\beta:=g(\beta):g\in\mathbb Q[x]\}.
\]

Selected-root semantic zero/equality/sign are decidable by polynomial gcd / Sturm root isolation and rational interval refinement.  After the Newton translation

\[
y=\beta+\theta^s x,
\]

every Taylor coefficient is exactly

\[
\frac{P_\sigma^{(k)}(\beta)}{k!}
=
\left[\frac{P_\sigma^{(k)}}{k!}\right]_\beta.
\]

Therefore a first irrational **translated** root encountered while the live coefficient carrier is still \(\mathbb Q\) may be adopted as the sole selected-root generator.  The residual jet remains finite over \(\mathcal S_{\rm rad}\) with coefficients in \(\mathcal A_\beta\).  Subsequent rational translated selected roots continue exactly in the same single-generator carrier.

### Absorption certificate

If coefficients already live in a single selected-root carrier \(\mathcal A_\alpha\) and a proposed later selected root has a supplied representation

\[
\beta=[h]_\alpha,
\]

then exact semantic verification

\[
E([h]_\alpha)=0
\]

together with an independent exact selected-real-branch certificate is sufficient to keep the recursion inside \(\mathcal A_\alpha\).  This is a **verification interface**, not a general algorithm for finding \(h\).

Hence the genuine multi-generator boundary is narrower than “an irrational translated root appeared”:

\[
\boxed{
\text{old algebraic data remain live}
+
\text{new irrational root}
+
\text{no absorption certificate}
}
\]

is the first point at which this Foundation no longer supplies a single-generator carrier.

### Main-backed evidence

PR #1191 dedicated exact gate:

- 22 irrational-translated-root repeated-block BRC samples;
- 88 real-root selector / multiplicity checks;
- 8,986 handoff recursive checks;
- 8,386 recursive-vs-direct semantic checks;
- 7,508 rational continuation checks;
- absorption certificate and Fibonacci/golden witnesses PASS.

The first failed PR #1191 run also exposed the resonance law formalized as WBRC-T55 below.

## WBRC-T55 — affine Newton scale pushforward and resonance aggregation

Fix one exact Newton step with selected root \(x_0\), multiplicity \(r\), and Newton scale \(\theta\).  For

\[
J_s(x)=\sum_\sigma \sigma^sP_\sigma(x)
\]

write

\[
P_\sigma(x_0+\theta^s y)
=
\sum_k a_{\sigma,k}\theta^{ks}y^k.
\]

Every Taylor source atom

\[
(\sigma,k,a_{\sigma,k})
\]

is sent to residual scale

\[
\boxed{\rho=\Phi_{\theta,r}(\sigma,k)=\sigma\theta^{k-r}}.
\]

For each residual scale define

\[
Q_\rho(y)
=
\sum_{\Phi_{\theta,r}(\sigma,k)=\rho}
 a_{\sigma,k}y^k.
\]

Then the Newton transform is the exact finite pushforward identity

\[
\boxed{
\theta^{-rs}J_s(x_0+\theta^s y)
=
\sum_\rho \rho^sQ_\rho(y).
}
\]

Two Taylor sources are scale-resonant iff

\[
\sigma_1\theta^{k_1-r}
=
\sigma_2\theta^{k_2-r},
\]

equivalently

\[
\boxed{
\sigma_1/\sigma_2=\theta^{k_2-k_1}.
}
\]

In rational prime-valuation coordinates this is the finite rational-linear equality

\[
v_p(\sigma_1)-v_p(\sigma_2)
=
(k_2-k_1)v_p(\theta)
\quad\forall p.
\]

The next Newton edge polynomial is exactly the residual \(\rho=1\) fiber.

### Mandatory operation order

The operation-safe order is

\[
\boxed{
\text{Taylor expansion}
\to
\text{scale pushforward}
\to
\text{equal-scale aggregation}
\to
\text{semantic zero reduction}
\to
\text{root/contact analysis}.
}
\]

Source-level nonzero terms are not individually root-active after aggregation.  Signed coefficients appearing here are determinant/characteristic algebraic-compression coefficients, not signed branch masses.

### Composition

Successive Newton pushforwards compose affinely.  Staged recursive substitution and one-shot nested substitution give the same residual scale-polynomial jet after equal-scale aggregation.  This provides the provenance-level representation law underlying the recursive-vs-direct identities already promoted in WBRC-T52.

### Main-backed evidence

PR #1193 dedicated exact gate:

- 576 synthetic Newton samples;
- 2,240 independent-pushforward / production checks;
- 1,728 Taylor-atom checks;
- 576 resonant scale fibers;
- 1,216 exact valuation-resonance criterion checks;
- 576 scale-one edge checks;
- 1,152 source-enumeration-order invariance checks;
- resonant edge, aggregation cancellation, staged/one-shot, and PR #1191 resonance/separation witnesses PASS.

### PR #1191 resonance witness

With

\[
\eta=\frac12,\qquad \tau_1=\frac13,
\]

the original trial \(\tau_2=1/4\) gives

\[
\frac{\tau_2}{\tau_1}
=
\frac{\eta^2}{\tau_1}
=
\frac34.
\]

The declared common-shift contribution and an intrinsic nonlinear contribution therefore occupy the same residual scale and must be combined in the third edge polynomial.  With \(\tau_2=3/10\),

\[
\frac{\tau_2}{\tau_1}=\frac9{10}>\frac34,
\]

so the scales separate and the next pure translated double root \(-1\) is recovered.

## Negative boundaries

### WBRC-N42 — irrational translated root does not automatically imply multi-generator

A first irrational translated root over rational coefficients may be handed off to a new single-root evaluation carrier.

### WBRC-N43 — handoff cannot discard live old algebraic data

If an old algebraic generator still appears in coefficients, simply replacing it by the new root is not justified.

### WBRC-N44 — absorption certificate is not a root-expression search algorithm

`beta=[h]_alpha` is an explicit candidate to verify, not a promise that such an `h` can always be found.

### WBRC-N45 — Newton resonance is not signed branch interference

Resonant signed coefficients arise after determinant/characteristic algebraic compression; positive branch semantics remain separately typed.

### WBRC-N46 — residual Newton jet does not preserve source provenance

Once Taylor atoms are pushed to the same residual scale/degree and aggregated, the residual jet does not identify their original source layers.

### WBRC-N47 — real-root selector does not replace WBRC-T41 critical root semantics

The general isolated-real-root carrier introduced for translated-root handoff is a downstream exact selector.  WBRC-T41 remains the canonical smallest-positive-root state for criticality polynomials.

## Prior-art boundary

Newton polygons, valuations, Puiseux transforms, Sturm isolation and simple algebraic-root evaluation are classical mathematics.  No generic novelty is claimed for them.  The promoted Enterprise contribution is the typed exact BRC integration, the single-generator/multi-generator boundary, the resonance pushforward law, and the operation-safe aggregation order.
