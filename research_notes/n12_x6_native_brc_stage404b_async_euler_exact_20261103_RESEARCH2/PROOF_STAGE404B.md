# Stage404-B — exact asynchronous minimal memory and coupled Euler transfer

Date: 2026-11-03. Parent: Stage403-B, commit 6e2d17d14ab6760f2fdf8ebe2e895cbe98980a56, Draft PR #1736. Classification: author-side mathematical proof and exact executable check; UNREVIEWED / NOT_ADMITTED.

Frozen scientific inputs: Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; account science bf84bd7c61a2444b59b1da96be57df0e9ae47e53; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Applicable current behavioral rules are separate. No changes to P000, ACTIVE worldview, or source pins.

## Definitions

Let D be the twelve signed native directions +Ei,-Ei (i=1,...,6), with formal inverses. A finite word is a Path-formal ordered native-source history. For two initially equal-length words P,Q of length m, observe both lengths, native six-axis displacements zP,zQ, each complete ordered adjacency count JP,JQ, their 20 triple readouts, exact unweighted native BRC endpoint counts N_m(z), and the absolute-index coincidence K(P,Q)=sum_{i<=min(lengths)} 1[P_i=Q_i]. Positive weighted BRC endpoint masses and multiplicative signed direction traces remain separate optional typed observers; for the examples their values are determined by the marginal endpoints or label counts.

The future operation language contains arbitrary paired APPEND(a,b), at most one POP_Q (delete one final Q letter), and up to C paired CANCELs (delete the two final inverse letters of each source, enabled only if both pairs are inverse). Budgets are cumulative. Enabledness and every intermediate observation are visible. This is a formal source-path operation language, not physical Cell dynamics.

For C=0 and m>=2, write T0(P,Q)=(last(P),penultimate(Q),last(Q)).

## Theorem 404.1 — exact individual-fiber quotient when C=0

For any m>=2 and any two equal-current-observation source pairs (P,Q),(P',Q'), the pairs have identical future observation and action-enabledness behavior for *every finite legal continuation* of paired APPEND and at most one POP_Q if and only if T0(P,Q)=T0(P',Q').

Proof (sufficiency). Before the Q-only deletion, each paired append extends both words at equal absolute index, contributes 1[a=b] to K, adds one known directed adjacency from the current last letter in each source, and adds known native steps to z. Equal T0 makes every update equal. If POP_Q first occurs after one or more APPENDs, it removes the last appended Q symbol, whose predecessor is known from the common append history (or original Q last at the first appended position). If POP_Q occurs immediately, the deleted original Q last and remaining original Q penultimate are both in T0. Its changes to Q length, z, J and K are therefore equal. Thereafter length(P)=length(Q)+1 permanently because there are no CANCELs. Each paired APPEND(a,b) compares the *previous* last P label (at index new Q length) with b for its K increment; this label is the original last P or an already known appended label. All further updates remain equal. Thus all finite continuations preserve observation and enabledness.

Proof (necessity). If the final P labels differ, the first paired APPEND(a,b), for any common a,b, adds different directed adjacency entries (lastP,a) to the currently equal JP, revealing the difference. If the final Q labels differ, immediately POP_Q; the resulting native six-axis zQ differs because the twelve signed native step vectors are distinct. If only the Q penultimate labels differ, immediately POP_Q; the removed directed edge (penultimateQ,lastQ) differs and the resulting JQ differs. Hence each component of T0 is necessary. QED.

Corollary. For any finite complete current-observation fiber F with common m>=2, its exact minimal additional state count is
q0(F)=|{T0(P,Q):(P,Q) in F}|, with fixed-length bits ceil(log2 q0(F)).
An exact coupled-Euler transfer retaining last two paired letters computes T0 without enumerating complete word pairs; the initial P penultimate is provably redundant at this horizon.

## Theorem 404.2 — strict full-fiber lossless compression with K>0

Write A=+E1, B=-E1. Take P1=AABA, P2=ABAA, Q=AAAA. Each has native length four. The two P histories have identical directed adjacency J_P={AA:1,AB:1,BA:1}, endpoint 2E1, direction counts and all endpoint-dependent BRC outputs; Q is fixed, J_Q={AA:3}. The current coincidence K is 3 for both. The marginal P Euler words with the prescribed J_P and endpoint 2E1 are AABA, ABAA and BAAB; BAAB has K(BAAB,AAAA)=2 and is excluded. The only Q word with J_Q and endpoint 4E1 is AAAA. Thus the *entire* exact current-observation fiber consists of the stated two source pairs.

Both pairs have the identical T0=(A,A,A); Theorem 404.1 therefore certifies exact future equivalence for the full twelve-symbol APPEND language and one Q POP. Their length-2 *paired suffixes* differ: (B,A),(A,A) versus (A,A),(A,A). The uniform Stage403 paired-suffix representation has two states, while the exact quotient has one: 1 bit -> 0 bits. Native twelve-direction BRC recurrence N4(2E1)=64.

## Theorem 404.3 — coupled residual-Euler transfer

For any two complete separate ordered-edge multiplicity matrices JP,JQ on D, fixed desired endpoints zP,zQ, coincidence K and positive tail window L, the following integer recurrence computes exactly the distribution of final paired suffixes of length min(m,L), without listing complete word pairs.

Choose starting vertices sP,sQ compatible with their endpoints: for each marginal source, label multiplicity n_v = indegree_J(v)+1[v=s], and z=sum_v n_v * native_step(v). Initialize residual matrices RP=JP,RQ=JQ, current vertices (sP,sQ), k=1[sP=sQ], tail=((sP,sQ),). For each ordered pair of available outgoing edge *types* (u->v, x->y) with residual multiplicities >0, decrement each multiplicity by one, update k+=1[v=y], and shift the paired suffix window by (v,y). At both residual matrices zero, emit one contribution to the resulting tail exactly when k=K. Add contributions from all compatible starts. Each label-path pair has exactly one such sequence; repeated edges have no artificial factorial multiplicity. Induction over unused edge counts proves the recurrence exact.

This is a count distribution D_L(o,t), not in general the minimal future quotient: for C=0 aggregate by T0, and for C>0 quotienting still depends on allowed operations. With a fixed 12-symbol alphabet and fixed C, L=2C+2 gives a numeric-m polynomial-size finite residual DP whose worst state count grows as a polynomial with degree depending on the number of directed edge types; it is not a general polynomial bound in the binary bit length of JP,JQ. Output integers may have exponentially many represented paths; count bit lengths must be included when claiming total runtime. No complexity improvement relative to an unspecified representation is asserted.

## Proposition 404.4 — an exact five-state C=2 fiber

Let A=+E1,B=-E1,T=+E3, P0=TTTAABAB and Q0=AABABABA, and fix m=8, the complete pair of marginal J matrices and displacements of (P0,Q0), and K=1. The full current-observation fiber is exactly five path pairs:

1. (TTTAABAB,AABABABA)
2. (TTTAABAB,ABAABABA)
3. (TTTAABAB,ABABAABA)
4. (TTTABAAB,ABABAABA)
5. (TTTABAAB,ABABABAA)

The residual-Euler transfer gives five distinct paired last-six-symbol states, each of multiplicity one. Independently enumerating the two marginal Euler trails under J and filtering by endpoints and K gives the same five. One fixed attempted future action trace, POP_Q then CANCEL then CANCEL, has five different sequences of observations/enabledness; in particular a disabled action is an observable outcome. Thus all five are pairwise distinguishable, while the entire fiber has exactly five members, so q2(F)=5, requiring ceil(log2 5)=3 bits. No Stage403 suffix theorem is needed for this exact five-state conclusion.

Exact all-12-direction endpoint counts are N8(zP)=68768 and N8(zQ)=385056. These count *all* native paths with the endpoint, distinct from the J-filtered five source pairs.

## Exact computation and evidence

File REPRO_STAGE404B.py runs: (1) integer-only marginal-Euler residual transfer for both fibers, (2) independent full Euler-word enumeration for these small fibers, (3) exhaustive common APPEND/POP continuation checks over A,B,T through depth four (10,559 compared reachable nodes) for the two C=0 pairs, (4) a five-way exact POP/CANCEL observation trace, and (5) unweighted 12-direction native BRC recurrence at n=4,8. Program was executed twice with byte-identical JSON stdout; recorded in REPRO_STAGE404B_EXECUTED.json. Return marker: STAGE404B_EULER_ASYNC_MINIMAL_PASS.

Theorems 404.1 and 404.3 are general mathematical arguments. Finite program assertions are crosschecks of the stated examples and restricted finite enumeration ranges. Full 12-direction APPEND coverage of Theorem 404.1 follows from its proof, not the 3-label experiment.

## Next frontier

Stage405-B: characterize the exact quotient for C=1 with one Q-only POP, find the shortest nontrivial fibers in which the 2C+2 paired suffix overcounts the minimal quotient, and construct a finite symbolic equivalence checker whose state is initial observation, remaining budgets, last needed source labels, and shifted coincidence boundary. Preserve absolute-index K, distinct positive/signed BRC types and native X6 source identity.
