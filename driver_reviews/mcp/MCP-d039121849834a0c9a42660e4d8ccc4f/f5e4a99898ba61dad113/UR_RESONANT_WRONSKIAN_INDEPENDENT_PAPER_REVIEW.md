# Independent paper review of the CM first-digit resonant boundary

Verdict: PASS for the displayed construction, resonant Wronskian identities,
both endpoint proofs and exact reduction to UR-SUM. No error was found in
the reviewed final bytes. UR-SUM itself remains unproved; this review does
not assert UR, LIFT or the mathematical mother goal complete.

Exact full-read input is
/workspace/em-owner-resume-20261011/cm24-ur-adjoint-frontier-20261011/CM_FIRST_DIGIT_RESONANT_WRONSKIAN_BOUNDARY_PREPARATION.md,
9663B, SHA256 ebddef65d87c32ff73901635f782596f4c33d9fe64e797ad96c1aed1ca95f970,
Git blob 110396185dd9425031596762ac1f1f865ac750e5.
Root requested this one local review and handoff. It uses my existing
identity EM-ENTERPRISE-3F2857, activity RA-C05628958AD19A1F120F685E and
session MCP-ed8b0698b5554016b829bddd5759a204. No new Task claim, Source write,
numerical calculation, old campaign or provider query was performed.
The author's formulas were exposed before review; this is directed,
shared, nonblind paper verification, not an implementation-independence
claim or formal DR acceptance. All previously frozen artifacts are unchanged.

## 1. The exact divided constructor and its precision

The preceding transport supplies M=f_p mod p^2 coefficientwise and the
exact independent M residual D_G M=0 mod p^2. The chosen V_lift is
precisely sum_(n=0)^m a_n w^n with a_n=(1/6)_n(1/3)_n/(n!)^2, not a
different lift of the residue polynomial. Therefore W=(M-V_lift)/p mod p
has zero coefficients through m and coefficients a_n/p for m<n<=2m.
For n>2m the two numerator p factors kill the quotient modulo p.
The top coefficient W_(2m) is nonzero, so W has degree exactly 2m.

For the exact cutoff at m,
(m+1/6)(m+1/3)=(p/6)((p+1)/6). The top residual is consequently
-p(p+1)a_m w^m/36; all lower coefficients cancel by the exact a recurrence.
After subtracting from D_G M and dividing by p this gives

    D_G V=0,       D_G W=(v_m/36)w^m.

This division is coefficientwise in p-integral rational arithmetic and is
justified independently of any target value. At the CM point c=1/2,
CM0 gives p|V_lift(c), so rho=V_lift(c)/p mod p exists. It does not
give divisibility by p^2 or rho=0. Evaluation commutes with the already
justified coefficient division because 2 is a unit. Thus

    M(c)/p=rho+W(c) mod p,
    U_0=6[rho+W(c)]V'(c) mod p.

Only the first digit is studied here: rho requires the exact V_lift value
through p^2. This paper does not replace the p^3 M precision needed by
the later divided second-digit product. The conceptual failure of deleting
rho is correctly stated; no numerical counterexample was run in this review.

## 2. The integrating factor and the genuine degree-p term

For a=w(1-w) and mu=(1-w)^(3m), the residue relation -3m=1/2 gives

    (a mu)'=mu(1-3w/2),
    mu D_G y=(a mu y')'-(mu/18)y.

These are polynomial identities, even though logarithmic differentiation
is a convenient way to check them. For the specified ordering

    Q=a mu(VW'-WV'),

the derivative is mu[V D_G W-W D_G V], with no reversed sign. Hence

    Q'=(v_m/36)w^m(1-w)^(3m)V.

The forcing has degree 5m, and its zero-constant coefficient primitive P
has degree 5m+1<p. All integral denominators lie between m+1 and 5m+1,
which are units for every m>=1. However Q's prefactor has degree 3m+2
and its Wronskian degree 3m-1, allowing total degree p=6m+1. Therefore
Q-P may contain a multiple of w^p, whose derivative is zero.

More precisely, a derivative-zero polynomial of degree <=p is constant
plus lambda w^p. Q(0)=P(0)=0 removes the constant; the actual factor
(1-w)^(3m+1) gives Q(1)=0 and fixes lambda=-P(1). Thus

    Q=P-P(1)w^p.

The endpoint at one is genuine for this weighted Q. It is distinct from
the earlier flat-adjoint K, for which no condition K(1)=0 was imposed.
Replacing Q by P would remove a real resonant term and change the CM result.

## 3. Endpoint proof by exact leading coefficients

The coefficient products reduce to

    v_m=(2m)!/(m!)^2,
    W_(2m)=(-1)^m m!(m-1)!/[6(2m)!] mod p.

For the latter, the single p/6 factor in (1/6)_(2m) occurs at index m;
after dividing by p its other factors give (-1)^m m!(m-1)!, while
(-2m)_(2m)=(2m)!. All factorial denominators are units. The leading
Wronskian coefficient is (2m-m)v_m W_(2m). Multiplying by the top
prefactor coefficient (-1)^(3m+1) gives

    [w^p]Q=(-1)^(3m+1)m v_m W_(2m)=-1/6.

This is nonzero: Q in fact has degree exactly p. Since deg P<p,
comparison with Q=P-P(1)w^p proves

    P(1)=1/6,       Q=P-w^p/6.

This proof neither evaluates a CM quantity nor consumes UR or OLD-R.
It also covers the smallest prime p=7,m=1, with integral degree 6<p=7.

## 4. Independent endpoint proof by terminating summation

Expanding V with t_k=binom(m,k)binom(2m,k), coefficientwise beta
integration gives

    int_0^1 w^m(1-w)^(3m)V dw
    =m!(3m)!/(4m+1)!
       * 3F2(-m,-2m,m+1;1,4m+2;1).

Every beta factorial index is at most 5m+1<p. The second lower parameter
4m+2 is congruent to 1-2m, and its rising products through k=m are units.
Saalschutz applies with a=-2m, b=m+1, n=m, c=1; the required second
lower parameter is 1+a+b-c-n=1-2m. Its finite quotient is exactly

    (-1)^m (3m)!(m-1)!/[(2m)!(2m-1)!].

No terminating denominator vanishes. Multiplication by v_m/36 gives

    P(1)=(-1)^m(3m)!^2/[36m(4m+1)!(2m-1)!].

Wilson supplies (4m+1)!(2m-1)!=1 and
(3m)!^2=(-1)^(3m+1). Thus the numerator is -1, and m=-1/6 gives
-1/(36m)=1/6. The signs, factorial ranges and normalization agree with
the first proof. The first proof remains self-contained without importing
the terminating summation theorem.

## 5. CM sign, retained rho and the still-open finite sum

For the two target classes (2/p)=-1, and 3m=(p-1)/2, so mu(c)=-1.
Since V(c)=0,

    Q(c)=-(mu(c)/4)W(c)V'(c)=W(c)V'(c)/4.

Using c^p=c and the proved endpoint yields

    6W(c)V'(c)=24P(c)-2,
    U_0=6rho V'(c)+24P(c)-2.

Therefore UR, namely U_0=1 mod p, is exactly

    6rho V'(c)+24P(c)=3 mod p.

The constant -2 in the first-digit formula and constant 3 in the remaining
target are both correct. With the memo's E_half binomial integral,
P(c)=(v_m/36)E_half, so 24P(c)=(2/3)binom(2m,m)E_half. Its index
denominators range from m+1 through 5m+1<p. The displayed UR-SUM is
therefore precisely the same remaining equality, not an already established
consequence of evaluating P(1).

Finally, expanding the exact parameters -m+p/6 and -2m+p/3 through
first order gives the negative harmonic coefficient

    j_k=-t_k[(H_m-H_(m-k))/6+(H_(2m)-H_(2m-k))/3].

Every harmonic reciprocal is a unit. Thus the stated constructor
rho=T_m(c)/p+sum j_k 2^(-k) mod p is valid: CM0 justifies the first
division, but does not erase its exact rational quotient. This retained
quotient is the unresolved divided boundary; neither endpoint proof fixes
it or P(c). A succeeding certificate must derive UR-SUM from these fixed
inputs, rather than choose rho to satisfy it.

All requested paper checks pass. The single review file is the entire new
output. Root owns unified Source capture and will provide actual Source
pins before the reviewer updates its own RA event; no remote capture of
this new review is claimed here. The bounded paper review is handed back
to Root, while UR/LIFT and the overall research remain OPEN.

Researcher-ID: EM-ENTERPRISE-3F2857 / RS-ENTERPRISE-CM24-HESSE-INHOMOGENEOUS-P3-TRANSPORT
