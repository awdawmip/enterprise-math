# Self-adjoint Heun boundary and a base-field reduction of the entire CM observer

Status: ROOT-DIRECTED BOUNDED LOCAL PAPER RESEARCH / NEW CONDITIONAL FINITE
LEMMAS PROVED / INDEPENDENT OLD-R COMPARISON OPEN / LIFT OPEN.

Prepared 2026-10-12 UTC. Native Researcher ID, native session and formal
Task/Claim are UNKNOWN for this local author and its algebra helper. The
labels `cm24_heun_zero_sum_next_proof` and `heun_adjoint_symbolic_helper`
are local collaboration labels, not registered identities. No native
mutation, Source write, accepted Result, provider query or prime campaign
is claimed. No prime was instantiated. The work is directed, nonblind
algebra following the fully frozen author paper and its independent review.

All finite fields, polynomial differential operators and scalar pairings
below are explicitly external auxiliary arithmetic observer models. Native
X6, the P000 contract and separately typed time retain their prior meaning.
No complete-state propagation or full-X6 theorem is obtained. Existing
semantic/tool coverage is retained; no general-tool novelty is asserted.

The new conclusions are (i) an exact self-adjoint operator and an actual
OLD-tau boundary under the same cubic coordinate as the full CM kernel;
(ii) a proved finite reversal and a reduction of the *entire* fixed CM
observer, including Gamma, to six base-field harmonic prefixes; (iii) a
precise obstruction to a universal rational logarithmic-source adjoint
ansatz, with the missing squared-logarithm modes identified. None evaluates
the remaining sum involving OLD-R.

## 1. Frozen premises and independent quantities

Retain the four conditional premises of the independently reviewed input:
finite transport; the complete forcing/four-boundary theorem; the fixed Xi
CM value theorem and marked quadratic Frobenius; and CM0. Nothing below
enlarges those premises. Let p=6m+1 be prime in the classes 13 or 19 modulo
24, N=3m=(p-1)/2, and work modulo p, extending the field only where noted.

The frozen finite polynomial and cubic coordinate are

    y(u)=V((1-u)(1-4u)^2)=sum_(n=0)^N h_n u^n,
    Y(t)=y(t^2), w(t)=(1-t^2)(1-4t^2)^2,
    a^2=1/2, a^p=-a.

The Heun recurrence is retained, not reproved by a new prime campaign:

    A_n h_(n+1)-B_n h_n+C_n h_(n-1)=0,
    A_n=(n+1)(2n+1), B_n=10n^2+5n+1, C_n=4n(2n-1),
    h_(-1)=h_(N+1)=0.

The frozen endpoints are y(1)=y(1/4)=1, with h_0=binom(3m,m) a unit.
The coefficient A_n is a unit for 0<=n<N and A_N=0. We explicitly retain
the fixed terminal relation h_N=4h_(N-1), and never divide by A_N.

OLD-R remains literally

    R=2 sum_(i=1)^m v_i 2^(-i)
                          sum_(r=1)^i [1+6(i-r)]D_r,
    v_i=(1/6)_i(1/3)_i/(i!)^2,
    D_r=2^(r-1)(r-1)!^2/[18(5/6)_r(2/3)_r].

The independent reverse-Gauss polynomial C(w), of degree at most 3m-1,
is the frozen reverse recurrence solution, not a scalar chosen to fit R.
It satisfies

    D_G V=0,
    D_G=w(1-w)partial_w^2+(1-3w/2)partial_w-1/18,
    D_G^* C=f(w)=-[(1-w)^(3m)-1]/(9w),
    tau=-(1/9)int_0^(1/2) V(w)[(1-w)^(3m)-1]/w dw.

The division by w denotes a polynomial. The original Gauss concomitant

    K_G=w(1-w)(CV'-VC')+(w/2)VC

is fixed by K_G(0)=0 and degree K_G<=4m<p; at w=1/2 it equals -tau.
The original target is Lambda+2q_3+R+6tau=0, and stays OPEN here.

## 2. An exact self-adjoint operator in the t coordinate

Put

    P(t)=(t^2-1)(4t^2-1)=4t^4-5t^2+1,
    S=partial_t[P(t)partial_t]+(8t^2-2).

Then the frozen Heun equation becomes exactly S Y=0. Indeed the pullback
of its u equation under u=t^2 is

    [(t^2-1)(4t^2-1)/2]Y''+(8t^3-5t)Y'
                                           +(4t^2-1)Y=0.

Multiplication by 2 gives S because P'=16t^3-10t. This establishes actual
flat-measure self-adjointness, not a pairing given that name.

More generally, let Pull_t(D_G) denote the differential operator obtained
by chain rule under the displayed w(t), in a rational function field.
The all-coefficient identity is

    S=-36(4t^2-1) Pull_t(D_G).                         (1)

For the leading coefficient, w_t'=-6t(4t^2-3)(4t^2-1) and

    w(1-w)/(w_t')^2=(1-t^2)/36.

The middle and constant coefficients give exactly P' and 8t^2-2 after
the same scaling. Equation (1) is a rational-function identity. It is
not pointwise division at t=0 or an apparent critical point.

Define, independently of any target scalar,

    E(t)=t(4t^2-3) C(w(t))/6.                         (2)

Then there are exact identities

    S E=w_t' f(w(t)),                                (3)
    P(EY'-YE')=K_G(C,V)(w(t)).                        (4)

Proof. In the u coordinate the scale between the Heun operator and the
Gauss pullback is -18(4u-1). Adjoint change of variable sends C to
[(w_u')/(-18(4u-1))]C=(4u-3)C/6. Changing u=t^2 and multiplying the
operator by 2 sends this flat-measure adjoint carrier to t(4t^2-3)C/6,
which is (2). Integration by parts, or direct coefficient substitution,
gives (3). This argument is an identity for arbitrary symbols C,C',C'';
it does not assume a characteristic-zero finite V solves the Gauss
equation for arbitrary m.

For a direct algebraic verification of (4), the coefficient of CV' on
the left is P[t(4t^2-3)/6]w_t'=w(1-w), the coefficient of VC' is its
negative, and the coefficient of VC is
-P[t(4t^2-3)/6]'=w/2. These are exactly the three original coefficients.
Thus no integration constant or new Frobenius normalization is chosen.

Because S is self-adjoint, differentiating (4) gives the finite Green
identity

    partial_t[P(EY'-YE')]=E S Y-Y S E=-Y w_t'f(w(t)). (5)

At the marked t=a, Y(a)=0, w(a)=1/2 and w_t'(a)=6a. Hence

    P(a)E(a)Y'(a)=C(1/2)V'(1/2)/4=-tau.             (6)

This is a proved new boundary representation of the *independently
defined* tau in the very same operator as the CM kernel. It does not give
R or Lambda+2q_3. In particular E generally has degree as high as 18m-3,
and the composed K_G as high as 24m. One cannot reconstruct (4) merely
by differentiating in characteristic p and discarding multiples of p:
these degrees cross the Frobenius integration threshold. The literal
composition of the original degree< p fixed K_G supplies the normalization.

## 3. Finite reflection with its legal endpoint

The following independently derived finite reflection supplies the
kernel reduction. Define g_n=4^n h_(N-n), 0<=n<=N. Since N=-1/2 modulo p,
with k=N-n,

    A_k=C_n/4, B_k=B_n, C_k=4A_n.

The Heun equation at k therefore proves the same recurrence for g_n,
including n=0,N with the stated zero exterior terms. Its solutions on
0,...,N form a one-dimensional space: the first N equations propagate
from h_0 using the unit A_0,...,A_(N-1), and a nonzero frozen solution
satisfies the last equation. Therefore g_n=c h_n for one scalar c.
The independent, already frozen endpoint values determine it without
reading the target:

    sum g_n=4^N y(1/4)=1,
    sum h_n=y(1)=1,
    4^N=2^(p-1)=1.

Consequently

    h_(N-n)=4^(-n)h_n,                               (7)
    h_N=h_0.

This is a modular statement with its endpoint proved, not a
characteristic-zero hypergeometric parameter substitution. It also gives
y(1/(4u))=u^(-N)y(u) as a rational-function identity, but no observer
comparison follows just from that symmetry.

Write L_j(x)=sum_(r=1)^j x^r/r and L=L_(p-1). Define the *fixed* log
observer F(x)=sum_(n=0)^N h_n L_(2n)(x). By reversing finite sums,

    sum_(n=0)^N h_n4^(-n)L_(2n)(x)
                         =L(x)+x^p F(1/x).          (8)

Proof. Substitute (7), replace n by N-n, and use

    L_(p-1-2n)(x)=L(x)+x^p L_(2n)(1/x).

The last identity reindexes only r=1,...,p-1, by r to p-r. All actual
log denominators are units. It is interpreted for x nonzero; after
clearing powers it is a polynomial identity and contains no division by p.

## 4. Reduction of the entire fixed observer to the base field

The original frozen equation was Lambda+2q_3=Gamma+sum h_n K_n(a),
including the original pole repairs and Gamma. Apply (8) to every
4^(-n)L_(2n) term of that fixed kernel, using the already frozen finite
log constants. One obtains, with no new definitions of R or tau,

    Lambda+2q_3=
      2q_2-3q_3-4a[L(a)-L(-a)]
      +F(1)-(5/3)F(-1)-(2/3)F(1/2)-4F(-1/2)
      +(4a+2)F(a)+(2-4a)F(-a).                     (9)

For transparency, the four reversed weighted logs are

    sum h_n4^(-n)L_(2n)(-2)=L(-2)-2F(-1/2),
    sum h_n4^(-n)L_(2n)(2)=L(2)+2F(1/2),
    sum h_n4^(-n)L_(2n)(-2a)=-2aL(-a)+2aF(-a),
    sum h_n4^(-n)L_(2n)(-1)=L(-1)-F(-1).

Substitution of L(-2)=2q_2-3q_3 and L(2)=L(-1)=-2q_2 cancels all
the a-dependent q_2 coefficients with Gamma. The surviving constants
are precisely the first line of (9). Thus (9) computes Lambda, with
its previously fixed pole repair, rather than an unrepaired antiderivative.

For 0<=n<=N and z in the base field put

    H_n(z)=sum_(r=1)^n z^r/r,
    O_n(z)=sum_(r=1)^n z^r/(2r-1), H_0=O_0=0,

and define

    beta_n=2H_n(1/2)+8O_n(1/2)
           -(1/3)H_n(1)+(8/3)O_n(1)
           -(7/3)H_n(1/4)+(20/3)O_n(1/4),
    kappa=2q_2-3q_3-8O_N(1/2).                      (10)

Then the new, entire base-field observer theorem is

    BOX: Lambda+2q_3=kappa+sum_(n=0)^N h_n beta_n.  (11)

Proof. For any nonzero t,

    F(t)+F(-t)=sum h_n H_n(t^2),
    F(t)-F(-t)=(2/t)sum h_n O_n(t^2).

Apply these identities to the pairs at t=1,1/2,a in (9). At the CM pair,

    (4a+2)F(a)+(2-4a)F(-a)
              =sum h_n[2H_n(1/2)+8O_n(1/2)],
    -4a[L(a)-L(-a)]=-8O_N(1/2).

The rational pairs contribute respectively -H_n(1)/3+8O_n(1)/3 and
-7H_n(1/4)/3+20O_n(1/4)/3. These are all terms in (10). No target value,
OLD-R coefficient or tau coefficient is used in the derivation. Every
division is by r<=N or 2r-1<=p-2, so the entire expression is in F_p.
The quadratic marking disappears algebraically rather than by assuming
the individual old K_n or Gamma were base-field-valued.

The new kernel has a particularly small, exact increment:

    beta_0=0,
    beta_n-beta_(n-1)
      =[(6n+1)+6(6n-1)2^(-n)+(6n+7)4^(-n)]
                                             /[3n(2n-1)], 1<=n<=N. (12)

This follows by subtracting the six finite prefixes in (10). It has only
the three fixed phases 1,2^(-n),4^(-n), with no division at or beyond p.
It substantially reduces the next discrete-adjoint comparison interface.

The unresolved LIFT theorem is now exactly

    kappa+sum_(n=0)^N h_n beta_n+OLD-R+6tau=0.        (13)

Neither (7), (11), (12) nor the independently fixed boundary (6) proves
(13). The helper's finite Green rank/cokernel theorem further shows why
automatic construction of an adjoint from beta cannot prove it: solving
the zero-boundary adjoint equation is subject to the very scalar pairing
one still has to establish, not a substitute for its proof.

## 5. The exact primitive interface and what a rational ansatz misses

This section first records a legal finite-field interface, then a
separate characteristic-zero universal-rational obstruction. It makes no
claim that a finite-field certificate of growing degree cannot exist.

For b=1 or b=-1/2 define the canonical polynomial primitive

    J_b(t)=int_0^t [Y(s)-1]/(s-b) ds.                (14)

Since Y(b)=1, the integrand is a polynomial of degree at most p-2. Its
zero-at-0 primitive has degree at most p-1, and all its denominators are
1,...,p-1. In particular J_1=F. Directly from the finite logs,

    J_(-1/2)(t)=sum h_n4^(-n)L_(2n)(-2t).

Thus the *complete original* sum h_n K_n is already a linear combination
of these two actual canonical primitives at the fixed endpoints. Equation
(8) explains why only J_1 is needed after reflection. This identifies the
same S and the exact normalization used by the entire observer.

Consider now, only in characteristic zero, a proposed universal rational
adjoint phi satisfying

    S phi=alpha/(t-1)+beta/(t+1/2),                 (15)

with fixed scalars alpha,beta and at least one nonzero. There is no such
phi rational over a characteristic-zero constant field. At an ordinary
finite pole of order k>=1, the leading second-derivative term of S phi
has pole order k+2 and nonzero coefficient P(c)k(k+1). At a simple root
b of P, a pole of order k has leading pole order k+1 and coefficient
P'(b)k^2. All four roots 1,-1,1/2,-1/2 are simple. Thus phi can have no
finite pole: the right side has only simple poles, whereas every allowed
pole of phi would produce a pole of higher order that cannot cancel.
Then phi is polynomial, and S phi is polynomial, contradicting (15).

This proves insufficiency for this specified one-carrier rational
logarithmic-source ansatz. It does not exclude the helper's higher-order
or multi-flux certificates, finite-field Frobenius modes, or a carrier
outside this function class. Over F_p the same local proof is valid only
under the expressly bounded pole orders k<=p-2 at ordinary points and
k<=p-1 at roots of P. Allowing orders where k or k+1 vanishes modulo p
can change the conclusion; it is not silently prohibited.

The missing characteristic-zero mode can be identified precisely. Near
a simple root b, take the local analytic solution U_b of S U_b=0 with
U_b(b)=1. This is a characteristic-zero local solution of the fixed S,
not the arbitrary-m terminating polynomial Y. Reduction of order gives

    S(U_b z)=[P U_b^2 z']'/U_b.

For S phi=gamma/(t-b), integrating twice forces

    phi(t)= [gamma/(2P'(b))] log(t-b)^2
                                  +terms with at most one log at order 0
                                  +higher powers of (t-b) with logs. (16)

Indeed the first integral has leading gamma log(t-b), and division by
P U_b^2 has leading gamma log(t-b)/[P'(b)(t-b)]. A second integral
produces (16). Homogeneous local additions alter only the single-log
and regular terms; they cannot remove the displayed squared-log mode.
Its coefficients are gamma/12 at b=1 and gamma/6 at b=-1/2.

For example the CM endpoint part of the original two-primitive observer
has logarithmic source coefficients alpha=2(2a+1), beta=2(a-1). They
are nonzero for a^2=1/2. Its corresponding missing squared-log coefficients
are (2a+1)/6 and (a-1)/3. The already fixed polynomial E from (2) supplies
the tau forcing in (3), and cannot be substituted for these two carriers:
S E has polynomial forcing, whereas (15) has the displayed simple poles.

This is compatible with (14) being polynomial. In characteristic zero,
take a local homogeneous solution U of S U=0 with U(b)=1, and suppose
S phi_b=1/(t-b). The Green identity gives its *subtracted* primitive

    J_b^U(t)=-[P(phi_b U'-U phi_b')]_0^t
                                      -log[(t-b)/(-b)].              (17)

Its derivative is (U-1)/(t-b); the explicit scalar logarithm cancels the
apparent logarithmic divergence at U(b)=1. Endpoint 0 means a chosen
regular reference reached on the same local continuation. No assertion
that the frozen finite Y solves S in characteristic zero is made. The
rational ansatz misses the
squared-log carrier and this fixed subtraction. Equation (17) is a
characteristic-zero operator interface, not a transferred proof of the
finite-field primitive. In F_p the legal object remains the literal (14)
or the finite prefixes in (10); all Frobenius and endpoint corrections
must be retained explicitly in any eventual certificate.

## 6. Concrete next unit, without a new campaign

Proposed task: CM24 finite three-phase Green comparison with OLD-R.
Its immutable inputs are (10)-(12), the independent old triangular R,
the independently fixed E/C and tau boundary (2)-(6), and the helper's
finite Green/cokernel theorem. The hard target is an actual finite flux
or inhomogeneous adjoint identity proving (13), with all boundaries fixed
before evaluation, or an exact residual with its coefficientwise source.

Search the three prescribed increment phases of (12) using the existing
Heun recurrence and the reciprocal D_r ratio; permit multiple fluxes or
logarithmic/Frobenius corrections explicitly. Keep n=0,N and the original
r=1,m endpoints. A proposed zero-boundary adjoint must independently meet
the helper's cokernel condition. A source term encoding R must be derived
from the unchanged triangular sum, never chosen to cancel a discrepancy.
No new general-purpose primitive or repeated prime scan is required.

Success at this unit is a new finite boundary/flux certificate or a saved
precise residual; it is not automatic completion of the parent weighted
p^3 congruence, raw period normalization, LIFT or native full-X6 propagation.
The fourth-order OLD-R terminal equality still fixes only R_(m+1)-R_m.

## 7. Verification and disclosure

The independent symbolic checker in this folder tests exact operator
coefficients, transformed concomitant, CM coefficient, reflected Heun
coefficients, the entire kernel/log-constant simplification, the six-prefix
base-field conversion, the three-phase increment, and the pole leading
coefficients. It instantiates no prime and runs no author checker. Proofs
above establish the statements; symbolic checks only corroborate them.

The helper independently derived the finite Green identity, rank-one
kernel/cokernel, legal finite reflection and initial full-kernel reversal;
the main author independently reached the self-adjoint operator, carrier,
base-field six-prefix reduction and rational/logarithmic-source obstruction.
They exchanged intermediate formulas, so this is directed collaboration,
not an independent final peer review. Root will perform separate Driver
paper review before relying on the increment in the state machine.

Newly established: (1)-(6), (7)-(12), the canonical primitive interface,
and the narrowly scoped obstruction/missing local modes (15)-(17).
Still OPEN: (13), LIFT, the weighted p^3 supercongruence, raw period
normalization, and complete native X6 propagation.
