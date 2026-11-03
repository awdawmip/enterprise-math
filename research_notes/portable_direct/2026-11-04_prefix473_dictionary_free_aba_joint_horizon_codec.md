# PREFIX-473 — Exact dictionary-free BRC × aba suffix-state encoding

**2026-11-04 | AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.** Native CLAIM, Result and Review not asserted.

## Model, observer and prior work

Frozen scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Compose PREFIX-470 (aba suffix occupancy theorem), PREFIX-471 (invertible X6 BRC gate normalization), PREFIX-472 (exact dictionary-free base-state ranking). P000 keeps six native spatial axes and separate time. We use a typed eleven-step subalphabet: special `x=+E1` and ordinary `±E2,...,±E6`. Every ordinary step is legal. An x is legal in the initial position or after the exact terminal word `aba`, where a=+E2 and b=+E3.

For path length n, the base exact positive-valuation readout is `f=(s,y1,...,y5,A,C)` with s=#x, signed displacement yi=ci+−ci−, pair count pi=min(ci+,ci−), and A=p2+2p4+p5, C=p3+p5. Let S_n be all reachable base readouts, B_n its cardinality; put B_m=0 for negative m. The KMP suffix state q=0,1,2,3 records longest final substring matching the prefix of aba, with q3=aba. A joint observation key is (f,q), not an ordered path or its multiplicity.

**Target.** For each n≥0 and future operation horizon H≥0, find a dense reversible ranking without materializing a whole codebook, retaining Boolean continuation admissibility and resulting base readout. Individual ordered-path provenance and q-separated multiplicities need a distinct carrier.

## Lemma 1 — exact reversible ordinary padding

For one ordinary positive letter repeated h≥0 times on an axis, with original signed displacement y and canceling-pair count p, direct reconstruction of positive and negative counts gives

`y_new=y+h; p_new=p+min(h,max(−y,0))`.

Its inverse subtracts h from y_new, recomputes the known increment and subtracts it from p_new. Therefore appending any known word of positive ordinary directions gives an injective reversible map on the base observer even where individual pi are not fully retained: each valuation increment is determined by known y and the word's axis multiplicities.

For v1=a, v2=ab, v3=aba, define T_j on f using (h_a,h_b)=(1,0),(1,1),(2,1):

`T_j(s,y,A,C)=(s,y+h_a e_a+h_b e_b,A+min(h_b,max(−y_b,0)),C)`.

Here b pairs are p2 and contribute coefficient one to A; a pairs are p1 and contribute to neither valuation coordinate. Inversion is explicit. This remains valid when initial y_b<0.

## Lemma 2 — all four reachable history supports

PREFIX-470's verified word-rearrangement and suffix deletion argument yields, for all n:

`S_(n,1)=T_1(S_(n−1)); S_(n,2)=T_2(S_(n−2)); S_(n,3)=T_3(S_(n−3))`.

For q2 and q3 the terminal suffix is exactly ab or aba and may be deleted; appending it to any legal prefix is legal. For q1 choose a representative of any predecessor base state not ending ab, by putting any x blocks in canonical form `x(aba x)^(s−1)` and ordering leftover ordinary b before a; append a. Deleting the terminal a gives the reverse. Lemma 1 ensures each support image is injective.

The q0 support is S_n except a finite exceptional set E_n, explicitly classified and proved in PREFIX-470: E_0 empty; E_1 contains f(a); for n≥2 it contains f(a^n), f(a^(n−1)b), f(xa^(n−1)), and also f(xab) precisely when n=3. These exceptional readouts have no hidden canceling pair because n=s+sum(abs(yi)), so a different Parikh representative cannot repair their q0 exclusion. Define t_n=|E_n| (t0=0, t1=1, t3=4, otherwise t_n=3 for n≥2). Consequently the four tagged q block sizes are

`Q0(n)=B_n−t_n, Q1(n)=B_(n−1), Q2(n)=B_(n−2), Q3(n)=B_(n−3)`.

The complete joint-state count is F_n=sum(Qj(n)). The result counts support, not total ordered paths; q0 holes prevent naive Cartesian-product counting.

## Theorem 3 — optimal no-codebook joint rank and inverse

Let R_n and its inverse be the actual explicit PREFIX-472 base ranking for gate length k=3; it uses constant-degree prefix formulae and signed-vector binary searches, not enumeration. Compute the at most four distinct sorted hole ranks `e1<...<et` by applying R_n to the explicit E_n.

For q0-reachable f define `D0(f)=R_n(f)−number_of_holes_strictly_below_R_n(f)`. This maps q0 states consecutively onto 0,...,Q0−1. Its inverse starts with integer u and traverses the hole ranks e_i in ascending order, adding one to u whenever e_i≤u; then applies R_n inverse. Exactly the excluded ranks are skipped.

For suffix j=1,2,3 set offset `O_j=Q0+sum(B_(n−i),i=1..j−1)`. Define `D_j(f,j)=O_j+R_(n−j)(inverse_T_j(f))`. To decode, locate the unique q block by offsets, decode the smaller-length base rank, and append the known ordinary word T_j. For q0 use the hole-skipping decoder above.

Lemmas 1–2 imply the tagged blocks are disjoint, exhaustive, and are bijective with the consecutive integer interval 0,...,F_n−1. Thus exact fixed-width encoding uses precisely `ceil(log2(F_n))` bits (zero if F_n=1), the information-theoretic minimum. Only a constant number of established base rank/inverse operations, no joint dictionary. With fixed aba, integer-operation complexity is O(log(n+1)), integer operands O(log(n+1)) bits, inheriting PREFIX-472 prefix and integer-arithmetic bit costs. This does not promise constant-time machine operations or sublinear enumeration of a full nonzero path-state population.

## Theorem 4 — arbitrary finite-future H, exact minimal quotient

Shortest further words enabling an x from q=3,2,1,0 have lengths 1,2,3,4 respectively: x, ax, bax, abax. Consequently the H-future language equivalence is:

`H0:{0,1,2,3}; H1:{0,1,2}|{3}; H2:{0,1}|{2}|{3}; H>=3:{0}|{1}|{2}|{3}`.

Every base f has at least a q0 or q1 representative, including the explicit excluded q0 keys. Hence the first block for H≤2 contains exactly the entire base support and ranks directly with R_n. Each remaining q2 or q3 block uses the same pad/inverse sublength ranking as above. The precise number of classes for n,H≥0 is:

`N(n,0)=B_n; N(n,1)=B_n+B_(n−3); N(n,2)=B_n+B_(n−2)+B_(n−3); N(n,H)=F_n for H>=3`.

Therefore an explicit dictionary-free reversible rank exists onto exactly 0,...,N(n,H)−1, with optimal width ceil(log2(N(n,H))) and O(log(n+1)) arbitrary-precision integer operations. The decoder at H<3 outputs the future-equivalence **class**, not a fictitious exact original q. The class is sufficient for declared legal-continuation and final-base observations, not for separate q multiplicities or ordered-source records.

## Exact execution, evidence, and limits

Attached `PREFIX473_EXECUTED_CODE_AND_LOGS.tar.xz` contains four real files: `prefix473_joint_codec.py` (independent Python3 exact integer codec, reversible ranking, exact DP and small-word enumeration), `PREFIX473_EXACT_EXECUTION.log`, `check_large_dp.py` (independent extended DP), `PREFIX473_EXTENDED_DP.log`. The archive has been locally listed/extracted and has SHA-256 `dfde53997cd59509dbe0bf8ac2cdac37646cc71c54728be776c28b70193c49e8`; the Git object SHA is `3dd27c6d0a3667ea7a3fa84f7b2580fd93046606`.

Code executed exhaustive joint rank/inverse for all 5,668 reachable tagged states, all n=0..5 and four H classes; direct ordered-path DFS through n=4 crosschecks independently propagated exact integer dynamic programming. DP itself continued to n=8, including exact suffix counts, base support, horizon counts and total ordered-path integer multiplicity; n=6..8 use selected ranks. Exact roundtrips at n=16,64,1024,10^9 used selected integers, not exhaustive enumeration.

At n=8: B=33295, (Q0,Q1,Q2,Q3)=(33292,15697,6824,2685), F=58498, horizon counts=(33295,35980,42804,58498), ordered paths=110054001. Actual logs conclude `ALL_CHECKS_PASS` and `DP_COUNTS_AND_SAMPLED_CODEC_ALL_PASS`. Universal statements follow from the exact lemmas and predecessor results, not finite testing alone.

BRC reuse: **COMPOSE_APPLIED** — PREFIX-470 KMP occupancy, PREFIX-471 normalization and PREFIX-472 base codec. No signed/phase arithmetic, trigonometric or BRC–Shor experiment was performed.

**Next PREFIX-474:** general KMP gate words with overlapping prefixes; determine which suffix-support sets equal injective fixed-padding images of a shorter base set and whether their q0 holes remain uniformly bounded. Search first counterexamples with a growing exceptional support family; independently derive suffix-conditioned exact path-multiplicity generating functions and retain the unrelated arbitrary-order X6 moment-rank problem.

**Authority:** GitHub authenticated login awdawmip, repository admin/push. Native task inventory rejected as CONTROL_QUOTA; Site-scoped identity is static readonly and research_authority_granted=false. Active native Owner, Researcher-ID and formal CLAIM unverified. Author-side portable source proof is neither independent review nor admission; P000/ACTIVE not modified.
