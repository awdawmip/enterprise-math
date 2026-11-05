# R5 — Exact finite-tag Bellman deficit as a directed minimum cut

Date: 2026-11-05 (Asia/Shanghai). AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Frozen scientific scope and predecessor

R5 mother question: in a strictly positive finite P/Q stopping BRC, can FULL_HIST and seedless LR have the **same complete four-observer convex hull** but **different actual real-behavior observation sets**? O4=(P[declare Q],Q[declare P],E_P[tau],E_Q[tau]). The present theorem treats a finite history-tag Bellman reduction at **one fixed support direction**; it neither answers nor changes the mother question.

Frozen inputs stay GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. Scientific predecessor: EM immutable 5cd25d2a531c69550c71a5e0055149975d983225, research_notes/brc_r5_finite_tag_overlap_20261105_emr5/RESEARCH.md, which derived the exact finite-selector deficit and overlap lower bound. Related positive BRC model-S inputs: a737b271c871375d90b8bf06e0e63469526fbfed. Current behavioral norms were separately consulted and do not re-pin the scientific evidence.

BRC carrier is positive P/Q branch mass with labeled incoming histories i, stochastic label T(y|i), and downstream stop/continue. The observer drops some history identity; this quotient is not assumed compatible with future decisions.

## Exact theorem — directed s–t min-cut

At a **globally valid** four-observer support-function Bellman reduction, assume:

J = C + sum_i w_i a_i (A_i + u_i z_i)

Here finite m, w_i>0, independently controllable upstream a_i in [0,1], and FULL_HIST downstream z_i in [0,1]. A tag y in finite Y has conditional row-stochastic T(y|i)>=0, independent of upstream randomization given i and with the same conditional distribution under P and Q, so it does not itself change likelihood ratios. Tagged policy chooses only z_y per y, inducing t_i = sum_y T(y|i) z_y. The coefficient reduction must already include optimization over *other* admissible stopping and declaration alternatives.

Define I_-={i:A_i>0 and u_i<0}, I_+={j:A_j+u_j>0 and u_j>0}. Create vertices s,t, an i-node for each I_-, one y-node per tag symbol, and a j-node for each I_+. Directed arcs and capacities:

* s -> i: w_i A_i for i in I_-.
* i -> y: w_i (-u_i) T(y|i) for i in I_-.
* y -> j: w_j u_j T(y|j) for j in I_+.
* j -> t: w_j (A_j+u_j) for j in I_+.

All capacities are nonnegative. Then

**D(n)=h_FULL_HIST(n)-h_TAG(n)=minimum s–t cut capacity=maximum s–t flow value.**

If coefficients are rational, D is exact rational. Graph has at most m+|Y|+2 vertices and m(|Y|+1) arcs. A minimum cut recovers a maximizing binary tagged rule: z_y=1 if y lies on the sink side; z_y=0 if y lies on the source side. This computes D without 2^|Y| enumeration using rational max-flow/min-cut. Complexity excludes the potentially difficult prior problem of deriving globally valid Bellman cells and full four-observer cone coverage.

### Proof

The verified predecessor's finite-selector formula reads

D=min_{S subset Y} sum_i w_i [M_i - (A_i+u_i T(S|i))_+],
M_i=max(0,A_i,A_i+u_i), T(S|i)=sum_{y in S}T(y|i).

For i in I_-, the summand becomes w_i min(A_i,(-u_i)T(S|i)). For j in I_+ it becomes w_j min(A_j+u_j,u_j(1-T(S|j))). Every inactive history contributes zero. Fix the tag partition: y in S on the **sink side**, all other y on the source side. A stop-history i placed on the sink side cuts only s->i (w_i A_i); if instead placed on source side, it cuts i->y for y in S (w_i(-u_i)T(S|i)). The cheaper choice is exactly the first min. A continue-history j on source side cuts j->t (w_j(A_j+u_j)); on sink side it cuts y->j for y not in S (w_j u_j(1-T(S|j))). The cheaper choice is exactly the second min. For fixed tag sides all history vertices can be optimized independently; minimizing over S yields the desired deficit. The standard max-flow/min-cut equality completes proof.

The construction is a standard flow reduction (not a priority/novelty claim about max-flow itself). It also recovers the prior zero-loss test: there is a zero-capacity cut iff the tag supports of active stopping and active continuing histories are disjoint. Positive overlap implies strict separation for that *valid* direction. The earlier inexpensive bound B=sum_y min(b_-(y),b_+(y)) satisfies B<=D but need not equal D: the flow solution enforces that each incoming history has one shared upstream decision.

### Exact run and numerical scope

The accompanying VERIFY.py (Python fractions.Fraction; source test run locally on 2026-11-05) builds the above graph, runs exact Edmonds–Karp with residual BFS, obtains the cut and tag policy, and independently compares all 2^|Y| binary policies in small instances. It checks model-S conditional Bellman coefficients across five binary tag noise levels, predecessor's ternary three-history example, and 512 seeded rational finite gate instances (1<=m,|Y|<=6, including neutral histories and zero channel weights). Every case passes exact equality with the enumerated deficit and the prior overlap lower bound. See EXACT_OUTPUT.txt.

Model S: w=(1/2,1/2), A=(1/200,-47/400), u=(-9/500,49/400), T rows (1-eta,eta),(eta,1-eta). Exact D(eta)=min(281*eta/4000,1/400); B=eta/200. For eta=0, D=0; eta=10/281, D=1/400; eta=1/2, D=B=1/400. Three-history positive ternary tag gives D=1/21, B=9/280. The 512 random rational checks yielded 200 with conflicting supports and 200 positive deficits. Finite tests do not establish the general theorem; the analytic cut construction does. No new full P/Q model-S tree was run, and the predecessor's complete-model evidence is reused rather than silently re-executed. No Lean proof or independent reviewer acceptance is claimed.

## Consequences and continuation

The exact computational benefit is **for an already certified direction's finite history-tag Bellman problem**, not a general faster solver for arbitrary four-dimensional BRC or the full R5 mother objective. Build cost O(m|Y|) rational capacities, plus max-flow arithmetic/bit costs, plus source Bellman/observer derivation. If an explicit FULL_HIST maximizing W and nonzero n are separately established, D>0 implies dist_infinity(W,conv O4(TAG)) >= D/||n||_1. No new numeric distance claimed here.

Reuse: REUSE_APPLIED predecessor exact finite-tag deficit and BRC provenance typing. Scoped GitHub code search for mincut/max_flow/Edmonds/submodular had no matches; not proof the repository lacks all general flows or that this is globally new machinery. Algorithmic standard method is rational max-flow/min-cut.

Next discriminating action: select a fully specified strictly positive finite P/Q nonterminal merger; derive and certify each global four-observer Bellman sign cone including stop and all terminal declaration alternatives; apply min-cut at rational cone witnesses/boundaries. A strict D(n)>0 is a convex-hull separation certificate; proving all cones D=0 is only a hull-equality step, to be followed by a separate actual-behavior image/nonmembership argument. R5 parent remains OPEN.
