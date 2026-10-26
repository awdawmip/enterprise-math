# Exact root-stopping masking of nonlumpable LR states (N=2)

2026-10-26; AUTHOR-LEVEL mathematical proof. External strictly positive two-measure finite ordered tree only. Independent review, formal/native CLAIM, frozen Result, and any P000/X6/Heartbeat transfer: NOT ESTABLISHED. No claim of world-literature priority.

## Fixed source / actual authority

GLOBAL_KNOWLEDGE_V1 immutable read: awdawmip/chatgpt-global-knowledge@b496110a673fd7785d200b0d14d6b07611a09f07, with bootstrap, manual, current P000 (original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), active worldview and research/BRC policies. EM source read: awdawmip/enterprise-math@611e4903c3a9babc1237b74f0ed3d99df3f33ab0, portable protocol blob ca5de2d680d2439ff4b67c2c55fbd4159813cd5c. Predecessor: research_notes/brc_lr_minimal_horizon2_20261026_r5/PROOF_LR_MINIMAL_N2.md and NEXT_TASK_PACKET.md. It proved a compulsory-first-sampling iff and left arbitrary root stopping open. GitHub authenticated actor awdawmip, push allowed; native control_tasks returned CONTROL_QUOTA; session_start returned STATIC_READONLY_SCOPE_DENIED and operation_sent=false. Owner and native CLAIM cannot be verified; this is an independent author-source result, not adoption of a live claim.

BRC reuse: apply the labeled positive-rational branch masses, P/Q likelihood transport and observer-scoped quotient of definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json and prior finite LR occupation lemma. Resolution REUSE_APPLIED, no tool executable claimed. A signed difference of two positive occupancy flows is NOT a signed BRC amplitude.

## Model, observables and general criterion

At depth 0 (root), a stopping/decision action is allowed. At depth 1 observe h from finite H, under both laws with P(h)=Q(h)=q_h>0 and sum q_h=1. Conditional depth-2 raw branches all have strictly positive P/Q probabilities, and terminal exact LR r=P(h,y)/Q(h,y). T_0=root, T_1=1 and T_2=r. Every policy may stop-P, stop-Q or continue when depth<2, and must decide at depth2. Its common randomization is hypothesis-independent.

The four observables are O(pi)=(P_pi[decide Q], Q_pi[decide P], E_P tau, E_Q tau)=(eP,eQ,tP,tQ). Universal 4-scalar sufficiency means FOR ALL full ordered-history randomized policies pi THERE EXISTS a time/exact-LR-only randomized behavioral beta with identical O. It does not promise fine occupancy, provenance, hidden-history interventions, or future-port equivalence.

For each theta>0 define
D_h(theta)=min(1,theta)-E_Q[min(LR_2,theta)|h] >=0,
d_min(theta)=min_h D_h(theta), and dbar(theta)=sum_h q_h D_h(theta).
The inequality is Jensen: E_Q[LR_2|h]=1.

**Theorem (root-masking iff).** In the stated finite strictly positive depth-two model with P(h)=Q(h), universal four-scalar LR sufficiency including root stopping holds IF AND ONLY IF

$$ \forall\theta>0:\quad \bar D(\theta)\le 2d_{\min}(\theta). \tag{RM} $$

**Proof of exact support criterion.** For arbitrary real coefficients A,B,C,D, minimize J=A eP+B eQ+C tP+D tQ. Every policy satisfies tP=tQ, so set gamma=C+D. Define H(r)=min(A*r,B), m=H(1), F_h=E_Q[H(LR_2)|h], d_h=m-F_h>=0 and dbar=sum q_h d_h. Bellman minimization INCLUDING root stop and mandatory termination at depth2 yields

$$ \inf_{\rm full}J=m+\min(0,\gamma-\sum_hq_h(d_h-\gamma)_+), $$
$$ \inf_{\rm LR}J=m+\min(0,\gamma-(\bar d-\gamma)_+). \tag{1} $$

Indeed at depth1 stop costs m, continue costs gamma+F_h; at root stop costs m, continue costs gamma plus the depth1 expected minimum. For LR policies the first-level action is common across h, and terminal LR-class decisions minimize H(r), giving Fbar=sum q_h F_h. These formulas handle all signed coefficients, root/terminal cases and randomization (linear extrema have deterministic optimizers).

If A,B have opposite signs or either is zero, H is affine on r>0 and all d_h=0. For A,B>0, put theta=B/A, then d_h=A D_h(theta). For A,B<0, set a=-A,b=-B>0 and use min(-a*r,-b)=min(a*r,b)-a*r-b; the affine correction cancels under E_Q[LR_2|h]=1, hence d_h=a D_h(b/a). Thus (RM) for positive theta is exactly the required criterion for ALL real linear costs.

Fix one H and d_* = min d_h, d^*=max d_h. If gamma<=d_*, both positive-part sums equal dbar-gamma, and (1) agrees. If gamma>=d^*, gamma>=0 and both are the root-stop value m. On d_*<gamma<d^*, write S(gamma)=sum q_h(d_h-gamma)_+. This is nonincreasing. If dbar<=2d_*, then S(gamma)<=S(d_*)=dbar-d_*<=d_*<=gamma: again both are m. Conversely, if dbar>2d_*, then S(d_*)>d_*; with all q_h>0 choose gamma strictly above d_* but below d^* so that S(gamma)>gamma. Because some d_h<gamma and some >gamma, strict convexity of the hinge across the split gives S(gamma)>(dbar-gamma)_+. The full optimum in (1) is strictly smaller than the LR optimum. A=1,B=theta and C=gamma,D=0 provide an actual separating linear functional whenever (RM) fails. This proves iff for equality of ALL linear support minima.

**Why support equality implies policy-by-policy matching.** The LR-only attainable set is a compact convex polytope, not merely an arbitrary nonlinear collection. Let x0P,x0Q,s>=0 with x0P+x0Q+s=1 be root action masses. Let x1P,x1Q,c>=0 with x1P+x1Q+c=s be unconditional depth1 action masses at its sole LR=1 state. Define qbar(r)=sum_h q_h Q(LR_2=r|h), and terminal Q-decision Q mass z_r in [0,c*qbar(r)]. Then

$$ e_P=x0Q+x1Q+\sum_r r z_r,\quad
e_Q=x0P+x1P+\sum_r(c\,qbar(r)-z_r),\quad
t_P=t_Q=s+c. \tag{2} $$

All constraints and observers are linear; every feasible flow is implemented by legal conditional LR policy probabilities (choose arbitrary decisions on unreachable states). Hence the LR observer set is nonempty compact convex. It lies inside the full-history set. If any full-history observer vector were outside it, strict finite-dimensional separation would yield a linear J contradicting the equality of all infima. Conversely, if (RM) fails, (1) supplies an explicit separating J. QED.

## Exact positive-rational LR-minimal nonlumpable example

Depth1 P(a)=Q(a)=P(b)=Q(b)=1/2; depth2 LR values r=(1/2,1,3/2). Conditional rows in that LR order:

| h | Q(r=1/2) | Q(r=1) | Q(r=3/2) | P(r=1/2) | P(r=1) | P(r=3/2) |
|---|---:|---:|---:|---:|---:|---:|
| a | 1/4 | 1/2 | 1/4 | 1/8 | 1/2 | 3/8 |
| b | 1/3 | 1/3 | 1/3 | 1/6 | 1/3 | 1/2 |

All rows are positive, normalized, non-iid, and P(h,y)/Q(h,y)=r. Both terminal and first statistics ARE EXACT LR, no redundant T-label. Strong P/Q lumpability fails (conditional probability of r=1/2 is 1/4 vs 1/3 under Q, 1/8 vs 1/6 under P).

Let a_a=1/4, a_b=1/3. Write G(theta)=2min(1,theta)-min(1/2,theta)-min(3/2,theta)>=0 by concavity. D_h(theta)=a_h G(theta). G is zero outside (1/2,3/2), equals theta-1/2 on [1/2,1] and 3/2-theta on [1,3/2]. Hence
d_min=G/4 and dbar=(G/4+G/3)/2=7G/24 <= G/2=2d_min, for every positive theta. (RM) proves universal four-scalar LR sufficiency despite nonlumpability, resolving the prior root-stopping necessity question by a strictly positive rational counterexample.

One full-history witness: root continue, after a continue, after b stop and decide P, and at depth2 decide Q only for r=1/2. Then O=(1/16,7/8,3/2,3/2). LR-policy: root continue, at T1=1 stop-P with probability 1/2 or continue with probability 1/2, then at r=1/2 decide Q with probability 6/7 (otherwise P), and at r in {1,3/2} decide P. The same O follows by direct fractions. The ORIGINAL MINUS LR policy incoming terminal Q flow over the three LR classes is (-1/48,1/24,-1/48), nonzero; both its sum and LR-weighted sum are zero. These are signed DIFFERENCES, not cancellation of positive BRC weights. Scalar sufficiency is not occupancy/future-port sufficiency.

## Independent exact finite certificate and bounds

Actually executed standard-library Fraction verifier: VERIFY_PORTABLE.py (also a more verbose local author checker). It enumerates 3*3^2*2^6=1728 full deterministic strategy tables, yielding 85 distinct observer triples (eP,eQ,t=tP=tQ), and 3*3*2^3=72 LR deterministic tables with 12 distinct triples. All coordinates multiplied by 48 are integers. It enumerates every triple-defined supporting plane of the full-dimensional LR hull and obtains seven facets, which in unscaled coordinates are

$$1\le 2e_P+e_Q\le2,\qquad 2\le 2e_P+3e_Q\le3,$$
$$1-\frac7{96}t\le e_P+e_Q\le1+\frac7{96}t,\qquad t\le2.$$

All 85 full-history distinct points satisfy each facet EXACTLY. Root and first actions are included. The two sum inequalities also imply t>=0. The LR occupancy polytope (2) gives the convexity needed to lift the finite containment to every randomized full-history policy; enumeration alone without that argument is not the claimed universal proof. An extra grid of 625 signed linear cost quadruples is a cross-check, not proof of real-coefficient universality.

Scope: external finite rational tree, author algebraic proof plus exact finite exhaustive check; no formal checker/independent Driver review/source-native Result or native P000/X6 theorem. All state/provenance/observer loss limitations are preserved.

**Next:** test non-unit first LR class root-robust necessity and mixed-class classification (see NEXT_TASK_PACKET.md).
