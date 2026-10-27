# Exact BRC two-law compression facet at the same-side off-diagonal point

Date: 2026-10-27. Role: local TASK_RESEARCH author (no native CLAIM). Status: AUTHOR_PROVED / EXACT_FINITE_EXHAUSTION / UNREVIEWED / NOT_ADMITTED. This is an external finite probability model, not an experiment in P000 X6 native Cell dynamics.

## Inputs and preservation boundary

Account GLOBAL_KNOWLEDGE_V1 frozen canonical main a3c59d04ad4cdb1e444c785b4ca3b3732674d4fd: 00_BOOTSTRAP, OPERATING_MANUAL, P000_STARTUP projection, original P000 matching Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview, mathematics/BRC/code policies. Initial EM source main 99eb207957daa0395c1915f32cff9752a32b3b2a; predecessor immutable proof 384ce351d1e157b532e42229c0f6e11d23732673, research_notes/brc_n3_signed_support_reverse_phase_20261027_r1t11/PROOF.md.

We preserve the existing BRC carrier (strictly positive Q and P branch masses, ordered branch provenance, path likelihood ratio r=P/Q), the observer O and allowed future stop/decision operations. The unique nonterminal compressed collision is ax~bu, both at (time 2,r=1). Their distinct future conditional kernels are structural residual information. P000 retains six native spatial axes plus separately typed time; this example is not transferred into native 3D slices/6D Cell geometry.

The horizon is 3, with 15 ordered prefixes, eight leaves and shared fresh-coin stop/decision actions. Q(root)=1; Q(a)=Q(b)=1/2; Q(ax)=Q(ay)=1/4; Q(bu)=1/8; Q(bv)=3/8. Ratios r=P/Q are 1, 3/2, 1/2, 1, 2, 1, 1/3 respectively. Under each ax or bu, the leaf ratios are (1/2,1,3/2); its Q conditional probabilities are (s,1-2s,s). ay and bv each have one terminal child preserving r. Freeze s_a=1/6 and s_b=1/5. Define P(h)=Q(h)r(h). All P/Q masses at every edge are strictly positive and conserve both probability laws.

Full-history strategies use ordered history. Seedless compressed strategies use only the current (t,r) and independent fresh local randomness; no persistent initial random seed. At terminal time 3 only decisions P,Q are available; at t<3 the actions are stop-P, stop-Q, or continue. They share decisions between distinct histories at identical (t,r).

Observe O=(P(decide Q), Q(decide P), E_P[T], E_Q[T]). In this model the eight leaves and the allowed early stopping are exactly specified; decisions and continuation are common between P and Q.

## Main exact facet theorem

For every compressed behavioral strategy, including arbitrary real-valued fresh local randomization, the following inequality holds:

  302 O_1 + 363 O_2 + 28 O_3 - 12 O_4 >= 1091/4.  (F1)

The convex hull of compressed observer vectors is full-dimensional in R^4, and equality in (F1) defines a three-dimensional face. Hence (F1) is a genuine rational facet inequality, not merely a supporting objective.

A legal full-history deterministic strategy has

  O_F=(37/80,11/40,9/4,5/2)

and attains

  302 O_F1+363 O_F2+28 O_F3-12 O_F4=545/2,

strictly below 1091/4 by 1/4. Therefore O_F lies outside the compressed behavioral image **and outside its convex hull**. At the previously unresolved same-side point (1/6,1/5), hull equality fails.

## Universal lower bound via finite Bellman equations

Let lambda=(302,363,28,-12). At a history with r=P/Q, normalize the remaining linear objective by its Q mass and exclude elapsed time already accrued. Stop P costs 363; stop Q costs 302r; continue costs 28r-12 plus the Q-conditional expectation of the successors' value. At terminal r=(1/2,1,3/2), the minimum costs are (151,302,363).

At either colliding history with parameter s, the continuation cost is

  (28-12)+151s+302(1-2s)+363s = 318-90s.

Thus at ax (s=1/6), continue costs 303, while stopping Q costs 302; at bu (s=1/5), continue costs 300, while stopping Q costs 302. The full-history optimizer chooses stop Q at ax and continue at bu. At ay the optimum is stop P, cost 363; at bv it is continue to its sole leaf, cost 98. At a, b, root the respective full-history values are 725/2, 301/2, and 545/2; all three choose continuation. This derives the full minimum and a deterministic witness, independently of enumerating compressed tables.

Every compressed state includes time, hence no trajectory visits an action state more than once. For any fixed other local action distributions, the expectation of this finite-horizon linear objective is affine in the remaining local distribution. Coordinatewise optimization over finite probability simplexes therefore attains a global minimum at a deterministic action at every compressed state. This reduction covers ALL real fresh-coin behavioral policies, not only rational or sampled randomization.

The only shared nonterminal action class is {ax,bu}. Force its common action, and Bellman-optimize the other singleton nonterminal states and compatible terminal classes. The exact global root minima are:

  shared STOP P: 273
  shared STOP Q: 1091/4
  shared CONTINUE: 1091/4.

Each terminal (time,ratio) class has a common normalized minimizing decision, so the Bellman calculation is also feasible in the compressed policy class. Therefore the compressed minimum over every possible randomized strategy is precisely 1091/4, proving (F1) for all such strategies.

## Exact facet dimension certificate

The immutable executable VERIFY.js exhausts 3^6 * 2^5 = 23,328 pure compressed action tables. It uses integer units of 1/240 for every coordinate (all P/Q terminal masses have denominators dividing 240), producing exactly 326 distinct four-vectors. Every one satisfies (F1), and precisely four distinct vectors meet equality. In original unscaled coordinates these are

  (1/2, 1/4, 7/4, 3/2)
  (17/80, 21/40, 3/2, 2)
  (1/2, 1/4, 17/8, 19/8)
  (2/5, 19/60, 5/2, 11/4).

Their affine difference matrix has rank three, checked by a nonzero exact BigInt 3x3 minor. A full-dimensional affine witness of rank four is given by

  (0,1,0,0)
  (1,0,0,0)
  (0,1,1,1)
  (3/4,1/2,1,1)
  (0,1,7/4,3/2).

Each occurs among the 23,328 tables, and the verifier checks its exact nonzero 4x4 determinant. Thus the compressed convex hull has dimension four and (F1)'s tight face dimension three: (F1) is a facet. Complete pure-strategy coverage and multi-affinity justify the assertion for the full behavioral convex hull.

The full witness continues at root,a,b,bu,bv; stops Q at ax; stops P at ay; and at terminal (r=1/2,1,3/2) decides (Q,Q,P), with ayT=P and bvT=Q. Its exact integer-scaled observation is (111,66,540,600), yielding O_F above. Exhaustive verification also checks all 15 prefixes, all 8 positive leaves, and P/Q mass conservation. No floating-point inequality or numerical hull oracle is used in the final certificate.

## Claim boundary and continuation

This is an author-side finite constructive proof with actual independent arithmetic routes (Bellman support derivation and complete integer table/affine rank verifier). No Lean checker, independent Research Driver acceptance, native Owner CLAIM/Result, or P000 X6 transition embedding has been established. Source is a reusable exact negative boundary for observer- and future-operation-specific BRC compression. In particular, current ratio equality does not suffice to merge these two futures.

Next: test the other same-side pair (s_a,s_b)=(1/3,2/5) with exact rational support/facet search; then seek a parameterized separation theorem or a genuine hull-equality regime if it exists. Only after rigorously proving hull equality for some off-diagonal point should one ask for a nonconvex-image-only witness using exact semialgebraic feasibility.
