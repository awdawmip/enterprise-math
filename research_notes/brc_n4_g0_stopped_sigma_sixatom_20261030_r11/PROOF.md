# BRC N=4 — Six-atom stopped filtration and sharp common-decoder deficiency

2026-10-30. **AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED.** This theorem concerns an **external finite 16-leaf P/Q dual-probability model**, not native P000 X6 cells, native heartbeat evolution, or a new original-game d2/d23 minimax.

## Pinned original model and lawful G0
Frozen prior source: [PR #1738](https://github.com/awdawmip/enterprise-math/pull/1738), commit eb248e7a4033a518556859e9c10060d7bb0a0b5f, especially the previous sequential-memory theorem. Original S2/S23 information sets: PR #1735 commit 6d9bc93c9d110418d22daf344ed83d883a4a1a23, PROOF.md Appendix I.

Omega has 16 leaves (s,j,k) where s is AU, AV, BU or BV and j,k are binary. Let q_s=(1/6,1/3,1/4,1/4), with time-three P/Q likelihood-ratio pairs r_AU=(9/10,11/10), r_AV=(1/4,1/4), r_BU=(1/5,9/5), r_BV=(2,2). The exact leaf masses are Q(s,j,k)=q_s/4 and P(s,j,k)=q_s*r_(s,j)/4. Both laws are strictly positive and normalized.

Take F2=sigma(s), F3=sigma(s,j), F4=sigma(s,j,k), with time-one information the A/B parent. Under deterministic G0, AU/BU continue from T2 and stop at T3, while AV/BV stop at T2. Early decisions are Q; at T3 AU decides P and BU decides Q. This is lawful S23: AU/BU stage-two continuation kernels coincide, and AU/BU time-three likelihood-ratio groups are disjoint. The full terminal observer O'=(T,Decision,Z_BU,Z_AU) has three possible values: E=(2,Q,0,0) on AV/BV; A=(3,P,0,1) on AU; B=(3,Q,1,0) on BU. Under both P and Q, its masses are P(E)=Q(E)=7/12, P(A)=Q(A)=1/6, P(B)=Q(B)=1/4.

## Theorem 1. The exact stopped sigma-field has SIX atoms
Use the standard stopped field F_T={D subset Omega : D intersection {T<=t} belongs to F_t for all t}. Its six atoms are:

  AV (all j,k), BV (all j,k), AU-j0 (both k), AU-j1 (both k), BU-j0 (both k), BU-j1 (both k).

Proof: at t=2, D restricted to {T<=2}=AV union BV must be F2-measurable, so it is constant on each AV/BV parent. As every path stops by t=3, D must also be F3-measurable, so it may distinguish AU/BU j children but cannot distinguish their k daughters. Conversely every union of those six atoms satisfies both stopping constraints. The conditions at t=1 and t=4 are automatic for these unions. This proves the exact classification, not merely an upper bound on the number of stopped atoms.

The full stopped-state P/Q masses are:

| F_T atom | P | Q |
|---|---:|---:|
| AV | 1/12 | 1/3 |
| BV | 1/2 | 1/4 |
| AU,j=0 | 3/40 | 1/12 |
| AU,j=1 | 11/120 | 1/12 |
| BU,j=0 | 1/40 | 1/8 |
| BU,j=1 | 9/40 | 1/8 |

Consequently TV(P_FT,Q_FT)=(1/2)*(1/4+1/4+1/120+1/120+1/10+1/10)=43/120, despite TV(P_O',Q_O')=0.

## Theorem 2. Sharp P/Q-common O'-decoder radius
Consider all law-independent stochastic decoders D(x|z), allowed arbitrary real probabilities and private randomization, required to preserve the observed z=O' while reconstructing the six-atom stopped-history variable x. Let e_L(D) be total variation between the actual joint stopped-state law under L and its decoder reconstruction.

**Exact minimax:** inf_D max(e_P(D),e_Q(D)) = 43/240.

Proof: the input O' has the same distribution under P and Q, so *every* common D yields the same reconstructed measure R under both laws. By the TV triangle inequality,

  43/120 = TV(P_FT,Q_FT) <= TV(P_FT,R)+TV(R,Q_FT) <= 2 max(e_P,e_Q).

This applies to all stochastic kernels, including real and boundary kernels. It is attained by the explicit conditional midpoint kernel

  D(x|z) = [P_FT(x)+Q_FT(x)]/[2 P_O'(z)]  for x in the O'-fiber z;

and zero otherwise. All denominators are positive. It is normalized in each fiber because P_O'=Q_O'. It reconstructs R=(P_FT+Q_FT)/2, and each error equals 43/240. QED.

This radius concerns a *different* observable and decoder family from the preceding two-query independent-emission value (sqrt(2)-1)/4; the results should not be conflated.

## Theorem 3. Exactly ONE observed conditional bit repairs all lawful stopped readouts
Every O' fiber contains exactly two positive F_T atoms. Retain one *actual branch/provenance bit* b, conditionally defined: on A or B let b=j, and on E let b=0 for AV and b=1 for BV. Then (O',b) is a bijection with the six F_T atoms. Hence every deterministic F_T-measurable readout factors **pathwise** through (O',b), and every P/Q-common randomized post-processing of stopped history can use that sufficient statistic. Zero extra bits do not universally suffice pathwise: each O' fiber contains two distinct stopped events with positive mass. Therefore one conditional actual bit is minimal for pathwise exact universal F_T readout under fixed G0.

An *independently resampled* b does not reconstruct the actually realized branch; this theorem assumes the original recorded label.

## Theorem 4. Post-stop k-query is not an original stopped-time output
BU paths under G0 stop at T=3. The two leaves (BU,j,0) and (BU,j,1) belong to the same F_T atom, and both have positive P/Q mass. Therefore the time-four k daughter, even when restricted to BU, is not F_T-measurable.

Moreover, let hat{k} be *any* F_T-adapted BU prediction, optionally using coins conditionally independent of the still-hidden k given F_T. The original BU bit is fair conditional on BU,j under BOTH laws. Accordingly,

  P(hat{k} != k and s=BU) = Q(hat{k} != k and s=BU) = (1/2)*(1/4) = 1/8.

The exact 1/8 concerns *pathwise prediction of the same physical sampled k*, not one-shot distributional TV: a fresh fair bit matches its one-read marginal but not the same realized path. The earlier persistent-fair-bit simulator reproduces the declared auxiliary read-only protocol's distributions but does not make its post-stop k reading a lawful original S2/S23 observation. Access requires explicit continuation to T4 **before stopping** or a separately declared later-sensor experiment.

## Verification and scope
VERIFY.py actually executed using standard-library Fraction arithmetic. It reconstructs all 16 positive P/Q leaves, verifies both normalizations, the six exact stopped-atom probabilities, the three equal O' masses, both TV values 43/120 and 43/240, decoder normalization, BU daughter fairness, and all four deterministic BU-j predictors' error 1/8 in both laws. The universal decoder theorem follows from the triangle inequality, the six-atom classification from the explicit stopping filtration, and the randomized pathwise prediction statement from conditional independence; finite checks do not substitute for those proofs.

Background standard definitions: https://en.wikipedia.org/wiki/%CE%A3-Algebra_of_%CF%84-past and https://planetmath.org/stoppingtime . These references do not supply the present exact numbers.

**Independent review needed:** source S2/S23 information sets and G0 legality; F_T partition at t=2,3; the six raw P/Q masses; common-decoder conditional kernel; and the pathwise-versus-distributional distinction. This is author-side portable evidence, not native Source CLAIM, Result, independent Driver admission, or a P000 native-X6/time result.
