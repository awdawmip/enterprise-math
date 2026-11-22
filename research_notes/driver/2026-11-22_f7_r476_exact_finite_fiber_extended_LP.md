# CBRC F7 r476 — an exact cubic-size extended LP for finite-box minimax

Date: 2026-11-22 (Asia/Taipei). New mathematical / computational formulation by original RESEARCH_DRIVER logical lane EM-DVR-DEBB5E. This is a separate, bounded scientific subunit; original F7 scientist EM-CBRCF7-83A1D4, frozen Result RR-AA38973D56330E59D315, Task provenance and all native review statuses remain unchanged.

## Statement under the original, unmodified F7 scalar conditions

Let A be the class of real-valued q: Z² -> R with q(-x,y)=q(x,y); q(0,0)=0; q(x,0)=1 for x!=0; q(x,y)>=1/2 for y!=0; and q(2,1)=q(-1,-1)=1/2. For integers a,b,c,d, put k=a-2b-c+2d and

D_q(a,b,c,d) = q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d).

Let E_B(q)=max_{a,b,c,d in [-B,B]∩Z}|D_q(a,b,c,d)| and e_B=inf_{q∈A} E_B(q).

For each r∈R_B={-2B,...,2B}, define the nonempty integer interval

T_r = {a-2b: |a|<=B, |b|<=B, a-b=r}
    = [2r-min(B,r+B), 2r-max(-B,r-B)]∩Z,

of size |T_r|=2B+1-|r|. Let h_r(v)=q(2r-v,r-v). For each unordered pair r<u introduce **two independent real auxiliary variables** L_{r,u},U_{r,u} and write F_{r,u}(v)=h_r(v)-h_u(v).

**Theorem (exact extended formulation).** For every B>=1 and real epsilon>=0, a globally F7-admissible q with E_B(q)<=epsilon exists if and only if the following finite rational linear system has a solution:

For every r<u in R_B,

(1) L_{r,u} <= F_{r,u}(t) <= U_{r,u}, for all t in T_r;

(2) U_{r,u}-epsilon <= F_{r,u}(s) <= L_{r,u}+epsilon, for all s in T_u;

together with the original axis/mark equalities, x-evenness and off-axis floor on the finite q coordinates that appear. Each distinct (|x|,y) off axis and outside the two fixed marks is one q variable, with lower bound 1/2; no extra upper bound or artificial regularity is assumed.

The exact number of scalar inequalities (1)–(2) is

    2*(|R_B|-1)*sum_{r∈R_B}|T_r|
  = 8B(2B+1)^2 = O(B^3),

compared with 2(2B+1)^4 inequalities from applying both signs to every original quadruple. There are exactly 2*binomial(4B+1,2) auxiliary variables. Fixing epsilon=1/2 yields a linear feasibility test; minimizing epsilon>=0 yields **e_B** itself.

**Corollary (rational finite-box attainment).** For every finite integer B, e_B is rational and attained by a globally defined F7-admissible q that can be chosen rational-valued, equal to the baseline outside a finite evenness-closed coordinate set. This strengthens r475's finite-box argument; r475 independently gives global attainment and m=lim e_B, without claiming that the infinite-domain optimum is rational.

## Exact proof

Write r=a-b, t=a-2b and u=c-d, s=c-2d. The inverse integer map is (a,b)=(2r-t,r-t). For fixed r, the constraint |a|,|b|<=B is equivalent to t∈T_r. The r471 identity is

    D_q(a,b,c,d) = F_{r,u}(s)-F_{r,u}(t).

For r=u this is identically zero. Exchanging the first input pair with the second leaves D_q unchanged, so it suffices to take r<u.

For a fixed r<u, all possible (a,b,c,d) are exactly the independent choices t∈T_r and s∈T_u. Suppose |D_q|<=epsilon for all of them. Let L=min_{t∈T_r}F(t) and U=max_{t∈T_r}F(t). Then L<=F(t)<=U. The cross-pair inequalities give, for every s∈T_u,

    F(s) >= max_{t∈T_r}F(t)-epsilon = U-epsilon,
    F(s) <= min_{t∈T_r}F(t)+epsilon = L+epsilon.

Thus (1)–(2) hold. Conversely, if (1)–(2) hold, then for every t∈T_r, s∈T_u,

    F(s)-F(t) <= (L+epsilon)-L = epsilon,
    F(t)-F(s) <= U-(U-epsilon) = epsilon.

Hence |D_q|<=epsilon for all four-input tuples. No relaxation occurred.

There are 4B+1 possible r, and sum |T_r|=(2B+1)^2, because (r,t) bijects with the (2B+1)^2 possible (a,b). For each unordered r<u there are 2|T_r|+2|T_u| inequalities. Summing over all unordered pairs counts each |T_r| exactly 4B times, giving 8B(2B+1)^2.

Only finitely many q values occur in this system. Every solution to the restricted scalar conditions extends to a globally admissible q by preserving each prescribed (|x|,y) value, and taking the baseline q(0,0)=0, q(x,0)=1 for x≠0, q(x,y)=1/2 otherwise. Thus the finite system tests the **same original global class A**. It is a nonempty rational polyhedron for epsilon sufficiently large (baseline has E_infty=1). The objective epsilon is bounded below by zero, so the standard rational linear-programming attainment theorem produces a rational optimal feasible assignment and rational e_B. The finite-to-global baseline extension then gives a globally defined rational q attaining e_B. QED.

## Reproducible generator, tests and actual computation status

The source checker constructs the inequalities using the integer-scaled values Q=4q and epsilon4=2, treating axis/origin and both marks as fixed constants, sharing the same variable across x and -x. It uses only the two interval bounds L,U for each unordered r,u.

- B=14: 1,596 unordered pairs, 3,192 auxiliary variables, **94,192 inequalities**; the pre-existing frozen r469 witness already proves epsilon=1/2 feasible.
- B=15: 1,830 unordered pairs, 3,660 auxiliary variables, **115,320 inequalities**. Actual sparse matrix build generated **4,730 free q coordinates and 340,040 nonzeros**. The original 31^4=923,521 quadruples would give 1,847,042 signed inequalities. Thus the exact reformulation cuts the inequality count by about **16.0 times**, with auxiliary variables added.
- Independent direct-quadruple versus pair-fiber exact integer oracles agreed for B=1,2,3,4, with sampled integer data and maxima in quarter units 4,5,5,5 respectively. The previous local matrix generator solved B=2 and B=3 numerically at epsilon4=2 with largest residual 0 and 4.44e-16 respectively. This tests the formulation and small-box feasibility but is not rational certification.
- Numerical HiGHS exploration of the full B=14 formulation hit a 20-second solver limit without a conclusion. The B=15 attempt also did not return a conclusive solver status before its process timeout. **No B15 feasibility, infeasibility, or exact e15 claim follows from these timeouts.**

Reproducer: research_checks/CBRC_F7_R476_FINITE_FIBER_EXTENDED_LP_20261122.py. Matrix construction is integer-exact; a successful float solver run must be rationalized and the entire sparse inequality system checked with exact arithmetic to become a mathematical witness. An infeasibility claim requires an exact dual/Farkas certificate or another proved obstruction.

## Scientific and operational significance

The original B15 all-variable half-error question has an exact O(B³)-inequality LP formulation, rather than requiring the 923,521 quadruple constraints to be explicitly materialized. The next constructive unit is to obtain a rational B15 primal or a verified dual witness using this formulation, with targeted numerical preconditioning/cutting planes as optional search methods. This is a new computational structural step, not proof that e15=1/2 or e15>1/2.

Source dependencies: r471 fiber identity at enterprise-math@013c38ab95d45a1c5fc6f3e583d6e62e688395f7; r475 finite-box compactness at enterprise-math@22909ee4fa32737595c5422d683aec956a96346d. The exact original scalar conditions and author contributions remain unchanged.

New proved subunit: 1 (theorem + rationality corollary). Native Review admitted 0, Result admitted 0, Task completed 0, parent objective completed 0. No owner reassignment, native CLAIM, secret exposure or scheduling change.
