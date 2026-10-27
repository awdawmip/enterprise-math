# R5 — Complete one-price test for the two-level BRC Jensen obstruction

Date: 2026-10-27, author-side portable research. Status: AUTHOR_PROVED / EXACT_FINITE_CROSSCHECK / UNREVIEWED / NOT_ADMITTED. This is a finite external two-measure observation model, not native X6 physical dynamics, a native Task Result, or independent mathematical admission.

Source pins: GLOBAL_KNOWLEDGE_V1 main@138a017a98649b4a7d16ddbff1cc0dfa13028cfb (both entries, P000 V4/projection matching Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview, TASK/code/math routes); initial Enterprise Math read main@b637846961841e3ea2110f6ee077fd4fe17e3850 (portable/autonomous and current control). Earlier exact source: research_notes/brc_r5_16leaf_jensen_hull_gate_20261027/PROOF.md (the general Bellman formula and a first-level unequal-group-mean Jensen gap). This study completes an all-price equivalence not established by its conditional group-mean criterion.

## 1. Model and exact claims

Fix a finite three-decision-stage P/Q observation tree. Time 1 reveals group g with Q=P probability p_g>0 (sum_g p_g=1); time 2 reveals within-group label j with conditional Q=P probability q_gj>0 (sum_j q_gj=1). Thus all nonterminal histories have likelihood ratio 1. Time 3 reveals a positive terminal likelihood ratio Y with conditional strictly positive Q kernel K_gj(y) on a finite common support, satisfying sum_y K_gj(y)=sum_y y K_gj(y)=1. Complete-history policies may use g and j; seedless LR policies may use only (t,R_t). At stopping declare P or Q; do not carry a shared random seed. Observe O=(P(D=Q),Q(D=P),E_P tau,E_Q tau). For each real s>=0 minimize J_s=O_1+O_2+s O_4.

Define terminal Bayes gain G_gj=1-sum_y K_gj(y)min(y,1)>=0, group mean M_g=sum_j q_gj G_gj, and overall mean M=sum_g p_g M_g.

**Theorem (complete single critical-price gate).** For every real s>=0,

  V_full(s)=1+s-sum_g p_g [sum_j q_gj (G_gj-s)_+ -s]_+ ,
  V_LR(s)=1+s-(M-2s)_+ .                                      (1)

In particular, with s*=M/2,

  Delta(s*)=V_LR(s*)-V_full(s*)
    =sum_g p_g [(M_g-M)+sum_j q_gj(s*-G_gj)_+]_+.              (2)

The following three conditions are EQUIVALENT:

  (a) V_full(s)=V_LR(s) for every real s>=0;
  (b) V_full(M/2)=V_LR(M/2);
  (c) M_g=M for every g, and G_gj>=M/2 for every g,j.         (3)

This gives a complete rational single-price screening oracle for this one-dimensional objective family. It does not decide equality in every signed four-dimensional direction.

## 2. Proof valid for every real stopping randomization

For terminal Y=y, Q-cost of declaring Q is y and of declaring P is 1. The optimal terminal conditional error cost is min(y,1). At time 2, stopping cost is 1+2s, while continuing to time 3 incurs 1-G_gj+3s. Its maximal improvement relative to stopping is (G_gj-s)_+. At time 1 group g, an additional stage costs s; expected maximal time-2 improvement is sum_j q_gj(G_gj-s)_+. Thus the time-1 improvement is its difference from s clipped at zero. Summing by p_g proves V_full in (1). An LR policy sees the same ratio 1 at all time-1 groups and all time-2 labels, so it has one average gain M and time-1 improvement (M-2s)_+ for s>=0, proving V_LR. Bellman minimization is affine in each local real action probability; hence deterministic decisions attain the minima for the entire [0,1] randomization domain.

At s*=M/2, the LR gain vanishes. The exact identity
  sum_j q_gj(G_gj-s)_+ = M_g-s+sum_j q_gj(s-G_gj)_+
proves (2). Since all p_g>0, Delta(s*)=0 iff each bracket in the original full-gain formula is <=0. Jensen gives sum_j q_gj(G_gj-s*)_+ >= M_g-s*, so every g must have M_g<=2s*=M. Their strictly positive weighted average is M, so all M_g=M. Then
  sum_j q_gj(G_gj-s*)_+=s*+sum_j q_gj(s*-G_gj)_+.
The desired <=s* is equivalent to every G_gj>=s*, since q_gj>0. Thus (b) implies (c). Conversely, under (c), if s<=s* every child satisfies G_gj>=s and the group improvement is (M-2s)_+. For s>=s*, sum_j q_gj(G_gj-s)_+-s is nonincreasing in s and equals zero at s*, so every group improvement vanishes just as (M-2s)_+ does. This proves (c) implies (a); (a) implies (b) is immediate. The same argument includes M=0. QED.

**Interpretation.** Equality of group-averaged Bayes gains is necessary but not sufficient. Even when every M_g is exactly equal, a child gain below M/2 produces an all-real-strategy strict support separation. At equal means, (2) simplifies to Delta(s*)=sum_g p_g sum_j q_gj(s*-G_gj)_+.

## 3. New exact 16-leaf counterexample to the mean-only screen

Let terminal Y=(1/10,99/100,101/100,19/10) and K(p)=(p,1/2-p,1/2-p,p), all 0<p<1/2. Every K(p) is strictly positive, has unit mass and mean Y equal to 1. Its exact gain is G(p)=1/200+(89/100)p.

Take two equiprobable groups A,B, two equiprobable time-2 children each, and
  p_A0=1/100, p_A1=49/100, p_B0=p_B1=1/4.
Then Q(g,j,k)=K(p_gj)_k/4 and P(g,j,k)=Y_k Q(g,j,k). All 16 P/Q leaf masses are strictly positive and each measure has total mass one. Exact gains are
  (G_A0,G_A1,G_B0,G_B1)=(139/10000,4411/10000,91/400,91/400).
Both group means equal M_A=M_B=M=91/400. However G_A0=139/10000<M/2=91/800.

At s*=91/800, equation (2) gives the new strict gap
  V_full=87103/80000,  V_LR=89100/80000,
  Delta=1997/80000 >0.                                    (4)

One realizing full policy continues group A at time 1 and stops B (declare P); at time 2 it stops A0 (declare P) and continues A1; at time 3 it declares Q for Y<1 and P for Y>1. Its exact observer is
  O_full=(589/40000,7/8,7/4,7/4).
The LR policy stopping and declaring P at time 1 gives V_LR=1+s*=891/800; equation (1) proves no seedless LR policy with arbitrary real local randomization can do better. Hence this candidate fails full-versus-LR support-hull equality despite perfect matching of every time-1 group mean. This corrects the overly weak mean-only filter without contradicting the predecessor's conditional theorem.

If desired, each synthetic leaf can be labeled by distinct ordered native X6 Cell paths with g selecting e1/e2, j selecting e3/e4, k selecting e5/-e5/e6/-e6. Those are static path/provenance tags in six axes, not a heartbeat transition law, a two-dimensional native plane, or a proof of native physical correspondence. Time is separate.

## 4. Validation and scientific boundary

The adjacent exact Python Fraction verifier constructs all sixteen positive leaf Q/P masses, checks both normalizations and all conditional ratio means, validates (4) and the full witness, and exhaustively checks 3^6=729 complete-history versus 3^2=9 seedless-LR early deterministic decision tables at eight declared rational prices. Time-3 declaration is optimized analytically by min(Y,1), so its omission from enumeration does not affect J_s minima. Adjacent EXACT_OUTPUT.txt is the literal program output ending ALL EXACT CHECKS PASSED. Universal all-real statements (1)-(3) follow the displayed Bellman/Jensen argument, not the eight computational probes. Not Lean-checked or independently reviewed.

BRC reuse classification: REUSE_APPLIED to positive Q/P branch weights and typed P/Q ratio transport, and COMPOSE_APPLIED to the prior two-level Bellman/Jensen calculation. Signed gaps are observer differences rather than positive branch masses. The current external tree does not establish full P000 X6 dynamics or a new native world axiom.

Next research: impose all group gains M_g=M and every child gain G_gj>=M/2, thereby passing this entire s>=0 family; then test OTHER signed four-dimensional directions using exact hull separation before real-image feasibility. Under the present all-prefix-LR-one topology, weak signature-kernel invariance is vacuously satisfied and LR image is convex (previously known); thus this topology by itself cannot be the target equal-hull/unequal-image witness. The next candidate must introduce nontrivial LR-signature merging at intermediate time or otherwise defeat the known sufficient convexity condition.
