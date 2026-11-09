# PREFIX-640-R6 — Whole-valley transverse uniqueness strip, 32 times wider

Date: 2026-11-09 (Asia/Shanghai). Scope: independent TASK_RESEARCH. Status: AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED. Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.

## Question and model

In the signed two-informative-direction BRC finite first-passage statistical observer of PREFIX-621/622, let \(Y\) be the maximum of the two unit-rate informative-Poisson stopping times, \(\mu(p,z)=E[Y]\), \(W(p,z)=\operatorname{Var}(Y)\), and
\[
F_q(p,z)=W(p,z)-\mu(p,z)/q,\qquad V_q(p,z)=q^2F_q(p,z).
\]
The two actual native sampling choices are \(q=12,24\); the formulas interpolate for real \(q\in[12,24]\). These \(p,z\) are signed-observer statistical parameters, not the spatial axes of P000's native six-dimensional discrete Cell world. The original native graph and scientific input pin remain unchanged.

The full mother objective is to determine the global maximum of \(V_q\) over its reduced two-parameter domain. This note asks whether the entire interior valley interval has a unique minimum on a nonzero-width transverse strip wider than PREFIX-636.

## Theorem 640.1

Let \(I=[3/20,1/6]\), \(z_0=19/128\), \(h=2^{-28}\), and \(J=[z_0-h,z_0+h]\). For every real \(q\in[12,24]\), \(p\in I\), \(z\in J\),
\[
\boxed{273<\mu_p(p,z)<322,\qquad 4000<F_{q,pp}(p,z)<71000}.
\]
Moreover \(F_{q,p}(3/20,z)<0<F_{q,p}(1/6,z)\). Thus \(p\mapsto F_q(p,z)\) is strictly convex over the *entire* \(I\), has one and only one critical point \(c(q,z)\in(3/20,1/6)\), and that point is its unique global minimum over \(I\). The local optimizer is analytic in \(q,z\), strictly decreases with \(q\), and
\[
\boxed{\frac{91}{568000}<c(12,z)-c(24,z)<\frac{161}{48000}}\quad(z\in J).
\]
Compared with PREFIX-636, the transverse radius increases from \(2^{-33}\) to \(2^{-28}\), exactly 32-fold, and the first-parameter interval expands from \([4/25,161/1000]\) to all of \([3/20,1/6]\). These new estimates are conservative; the former PREFIX-636 bounds remain available on its smaller domain.

## Proof from exact predecessor certificates

**PREFIX-639 (fixed-slice exact Bernstein certificate):** for every \(p\in I\), real \(q\in[12,24]\), at \(z=z_0\),
\[
274<\mu_p(p,z_0)<321,\qquad 27100<F_{q,pp}(p,z_0)<48100.
\]

**PREFIX-636 (uniform mixed derivatives):** everywhere on the parameter square, for \(q\ge12\),
\[
|\mu_{pz}|\le K_0=189\cdot188^2=6680016,\quad
|F_{q,ppz}|<K_2=25\cdot189^2\cdot188^3=5933858212800.
\]
These follow from Bernstein survivor coefficients and negative-binomial weights in that same frozen observer. All quantities use identical model definitions in the three cited sources.

**PREFIX-631 (uniform endpoint sign):** for *all* \(z\in[37/256,39/256]\) and all \(q\ge12\),
\[
F_{q,p}(3/20,z)<0<F_{q,p}(1/6,z).
\]

Our interval \(J\subset[37/256,39/256]\) so the endpoint signs hold without a new local gradient estimate. Integrating the mixed derivative bounds along \(z_0\to z\), for every \(p\in I\) gives
\[
|\mu_p(p,z)-\mu_p(p,z_0)|\le K_0h,\quad
|F_{q,pp}(p,z)-F_{q,pp}(p,z_0)|<K_2h.
\]
The exact rational products are
\[
K_0h=\frac{417501}{16777216},\qquad
K_2h=\frac{92716534575}{4194304}.
\]
Fraction arithmetic verifies
\[
274-K_0h>273,\quad321+K_0h<322,\quad
27100-K_2h>4000,\quad48100+K_2h<71000.
\]
This proves both derivative envelopes throughout \(I\times J\). Strict positivity of \(F_{q,pp}\) plus the endpoint signs implies existence and uniqueness of the interior minimizer. Analyticity follows from the finite survivor polynomial model and the implicit function theorem.

Implicitly differentiating \(F_{q,p}(c(q,z),z)=0\) yields
\[
c_q=-\frac{\mu_p(c(q,z),z)}{q^2F_{q,pp}(c(q,z),z)},\quad
-\frac{322}{4000q^2}<c_q<-\frac{273}{71000q^2}<0.
\]
Integrating from \(q=12\) to \(24\), with \(\int_{12}^{24}q^{-2}\,dq=1/24\), gives
\[
\frac{273}{24\cdot71000}<c(12,z)-c(24,z)<\frac{322}{24\cdot4000},
\]
reducing to the announced rational fractions. QED.

## Corollary 640.2 — optimal-value curvature

Define \(\Phi(t,z)=\min_{p\in I}(W(p,z)-t\mu(p,z))\) for \(t\in[1/24,1/12]\), \(z\in J\). Since the minimizer is unique and interior,
\[
-\Phi_{tt}(t,z)=\frac{\mu_p(c(1/t,z),z)^2}{F_{1/t,pp}(c(1/t,z),z)},\quad
\boxed{\frac{273^2}{71000}<-\Phi_{tt}<\frac{322^2}{4000}}.
\]
Hence the optimized statistical-observer value is uniformly strongly concave on the full new strip. The corresponding exposed mean–variance arc has \(4000/322^2<d^2B/dA^2<71000/273^2\), in the notation of PREFIX-638.

## Executed arithmetic verification and scientific scope

The companion `PREFIX640_R6_FULL_INTERVAL_TRANSVERSE_CERTIFICATE.py` checks all 17 arithmetic assertions exactly using Python's Fraction, including both rational products, all four strict margins, domain inclusion, the integrated gap, and the 32-fold width. Execution result on 2026-11-09: `ALL_CHECKS_PASS 17`. The JSON preserves the exact inputs and comparison outputs. It is a certificate of the **logical/arithmetic implication from PREFIX-631/636/639**; it does not rerun the predecessor's 189-layer recurrence or the native 96-port graph. Predecessor mathematical results and this deduction are author-proved, awaiting independent review.

## Next exact research unit

Seek \(F_{q,pp}>0\) over the larger \(I\times[37/256,39/256]\) using two-variable Bernstein controls and adaptive subdivision in \(z\). Checking \(q=12\) and \(q=24\) suffices for intermediate \(q\) because \(F_{q,pp}\) is affine in \(1/q\). PREFIX-631 already supplies endpoint gradient signs on that full bracket. A successful exact bivariate certificate extends unique valley structure across the entire band; a failed Bernstein cell directs further subdivision or an exact sign witness. The global two-parameter maximum of \(V_q\) remains the open mother objective.

## Fixed provenance

- PREFIX-631 `enterprise-math@cab564fd9a112feed4a5a1fac0ee5556ebe7d7b6:research_notes/portable_direct/2026-11-09_prefix631_r6_uniform_gradient_reversal_valley.md`.
- PREFIX-636 `enterprise-math@c70457fde1d39265b126976bd92126731c31c23e:research_notes/portable_direct/2026-11-09_prefix636_r6_transverse_unique_valley_stability.md`.
- PREFIX-639 `enterprise-math@6acbf4f472a48d846859a71a31af243808961cff:research_notes/portable_direct/2026-11-09_prefix639_r6_full_central_valley_convexity.md`.
- Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
