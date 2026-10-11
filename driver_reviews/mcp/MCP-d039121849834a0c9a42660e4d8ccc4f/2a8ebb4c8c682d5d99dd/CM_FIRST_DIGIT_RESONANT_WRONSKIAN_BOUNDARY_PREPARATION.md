# CM first digit: a normalized resonant Wronskian boundary

Status: DIRECTED_PAPER_PREPARATION / NO_NEW_TASK_CLAIM / UR_AND_LIFT_OPEN.

Prepared 2026-10-12 00:32:47 Asia/Shanghai (2026-10-11 16:32:47 UTC) by
the delegated `cm24_ur_adjoint_frontier` agent for Root EM-DVR-4C90FB.
This is local paper work authorized by Root, not a continuation of author
EM-ENTERPRISE-CB50ED's closed run, a new Source publication, a numerical
campaign, an independent blind review, or formal Task acceptance. The
immutable sixteen-file RR-AA50A881C6A2DD42BDD3 is unchanged.

Full-read inputs are the author's independent scalar/reverse-Gauss and
finite-adjoint preparations and the independently registered reviewer's
FINITE_ADJOINT_AND_WRONSKIAN_BRIDGE_REVIEW.md. Their byte pins are in the
adjacent INPUT_AND_OUTPUT_PINS.json. The derivation below is different
from the already proved flat-measure C/V adjoint concomitant: it studies
the first divided digit of the symmetric M constructor itself.

## 1. Fixed independent inputs and the divided lift that must remain

Let p=6m+1>=7, and for the CM evaluations restrict p to 13 or 19 mod24.
Keep the already frozen independent symmetric constructor

    S_0(w)=2, S_1(w)=1,
    S_n(w)=S_(n-1)(w)-(w/4)S_(n-2)(w),
    M(w)=(1/2) sum_(n=0)^(p-1) b_n S_n(w),
    b_n=(1/3)_n(2/3)_n/(n!)^2.

The proved descended finite transport gives, coefficientwise,

    M(w)=f_p(w) mod p^2,
    f_p(w)=sum_(n=0)^(p-1) a_n w^n,
    a_n=(1/6)_n(1/3)_n/(n!)^2.

Use the EXACT rational truncation, with its displayed parameters fixed,

    V_lift(w)=sum_(n=0)^m a_n w^n,    V=V_lift mod p.

Define the independent coefficientwise division

    W=(M-V_lift)/p mod p.

For 0<=n<=m the difference between the M coefficient and a_n is divisible
by p^2. For m<n<=2m, a_n contains exactly one numerator p factor; for
2m<n<p it contains two. All denominators n! and 6,3 are units. Hence

    W(w)=sum_(n=m+1)^(2m) (a_n/p mod p) w^n.

In particular W_0=...=W_m=0 and deg W=2m, not just deg W<=2m. No
unknown constant or homogeneous V term is added to W.

Let

    D_G=w(1-w)d^2+(1-3w/2)d-1/18.

The exact finite truncation equation is

    D_G V_lift= -p(p+1)a_m w^m/36.

Indeed the top multiplier is
(m+1/6)(m+1/3)=p(p+1)/36, while all preceding coefficients cancel
by the exact Gauss recurrence. The already proved exact M equation is
D_GM=0 mod p^2. Dividing their difference by p therefore proves

    D_G V=0,
    D_G W=(v_m/36)w^m,        v_m=a_m mod p.

The upper homogeneous polynomial resonance at n=m is resolved by the
zero coefficients through degree m. All these statements are independent
of U, h, OLD-R and a target value at w=1/2.

CM0 supplies V(1/2)=0 mod p. It does NOT supply V_lift(1/2)=0 mod p^2.
The independently fixed divided quantity

    rho=V_lift(1/2)/p mod p

is therefore retained. The first digit of the already frozen scalar is

    U_0=6[rho+W(1/2)] V'(1/2) mod p.

Here M(1/2)/p is rho+W(1/2), and the M(1/2) term in
(M(1/2)/p)(M(1/2)+6M'(1/2)) vanishes modulo p. In particular replacing
U_0 by 6W(1/2)V'(1/2) has no justification.

## 2. The genuine self-adjoint factor and its p-degree resonance

Put

    mu(w)=(1-w)^(3m),          a(w)=w(1-w).

In F_p, -3m=1/2, so

    mu'/mu=1/[2(1-w)],
    (a mu)'=mu(1-3w/2).

The latter is a polynomial identity; the fraction is only a shorthand
for checking the coefficients. Thus

    mu D_G y=(a mu y')'-(mu/18)y.

Define the actual Wronskian polynomial

    Q(w)=w(1-w)^(3m+1)[V W'-W V'].

Its derivative, with its sign fixed by this order of V,W, is

    Q'=(v_m/36) w^m(1-w)^(3m)V(w).                 (A)

The integrand in (A) has degree 5m. Its unique zero-constant ordinary
coefficient primitive

    P(w)=(v_m/36) int_0^w z^m(1-z)^(3m)V(z) dz   (B)

has degree 5m+1<p. Every coefficient division is by an integer between
m+1 and 5m+1, all nonzero modulo p, including m=1.

But Q itself can have degree p: its factor has degree 3m+2 and its
Wronskian has degree 3m-1. Thus Q(0)=0 alone does not identify Q with P.
The derivative-zero kernel in degree <=p is constant+lambda*w^p.
The constant vanishes at zero, and the genuine endpoint Q(1)=0 fixes

    Q(w)=P(w)-P(1)w^p.                            (C)

This is the actual endpoint x-independent normalization. Omitting the
w^p term is an erroneous integration step. This resonance differs from
the earlier C/V flat-adjoint concomitant, whose degree is <p.

## 3. The endpoint is proved to be 1/6; it is not a fitted target

The independent coefficient constructors determine

    v_m=(2m)!/(m!)^2,
    W_(2m)=a_(2m)/p
           =(-1)^m m!(m-1)!/[6(2m)!] mod p.

For the second identity, in (1/6)_(2m) the unique vanishing factor is
p/6 at index m. After division by p the other factors reduce to
(-m)...(-1) and 1...(m-1). The second rising product reduces to
(-2m)_(2m)=(2m)!. All factorial arguments are <p.

The leading coefficient of V W'-W V' is m v_m W_(2m), and the leading
coefficient of w(1-w)^(3m+1) is (-1)^(3m+1). Consequently

    [w^p] Q=(-1)^(3m+1) m v_m W_(2m)=-1/6.

Since deg P<p, comparison with (C) proves the all-prime identity

    P(1)=1/6,       Q(w)=P(w)-w^p/6.              (D)

This normalization uses exact finite coefficients and actual endpoints;
it does not read U, h, a CM value or OLD-R.

There is also an independent finite-sum check of this endpoint using
the terminating Pfaff-Saalschutz identity, which does not consume W.
Modulo p, v_k=binom(m,k)binom(2m,k), and beta integration gives

    int_0^1 w^m(1-w)^(3m)V(w) dw
      = m!(3m)!/(4m+1)!
        * 3F2(-m,-2m,m+1; 1,4m+2; 1).

The second lower parameter 4m+2 is congruent to 1-2m modulo p; its
rising products through k=m are units. Terminating Saalschutz gives

    3F2(-m,-2m,m+1;1,1-2m;1)
      = (-1)^m(3m)!(m-1)!/[(2m)!(2m-1)!].

Multiplying by v_m/36 yields

    P(1)=(-1)^m(3m)!^2/[36m(4m+1)!(2m-1)!].

Wilson gives (4m+1)!(2m-1)!=1 and
(3m)!^2=(-1)^(3m+1) modulo p. As m=-1/6 modulo p, the displayed
expression is again 1/6. All lower factorial and beta denominators are
units. The direct leading-coefficient proof above needs no summation
theorem, so this is supplementary algebraic confirmation.

## 4. The exact remaining CM finite-sum identity

At w=1/2, V=0 and mu(1/2)=2^(-3m)=chi_2(p)=-1 for the two target
classes. Therefore

    Q(1/2)=W(1/2)V'(1/2)/4.

Since (1/2)^p=1/2 in F_p, the properly normalized relation (D) gives

    6W(1/2)V'(1/2)=24P(1/2)-2.

The actual first digit is thus

    U_0=6rho V'(1/2)+24P(1/2)-2.                  (E)

Accordingly the still-open UR theorem is EXACTLY the following identity
between independent fixed finite inputs:

    6rho V'(1/2)+24P(1/2)=3 mod p.               (UR-BOUNDARY)

Equations (A)-(E) and the endpoint P(1)=1/6 are proved here. The
CM-specific last equation (UR-BOUNDARY) is not proved here. It must not
be encoded as a definition of rho or used to choose its lift.

For a completely explicit sum interface, put t_k=binom(m,k)binom(2m,k).
Then V=sum t_k w^k mod p and

    d=V'(1/2)=sum_(k=1)^m k t_k 2^(1-k),

    E_half=sum_(k=0)^m sum_(r=0)^(3m)
           t_k (-1)^r binom(3m,r)
           2^(-(m+k+r+1))/(m+k+r+1).

All divisions in E_half are units since m+1<=m+k+r+1<=5m+1<p.
The last remaining first-digit identity is

    6rho*d+(2/3)binom(2m,m)*E_half=3 mod p.       (UR-SUM)

The divided rho itself has a separate first-order rational constructor
which can be useful for a finite summation proof. Write H_j=sum_(a=1)^j
1/a, H_0=0, and set

    T_m(w)=sum_(k=0)^m t_k w^k,
    j_k=-t_k[(H_m-H_(m-k))/6
             +(H_(2m)-H_(2m-k))/3].

Expanding the exact independent parameters
1/6=-m+p/6 and 1/3=-2m+p/3 coefficientwise gives

    V_lift(w)=T_m(w)+p sum_(k=0)^m j_k w^k mod p^2.

All reciprocals in this expansion are units. CM0 gives p|T_m(1/2), so

    rho=T_m(1/2)/p + sum_(k=0)^m j_k 2^(-k) mod p.

The first term is the exact rational finite binomial sum divided by p,
not a zero value, a Teichmuller replacement or a fitted boundary. This
formula retains the second precision of the exact truncation while the
integral constructor only needs F_p.

## 5. Saved negative evidence and one concrete next Task

* The hypothesis V(1/2)=0 mod p does not imply rho=0. Deleting rho loses
  the fixed exact rational lift. No assertion of its p^2 vanishing is made.
* The self-adjoint Q has degree p, even though its derivative has degree
  5m. Replacing Q by its zero-constant primitive drops the actual
  -w^p/6 term and shifts the CM first-digit formula by 2.
* Evaluating P(1)=1/6 is genuine endpoint progress, but it does not
  evaluate P(1/2) or rho, and does not prove UR.
* The already proved correction tau and OLD-R remain separate. This
  paper does not address the second digit or normalize a crystalline
  cup product merely by terminology.

One suggested next bounded formal Task: prove (UR-SUM) for the two
specified classes from the separately frozen rational truncation rho,
the binomial derivative d and the beta-integral sum E_half. Require an
explicit finite telescoping/parameter-jet boundary certificate whose
denominators and endpoints are checked; it must derive the constant 3
without reading U as a normalization. Preserve the precise residual if
the proof does not close. A future independently authorized p=13,19
constructor check may diagnose this new boundary interface, but none
was executed here. This is one proof direction, not a request to repeat
the old six-prime/77-prime arithmetic campaign or provider queries.

Parent UR/LIFT, raw theta periods, marked crystalline identification and
native global X6 propagation remain OPEN. Local papers and this exact
handoff are the entirety of the delegated output.
