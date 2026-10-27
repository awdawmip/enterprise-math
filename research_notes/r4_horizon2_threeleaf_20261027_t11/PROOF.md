# R4 / EC48J: three-leaf horizon-two likelihood-ratio memory obstruction

**Date:** 2026-10-27. **Contributor:** EM-R004-N2-20261027-1639-LOCAL (locally allocated; not a native session/owner). **Activity:** RA-EMR4-20261027-1639-T11-N2. **Status:** UNREVIEWED / NOT_ADMITTED; author-side proof and exact checks, no native CLAIM/Result/independent Driver acceptance.

**Fixed source pins:** GLOBAL_KNOWLEDGE_V1 main 9a98adbf15fe74f714c01dd2480595fe5e56d50a (P000 V4 and ACTIVE worldview included); Enterprise Math main c91d798c220e09147713a2cfb7c5947deb2adb60 (portable research and weighted BRC). Direct predecessor: eight-leaf horizon-three residual theorem, 9a5469f7d00779eede0530febacc5ccd7cb93c53, research_notes/r4_8leaf_one_bit_residual_20261027_t11/PROOF.md. This is a different, shorter-horizon question; no predecessor result is re-proved.

## 1. Typed model, observer, and future operations

This is **external auxiliary finite positive-mass BRC observer mathematics**, not native Heartbeat/X6, native BRC–Shor, a physical theorem, or a 3D-slice embedding. We use the existing explicit positive-rational branching carrier and observer/fiber discipline from definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json; the signed functional below is a *readout comparing separately accumulated positive P and Q masses*, not a signed primitive branch mass. The previous exact Bellman/occupancy method is reused (REUSE_APPLIED), without introducing a new general tool family.

At observation time 1, histories are A and B with common P,Q masses u and 1-u, 0<u<1. At time 2, A has two leaves A+ and A- with conditional probabilities P(+|A)=p and Q(+|A)=q, 0<q<p<1. B has one deterministic but positive terminal continuation B*. Ordered source masses are

P=(up,u(1-p),1-u),  Q=(uq,u(1-q),1-u).

All leaves have strictly positive P and Q mass. The two first-stage likelihood ratios coincide at L1=1. The three terminal likelihood ratios are p/q, (1-p)/(1-q), 1, all distinct.

A causal observer either stops and makes a binary decision D at time 1, or continues and must stop/decide at time 2. Every action can use fresh source-independent private randomization. Full observer F can use the complete observed history; L uses only (current time, current likelihood ratio) and fresh private randomness, with no retained history or public persistent seed; B1 additionally retains one writable bit after observing A versus B. For each class X, S_X denotes its **original (possibly nonconvex)** readout set:

O=(alpha,beta,tauP,tauQ)=(P[D=1],Q[D=1],E_P[T],E_Q[T]).

The observation horizon is exactly 2; later transitions, physical source dynamics and native geometry are outside the claim.

## 2. Global exact support theorem

Define delta=u(p-q)>0, c>0, and the signed linear observer

Jc(O)=alpha-beta-c(tauP+tauQ).

**Theorem 1 (all-real support identities).** For every real parameter tuple in the stated domain,

V_full = sup(S_F Jc) = -2c + max(0,delta-2cu),

V_LR = sup(S_L Jc) = -2c + max(0,delta-2c).

The exact gap G=V_full-V_LR is

G(c)=2c(1-u) if 0<c<=delta/2;
G(c)=delta-2cu if delta/2<=c<(p-q)/2;
G(c)=0 if c>=(p-q)/2.

Both middle expressions agree at delta/2. Hence G>0 **if and only if** 0<c<(p-q)/2. For fixed (u,p,q), the maximum gap over c>0 occurs at c=delta/2 and equals u(1-u)(p-q).

**Proof.** The mandatory time-1 observation contributes -2c. Because P=Q at both time-1 histories, stopping/accepting early contributes zero to alpha-beta. Continuing A until time 2 allows optimal acceptance of A+ and rejection of A-, gaining delta; source-wise survival mass u creates the extra combined stopping-time cost 2cu. Continuing B only pays an extra 2c(1-u)>0 and gains no discrimination. The full observer therefore stops B and selects whether to continue A: improvement max(0,delta-2cu). L sees the identical statistic (1,1) at both first-stage histories and must make the same policy choice at A and B. A deterministic L policy either stops both (improvement zero) or continues both (gain delta minus extra combined time cost 2c). The three terminal likelihood ratios identify which leaf is informative. A fresh-local-randomized policy is a mixture of deterministic choices for this *linear* support and cannot improve the optimum. This proves the formulas. Subtract and use delta/(2u)=(p-q)/2 to obtain the piecewise gap and unique maximizing switching cost. QED.

**Exact three-leaf witness.** Let u=1/2, p=3/4, q=1/4, c=1/8. Then

P=(3/8,1/8,1/2),  Q=(1/8,3/8,1/2),  delta=1/4.

The full-history policy “continue A; stop and reject B; at time 2 accept A+ only” has

O_full=(3/8,1/8,3/2,3/2),  Jc(O_full)=-1/8.

For L, “stop and reject both at t=1” and “continue both and accept A+ at t=2” both attain V_LR=-1/4; no L policy can exceed that by Theorem 1. The strict exact support separation is

V_full - V_LR = 1/8.

Thus even conv(S_L) differs from conv(S_F), and hence their original sets differ. The B* path is source-positive and has a real time cost if observed to t=2, despite being deterministic conditional on B.

## 3. Minimum terminal-leaf count

**Theorem 2.** No positive two-source horizon-two tree with one or two terminal leaves can separate S_F and S_L as four-dimensional readout sets. The three-leaf witness is therefore leaf-minimal **when deterministic terminal continuations are allowed**. Under the additional convention that *both* of two first-stage histories must each have at least two terminal descendants, the minimum is four leaves.

**Proof.** With one first-stage history there is no earlier history for L to forget. At terminal time, a full observer's randomized decision on each equal-ratio fiber can be averaged using Q-mass: P=rQ on that fiber, so the average matches both alpha and beta, while every terminal leaf incurs the same stopping time 2. Thus all four readouts are reproduced by L.

If there are two first-stage histories but at most two terminal leaves, each history has exactly one descendant, so its time-2 likelihood ratio is its time-1 ratio. If the two time-1 ratios differ, L distinguishes histories and exactly imitates F. If they coincide, normalization forces the common value to 1; consequently P=Q on the whole two-leaf tree. Any four-readout vector is then (a,a,t,t) with 0<=a<=1, 1<=t<=2. L achieves every such point by continuing at time 1 with probability t-1 and choosing acceptance probability a at either stopping time. Therefore S_L=S_F. One terminal leaf is trivial.

This proves lower bound three, attained above. If two genuine terminal descendants are required below both first-stage histories, four leaves are necessary by counting. Sufficiency follows by splitting B* into two positive source-identical terminal leaves, with conditional 1/2,1/2 under both sources: the Bellman identities and strict separation remain unchanged. QED.

## 4. Exact original-region repair by one bit

**Theorem 3.** In any finite positive two-source horizon-two model with **at most two observed first-stage histories**, a writable bit preserving the first-stage history and the current terminal likelihood ratio realize exactly the full-history readout set:

S_B1 = S_F,

not merely convex-hull equality. If the model has the strict witness of Theorem 1, an extra binary memory state is necessary relative to the zero-bit LR observer and sufficient for all four readouts; no persistent public seed is needed.

**Proof.** Let bit b identify the first-stage history h. Copy all full-policy time-1 stop/reject, stop/accept and continue probabilities conditional on h. For terminal time-2 histories z that are reached after h, group them by the exact joint likelihood ratio r=P(z)/Q(z). On a reachable fiber F(h,r), let s_h denote its source-independent time-1 survival factor and a_z the full-policy conditional terminal acceptance probability after any earlier private coins have been marginalized. Set the (h,r)-specific acceptance probability to

a_(h,r) = [sum_(z in F(h,r)) Q(z) s_h a_z] / [sum_(z in F(h,r)) Q(z) s_h].

A zero denominator means the fiber is unreachable and its kernel is arbitrary. This reproduces Q-acceptance mass exactly. Since P(z)=rQ(z) on the fiber, it simultaneously reproduces P-acceptance mass. Terminal times equal 2 throughout that fiber; source-wise time-1 continuation masses and early decisions were already copied. Both tauP and tauQ therefore agree, as do alpha and beta. A full observer can imitate B1, giving the converse inclusion. Marginalizing prior private coins is justified by the declared source-independent stochastic actions, which do not influence conditional future signal laws. This is observer equality, not pathwise reproduction of an identical hidden coin trace. Strict support separation rules out zero-bit L in the witness regime. QED.

## 5. Executed checks, limitations and next question

The reproducible Python Fraction script VERIFY.py exhaustively enumerates all 3^2*2^3=72 deterministic F policies and 3*2^3=24 deterministic L policies for the rational three-leaf witness, checking the exact optimal values and explicitly computed witness vector. On a declared grid of 425 distinct strictly positive rational models, it re-enumerates the same finite policy sets and checks the two symbolic formulas exactly; 235 parameter tuples have strict positive gaps. Results are saved to EXACT_OUTPUT.json. The script is an independent arithmetic check of a complete finite family; **the universal real-parameter claims come from the proofs above**, not from the grid.

The two-history one-bit theorem is observer- and horizon-specific. No assertion of sufficiency for three or more collided first-stage histories, arbitrary later operations, an actual native X6 six-axis model, physical residuals, or 3D-slice transfer is made. Transferring to the Heartbeat World would require typed source-state and native-path maps, declared third-slice-coordinate meaning, readout maps and proof of the preserved future operations.

**Next problem:** classify a minimum three-first-stage-history positive rational tree where one binary residual state cannot recover all four original readouts, or prove that one bit remains sufficient under an explicit source-neutral continuation profile restriction. Search separately for linear support gaps and for nonconvex region gaps; do not infer original-region equality from a support-zero search.
