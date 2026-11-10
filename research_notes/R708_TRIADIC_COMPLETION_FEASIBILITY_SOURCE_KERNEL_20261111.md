# R708 — X6 triadic completion feasibility and conditional hidden-source BRC kernel

Date: 2026-11-11 (Asia/Shanghai). Researcher: EM-X6-640177. Research activity: RA-BC55A6E8FF1DD5106A03841E.
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; immutable publication TP2-8B7E13C5904A2D6F1142.
Frozen scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Predecessor: R707, PR #2033, immutable source 877562f8f1affc12016fbd5c35f623d8a27f467b.

## 1. Typed finite candidate

Fix a chosen native X6 Cell c (chart-relative, no universal origin), positive quantum q, and 3m individually distinguishable force-token identities. Each token retains (id, c, native axis i in {0,...,5}, sign ±, q, source). Its Cell triad consists of three tokens of pairwise different native axes. This is the explicitly declared R707 equal-quantum candidate specialization of TRIADIC_CLOSURE_E; signed force cancellation is NOT derived from positive BRC mass. S6 acts by joint axis/token/observer relabeling. A full triadic decomposition is an UNORDERED partition of all 3m labeled tokens into m such triads. Let n_i count tokens on axis i, with sum_i n_i=3m, and D(n) be the number of complete labeled decompositions.

From R707, with H(x)=sum_{i<j<k}x_i*x_j*x_k:
D(n) = (prod_i n_i! / m!) * coefficient[x_0^n_0 ... x_5^n_5] H(x)^m.

## 2. Theorem R708-A: complete realizability criterion

For every m>=0 and n in nonnegative integers^6 with sum_i n_i=3m,
D(n)>0 if and only if max_i n_i<=m.

Proof. Necessity: a triad can use each axis at most once, so an axis can occur in no more than m triads. For sufficiency induct on m. At m=0 the empty decomposition is unique. For m>0 there must be at least three positive entries, since the six counts total 3m and every entry is <=m. Choose the three largest entries and subtract 1 from each, assigning any still-unused labeled token on each selected axis to a new triad. The resulting total is 3(m-1); selected entries are now <=m-1. Every unselected entry is strictly less than m: if an unselected entry equaled m, the three selected entries were each also m, whence the original sum would be at least 4m, a contradiction. Therefore all remaining counts are <=m-1. The induction hypothesis supplies a decomposition of the remaining labeled tokens. This gives a constructive greedy certificate with m triples and establishes the theorem. QED.

For six fixed axes, sorting six counts and removing three counts m times takes O(m) elementary count updates and constant-size sorts. The existence decision itself needs only sum and max.

## 3. Theorem R708-B: exact BRC hidden-source conditional kernel

Fix identified tokens u and v on two DIFFERENT axes i and j. The queried event Q means that u and v belong to the SAME complete triad. For a third axis k not in {i,j}, define the remaining population n^(ijk)=n-e_i-e_j-e_k and set D=0 on an invalid population. The exact integer source multiplicity with hidden third axis k is

C_k(n;u,v) = n_k * D(n-e_i-e_j-e_k).

Proof. First choose one of the n_k distinct third-token identities on axis k. The specified triple is now fixed, and deleting it gives a bijection between decompositions containing it and all complete decompositions of the remaining labeled tokens. Disjoint choices of third-token identity, hidden axis, and residual decomposition are distinct positive BRC branches. Hence their count is n_k D(n^(ijk)). QED.

Conditional on Q (provided C_total=sum_{k !=i,j} C_k >0), the positive source kernel is P(k | Q)=C_k/C_total. The state retains token id, sign, path/provenance; the scalar mass is only a conditional SOURCE observation, not force amplitude or a physical balance equation. Simultaneous S6 relabeling of n,u,v,k preserves all C values up to relabeling.

## 4. Infinite family with nonuniform hidden-third mass

For four distinct native axes i,j,k,l and m>=1, 0<=a<=m, set n_i=n_j=m, n_k=a, n_l=m-a, remaining two counts zero. Every complete triad must use exactly one token from each saturated axis i,j and one from the union of k and l (there are m such third tokens). A complete partition is exactly two independent bijections from the labeled i-tokens to labeled j-tokens and the labeled third-token pool, so

D(n)=(m!)^2;
C_k=a*((m-1)!)^2;
C_l=(m-a)*((m-1)!)^2;
P(k|Q)=a/m; P(l|Q)=(m-a)/m.

For m=3,a=2,n=(3,3,2,1,0,0), D(n)=36. For a fixed named pair of the first two axes, exactly 12 of these branches contain it in a common triad: 8 third-axis-2 branches and 4 third-axis-3 branches; probabilities 2/3 and 1/3. The local eight signed-axis completion options in R707 and the conditional global completion kernel refer to different declared populations; the latter introduces exact global completion constraints.

## 5. Exact computation and source status

The executable checker in experiments/R708_TRIAD_FEASIBILITY_BRC_VERIFY_20261111.py independently implements (i) polynomial coefficient recursion for H^m, (ii) first-labeled-token decomposition-count recursion, (iii) largest-three greedy construction. Exact enumeration checks all 6-axis populations with sum n=3m and n_i<=m for m=0,...,5. Profile numbers: m=0:1, m=1:20, m=2:141, m=3:580, m=4:1751, m=5:4332, total 6825. It checks every 0<=a<=m for 1<=m<=7 in the infinite family, and the 36/12/8/4 witness. Pure integer arithmetic; no floating-point or classical pi/trigonometry. Finite enumeration validates the declared finite coverage; the proofs above establish their claims for all m.

Validation marker: R708_TRIAD_FEASIBILITY_SOURCE_KERNEL_EXACT_PASS.

## 6. Live unfinished native interface

The named event is a candidate R707 equal-quantum Cell triad, not yet a complete source-verified X6 Link/Port, V29 PASS/TRANSFER, V39 loop-flow j or triadic native-rotation generator realization. The next discriminating experiment is to select one exact full triad decomposition at a chosen Cell, attach all required native Link/Port state, and test a single legal PASS/TRANSFER/loop-j update against the hidden-source kernel, retaining all provenance. No P000 or frozen-source change is made.
