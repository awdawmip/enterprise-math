# PREFIX-648-R6 — Positive fourth cumulant and negative third cumulant on a nonzero BRC parameter rectangle

Date: 2026-11-10 (Asia/Shanghai). Frozen scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Status: `AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED`.

## Scientific object

Use the unchanged signed two-informative-direction BRC first-stop statistical observer: two separate Bernoulli mark histories with 189 finite survivor layers; two independent rate-one Poisson information clocks; their maximum `Y(p,z)`; and the marked-thinning discrete action stopping count `T_q(p,z)`. Branch identities, signs and 96-port provenance are retained in the underlying model. The cumulants are only a declared observer of that model; the two probability coordinates do not retype the six-dimensional P000 native space.

The exact central witness from PREFIX-645 (`enterprise-math@f11c0345bf89321aba48d90671c244bdec25d416`) at `(p0,z0)=(1/6,19/128)` supplies `E[Y0]<109`, `336<Var(Y0)<337`, `-1210<kappa3(Y0)<-1209`, and `50374<kappa4(Y0)<50375`. PREFIX-646 (`@d64c99d8e6ea82f6c1d803df9f93b91e70eaf7b0`) supplies the exact all-order moment perturbation bound
`|m_r(p,z)-m_r(p',z')| <= 378*(189)_r*(|p-p'|+|z-z'|)`,
where `m_r=E[Y^r]` and `(189)_r` denotes the rising factorial. PREFIX-647 (`@0dcaaf8c51a6cd38c8bc0d9183f916246e1e377c`) supplies `E[Y]<110`, `Var(Y)>334`, `kappa3(Y)<-322` on coordinate half-width `2^-25`.

## Theorem 648.1

Put `h=2^-29`. For every admissible pair `(p,z)` satisfying
`|p-1/6|<=h` and `|z-19/128|<=h`,
we have the strict uniform inequalities

`E[Y]<110; Var(Y)>334; kappa3(Y)<-322; kappa4(Y)>14638.`

For every real `q>=12` for which the original marked-thinning action count is defined,

`kappa3(T_q)<0`, and
`kappa4(T_q)>14638*q^4+1932*q^3+2338*q^2-110*q>0.`

Consequently `kappa4(T_12)>307207416`, `kappa4(T_24)>4884589104` throughout the closed two-parameter rectangle. This is a continuous-parameter distribution-shape theorem *within the frozen statistical observer*.

## Exact proof

Let `delta=|p-p0|+|z-z0|<=2^-28`. The inherited moment coupling lemma gives `L_r=378*(189)_r`, hence `L1=71442`, `L2=13573980`, `L3=2592630180`, `L4=497784994560`.

From `m2=Var+mu^2` and `m3=kappa3+3*mu*Var+mu^3`, the strict central-point envelopes yield `m2(p0,z0)<12218` and `m3(p0,z0)<-1209+3*109*337+109^3=1404019`. Direct rational comparisons give `L1*delta<1`, `L2*delta<1`, `L3*delta<10`. On the entire segment from the center to any rectangle point, `m1<110`, `m2<12219`, `m3<1404029`.

Write `M1=110, M2=12219, M3=1404029`. The exact fourth raw-moment cumulant identity is
`kappa4=m4-4*m1*m3-3*m2^2+12*m1^2*m2-6*m1^4`.
Telescoping each product difference under the just-proved local envelopes yields

`|kappa4(p,z)-kappa4(p0,z0)|<=K4*delta`, with

`K4=L4+4*(M1*L3+M3*L1)+6*M2*L2+12*(M1^2*L2+2*M1*M2*L1)+24*M1^3*L1`.

Exact integer arithmetic gives `K4=9592604213472` and `K4*2^-28=299768881671/8388608<35736`. Consequently,
`kappa4(p,z)>50374-299768881671/8388608=122798857721/8388608>14638`.

This rectangle is contained in PREFIX-647's, so the first three moment/cumulant inequalities hold. Apply PREFIX-645's fourth-order Stirling transform

`kappa4(T_q)=q^4*kappa4(Y)-6*q^3*kappa3(Y)+7*q^2*Var(Y)-q*E[Y]`.

Substitution gives the explicit strict polynomial lower bound. After dividing by `q>0`, its lower polynomial `14638q^3+1932q^2+2338q-110` is positive at 12 and strictly increasing for `q>=12`. Similarly, `kappa3(T_q)/q<-322q^2-1002q+110<0` for `q>=12`, by the negative slope and value at 12. QED.

## Verification and evidence status

`PREFIX648_R6_POSITIVE_FOURTH_CERTIFICATE.py` regenerates `PREFIX648_R6_RESULTS.json` and checks all arithmetic with Python standard-library integer/Fraction operations, reporting `ALL_CHECKS_PASS`. It verifies the **new implication conditional on the exact PREFIX-645/646/647 inputs**. We did not reexecute the 189-layer survivor certificate, rerun the native 96-port BRC dynamics, or conduct independent mathematical review. The assertion is not a formal Source Result/Review or Foundation promotion.

BRC use: `REUSE_APPLIED` to the existing signed two-direction observer, exact moment coupling and Stirling-transform interfaces. Preserve branch/provenance and discrete action-clock semantics; fourth cumulant is a richer observation than mean/variance.

## Next discriminating unit

Compute certified local Bernstein/score bounds for derivatives of the *centered* fourth cumulant and test enlargement toward `p in [3/20,1/6]` and `z in [37/256,39/256]`. A negative exact witness would refute the corresponding universal positivity claim at its proper scope. Independently replicate the PREFIX-645 center witness and audit the PREFIX-646 moment perturbation lemma before promotion. The mother objective remains the two-parameter global maximum of sampled stopping-time variance.
