# Stage428-B — Sharp asymmetric alignment corridor and linear information lower bound

2026-11-04. Research2 author-side research, UNREVIEWED / NOT_ADMITTED. Parent Stage427-B at c7256177a1ae9ac75abb591c7451c8b54feb4a19, Draft PR #1736. Frozen science pins: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavioral rules have been read separately.

## Scope, typed observer and Stage427 context

Work in the full chart-relative native X6 signed primitive alphabet D={+E1,-E1,...,+E6,-E6}; define A=+E1 and B=-E1. P,Q are ordered native-step words. The complete observer records both word lengths, both six-component signed endpoints, two full 12-by-12 directed adjacency inventories J_s(u,v), and absolute-position matching count K(P,Q)=sum_{i=1}^{min(|P|,|Q|)} [P_i=Q_i]. Operation executability is also observable. This is a discrete typed path model, neither an external Euclidean angle computation nor an assertion of physical heartbeat dynamics or final Cell addresses.

The Stage427 sufficient corridor has c_s=max(0,m_s-p_s), c=min(c_P,c_Q), H=min(m_P+a_P,m_Q+a_Q), and W=H-c<=max_s(a_s+p_s), with per-source cumulative append/delete budgets a_s,p_s. We address sharpness and information lower bounds, not a global minimum-state theorem for all operation languages.

## Theorem 428.1 — A two-index corridor is attained and exposes a hidden direction

For every integer n>=1 and L>=1, let

P=A^(n-1) · AAABA · A^L,  P'=A^(n-1) · ABAAA · A^L,  Q=A^n.

The initial pairs (P,Q) and (P',Q) have equal full observers, the same final L native labels in P/P', and length gap m_P-m_Q=4+L>=5. Use operation budgets (a_P,p_P,a_Q,p_Q)=(0,0,1,1), giving c_P=m_P, c_Q=n-1, H=n+1, and exactly W=2. A single legal independent Q-APPEND(A) produces

K(P,Q·A)=n+1,  K(P',Q·A)=n.

**Proof.** The blocks AAABA and ABAAA each start/end with A, contain exactly four A and one B, and have edge counts J(AA)=2, J(AB)=1, J(BA)=1, all other directed edge counts zero. Replacing one with the other does not alter junction edges, native endpoint, or full J. The two P words agree through position n, so the original K with Q=A^n is n. At position n+1 the words differ (A versus B); Q·A exposes that position. The corridor-width calculation above is exact. This shows the width upper bound is attained and an invisible direction can be future-relevant, not that both raw corridor labels are separately minimal. QED.

## Theorem 428.2 — Exponential full-observer fiber with linear information requirement

Let U_0=AAABA, U_1=ABAAA. For any b>=1, L>=1 and bit vector e=(e_1,...,e_b) in {0,1}^b define

P_e = U_(e_1) U_(e_2) ... U_(e_b) A^L; Q=A.

Take budgets (a_P,p_P,a_Q,p_Q)=(0,0,5b-1,0). All 2^b initial word pairs have *exactly the same full original observer*, including endpoints, lengths, all directed J entries and K=1. Moreover, under the single common legal continuation Q-APPEND(A) repeated 5b-1 times, the resulting K observation traces are all different. Thus any exact deterministic future-sufficient carrier refining that initial full observer must have at least 2^b distinguishable states in its fiber, equivalent to at least b bits in a fixed-length binary encoding. The Stage427 corridor width here is W=5b-1. Along this unbounded subsequence, required additional information is therefore at least (W+1)/5 bits. In particular, no universal o(W)-bit corridor replacement preserves this future observation language.

**Proof.** Every U block has exactly four A, one B, two AA, one AB and one BA directed edges. Each block begins/ends with A, so every inter-block edge and the edge connecting A^L are AA independent of e. The total endpoint, full J, length, common terminal suffix and K(P_e,A)=1 are independent of e. For any two distinct bit vectors let j be their first differing block. Their native words coincide at all positions before k=5(j-1)+2, but one has A and the other B at k. The common continuation Q=A^k is legal since k<=5b. All matching contributions before k coincide and the kth contributions differ, so the common observation traces differ. Hence the trace map is injective on 2^b histories. A carrier identifying two histories would give the same output trace for the same legal continuation, contradiction. Since c_P=5b+L, c_Q=1 and H=5b, W=5b-1. QED.

This is a BRC provenance/ordered-path residual statement: reducing a full history to current endpoint/J/K erases a branch degree of freedom that a legal future positional observer can recover. The construction uses only two of the 12 distinct typed native X6 directions but lives in the full six-axis carrier. This is not a dimensional reduction or a proof about the global native Cell dynamics.

## Proposition 428.3 — Constant-size boundary update for cached positional K

For a legal primitive word-end edit (P,Q)->(P*,Q*), set h=min(|P|,|Q|) and h*=min(|P*|,|Q*|). Because all such edits preserve the letters at every common unchanged absolute index, the exact increment is

K(P*,Q*)-K(P,Q)
= sum_{h<i<=h*} [P*_i=Q*_i] when h*>h;
= -sum_{h*<i<=h} [P_i=Q_i] when h*<h;
= 0 when h*=h.

For independent or paired one-letter APPEND/POP, |h*-h|<=1. For a legal two-letter paired CANCEL, |h*-h|<=2. With Stage427's bounded indexed alignment corridor, these equality queries are accessible, giving an at-most-two-comparison O(1) per-operation K update instead of O(W) re-summing. Updating a directed J table and six-component endpoint also uses constant local arithmetic per such primitive.

**Proof.** At every index i<=min(h,h*) both old and new path letters are unchanged. Their equality contributions cancel in the difference of K sums; only the newly covered or uncovered absolute indices remain. Corridor access and per-primitive length bounds yield the stated cost. QED.

**Cost semantics.** The O(1) figure is for one update on already built indexed stacks/maps, excluding required initial O(m_P+m_Q) input conversion. Full directed J has 12x12 slots per source, and the carrier needs O(12^2+W+sum_s(a_s+p_s)) slots plus constant native vector coordinates. Counter bit-length grows as O(log(m_P+m_Q+sum budgets)). This does not prove O(1) initial ingestion, whole Euler-family counting, address conversion, or state minimization.

## Exact executed checks and evidence scope

The companion Node.js source (standard library only) was run locally. It computes native signed six-component endpoints, full 12x12 directed J, and positional K with exact integers, and verifies:

1. Theorem 428.1 for every n=1..128 and L in {1,7,31}: 384 examples.
2. For b=1..10 and L in {1,3,7}, all 2^b histories per pair (b,L), 6,138 histories total, common full initial observation and distinct full K traces of the all-A append continuation.
3. Proposition 428.3 against direct recomputation for every pair of three-native-symbol words of lengths 0..4, 14,641 word pairs. All 12 primitive directions are used for independent and paired append options; legal single/paired POP and paired inverse-CANCEL are included: 2,503,804 transitions and 2,232,956 boundary-equality comparisons.

The actual local checker marker was STAGE428B_SHARP_CORRIDOR_ENTROPY_PASS. All finite checks completed without assertion failure. They corroborate the symbolically proved all-n, all-b and all-L statements but are not their substitute. The companion executed-evidence JSON records the actual observed totals. No independent native Driver assessment, formal task CLAIM, or canonical Source Result is claimed.

## Further research

Stage429-B: determine the exact future quotient of the narrow (a_Q,p_Q)=(1,1) asymmetric model (possibly one cross-source match bit plus the known K baseline, rather than two original raw labels). Integrate the at-most-two-comparison K updater with the Stage424 actual Euler/J transfer code, accounting for memoization and original input conversion. Independently prove or falsify the finite-sample Stage424 formulas S(n)=68n-463, T(n)=85n-628 by analyzing its actual pruning. Neither fit is promoted from finite evidence to a theorem. Preserve source pins and the separation between author-side proof and review/admission.
