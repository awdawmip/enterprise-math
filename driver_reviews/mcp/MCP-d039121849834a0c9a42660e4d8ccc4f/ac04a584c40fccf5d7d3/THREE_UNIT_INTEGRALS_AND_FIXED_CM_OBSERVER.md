# Three unit integrals for the fixed CM second-digit observer

Status: BOUNDED_LOCAL_PAPER_PREPARATION / NEW_FINITE_CONSTRUCTOR_PROVED /
OLD_R_COMPARISON_OPEN / LIFT_OPEN.

Prepared 2026-10-11 by the directed `cm24_lift_value_identity` delegate.
This is a shared-work algebra unit, not blind review, a formal Task,
Claim, identity, immutable Result, or Source publication. No prime
campaign, provider request, or native control mutation was performed.
The supplied forcing and boundary theorem is an explicit conditional
input awaiting its parent's final independent review. The calculations
below do not rederive that theorem or claim to settle its audit.

The P000/Heartbeat and joint-observer contracts were read locally; the
residual-faithful companion was read. Native X6 and separately typed
time remain unchanged. The variable z and its Frobenius extension are
external classical arithmetic readouts; no native spatial propagation,
complete-state reduction, or global mathematical parent closure follows.
Both marked CM branches and the independently frozen OLD-R observer are
retained. All author files and old Result bytes remain untouched.

## 1. Inputs and the exact independent target

Let p=6m+1 be prime, p>=7. The final CM comparison concerns precisely
p=13 or19 mod24. Over F_p retain

    H(x)=sum_(n=0)^(2m) b_n x^n,
    b_n=(1/3)_n(2/3)_n/(n!)^2,
    V(w)=sum_(k=0)^m v_k w^k,
    v_k=(1/6)_k(1/3)_k/(k!)^2,
    H(x)=V(4x(1-x)).

Let A=(3z-1)/(z-1)^3, B=(3z-1)^2/(z+1)^3, and X=z^p.
The supplied finite forcing theorem fixes a proper rational Xi(z),
with poles only at +/-1 of order at most3p-1, and

    Xi'=Q,
    Xi(0)=0, Xi(3)=Xi(1/3)=3q_3/8,
    [z^-p]Xi=q_3,
    q_3=(3^(p-1)-1)/p mod p.                            (1)

It also fixes, for delta^2=2, zeta=3-2delta and zeta^p=zeta^-1,

    Xi(zeta)=(1-U)/(12p) mod p.                         (2)

The same input gives the following combined forcing (audit equation6):

    Q=-(3X-1) H(B) [4z(X+1)^2
            -(z-3)(3X-1)(X-1)^2]
       /[3(z+1)(3z-1)(X-1)^3(X+1)^2]
       + z^(p-1) J'(X)/3,
    J(X)=X(X-3)(3X-1)/(X^2-1)^2.                       (3)

The old target is independently Source-pinned, before Xi or U:

    OLD-R=2 sum_(i=1)^m v_i2^-i
                sum_(r=1)^i (1+6(i-r))D_r,
    D_r=2^(r-1)(r-1)!^2/[18(5/6)_r(2/3)_r].           (4)

The retained adjoint correction is independently

    tau=-(1/9) int_0^(1/2)
                V(w)[(1-w)^(3m)-1]/w dw.              (5)

All integral denominators in (5) lie in1..4m<p. The requested identity
remains Xi(zeta)=-(OLD-R+6tau)/12. Neither (4) nor (5) is defined from
Xi, U, its residual, or a desired boundary value.

## 2. A Frobenius-basis decomposition of the forcing

Define the polynomial and its exact divided companion

    W(z)=(z+1)^(p-1)H(B(z)),
    T(z)=[W(z)-1]/(3z-1).                             (6)

These are polynomials: the largest denominator in H(B) has exponent
3(2m)=p-1. As B(infinity)=0 and H(0)=1, W is monic of degree p-1.
At z=1/3, B=0 and W=(4/3)^(p-1)=1. Thus division in (6) is exact,
and deg T=p-2. The symbol T here is a rational-map polynomial; it is
not the old reflected tail or the earlier Hesse forcing integral T_*.

Set

    a(X)=4(X+1)^2-(3X-1)(X-1)^2,
    b(X)=3(3X-1)(X-1)^2,
    d(X)=(X^2-1)^3,
    alpha(X)=-(3X-1)a(X)/(9d(X)),
    beta(X)=-(3X-1)[a(X)+3b(X)]/(9d(X)),
    chi(X)=-[a(X)+3b(X)]/(9d(X)).                     (7)

Using (z+1)^p=X+1, equation(3) becomes

    Q=-(3X-1)W(z)[a(X)z+b(X)]/[3d(X)(3z-1)]
      +z^(p-1)J'(X)/3.                               (8)

Write W/(3z-1)=T+1/(3z-1), and use
1/(3z-1)=(3z-1)^(p-1)/(3X-1). Polynomial division gives the exact
identity

    Q=alpha W+beta T+chi(3z-1)^(p-1)
                               +z^(p-1)J'(X)/3.

There is no nonintegrable top basis mode, because

    J'(X)d(X)=X a(X)+b(X),
    alpha(X)+chi(X)+J'(X)/3=0.

Consequently the useful final decomposition is

    Q=alpha(X)[W(z)-z^(p-1)]
        +beta(X)T(z)
        +chi(X)[(3z-1)^(p-1)-z^(p-1)].                (9)

This is an identity in F_p(z), not a substitution that treats X and z
as independent numerical values. Rational functions of X=z^p have
derivative zero. The three bracketed polynomials have degree <=p-2.

## 3. Three canonical unit-denominator integrals

For a polynomial of degree <=p-2, denote by int_0^z its unique
polynomial integral with zero constant and degree <=p-1. Its coefficient
denominators lie in1..p-1 and are all units. Define independently

    I_W(z)=int_0^z [W(t)-t^(p-1)]dt,
    I_T(z)=int_0^z T(t)dt,
    I_E(z)=int_0^z [(3t-1)^(p-1)-t^(p-1)]dt.          (10)

No log, p denominator, missing w^p integration mode, CM value, OLD-R,
or q_3 enters these definitions. In particular, if
W=sum_(j=0)^(p-1)w_j z^j and T=sum_(j=0)^(p-2)t_jz^j, then

    I_W=sum_(j=0)^(p-2)w_j z^(j+1)/(j+1),
    I_T=sum_(j=0)^(p-2)t_j z^(j+1)/(j+1).

The binomial theorem in characteristic p gives

    (3z-1)^(p-1)-z^(p-1)=sum_(j=0)^(p-2)3^jz^j,
    I_E(z)=(1/3) sum_(j=1)^(p-1)(3z)^j/j.             (11)

Thus I_E is an explicitly normalized finite logarithm, and
I_E(1/3)=H_(p-1)/3=0. It is not an analytic logarithm or a new
period normalization.

The directly integrated forcing is

    P_hat(z)=alpha(X)I_W(z)+beta(X)I_T(z)+chi(X)I_E(z).
                                                                  (12)

Equation(9) proves P_hat'=Q. This construction replaces the full
partial-fraction extraction by three polynomial integrals. Its initial
pole bound is3p rather than3p-1; that one possible Frobenius pole mode
must be repaired explicitly, not silently dropped.

## 4. A target-independent repair of the 3p pole modes

The numerator of P_hat over d(X) is

    N(z,X)=-(3X-1)a(X)I_W(z)/9
            -(3X-1)[a(X)+3b(X)]I_T(z)/9
            -[a(X)+3b(X)]I_E(z)/9.

Its possible leading pole coefficients are the two values

    r_+=N(1,1)
       =-32[I_W(1)+I_T(1)]/9-16I_E(1)/9,
    r_-=N(-1,-1)
       =64I_W(-1)/9-512I_T(-1)/9+128I_E(-1)/9.        (13)

Set the explicitly fixed linear polynomial

    n(X)=n_0+n_1X,
    n_0=-(r_++r_-)/2,
    n_1=-(r_+-r_-)/2,
    P(z)=P_hat(z)+n(z^p)/(z^(2p)-1)^3.                (14)

Since n(1)=-r_+ and n(-1)=-r_-, the numerator in(14) vanishes at
each z=+/-1. The denominator has pole order3p there; the actual pole
order is therefore <=3p-1. The added term is derivative zero. No target
observer was used to choose it.

At infinity alpha,beta=O(X^-2), chi=O(X^-3). All I polynomials have
degree <=p-1. The repair term is O(z^-5p). Therefore

    P'=Q, P has only +/-1 poles of order<=3p-1,
    P=O(z^(-p-1)), and [z^-p]P=0.                    (15)

P need not equal the earlier local-partial-fraction primitive. It is
a different fixed, legal primitive with the same forcing and pole
bound. Its remaining derivative-zero difference from Xi is completely
fixed by the same finite data(1). This distinction is essential: no
primitive was declared canonical merely because it integrates Q.

## 5. The uniquely reconstructed CM observer

Let

    v0=-P(0), v3=3q_3/8-P(3), va=3q_3/8-P(1/3),
    eta(X)=v0(X-3)(X-1/3)
             +8v3X(X-1/3)-(8/9)vaX(X-3).

The earlier four-dimensional Frobenius-kernel argument, or direct
interpolation with the pole bound(15), gives

    Xi(z)=P(z)+eta(z^p)/(z^(2p)-1)^2
                                   +(q_3/3)J(z^p).   (16)

There is no fitted coefficient: the last coefficient is q_3/3 because
[z^-p]P=0 and [z^-p]J(z^p)=3. The three finite coefficients use only
the independently derived endpoint data(1).

At zeta=3-2delta put X=zeta^-1=3+2delta. Then X^2-6X+1=0. Equations
(7) simplify exactly to

    alpha(X)=-1/6+delta/8,
    beta(X)=-1/6,
    chi(X)=1/6-delta/8=-alpha(X).

Hence the forcing primitive's CM term has the particularly small form

    12P_hat(zeta)=(1-3zeta)[I_W(zeta)-I_E(zeta)]/4
                                                   -2I_T(zeta).   (17)

For the interpolation term, the three CM coefficients are

    12(X-3)(X-1/3)/(X^2-1)^2=zeta,
    96X(X-1/3)/(X^2-1)^2=3-zeta,
    -(32/3)X(X-3)/(X^2-1)^2=zeta-1/3.

Also J(X)=1/4. Inserting these in(16) yields the exact value formula

    12Xi(zeta)=Lambda_p+2q_3,
    Lambda_p=12P(zeta)-zeta P(0)
                 -(3-zeta)P(3)-(zeta-1/3)P(1/3).      (18)

The factor2 in front of q_3 has two independently derived sources:
the two nonzero finite endpoints contribute q_3, and the infinity
normalization contributes q_3. Omitting either changes the observer.
The whole right side is in F_p by the supplied CM formula(2), but its
individual terms can lie in F_(p^2). The conjugate marked point must
be retained until the whole combination is formed.

## 6. Exactly what is still missing

Using the original definitions(4),(5), the sole outstanding identity
is now the explicit finite integral/Green-observer comparison

    Lambda_p+2q_3
       +2 CT_v[B_m(v^-1)D_m(v)(1+5v)/(1-v)^2]
       -(2/3) int_0^(1/2)
              V(w)[(1-w)^(3m)-1]/w dw=0,             (19)

where B_m(v)=sum_(i=0)^m v_i2^-i v^i and
D_m(v)=sum_(r=1)^m D_rv^r. The signs in(19) are OLD-R+6tau:
6tau=-(2/3) times the integral. The polynomial T in(6) and the old
Green polynomial D_m in(19) are different objects and are not equated.

Formula(19) has not been proved here. It is not treated as true because
earlier finite tests passed, because first digit UR is known, or because
Xi has fully fixed boundary constants. In particular q_3 is not
assigned from OLD-R or an observed CM discrepancy.

The disjoint delegated OLD-R helper additionally derived, directly
from the fixed constant-term sum, the exact CM boundary reduction

    OLD-R=6V'(1/2)D_m(1)+2T_old,
    T_old=sum_(r=1)^m D_r
                   sum_(i=0)^(r-1)[6(r-i)-1]v_i2^-i.  (20)

Its proof is a finite Laurent-polynomial coefficient split (or a
three-residue calculation), using V(1/2)=0. T_old is a new name for
that explicit fixed triangular sum, not a fitted discrepancy and not
the polynomial T of(6). Combining(20) with the already proved
C_rev(1/2)V'(1/2)=-4tau gives a second equivalent exact missing identity

    Lambda_p+2q_3+2T_old
       +V'(1/2)[6D_m(1)-(3/2)C_rev(1/2)]=0.          (21)

Every term on the right is independently constructed before comparison.
Neither T_old nor the bracket has been evaluated here. The helper
proved a precise limitation of the simplest next ansatz: a universal
characteristic-zero one-variable rational antidifference for either
affine-weight B_i or D_r summand cannot exist. This does not exclude
a finite-field certificate of growing degree, a two-variable adjoint
certificate, or a higher-order telescoper. The helper's pole/degree
proof and its independently saved symbolic output are preserved in
`old-r-helper/`; no general impossibility of LIFT is inferred.

This is a strictly smaller evaluation interface than extracting up to
3p partial fractions at each of two poles: three polynomial integrals,
two fixed pole repairs, three finite endpoint evaluations and one
fixed Frobenius constant determine the entire desired value. All
coefficient integrations use units. It does not change the hard target.

An executable next ansatz is to substitute

    W(z)=(z+1)^(p-1)
          V(4z(z-3)^2(3z-1)^2/(z+1)^6)

into(10),(13),(18), expand the resulting linear functional coefficient
by coefficient in v_k, and compare it with the independently fixed
OLD-R kernel plus the binomial integral in(19). A valid certificate
would be a finite summand telescoper in k and the binomial expansion
index, using the exact Gauss ratio

    v_(k+1)/v_k=(k+1/6)(k+1/3)/(k+1)^2,

and would display its terminal k=m boundary together with the fixed
finite logarithm terms(11). The endpoint must be derived, not chosen
to make(19) vanish. The zero at V(1/2), the low cutoff m, and both
prime classes must remain explicit. If no such telescoper is found,
equation(19), with its exact independent constituents, is the saved
next unit; a larger prime scan does not replace it.

## 7. Verification and scope

The adjacent exact symbolic checker records23 passing identities:
forcing-basis coefficients, cancellation of the top nonintegrable
mode, CM coefficients, both pole-repair numerators, the interpolation
weights and both q_3 contributions. No prime was instantiated.

The polynomial degree/integral/pole arguments above are paper proofs.
The source-pinned OLD-R, independent symmetric M and reverse carrier
remain the authoritative inputs; no new pairing defines their values.
The parent's full forcing certificate and CM Wronskian relation are
explicit inputs, not retroactively accepted by this calculation.

Newly derived: the three-integral forcing decomposition(9)-(12),
independent pole repair(13)-(15), and fixed CM value formula(18).
Not derived: vanishing of(19), LIFT, the weighted p^3 supercongruence,
an all-prime new theorem beyond the stated conditional lemma, raw
period normalization, or complete native X6 propagation.
