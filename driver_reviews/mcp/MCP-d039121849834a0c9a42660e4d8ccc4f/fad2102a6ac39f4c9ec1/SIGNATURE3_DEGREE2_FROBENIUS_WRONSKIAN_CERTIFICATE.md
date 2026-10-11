# A finite signature-3 degree-2 Wronskian certificate for UR

Status: DIRECTED_PURE_PAPER_PREPARATION / EXACT_CERTIFICATE_PENDING_PARENT_AUDIT.

Prepared locally on 2026-10-11 within Root's bounded mathematical
preparation. No new Task claim, researcher identity, Source publication,
remote operation, numerical campaign, or change to immutable Results is
made here. P000_REALITY_FOUNDATION.json and the Heartbeat World contract
were read first and are not changed. This is external finite arithmetic,
not a native spatial model. The parent second-digit LIFT remains open.

This certificate uses the frozen independent symmetric constructor and
the exact divided lift in CM_FIRST_DIGIT_RESONANT_WRONSKIAN_BOUNDARY_PREPARATION.md.
It does not import Sun A14(ii), an analytic period normalization, or the
target value of U. The rational pullback is proved directly below.

## 1. Fixed input and the auxiliary finite polynomial

Let p=6m+1 be prime, p=13 or 19 modulo 24. Put

    a_n=(1/6)_n(1/3)_n/(n!)^2,
    b_n=(1/3)_n(2/3)_n/(n!)^2,
    V_lift(w)=sum_(n=0)^m a_n w^n,
    V=V_lift mod p,
    d=V'(1/2),
    rho=V_lift(1/2)/p mod p.

The independent symmetric constructor is

    M(w)=(1/2)sum_(n=0)^(p-1)b_n S_n(w),
    S_n(w)=S_(n-1)(w)-(w/4)S_(n-2)(w), S_0=2,S_1=1.

Frozen transport gives M=f_p modulo p^2 and the first digit

    U_0=6 (M(1/2)/p) d.

CM0 supplies V(1/2)=0. The exact rational rho is retained throughout:

    M(1/2)/p = rho+W(1/2) mod p.

For the certificate use the auxiliary rational truncation

    F(z)=sum_(n=0)^(4m)b_n z^n,
    H(z)=F(z) mod p.

All coefficient denominators are units at p. The valuations are 0 for
n<=2m, at least 1 for 2m<n<=4m, and at least 2 for 4m<n<p. Thus
F equals the original signature-3 truncation through p-1 modulo p^2.

Let

    D_H=z(1-z)d_z^2+(1-2z)d_z-2/9.

The exact coefficient recurrence gives

    D_H F=-(4m+1/3)(4m+2/3)b_(4m) z^(4m).

Here 4m+2/3=2p/3 and b_(4m) has one p factor. Consequently

    D_H F=0 mod p^2.                                      (1)

In characteristic p,

    H(z)=2F1(-2m,2m+1;1;z)=P_(2m)(1-2z),                 (2)
    H(z)=V(4z(1-z)).                                      (3)

Equation (2) is the terminating definition of Legendre P_(2m), since
2/3=-4m=2m+1 modulo p. Equation (3) follows directly by pulling D_G
back under w=4z(1-z): the result is D_H, and both polynomials have
degree at most 2m<p and constant term 1. The recurrence at z=0 has
nonzero divisor n^2 for 1<=n<=2m, so these polynomial solutions agree.
This is a finite quadratic identity, with no analytic branch assumption.

## 2. Exact rational degree-2 pullback

Introduce a rational variable s and set

    A=(3s-1)/(s-1)^3,
    B=(3s-1)^2/(s+1)^3,
    L=(s+1)/(2(1-s)),
    K=B(1-B)/B'=-s(s-3)(3s-1)/(3(s+1)^2).

All following identities are exact over Q(s), not assumed modular
period transformations. Pullback of D_H along B gives

    y''+P_B y'+Q_B y=0,
    P_B=(3s^3+9s^2-23s+3)/(s(s-3)(s+1)(3s-1)),
    Q_B=-2/(s(s+1)^2),
    K'/K=P_B.

If P_A,Q_A denote the same pullback coefficients along A, direct
rational differentiation gives

    P_A-2L'/L=P_B,
    Q_A-P_A L'/L+2(L'/L)^2-L''/L=Q_B.                     (4)

These two rational identities are an explicit differential certificate
that L times an A-pullback satisfies the B-pullback equation.

Put

    f(s)=F(B(s)),  g(s)=L(s)F(A(s)),
    R(s)=K(s)[f(s)g'(s)-g(s)f'(s)].

By (1) and (4), f and g solve the same pullback equation modulo p^2.
Their Wronskian therefore satisfies the coefficientwise rational identity

    R'(s)=0 mod p^2.                                     (5)

R lies in Z_(p)[s,(s-1)^(-1),(s+1)^(-1)]. In particular, critical
points 0,3,1/3 introduce zeros through K, not additional poles. Direct
evaluation shows

    R(0)=R(3)=R(1/3)=0                                   (6)

exactly, and R(s)=O(s^(-1)) at infinity.

## 3. Frobenius pole rigidity proves divisibility and fixes the shape

First reduce modulo p, where F has degree 2m.

At s=1, g has pole order at most 6m+1=p. Its leading derivative
coefficient is -p=0, so g' has pole order at most p; f and K are regular.
Thus R has pole order at most p there.

At s=-1, f has pole order at most 6m=p-1 and g has a zero of order
at least 1. The leading coefficient of fg'-gf' has the factor

    1+(p-1)=p=0 mod p.

Hence the Wronskian has pole order at most p-2; K has pole order 2,
so again R has pole order at most p. There are no other poles.

The derivative-zero kernel of F_p(s) is F_p(s^p). Therefore (5), the
two pole bounds, and the decay at infinity give

    R mod p = N(s^p)/[(s^p-1)(s^p+1)],  deg N<=1.

The three distinct zeros (6) force N=0. Thus

    R=0 mod p,                                           (7)

and the coefficientwise divided rational function R_1=R/p mod p is
well-defined independently of any target value.

In the full degree-4m truncation, g has pole order at most 12m+1=2p-1
at s=1, while f is regular, so R has pole order at most 2p. At s=-1,
f has pole order at most 12m=2p-2, g has a zero of order at least 1,
and K has pole order 2; R again has pole order at most 2p. Equation
(5) implies R_1'=0. The same three zeros and decay now yield

    R_1(s)=C s^p(s^p-3)(3s^p-1)
                /[(s^p-1)^2(s^p+1)^2].                  (8)

Indeed, in x=s^p the denominator has degree 4, the numerator has
degree at most 3, and its three roots are 0,3,1/3. This is the complete
finite resonance normalization; no homogeneous term is discarded.

## 4. The leading pole determines C=-1/3

Put c=b_(4m)/p mod p. The unique numerator p factor at index 2m in
(1/3)_(4m), and the unit product in (2/3)_(4m), give

    c=(2m)!(2m-1)!/[3(4m)!].

At s=1, with e=s-1,

    A=2e^(-3)+3e^(-2),  L=-e^(-1)-1/2,
    g=-p c 2^(4m)e^(-(2p-1))+lower pole terms mod p^2,
    f(1)=H(1/2) mod p,  K(1)=1/3.

Therefore the leading coefficient of R_1 at this pole is

    -c 2^(4m)H(1/2)/3.

The rational shape in (8) has leading coefficient -C at s=1,
because x(x-3)(3x-1)/(x^2-1)^2 has coefficient -1 at (x-1)^(-2).
Consequently

    C=c 2^(4m)H(1/2)/3.                                 (9)

Legendre's terminating value gives

    H(1/2)=P_(2m)(0)=(-1)^m(2m)!/[2^(2m)(m!)^2].

Wilson gives (4m)!(2m)!=-1. Hence

    c 2^(4m)H(1/2)
      =(-1)^m 2^(2m)(2m)!^4/(m!)^2.

In this simplification (2m-1)!=(2m)!/(2m) first leaves a denominator
6m; the additional reduction 6m=-1 modulo p produces the displayed
sign and removes that denominator.

To evaluate this last factorial quotient, split the even product
2,4,...,6m into its first 2m terms and its last m terms. Reduction of
the last m terms modulo p gives the negatives of the odd terms
1,3,...,2m-1, so

    2^(3m)(3m)!=(-1)^m 2^m(2m)!^2/m!.

Squaring and using 2^(6m)=2^(p-1)=1 gives

    2^(2m)(2m)!^4/(m!)^2=(3m)!^2=(-1)^(3m+1).

Thus c 2^(4m)H(1/2)=-1, and (8) is the explicit finite certificate

    R(s)/p = -(1/3) s^p(s^p-3)(3s^p-1)
                   /[(s^p-1)^2(s^p+1)^2] mod p.          (FC)

All factorial arguments are below p. The only excluded rational
denominators are 2 and 3; both are units for p>=7.

## 5. CM evaluation gives the independently fixed first digit

Work in the unramified quadratic extension and choose delta^2=2.
For the two specified prime classes delta^p=-delta. Set

    s=3-2delta,  s^2-6s+1=0,  s^p=1/s,
    alpha=A(s)=(2+delta)/4,
    beta=B(s)=(2-delta)/4,
    L(s)=delta/2.

The marked rational substitutions give alpha+beta=1 and
4alpha(1-alpha)=4beta(1-beta)=1/2 exactly. Their derivatives satisfy

    A'(s)=B'(s)=r,  K(s)r=1/8.

The finite quadratic identity (3), with the frozen CM0 value, gives

    H(alpha)=H(beta)=0,
    H'(alpha)=-2delta d,  H'(beta)=2delta d.

Both F(alpha) and F(beta) are consequently divisible by p. The original
symmetric constructor satisfies, modulo p^2,

    M(1/2)=[F(alpha)+F(beta)]/2.

This equality follows directly from S_n=alpha^n+beta^n and the omitted
coefficients' two p factors; it is not an identification with an analytic
period or a freely selected lift.

Evaluating the actual Wronskian and dividing coefficientwise by p gives

    R(s)/p
      =K L r[(F(beta)/p)H'(alpha)-(F(alpha)/p)H'(beta)]
      =-(d/4)[F(alpha)/p+F(beta)/p]
      =-(d/2)(M(1/2)/p)
      =-U_0/12.                                        (10)

The discarded term K L'F(alpha)F(beta)/p is divisible by p, which is
why it vanishes. No divided rational V_lift contribution is removed.

Since s^p=1/s and s^2-6s+1=0, direct reduction gives

    s^p(s^p-3)(3s^p-1)/[(s^p-1)^2(s^p+1)^2]=1/4.

The explicit finite certificate (FC) therefore gives R(s)/p=-1/12.
Comparison with (10) proves

    U_0=1 mod p.

Finally the independently proved resonant boundary from the input paper
is

    U_0=6rho d+24P(1/2)-2.

The resulting boundary identity is exactly

    6rho d+24P(1/2)=3 mod p,

or its displayed finite-sum UR-SUM form. The exact rational rho remains
the fixed low-block divided lift; it is neither set to zero nor fitted
to the answer. This proof concerns only the first digit. No second-digit
LIFT, marked crystalline period statement, theta normalization, or native
global propagation result is obtained.

## 6. Verification scope

The adjacent symbolic script verifies the rational pullback identities,
the CM derivative factors, the leading pole shape, and the exact top
recurrence formula symbolically. No primes are scanned. The pole and
finite-field derivative-kernel arguments above are mathematical proofs,
not numerical checks. Parent audit is requested before any ledger or
immutable Result status is changed.
