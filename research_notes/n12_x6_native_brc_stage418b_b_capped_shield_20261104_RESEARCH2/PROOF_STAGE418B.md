# Stage418-B — B-capped shielding of two-source native-X6 BRC histories

2026-11-04. Research2 portable author-side proof; continuation of Stage417-B (baa93254d0109f9ba4ab4dcfaebaa54effdaa599), Draft PR #1736. Frozen scientific inputs: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative rules are read separately. Classification: AUTHOR_SIDE_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Exact declared model

D={±E1,...,±E6} is the set of twelve signed native directions in the fixed six-axis space, A=+E1, B=-E1. We observe the complete joint record O(P,Q)=(|P|,|Q|,z(P),z(Q),J(P),J(Q),K(P,Q)); z is the six-component chart-relative endpoint; J is EACH source's full directed D×D adjacency histogram; K counts equal direction labels at the same absolute positions through the shorter word. This is a restricted path population embedded in native X6; the six-axis semantics remain unchanged.

The future language has arbitrary paired APP(a,b), a,b∈D, up to two Q-only POP operations, and up to two paired CANCEL operations. CANCEL is enabled only if the terminal two labels in EACH source are inverse directions, and removes both terminal labels in both sources. Every successful intermediate full observation and every attempted action's enabledness (including DENIED) is observed.

## Theorem 418.1 — common B-capped four-A shield, all finite horizons

Suppose two initial pairs (P,Q), (P',Q') have equal length n, identical complete O, and all P,P' words end in A^4 while all Q,Q' words end in the SAME B A^4, B=-A. Then they are observationally equivalent under EVERY finite common attempted trace in the full twelve-direction APP language with the above POP/CANCEL budgets.

Proof. For each successfully reached state, decompose each source as surviving original prefix followed by surviving appended suffix: P=P0[:n-dP]+U; Q=Q0[:n-dQ]+V. We establish by induction equality of dP,dQ, U,V, remaining budgets and full observations across the compared histories. Initially these data agree.

First establish that the original Q predecessor B is never removed. A paired CANCEL can remove at most one original P label, since the original P terminal A^4 has no inverse adjacent original A's; thus dP≤2 and P has at least two original A's. Q can lose one original terminal A per Q POP or per CANCEL unless a CANCEL deletes the boundary pair (B,A). Suppose the earliest such Q-boundary deletion exists. Immediately beforehand Q must have its original terminal pair (B,A) and zero appended labels; exactly three of its four terminal original A labels have already been removed. Since the purported B-deleting CANCEL is the second or first of a budget of two, these three prior deletions require EXACTLY two POPs and one CANCEL, each removing one original A, so neither POP removed an appended Q label.

The earlier CANCEL must remove one original Q A using exactly one appended inverse B directly above it (original A,A is not an inverse pair). Because no POP removed appended labels and this is the only earlier CANCEL, exactly one simultaneous APP occurred earlier, and no further APP can leave Q's appended tail empty at the purported B deletion. That same single APP put one label onto P. As P still had original A,A at its boundary, the earlier CANCEL removes the appended P label plus exactly one original P A; P then retains at least three original terminal A labels and has no appended suffix. Its last two labels are A,A, so the purported Q-boundary-deleting second CANCEL is disabled on P. Contradiction. Therefore every removed original label on either source is A, 0≤dP≤2 and 0≤dQ≤4. If dQ=4, both POP and both CANCEL budgets have been fully spent; Q's exposed B remains a common terminal original boundary.

The induction now preserves the full observation. Signed endpoints are initial endpoints minus dP*A and dQ*A plus the sums of common U,V. Removing dP terminal original A labels from P deletes exactly dP original AA adjacency edges; deleting dQ≤3 terminal original Q A labels deletes dQ original AA edges; dQ=4 deletes three AA plus the one BA edge. The surviving original/appended junction has common original label A in P, and A or (when dQ=4) B in Q. Internal appended edges are common. Hence both complete directed J histograms agree.

For aligned K, set t=min(n-dP,n-dQ), so t≥n-4. The originally aligned prefix through position t contributes K_initial-(n-t), because every removed original aligned terminal position was (A,A). Every further aligned comparison beyond t includes at least one appended label and any original operand lies strictly after n-4, where BOTH original source words have label A. Such comparisons are completely determined by common dP,dQ,U,V. Thus full absolute-position K agrees without dropping cross-source relations.

APP is unconditionally enabled; POP depends on the common budget and Q length. For CANCEL the last two P labels are determined by its surviving original A^≥2 and common U, and the last two Q labels by its surviving original terminal A-run (or the common B once four As are removed) and common V. The inverse tests agree. At dQ=4 no CANCEL budget remains. Each successful action preserves equality of deletion counts and appended tails because the original/appended boundaries used by a terminal operation have identical labels and status. An attempted denied action is denied for both pairs. Induction closes for every finite operation sequence. QED.

The B cap allows four rather than five terminal Q As because the second CANCEL cannot remove the preceding B after two original-Q POPs and one prior original-Q CANCEL. This argument is budget-aware and retains joint K, provenance and directed J.

## Theorem 418.2 — 16 ≤ q(F_n) ≤ 26 for all n≥11

The Stage411/415 complete initial-observation fiber is P_i=A^(i-1) B A^(n-i), Q_(r,s)=A^(r-1) B A^(s-r-1) B A^(n-s) for 2≤r, r+2≤s≤n-1 and i∈{r,s}. It has (n-3)(n-4) histories and equal complete initial O. Stage416 established 32 sufficient raw (last6(P),last7(Q)) keys for every n≥11. Stage417's three exact fixed future tests distinguish sixteen signatures and proved that its class 0, s≤n-5, merges FOUR raw keys into one full-future class.

The Stage417 class 1 is exactly s=n-4, with either i choice and 2(n-7) histories. Every such history has P ending in A^4 and Q ending in B A^4. By Theorem418.1 its FOUR raw keys merge into ONE full-future class. Distinct fixed future-test signatures remain distinguishable. Thus the 32-key sufficient bound loses three keys from class 0 and another three from class 1, proving precisely the bounded interval 16≤q(F_n)≤32-3-3=26 for all integers n≥11.

For n=16 there are 156 histories. Stage417 class 0 contains 72 and new Stage418 class 1 contains 18 histories. These 90 histories collapse to two distinct all-future states. The remaining fourteen finite-test signatures occupy twenty-four raw safe keys; their possible further full-future mergers remain the next question.

## Executed exact validation and limits

The saved standard JavaScript REPRO_STAGE418B.js was actually run with Node.js. It verifies 1,110 class-1 histories at n=11..40, four safe suffix keys and common full O for each n. For n=11 its four raw representatives agree over every successful/denied prefix of 10,243 finite traces with ≤1 APP using all 12 native directions, 395,573 traces with ≤2 APP using all 12 directions and ≤1 POP/≤1 CANCEL, 47,491 traces with ≤2 APP over ±E1,±E2 and full budgets, and 27,455 traces with exactly 3 APP over ±E1 and full budgets. Program returns STAGE418B_B_CAPPED_CLASS1_PASS and the actual stdout is saved as REPRO_STAGE418B_EXECUTED.json. The universal theorem is proved above, not inferred from finite test counts.

BRC observer preservation: original path order, source identity, six-component endpoints, both full directed J histograms and joint K are retained until the scoped all-future quotient is established. This uses the Stage412 Euler/K counting and the native-X6 BRC direction interface at its declared scope, not a new physical-coordinate or Foundation theorem.

## Next scientific unit

Stage419-B: study signatures 2 and 3 (s=n-3; i=r versus i=s), each three raw keys. Their Q terminal form B A^3 may permit a second CANCEL to expose the preceding B, so the new proof must inspect the exact destructive budgets and aligned K. Find a full-horizon bisimulation or a shortest explicit distinguishing trace in the full native 12-direction alphabet. Then continue with the other signatures and, once classes are decided, reuse the Stage412 Euler/K dynamic-program counts. Native Owner, CLAIM, Source Result and independent Driver review remain separate authority processes.
