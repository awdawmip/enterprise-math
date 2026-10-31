# BRC N=4 — exact three-symbol no-time radius via lawful binary shattering

**2026-10-31. AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED.** Portable author-side mathematical research, not a native Source Task/CLAIM, Result, Driver review or proof of physical X6 dynamics.

## Frozen experiment

Under each of the full P and Q laws there are sixteen strictly positive leaves (S,J,K), with S in {AU,AV,BU,BV}, J,K binary and K independent fair. Per-K unnormalized leaf numerators with common denominator 240:

| S | Q: J=0,1 | P: J=0,1 |
|---|---|---|
| AU | 10,10 | 9,11 |
| AV | 20,20 | 5,5 |
| BU | 15,15 | 3,27 |
| BV | 15,15 | 30,30 |

The eight conditioned preparation laws have J rows: AU_Q=(1/2,1/2); AU_P=(9/20,11/20); AV_Q=AV_P=(1/2,1/2); BU_Q=(1/2,1/2); BU_P=(1/10,9/10); BV_Q=BV_P=(1/2,1/2). The six **distinct** third-stage P/Q likelihood-ratio classes are AU0=9/10, AU1=11/10, AV=1/4, BU0=1/5, BU1=9/5, BV=2. S23 requires the action be constant on equal-ratio histories. S2 also ties AU/BU second-stage actions. All other lawful policies, including randomized ones, are retained in the supremum.

An encoder E is a single pre-policy row-stochastic 8×k matrix and may randomize. For each policy H, a row-stochastic decoder D_H may vary but may not access the original preparation or (S,J,K). Score max over eight preparations of total variation on the public observer, worst over **all** S23 or S2 policies and best decoder; then infimize over E. Observer A: Y=(Decision,Z_BU), with stopping time T erased, but BU sensor presence retained. At a stage-three BU terminal event, Z_BU=J XOR Bernoulli(epsilon); at non-BU terminal outputs Z_BU=bottom. The frozen stage-two BU early-stop semantics of the predecessor are retained. Observer B: only Decision. Epsilon is any real number between 0 and 1/2.

## Theorems

For either F=S23 or F=S2, for every real 0<=epsilon<=1/2:

**A:** R_3(F; noT, withZ)=1/2.

**B:** R_1(F; Decision-only)=R_2(F; Decision-only)=R_3(F; Decision-only)=1/2.

These are **distributional** reconstruction radii, not pathwise recovery, information equivalence or a P000 native-state theorem. The observer erasure does not delete private provenance or future policies.

## General binary-shattering rank lemma (exact analytic proof)

Suppose G selected input distributions admit all 2^G source-wise deterministic binary output labelings through lawful future policies. For any pre-policy row-stochastic encoder E with k<G, choose a nonzero left-null vector w of the G×k selected-row matrix, so w^T E=0. As E·1_k=1_G, the vector w has sum zero and both positive and negative entries. The adversary chooses the lawful binary labeling b_i=1 exactly where w_i>0; other b_i=0.

For *any* decoder for that policy, let d_c be its probability of public Decision=1 and q=E d. Marginalization contracts total variation. Hence a public TV error δ would require |b_i-q_i|<=δ for all G selected inputs. Yet

    w^T q=0,
    w^T b=sum_(w_i>0) w_i=(1/2)sum_i |w_i|,

so (1/2)||w||_1=|w^T(b-q)|<=δ||w||_1. Therefore δ>=1/2. This proof allows arbitrary real stochastic E, all randomized decoders, and any richer public observer containing the binary Decision marginal. It is the elementary left-nullspace obstruction; no general novelty claim is made.

## Verification that the shattering policies are actually lawful

Choose the four conditioned inputs AU_Q, AV_Q, BU_Q, BV_Q. For each b in {0,1}^4 define H_b: at stage two **continue all** histories (therefore S2's AU/BU constraint is satisfied); at stage three terminate every survivor and choose P if b_S=1, Q otherwise. Give AU0/AU1 the same action, BU0/BU1 the same action, and independent choices to AV and BV. The six ratio classes displayed above are distinct; thus every H_b respects S23's ratio-class restriction. These 16 policies are also S2 lawful.

On each of the four selected preparations the public Decision marginal is deterministically b_S regardless of J,K,epsilon or the BU sensor. Apply the rank lemma with G=4, k=3: the TV error cannot be smaller than 1/2 for the no-time/with-Z observer. The same argument applies to the Decision-only observer with k=1,2,3.

This does NOT secretly disclose S to the decoder: only the lawful action H_b internally depends on the distinguishable ratio classes, and the observable lower certificate uses solely Decision.

## Exact upper bound for A: two-code predecessor reference

Reuse the author-side two-code full-path construction from immutable predecessor e160c3842237fc16ea6d7ac6b0b11df299de0e64. On the (S,J) carrier, attach independent fair K and define:

    F_L: AU0=19/80, AU1=21/80, AV0=1/4, AV1=1/4;
    F_R: BU0=1/10, BU1=2/5, BV0=1/4, BV1=1/4;

other entries are zero. Both references sum to 1. Encode AU/AV to L, BU/BV to R. For all eight actual source preparations, the corresponding reference places precisely half of its mass on that source fiber, pointwise dominated by the actual law; the overlap is exactly 1/2, so TV(original,reference)=1/2.

For every lawful stochastic H, let decoder L output the push-forward H#F_L and decoder R output H#F_R, including the requested observer erasure. The same law-independent kernel applies to original and reference, so TV cannot increase under pushforward. The common two-code encoder has error <=1/2 for all lawful S23/S2 policies, all eps, and *a fortiori* with at most three codes. Combining with the rank lower bound proves A.

## Exact upper bound for B

For Decision-only output, choose even one constant code and let its decoder return the fair Bernoulli distribution (P=Q=1/2). Its TV distance to every Bernoulli(p) is |p-1/2|<=1/2. With more codes, the best error cannot increase. The rank lower bound proves equality at k=1,2,3.

## Evidence, interpretation and boundaries

The standalone `VERIFY.py` uses Fraction exact rational arithmetic. It reconstructs both 16-leaf laws, checks normalization and all eight preparation conditionals, six pairwise-distinct ratio classes, 16 legal b masks at four epsilon values (512 full public Y distributions and decision marginals), eight exact full-carrier reference overlaps, and 1,105 exact left-nullspace sign certificates (all 81 deterministic 4×3 encoders plus 1,024 seeded rational stochastic examples). `RUN_EVIDENCE.txt` contains the actual local run. Universal real encoder/policy/epsilon quantifiers come from the analytic proof, not finite enumeration.

**BRC reuse:** exact positive-rational provenance carrier and F_L/F_R observer-safe data processing were genuinely applied, not renamed as new tools. The plateau R_2=R_3=1/2 persists even after both T and sensor erasure, because the legal policy family shatters four source classes through Decision alone. It may cease under a restricted policy class, average-case loss, or a different semantic bridge. The native P000 six-axis Cell+independent-time dynamics and its observer-preserving map into the stipulated sixteen-leaf experiment remain unproved. No new Foundation/Working Truth claim is made.
