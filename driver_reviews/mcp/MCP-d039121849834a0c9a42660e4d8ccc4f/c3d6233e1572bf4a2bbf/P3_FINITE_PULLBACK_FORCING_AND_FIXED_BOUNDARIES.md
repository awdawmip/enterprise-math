# The p^3 finite pullback forcing and its fully fixed boundary

Status: DIRECTED_BOUNDED_PAPER_PREPARATION / FINITE_FORMULAS_PROVED /
LAST_CM_COMPARISON_OPEN / LIFT_OPEN.

Root-directed continuation of the already frozen six-file finite UR
certificate at Source b891782c43d75f0ca227734a4cc894ffad6629e6. The
delegate is `cm24_ur_adjoint_frontier`; complementary algebra was checked
by its `lift_forcing_algebra_audit` child. This is shared, directed,
nonblind paper work, not a new formal Task, Claim, identity, activity or
Source mutation. Original Hesse RR bytes are untouched. No new prime
campaign or provider query was run. P000, Heartbeat and residual-fidelity
contracts were read; these are finite external arithmetic tools, not new
native spatial axioms. UR's first digit has existing prior art and is
used as a frozen theorem, with no first-discovery claim.

All independent inputs and final output bytes are pinned in
FINAL_LIFT_UNIT_PINS.json. The old R_p and tau_p below retain exactly
their frozen definitions. This paper never assigns either from U_p.

## 1. Exact finite truncation and its p^3 residual

Let p=6m+1>=7 be prime. CM conclusions require p=13 or19 mod24. Set

    b_n=(1/3)_n(2/3)_n/(n!)^2,
    F(x)=sum_(n=0)^(p-1)b_n x^n,
    D_H=x(1-x)d_x^2+(1-2x)d_x-2/9.

All denominators are p units. Coefficients are units for n<=2m,
have one p factor for 2m<n<=4m, and two for 4m<n<p. The full cutoff
p-1 must be retained at precision p^3; the previous 4m cutoff is only
valid modulo p^2.

Define the exact scalar

    Lambda_p=(p-2/3)(p-1/3)b_(p-1).

The exact rational recurrence gives

    D_H F=-Lambda_p x^(p-1).                         (1)

The removed-factor Wilson products give b_(p-1)/p^2=1 mod p. More
explicitly, in (1/3)_(p-1) the removed factor is p/3 and the remaining
residues are all nonzero residues except -2/3; their product is 3/2.
The corresponding quotient is 1/2. For (2/3)_(p-1), the removed factor
is 2p/3 and the remaining product is 3; its quotient is 2. The product
is 1, and ((p-1)!)^2=1 mod p. Hence

    Lambda_p/p^2=2/9 mod p,
    D_H F=-(2p^2/9)x^(p-1) mod p^3.                 (2)

Equation (1), not an infinite Gauss equation, supplies the next forcing.

## 2. Exact pullback Wronskian and the inhomogeneous derivative

Keep the frozen rational maps and multiplier, with a new variable z:

    A=(3z-1)/(z-1)^3, B=(3z-1)^2/(z+1)^3,
    L=(z+1)/(2(1-z)),
    K=B(1-B)/B'=-z(z-3)(3z-1)/(3(z+1)^2).

Put f=F(B), g=LF(A), and

    R=K(fg'-gf'),
    O(Y)=(K Y')'-(2/9)B'Y.

The frozen exact rational pullback identities hold before reduction:

    O(F(B))=B'(D_HF)(B),
    O(LF(A))=A'/(2L)(D_HF)(A).

Consequently the SIGNED exact derivative is

    R'=-Lambda_p [F(B) A' A^(p-1)/(2L)
                       -L F(A) B' B^(p-1)].           (3)

For the next digit only H=F mod p is needed on its right:

    H(x)=P_(2m)(1-2x)=V(4x(1-x)),
    V(w)=sum_(n=0)^m a_n w^n mod p,
    a_n=(1/6)_n(1/3)_n/(n!)^2.

R' is generally nonzero modulo p^3. Treating R/p as a derivative-zero
Frobenius rational function at this precision would erase the forcing.

## 3. A fixed reference, legitimate p^2 division and its derivative

Let

    N(t)=t(t-3)(3t-1),
    J(t)=N(t)/(t^2-1)^2.

The frozen first-digit certificate states R=-pJ(z^p)/3 mod p^2.
Use precisely this rational p-integral reference, with its displayed
integer coefficients and literal z^p, and define

    Xi_p(z)=[R(z)+(p/3)J(z^p)]/p^2 mod p.              (4)

This coefficientwise division exists by the proved first-digit
congruence. Common denominators are p-primitive polynomials, so the
division is in the p-integral rational-function localization. It does
not require pointwise division at a root of a denominator and does not
borrow a different lift of J.

Differentiating the exact reference retains its contribution:

    Xi_p'=Phi_p,
    Phi_p=-(2/9)[H(B)A'A^(p-1)/(2L)
                        -L H(A)B'B^(p-1)]
                     +(1/3)z^(p-1)J'(z^p) mod p.      (5)

The final term in (5) is essential: d[(p/3)J(z^p)] is
(p^2/3)z^(p-1)J'(z^p), not zero modulo p^3. Both inputs to (5) are
fixed finite rational functions; U, OLD-R and tau are not consumed.

## 4. Pole bounds: cyclotomic lifts cannot be ignored

The full F has degree p-1=6m. At z=1, g has pole order at most
3(p-1)+1=3p-2, so its derivative and R have order at most 3p-1.
At z=-1, f has order at most 3p-3, g has a zero of order at least 1,
and K has pole order 2, again giving R order at most 3p-1.

The exact reference J(z^p) has additional cyclotomic poles before
reduction. It is incorrect simply to give it the two endpoint poles.
For its precise modulo-p^2 expansion let

    D=z^2-1,
    E_p(z)=[z^(2p)-1-D^p]/p in Z[z].

Binomial divisibility makes E_p integral, and evaluation at z=1,-1
shows that D divides E_p. Thus

    J(z^p)=N(z^p)/D^(2p)
             -2p N(z^p)E_p(z)/D^(3p) mod p^2.         (6)

The correction has endpoint pole orders at most 3p-1. In (4), the
p times first term cancels the already proved p-order part of R; the
remaining p^2 quotient and the correction in (6) therefore show

    Xi_p has poles only at +-1, of orders <=3p-1;
    Phi_p has pole orders <=3p.                       (7)

The exact large-z derivative in (3) begins at z^(-p-1); R vanishes
at infinity. Hence R=O(z^-p) exactly, the reference is O(z^-p), and
Xi_p=O(z^-p) after division and reduction.

## 5. Three actual endpoints and one infinity coefficient

R vanishes exactly at z=0,3,1/3 through K, but J(z^p) need not vanish
there before reduction. Let q_3=(3^(p-1)-1)/p mod p. Using

    J'(3)=3/8, J'(1/3)=-27/8,

the fixed reference gives the nonzero corrected endpoint data

    Xi_p(0)=0,
    Xi_p(3)=Xi_p(1/3)=3q_3/8.                        (8)

Indeed (3^p-3)/p=3q_3 and
[(1/3)^p-1/3]/p=-q_3/3 modulo p; dividing pJ/3 by p^2 supplies
exactly (8). Treating a^p=a modulo p^2 would wrongly erase this data.

There is a fourth independent normalization at infinity. From
B=9/z+O(z^-2), A=3/z^2+O(z^-3), L=-1/2+O(z^-1), the exact leading
coefficient in (3) is

    R'=Lambda_p 9^p z^(-p-1)/2+O(z^(-p-2)),
    [z^-p]R=-Lambda_p 9^p/(2p).                      (9)

Since [z^-p]J(z^p)=3, equation (4) gives

    [z^-p]Xi_p=[1-9^p Lambda_p/(2p^2)]/p mod p.      (10)

Its numerator is divisible by p; this is a second legitimate scalar
division. The following finite factorial computation evaluates it
without a target normalization. Using b_n=(3n)!/[27^n(n!)^3], split
(3p-3)! into three p blocks and remove p,2p. If Q=(p-1)!, then

    (3p-3)!/p^2
      =2 Q^2 (p-3)![1+2p H_(p-3)] mod p^2,
    H_(p-3)=3/2 mod p.

The complete middle block contributes 1+pH_(p-1)=1 mod p^2. Dividing
by Q^3 yields 2/[(p-1)(p-2)], which is 1+3p/2 mod p^2. Finally
27^(p-1)=1+3p q_3 mod p^2. Therefore

    b_(p-1)/p^2=1+p(9/2-3q_3) mod p^2,
    Lambda_p/p^2=(2/9)(1-3p q_3) mod p^2.

Since 9^p=9(1+2p q_3) mod p^2, (10) becomes the fully fixed value

    [z^-p]Xi_p=q_3.                                  (11)

No Wilson quotient, theta period or value of U was used to choose it.

## 6. A finite canonical constructor of the entire second function

This section makes the forcing interface constructive over F_p without
carrying a hidden adjustable Frobenius constant.

Expand the explicit rational Phi_p at its only poles:

    Phi_p=sum_(a in {1,-1}) sum_(k=1)^(3p)
                    e_(a,k)/(z-a)^k.

There is no polynomial part because Phi_p decays at infinity. As
Phi_p is already proved to be a derivative of Xi_p, the coefficients
with k=1,p+1,2p+1 vanish. These are precisely the logarithmic or
noninvertible integration modes in the degree range. Define the fixed
partial-fraction primitive

    G_p=-sum_(a in {1,-1})
          sum_(2<=k<=3p, k-1 not 0 mod p)
                    e_(a,k)/[(k-1)(z-a)^(k-1)].        (12)

All denominators k-1 in (12) are units. This constructor sets the
local Frobenius modes of G_p at pole orders p,2p to zero, has no
constant, and is fixed before any CM comparison. It gives G_p'=Phi_p.

The difference Xi_p-G_p lies in F_p(z^p), has poles at most 2p at the
two endpoints (3p is excluded by (7)), and decays at infinity. Let
eta_p(t) be the unique polynomial of degree <=2 interpolating

    eta_p(a)=[Xi_p(a)-G_p(a)](a^2-1)^2,
                     a=0,3,1/3,

where the Xi_p(a) values are the independently fixed data (8). All
three nodes and denominators are distinct units for p>=7. Then the
remaining kernel is exactly one multiple of J, and (11) fixes it:

    c_p=[q_3-[z^-p]G_p]/3,
    Xi_p(z)=G_p(z)+eta_p(z^p)/(z^(2p)-1)^2
                                 +c_p J(z^p).          (13)

To see uniqueness, write a derivative-zero kernel over the denominator
(t^2-1)^2. Its numerator has degree <=3. Interpolation fixes its values
at 0,3,1/3, leaving only a multiple of N(t). The eta term has no
z^-p coefficient at infinity, while J has coefficient 3; (11) fixes
that last multiple. Thus all boundary constants in (13) are derived,
not fitted to U, OLD-R or a CM target. This is a finite algorithm in
H, rational differentiation/partial fractions, p and q_3.

## 7. The exact CM comparison through the second digit

Take delta^2=2 and zeta=3-2delta. For p=13 or19 mod24, delta^p=-delta
in F_(p^2), so zeta^p=zeta^-1 modulo p. Set

    alpha=A(zeta)=(2+delta)/4,
    beta=B(zeta)=(2-delta)/4,
    A'=B'=r, Kr=1/8, L=delta/2, KL'=-1/12.

All equations here are exact algebraic equalities when no reduction is
marked. Let M_0=M(1/2) and M_1=M'(1/2) be the exact finite values from
the frozen independent symmetric constructor. The final products only
require these values through p^3 and p^2 respectively; using the exact
values makes the displayed derivative congruences unambiguous. Retain the full carrier
from the proved global reflection descent, writing its q polynomial
as C (this C is neither Xi_p nor OLD-R). Let C_0=C(1/2), C_1=C'(1/2)
in F_p. The full coefficientwise identity gives

    F(alpha)=M_0+p^2 delta C_0/4,
    F(beta)=M_0-p^2 delta C_0/4                         mod p^3,
    F'(alpha)=-2delta M_1-p^2(C_1-C_0),
    F'(beta)=2delta M_1-p^2(C_1-C_0)                   mod p^3.

These are the retained full derivative corrections, not a zero-seed
replacement. In F(beta)F'(alpha)-F(alpha)F'(beta) their reflection
terms cancel, giving -4delta M_0 M_1 modulo p^3. Also
F(alpha)F(beta)=M_0^2 modulo p^3. Therefore the actual Wronskian is

    R(zeta)=KL'M_0^2+(L/8)(-4delta M_0M_1)
            =-M_0^2/12-M_0M_1/2
            =-p U_p/12 mod p^3,                      (14)
    U_p=(M_0/p)(M_0+6M_1) mod p^2.

The KL' term is essential at the second digit. Dropping it would omit
the M_0^2 term in U_p. CM0 gives p|M_0, so division by p in (14) is
valid at exactly the retained precision; no exact rational rho or
branch data has been discarded.

The literal zeta^p must not generally be replaced by zeta^-1 modulo
p^2. Here the fixed rational reference has a special double critical
identity:

    J(t)=1/4-(t^2-6t+1)^2/[4(t^2-1)^2].               (15)

Its numerator vanishes to second order at t=zeta^-1. Since
zeta^p-zeta^-1 is divisible by p, (15) gives

    J(zeta^p)=1/4 mod p^2.

This proves, rather than assumes, that the first Frobenius-lift error
does not contribute at this particular CM point. Equations (4),(14)
now give the exact second-digit relation

    Xi_p(zeta)=(1-U_p)/(12p) mod p,
    (U_p-1)/p=-12Xi_p(zeta) mod p.                    (16)

Xi_p(zeta) is in F_p because U_p is the independently constructed
base-field scalar. One may use (13) at both conjugate marked points;
their equality follows from (16), not a prior deletion of branch data.

## 8. What remains unproved, with its exact independent residual

The frozen reflected-tail target and the already proved finite
correction are

    OLD-R_p=2 sum_(i=1)^m a_i2^(-i)
                 sum_(r=1)^i (1+6(i-r))D_r mod p,
    D_r=2^(r-1)(r-1)!^2/[18(5/6)_r(2/3)_r],
    tau_p=-(1/9) int_0^(1/2)
                    V(w)[(1-w)^(3m)-1]/w dw mod p.

Equivalently, with B_m(v)=sum_(i=0)^m a_i2^(-i)v^i and
D_m(v)=sum_(r=1)^m D_r v^r, the already frozen Green-observer formula is

    OLD-R_p=2 CT[B_m(v^-1)D_m(v)(1+5v)/(1-v)^2].

Indeed the last kernel has coefficient 1+6j in degree j; this preserves
the previously fixed reflected observer, rather than deriving its value
from Xi_p. These keep their original unit ranges and normalizations. The existing
transport gives G_ph=U_p-6p tau_p mod p^2. Thus the original second
digit LIFT is EXACTLY the still-unproved finite identity

    Xi_p(zeta)=-(OLD-R_p+6tau_p)/12 mod p.             (LIFT-XI)

Using the completely fixed constructor (13), its explicit residual is

    Delta_p=12G_p(zeta)
       +12eta_p(zeta^-1)/(zeta^-2-1)^2
       +q_3-[z^-p]G_p+OLD-R_p+6tau_p mod p.           (17)

Delta_p is a base-field scalar once the full sum is formed. LIFT holds
if and only if Delta_p=0 in both specified prime classes. Formula (17)
is not asserted to vanish. All its inputs are independently defined
before comparison; in particular the q_3 and interpolation constants
were derived from endpoints and infinity rather than chosen to kill it.

Proved in this unit: the exact finite residual, inhomogeneous R', legal
divided Xi, corrected pole bounds, four actual boundary values, complete
canonical forcing constructor, the M_0^2 contribution and CM critical
Frobenius cancellation, and equivalence of the remaining LIFT identity.
Not proved: Delta_p=0, the second weighted supercongruence, new period
normalization, full crystalline marking, or the native mother goal.

The single meaningful successor is to derive an explicit finite
partial-fraction/adjoint comparison between (17) and the fixed OLD-R
and tau observers, without assigning a boundary from their target.
An independently authorized small constructor check would test (1),
(5),(8),(11),(13),(14) first; no such prime calculation was executed
here. All prior frozen Results and earlier failure evidence remain.
