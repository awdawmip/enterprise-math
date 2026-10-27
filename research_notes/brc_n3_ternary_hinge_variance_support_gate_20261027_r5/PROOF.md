# R5 — Ternary hinge/variance obstruction for equal-support searches

Status: AUTHOR_SIDE_PROOF + EXACT_RATIONAL_ENUMERATION; no native CLAIM, Result freeze, independent Driver review or P000 theorem admission. Date: 2026-10-27.

## Sources, observer and mathematical boundary

Global canonical input snapshot: awdawmip/chatgpt-global-knowledge main@824a3f3e950c014aeca70b0342cfe65e21d8e433 (00_BOOTSTRAP, OPERATING_MANUAL, TASK bootstrap, P000 original and verified STARTUP projection, active 我眼中的世界, math/BRC/code policies). Project research/control input snapshot: awdawmip/enterprise-math main@6f902e961157066f110980cbc2c3d4ced0946fc3, docs/PORTABLE_RESEARCH_PROTOCOL.md, AGENTS.md and exact prior R5 ancestral-signature coefficient theorem/NEXT_TASK. P000 is a locked internal worldview premise; the following is an **external finite probability tree**, not a Heartbeat dynamical law or an X6 embedding.

Carrier: ordered strictly positive rational Q branch masses q(h), corresponding P masses p(h)=L(h)q(h), and preserved hidden-history labels. Observer: O=(P(decide Q),Q(decide P),E_P tau,E_Q tau). Future actions: at depth t=1,2 either stop and decide P/Q, or continue; at depth t=3 decide. "Seedless LR" means a single behavioral action distribution for every (t,L), with no persistent common random seed. Bayesian linear objectives use positive coefficients for errors and E_Q tau. This is an actual positive-weight BRC occupancy computation, not a reduction to Boolean support or a native signed/amplitude BRC calculation.

## Theorem 1. Exact terminal hinge discrimination and conditional support gap

Let a finite positive support S={y_1<...<y_m} of terminal likelihood ratios (m>=3), and two different rational Q kernels K_1,K_2 on S have the same conditional mean r:
sum_j K_i(y_j)=1, sum_j y_j K_i(y_j)=r>0. Define H_i(u)=sum_j K_i(y_j) min(y_j,u).

(A) There exists an interior knot u in {y_2,...,y_(m-1)} with H_1(u) != H_2(u). One can find it by at most m-2 exact rational hinge comparisons. Moreover, for any chosen interior u, set s=min(r,u) and gamma=s-(H_1(u)+H_2(u))/2. Then gamma>=0.

(B) Consider a penultimate-time decision subproblem with exactly two positive Q occupation masses w_1,w_2 for histories having equal LR r but kernels K_1,K_2. Their earlier arrival masses are fixed independently of this decision (e.g. earlier continuation is constrained/forced), and other states are held fixed with no competing action difference. For the linear observer objective

    J_u = e_P + u e_Q + gamma E_Q tau

where terminal decisions minimize the Bayes risk, full-history control of stop/continue at this collision yields a strictly smaller value than one shared seedless-LR stop/continue control whenever H_1(u)!=H_2(u). The *exact local difference* (seedless minus full) is

    gap = (min(w_1,w_2)/2) * abs(H_1(u)-H_2(u)) > 0.

(C) If S={a<b<c}, choose u=b. With second moments M2_i=sum_j y_j^2 K_i(y_j),

    H_1(b)-H_2(b) = -(M2_1-M2_2)/(c-a),

    gap = min(w_1,w_2)*abs(M2_1-M2_2)/(2(c-a)).

Thus a nonzero conditional variance difference (the means are fixed) is an exact linear-support obstruction **provided the collision is actually reached with the stated fixed masses and the optimization elsewhere does not wash out the local gap**. This condition does not claim that arbitrary differing kernels imply a global support gap in an unconstrained stopping problem.

### Proof

For each distribution let H(u)=E[min(Y,u)]. The piecewise-linear function H has slope P(Y>u) between support knots, jump of derivative -K(y_j) at each knot, H(y_1)=y_1 and H(y_m)=r. If H_1=H_2 at all interior knots, they coincide at all knots and hence everywhere by linear interpolation; their slope jumps coincide, forcing K_1=K_2. This proves (A)'s existence. The map y -> min(y,u) is concave, hence H_i(u)<=min(EY,u)=s by Jensen; gamma>=0.

Under Q mass w and current LR r, stopping with the better decision costs w*s in e_P+u e_Q, while continuing to one remaining terminal observation costs w*(H_i(u)+gamma); the difference per mass is C_i=H_i+gamma-s. Our chosen gamma gives C_1=(H_1-H_2)/2=-C_2. Full-history stopping selects min(0,w_i*C_i) separately; seedless control must choose one common continuation probability, and the linear objective is minimized at a common deterministic stop or continue. With opposite signs, the resulting exact gap equals min(w_1,w_2)*abs(H_1-H_2)/2. Neither arbitrary seedless randomization nor terminal decision randomization improves a linear objective.

For (C), write delta_j=K_1(y_j)-K_2(y_j). Sum delta_j=sum y_j delta_j=0, so (delta_1,delta_2,delta_3)=v(c-b,a-c,b-a). Direct substitution gives delta M2=v(b-a)(c-b)(c-a) and delta H(b)=-v(b-a)(c-b); divide. QED.

## Theorem 2. An unconstrained ten-leaf rational N=3 strict-gap witness

There exists a fully positive rational two-measure tree with ten terminal leaves for which *earlier continuation is endogenously optimal*, and the kernels at the single LR=1 time-2 collision have different variances. Use the following exact data.

At time 1: branches a,b have Q masses 1/2 each, LR=1 each.

At time 2, under *either* branch: Q conditional weights for states L,M,H equal (2/5,1/5,2/5). Their absolute LR are respectively (1/10,1,19/10). Their Q-weighted mean LR is 1, so P mass is normalized. L and H lead at time 3 to one terminal child each with the same LR (strictly positive mass); at M there are three terminal LR values y=(1/2,1,3/2). The conditional Q kernels of time-2 histories aM and bM are respectively

    K_a = (1/4,1/2,1/4)
    K_b = (1/3,1/3,1/3).

Each kernel has terminal LR mean 1; all leaf Q and P masses are strictly positive, and the leaf Q and P totals equal 1. There are 18 non-root nodes (2+6+10).

Take J=e_P+e_Q+(7/48) E_Q tau. At an LR=1 time-2 stop, Bayes error per Q mass is s=1. Continuing at aM costs 7/8+7/48=49/48, while continuing at bM costs 5/6+7/48=47/48. Thus full-history control stops at aM and continues at bM; the seedless-LR strategy must use one shared decision at the collision. At time-2 low and high LR nodes, stopping is uniquely better than sampling because the next terminal LR does not change and gamma>0.

At time 1, conditional full-history Bellman costs of continuing (including the t=1->2 extra sample cost) are

    V_1(a)=943/1200, V_1(b)=938/1200 < 1,

where 1 is immediate stopping error cost at LR=1. Therefore *both* initial histories continue, with no externally forced arrival assumption. In the seedless model the two time-1 histories share the same coarse state and similarly both continue, with conditional cost 943/1200 < 1. The pooled time-2 mid continuation value is (7/8+5/6)/2 + 7/48 = 1, equal to the stopping value, so the compressed optimum is indifferent between the shared mid stop and continue actions.

The root initial one-observation cost is gamma=7/48. This yields exact globally optimal values

    V_full = 7/48 + (943/1200+938/1200)/2 = 2231/2400,
    V_seedless = 7/48 + 943/1200 = 559/600,
    V_seedless - V_full = 1/480 > 0.

An optional time-0 stopping action has cost 1 and is suboptimal for both classes, so allowing it changes neither value.

One full-history optimal four-vector (ties in decision at LR=1 broken toward deciding P) is

    O_full = (17/300, 17/30, 21/10, 21/10).

Two seedless optimum four-vectors (respectively both mid histories stop, or both continue) are

    O_stop = (1/25, 3/5, 2, 2),
    O_continue = (83/1200, 13/24, 11/5, 11/5).

The strict linear-support separation certifies that O_full is outside the seedless image *and* its convex hull. It therefore **does not** solve the stronger mother question about equal support functions but different observable images.

### Completeness of the finite check

VERIFY.py uses only fractions.Fraction and tests all 256 deterministic full stopping patterns on the 2+6 nonterminal histories, as well as all 16 deterministic seedless stopping patterns on the four (t,LR) nonterminal classes. Bayes-optimal decisions minimize e_P+e_Q at each stop/terminal state. Since no (t,LR) state can recur on one sample path, J is multiaffine in each separate shared action probability; extrema over all real seedless behavioral probabilities are attained at deterministic vertices. Full-history optimality similarly reduces to deterministic decisions by backward induction. This proves that the finite enumerations calculate the global minima, not just a parameter grid. Fractions check every node's Q and P consistency exactly.

## What this establishes, and does not

Author-level conditional hinge separation theorem plus an unconditional ten-leaf strict-gap construction are proved and rationally checked. The result supplies a practical **candidate-elimination gate** for the R5 equal-support mother problem: when a penultimate LR collision has distinguishable conditional kernels, search for a hinge threshold; next verify optimal arrival/continuation. Only after those checks may a SUPPORT_GAP be declared. A failed kernel-invariance test by itself is not a support-gap certificate. No native Task Owner was claimed, no Driver review took place, and no Heartbeat/X6 dynamical, P000 or physical realization claim is made.

Exact program and independent textual output: VERIFY.py and EXACT_OUTPUT.txt in this directory. Open problem and next unit: NEXT_TASK.md.
