# R242 — Exact first one-mode relative-error horizons at three rational parameters

Date: 2026-11-17 (Asia/Shanghai). Scientific status: AUTHOR_PROVED / EXACT_RATIONAL_EXECUTED / NOT_REVIEWED.

## Scope and source pins

This is independent portable continuation of the seven-source stationary reversible sticky-reset **scalar source-support principal-ideal-cardinality observer**. Frozen original scientific pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Immutable dependencies: R234@37786e0e0acb51ce36fa9ae68ec84ce28ad46dc6 (family), R239@f052feb457712a8f621e9111404e7da69a542196 (exact weights), R241@727b4b58a6072167f0864112e361d1e5be8cf1c9 (positive spectral decomposition and prior sufficient thresholds). Native P000 Heartbeat World, six spatial axes, separate time, twelve signed directions, provenance and joint BRC sign/port/source/branch/multiplicity/rational-weight/cross-moment state remain independently typed.

For s in the closed parameter extension [39/100,41/100], define

\[
\alpha=(1/5,1/4,3/10,9/20,s,2/3,(1691s-2615)/(2615s-3539)),
\]
\[
b_0=13/60,\quad b_j=(5/18)|1/2-\alpha_j|\ (1\le j\le6),\quad \pi_j=b_j/(1-\alpha_j),
\]
\[
P_{ij}=\alpha_i\delta_{ij}+(1-\alpha_i)\pi_j,\quad
Z=\sum_j b_j/(1-\alpha_j)^2,\quad \rho_j=b_j/((1-\alpha_j)^2Z).
\]

For each proper mask U of the six nonneutral sources let D_U={0} union U and W=(144,576,1440,4320,17280,86400,518400). The exact rational observable is

\[
\Phi_n(s)=\sum_{U\subsetneq[6]}W_{|U|}\rho_{D_U}^{\mathsf T}P_{D_U}^{n-1}{\bf1}
=\mathbb E[F_n]-W_6,\qquad n\ge2.
\]

With dominant killed-block Perron root r(s) (the source-3-deleted block) and its positive coefficient A(s), let E_n=(\Phi_n-Ar^{n-1})/(Ar^{n-1}).

## Theorem 1 — Strict event-time monotonicity of the *actual* error

For every real s in the specified interval, including its boundary extensions, E_n>0, E_(n+1)<E_n for every integer n>=2, and E_n tends to zero.

**Proof.** R237/R238 provide the positive finite spectral expansion E_n=\sum_{\ell\ne *}(c_\ell/A)(\lambda_\ell/r)^{n-1}. Every c_\ell is nonnegative, every 0<\lambda_\ell/r<1, and the source-4-deleted block contributes one strictly positive subleading coefficient. Each positive summand strictly decreases. The same strict spectral separation holds at the two endpoints. Therefore verifying E_(n-1)>threshold and E_n<threshold establishes *the first* integer crossing. QED.

## Theorem 2 — Exact first thresholds

Define N_d(s)=min{n>=2:E_n(s)<1/d}. Exact rational certificates yield:

| s | N_100 (1%) | N_1000 (0.1%) | scope |
|---|---:|---:|---|
| 39/100 | 513 | 768 | left boundary extension |
| 2/5 | 608 | 912 | interior |
| 41/100 | 752 | 1128 | right boundary extension |

The R241 parameter-uniform sufficient thresholds were 1073 and 1449; at the interior anchor s=2/5 the *actual* first horizons are 608 and 912.

**Proof by exact integer and rational enclosures.** The companion standard-library Python verifier constructs all 63 killed blocks. Writing P=H/M and rho=w/C with integer H,w and common denominators M,C, it propagates each integer row vector under its own killed H_D, retaining exact \rho_D^T P_D^(n-1)1. Thus it obtains the exact rational \Phi_n for each reported n and n-1.

The secular function f(x)=\sum_{j\ne3}b_j/(x-\alpha_j)-1 strictly decreases above the holding poles. Exact bisection isolates the unique Perron root between consecutive rational numerators L/10^30 and (L+1)/10^30 by checking f(L/10^30)>0>f((L+1)/10^30). Write r_-<r<r_+. Let

\[
S(x)=\sum_{j\ne3}\frac{b_j}{(1-\alpha_j)(x-\alpha_j)},\qquad
Q(x)=\sum_{j\ne3}\frac{b_j}{(x-\alpha_j)^2}.
\]

Both S and Q decrease on the root interval. From the pinned amplitude identity A=W_5 S(r)^2/(ZQ(r)), valid rational amplitude bounds are

\[
A_-=\frac{W_5S(r_+)^2}{ZQ(r_-)}<A<
A_+=\frac{W_5S(r_-)^2}{ZQ(r_+)}.
\]

For each target d and candidate n, the actual program checks by exact rational cross-multiplication

\[
d\Phi_n<(d+1)A_-r_-^{n-1},\qquad
d\Phi_{n-1}>(d+1)A_+r_+^{n-2}.
\]

These strictly certify E_n<1/d<E_(n-1). Theorem 1 proves minimality. All six threshold/predecessor pairs PASS. Each verification record preserves the root bracket, exact rational moment hashes, integer bit sizes and two comparison booleans. No floating-point agreement is used as proof.

## Theorem 3 — Local stability

At each of the three parameters in Theorem 2 there exists a nonempty neighborhood relative to the closed parameter extension on which both integer horizons remain unchanged.

**Proof.** For fixed n, \Phi_n(s) is rational and continuous, while the isolated simple positive Perron root and its amplitude are continuous functions of s. The exact strict predecessor/threshold inequalities persist on an open relative neighborhood. Theorem 1 completes the first-crossing claim. QED.

The three anchors alone do not settle the maximum exact horizon over the entire real parameter interval or monotonicity in s. Candidate next step: prove/disprove parameter monotonicity; otherwise certify a whole-interval bound by rational subdivision with exact Phi, A and r interval enclosures. Compare bit complexity against the 230-order recurrence and 256-state propagation. Native BRC EffectHistogram integration remains NOT_EXECUTED. Independent mathematical review NOT_REVIEWED; no formal CLAIM, Result, Review or Foundation acceptance is asserted.

## Reproduction

Run: python3 R242_exact_anchor_horizons.py > R242_verification.json

The verifier is pure standard-library Fraction/integer arithmetic; it checks all 63 proper masks, the three rational parameter values, the two targets and immediate predecessors. The saved JSON is its actual PASS output. Theorem 1 and continuity are author proofs; numerical verification of the all-real claim is not asserted.
