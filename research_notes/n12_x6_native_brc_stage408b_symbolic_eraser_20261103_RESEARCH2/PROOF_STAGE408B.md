# Stage408-B — Three-APP shielding, adaptive two-APP shielding and symbolic signed-axis templates

Date: 2026-11-03 (Asia/Shanghai). Research2 continuation from Stage407-B at `c6c23010e8d71557399c9281690ce383cf1abe14`, Draft PR #1736. Status: AUTHOR_PROVED / FINITE_CHECK_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Frozen science: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current behavioral rules were separately read from current global canonical main `d9008fb7358c749de88f80c5fc9901762766dbba` and EM main `621a2afb5a676bace3f83d79522ddb9158a762f0`. Neither P000 nor the ACTIVE worldview was changed.

## 1. Exact model and open mother question

The alphabet `D={+E_i,-E_i:1<=i<=6}` is the twelve signed directions of the native X6 space. Two finite ordered words P,Q start at equal length. An observer at each intermediate state returns (|P|,|Q|, six-axis endpoints, directed adjacency histograms J_P,J_Q, absolute-position coincidence K) and any endpoint-derived native BRC counts/positive weights and direction-local multiplicative factors already fixed in the Stage407 model. Here K(P,Q)=sum_{i<=min(|P|,|Q|)}[P_i=Q_i]. An action is paired APP(a,b), a Q-only POP, or a simultaneous CANCEL deleting the last two inverse letters of each word if enabled; POP and CANCEL have separate budgets <=1. Each operation's enabledness is observed. Because only Q can be popped, at all reachable states the length difference `Delta=|P|-|Q|` is in {0,1}. All words remain native X6 paths; restricting test examples to E1 is an embedded subfamily, not an independent lower-dimensional native world.

Two states with equal current observers are future-equivalent iff every common legal finite action trace has equal intermediate observers and enabledness. Stage407 proved that the distinguishing tests need no run of four consecutive APP and hence at most 11 total actions. This note improves that bound and supplies symbolic action alphabets.

## 2. APP probe lemma

**Lemma 408.1.** Let two reachable states have equal observers and Delta in {0,1}. If the first common APP(a,b) also yields equal observers, the old terminal P label and the old terminal Q label agree across the states wherever the corresponding old word is nonempty. All immediately subsequent APP-only observer comparisons agree for arbitrary common appended direction pairs.

**Proof.** The new J_P minus old J_P consists of the single edge (last(P),a) when P is nonempty, and analogously for Q. Equality of both old and new labelled histograms forces equality of each old terminal label (the appended label is identical on both sides). If an old word is empty, its length/empty boundary is shared. The first APP changes K by [a=b] when Delta=0; when Delta=1, the first new Q letter is compared with the old P terminal, now shown equal. Subsequent APP operations compare known appended letters at the same absolute indices and use identical terminal boundaries. Endpoints, J and direction-local multiplicative changes are deterministic under a common APP. No future APP-only step can create an observational discrepancy after that first successful probe. □

## 3. Three-APP shielding and the eight-action completeness theorem

**Lemma 408.2 (unconditional shielding).** Starting from any equal-observer pair of reachable states, suppose three consecutive common APP steps have equal intermediate observers. Then *all* future legal common traces with the remaining at-most-one POP_Q and at-most-one CANCEL have equal observer/enabledness traces, over the full twelve-direction alphabet.

**Proof.** Write the two old word lengths as n_P,n_Q, with Delta in {0,1}. The three APPs attach a common known suffix of three letters to each source. Every later CANCEL removes at most two suffix positions from P and Q; every later POP removes at most one further position from Q only. Hence throughout all future actions the original P word is never shortened and neither is the original Q word: P retains at least one of those three appended letters, Q retains at least zero. Further APPs only increase available appended letters. Consequently each current word is its entire old word plus an explicitly known prefix of the post-shield appended stream. In particular, no unknown old adjacency edge is removed.

By Lemma 408.1 the old terminal P and Q letters are equal across compared histories. The six-axis endpoints and each J are then computable from the common old observer, those terminals and the common still-attached appended strings. Enabledness depends only on the last two labels; if an appended string has length one or zero, the old terminal (and, only if the string is zero and a CANCEL could still occur, its penultimate letter) might appear. But a remaining CANCEL always has P with at least one post-shield appended letter. If Q has zero appended letters, all three Q-side destructive deletions have already been used; therefore no further CANCEL is possible. If Q has exactly one appended letter and a CANCEL remains, at most one Q-side deletion has happened (POP), so there are at least two appended Q letters before the CANCEL unless other additions happen; alternatively if Q has one after CANCEL, that CANCEL budget is spent. Thus a pending CANCEL never needs an unknown old Q penultimate; likewise P has an appended terminal with a pending CANCEL only after three APPs and before any CANCEL, so its last two labels are appended. This proves identical enabledness.

For K, the old shared overlap contributes the same K_old because neither original word was shortened. When Delta=0, all extra matched indices compare known appended letters; when Delta=1, only the first appended Q letter can overlap the old P terminal, identified by the probe, and all later matches use appended letters. Truncating appended suffixes does not change the original overlap. The same formulas handle zero-length old words. Direction-local products and endpoint-derived BRC readouts change by the same appended contributions. Induction over all further actions completes the claim. □

**Theorem 408.3 (improved complete test language).** To determine exact future equivalence it is enough to examine common legal action traces containing at most one POP, one CANCEL and **no three consecutive APP actions**. Such traces contain at most six APP operations and two destructive operations, hence at most **eight actions**, versus Stage407's bound of eleven.

**Proof.** Consider the first distinguishing prefix of an arbitrary trace. If it contained a three-APP run, its first APP could not distinguish by minimality, and Lemma 408.1 makes the second and third APP observationally identical; Lemma 408.2 makes every subsequent action identical, contradicting minimality. Thus a first distinguishing prefix cannot contain such a run. At most two destructive operations divide APP operations into at most three runs; each run has length at most two. This gives 3*2+2=8. The argument also covers enabledness mismatches. □

This is a uniform upper bound for the specified action language, not a claim that eight is shortest or that all paths can be stored in eight characters.

## 4. Adaptive two-APP shielding

**Lemma 408.4 (contextual shielding).** In Lemma 408.2's setting, assume additionally that the compared pre-APP states have identical suffixes of their last two original P labels and last two original Q labels (the whole word if shorter than two). After **two** common APP steps with matching observations, all subsequent allowed traces agree.

**Proof.** At most two P labels and three Q labels can be removed later. Thus P's old word is untouched, and at most the last one Q-old label can be removed. In that event, the only removed old Q adjacency edge is (penult(Q),last(Q)), identical by hypothesis, and the removed old Q endpoint increment is identical. Pending CANCEL legality is determined by known appended letters and at most those old last-two labels. If Q's last original label is removed, the old-overlap K decreases by its equality indicator with P at the same original index. Because Delta is 0 or 1, that P label is the old last or penultimate P label, respectively, both identical by hypothesis; any remaining cross-boundary K comparison likewise uses known appended tags and at most P's old terminal. With the old P intact and the potentially shortened Qold known at the boundary, the same induction as Lemma 408.2 applies. □

Thus a signature-compare engine can stop at two APPs when its current two-label suffix pairs match, and otherwise use the uniform three-APP rule. The check is on actual suffixes in the compared states and is not inferred merely from equal endpoints or J.

## 5. Native signed-axis symmetry: exact symbolic APP templates

For an initial comparison whose *entire* old histories use only A=+E1 and B=-E1, the signed permutations of axes 2..6 fixing E1 act on all subsequently appended directions while fixing the initial histories. Observer equality, enabledness, the inverse relation, and K equality are equivariant under this action. Therefore one representative per orbit of appended directions suffices for existence of a distinguishing trace (although its resulting *values* in labelled X6 coordinates are permuted). This uses a genuine group symmetry of the comparison, not a factorisation of independent sources.

Flatten r paired APP operations into 2r ordered slots. Canonicalise each new unsigned axis on its first appearance to the next fresh axis 2,3,... with positive sign; subsequent signs are recorded relative to that first occurrence. Existing axis E1 retains its sign. This gives exactly one canonical word per orbit of the group fixing E1.

Let F(k,t) count canonical continuations with k newly introduced axes among the five available and t unfilled slots. Then

F(k,0)=1,
F(k,t)=(2+2k)F(k,t-1) + [k<5]F(k+1,t-1).

The first term chooses either sign of the pinned axis or any previously introduced fresh axis; the second chooses the unique canonical positive sign of the next new axis. Consequently:
- 1 paired APP: raw 12^2=144, orbit representatives F(0,2)=11.
- 2 paired APPs: raw 12^4=20,736, orbit representatives F(0,4)=257.
- 3 paired APPs: raw 12^6=2,985,984, orbit representatives F(0,6)=10,298.

The two short counts are also checked by independent exhaustive enumeration of all raw ordered tuples. This orbit reduction applies to initial words fixed by that signed-permutation group. For broader old supports use the subgroup fixing **every** original label that matters (or test the particular candidate's equivariance); do not blindly reuse the numeric 11/257 counts. In mixed traces, retain the full chronological assignment of APP letters even after deletions: the group acts globally across all APP slots.

## 6. Reproducible finite cross-check

`REPRO_STAGE408B.py` and `REPRO_STAGE408B_EXECUTED.json` are a Python-standard-library exact-integer check. Two executions returned byte-identical JSON. The program compares the three-APP and four-APP reduced-trace enumerators on Stage407's complete six-step three-element fiber, checks 40 nontrivial distinct-member pairs among 301 observer fibers for all two-letter paired histories of initial length <=4, verifies two-APP contextual shielding in the first Stage407 pair, and independently checks orbit counts for one/two APPs. For the equivalent Stage407 pair the three-APP search visits 2,805 paired states (versus 86,273 for four-APP); the contextual two-APP search visits 168. All finite tests are scoped to the explicit two-letter sample; the 12-direction theorems are supported by the proofs above. No physical calibration or new BRC endpoint computation is claimed; Stage407's typed native BRC input/recurrence remains the inherited verified scientific front.

Exact stdout status: `STAGE408B_THREE_APP_SHIELD_FINITE_PASS`.

## 7. Next problem and authority

Stage409-B: combine the adaptive two-APP termination rule with an Euler/K feasibility oracle and orbit-canonical APP templates to compute the minimum quotient for a longer full observation fiber without enumerating complete word pairs. First implement the exact signed-axis-class dynamic canonicaliser; distinguish its proof-level orbit invariance from runtime feasibility; quantify pseudopolynomial histogram cost and integer-output sizes. The parent question remains the precise minimal sufficient memory for typed joint BRC observations with expanded asynchronous operations.

Project GitHub author-side storage does not grant CLAIM/Result/Driver acceptance. This run's native service `em_control_tasks` returned `CONTROL_QUOTA`; `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. The present result remains unreviewed and not admitted.