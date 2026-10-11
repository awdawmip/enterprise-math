# A terminating parameter jet fixes the second-digit boundary by finite harmonic sums

Status: READONLY_MATHEMATICAL_PREPARATION / NOT_EXECUTED / NOT_REVIEWED.
No finite regression, native Task claim, execution, remote write, or provider query
was performed for this draft. The formulas below are derived from the already
proved coefficientwise mod-p² comparison and characteristic-zero quadratic
identity. They are candidates for independent review and bounded execution.

## 1. The independently defined scalar

Let p=6m+1 be prime, m≥1. Put

    q₂ = (2^(p−1)−1)/p,
    S₂ = Σ[k=0..m−1] 1/(6k+2),
    T_r = Σ[k=0..m−1] 1/(6k+r)²,  r∈{2,3,6}.

Every displayed denominator is a p-unit. The known mod-p² quadratic comparison
implies −3S₂−q₂∈p Z_(p); section 4 gives the precise deduction. Define

    B_p = (2/9) * {
              (−3S₂−q₂)/p + q₂²/2 − 3T₆ + 12T₃ + (33/2)T₂
          } mod p.                                             (HB)

This is an explicit finite harmonic/Fermat scalar. It is not the difference
quotient of the two Task values. To compute it, S₂ and q₂ require mod-p²
precision; T₂,T₃,T₆ require only mod-p precision. Obtain q₂ mod p² by
computing 2^(p−1) mod p³ and taking the exact Fermat division. For the first
division in (HB), reduce −3S₂−q₂ mod p² into p Z/p² Z, then divide by p.
No arbitrary lift or choice of period multiplier occurs.

If the parent investigator's independent residual derivation is verified, (HB)
fixes its one free initial coefficient J₀=B_p in

    (j+1)² J_{j+1} − (j+1/3)(j+2/3) J_j = −2/9,
    0≤j≤p−3,    deg J≤p−2.                                     (REC)

The correction then is

    f_p(4x(1−x)) − L_p(x) = p² x^p J(x) mod p³,                 (CORR)

and at the exact Task lifts x±=(2±√2)/4, under inherited CM0,

    g_p/p = L_p(x±)/p + p*x±^p*J(x±) mod p².                    (DIGIT3)

Only x±^p mod p is required in the second term. On the Task classes 13,19
mod 24 this is 1−x± mod p. This residue-field observation does not replace the
exact lift in L_p(x±)/p and does not assert that literal p-th powering is the
lifted Frobenius mod p².

The residual and (REC) were supplied by the parent investigator and have not
been independently checked in this preparation. The independent result here
is the candidate formula (HB) for the initial coefficient, proved algebraically
below. It can also be used without (REC): it equals the coefficient of x^p in
the polynomial (f_p(4x(1−x))−L_p(x))/p² modulo p.

## 2. The parameter family that actually has c=1

Write

    A(t)=1/6−t/6,       B(t)=1/3+t/6,
    C(t)=1/3−t/3,       D(t)=2/3+t/3.

The opposite shifts preserve A+B=1/2 and C+D=1. Hence the exact formal
quadratic identity is

    ₂F₁(A(t),B(t);1;4x(1−x)) = ₂F₁(C(t),D(t);1;x).             (Q(t))

At t=p, A=−m and C=−2m; both sides terminate and (Q(t)) is an exact
polynomial identity of degree 2m. This is the family corresponding to the
suggested Hesse parameters (−2m, 2/3+p/3).

The alternative same-direction Gauss pair (−m,−2m) cannot be placed into
(Q(t)) with c=1. Its correct quadratic family is

    A=(1−t)/6, B=(1−t)/3, c=1−t/2,
    Hesse parameters ((1−t)/3, 2(1−t)/3; 1−t/2).

That family is valid too, but changes the denominator parameter and therefore
adds its own harmonic terms. Silently retaining c=1 would be an incorrect
quadratic transformation.

For completeness, the general transformation follows by the differential
equation when c=A+B+1/2. With w=4x(1−x), the pullback of the Gauss operator
is four times the Hesse operator with parameters (2A,2B;c). Both formal
solutions have constant coefficient 1 and the same recurrence. This proves
(Q(t)) over Q(t)[[x]] without a truncation exchange.

## 3. Integral jets and all factor-entry boundaries

For n<p, define coefficient polynomials

    G_n(t) = Π[j=0..n−1](6j+1−t)(6j+2+t) / (36^n(n!)²),
    H_n(t) = Π[j=0..n−1](3j+1−t)(3j+2+t) / (9^n(n!)²).

Their coefficients lie in Z_(p), because n!, 3 and 6 are units. Let
G(t;w)=Σ[n<p]G_n(t)w^n and H(t;x)=Σ[n<p]H_n(t)x^n.
Then G(0;w)=f_p(w), H(0;x)=L_p(x), and G(p;q)=H(p;x) exactly.
Taylor expansion of these finite coefficient polynomials gives

    f_p(q)−L_p(x)
      = −p*(G_t(p;q)−H_t(p;x))
        + p²/2*(G_tt(p;q)−H_tt(p;x)) mod p³.                    (JET)

Higher Taylor terms lie in p³ Z_(p)[x]. This assertion uses polynomial
coefficients, not rational harmonic expressions that might contain 1/p.

Here is an explicit denominator-safe description of each jet. It covers both
families with k=6, N=m, M=2m, denominator 36^n(n!)² for G, and k=3,
N=2m, M=4m, denominator 9^n(n!)² for H. At t=p put

    U_j=k(j−N),        V_j=kj+2+p.

The first exact zero is U_N=0. The unique additional p-divisible factor is
V_M=3p. Their entry indices are n=N+1 and n=M+1, respectively.

If n≤N, every factor is a unit. For C_n=ΠU_jV_j/denominator and

    h_n=Σ(−1/U_j+1/V_j),
    e_n=Σ(1/U_j²+1/V_j²),

the two jets are C_n*h_n and C_n*(h_n²−e_n).

If N<n≤M, omit U_N from the product to obtain a p-unit R_n. Omit
that same zero factor from the h_n sum. Then

    coefficient(p)=0,  coefficient_t(p)=−R_n,
    coefficient_tt(p)=−2R_n*h_n.

If n>M, omit BOTH U_N and V_M to obtain a p-unit R_n. All terms
in h_n, with those two factors omitted, are units. Writing δ=t−p,

    coefficient(t)=−δ*(3p+δ)*R_n(t),
    coefficient_t(p)=−3p R_n,
    coefficient_tt(p)=−2R_n−6p R_n*h_n.

In particular coefficient_tt(p)=−2R_n mod p, and the original
coefficient at t=0 satisfies

    coefficient(0)/p² = 2R_n mod p.                            (DOUBLE)

No term of the form 0*(1/0) or p*(1/p) was used. The factor-entry equalities
have been treated exactly before forming harmonic sums. At n=p the
denominator ceases to be a unit; section 4 handles that single boundary
coefficient separately by exact cancellation of both p factors.

The jets therefore do supply a structural p³ correction, but they do not
remove the high-degree cutoff data by themselves. For the coefficient x^p,
only Gauss indices n≥ceil(p/2)=3m+1 occur. They are all in the DOUBLE
layer, so the harmonic jet terms disappear and (JET) gives precisely the
same beta-type boundary sum as a direct high-tail expansion. A separate
boundary simplification is necessary; section 4 supplies it.

## 4. Derivation of the finite harmonic boundary

Let a_p,b_p denote the index-p coefficients of the INFINITE characteristic-
zero series, not a new term in either finite Task polynomial. Coefficient
extraction from the exact quadratic identity gives

    [x^p](f_p(q)−L_p(x)) = b_p − 4^p a_p.                      (BOUND)

Indeed, terms n>p cannot contribute to x^p and the only omitted Gauss term
n=p contributes 4^p a_p. The finite Hesse polynomial has no x^p term.

In a_p the numerator factors divisible by p are exactly p in (6j+1)
at j=m and p in (3j+1) at j=2m. In b_p they are p at j=2m
and 2p in (3j+2) at j=4m. Their p² cancels exactly against the
two factors of p in (p!)². All remaining factors are units, and permutation
of the nonzero residue classes gives

    a_p = 1/18 mod p,    4^p a_p = b_p = 2/9 mod p.             (UNIT)

The exact unit ratio is

    R=b_p/(4^p a_p)
      =2^(1−p) * Π[j=0..p−1,j≠4m](3j+2)
                    / Π[j=0..p−1,j≠m](6j+1).                 (RATIO)

For each residue r=1,...,p−1, the corresponding numerator and denominator
factors in (RATIO) are respectively r+pκ_B(r) and r+pκ_A(r), with

    κ_A(r) = least nonnegative (1−r) mod 6,
    κ_B(r) = least nonnegative (2−r) mod 3.

The bounds 0≤κ_A≤5 and 0≤κ_B≤2 ensure that these are exactly the factors
in the displayed products, not merely congruent replacements. Put

    V₁=Σ[r=1..p−1](κ_B(r)−κ_A(r))/r,
    V₂=Σ[r=1..p−1](κ_B(r)²−κ_A(r)²)/r².

Multiplying integral unit products and expanding to precision p³ yields

    R = 1 + p(V₁−q₂)
          + p²*((V₁²−V₂)/2 − q₂V₁ + q₂²) mod p³.             (EXP)

The previously proved mod-p² polynomial comparison says that (BOUND) lies
in p² Z_(p). By (UNIT), R−1 lies in p² Z_(p), so V₁−q₂∈p Z_(p).
Consequently

    (R−1)/p² = (V₁−q₂)/p + (q₂²−V₂)/2 mod p.                (SCALAR)

Pair residues r and p−r. The six residue-class values of κ_B−κ_A,
for r mod 6 equal to 1,2,3,4,5,0, are

    1, −5, −2, −2, −2, 1.

The corresponding values of κ_B²−κ_A² are

    1, −25, −12, −8, −4, 3.

Using the representatives r=6k+2, 6k+3 and 6k+6, each k=0,...,m−1,
their partners have residues 5,4 and 1. Since

    1/(p−r)=−1/r−p/r² mod p²,

we obtain

    V₁ = −3S₂ + p*(−T₆+2T₃+2T₂) mod p²,
    V₂ = 4T₆−29T₂−20T₃ mod p.

This proves −3S₂−q₂∈p Z_(p). Substitution into (SCALAR), then multiplication
by the known unit 4^p a_p=2/9 mod p, proves (HB) and (BOUND)/p²=B_p.
In particular the scalar is independent of x, of the two CM branches, and of
the value sought for the UR identity. It comes from a fixed coefficient
boundary and explicit integer residue carries.

## 5. What the candidate buys, and what it does not

The parameter family is a precise organizing argument, rather than a claim
that arbitrary terminating parameters preserve the original quadratic
identity. Its second jets still reach the full cutoff. The harmonic boundary
(HB) replaces one beta sum by m-term reciprocal sums and a Fermat quotient;
it fixes the homogeneous ambiguity in a simple inhomogeneous Hesse equation.
There is no asymptotic improvement over an optimally evaluated O(p) beta sum
or the O(p) recurrence (REC), but the constant-size collection of harmonic
sums is a different independently evaluable scalar carrier. It does not
require evaluating the two Task polynomials and dividing their difference.

The correction, if independently verified, transports the second divided
digit across the finite Gauss/Hesse cutoff. It does not prove UR or LIFT,
identify the raw oriented period normal, or solve the separate period-gauge
calibration problem. CM0 is inherited only when dividing by p in (DIGIT3).
The branch derivative and coordinate Jacobian must remain tagged as in unit16.

Recommended bounded execution after the formal route is ready: compare the
independently computed harmonic B_p against the beta boundary coefficient,
then verify (REC) and the two exact-lift identities (DIGIT3) for a few primes
including 7 and both Task classes. Include the old p=13 pointwise counterexample
as a negative check of the uncorrected formula. No such regression has been
run in this preparation, and no claim of final mathematical acceptance is made.

Read input: CM24_QUADRATIC_MOD_P2_TASK_LIFT_PROOF.md from the existing
published-source-full-bytes directory, especially sections 2,3,4 and 7.
Author: subagent /root/number_theory_next_unit/hypergeometric_parameter_jet,
finite readonly preparation under the parent investigator's assignment.
