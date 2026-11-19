# X6 R35 — Same triadic one-step admission, different feedback, different minimal historical state

Status: CONDITIONAL_AUTHOR_PROOF / EXACT_FINITE_CHECK_PASS / NOT_REVIEWED  
Date: 2026-11-20 (Asia/Shanghai)  
Task: RS-X6-NATIVE-TIME-DYNAMICS; original Researcher EM-X6-214D9C; Session MCP-d467c19ce42d4d7fa65a3901db1cf6b2.  
Frozen scientific pin: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json` (V5).  
Immediate frontier: R33 conditional pair-product divergence and R34 global Markov quotient, exact files in `research_notes/portable_direct/`.  
Source scope: P000 triadic balance definition `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md` and joint relation observer preservation (same frozen pin).  

## Question and exact conditional models

Does a P000-compatible *one-step* triadic event-admission certificate, even with all named source/Port event labels preserved, determine the whole-future minimal Boolean-BRC state? Answer: **no**. The missing datum is the event's Link/operational successor law.

Work at a chosen fixed Cell (c\in\mathbb Z^6) of the X6 affine Cell torsor; no global distinguished origin is claimed. Both events are assigned the same candidate closed three-nonzero-force witness type (\tau=(f_1,f_2,f_3)), with the canonical equal-quantum (\mathrm{PERP}_E) triad and `TRIADIC_CLOSURE_E=true` in the **candidate event typing**. Each event carries its own named source and signed Port identity; the Cell coordinate is unchanged, while used flags and public Link may change. This is a *syntactic possible dynamic completion* of the currently stated P000 arity/closure constraints. It is **not an established native event-admission theorem**: actual incidence, realization and all other native conditions remain to be checked.

Let (\theta_0,\theta_1\in\{0,1\}) be preserved hidden provenance bits, (u_0,u_1\in\{0,1\}) mark one-use events, and (x\in\{0,1\}) be public Link. The initial operational state is ((u_0,u_1,x)=(0,0,1)). There are only the fully named events (Q_0,Q_1).

In **both** models the exact current-state admission guards are:

\[
Q_0:\ u_0=0\land\theta_0=1;\qquad
Q_1:\ u_1=0\land(\theta_1=1\lor x=1).
\]

A successful (Q_i) sets (u_i=1) (other used bit unchanged). Successful (Q_1) leaves (x) unchanged. The sole difference is:

- Completion **A (RESET)**: successful (Q_0) also sets (x=0);
- Completion **B (INERT)**: successful (Q_0) leaves (x) unchanged.

The declared observer is the complete finite word of named, ordered successful event labels. It does not additionally read public (x) instantaneously; adding that observer can refine the equivalence classes. Event count is not identified with physical duration, periodic C6/C12 phase, or precision-refinement depth.

## Theorem R35.1 — One-step identical, future quotient different

For every hidden history (\theta), the two completions have identical initial successful event languages through depth (h=1), including exactly the same one-step admissible labels. However their initial-history future-language class counts are

\[
\boxed{C_h^A=(1,2,3),\qquad C_h^B=(1,2,2)\quad\text{for }h=0,1,\ge2.}
\]

More explicitly, histories are encoded (\theta=\theta_0+2\theta_1). In A, the unbounded-future classes are
\[
\boxed{\{0,2\},\ \{1\},\ \{3\}.}
\]
In B, they are
\[
\boxed{\{0,2\},\ \{1,3\}.}
\]
The minimum fixed-length initial-history encodings are respectively 2 bits (A) and 1 bit (B) at all depths (h\ge2).

**Proof.** When (\theta_0=0), only (Q_1) can occur, and it is always initially enabled because (x=1); all such histories have ({\epsilon,Q_1}) as their future language. When (\theta_0=1), both labels are initially enabled, and (Q_1Q_0) always succeeds. Under A, the word (Q_0Q_1) succeeds iff (\theta_1=1): after (Q_0) the Link becomes zero. Under B, (x=1) persists, so (Q_0Q_1) succeeds under both values of (\theta_1). The two probes are one-use, so all legal words have length at most two, establishing the entire future-language classification. This proves the formulas and shows that even **identical initial one-step event admission** cannot fix the future residual. QED.

## Theorem R35.2 — Distinct global Markov minima

Form the complete reachable decorated-state closure over all four histories and both event orders. There are 12 reachable states in each completion. Their complete residual successful-word languages form exactly

\[
\boxed{|Q_A/{\sim_\infty}|=5,\qquad |Q_B/{\sim_\infty}|=4.}
\]

Thus the optimal fixed-length *global* labelled Markov-state encoders require 3 bits in A and 2 bits in B. This differs from the respective initial-history-only encoders above.

**Proof.** Deterministic partial labelled-transition residual equality is a right congruence (R34), so the distinct residual successful-word sets yield the exact minimal global Markov quotient. Exhaustive reachable-state enumeration gives the counts in the attached verifier. Analytically, A has five distinct future languages:
({\epsilon}), ({\epsilon,Q_0}), ({\epsilon,Q_1}), ({\epsilon,Q_0,Q_1,Q_1Q_0}), and ({\epsilon,Q_0,Q_1,Q_0Q_1,Q_1Q_0}).
B has four:
({\epsilon}), ({\epsilon,Q_0}), ({\epsilon,Q_1}), and ({\epsilon,Q_0,Q_1,Q_0Q_1,Q_1Q_0}).
All reachable phases belong to one of these classes, and each class is realized. QED.

## Positive transfer criterion (R35.3, sufficient, not necessary)

Suppose a proposed native realization has a map (\iota) from all reachable conditional decorated states into admitted whole-triad native states, and an injective label map (\sigma) preserving signed Port and source identity. Assume for every conditional state (q) and declared label (a):

1. (a) is enabled at (q) iff (\sigma(a)) is enabled at (\iota(q));
2. when enabled, (\iota(T(q,a))=T_{\mathrm{native}}(\iota(q),\sigma(a)));
3. the declared native observation is exactly the restricted (\sigma(\Sigma))-word language (or any other native labels and independent state readouts are separately proved future-inert for the claimed full observer).

Then by induction on word length,
\[
\boxed{w\in L(q)\iff\sigma(w)\in L_{\mathrm{native}}(\iota(q))}
\]
for all finite words (w). Consequently the R33/R34 Boolean-BRC equivalence partitions transfer to the **declared restricted native observer**, for the represented states, without information loss. Forward simulation alone supplies at most one-way inclusion and is not such a certificate. The criterion does not assert that the required (\iota) has already been found.

## Exact evidence and research meaning

The accompanying self-contained JavaScript verifier enumerates all four hidden histories, all legal successful words (maximum length two), all 12 reachable decorated states in each completion and exact residual classes. It asserts the identical one-step observer, the first two-step distinguishing word, (C_h^A=(1,2,3)), (C_h^B=(1,2,2)), and global minima 5 and 4. There is no floating-point calculation; the universal claim here is only over the two fully defined finite completions. The preceding symbolic proofs settle those specific models independently.

**Result:** P000 fixes six-dimensional Cell typing, nonzero primitive stable arity three, and triadic closure, but leaves concrete Cell/Port/Link dynamics open. An arity/closure witness or agreement on one-step event labels cannot certify a native transition map or the global historical quotient. A source-preserving *successor* law and actual triadic event admission are the smallest unresolved bridge; replacing them by assumed correspondence would beg the question.

**Next discriminating work:** Read the exact native event-incidence implementation/accepted theorem at the task's frozen science pin if one is present; construct `TRIADIC_CLOSURE_E` whole-event `(Cell, force triple, rotation/frame, signed Port, Link, lineage) -> successor` and check all clauses of R35.3 for R33 and R34. If event admission cannot be established, retain both P000-compatible completions and the exact non-identifiability result. Separately study physical event count versus phase/refinement using the existing Viète C6/C12 clock split. Neither R35 completion is promoted to the native truth or independently reviewed.
