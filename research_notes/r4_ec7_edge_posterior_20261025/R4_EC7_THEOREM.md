# R4-EC7 — Exact edge posteriors and unbounded rational coefficients in an effect-conditioned BRC

Date: 2026-10-25. Author-side mathematical derivation and symbolic exact verification only; no independent review or theorem admission.

## Model and provenance

Source frontier: R4-EC6 author evidence, enterprise-math@b8ea661372068b2059cf8121fb5d50dde83571c4. Related but distinct: R276 extreme dirty-channel result @ab39a2962c39f99c69fee8a04d555fd93f5697d7. This proof concerns *clean monitor r=0 versus r=1*, not clean versus dirty counts. Account canonical rules pinned at chatgpt-global-knowledge main@5ddaf5f3d8bd1ce9934486e7ab80b3627ddaec6c, P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc (ACTIVE_LOCKED). EM baseline main@b58330b74576153cdadde5d80a3d92df3a819a0e, current portable research rules read. No native Owner/CLAIM verified (dispatch CONTROL_QUOTA, session_start STATIC_READONLY_SCOPE_DENIED, operation_sent=false).

This is the *auxiliary* positive ordered binary-path BRC, not a complete native X6 dynamic, R193 interpretation, native spatial three-dimensional slice, or calibrated heartbeat-time statement.

Each input bit a has weight one. Starting at (q,r,epsilon,k)=(0,0,+1,0), the edges for a=0,a=1 are, respectively: q=0 -> (2,-1,-1),(2,+1,-1); q=1 -> (0,-1,-1),(0,+1,-1); q=2 -> (1,+1,+1),(2,+1,-1). Each tuple is (q_next,eta,b), where (epsilon_next,k_next)=(eta epsilon,eta k+b). The clean provenance monitor is r=0 if no consecutive 00 and last bit !=0, r=1 if no 00 and last bit =0, and r=2 if 00 has ever occurred. Bit zero maps r=0->1,r=1->2,r=2->2; bit one maps r=0->0,r=1->0,r=2->2.

Let P_n(q,r,epsilon,k) count *ordered raw words* exactly. The R4-EC6 six-observation-label kernel, for unhit h=0, uses its bit-zero hit-creating edge at the effect-dependent rational weight

 theta_n(q,epsilon,k) = P_n(q,1,epsilon,k)/(P_n(q,0,epsilon,k)+P_n(q,1,epsilon,k))

on occupied fibers. The numerator is *last-zero and still clean*, not already-dirty mass.

## Theorem (all n>=7)

At q=2 and integer effect grade k=n-6, the clean fibers have the following **exact** counts:

 P_n(2,0,+1,n-6)=1; P_n(2,1,+1,n-6)=n-7;
 P_n(2,0,-1,n-6)=1; P_n(2,1,-1,n-6)=n-6.

Consequently:

 theta_n(2,+1,n-6)=(n-7)/(n-6),
 theta_n(2,-1,n-6)=(n-6)/(n-5).

For all n>=8, both are strictly between 0 and 1. Their signed difference equals

 theta_minus - theta_plus = 1/((n-6)(n-5)) > 0.

## Complete all-n proof: a finite-defect generating-function identity

Put t=epsilon*k. A single input step satisfies t_next=t+epsilon*eta*b=t+epsilon*(1-2a); the latter identity follows by checking the six edges in the table. Every increment is exactly +1 or -1.

Restrict to clean paths r=0,1. Index the twelve states s=(q,r,epsilon) by q=0,1,2; r=0,1; epsilon=+1,-1. For sign sigma in {+1,-1}, define two 12x12 nonnegative integer adjacency matrices A_(sigma,0), A_(sigma,1) directly from the table: keep only transitions with r_next<2; classify them into matrix A_(sigma,0) when t_next-t=sigma and into A_(sigma,1) when t_next-t=-sigma. Matrix rows are destination states and columns source states. e0 is the basis column for (0,0,+1).

The formal power-series vector whose coefficient of x^n y^d counts clean words with n steps and d increments opposite to sigma is

 F_sigma(x,y)=(I-x A_(sigma,0)-x*y A_(sigma,1))^-1 e0.

Therefore the coefficient of y^3 is exactly

 V_(sigma,3)(x)=[(I-x A_(sigma,0))^-1 x A_(sigma,1)]^3 (I-x A_(sigma,0))^-1 e0.

This equality is the formal geometric series for an invertible matrix with identity constant term. The target signed displacement t=sigma*(n-6) has exactly three opposite-sign increments, so the x^n coefficient of the relevant V coordinate *is the desired path count*. There is no truncation in n.

The 12-row exact algebra gives det(I-x A_(sigma,0))=1-x for both signs and the following selected rational-function identities. Each can be verified by symbolic matrix elimination from the preceding explicit state/edge definitions:

  sigma=+1, epsilon=+1, q=2, r=0:  x^3*(x^3-x^2+1)/(1-x)
  sigma=+1, epsilon=+1, q=2, r=1:  x^8/(1-x)^2
  sigma=-1, epsilon=-1, q=2, r=0:  x^3*(x^2-x+1)/(1-x)
  sigma=-1, epsilon=-1, q=2, r=1:  x^7/(1-x)^2.

The accompanying Python verifier constructs the two matrices from the raw six edges and checks all four rational identities *as formal symbolic expressions*. Extraction of coefficients shows that, for every n>=7, the two r=0 coefficients are 1, the positive-sign r=1 coefficient is n-7, and the negative-sign r=1 coefficient is n-6. Rational substitution and subtraction establish the theorem and the strict orientation gap. QED.

## Corollaries and exact boundary

1. The positive-orientation coefficient (n-7)/(n-6) takes infinitely many distinct exact rational values for n>=8, with reduced denominator n-6. Therefore **a fixed finite palette of rational coefficient values** cannot supply *this specified R4-EC6 posterior kernel* at all depths. Explicitly storing the denominator needs floor(log2(n-6))+1 bits, although a short formula can generate it when n is available.
2. For each n>=8 both effect fibers have the same q=2, unhit h=0, depth n and scalar k=n-6 but different epsilon. Their split coefficients differ, so the particular posterior rule cannot depend on n,q,h,k alone: the orientation sign is necessary at these grades.
3. These are not impossibility results for every possible six-state *effect-blind* BRC with alternative internal labels or decoder. The stricter six-versus-seven question remains open. No claim is made about minimum total space for symbolic schedule evaluation.

## Verification and next question

Locally executed algebraic rational-function identity checks: PASS, no floats. Independent raw-word enumeration through depth 13 (all histograms) versus arbitrary-precision DP: PASS. All-n formulas additionally checked computationally through depth 150: PASS; *the proof itself is the exact generating-function calculation, not the finite tests*. The attached complete local evidence bundle includes the fuller executed reproducer, machine report, entire proof and SHA manifest; the GitHub reproducer in this directory proves the same rational identities.

Research methodology: BRC ordered path counts, source monitor, exact affine grade and observer-fiber projection; REUSE_APPLIED. Future R4-EC8: find a uniform rational recurrence/efficient evaluation strategy for the *interior* posterior theta schedule that avoids carrying the seventh source state, while separately testing arbitrary encoded effect-blind six-state realizability. Preserve native Owner, CLAIM, Source Result, and independent Driver review distinctions.