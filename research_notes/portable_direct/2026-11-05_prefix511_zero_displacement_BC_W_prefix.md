# PREFIX-511 — Exact B/C two-dimensional W-prefix on the zero-displacement X6 path fiber

Date: 2026-11-05 (Asia/Shanghai). Researcher-ID: EM-DIRECT-D7DAFF. Activity: RA-5BCBF3AE697DB72CBC4752F8 (native MCP session and Source registration). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. Research conducted as independent author-side contribution; no formal task CLAIM.

Scientific input is the frozen Enterprise Math commit f42f2906d77f24085c123f3ccfe9667d41caa96d. Current P000 and Heartbeat World describe native six-dimensional X6; the ten signed steps here form a restricted five-axis path family **inside** X6. This is a path-observer counting theorem, not a separate lower-dimensional ontology. Direct prerequisites are PREFIX-508 (mod-six V rows), PREFIX-509 (index-free V rank), and PREFIX-510 (N-tag W-prefix).

## Exact theorem

Take an ordered native signed-step word on a/A, b/B, c/C, d/D, e/E; n=2m with m a nonnegative integer and final signed five-axis displacement y=(0,0,0,0,0). Each axis then has the same positive and negative occupation p_i>=0 and sum p_a+p_b+p_c+p_d+p_e=m. Retain the BRC cancellation observations V=p_b+2p_d+p_e and W=p_c+p_e; terminal KMP prefix state q∈{0,1,2,3} for g∈{aab,aba}; and first-source tag t∈{N,B,C}, where source B first means a b/B step is the earliest b/B or c/C step, and source C analogously.

For nonnegative thresholds A,B,C, define the set of **distinct observer pairs** (W,V) which have a realization with p_a>=A, p_b>=B and p_c>=C. For every integer W its exact V support is

    C <= W <= m-A-B,    B <= V <= 2m-W-2A-B-C.      (1)

An invalid interval is empty. Every integer V in (1) is realized. Thus its row weight is

    L_{A,B,C}(W)=2m-W-2A-2B-C+1.

The support count in all rows 0<=W<j is computed by setting

    J = max(0, min(j,m-A-B+1)-C)
    P_{A,B,C}(j)
      = J*(2m-2A-2B-C+1) - J*(2C+J-1)/2.             (2)

The number is an integer, with zero when J=0; no W index and no V enumeration is required. Its full-W value is Phi(m-A-B-C), where

    Phi(h)=(h+1)(3h+2)/2 for h>=0, and Phi(h)=0 for h<0. (3)

For each first-source tag and KMP state, precisely the following threshold triples (A,B,C) apply, in order q=0,1,2,3:

    g=aab, t=B: (0,1,0), (1,1,0), (2,1,0), (2,1,0).
    g=aab, t=C: (0,0,1), (1,0,1), (2,0,1), (2,1,1).
    g=aba, t=B: (0,1,0), (1,1,0), (1,1,0), (2,1,0).
    g=aba, t=C: (0,0,1), (1,0,1), (1,1,1), (2,1,1).

Each list item is a **different (q,t) state**, even if threshold triples coincide. The exact complete B/C W-prefix is the sum of (2) over these eight entries. In particular the full B/C joint-state totals are

    S_BC(aab,m) = 2Phi(m-1)+2Phi(m-2)+3Phi(m-3)+Phi(m-4)
    S_BC(aba,m) = 2Phi(m-1)+3Phi(m-2)+2Phi(m-3)+Phi(m-4).   (4)

Combined with the separately established PREFIX-510 no-source theorem, total **all-tag** joint observations over W,V,q,t for this zero-displacement fiber are

    S(aab,m)=3m(m+1)/2+1+S_BC(aab,m),
    S(aba,m)=(m+1)^2+S_BC(aba,m).                           (5)

The corresponding all-tag W-prefix likewise uses (2) plus the PREFIX-510 N-prefix; its cost is O(1) integer operations on O(log(m+2))-bit inputs, for the fixed two gates.

## Constructive proof

**1. Occupancy geometry.** Fix W. Write E=p_e; since p_c=W-E>=C, E ranges over 0,...,W-C. The remaining budget is p_a+p_b+p_d<=m-W, so setting p_a=A reduces to p_b+p_d<=L=m-W-A. For p_b>=B, all integer values z=p_b+2p_d in the full interval [B,2L-B] occur. Indeed, for a target z write d=floor((z-B)/2), b=z-2d∈{B,B+1}; then b+d=B+ceil((z-B)/2)<=L. The target V=z+E is therefore a union of adjacent translated integer intervals, exactly [B,2L-B+(W-C)]. This proves (1). Counting its integer points and summing an arithmetic progression proves (2) and (3).

**2. Earliest source.** At zero signed displacement, p_b>=1 supplies both the native positive b and negative B steps, while p_c>=1 supplies both positive and negative c steps (both have KMP color c). For tag B, place a b/B source step first; for tag C, place a c/C source step first. Other source steps may follow. q=0 is always constructible because a remaining negative B or c-colored step may end the word. Thus q=0 thresholds are respectively B>=1 and C>=1.

**3. Terminal KMP conditions.** In the zero-displacement family, q=1 for either gate is possible precisely when p_a>=1: the native negative A (color x) immediately followed by positive a realizes terminal prefix a, with a chosen source step earlier. For g=aab, q=2 requires and is realized by two positive a steps (p_a>=2). For g=aba, q=2 requires final colors ab, hence p_a>=1 and p_b>=1. For either gate, q=3 requires the whole gate word at the end, hence p_a>=2 and p_b>=1. The extra B/C steps furnished by p_b>=1 or p_c>=1 can be placed before each displayed terminal suffix, including for B-tag q=3 where the negative B can precede final positive b. These necessary and sufficient conditions give exactly the eight thresholds for each gate. Each reachable controller state is counted once, not once per path.

**4. Summation.** Apply the first-source and KMP threshold list to the exact occupancy region (1), add disjoint (q,t) states, then sum via (2). Formula (4) follows from (3). N, B and C are disjoint first-source tags, so adding the earlier N result yields (5). All claims hold for every integer m>=0; Phi automatically handles small boundary cases.

## Executed checks and scope

An independent native ordered signed-step dynamic program retaining y,V,W,q,t was executed with Python 3 (source and full JSON retained in the same handoff evidence), exhaustively checking both gates for n=0,2,4,6,8,10 (m=0..5). Results: B/C counts for aab 0,2,12,37,84,155; for aba 0,2,13,41,91,165. It checked 42 complete native W rows, 66 W prefixes, 602 individual B/C states, and both-gate all-tag totals against the N theorem. It also checked analytic prefix identities for m=0..60. Result: ALL_CHECKS_PASS. An independently implemented JavaScript certificate stored alongside this note additionally checks full native DP through n=8, and analytic m=0..60, returning ALL_CHECKS_PASS. The arbitrary-m theorem is proved in sections 1–4, not extrapolated from the finite checks.

This exact family provides the full B/C source contribution on the **zero signed-displacement fiber**. Other signed y and the general full-X6 rotation/dynamics remain independent research questions. The declared future operation is append a signed native primitive step then recompute the full observer, retaining q,t and source order; the present compressed prefix is a query accelerator for the specified fiber, not an erasure of the live full state.

## Next unit: PREFIX-512

Extend the threshold-lattice argument to a nonzero signed displacement family, beginning with |y_b|+|y_c|=1 and keeping first-source B/C. Test whether the W,V supports remain contiguous integer intervals or split into exact residue classes. Use PREFIX-508's fixed-mod-six compiler and the native ordered-step DP to distinguish candidate formulas. Compare exact global ranks after including all sources; retain native observer/provenance until their future append update has been verified.

Provenance: frozen project scientific input f42f2906d77f24085c123f3ccfe9667d41caa96d; PREFIX-508, 509, 510; current P000/ACTIVE and joint-observer-preservation contract; docs/PORTABLE_RESEARCH_PROTOCOL.md; currently applicable global math and output policies. Formal independent review and admission have not occurred.
