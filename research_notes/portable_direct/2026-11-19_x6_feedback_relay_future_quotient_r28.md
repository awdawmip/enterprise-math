# X6 R28 — Feedback relay destroys the static arity horizon; exact first-distinction and minimal future residual

Date: 2026-11-19 (Asia/Shanghai). Scope: RS-X6-NATIVE-TIME-DYNAMICS; publication TP2-91D4A7C2F63805BE21A3. Original scientific lineage EM-X6-214D9C, original owner/run to be checked separately for privileged publication. Status: CONDITIONAL_AUTHOR_PROOF / EXACT_FINITE_BOOLEAN_BRC_PASS / NOT_INDEPENDENTLY_REVIEWED / NATIVE_TRIADIC_ADMISSION_OPEN.

## Immutable science and audited starting point

Frozen P000 V5: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. Taskbook: awdawmip/enterprise-math@f41c2690daba467ecbde99615a1337e67be46ffd:research_tasks/RS_X6_NATIVE_TIME_DYNAMICS_20260906.md. Continuation: R26 pairwise Link quotient and R27 hyperguard arity filtration, both CONDITIONAL and without verified native TRIADIC_CLOSURE_E transition embedding.

P000 supplies six signed spatial Cell axes and time as event order, plus three-quantum primitive TRIADIC_CLOSURE_E; it does not prescribe the source-specific feedback rules introduced below. Every moving object here is an intact triad, and every move is one signed native-axis step. Other coordinates remain present and fixed; there is no primitive 2D plane, diagonal jump or seventh space axis.

## R28 controller family (precise hypotheses)

Choose k>=2 trigger sources, t>=1 probe sources and q>=0 relay consumers. Label the trigger indices 0,...,k-1 and probe indices k,...,k+t-1; their conserved hidden frame bits are theta_i in {0,1}. Each B_i occupies its own disjoint two-Cell lane of the X6 affine Cell torsor. It executes alternating successful B_i+ and B_i- signed Port moves, independent of theta_i. The first completed return records a typed returned bit; all later movements remain legal.

A separate one-use complete triadic consumer A+ moves only after ALL k trigger B_i have returned and ALL their theta_i equal 1. Its move sets an irreversible public-to-dynamics trigger-used bit. After A+, q further one-use intact consumers R_1+,...,R_q+ must move in that order (R_1+ is eligible after A+, R_{j+1}+ after R_j+); these relay guards are independent of hidden theta. If q=0 the chain is empty.

For every probe index j, a separate one-use complete-triad D_j+ action is eligible after the q-th relay (or A if q=0), B_j's first return, and theta_j=1. D_j+ does not change other sources, guards or consumers. All lanes are mutually disjoint. The sole observer is the Boolean set L_h(theta) of **successful, fully source-and-signed-Port-labelled** words of length <=h. Failed attempts, hidden frame bits and internal flag readouts are not directly observed. No event records physical elapsed duration. All rules are declared conditional controller gates; no native TRIADIC_CLOSURE_E admission is inferred from the geometric embedding.

Define g(theta)=prod_{i=0}^{k-1} theta_i (Boolean AND), and T(theta)={j in {k,...,k+t-1}:theta_j=1}. Define H=2k+q+4.

## Theorem R28.1 — Complete observer quotient and delayed residual

For all k>=2, t>=1, q>=0, and all hidden histories theta, eta:

1. If 0<=h<=2k, L_h(theta)=L_h(eta) for all theta,eta.
2. If 2k+1<=h<H, L_h(theta)=L_h(eta) iff g(theta)=g(eta).
3. If h>=H, L_h(theta)=L_h(eta) iff g(theta)=g(eta)=0, OR both have g=1 and T(theta)=T(eta).

Consequently the exact initial-fiber class count and minimal fixed-length Boolean-BRC storage are

  C_h = 1                          (h<=2k);
        2                          (2k+1<=h<H);
        1+2^t                      (h>=H).
  b_h = ceil(log2(C_h)).

For h>=H, the dark fiber g=0 has size (2^k-1)2^t, and each of the 2^t illuminated fibers has size one. The coordinate (g, g*T) is an exact minimal initial-fiber future-language coordinate for all horizons >=H; the bare g coordinate is insufficient there.

**Necessity / first distinguishing words.** The shortest successful word containing A+ has length 2k+1: every trigger B_i must first execute two native Port moves. It occurs iff g=1. Every D_j+ requires those 2k trigger movements, A+, q ordered R moves, B_j+ B_j-, and D_j+; therefore it occurs first at H=2k+q+4, and the word
  B_0+ B_0- ... B_(k-1)+ B_(k-1)- A+ R_1+ ... R_q+ B_j+ B_j- D_j+
is legal precisely when g=1 and j in T. No shorter successful word can mention a probe D, and no shorter word can mention A than 2k+1.

**Sufficiency / future safety.** B_i eligibility and relay ordering are independent of theta. Before A is possible, the only distinction that can affect a successful word is g, exposed at 2k+1; all relay actions require A. D actions cannot occur before H and, once possible, their eligibility depends only on g and the corresponding probe membership in T, plus explicit public returned/used/relay state. Starting from initial states with the same declared quotient, couple identical B phases, returned masks, A-used flag, relay depth and D-used masks. Every enabled labelled transition agrees and successor states remain coupled. When g=0, A/relay/D actions never occur, so all probe bits and individual inactive-trigger bits are permanently unobservable. When g=1, the full T set is retained. This yields identical full future word languages and a forward simulation preserving signed source/Port provenance, not merely equal counts or positive mass. Prefix-restricted versions give (1) and (2).

**Important state distinction.** The minimality claim is about the common *initial public fiber*. Intermediate reachable states additionally require B-phase, returned, trigger-used, relay counter and probe-used typed state. Global minimization of the entire dynamic controller is not asserted by this formula.

## Theorem R28.2 — No arity-only upper bound after feedback

Fix the trigger guard arity k=2 and a single probe t=1. For every nonnegative integer q, the three eventual future-language classes first separate into all three classes at the exact observation depth H=q+8. Thus increasing the number of serial one-use feedback relay consumers delays the final history distinction without increasing any conjunction's maximum guard arity (it stays at two for A and one for probes/relays). The terminal fixed-length historical residual is 2 bits, independently of q, while the exposure time is unbounded over this controller family.

This supplies a sharp counterexample to *extending* R27's static arity-only stabilization bound to feedback controllers. It does not refute R27 under its original non-feedback assumptions.

## Exact finite Boolean-BRC test

Companion verifier: x6_feedback_relay_brc_verify_r28.js. It constructs recursively interned deterministic tries for all successful fully labelled words at each horizon (the empty word is always present), compares exact language signatures against the predicted quotient for every initial theta, and checks all predicted class counts. Tested parameter triples:
  (k,t,q)=(2,1,0),(2,1,1),(2,1,2),(2,1,3),(2,2,0),(2,2,2),(3,1,0),(3,1,2).
For each, all horizons 0 through H+1 and all 2^(k+t) hidden histories pass; checked pairwise equivalence across all history pairs at each horizon. Memoized recurrence states and class counts are retained in x6_feedback_relay_brc_results_r28.json. Universal k,t,q results follow from the symbolic proof, not from finite extrapolation.

## Mother-objective relevance and next actual problem

The mother task asks for a minimal Markov time state preserving spatial Cell, frame, path origin, internal triadic relationships and clock separation. R28 isolates an exact conditional obstruction: the maximum guard arity alone does not bound future observation depth when one-use feedback and serial event provenance exist. R28 is not yet an authenticated native TRIADIC_CLOSURE_E event admission theorem. Next: extract the frozen genuine Cell/Link/Port transition rule and test whether a complete three-quantum triad can support the trigger/relay/probe guard morphism while preserving source, signed Port, full Link state, event order and provenance; if not, find the smallest admitted feedback gate and recompute its exact Boolean-BRC quotient. Separately test one feedback consumer that resets a prior Link flag, where the initial quotient and intermediate Markov repair may differ.
