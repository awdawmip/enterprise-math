# R762CA — Exact C3-covariant signed triadic closure / Port-gate classification

Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. Date: 2026-11-16.
Status: AUTHOR-PROVED CONDITIONAL FINITE THEOREM / EXACT CHECKS PASSED / INDEPENDENT REVIEW NOT_REVIEWED. Native TRIADIC_CLOSURE_E licensing, Cell dynamics and V17/V29/V39 physical transducer remain OPEN. No formal Result, Foundation promotion, or physical residual attribution is claimed.

## Sources, assumptions and precise scope

The frozen task science remains awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json (actual blob dc84bdae6595b5e237a2ad50d8b21916adb2e447), its pinned P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md, and taskbook blob 218bf9ce05fd2dd79f477ac269fc3590f83f482e. Current P000 and ACTIVE worldview preserve six signed native axes in a discrete Cell torsor, distinct time, PERP_E/120-degree native orthogonality, three-force primitive closure and obligatory triadic lift of an apparent two-force equilibrium. No classical Euclidean force sum is used.

R762BY, PR #2544@91356f8b05c2682ca1bf454d9ea5fae686b7ee95, proved that a fixed, sign-INDEPENDENT eligible Port set J has S_J return holonomy and that C3 covariance forces static J to be empty or all. R762BZ, PR #2547@18e395e906bbad861cfe6afb3a5c33799d86d6e8, proved an exact eight-element conditional two-Port lift fiber. V17 source research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md (Git blob 42b810a8f82c504833027da17884cc4fb2943e5b) defines conditional shared-axis, slot-inheriting transport, NOT an independently licensed physical primitive event.

Fix one X6 Cell anchor c and positive equal quantum q. Three named Port slots 0,1,2 carry a directed Link cycle 0→1→2→0. An ordered axis tuple a=(a0,a1,a2) is an injection from the Ports into native axes A={1,...,6}; a sign word s=(s0,s1,s2) belongs to {+,-}³. There are 6·5·4·2³=960 signed frames at fixed c,q. Signed direction means a typed Port attribute, not a signed physical amplitude.

The CONDITIONAL candidate switch (p,y) replaces a_p by unoccupied native label y, retaining c,q, the three named Ports, all signs, the Link cycle and the ordered event provenance. Let C(s) be a sign-only Boolean closure predicate and g(s,p) a sign-rooted Boolean permission predicate. A conditional event exists precisely when C(s)=1, g(s,p)=1 and y is unoccupied. Since events preserve s, they remain within the same closure sector. Not every sign word is automatically a licensed native balance; this is a classification of candidate sign-only laws.

Simultaneous S6 axis relabeling and cyclic C3 rotation of Port, sign and Link positions are the declared covariance group. Reflection of the oriented Link cycle (D3), and global sign reversal, are ADDITIONAL optional assumptions, never silently imposed.

## Theorem A — exact 16 / 256 / 729 classification

There are exactly 16 S6×C3-invariant sign-only closure predicates C; exactly 256 S6×C3-covariant sign-rooted gates g; and exactly 729 coherent pairs (C,g) with g(s,p)=1 implying C(s)=1.

Proof: S6 acts transitively on injections a with three occupied labels and leaves the sign word unchanged. Thus the independent Boolean data are the sign word for C and sign word plus marked Port for g. C3 partitions the eight sign words into four orbits: +++, ---, exactly one minus, and exactly one plus, with sizes 1,1,3,3. Hence C has 2^4=16 choices.

On (s,p), a nonidentity three-cycle cannot fix marked Port p. Every C3 orbit has size 3; the 8·3=24 rooted words give exactly eight orbits and 2^8=256 gates. A gate is equivalently any Boolean function F(s_p,s_(p+1),s_(p+2)), whose arguments are read cyclically from the event Port.

The number of rooted gate orbits lying over the four closure orbits is respectively 1,1,3,3. If a closure orbit is excluded, the gate above it must be zero, leaving one choice. If included, its r gate bits may be freely selected (2^r choices). Therefore the coherent count is (1+2)(1+2)(1+8)(1+8) = 729. All signs and all Port positions were included in the orbit argument. QED.

The 729 are NOT asserted to be actual physical licenses. In particular, P000's equal-quantum canonical closure cannot be translated into arbitrary sign-sector acceptance without the missing sign-to-TRIADIC_CLOSURE_E correspondence.

## Theorem B — additional, explicitly hypothetical symmetries

If an extra Port reflection reversing directed Link orientation is imposed, rooted gate orbits above the four closure classes have multiplicities 1,1,2,2. This yields 16 closure laws, 64 rooted gates and 3²·5²=225 coherent pairs.

If instead global sign reversal is imposed alongside C3, the closure orbits merge into two classes (homogeneous and mixed), with gate-bit multiplicities 1,3; the numbers become 4 closure laws, 16 gates and (1+2)(1+8)=27 coherent pairs.

If both extra transformations are imposed, the rooted multiplicities over the two closure classes are 1,2, yielding 4 closure laws, 8 gates and (1+2)(1+4)=15 coherent pairs.

These are exact orbit-stabilizer counts. The original oriented Link interface does not itself authorize reflection or global sign gauge.

## Theorem C — proper sign-gated Port permissions preserving C3

Set C(s)=1 as a conditional illustration and g_+(s,p)=[s_p=+]. This gate is invariant under S6 axis relabeling and covariant under C3 rotating the Ports and their sign attributes. Yet for mixed sign patterns its set J(s) of eligible Ports is a PROPER subset. Thus the R762BY no-proper-gate claim applies only to static sign-independent J, not the wider sign-rooted family.

The numbers of sign words with k=0,1,2,3 positive Ports are 1,3,3,1. For a fixed sign word s, J(s) is preserved along every candidate event, and R762BY's exact return-holonomy proof applies without change: holonomy group S_(J(s)), with |S_J|=k!. The sharp terminal named-Port-order repair bits with known sign word and observed unordered return triad are ceil(log2(k!))=0,0,1,3 for k=0,1,2,3. This is a terminal-observer claim, not safe collapse of full event histories.

If a future observer must recover both the full sign word and terminal named-Port ordering from the unordered triad, the union over all finite path lengths contains exactly
1·0! + 3·1! + 3·2! + 1·3! = 16
distinct signed terminal signatures. Hence a 4-bit fixed-length repair is necessary and sufficient for THIS observer. At fixed exact length m=0,1,2,3 the return signature counts are respectively 8,0,7,13; at every fixed m≥4 they are 15 because the all-minus gate has no positive-length path. The 15 bound uses the previously proved exact-length S_J supports from R762BY. Full BRC provenance can require larger state.

## BRC branch census and exact validation

The underlying branch population is the multiset of ordered paths, with Cell, named Port, axis labels, signs, Link and event index conceptually retained. The scoped terminal-frame count observer pushes those branches forward using N_(m+1)(F')=sum_(F→F') N_m(F), initialized at N_0(123;s)=1 for each of eight sign words. These are NONNEGATIVE INTEGER PATH MULTIPLICITIES, not physical signed amplitudes, cancellation or an implementation of a full native BRC propagator. The dynamic-programming aggregation is exact for the declared terminal observer, without an arbitrary-future safe-erasure claim.

For the sign-positive gate, aggregate based-return path counts for m=0..8 are
8, 0, 36, 108, 846, 5418, 41580, 324576, 2664810.
Distinct (sign,holonomy) based-return signatures for m=0..8 are
8, 0, 7, 13, 15, 15, 15, 15, 15.
They equal binomially weighted sums of previously saved R762BY k-gate counts, weighting k=0,1,2,3 by 1,3,3,1.

The companion Python verifier exhaustively enumerates four requested orbit systems, directly checks all Boolean coherent pairs, performs 51,840 S6 relabeling checks and 8,640 C3 covariance checks, and computes exact positive-integer path pushforwards through length 8. All assertions passed locally. Exactness comes from the finite domain and orbit proof, not finite extrapolation. No π, trigonometry, Euclidean vector force sum, time calibration, or native residual inference was performed. Independent review remains NOT_REVIEWED.

Files: R762CA_VERIFY_PORTABLE.py, R762CA_VERIFY_PORTABLE_EVIDENCE.json.

## Open scientific dependency and next discrimination

The full task still requires a justified actual signed Cell/Port/Link TRIADIC_CLOSURE_E predicate and lawful event-to-V17/V29/V39 transducer. The sign-only 729-candidate classification proves that S6×C3 covariance alone does NOT select a unique source dynamics. One may now confront actual native licensing and signed rotation with 729 concrete coherent alternatives; if the licensed predicate depends on Cell, Link, provenance or event history, this restricted sign-only family must be enlarged rather than mistaking its count for a universal bound.

Next precise unit: read authenticated native event/rotation source rules, determine the sign-sector closure and Port/Link transition semantics, eliminate inconsistent candidate gates, and recompute observer-safe BRC source fibers on the legal subgraph. Preserve frozen P000, author history and all previous R762B* results.