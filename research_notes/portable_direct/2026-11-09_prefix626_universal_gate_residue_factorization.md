# PREFIX-626 — Universal four-residue gate factorization for native X6-BRC

2026-11-09 (Asia/Shanghai). Author-side exact proof and executable certificate; independent Driver review pending. Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Researcher EM-X6-E90CA6; activity RA-DBF18FC5261DB71FA7124AE9. Extends PREFIX-623–625 without changing P000 or the source firewall.

## Exact native scope

Use the original 48 STAR phases, 96 two-bit ports, 576 ordered source-labelled BRC actions, weights (1,1,1,1,0,0), and special target phase G=4. A(g) is the original destination-summed 96×96 native action transition under gate g≥0. For any nonnegative predecessor port vector r, the terminal output is F_n r, where F_n=A(g_n)...A(g_1). The complete source-/action-labelled path history is a separate observer. A=A(0), E=A(1)-A(0). All matrix products here are exact compositions of this original BRC operator.

## Theorem 626.1: rank-one gate feedback with period four

Direct original action enumeration yields E=u v^T, with u=e_7+e_29+e_31 and v=e_9 (zero-based ports). E has exactly three ones at (7,9),(29,9),(31,9) and E²=0. Exact finite 96-component identities:

- A⁵u=12Au, and v^T A⁵=12v^T.
- v^T A^k u for k=0,1,2,3,4 equals (0,0,0,4,0).
- The supports of A^h u for h=1,2,3,4 are six-element, mutually disjoint sets; the supports of v^T A^h have the same property.

It follows for every integer k≥0 that

c_k=v^T A^k u = 4·12^((k-3)/4) when k≥3 and k≡3 (mod 4), and c_k=0 otherwise.

In particular, E A^k E=c_k E. The recurrence c_(k+4)=12c_k for k≥1 follows immediately from the finite identities; its k=0 instance follows by the stated base values. The vector support laws persist modulo four because every future four-step iterate is 12 times the previous one once h≥1.

## Theorem 626.2: exact four-product factorization of the entire endpoint operator

For n≥2 and interior residue classes r∈{0,1,2,3}, define

I_r={j : 2≤j≤n−1 and j≡r (mod 4)},  P_r=∏_(j∈I_r)(1+g_j/3).

An empty product is 1. For any nonempty I_r choose any j∈I_r and define B_(n,r)=A^(n-j) E A^(j-1); set B_(n,r)=0 for an empty class. B_(n,r) is independent of the choice of j, by the two four-step Krylov identities. Put D_n=4·12^((n−5)/4) E when n≥5 and n≡1 (mod 4), and D_n=0 otherwise.

Then the following **full 96×96 matrix identity** holds for every finite n≥2 and arbitrary real gate values (in particular all admissible nonnegative gates):

F_n = A^n + 3 Σ_(r=0)^3 (P_r−1) B_(n,r)
      + g_1 P_1 A^(n−1) E
      + g_n P_(n mod 4) E A^(n−1)
      + g_1 g_n P_1 D_n.

Proof. Expand the ordered product ∏_(j=n)^1(A+g_j E). The coefficient associated with selected indices 1≤j_1<...<j_m≤n is

A^(n−j_m) u [∏_(a=1)^(m−1) c_(j_(a+1)−j_a−1)] v^T A^(j_1−1).

This vanishes unless every selected gate index lies in a **single residue class mod four**, by Theorem 626.1. For a nonempty selection of m interior gate indices in the same class, the coefficient is 3^(1−m) B_(n,r), using the 12-fold four-step recurrence and c_(4l−1)=4·12^(l−1). Summing all nonempty subsets produces 3(P_r−1)B_(n,r). Selected sets containing gate 1 but not n contribute g_1 P_1 A^(n−1)E; sets containing gate n but not 1 contribute g_n P_(n mod 4) E A^(n−1). Both endpoint gates can occur together precisely when n−1 is a positive multiple of four, producing g_1g_nP_1D_n. These exhaust all subsets and prove the identity.

**Universal operator equivalence:** for fixed horizon n and identical boundary gates (g_1,g_n), two interior histories with identical P_0,P_1,P_2,P_3 have the *same full 96×96 endpoint operator*, hence the same terminal ports for **every** initial input. In particular, permuting interior gate values at positions in the same residue class leaves the complete endpoint operator unchanged. Four exact scalar product accumulators suffice to encode the variable interior dependence for a fixed-horizon operator, in addition to boundary gates and horizon-specific fixed matrices. Bit complexity and output reconstruction costs remain part of algorithmic assessment.

## Theorem 626.3: all four products are complete when boundary gates vanish

If g_1=g_n=0, then F_n=A^n+3Σ_r(P_r−1)B_(n,r). For each active r, B_(n,r)=(A^(n−j)u)(v^T A^(j−1)) has exactly 36 nonzero entries: both exponents are ≥1 and each factor has exactly six nonzero coordinates. The four active B_(n,r) have pairwise disjoint matrix-entry supports, because the column factor A^(n−j)u lies in a support class determined by (n−j) modulo four and the four support classes are disjoint.

Consequently, with zero boundary gates and fixed n≥2:

F_n(g)=F_n(g') **if and only if** P_r(g)=P_r(g') for every nonempty class I_r.

When n≥6, all four classes occur. Their product values vary independently on the nonnegative domain by changing one interior gate per class; the four-product description is therefore nonredundant for this operator observation.

## Exact source-labelled witness

Let n=10 with 1-based gate histories

alpha=(0,1,0,0,0,2,0,0,0,0)
beta =(0,2,0,0,0,1,0,0,0,0).

Both have P_2=(1+1/3)(1+2/3)=20/9 and P_r=1 for r≠2; therefore F_10(alpha)=F_10(beta) **as 96×96 operators**. However, from unit initial source port 22 the legal ten-action path

22→9→29→80→52→8→28→80→52→8→28

has action labels (i,j,u,v), in order:
(4,11,1,0); (14,4,1,1); (40,14,0,1); (26,40,0,0); (4,26,0,0); (14,4,0,0); (40,14,0,0); (26,40,0,0); (4,26,0,0); (14,4,0,0).

All path weights except the second equal one; at step two the original gate weight equals g_2. The **tagged-path masses are 1 under alpha and 2 under beta**, while every terminal 96-port output is identical. Thus the operator quotient forgets within-residue action timing; a specified ordered path query retains it.

## Execution, verification and status

The standalone native checker reconstructs the original 48-phase STAR adjacency and all 576 typed actions; verifies the rank-one gate positions, complete finite Krylov recurrences, disjoint four-class supports and feedback values by exact SymPy integer/rational arithmetic; compares the formula against **22 full 96×96 exact matrix products** at 11 horizons n=2,3,4,5,6,7,8,9,10,13,17 with rational and zero gates; and checks the gate-swap full-operator collision plus ten-action positive path witness. All executed assertions passed. The all-horizon theorem is supported by the exact finite recurrence certificate and general coefficient expansion, not by extrapolating the tests.

Model scope: original native positive typed BRC action operator, full destination-summed 96-port output, arbitrary predecessor port vectors and nonnegative gates. The source-labelled path observation uses original ordered labels. Exact theorem source and certificate here are author-side research, **unreviewed**; this write creates no CLAIM, Native Result, Foundation admission or physical calibration.

Next: find minimal extra online memory for selected bounded-lag tagged-path queries when only the four products and boundary information are retained; compare original sequence, moments and explicit path-expansion bit costs. Specialize the resulting memory law to the fixed four-point probe reachable family.

Prior related evidence: PR #1864 PREFIX-623, PR #1868 PREFIX-624, PR #1869 PREFIX-625; original native action enumerator in PREFIX625_native_two_generation_path_checker.py at PR #1869. Research identity and current task owner are verified separately in the native Source control state.
