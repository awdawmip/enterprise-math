# R700 — Sharp one-scalar reconstruction of a frozen E* BRC group histogram

Date: 2026-11-11 (Asia/Shanghai).
Researcher: EM-X6-54D0A4; activity RA-26A5311133C612C9AB521167.
Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS, task publication TP2-8B7E13C5904A2D6F1142. Immutable task science unchanged.
Scientific predecessor: R699, commit 55743642c88a24377ad4797cc2c6359c98b20553 (Draft PR #2010), itself extending R697–R698.
Evidence status: independent author-side exact combinatorial proof and executed finite Python checker; unreviewed.

## Definition and scope

This is an exact algebraic observer for the already defined R699 *static E* candidate*: a four-group labeled-return-path histogram v=(e,t,c,z) with coordinate caps N=(24,18,6,12) and known s=e+t+c+z, 1<=s<=60. It does not replace the original six-axis X6 Cell space or the labeled 60 path branches. The four variables are output-group counts, not native spatial dimensions. The contextual positive-rational BRC observers frozen in R699 are

U=4e+5t+z; V=2e+2c+z;
T3=U/(10s); T8=V/(5s).

For nonnegative integer k define the derived one-scalar algebraic readout
P_k=T3+(k/2)T8=(U+kV)/(10s).
This is a linear postprocessing operation on two exact readouts; it is not claimed to be a physically admitted single-probe X6/V29/V39 event. Original provenance remains upstream.

## Theorem 1: exact, optimal integer fusion

The **least nonnegative integer k** for which (s,P_k) uniquely determines every valid v is k=46. At this coefficient,

W:=U+46V=96e+5t+92c+47z,
P_46=T3+23*T8=W/(10s).

**Decoder.** Put Q=W-47s=49e-42t+45c. Modulo seven, Q=3c mod7. Because 0<=c<=6, c=(5Q) mod7 is uniquely determined. Then H=(Q-45c)/7=7e-6t. Enumerate the integers e in [0,24] with e=H mod6; put t=(7e-H)/6 and z=s-e-t-c. There is exactly one candidate with 0<=t<=18 and 0<=z<=12 for any valid observation.

**Proof of uniqueness.** Two admissible states with identical (s,W) have delta c=0. They also satisfy 7 delta e=6 delta t, hence delta e=6q, delta t=7q. Conservation of s gives delta z=-13q. The cap 0<=z<=12 forces |delta z|<=12, hence q=0, and every coordinate difference vanishes.

**Proof k<46 fails (constructive).** For k in {0,1,2,3,6}, choose the following valid nonzero difference vectors delta=(delta e,delta t,delta c,delta z), respectively:
k=0: (-1,1,1,-1); k=1: (0,0,-1,1); k=2: (0,-1,2,-1); k=3: (0,-2,1,1); k=6: (-1,-2,1,2).
Each has sum zero, coordinates bounded by N in absolute value, and delta(U+kV)=0.

For k in {4,5} or 7<=k<=45, write n=k-1=4x+3y with x,y nonnegative, 0<=y<=6 and x-y<=5. At k=4,5 use (x,y)=(0,1),(1,0). For 7<=k<=45, choose y0 in {0,1,2,3} such that 3y0=n mod4 and x0=(n-3y0)/4. This has x0>=0. If x0-y0>5, then y0<=2 since n<=44, and replace (x0,y0) by (x0-3,y0+4). The new pair is nonnegative, y<=6, and -7<=x-y<=5. Define
delta=(-x,-y,1+x-y,2y-1).
Its sum vanishes, its absolute coordinates lie below N, and delta V=1, delta U=-4x-3y-1=-k. Therefore delta(U+kV)=0. For any such delta, v+_i=max(delta_i,0) and v-_i=max(-delta_i,0) are valid distinct histograms with identical s and fused observation. Thus all 46 smaller integers fail.

## Theorem 2: exact minimax scalar noise threshold

Let d_s=min{|W(v)-W(v')|:v != v' in X_s}. Then:
s=1 or 59: d_s=4;
s=2 or 58: d_s=3;
3<=s<=57: d_s=1;
s=60: X_s contains one state.

For the observed P_46=W/(10s) with independent of sign absolute error <=epsilon, a worst-case recovery algorithm succeeds for *every* X_s state and all allowed noises if and only if 2epsilon<d_s/(10s). Thus the strict sharp thresholds are epsilon<1/(5s) at s=1,59; epsilon<3/(20s) at s=2,58; epsilon<1/(20s) for 3<=s<=57. Equality fails by the midpoint of the two closest exact values.

**Proof of gaps.** At s=1 the four singleton W weights are (96,5,92,47); minimum separation 4. At s=2 the ten two-atom sums sorted are (10,52,94,97,101,139,143,184,188,192), minimum separation 3. For s=3, pair (1,0,0,2) and (0,1,2,0) has delta U=1, delta V=0, so W difference 1. Adding a common vector h with independent caps (23,17,4,10) spans every additional total 0..54. Therefore distance one occurs for all s=3..57 and is minimal by integer distinctness. Complementation v -> N-v interchanges s and 60-s and preserves difference magnitudes, yielding the endpoint symmetry. At s=60 only v=N exists.

If T3 and T8 are **measured separately** with noise radii eps3 and eps8, eps3+23 eps8<d_s/(20s) is sufficient to decode via the fused scalar. R699's exact two-coordinate Pareto-error theorem is sharper for those separate-error observations.

## Verification and limitation

The accompanying deterministic Python standard-library checker exhausts all 43,224 nonzero bounded histograms; checks the exact modular decoder for every state; constructs 46 explicit smaller-k collisions; independently scans all k<=45; computes all sixty total-group counts and minimum W spacings. Expected console result:
R700_SINGLE_FUSION_MINIMAL_COEFFICIENT_EXACT_PASS 43224 46

This calculation tests bounded exact BRC-*derived* algebraic histogram readouts. It did not run the native BRC kernel, nor supply a V29 PASS/TRANSFER or V39 j event, and does not prove P000 triadic closure or rotation covariance. This remains a possible information-preserving static observer compression, not an admitted native X6 dynamics theorem.

Next exact action: build a source-labeled legal X6 Cell/Link/Port packet for T3 and T8 with V29 and V39 event obligations, verify that s is an admissible observable, then test whether the fused rational scalar can be measured within that native event vocabulary.