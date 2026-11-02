# EC49EG — Complete a–g native-X6 multi-horizon prefix-trie theorem

Date: 2026-11-02. Parent: EC49EF (restricted c,d,e grammar). Status: AUTHOR_ANALYTIC_PROOF / TWO_EXACT_CHECKS_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. The proof is author-side, not a native Source Result or Driver review. Existing handoff: Draft PR #1730.

**Frozen scientific source pins:** GLOBAL_KNOWLEDGE_V1 773d538180bfb49e24cffeb35c3ee75eb0628e2e; Enterprise Math fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Current behavioral rules were separately read from canonical main on 2026-11-02. P000 and ACTIVE Heartbeat World unchanged.

## Exact native semantics and observer

Use genuine *ordered, signed six-axis primitive steps*, not a diagonal-plane approximation. The original complete operation alphabet from EC49DW is

    a=(-E1,-E1), b=(-E2,-E2), c=(+E1,+E2,-E1,-E2),
    d=(+E2,+E1,-E2,-E1), e=(+E3,+E1,+E1,-E3),
    f=(+E1,-E1), g=(+E2,-E2).

The two extra operations f,g each cost TWO genuine primitives and have zero native displacement. Historical paths finish at full six-axis displacement -2E1; each future word of exactly h operation letters must return by full native displacement +2E1. A=(+E1,+E2), B=(+E2,+E1) are adjacent *positive* primitive pairs, with the observation recording which event occurred first. Terminal buckets are N, A, B, AB, BA. The nine historical atoms N0,N1,N2,A0,A2,B0,B1,AB,BA record the applicable last-primitive seam port and are realized by nine genuine ten-step histories with identical positive counts (2,2,0,0,0,0) and displacement -2E1. Preserve future-word and horizon labels separately.

For each positive real six-axis vector x and y, retain both exact multiplicative weighted BRC instruments X(w)=prod_i x_i^p_i(w), Y(w)=prod_i y_i^p_i(w), where p_i counts genuine +Ei primitives, plus an unweighted path-count instrument. Under concatenation p(wt)=p(w)+p(t), X(wt)=X(w)X(t), Y(wt)=Y(w)Y(t). Each fixed future-word BRC factor is strictly positive and separately invertible; unequal positive-count words are NOT aggregated before terminal observation.

Let U_ag(H) be the least number of distinct nonempty *signed primitive-step* prefixes of the union of all future words chosen at exact horizons h=2,...,H. At each h its word-by-bucket Boolean transfer must have rank nine over Q on these nine historical atoms. Word sets may contain arbitrary additional words, and individual horizons need not minimize their cost independently. In this problem, equality of word positive-count vectors is NOT required.

## Theorem EC49EG-1: exact all-H optimum

For every integer H>=2, and all strictly positive two-channel BRC weights:

    U_ag(H)=4H+4.

In particular at H=2,3,4,5 the optima are 12,16,20,24 (previous restricted c,d,e costs 28,44,60,76). At h=1 the only returning full-alphabet word is e, and its nine-atom observation rank is five.

**Lower bound for every candidate family, including extra words.** A returning word must satisfy n_b=0 and n_e-n_a=1: only b changes E2 by -2 and only e,a change net E1 by +2,-2. Thus each returning h-letter word has at least one four-step e, and all other letters have at least two primitives, so its signed primitive length is >=2h+2. Consider the genuine historical pair A0 vs A2: they have identical prior A-only observation and BRC positive count, differing only by whether the last primitive is +E2. Their future readouts can differ only if the *first* future primitive equals +E1, creating a new B seam event. The genuine pair B0 vs B1 similarly requires the first future primitive +E2, creating a new A seam event. Therefore any rank-nine family MUST contain one return word beginning +E1 and another beginning +E2. Their nonempty signed-primitive prefixes share no edge from the root. Already these two words at horizon H require at least 2(2H+2)=4H+4 distinct trie edges. This holds irrespective of how many more words are selected at any horizon.

**Uniform upper certificate.** At exact horizon h>=2, choose

    F_h = f e f^(h-2),     G_h = g e f^(h-2).

Both return full displacement +2E1 and contain exactly 2h+2 genuine primitives. The first starts +E1 and the second +E2. They have NO internal A/B adjacent positive pair: each operation ends with a negative primitive and all within-operation positive runs avoid the two ordered pairs. Therefore their terminal A/B-first transitions depend only on the first seam primitive and are independent of h. On the nine genuine historical atoms, the nine Boolean observation columns

    [F:A,F:B,F:AB,F:BA,G:N,G:A,G:B,G:AB,G:BA]

have exact 9-by-9 integer determinant -1 for EVERY h>=2. Hence these two words are a rank-nine right-inverse witness and suffice for every historical population via the earlier nine-feature transfer factorization. Strictly positive BRC factors scale known word columns by nonzero scalars and preserve rank in each instrument.

Moreover F_h is a full genuine primitive-step prefix of F_(h+1), likewise G_h of G_(h+1), with disjoint roots. Consequently the entire shared multi-horizon trie is precisely the two H-horizon paths, with 2(2H+2)=4H+4 edges. This attains the lower bound, proving the theorem.

**No positive-count collapse is assumed.** p(F_h)=(h+1,0,1,0,0,0) and p(G_h)=(h,1,1,0,0,0). Thus X(F_h)=x1^(h+1)x3 and X(G_h)=x1^h*x2*x3; Y uses the same law with y. These future multipliers differ in general and are retained with word provenance. This difference motivates the next scientific unit.

## Exact tests, finite scope and provenance

Executed Python standard-library checker (full original program and JSON included in the separately supplied complete evidence archive) reconstructed nine genuine length-ten X6 histories with identical displacement/count; reconstructed the 9x9 transfer determinant -1, seam events, both BRC factors and shared primitive tries for h=2..25; exhaustively enumerated full a–g returning words for h=1..5: 1,8,51,304,1770 words, checking native displacement, minimal lengths, and exact rank failures if either seam-start port is absent. It returned PASS and reproduced the captured output byte for byte on reexecution.

The independently implemented JavaScript BigInt checker stored alongside this README was executed with Node.js, returned PASS, reconstructed genuine histories and native paths, computed the integer Bareiss determinant -1, BRC concatenation and multi-horizon trie lengths for H=2..64; its original result JSON is preserved alongside this README. The Python exhaustive rank checks used mod prime 1000003; the 9-row 0/1 Hadamard determinant bound is below that prime, so full modular rank exactly detects rational rank nine. All-H optimality rests on the analytic lower bound and uniform construction above, not finite extrapolation.

This is an exact model-internal signed-X6 path/trie result with a *positive* BRC observer. The counted resource is distinct primitive trie edges; RAM, instrument readout and storage cost are separate engineering questions. Protected P000 and ACTIVE worldview are unchanged, and no physical dynamics or signed-phase BRC claim is made.

GitHub actor: awdawmip. Native Enterprise Math MCP 0.6.11 reported research_authority_granted=false; active owner lookup returned CONTROL_QUOTA. No formal native Research Activity, CLAIM, Result or independent Driver review was obtained, and ownership remains unconfirmed. Author-side Draft PR storage preserves the result, not canonical research admission.

## Next executable unit

EC49EH: impose same complete positive-count vector for every selected future word *within* each horizon. Determine the multi-horizon shared signed-primitive trie optimum for H=2,3,4,5 and general H, retaining word/horizon labels, dual positive BRC and the nine actual seam atoms. The F/G certificate here uses different positive-count vectors and therefore is not an equal-fiber construction. Then account for readout and state-storage costs without conflating them with primitive trie edges.

### Evidence references

Canonical predecessors: EC49DW full alphabet, EC49DX nine-atom order observer, EC49DZ nine-feature future transfer, EC49EB native primitive lengths, EC49EC/ED finite and all-h costs for the five-operation language, EC49EF restricted three-operation multi-horizon costs. Complete evidence (the Python source, exact 21K result, independent JS source and result, complete Chinese proof, SHA256 inventory and next unit) is also provided as a local downloadable archive in this run.
