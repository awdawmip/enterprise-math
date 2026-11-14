# X6 / LP011 — sharp dominant-axis information loss at native length 3 under the complete 20-slice observer

Date: 2026-11-15 05:00 (Asia/Hong_Kong). Parent: RS-X6-LEGACY-PLANE-RECONCILIATION; immutable publication TP2-B4A441B23DA3159232C2. Author/source: Researcher EM-X6-FB6990; original research SID MCP-082892eb480e45dea6d4b9fcc0491034; existing CLAIM MCP-30a8f5fd123215e08bd4a7cf; RUN RUN-3356cbe3c2b4916d79399941. These are evidence provenance, not a grant of fresh authority.

Scientific pins: P000 V5 signed six-axis Cell torsor and component quadratic @ awdawmip/enterprise-math:59538f585d037d09ef687b28715c4bc1a3f9fe03, compared with the pre-centered historical corpus @ fd2bcff10ca6e147348b6c1236027fc0d2877df3. Current corrected V10 twenty-slice inverse-limit theorem @ f5246fd204222d6c6903536f9336d02d367de173:research_notes/X6_20_SLICE_INVERSE_LIMIT_RECONSTRUCTION_V10_20260905.md; existing LP019 twenty-slice N-BRC proof @ 22b95e723d26d43ec9426bcae29854d9a89262d1. **NEW AUTHOR-PROVED EXACT INTEGER THEOREM / EXECUTED FINITE CERTIFICATE / UNREVIEWED / NOT_ADMITTED.** The historical alleged wrong LP011 argmax *caller* is still UNRESOLVED_PROVENANCE.

## Definitions and retained types

Work on the signed native Cell-displacement lattice Z^6, with six explicitly labeled axes i=0,...,5 and native primitive steps ±e_i. For each triple T of axis indices, let can_T(z_T) subtract the minimum of its three entries. Define the full *derived observation*, not a native identity,
F(z)=(can_T(z_T)) over all C(6,3)=20 triples T.
By overlapping pair differences, F(z)=F(w) iff w=z+kD for an integer k and D=(1,1,1,1,1,1).

Keep the native length L(z)=sum_i |z_i|, native squared component norm G(z)=sum_i z_i^2, **set-valued** native absolute dominant-axis selector A(z)={i: |z_i|=max_j|z_j|}, and positive native shortest path multiplicity B(z)=L(z)!/product_i |z_i|!. F, L, G and B are different typed observables; A remains a native step-axis selection. The path sign on each active axis is the sign of the component, and its order/provenance is not quotiented by F.

## Theorem 1 — sharp earliest failure, and complete classification of all first failure fibres

(i) For all z,w∈Z^6 with F(z)=F(w) and L(z)=L(w)=m≤2, one has z=w. Consequently even F and L alone recover A for those shortest lengths.

(ii) At m=3 there are **exactly 20 distinct nontrivial F,L,G fibres**. For each three-element subset S⊂{0,...,5} the fibre consists of the two distinct native endpoints
  p_S = +1_S (one on S, zero on S^c),
  n_S = -1_{S^c} (negative one on S^c, zero on S).
The same F observation follows from n_S=p_S-D, and both endpoints have L=3, G=3 and B=3!=6. Nevertheless their native selectors A(p_S)=S and A(n_S)=S^c are disjoint. No other F,L,G fibre of length ≤3 is nontrivial.

**Proof.** If F(z)=F(w), write w=z+kD. For each axis, |z_i|+|z_i+k|≥|k|. Hence 2m≥6|k|, or m≥3|k|. If m≤2, k=0 and z=w. At m=3, nonzero k must be ±1, and every coordinate saturates the triangle inequality. Swap endpoints so k=1: each integral coordinate z_i lies in {-1,0}. Equality of lengths forces exactly three entries -1 and three entries 0. Thus (z,w)=(-1_{S^c},+1_S) for exactly one S of size 3. Their G=3, positive B=6 and A sets are as stated. Distinct S yield distinct full F observations, since their 0/1 vectors cannot differ by a nonzero constant. There are exactly C(6,3)=20 such fibres, each of size 2. QED.

A concrete source-identifiable witness: p=(0,1,1,1,0,0) and n=(-1,0,0,0,-1,-1); native A(p)={1,2,3}, A(n)={0,4,5}, with identical complete F, L=3, G=3, B=6. Thus *even preserving both native scalar invariants plus all 20 slices* does not determine native signed-axis dominance; **BRC itself is equal here**, distinguishing the LP011 problem from the later LP019 BRC failures (L=4 for F,L and L=7 for F,L,G).

An infinite exact family: for each integer t≥1, replace 1 by t and -1 by -t in the two endpoints. Then F agrees (difference -tD), L=3t, G=3t², B=(3t)!/(t!)³ for both, and A remains complementary.

## Theorem 2 — exact native argmax reconstruction with one depth-comparator

For arbitrary signed native displacement z, let h=min_i z_i, a_i=z_i-h≥0, M=max_i a_i. The relative data a (equivalently the information partition F) gives min and max index sets; the full integer h is the common-depth repair coordinate. If M=0, A(z) comprises all six axes. For M>0, the exact native selector is
- {i:a_i=M}, if 2h+M>0;
- {i:a_i=0}, if 2h+M<0;
- {i:a_i=0 or a_i=M}, if 2h+M=0.

**Proof.** |z_i|²=(h+a_i)², a strictly convex quadratic in a_i. Its maximum over the finite set {a_i} with extrema 0 and M occurs exclusively at an extremal a-value when M>0. The difference of endpoint squared magnitudes is (h+M)²-h²=M(2h+M). Its sign yields the three exact cases. The M=0 case is immediate. QED.

**Interface consequence.** An implementation that chooses the largest min-zero observer coordinate as the native absolute dominant axis is valid only in the strict positive comparator chamber 2h+M>0 (and M>0), and must retain the full set-valued tie in the equality chamber. Supplying the sign of 2h+M together with the retained relative a is sufficient to recover A. Supplying the original integer common depth h additionally recovers raw native z and all derived lengths, norms and N-BRC counts.

## Reproducible exact finite certificate and provenance

An independently executed stdlib-only Python source test enumerated **every signed six-axis integer endpoint at L=0,1,2,3**, evaluates all 20 triple observations directly (rather than relying on can6 as a code shortcut), and groups by (F,L,G). Its counts are:
- L0: 1 native endpoint, 1 fibre, 0 argmax-ambiguous fibres;
- L1: 12 endpoints, 12 fibres, 0 ambiguous;
- L2: 72 endpoints, 72 fibres, 0 ambiguous;
- L3: 292 endpoints, 272 fibres, exactly 20 two-element argmax-ambiguous fibres.

All 20 ambiguous fibres have equal positive B=6 and complementary selectors. The depth-comparator formula was checked at every enumerated endpoint. A separate integer scaling test covers t=1,...,12 (the proof covers every integer t≥1). Terminal checker output: PASS_X6_LP011_F20_DOMINANT_ARGMAX_SHARP_L3; process exit 0. The exact source used locally is research_checks/X6_LP011_F20_DOMINANT_ARGMAX_SHARP_L3_20261115_0500.py (source SHA256 e38668703609b3c89956e75d331943a162e5ffd28dfe3eae76bf7cff0ff60da8).

**Ledger/update boundary:** This supplies a sharp new LP011 native selector theorem and reconstruction interface, not evidence that a particular pre-rebase executable actually made the alleged incorrect call. Its old callsite remains unresolved. This note neither modifies frozen P000 inputs nor runs/replaces the original R063 C3/C4 512-case benchmark (existing support issue #2416). The separate 17:00 host safety-denied research prose mutation remains stopped, without replay or replacement. Independent Driver REQUEST_REVISION and unfinished 28-LP consumer closure retain their original review status.
