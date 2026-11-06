# D25 — Triple-carry filtration, signed observer kernel, and Clausen third jet

Date: 2026-11-06. Lane: TASK_RESEARCH, portable author-side. Mathematical status: AUTHOR-DERIVED EXACT ALGEBRA; 428-PRIME FINITE EXACT CHECK; UNREVIEWED; NOT_ADMITTED; NOT_NATIVE_CHECKPOINT.

Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific input pin c47e13e4aba0e006366f989d6334d443f6333ae3. The previous D25 single-carry shell and Clausen first/second-jet formulas are inherited, not credited again.

## 1. New exact double/triple carry theorem

Let q >= 5 be prime. Put epsilon=1 if q=1 (mod 6), epsilon=-1 if q=5 (mod 6); set m=(q-epsilon)/6 and delta=(1-epsilon)/2. Then a=2m-delta, b=3m-delta, c=4m-delta satisfy 0<=a<b<c<q. Work in F_q[[t]], j in [0,q-1].

Define

    M_j(t) = (-1/2)^j * (j!/(1-3t)_j)
             * binom(a+t,j)*binom(b+t,j)*binom(c+t,j),

where (x)_j is a rising factorial. Put

    ell(j) = 1_{j>a} + 1_{j>b} + 1_{j>c}.

**Theorem:** ord_t M_j(t) = ell(j), and the first nonzero Taylor coefficient is

    [t^{ell(j)}] M_j(t) = (-1/2)^j product_{s in {a,b,c}} beta(s,j),

    beta(s,j) = binom(s,j)                          if j<=s;
              = (-1)^{j-s-1} s!(j-s-1)! / j!        if s<j<q.

All the displayed beta factors are nonzero in F_q. Thus the exact four shells are: regular 0<=j<=a (order 0); single carry a<j<=b (order 1); **double carry b<j<=c (order 2)**; and **triple carry c<j<q (order 3)**.

**Proof:** For j>s, binom(s+t,j) contains exactly one factor t, with the other factors multiplying to (-1)^{j-s-1}s!(j-s-1)!/j!. If j<=s the constant term is binom(s,j). All factorials with arguments <q are units modulo q, and the prefactor j!/(1-3t)_j has unit constant 1. Multiplying the three independent factors gives the exact valuation and nonzero leading coefficient.

## 2. Exact signed weighted observer-kernel witness

For the D25 readout w_j=6j+1, there is exactly one index j_* in 0<=j<q with w_{j_*}=0 modulo q. Its shell is given by

    (j_*,ell(j_*)) = (m,0)       if q=6m+1;
                    (5m-1,3)   if q=6m-1.

Indeed 6 is a unit modulo q, so the root is unique, and substituting each expression verifies w_{j_*} is a multiple of q and locates the shell. At j_* the unweighted leading source coefficient is nonzero. Therefore **weighted summation erases this labelled source coordinate**, including a regular-shell coordinate in the D25 target prime class q=13,19 (mod 24), or a triple-carry coordinate in q=5 (mod 6). Preserve (j_*,ell(j_*),[t^ell]M_{j_*}) as a repair coordinate for subsequent coefficientwise and derivative observations. The population and operation are exactly the labelled j-shell jets and weighted aggregation; no positive-mass BRC replacement is asserted.

## 3. New third-jet Clausen defect and source support horizon

Define the Clausen companion with the same numerator polynomial:

    C_j(t) = (-1/2)^j *
             product_{s in {a,b,c}} product_{r=0}^{j-1}(s+t-r)
             / (j! * (1-t)_j * (1-2t)_j).

Then M_j(t)=R_j(t)C_j(t), where R_j has unit constant and is well-defined even when C_j(0)=0:

    R_j(t) = (1-t)_j(1-2t)_j / (j!(1-3t)_j)
           = 1 + 2 H_j^(2) t^2 + 6 H_j^(3) t^3 + O(t^4),

    H_j^(r) = sum_{h=1}^j h^(-r) in F_q.

Consequently the **third Taylor coefficient correction** is exactly

    [t^3](M_j-C_j) =
        2 H_j^(2) [t]C_j + 6 H_j^(3) C_j(0).

Moreover ord_t(M_j-C_j) >= ell(j)+2. Thus all double-carry terms agree with their Clausen companions through t^3, and all triple-carry terms agree through t^4. At order t^3 the possible disagreement is confined to regular and single-carry shells.

**Proof:** For each 1<=h<=j, form (1-t/h)(1-2t/h)/(1-3t/h). Expanding its logarithm to cubic order and summing over h gives the t^2 coefficient 2H_j^(2) and the t^3 coefficient 6H_j^(3), with zero linear coefficient. As q>=5 the needed constants 2 and 3 and h are units. Multiply by C_j, which has t-order ell(j), to obtain the coefficient identity and vanishing horizon.

## 4. Independent exact finite-field checks

The accompanying Python script computes the degree<=3 Taylor jets via *two separately specified rational recurrences* for M_j and C_j. It also computes each first-nonzero coefficient from a precomputed factorial/inverse-factorial product, checks all j, the exact unique weighted kernel, and the second/third Clausen corrections. Executed over all **428 primes from 5 to 3000**: **428/428 PASS**. All operations are exact modulo q.

Selected E3 = sum_{j<q}(6j+1)([t^3]M_j-[t^3]C_j), reduced modulo q:

| q | E3 | lost coordinate (j_*,ell) |
|---:|---:|---|
| 13 | 9 | (2,0) |
| 19 | 5 | (3,0) |
| 373 | 310 | (62,0) |
| 1009 | 947 | (168,0) |
| 2999 | 168 | (2499,3) |

The original W_q/q, native original-class H0/B0 experiment, [X]U modulo 373^2, Frobenius normalization eta/kappa, and independent review remain open at this specific author-side source.

## 5. Next scientific step

Use the labelled double/triple shell coefficients and the unweighted kernel repair to form a source-preserving candidate finite telescope for the outstanding Gauss-jet Theta_q cancellation, separately for G=0 and G!=0. Check the exact formulas at q=13,19,373 and then pursue the general prime class. The unchanged frozen mother objective is Delta_p-R_p=0 mod p for p=13,19 mod 24.

BRC resolution: COMPOSE_APPLIED to signed labelled shell/provenance and observer-safe quotient; no positive-weighted BRC engine run. This evidence is durable author-side mathematical progress, not an authorized native Source checkpoint or Result.
