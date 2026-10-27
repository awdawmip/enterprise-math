# R1/N14 — Exact convexity and occupancy polytope for all finite IID two-law LR-fiber quotients

Date: 2026-10-27. Status: AUTHOR MATHEMATICAL PROOF, independent Driver review / Lean / native P000-X6 correspondence PENDING.

## Source and target
GLOBAL_KNOWLEDGE_V1 immutable read snapshot `28f64a904bd2a8c659ab65dc4eccb0de5b49edff` (P000 projected canonical blob verified: `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`). Enterprise Math source input `8e319f70db14e428cb914c0119f26a0fad500a35`, portable research protocol `docs/PORTABLE_RESEARCH_PROTOCOL.md`. Exact predecessor `research_notes/r1_n14_brc_lr_fiber_nonconvex_n3_20261027_r1/PROOF.md` proved non-IID N=3 nonconvexity even with all LR-constant fibers. Its `NEXT_TASK.md` asks whether IID admits the same phenomenon.

## Exact theorem
Let A be finite, N finite, P=(p_a) and Q=(q_a) strictly positive IID probability vectors (real parameters allowed), and x_t:A^t->S_t a time-typed deterministic recursively updated finite state: x_0(empty)=s0 and x_{t+1}(ha)=rho_t(x_t(h),a). Distinct times have disjoint labels. Suppose every x-fiber has a constant Q/P likelihood ratio: for h,h' with x_t(h)=x_t(h'), Q(h)/P(h)=Q(h')/P(h')=:r_x. A common stopping/finite-decision policy uses the same conditional randomization under both P and Q and must stop by N. An x-only policy depends solely on x and a fresh randomized action, with no hidden persistent selector.

**Theorem:** At every finite N, every common full ordered-history stopping/decision policy has a common x-only fresh-coin policy preserving the **entire joint law of (T,x(H_T),D)** under P and under Q. Therefore it also preserves any deterministic coarsened terminal observer (T,o(x(H_T)),D). The simultaneous two-law attainable set is exactly a linear image of a bounded finite-dimensional occupancy polytope, hence compact and convex, rational-polyhedral if P,Q are rational. Thus an IID analogue of the predecessor's LR-fiber N=3 nonconvexity witness cannot exist under these assumptions, at any finite horizon.

## Proof: preserve BRC branch weights before quotienting
For ordered path h, P(h)=product of its p_a and Q(h)=product of its q_a. Retain h as distinct positive BRC branch with conditional survival multiplier s(h), the product of continuation probabilities on strict prefixes. For u in S_t, v in S_(t+1), define

K_P(u,v) = sum_{a:rho_t(u,a)=v} p_a,   K_Q(u,v) = sum_{a:rho_t(u,a)=v} q_a.

Because the next symbol is IID under each law and the state update rho is deterministic, these are genuine *history-independent* state transition kernels (strong lumpability for each law). On an edge rho_t(u,a)=v, take any h in the u-fiber. Fiber LR constancy implies

r_v=Q(ha)/P(ha)=[Q(h)/P(h)](q_a/p_a)=r_u q_a/p_a,

so r_u q_a=r_v p_a. Summation over symbols leading to v yields the **edge intertwining identity**

                     r_u K_Q(u,v)=r_v K_P(u,v).            (1)

The root ratio r_s0=1. Importantly, IID supplies the strong-lumpability part which failed in the predecessor's non-IID example. LR constancy alone did not supply it.

## Exact linear flow representation
Introduce nonnegative P-state occupancies m(u), stop-and-decision P action flows z(u,d) for every d in finite D, and continuation flow z(u,c) for t<N (zero at N). Define the finite occupancy polytope F:

m(s0)=1;
m(v)=sum_{u in S_t} K_P(u,v) z(u,c) for all v in S_(t+1);
m(u)=sum_{d in D} z(u,d)+z(u,c) at each u;
m,z>=0 and z(u,c)=0 at N.

For every terminal observer label b and decision d, define paired linear output forms

Y_P(t,b,d)=sum_{u in S_t : o_t(u)=b} z(u,d);
Y_Q(t,b,d)=sum_{u in S_t : o_t(u)=b} r_u z(u,d).     (2)

**Forward, x-only -> F and (2).** Given common x-policy pi_u, its P masses m_P and z_P(u,a)=m_P(u)pi_u(a) obey F by the controlled Markov property. By induction and (1),

m_Q(v)=sum_u K_Q(u,v)m_Q(u)pi_u(c)
       =sum_u K_Q(u,v)r_u z_P(u,c)
       =r_v sum_u K_P(u,v)z_P(u,c)=r_v m_P(v).

Thus z_Q(u,d)=r_u z_P(u,d) and terminal outputs obey (2).

**Reverse, F -> common x-only fresh-coin policy.** For every feasible m,z, define pi_u(a)=z(u,a)/m(u) if m(u)>0; for a zero-mass state select any legal stop action. The P occupancy induction exactly recovers m,z. Identity (1) then forces the Q occupancy to be r_u m(u), and its observer outputs are precisely (2). The construction uses only immediate fresh coins and a **single law-independent action kernel**; it carries no hidden prior strategy selector.

**Full-history policies are already represented.** Given any shared ordered-history policy with survival s(h) and history-dependent action pi_h(a), form

m(u)=sum_{h:x_t(h)=u} P(h)s(h),
z(u,a)=sum_{h:x_t(h)=u} P(h)s(h)pi_h(a).

Positive BRC branch masses guarantee nonnegativity and state-wise mass conservation. Summing the histories' successor flows commutes with quotienting because IID+rho implies K_P(u,v) independent of which h is in u. Hence these m,z satisfy F. On each u-fiber Q(h)=r_u P(h), so the original history-policy Q stop flow equals r_u z(u,d), **without changing its policy between laws**. The reverse construction then gives an x-policy reproducing the original full-history outputs simultaneously for P and Q. This proves universal two-law Markovization and exact equality of the attainable sets.

**Convexity / rational exactness.** F is closed, finite-dimensional and bounded: sum of state occupancies at any time <=1 and each z<=m, hence compact. Formulas (2) are linear; their image is therefore compact and convex. If p,q rational, then K_P and r_u rational, so F and the image are rational polytopes with finite exact linear-programming/Farkas certificates. No finite test has been substituted for this all-finite-N proof. QED.

## Direct policy-level mixing formula
For x-only policies A,B and lambda in [0,1], mix their **P** state occupancies/actions: m=lambda m_A+(1-lambda)m_B and z=lambda z_A+(1-lambda)z_B. At positive m define

pi_mix(u,a)=[lambda*m_A(u)*pi_A(u,a)+(1-lambda)*m_B(u)*pi_B(u,a)]
             /[lambda*m_A(u)+(1-lambda)*m_B(u)].

This common local kernel exactly realizes the paired distribution mixture under P and Q because m_Q,alpha(u)=r_u m_P,alpha(u). Arithmetic averaging of local decisions without incoming BRC path weights need not preserve flow.

## Executed finite evidence and scope
Standalone CPython `fractions.Fraction` checker `VERIFY.py` with `RESULT.json` was actually run on N=4, A={0,1,2}, P=(1/2,1/3,1/6), Q=(1/3,1/2,1/6), x=(time,#0,#1), lambda=2/5. All 121 ordered prefixes / 35 time-count states were enumerated, LR constancy and two-law exact Markovization verified; original full-history policies and separately quotient-only policies both tested. The original executed source and full output are bundled as a local evidence archive. These finite results are a sanity check, not the logical basis of the universal theorem. Independent Research Driver, Lean, and P000 native six-dimensional Cell / three-dimensional slice mapping are NOT verified.

BRC/tool resolution: REUSE_APPLIED positive-rational ordered branch mass and predecessor-kernel reasoning from `research_notes/r1_n14_brc_two_law_strong_lumpability_iff_20261026_r1/PROOF.md`; COMPOSE_APPLIED BRC flow conservation + IID strong lumpability + LR intertwining. No new top-level tool family, no signed/complex cancellation, no physical inference and no claim of academic novelty beyond this precisely scoped author proof.

## Next exact open problem
For finite strictly positive **non-IID** history laws with LR-fiber constancy but lacking SL, construct the coarsest time-typed recursively updated refinement z=(x,repair) satisfying both LR and SL. Prove a terminating exact partition-refinement algorithm, determine its minimal state number for the predecessor's 40-prefix N=3 witness, and identify which coarser terminal observers factor through z. See `NEXT_TASK.md`.
