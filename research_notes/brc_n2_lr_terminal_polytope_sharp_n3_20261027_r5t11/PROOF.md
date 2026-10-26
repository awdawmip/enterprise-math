# N=2 likelihood-ratio homogeneous terminal fibers form an exact rational polytope

Date 2026-10-27. Proof status: AUTHOR_PROVED / external finite two-law decision-tree model / not independently reviewed or native P000/X6 dynamics.

## Source and question
Frozen read snapshots: GLOBAL_KNOWLEDGE_V1 main ac62f31cce08180e194315a13a299f66491bd647; Enterprise Math main 953a90bc8d1d8cf252c1e671741a4b7d5e3625e8. The current P000 and ACTIVE residual-faithful worldview remain unchanged. BRC reuse: ordered strictly positive rational P/Q branch masses, labeled histories, typed quotient and readout. This analysis does not assert a native X6 realization.

Question: given two probability laws P and Q, a finite horizon N=2 observation tree, a deterministic time-typed compressed state x(h), and a single common behavioral policy with fresh local coins but no persistent selector, when is the *paired* P/Q stopped-time/observer/decision output set necessarily convex?

## Theorem A (terminal-LR homogeneous convexity)
Assume a unique deterministic root, finite strictly positive rational P/Q cylinder probabilities and finitely many decision labels d. The policy may continue or stop-and-decide at time 0 or 1, and must decide at time 2. At every history h the action depends only on the state x_t(h), identically under P and Q. Require only that every *terminal* state z has a constant likelihood ratio

    P(h)/Q(h)=ell_z  for all terminal h with x_2(h)=z.                 (LR2)

No strong predictive lumpability of hidden histories and no time-1 LR homogeneity is required.

For any fixed observer o(x), collect all coordinates

    Y_{m,t,v,d} = Pr_m(tau=t, o(x_t(H_t))=v, decision=d), m in {P,Q}.

Then the attainable simultaneous Y-image of all such quotient behavioral policies is a compact RATIONAL CONVEX POLYTOPE. Every finite convex combination of attainable Y-vectors has a realization by one quotient behavioral policy with no persistent root seed. For rational source probabilities and rational mixing weights the recovered local action probabilities are rational. The theorem includes all real-valued behavioral probabilities.

In particular, the image of the four standard coordinates
    O=(P(decide Q), Q(decide P), E_P tau, E_Q tau)
is convex.

## Exact flow proof
Let S be the time-1 compressed state set and Z the time-2 state set. Define fixed rational constants

    q_s = sum_{h in H1 : x1(h)=s} Q(h),
    p_s = sum_{h in H1 : x1(h)=s} P(h),
    K_{sz} = sum_{g in H2 : x1(prefix(g))=s, x2(g)=z} Q(g).

Since every g in terminal state z obeys (LR2), the analogous P sum in K_{sz} equals ell_z K_{sz}. The theorem does *not* require K_{sz} to factor by hidden predecessor history.

Introduce nonnegative POLICY-ONLY variables: r=root continuation; b_d=root stop/decide d; c_s=root continuation AND continue at t1 state s; a_{sd}=root continuation AND stop/decide d at t1 state s; v_{zd}=Q terminal arrival mass in state z assigned decision d. The entire feasible system is LINEAR:

    r+sum_d b_d=1;
    c_s+sum_d a_{sd}=r                               for each s;
    sum_d v_{zd}=sum_s K_{sz} c_s                    for each z.        (F)

For a genuine quotient policy, set r and b_d to its root action probabilities; let c_s=r*Pr(continue | s) and a_{sd}=r*Pr(stop/decide d | s). The Q arrival mass at terminal z is w_z=sum_s K_{sz}c_s, because all histories in the same t1 state use one kernel. Set v_{zd}=w_z*Pr(decision d|z). Its P-terminal mass is ell_z v_{zd}, *independent of the upstream mixture*. Thus all observer coordinates are affine linear functions of (F):

    Y_{Q,0,v,d}=1[o(x0)=v] b_d;
    Y_{P,0,v,d}=1[o(x0)=v] b_d;
    Y_{Q,1,v,d}=sum_{s:o(s)=v} q_s a_{sd};
    Y_{P,1,v,d}=sum_{s:o(s)=v} p_s a_{sd};
    Y_{Q,2,v,d}=sum_{z:o(z)=v} v_{zd};
    Y_{P,2,v,d}=sum_{z:o(z)=v} ell_z v_{zd}.         (Y)

Conversely, given any nonnegative solution of (F), use root action probabilities (r,b_d); at each t1 state s use (c_s/r,a_{sd}/r) if r>0; at each terminal state z use v_{zd}/w_z if w_z>0. At unreachable states select any admissible action. The constraints imply all kernels are normalized and nonnegative. These *same* kernels work under BOTH measures, exactly reproducing (Y). This proves equality of the output image and the linear image of bounded rational polytope (F); compactness, rationality, convexity and rational mixture lifting follow. No inference from a finite grid is used. QED.

## Corollary B (exclusion of an N2 equal-support / missing-image witness)
The complete-history four-observable set F_full is a compact convex polytope by standard full-history policy-only occupancy-flow linearization. The quotient set K_O is also compact convex by Theorem A, and K_O is included in F_full. By finite-dimensional convex separation,

    [min_{x in K_O} c*x = min_{x in F_full} c*x for every signed c in R^4]
       iff K_O=F_full.

Consequently, when the N2 terminal state preserves likelihood ratio, it is IMPOSSIBLE to have full/quotient equality for every signed Bellman linear objective but a four-observable full-history vector missing from the quotient image. This narrows the stronger unresolved N3/4 search to N>=3 (within this policy/observer class).

## Sharp horizon and boundary with concurrent R1 result
The prior independent R1 proof
  research_notes/r1_n14_brc_two_law_fresh_coin_nonconvex_n2_20261027_r1t11/PROOF.md
provides an N2 binary strictly positive *nonconvex* simultaneous two-law (T,D) observer image when its compressed terminal state merges different likelihood ratios; its midpoint rank-one determinant is 1/8. That does NOT contradict Theorem A, since (LR2) fails. Thus terminal LR homogeneity is a consequential scope condition, not merely cosmetic.

The prior R5 proof
  research_notes/brc_n3_seedless_behavioral_nonconvexity_20261027_r5/PROOF.md
supplies an 8-leaf strictly positive N3 model with x=(time,exact LR) and a nonconvex four-observable image. Its two feasible vectors are
    O0=(1/9,5/9,13/9,19/9);
    O1=(5/42,3/7,5/2,17/6),
while midpoint
    O*=(29/252,31/63,71/36,89/36)
has no real seedless quotient realization. Its proof uses an explicit signed Bellman lower envelope over ALL real local probabilities, not only deterministic grid search. The archived verifier was re-executed on this turn, checking 23,328 deterministic quotient tables and the same two optimal time-pairs. Therefore for LR-exact quotient states and the four-vector observer, horizon N3 is the first possible horizon of seedless behavioral nonconvexity. This *minimality synthesis* combines Theorem A with already published N3 author proof; it is not a new independent review of the latter.

## Exact rational N2 witness
Let Q(a,b)=(1/3,2/3), P(a,b)=(2/3,1/3). At time 2:

    history      Q        P        LR
    ax           1/6      1/6      1
    ay           1/6      1/2      3
    bx           4/9      1/9      1/4
    by           2/9      2/9      1

The terminal LR=1 class merges ax and by, reached from different time-1 LR classes 2 and 1/2. With source quotient policies A,B and lambda=2/5 (defined in VERIFY.py), the algebraic flow-recovered quotient policy C is

    root actions (continue,P,Q)=(3/5,3/10,1/10);
    t1 actions, at each LR 2 and 1/2: (continue,P,Q)=(1/2,3/8,1/8);
    t2 Pr(decide Q | LR 1/4,1,3)=(5/6,13/28,3/8).

Exact independent path-probability accumulation yields

    O(A)=(677/1152,577/1152,19/16,17/16);
    O(B)=(25/192,47/64,17/24,19/24);
    O(C)=(451/1440,923/1440,9/10,9/10)
        =(2/5)O(A)+(3/5)O(B).

All twelve paired law/time/decision coordinates, not only four, match the mixture. A stdlib Python fractions.Fraction verifier checks positivity, P/Q normalization, exact LR identities and this equality. It also checks 7,776 seeded choices of pairs/weights from a universe of 216 deterministic quotient policies (216*12*3), all exact rational. This is finite cross-checking, not an all-real proof; the all-real proof is (F)-(Y). The actual executed script's Git blob is 791d301e0ce442e3391e27b010916de9e76ff091.

## Scientific status and next question
REUSE_APPLIED: BRC positive ordered rational path-mass carrier, history provenance, typed LR quotient and observer. The validity is external finite P/Q tree mathematics only. This result proves quotient convexity, NOT that full-history compression preserves all values at N2 for every model, nor any P000 native dynamics law. No native CLAIM, Source Result freeze, independent Driver review or X6 transfer is implied.

Unresolved: for N>=3 LR-homogeneous quotient, find/exclude equality of all signed full/quotient four-observable supports with an absent full-history four-vector. First certify deterministic full-history hull inclusion into quotient deterministic hull using rational LP; only then try exact real polynomial nonrealizability. See NEXT_TASK.md.
