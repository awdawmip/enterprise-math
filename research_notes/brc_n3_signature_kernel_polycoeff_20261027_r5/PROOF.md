# R5 — ancestral-signature coefficient criterion for policy-invariant exact-LR prediction

Status: AUTHOR_LEVEL_ALGEBRAIC_PROOF / EXACT_RATIONAL_CHECK_PASSED / NO_NATIVE_CLAIM / NOT_DRIVER_REVIEWED. Date: 2026-10-27.

## Fixed sources and semantics

GLOBAL_KNOWLEDGE_V1 canonical main pinned at b93af5fa5d1f56cff9a63f730c86247619d79b86; Enterprise Math research input main pinned at 28ecdefbfebe8418383794ebe1635617fd1df069. Loaded global 00_BOOTSTRAP, OPERATING_MANUAL, Enterprise Math TASK research startup, P000 startup projection and original (canonical Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), ACTIVE residual worldview, math/code/BRC policies, project portable research protocol. Scientific predecessor: research_notes/brc_n2_universal_convex_hull_gate_20261027_r5/{PROOF,NEXT_TASK}. This is an **external finite positive two-measure tree**; its depth is observation count, not Heartbeat native physical time, and its exact likelihood ratio is not a six-axis spatial coordinate. Weighted-BRC reuse: ordered positive Q branch mass, P mass as exact LR times Q mass, retained ancestral source signature, exact rational quotient audit.

Native read-only control-tasks returned CONTROL_QUOTA and a native RESEARCHER session attempt returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. GitHub authentication is awdawmip with push/admin for this project. The local session label is client-assigned and no active Owner, CLAIM, Result or independent Driver review has been asserted.

## Exact problem

Let a finite strictly positive Q/P observation tree have horizon T, histories h at depth t, unconditional masses q_h>0 and p_h>0, and r_h=p_h/q_h. At every nonterminal time/likelihood-ratio state g=(t,r), a seedless behavioral policy shares the same continuation probability c_g independently of hidden history; the remaining stop mass can be split between decisions P and Q. No persistent root lottery is available. The full-history strategy distinguishes every ordered history.

For h at time t, write its ancestors h_0,...,h_(t-1), and define the ancestral time/LR signature sig(h)=((0,r_h0),...,(t-1,r_h(t-1))). The independent continuation variables attached to these signatures give the monomial

    M_h(c) = product over j<t of c_(j,r_hj).

Let H_g be the histories with state g. Define the conditional Q next-step LR kernel K_h(s)=sum_{child u of h:r_u=s} q_u/q_h. Define polynomials

    D_g(c)   = sum_{h in H_g} q_h M_h(c),
    N_g,s(c) = sum_{h in H_g} q_h M_h(c) K_h(s).

For strictly positive interior c, the reachable aggregated kernel after *continuing at g* is N_g,s(c)/D_g(c). The factor c_g cancels because it is common to the histories in H_g.

## Theorem A — coefficientwise necessary-and-sufficient gate (arbitrary finite T)

For each signature sigma represented in H_g set

    d_(g,sigma) = sum_{h in H_g:sig(h)=sigma} q_h > 0,
    n_(g,sigma,s) = sum_{h in H_g:sig(h)=sigma} q_h K_h(s),
    k_(g,sigma,s) = n_(g,sigma,s)/d_(g,sigma).

Then the following are equivalent:

1. For every seedless continuation policy with all c in (0,1), the conditional Q next-step LR distribution at g is independent of policy.
2. For each possible next LR s, all ancestral-signature coefficients k_(g,sigma,s) agree, independently of sigma.
3. For each s there is a rational constant k_(g,s) such that the polynomial identity N_g,s(c)=k_(g,s)D_g(c) holds.
4. On the finite two-point grid c_u in {1/3,2/3} for every ancestor coarse-state coordinate u that occurs in the signatures, the conditional next LR kernel is identical at every grid point.

Here the positivity and rationality assumptions make all coefficients and witnesses exact. No pointwise strong lumpability K_h=K_h' is required inside a shared ancestral signature.

**Proof.** Group h by sig(h). Since each time t' occurs at most once among the ancestors, each M_h is squarefree/multiaffine in the independent time/LR variables. Two different ancestral signatures contain a different variable at some fixed time and hence determine distinct monomials. We obtain D=sum_sigma d_sigma M_sigma and N=sum_sigma n_sigma,s M_sigma. Statement 2 is exactly the coefficientwise polynomial identity in 3. This implies 1 by division by D>0. Conversely, if N/D equals a constant k on the open cube, the polynomial N-kD vanishes on an open set and hence identically; uniqueness of monomial coefficients gives n_sigma,s=k d_sigma for all sigma. Thus 1 implies 2. Finally, N-kD is multiaffine in each ancestor variable. A multiaffine polynomial vanishes identically iff it vanishes on the Cartesian product of any two distinct values of each variable (induction on variables using affine interpolation). Choose k as the conditional kernel at one grid point, denominators being positive. Grid constancy is then equivalent to 3. QED.

**Certificate/execution complexity.** Group histories once by (t,r,sigma), add unconditional exact q masses and child-q masses by next s, then compare each signature-conditional rational vector. There are at most as many signature groups as tree nodes, and assembling signatures takes O(T times number-of-nodes) combinatorial operations, plus exact rational arithmetic. Failing coefficient vectors are a compact exact obstruction; the two-level positive rational grid supplies an actual policy-variation witness. Bit-complexity depends on input denominators and is not claimed strongly polynomial.

## Theorem B — a general exact strong-counterexample exclusion gate

If Theorem A's coefficient test succeeds at *every* nonterminal (t,r), then the four-observer image of seedless time/exact-LR strategies is a compact **rational convex polytope**.

**Proof.** Let m_g be Q arrival mass at g and d_g^P, d_g^Q, a_g the Q occupation masses stopping/deciding P, stopping/deciding Q, and continuing. They obey m_g=d_g^P+d_g^Q+a_g, with a_g=0 at terminal time. Theorem A makes K_g(s) independent of policy; hence m_(t+1,s)=sum_r a_(t,r) K_(t,r)(s). Fix m_(0,1)=1. All these constraints are linear with rational coefficients and nonnegative variables. Any seedless behavioral policy induces such a flow. Conversely a feasible flow yields a seedless policy by conditional action ratios (d_g^P/m_g,d_g^Q/m_g,a_g/m_g) at m_g>0, arbitrary choices at zero-mass states. Induction on depth plus the policy-invariant aggregate kernel shows that these ratios reproduce the prescribed flows. The observer map is linear:

    e_P = sum_g r_g d_g^Q;
    e_Q = sum_g d_g^P;
    E_P(tau) = sum_g t_g r_g (d_g^P+d_g^Q);
    E_Q(tau) = sum_g t_g (d_g^P+d_g^Q).

Thus the image is a linear projection of a bounded rational flow polytope. The full-history image is also a compact convex polytope, by the identical construction retaining each complete history rather than merging LR states. Therefore, within this coefficient-test-passing class, if *all* signed four-observer linear support extrema are equal between full-history and seedless strategies, their actual four-vector images are equal. In particular this class cannot realize the open equal-support/different-image counterexample. QED.

Passing Theorem A is a sufficient structural gate for convexity, not a necessary condition for convexity or exact four-observer fidelity. Failure of Theorem A alone does **not** prove a support gap, nonconvexity, or an image hole.

## A new 14-leaf strict-positive rational family

Root: Q(a)=1/3, Q(b)=2/3, LR(a)=2, LR(b)=1/2; P masses are respectively 2/3,1/3.

At both a and b, the Q transition weights into u,v,w are (1/8,1/8,3/4). Set LR(au)=LR(av)=LR(bu)=LR(bv)=1, LR(aw)=7/3, LR(bw)=1/3. All P transitions equal corresponding Q transition times child-LR/parent-LR; these normalize (a: 1/16,1/16,7/8; b: 1/4,1/4,1/2). At each of the four LR=1 histories h in {au,av,bu,bv}, terminal LR values y=(1/2,1,3/2) have conditional Q weights (s_h,1-2s_h,s_h), where 0<s_h<1/2. Their conditional P weights are (s_h/2,1-2s_h,3s_h/2). The w nodes have one terminal child with unchanged LR and probability 1, which is strictly positive. This tree has 23 nodes, including 14 leaves.

Let \bar s_a=(s_au+s_av)/2, \bar s_b=(s_bu+s_bv)/2, and let x_a,x_b>0 be first-stage continuation probabilities. At the only strategic LR collision g=(2,1), BRC's retained ancestral source signatures give Q arrival weights (x_a/12,x_b/6). Hence

    K_g(y=1/2; x_a,x_b) = (x_a \bar s_a + 2 x_b \bar s_b)/(x_a+2 x_b).

The central probability is one minus twice this expression, and the y=3/2 probability equals this expression. So **the entire finite tree passes the invariant-kernel coefficient gate iff**

    s_au+s_av = s_bu+s_bv.

The equality is signature-level, not history-level; four terminal kernels may be pairwise distinct.

For a safe but NOT pointwise lumpable example choose (s_au,s_av,s_bu,s_bv)=(1/10,2/5,1/5,3/10). Then each signature-average equals 1/4, and K_(2,1)=(1/4,1/2,1/4) for every earlier seedless policy. Theorem B excludes the sought strong equal-support/different-image phenomenon throughout this safe hyperplane.

Change only s_bv to 1/4. Now \bar s_b=9/40, \bar s_a=1/4. Conditional outer probability equals 7/30 at (x_a,x_b)=(1,1), and 19/80 at (1,1/2), a strictly nonzero exact difference of 1/240. This certifies policy-dependent aggregate prediction, **not** a four-observer image separation.

## Verification, reproducibility, epistemic boundary

The attached stdlib fractions.Fraction verifier explicitly constructs all 23 nodes, checks each Q and P parent/child conservation identity, positivity, leaf normalization and LR labels, groups every nonterminal state by ancestral signature, checks exact coefficient kernels for both variants, and checks the above rational values and two-point grid. Its executed output is EXACT_OUTPUT.txt. The universal coefficient/polytopal theorems are algebraic proofs, not extrapolations from this finite model. No real-closed-field elimination or general equal-hull counterexample was computed.

BRC application: REUSE_APPLIED (ordered weighted positive branch mass, exact LR and signature-preserving flow); do not infer native Heartbeat dynamics, independent Driver review, a formal CLAIM, or P000 change.

## Unfinished mother question

For failing coefficient-gate N=3 ternary models, test exact inclusion of all full-history deterministic four-vectors in the convex hull of the seedless deterministic vectors, with a rational Farkas separator on failure. Only equal-hull candidates proceed to all-real polynomial nonmembership/QE. Theorem A is a fast *convexity exclusion gate*, not a substitute for that stronger test.
