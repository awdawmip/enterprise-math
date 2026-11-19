# X6 R27 — Link feedback reveals dormant source bits at exact horizon eight

Date: 2026-11-19. Task: RS-X6-NATIVE-TIME-DYNAMICS, publication TP2-91D4A7C2F63805BE21A3. R26 predecessor: \`7d0763cb06daf5d27cd165888eed707aef84a2b6\`. Frozen pins: P000 V5 \`a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`; taskbook \`f41c2690daba467ecbde99615a1337e67be46ffd:research_tasks/RS_X6_NATIVE_TIME_DYNAMICS_20260906.md\`. Status: CONDITIONAL_AUTHOR_PROOF / EXACT_BOOLEAN_BRC_PASS / NOT_REVIEWED / NATIVE_EVENT_ADMISSION_PENDING.

## Controller and complete event-language observer

Take a finite simple graph G=(V,E), m=|V|>=1. Each named complete triadic source B_i has a disjoint two-Cell signed-axis lane embedded in six-dimensional native X6. Its B_i^+ and B_i^- events alternate, with the first return setting permanent flag r_i. Conserved hidden frame bits theta_i in {0,1} do not affect B moves. Each edge e={i,j} has an intact one-use consumer A_e, executable exactly after both endpoint returns when theta_i=theta_j=1; execution sets usedA_e. This is the R26 model.

**New R27 feedback:** Every vertex k has an additional intact one-use consumer Q_k. Q_k is enabled exactly if some A_e was previously executed, r_k=1, theta_k=1, and Q_k is unused. It changes only its own used bit. Lanes and consumers are disjoint; each event carries its own genuine signed native-Port label. A_e therefore activates a global family of source-sensitive probes. The feedback is a *declared conditional model*, not yet a source-verified native TRIADIC_CLOSURE_E admission law.

The observer records all SUCCESSFUL words with complete source, signed Port, order, A and Q labels, but does not read theta, internal flags, failed attempts or physical durations. Let S={i:theta_i=1}, F(S)=E[S] be the active induced edge set and L_h(S) the Boolean successful-word language of length at most h. The exact Boolean BRC carrier is the set of such labeled traces, with Boolean union and prefix-concatenation; recursive interned successor signatures test language equality without counting word multiplicity as mass.

## Theorem R27.1 — Exact first distinction in three observation phases

For any finite G and S,T subseteq V:

1. If 0<=h<=4, all initial languages L_h(S) are equal.
2. If 5<=h<=7, L_h(S)=L_h(T) iff F(S)=F(T).
3. If h>=8, L_h(S)=L_h(T) iff S=T, or both S and T are independent sets of G.

For distinct S and T the exact first distinguishing successful-word depth is

\[
\delta(S,T)=
\begin{cases}
5,&F(S)\neq F(T),\\
8,&F(S)=F(T)\neq\varnothing,\\
\infty,&F(S)=F(T)=\varnothing.
\end{cases}
\]

**Proof.** An A event first requires two endpoint excursions (four B events), then A itself (fifth event). All shorter words contain only B events and are theta-independent. The word \`B_i^+ B_i^- B_j^+ B_j^- A_{ij}\` exists exactly if ij belongs to F(S), distinguishing unequal edge signatures at depth five.

After an A event, Q_k first requires r_k and theta_k=1. If k is an endpoint of that A edge, its return has already occurred and a Q word may appear at depth six, but theta_k=1 is already determined by the active-edge signature. If k is not an endpoint, its two B events are additionally necessary; no Q witness of its hidden bit has length below eight. Thus equal active-edge signatures determine all words through horizon seven, irrespective of interleaving.

If both supports are independent, no A ever fires, hence no Q ever fires: their successful languages coincide forever. If F(S)=F(T) is nonempty but S differs from T, choose k in their symmetric difference. Since the endpoints of every active edge belong to both supports, k lies outside every active edge. Choose any active e={i,j}. Then the eight-event word
\`B_i^+ B_i^- B_j^+ B_j^- A_e B_k^+ B_k^- Q_k\`
exists precisely when theta_k=1. This is the first distinction by the preceding horizon-seven equivalence. Identical supports have identical transition rules at all states. QED.

## Theorem R27.2 — Exact quotient sizes and residual

Let I(G;1) count independent subsets (including empty). Let
\[
C_{26}(G)=\#\{W\subseteq V : G[W]\text{ has no isolated vertices}\}
\]
also count the empty W. Then the exact number of future-language classes of the common initial public fiber is

\[
C_h(G)=
\begin{cases}
1,&0\le h\le4,\\
C_{26}(G),&5\le h\le7,\\
1+2^m-I(G;1),&h\ge8.
\end{cases}
\]

The minimum fixed-length representation needs \(\lceil\log_2 C_h(G)\rceil\) bits. At h>=8, the independent subsets form one class of size I(G;1), while every nonindependent support forms a singleton.

With N[W] the closed neighborhood of W, R26's exact independent-set fiber count gives the new feedback-visible residual
\[
C_8(G)-C_{26}(G)=
\sum_{\substack{\varnothing\ne W\subseteq V\\G[W]\text{ without isolated vertices}}}
\left(I(G[V\setminus N[W]];1)-1\right).
\]
This is a true initial-fiber count, not a statement that edge signatures suffice after arbitrary intermediate events.

**Strict refinement certificate:** C_8(G)>C_26(G) exactly when G contains an induced K2 disjoint union K1. If ab is an edge and k is adjacent to neither endpoint, the supports {a,b} and {a,b,k} are R26-equivalent but split at event eight. Conversely, if a nonempty active-edge signature has an extra invisible positive vertex k, it is outside the closed neighborhood of every active-edge endpoint; any active edge plus k supplies that induced triple. QED.

Examples: on four vertices, one edge and two isolated vertices has C26=2 and C8=5; P4 has 7 and 9; K4 has 12 and 12; star K1,3 has 8 and 8. P5 has 12 and 20.

## Evidence, source typing and open frontier

The executable \`x6_feedback_probe_brc_verify_r27.js\` independently implements exact Boolean-BRC recursive language signatures for each source/Port-labeled event. Direct JSON output \`x6_feedback_probe_brc_results_r27.json\` contains each graph's class counts and signature-state counts. Exhaustive graph coverage: all 75 labeled simple graphs on 1,2,3,4 vertices plus five five-vertex cases (empty, one edge, path, star, complete). All initial theta supports and horizons 0..8: 80 graphs, 11,322 initial state/horizon signatures, 93,573 pairwise comparisons and 835,485 memo states. All assertions PASS. Infinite-horizon claims use the proof, rather than extrapolation.

This quotient is strictly for the **initial common public fiber and successful-word observer**. An ongoing Markov realization must retain each B phase, return flags, consumed A/Q flags, global A activation and source-sensitive theta residual needed after Q activation. General state compression must be certified against its own future operations. Relative X6 Cell coordinates use an affine anchor, not an ontic origin; event count is separate from physical duration, precision level and any seventh spatial axis. No trig/pi, phase propagation or classical reference is used. Physical native TRIADIC_CLOSURE_E, Link feedback and irreversible Q admission remain unresolved.

**Next scientific step:** Obtain exact frozen-source native Cell/Link/Port and TRIADIC_CLOSURE_E legal event predicates; test whether they admit A-triggered source-sensitive probes under complete triadic carrier/provenance constraints. If not, formulate and verify the strongest admitted feedback rule and recompute the observer-safe quotient. Scientific lineage: EM-X6-214D9C; native PROGRESS and independent review are separate authority steps.
