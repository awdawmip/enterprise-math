# X6 R63 — Positive-BRC star moments with an unknown common offset: exact quotient and precision certificate

Date: 2026-11-21 (Asia/Shanghai)
Line: RS-X6-NATIVE-TIME-DYNAMICS
Scientific status: CONDITIONAL_AUTHOR_PROOF / EXACT_INTEGER_RATIONAL_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED

## Input, sources, typing

This independently preserved research unit continues X6 R62 (research_notes/portable_direct/2026-11-20_x6_r62_truncated_star_moment_integer_lattice.md, blob 226f5e9b9545e26f873dbc1febaa56e82bd7559a, immutable paper commit 2667ffe1c2fd9eb25a1812d1d6535b5022574966) and the R61 repeated-A positive-BRC observation. R49 provides a distinct earlier common-offset motivation.

The frozen scientific P000 pin remains awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. Current normative documents were independently read from the present canonical main; they do not change frozen scientific inputs. P000's six native spatial axes, separate time, Cell/Link provenance and primitive whole-triad TRIADIC_CLOSURE_E are preserved.

Fix known integers p>=D>=1, p named A Ports and p named B Ports, a p by p binary success-incidence S, and Port-independent positive event weights u,v>0. Each successful AB branch (i,j) has positive BRC mass uv, and only successful named branches contribute. In a repeated-A star of depth t, t independently reset AB trials must use exactly the same first-source Port i, while B choices are free. Its normalized positive-branch mass is

\[
m_t=Z_\mathrm{star}(t)/(uv)^t=\sum_{d=0}^{D}c_d d^t,\qquad 1\le t\le D,
\]

where c_d counts rows of S with exactly d successful B choices; c_d are nonnegative integers summing to p. The convention m_0=p represents the known Port population, not a further measured biased channel. Depth t is not physical heartbeat time. Our instrument reports y_t=m_t+b for t=1,...,D, with one unknown real additive bias b in the NORMALIZED units (not raw mass units).

## R63.1 Complete exact solution fiber

Let s(k,t) denote signed Stirling numbers of the first kind, determined by s(0,0)=1 and

\[
s(k,t)=s(k-1,t-1)-(k-1)s(k-1,t).
\]

For k=2,...,D define

\[
B_k=\frac1{k!}\sum_{t=1}^k s(k,t)y_t.
\]

**Theorem.** Each B_k is an EXACT integer independent of b. All high-degree counts are uniquely recovered via

\[
c_d=\sum_{k=d}^{D}(-1)^{k-d}{k\choose d}B_k,\quad d=D,D-1,\ldots,2.
\]

Put R=p-\sum_{d=2}^D c_d and beta=y_1-\sum_{d=2}^{D}d c_d. For every genuinely attainable observation vector, its ENTIRE set of nonnegative-integer histograms and real biases is

\[
(c_0,c_1,b)=(R-j,j,\beta-j),\quad j=0,1,\ldots,R,
\]

with c_2,...,c_D fixed by the inversion. Hence the fiber has exactly R+1 elements (one when R=0). The only information loss is the count allocation between degrees 0 and 1 with its compensating common offset. Recording the integer j uses exactly at least ceil(log2(R+1)) bits for a fixed fiber, and that many bits suffice. Alternatively an exact calibrated b, c_0, or c_1 restores the histogram.

**Proof.** The falling-factorial identity

\[
(d)_k=\sum_{t=0}^k s(k,t)d^t=k!{d\choose k}
\]

applies to every integer d>=0. Since for every k>=2,

\[
\sum_{t=1}^{k}s(k,t)=(1)_k=0,
\]

the common bias vanishes. Thus B_k=\sum_{d=k}^D {d\choose k}c_d. This is a unit-diagonal upper-triangular linear system for c_2,...,c_D. Exact binomial inversion gives the formula. Total count fixes c_0+c_1=R, and y_1 fixes c_1+b=beta. Every integer j in [0,R] yields an allowable histogram and b: changing a degree-0 row to degree-1 increases EVERY positive-depth moment by one, exactly canceled by reducing b by one. No other candidates exist because the high-degree triangular system is invertible. D=1 has an empty high-degree system and correctly gives R=p.

An equivalent exact kernel certificate is this: if an integer histogram difference h has total sum zero and all positive-depth moment differences are a common number C, then h=C(e_1-e_0). Subtract this vector and apply invertibility of the full (D+1) by (D+1) Vandermonde matrix at 0,...,D. Hence this is the entire offset-blind observer kernel, not an artifact of a numerical example.

## R63.2 Noisy observer, uniform stable high-degree recovery

Suppose instead y_t=m_t+b+e_t, where the single unknown b is unchanged and each normalized channel has |e_t|<=eta. Form the same Bhat_k from noisy y for k>=2. Then

\[
|\widehat B_k-B_k|
\le \frac{\eta}{k!}\sum_{t=1}^k |s(k,t)|=\eta,
\]

because the unsigned first-kind Stirling numbers enumerate all k! permutations. Therefore at eta<1/2, rounding each Bhat_k to the nearest integer exactly recovers every B_k and consequently all c_2,...,c_D and R, for arbitrary p,D satisfying the hypotheses. The remaining c_0/c_1 ambiguity is already present at zero noise. The bound concerns exact rational normalized measurements; it does not assert constant computational bit cost.

The constant 1/2 is SHARP as a *single bound uniform across all p,D>=2*. For p=D=2 compare c=(1,0,1), with (m_1,m_2)=(2,4), against c'=(0,2,0), with (2,2). Give the candidates biases 0 and 1 respectively. The two theoretical observed vectors are (2,4) and (3,3). Their midpoint y=(5/2,7/2) is within eta=1/2 of both yet c_2 differs. No assertion is made that every fixed p,D attains this sharpness.

## A zero-noise ambiguity at R62's D=4,p=8 instance

The two histograms c=(1,0,6,0,1) and c'=(0,1,6,0,1) yield moments (16,40,112,352) and (17,41,113,353). With common offsets 5 and 4 respectively, they give the identical four-channel observation

\[
(y_1,y_2,y_3,y_4)=(21,45,117,357).
\]

The bias-invariant algorithm recovers exactly (c_2,c_3,c_4)=(6,0,1), R=1, and the two admissible low-degree allocations. Both histograms are realized by p by p binary success tables since p>=D. The ambiguity is an exact retained observer residual, not an arithmetic rounding defect.

## Verification, preservation and native scope

Companion source: research_notes/portable_direct/x6_r63_common_bias_star_moment_verify.py.
Companion results: research_notes/portable_direct/x6_r63_common_bias_star_moment_results.json.

The exact Python integer/Fraction checker verifies 23,118 biased reconstruction cases for D=1,...,6, p=D,...,min(8,D+2), and offsets -13,0,7; 7,706 adversarial bounded-error examples (channel errors ±2/5 with rational bias 5/7); 1,570 direct counts of literal named successful AB branches across all 530 p=1,2,3 incidence tables; and both explicit ambiguity certificates. All assertions returned PASS. The unrestricted theorem is proven combinatorially above, not inferred solely from those finite checks. This work is an author check, not an independent proof review.

Keep the original full S and named Cell/Link/source incidence intact for future observables: the recovered histogram is only sufficient for its declared degree-observer target. No native TRIADIC_CLOSURE_E reset/equality/whole-triad carrier map, time-dynamics or physical calibration is claimed. The operation uses positive BRC branch counting; no signed cancellation, classical propagator, pi or trigonometric approximation is executed.

## Next scientific questions

1. For a fixed p,D and known feasible nonnegative histogram family, calculate the *instance-sharp* eta for reconstructing high-degree counts under unknown common normalized bias. Quantify the Chebyshev separation of distinct feasible moment fibers; the uniform 1/2 certificate can be conservative.
2. Treat a common raw-mass offset on Z_star(t), where division by (uv)^t changes the bias direction across depths.
3. Verify or refute a frozen-P000 native whole-triad Cell/Link/Port reset-and-equality map. Only such a map can justify native X6 time-dynamics attribution for this observer.

## Control provenance

The original historical Researcher EM-X6-214D9C / Activity RA-545183ADD4EF71C3E4698AEE is retained as provenance, not current private capability. Original continuation read r2-20261121-0009-x6-current-cont-read-v1 returned SUCCEEDED, observed 2026-11-20T16:14:46Z; it reported NEEDS_DISPATCH, no current active task execution authority (execution_authorized=false), and Source drift during the read. This publication is independent GitHub scientific evidence only. It does not modify CLAIM, formal PROGRESS, Result, Review or the original Activity. Current activity association requires its own legal identity/CAS route.
