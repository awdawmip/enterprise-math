# BRC N=4 S23 — Fisher-equal price Chernoff-efficiency reversal

Date: 2026-11-03. Status: AUTHOR_ANALYTIC_PROOF / BIGINT_EXACT_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED. This is an author-side independent, unclaimed scientific continuation, not a native task Result or review.

## Pinned scope and question

Frozen science input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Predecessor: PR #1765 @ 670015d35488f2995405339da1527462161f70d2, research_notes/brc_n4_s23_chernoff_asymptotic_cost_20261103_research1/PROOF.md. Reuse the same lawful two-state witness, scheme (3,31), deleted source row 0, retained E row 1 full-source trial T and Bernoulli E row 0 event-2 repair B. Preserve independent conditional trials, source/branch tags, equal prior hypothesis testing, nonadaptive allocations and stipulated abstract costs. Set 0<h<=1/42, s=(1-beta_E)^2 in (0,1], p=1/2+h, q=1/2-h and beta_N=0.

T has distributions (sp,1-s,sq) versus (sq,1-s,sp). B has Bernoulli success probabilities sp and sq. Define Chernoff information C_X=-ln(min_{0<=t<=1} Z_X(t)), where Z_X(t)=sum_v P_+(v)^t P_-(v)^(1-t). Cost T is c_T=2-s, and cost B is 1: the two have equal local Fisher information per cost at h=0, since I_T(0)=4s and I_B(0)=4s/(2-s). The question is whether this equality orders their positive-h Chernoff efficiencies uniformly as s varies.

## Theorem 1: exact fourth-order phase change

For every fixed s in (0,1), as h tends to 0 through positive values,

C_T/(2-s)-C_B =
-2s(1-s)(9s^2-40s+4) / [9(2-s)^3] * h^4 + O_s(h^6).

Let s_*=(20-2 sqrt(91))/9=0.102357330184565... . Therefore:
- for every fixed 0<s<s_*, B has strictly GREATER Chernoff information per stipulated cost than T for all sufficiently small lawful h>0;
- for every fixed s_*<s<1, T has strictly GREATER information per cost for all sufficiently small lawful h>0;
- at s=1, the T and B experiments coincide (no erasure), c_T=1 and their Chernoff efficiencies are equal at every lawful h.

At s=s_* the fourth-order term vanishes; this theorem does not determine the sixth-order sign or a universal-in-h crossover. The asymptotic qualification depends on fixed s. At any s it makes no assertion about actual engineering costs or full nine-parameter experiment design.

### Proof

Set u=s/2, v=1-s/2, d=sh. Then B is (u+d,v-d) against (u-d,v+d). Put delta=2t-1. Introduce
A2=s^2(1/u+1/v)=4s/(2-s),
A3=s^3(1/u^2-1/v^2)=16s(1-s)/(2-s)^2,
A4=s^4(1/u^3+1/v^3)=16s(3s^2-6s+4)/(2-s)^3.

The T coefficient is Z_T(1/2)=1-s+s sqrt(1-4h^2); its minimum occurs at t=1/2 by symmetry and strict convexity, hence
C_T=2s h^2+(2s+2s^2)h^4+O_s(h^6).

For B each outcome term is p0(1+x)^t(1-x)^(1-t), with p0=u,v and x=+d/u,-d/v respectively. Expand
(1+x)^t(1-x)^(1-t)=exp[delta(x+x^3/3+O(x^5))-x^2/2-x^4/4+O(x^6)].
The sum of its linear delta*x terms vanishes exactly because the perturbations sum to zero. For delta=O(h) this gives
Z_B((1+delta)/2)=1-A2*h^2/2 + A2*delta^2*h^2/2 - A3*delta*h^3/6 - A4*h^4/8 + O_s(h^6).

For all sufficiently small nonzero h, Z_B(t) is strictly convex on [0,1]. Its minimizer is interior and solves the derivative equation; dividing that equation by h^2 and applying the implicit function theorem around (delta,h)=(0,0) yields
delta_*(h)=A3*h/(6*A2)+O_s(h^3).
Inserting this into the preceding expansion gives
min_t Z_B(t)=1-A2*h^2/2-[A4/8+A3^2/(72*A2)]*h^4+O_s(h^6).
Thus
C_B=A2*h^2/2 +[A4/8+A3^2/(72*A2)+A2^2/8]*h^4+O_s(h^6)
=2s/(2-s)*h^2 +4s(11s^2-22s+20)/[9(2-s)^3]*h^4+O_s(h^6).

Subtracting from C_T/(2-s) yields the stated factorization. The relevant roots of 9s^2-40s+4 are (20±2 sqrt(91))/9; only the minus root lies in (0,1). Since the quartic coefficient is nonzero away from s_* and s=1, the strict signs hold for sufficiently small positive h. At s=1 both original distributions reduce to the same two-outcome law. QED.

## Theorem 2: finite lawful reversal at beta_E=3/4, h=1/42

Set s=1/16, h=1/42, so beta_E=3/4 and c_T=31/16. Then **C_B>C_T/(31/16)** at this actual finite extremal witness, not only infinitesimally.

The B success probabilities are 11/336 and 10/336, and the T Bhattacharyya coefficient is
Z_T(1/2)=(315+2 sqrt(110))/336.
At t=63/125,
Z_B(t)=[(11^63*10^62)^(1/125)+(325^63*326^62)^(1/125)]/336.

The exact BigInt certificate (VERIFY.js) sets Q=10^17 and finds integers r1,r2,r3 satisfying
r1^125 <= Q^125 11^63 10^62 < (r1+1)^125,
r2^125 <= Q^125 325^63 326^62 < (r2+1)^125,
r3^2 <= 110 Q^2 < (r3+1)^2.
It then checks the STRICT integer inequality
(r1+r2+2)^31 < (315 Q+2 r3)^16 (336 Q)^15.
Hence Z_B(63/125)^31 < Z_T(1/2)^16. Since C_B >= -ln Z_B(63/125) and C_T=-ln Z_T(1/2), C_B > (16/31) C_T as claimed. QED.

## Reuse, scope and next unit

BRC reuse: the source-tagged ternary erasure observer and its Bernoulli coarse observer from the frozen two-state S23 witness. The projection T->B preserves event-2 probability but removes erasure and the other non-erased event label; this theorem quantifies the observer-cost tradeoff without collapsing underlying provenance. It is a special paired-state statistical result, not a native six-axis dynamical theorem, not a P000 update, not a refutation of the preceding s=1/4 theorem, and not a solution of ten-label decoder minimax (current [1/2,2/3]). Source and complete computational evidence accompany this note.

Next: determine sign/order for arbitrary h in (0,1/42] and the exact s_c(h) crossover (or detect multiple crossings); settle the O(h^6) sign at s=s_*. Then consider how the price-optimal source/single-event crossover changes finite-budget allocations and full nine-parameter restoration. Native owner, CLAIM, Result and independent review remain unconfirmed.
