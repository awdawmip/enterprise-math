# X6 R74 — 双低精度通道的全实权重相图与最小统一饱和 Port 数 27

Date: 2026-11-21 (Asia/Shanghai)
Scientific status: CONDITIONAL_AUTHOR_PROOF / EXACT_RATIONAL_FINITE_AUTHOR_CHECK / NOT_INDEPENDENTLY_REVIEWED
Scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json (P000 V5)
Predecessors: R68 common-bias weighted pair lemma, R72 (all-positive-weight D4 saturation at 125), R73 (one noisy channel).
Scope: conditional positive-count BRC degree-histogram observer, not a native X6 Cell/Link/Port dynamic theorem. Keep whole TRIADIC_CLOSURE_E, six native axes, independently typed time, named-port history, joint relational directions and future-operation safety outside this quotient.

## Model and exact result

Let D=4 and p be an integer at least 27. A p-Port outcome has integer counts c_0,...,c_4 ≥ 0 with sum p; the target is (c_2,c_3,c_4). We observe four moments Y_i=m_i+b+e_i, m_i=sum_d c_d d^i, 1≤i≤4, with a shared unknown real offset b and errors |e_i|≤ηw_i. Here the weight family is w=(1,t,t,1), t>0.

For a nonzero integer difference a=(a_2,a_3,a_4), set q(a)=max(sum max(a_d,0),sum max(-a_d,0)). It is realizable at p exactly when q(a)≤p. The moment differences after eliminating the shared degree-1 contribution and common offset are
z=(0, 2a_2+6a_3+12a_4, 6a_2+24a_3+60a_4, 14a_2+78a_3+252a_4).

Put B=|z_4|, T=|z_3-z_2| and U=max(|z_2|,|z_3|,|z_4-z_2|,|z_4-z_3|). The R68 exact pair-collision threshold specializes to
η_pair(a;t) = max(B/4, T/(4t), U/[2(1+t)]).

THEOREM (all real t>0, every integer p≥27):

η*_{p,4}(1,t,t,1) =
  6/(1+t)     if 0<t≤1/11;
  1/(2t)      if 1/11≤t≤1;
  1/2         if 1≤t≤11;
  6/(1+t)     if t≥11.

The formulas agree at all shared boundaries. In this entire one-parameter weight family the smallest universally sufficient Port count is exactly 27: η*_{p,4}(1,t,t,1)=η*_{27,4}(1,t,t,1) for all p≥27 and all t>0; for every integer p≤26 with p≥4, some t>11 yields a strictly larger threshold.

The three witnesses, with exact (B,T,U) and Port demand, are
- a_A=(15,-6,1), q=16, (B,T,U)=(6,0,12), attaining 6/(1+t) when 0<t≤1/11;
- a_B=(10,-5,1), q=11, (B,T,U)=(2,2,2), attaining 1/(2t) for 1/11≤t≤1 and 1/2 for 1≤t≤11;
- a_C=(24,-14,3), q=27, (B,T,U)=(0,12,12), attaining 6/(1+t) when t≥11.

## Complete symbolic proof (independent of the R72 28-vector atlas)

1. Every z_i is even, hence each nonzero B or T is at least 2. We prove two stronger integer-lattice divisibility lemmas.

2. If T=0, then 4a_2+18a_3+48a_4=0. Modulo 2 this makes a_3 even. Write a_3=2k, a_4=l, a_2=-9k-12l. Consequently z_2=z_3=-6(k+2l), and z_4-z_2=12(3k+8l). Thus U=max(6|k+2l|,12|3k+8l|). For a≠0, if 3k+8l≠0 then U≥12. If 3k+8l=0, integer solutions are k=-8m, l=3m, so k+2l=-2m≠0 and again U≥12.

3. If B=0, then 7a_2+39a_3+126a_4=0. Reducing modulo 7 shows a_3=7k. Let a_4=l and a_2=-39k-18l. Then z_2=-12(3k+2l) and z_3=-6(11k+8l). If z_2≠0 then U≥12. If z_2=0, integer solutions satisfy k=2m, l=-3m, and z_3=12m≠0. Hence B=0 and a≠0 also force U≥12.

4. Lower bounds in four t-ranges:
- 0<t≤1/11: when T≠0, η_pair≥1/(2t)≥6/(1+t); when T=0, Step 2 gives η_pair≥6/(1+t).
- 1/11≤t≤1: when T≠0, η_pair≥1/(2t); when T=0, Step 2 gives η_pair≥6/(1+t)≥1/(2t).
- 1≤t≤11: when B≠0, η_pair≥1/2; when B=0, Step 3 gives η_pair≥6/(1+t)≥1/2.
- t≥11: when B≠0, η_pair≥1/2≥6/(1+t); when B=0, Step 3 gives η_pair≥6/(1+t).
These bounds hold for every nonzero integer a, without any assumption on q(a). The three listed differences attain all four bounds with q≤27, proving the asserted global minimum for all p≥27.

5. Sharpness of 27. If t>11 then the proved optimum 6/(1+t) is strictly less than 1/2. Hence any attaining difference must have B=0. Step 3 gives U≥12, and equality with the optimum forces U=12. In the B=0 parameterization, set u=3k+2l, v=11k+8l. The condition U≤12 becomes |u|≤1, |v|≤2, |v-2u|≤2. Solving gives k=4u-v, l=(3v-11u)/2, so v≡u (mod 2). The only nonzero solutions, up to common sign, are (u,v)=(0,2) and (1,1). They yield respectively a=(24,-14,3), q=27, and a=(-45,21,-4), q=49. Thus no q≤26 difference attains 6/(1+t) for any t>11. Monotonicity in p proves the minimum uniform threshold is exactly 27. QED.

## Author crosschecks, reproducibility, and boundaries

The accompanying stdlib-only Python Fraction verifier independently enumerates all 47,305 unoriented nonzero integer differences with q≤30, for nine rational t values and p=26,27,30. All 27 exact comparisons passed. For t=12, p=26 gives 1/2 whereas p=27 gives 6/13. For t=100, p=26 gives 9/101 whereas p=27 gives 6/101. These finite computations are crosschecks of the above all-real-t, all-p≥27 symbolic proof, not substitutes for it.

This family demonstrates a sharp saturation 27 versus the all-weight threshold 125 from R72, with *two* nonuniform measurement channels. No conclusion about underlying labeled Port/Cell/Link trajectories, true physical event time, causal resetting or signed/phase cancellation is inferred from the positive-count quotient.

## Next questions

- Classify the exact weight chambers and which R72 28 candidates can be globally optimal across all positive quadruples; some Pareto-nondominated gaps may still never optimize additive edge-sum denominators.
- Extend lattice zero-gap lemmas to larger D and arbitrary subsets of precise channels.
- Establish a type-safe provenance-preserving map from source-admitted whole-triad event traces to BRC histograms, or construct exact failure witnesses for future-operation descent.

Control provenance: original task RS-X6-NATIVE-TIME-DYNAMICS; this is independent portable science continuing R73, not an assertion of current session CLAIM or authority. Historical researcher EM-X6-214D9C and Activity RA-545183ADD4EF71C3E4698AEE are provenance only. Current native continuation request r2-20261121-1110-x6-r74-native-cont-read-v1 returned SUCCEEDED / execution_authorized=false at 2026-11-21T03:08:38 UTC. Preserve current active holder and all existing Activity data.