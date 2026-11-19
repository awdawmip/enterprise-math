# X6 R29 — Frozen-guard feedback DAG: exact observer quotient, cumulative preparation depth, and a reset obstruction

Date: 2026-11-19 (Asia/Shanghai). Research Task: RS-X6-NATIVE-TIME-DYNAMICS / TP2-91D4A7C2F63805BE21A3. Research attribution: EM-X6-214D9C (original research lineage; privileged native PROGRESS requires separate current authorization). Evidence state: CONDITIONAL_AUTHOR_PROOF / EXACT_FINITE_BOOLEAN_BRC_PASS / NOT_INDEPENDENTLY_REVIEWED / NATIVE_TRIADIC_ADMISSION_OPEN.

## Scientific pins, ontology, and scope

Frozen P000 V5: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`. Original Taskbook: `awdawmip/enterprise-math@f41c2690daba467ecbde99615a1337e67be46ffd:research_tasks/RS_X6_NATIVE_TIME_DYNAMICS_20260906.md`. This extends the conditional R27 hyperguard arity result and R28 serial feedback relay result. The model preserves six native signed spatial axes, a chosen affine Cell anchor rather than an ontic global origin, intact three-quantum carriers, typed source and signed-Port labels, and event order as time. An auxiliary lane is not a claim that a two-dimensional native plane exists. The source-specific gate controls below are **explicit conditional hypotheses**; no native `TRIADIC_CLOSURE_E` admission or physical clock law is asserted.

## Controller family (all quantifiers explicit)

Let I={1,...,n} be a finite set of named sources, n>=0; let F be a finite DAG of m>=0 named, one-use gate events, with a fixed topological order. Each source B_i may perform exactly two independent preparation events `B_i+`, then `B_i-`, moving one intact triad one signed native-axis step to an adjacent Cell and back along its own disjoint lane. These two events mark its first return; a source's hidden bit theta_i in {0,1} remains unchanged. All sources have the same initially unprepared phase, independent of theta.

Each gate a in F has (i) a set of direct predecessor gate events P_a, (ii) a set R_a subseteq I of sources whose first returns must have completed, and (iii) a frozen hidden guard G_a subseteq I requiring theta_i=1 for every i in G_a. It executes once, under its own unique fully labelled event name `A_a+`, precisely when all three prerequisites hold. Gates do not change theta, source positions or phases, other guards, or already completed gates; they only set their own one-use completion flag. The observer sees the Boolean language L_h(S) of **successful, fully source/Port/gate-labelled words of length at most h**, including the empty word, from the common initial public state with S={i:theta_i=1}. It does not observe hidden bits or failed attempts. There are no other events in this theorem.

For any gate a let D(a) be its ancestor down-closure including a. Put

  U(a) = union_{b in D(a)} R_b,
  Q(a) = union_{b in D(a)} G_b,
  d(a) = 2 |U(a)| + |D(a)|,

and for h>=0 define the observable activated-gate set

  A_h(S) = {a in F : d(a)<=h and Q(a) subseteq S}.

Here d is an **event count**, not elapsed physical time. Shared prerequisites or shared source returns are counted once.

## Theorem R29.1 — Sharp first-exposure depth and exact Boolean-BRC initial quotient

For every finite DAG F, every source set I, every choice of R_a,G_a and every initial history S:

1. A successful word that contains gate label A_a+ exists iff Q(a) subseteq S.
2. When it exists, the shortest such word has **exactly** d(a) events.
3. For every h>=0 and all S,T subseteq I,

   `L_h(S)=L_h(T)  <=>  A_h(S)=A_h(T).`

4. Consequently the exact number of future-language equivalence classes on this common initial public fiber and its minimum fixed-length Boolean-BRC bits are

   `C_h = |{ A_h(S) : S subseteq I }|,`
   `b_h = ceil(log2 C_h)` (with C_h>=1).

These formulas apply to arbitrary branching and reconverging DAG prerequisites, and every finite or infinite future horizon. In particular L_h stabilizes as a classifier once h reaches `max_a d(a)`; for F empty there is just one class.

### Proof

A gate a cannot occur unless all gates in D(a) have occurred, because F is acyclic and every direct predecessor must be completed. Each b in D(a) requires every source in R_b to have returned, forcing two preparation events for every distinct i in U(a). Distinct labelled gate events in D(a) are one-use. Hence every successful word containing a has at least 2|U(a)|+|D(a)|=d(a) events; its guards entail Q(a) subseteq S. Conversely, if Q(a) subseteq S, first perform B_i+,B_i- for each i in U(a), then execute all gates in D(a) once in a topological order. Every gate guard, return requirement and predecessor condition holds, and this explicit word has length d(a). This proves statements 1 and 2.

If A_h(S) differs from A_h(T), choose a in the symmetric difference. By the exact witness above, one initial language has a word of length d(a)<=h containing A_a+, while the other has no successful word containing that label. Thus L_h differ.

Conversely suppose A_h(S)=A_h(T), and let w in L_h(S). Every gate a appearing in w has its entire ancestor closure present in w, so d(a)<=|w|<=h and Q(a) subseteq S. Thus a is in A_h(S)=A_h(T), and in particular its own guard G_a is true in T. All source preparation events, predecessor completion and unique-event conditions are independent of the hidden assignment. Induction through the labelled prefix of w shows the same word is successful under T; symmetry gives language equality. Finally A_h is an explicit sufficient-and-necessary equivalence invariant, so distinct values are precisely the minimum initial-fiber states and fixed-length bit count is ceil(log2 C_h). QED.

A useful point: this quotient minimizes the **initial history fiber**. Reachable intermediate Markov states also carry individual source phase/return flags and completed-gate flags. The theorem does not remove that dynamic state.

## R29.2 — Shared-preparation branching example

Take three sources B_0,B_1,B_2, and three gates A_0,A_1,A_2. A_0 has R_0=G_0={0,1}; A_1 has R_1=G_1={1,2}; A_2 has parents {A_0,A_1} with empty direct return and guard sets. The exact depths are

  d(A_0)=5, d(A_1)=5, d(A_2)=2*3+3=9.

The branch-and-join event is possible iff theta_0=theta_1=theta_2=1. Counting independent branch lengths as 5+5+1=11 would double-count B_1's return; the actual shortest witness has nine events. By depth 5 the active A_0/A_1 pair already classifies the four possible visible patterns {none,A_0,A_1,both}; A_2 at depth 9 adds no new initial history class even though it is a genuinely new event label.

The R27 no-feedback hyperguard model is the specialization with each gate having no predecessor and R_a=G_a=e: d(a)=2|e|+1. R28's serial trigger/relay/probe latency is obtained by taking a trigger gate with k required returned/positive trigger bits, q unconditional serial relay gates, and a final probe gate with one additional returned/positive probe bit: d(probe)=2(k+1)+(q+2)=2k+q+4. This is a comparison of **initial fiber quotients and shortest witness depths**; R28 allows further irrelevant independent lane repetitions.

## R29.3 — A one-reset counterexample to the frozen-guard shortcut

Take one source with theta=1. After B_0+,B_0-, gate A_0+ is allowed by the current Link bit x=1, and its execution irreversibly updates x:=0. Gate A_1+ requires A_0 to have executed and **current** x=1. In the frozen-guard DAG approximation (both gates guarded by the initial bit), A_1 is predicted at depth 2+2=4. In the actual mutable-guard system A_1 is unreachable at every finite depth: before A_0 it fails its predecessor; after A_0 it fails x=1. This is an explicit four-state-flag reachability obstruction, not an empirical extrapolation.

Thus the theorem's frozen-guard/no-feedback hypothesis is load-bearing. A native feedback model with Link updates must include the current guard-changing Link state in the transition semantics before applying a future-language quotient. For a finite such controller, exact partition refinement as in R21 is available; the closed-form D(a),Q(a) formula need not apply.

## Reproducible finite evidence

Companion exact checker `x6_frozen_guard_dag_brc_verify_r29.py`, result `x6_frozen_guard_dag_brc_results_r29.json`. Exhaustive domain: all 512 controllers with two returned sources and two ordered DAG gates (predecessor edge absent/present; all four source masks for each gate's returns and frozen hidden guard), each of four hidden histories, all observation horizons 0..6; 21,504 pairwise future-language equality checks, plus first-label depth assertions. A 3-source branching/joining controller checks the depths (5,5,9) and 280 additional initial-pair/horizon comparisons. The dynamic reset example is checked by explicit graph reachability. The finite checker uses only exact integers and sets of fully labelled successful words; it is not the universal proof.

## Next unresolved native step

Resolve the genuine, pinned `TRIADIC_CLOSURE_E` admissible whole-triad Cell/Link/Port update and its frame-dependent guard mutation, rather than postulating the feedback gate as a native law. A positive type- and provenance-preserving event-map would allow the R29 theorem on its corresponding frozen-guard subdomain; a mutable-link native gate instead requires the expanded Markov state and exact future-language recomputation. Also connect source/path event count to physical trajectory phase and precision-refinement clocks under the Taskbook's actual clock-separation acceptance criteria.

Attribution: conditional author result, not independent review or formal canonical Result admission.
