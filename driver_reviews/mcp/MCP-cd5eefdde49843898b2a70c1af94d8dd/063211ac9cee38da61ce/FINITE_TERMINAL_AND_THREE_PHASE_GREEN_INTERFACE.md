# Finite terminal defect and the three-phase Green interface

Status: LOCAL CONTINUATION / FINITE INTERFACE LEMMAS PROVED / LITERAL OLD-R
COMPARISON OPEN / LIFT OPEN. Prepared 2026-10-12 UTC.

This continues the mathematical unit interrupted before a paper was saved.
The named interrupted directory exists but contained zero files at intake;
`INTERRUPTED_AUTHOR_BYTES_PINS.json` records that observation. Consequently
this is a fresh written derivation of the already directed continuation,
not a claim to have inherited a saved three-phase paper. The preceding
self-adjoint paper, its adjoint helper, and the literal OLD-R certificate
are unchanged; their input bytes were verified against their frozen pins.
No prime is instantiated, no frozen checker is read or executed, and no
target value is fitted. This local collaboration label is not a native
identity, Claim, Task, Source, accepted Result, or operational completion.
The arithmetic models remain external finite classical observers, with
native X6 and separately typed time unchanged.

The results here are an exact terminal defect for a canonical constant-
forcing adjoint; a signed, endpoint-correct three-phase identity for the
entire reduced observer; an explicit order-three polynomial operator for
its increment and order-four operator for its prefix; and a precisely
scoped explanation of why the existing OLD-R certificate is not the same
operator under a rational scalar gauge at the same index. None proves the
remaining scalar comparison.

## 1. Literal normalization and finite inputs

Retain the conditional premises and fixed constructors of
`SELF_ADJOINT_HEUN_AND_BASE_FIELD_OBSERVER_REDUCTION.md`. Let p=6m+1 be prime,
N=3m=(p-1)/2, in the previously specified classes when the CM marking is
used. All finite formulas in sections 1–4 are over F_p. Set

    A_n=(n+1)(2n+1), B_n=10n^2+5n+1, C_n=4n(2n-1),
    (Lh)_n=A_n h_(n+1)-B_n h_n+C_n h_(n-1),
    (L* f)_n=A_(n-1)f_(n-1)-B_n f_n+C_(n+1)f_(n+1).

The literal frozen polynomial is y(u)=V((1-u)(1-4u)^2)=sum h_n u^n.
Its normalization is

    Lh=0, h_(-1)=h_(N+1)=0,
    h_0=h_N=g=binom(3m,m) != 0, sum_(n=0)^N h_n=1.

In particular h_0 and h_N are not silently changed to 1. Dividing the
sequence by g would also change its sum to 1/g and would change the fixed
observer. Here both the literal g and the literal sum 1 are retained.
The terminal identities are

    A_(-1)=C_0=A_N=C_(N+1)=0,
    B_N=1, C_N=4, A_(N-1)=1,
    h_N=4h_(N-1), C_(n+1)=4A_n.

Every A_n for 0<=n<N and every C_n for 1<=n<=N is a unit. There is no
division by A_N, C_(N+1), or a terminal harmonic denominator.

The fully repaired fixed observer is already proved to be

    Lambda+2q_3=kappa+sum h_n beta_n,
    kappa=2q_2-3q_3-8O_N(1/2),
    beta_n=2H_n(1/2)+8O_n(1/2)-H_n(1)/3+8O_n(1)/3
                                      -7H_n(1/4)/3+20O_n(1/4)/3,
    H_n(z)=sum_(r=1)^n z^r/r, O_n(z)=sum_(r=1)^n z^r/(2r-1).

Thus beta_0=0. Its actual finite increment, only on 1<=n<=N, is

    d_n=beta_n-beta_(n-1)
       =[(6n+1)+6(6n-1)2^(-n)+(6n+7)4^(-n)]/[3n(2n-1)].       (1)

All denominators in (1) are units in this range. At n=N+1 its denominator
contains p; (1) is not continued there. OLD-R and tau remain the independent
constructors from the frozen papers. The target is still exactly

    kappa+sum h_n beta_n+OLD-R+6tau=0.                          (OPEN)

## 2. Canonical constant forcing and its forced last row

For arbitrary finite vectors h,f the flux

    J_n(f,h)=A_n f_n h_(n+1)-C_(n+1)f_(n+1)h_n

satisfies the all-coefficient identity

    f_n(Lh)_n-h_n(L* f)_n=J_n(f,h)-J_(n-1)(f,h).                (2)

The four zero endpoint coefficients imply J_(-1)=J_N=0 without imposing
extra values on exterior vectors. Therefore sum h_n(L* f)_n=0 for every
finite f. In particular the equation L* Q=1 on all N+1 rows is impossible:
it would give 0=sum h_n=1. This is the actual finite modular cokernel, not
a characteristic-zero obstruction to an unrelated infinite equation.

Define the canonical vector Q by Q_0=0 and the first N rows only:

    Q_(n+1)=[1+B_n Q_n-A_(n-1)Q_(n-1)]/C_(n+1), 0<=n<N.       (3)

At n=0 the exterior term has coefficient zero, so Q_1=1/4. Every divisor
in (3) is a unit. For an explicit finite formula define

    DQ_0=1, DQ_n=product_(k=1)^n C_k=2^n(2n)!,
    K_(a,a-1)=1, K_(a,a-2)=0,
    K_(a,b)=B_b K_(a,b-1)-A_(b-1)C_b K_(a,b-2),
    Q_n=DQ_n^(-1)sum_(j=0)^(n-1) DQ_j K_(j+1,n-1), 1<=n<=N.

Multiplying (3) by DQ_(n+1) gives the forced continuant recurrence
DQ_(n+1)Q_(n+1)=DQ_n+B_n DQ_nQ_n-A_(n-1)C_n DQ_(n-1)Q_(n-1),
which proves the formula. Every factorial stops at 2N=p-1, and no internal
h_n is divided out. Put t=(L*Q)_N=Q_(N-1)-Q_N. Applying the finite pairing
to this actual vector gives

    0=sum_(n=0)^(N-1)h_n+h_N t=1-g+g t.

As g is a unit,

    BOX: (L*Q)_n=1-g^(-1)delta_(n,N),
         Q_(N-1)-Q_N=1-g^(-1).                              (4)

The terminal defect relative to forcing 1 is exactly g^(-1), with the
displayed minus sign. Adding an adjoint homogeneous vector to Q changes
its initial convention but not this defect. Equation (4) uses the supplied
finite homogeneous h, its literal endpoint g, and its literal sum 1. It
is not asserted for arbitrary truncations over Q or for characteristic zero.

There is also an explicit partial-flux normalization. For 0<=n<N, (2)
and (3) imply J_n(Q,h)-J_(n-1)(Q,h)=-h_n. Since J_(-1)=0,

    J_n(Q,h)=-sum_(k=0)^n h_k, 0<=n<N; J_N(Q,h)=0.            (5)

The jump from J_(N-1)=g-1 to J_N=0 equals -(g-1), exactly the terminal
row -h_N(1-g^(-1)). Thus (4) and (5) include the last row, rather than
mistaking the constant-forcing equation for a globally solved adjoint.

## 3. Exact signed three-phase sources

Define three fixed affine numerators and phases

    c=1:   phi_c(n)=6n+1,
    c=1/2: phi_c(n)=36n-6,
    c=1/4: phi_c(n)=6n+7.

For each phase define a finite source s_c(n) on 0,...,N by the explicitly
truncated expression

    s_c(n)=c^n/3 [ 1_(n>=1) phi_c(n)Q_(n-1)
                        -1_(n<N) 4c phi_c(n+1)Q_(n+1) ].    (6)

The indicators mean absent endpoint terms, not products of a zero with an
undefined value. In particular neither d_(N+1) nor Q_(N+1) is introduced.
For 1<=n<N, this is the actual shifted expression; at n=0 its first term
is absent, and at n=N its second term is absent. Write s_n=sum_c s_c(n).

The cancellations inside the legal ranges are

    A_(n-1)d_n=sum_c phi_c(n)c^n/3,             1<=n<=N,
    C_(n+1)d_(n+1)=sum_c 4c phi_c(n+1)c^n/3,   0<=n<N.

Applying the product rule for the actual tridiagonal adjoint gives

    L*(beta Q)_n=beta_n(L*Q)_n
                  -1_(n>=1)A_(n-1)Q_(n-1)d_n
                  +1_(n<N)C_(n+1)Q_(n+1)d_(n+1)
                =beta_n-(beta_N/g)delta_(n,N)-s_n.           (7)

Pair (7) with h and use h_N=g. This proves the fixed terminal and all
three sources, including their signs:

    BOX: sum_(n=0)^N h_n beta_n
           =beta_N+sum_(c in {1,1/2,1/4})sum_(n=0)^N h_n s_c(n).        (8)

For a direct independent sign check, regroup the two terms in (7) by the
increment index. Equations (2) and (5) yield

    sum h_n beta_n=beta_N+sum_(r=1)^N J_(r-1)(Q,h)d_r
                 =beta_N-sum_(r=1)^N [sum_(k=0)^(r-1)h_k]d_r.          (9)

Equation (9) is finite summation by parts, now with a canonically fixed
Green flux. It corroborates (8); it does not evaluate its source pairing.
At the lower endpoint s_0=-d_1=-101/12 (mod p), as Q_1=1/4. At the upper
endpoint s_N=Q_(N-1)d_N, because A_(N-1)=1. These values are checks of
the actual endpoint equations, not interior extrapolations.

On the frozen marked branch 2^N=2^(-N)=-1 and 4^N=1. Hence the actual
terminal numerator in (1) is 26, d_N=26/3 and s_N=26Q_(N-1)/3. The
formal numerator at N+1 would instead be 1/2, while its denominator is
zero. It does not restore the missing update; the omitted forward term
in (6) is essential.

The exact remaining residual interface is therefore

    kappa+beta_N+sum_c sum_n h_n s_c(n)+OLD-R+6tau.             (10)

All five quantities in (10) are independently specified. Its vanishing
is equivalent to (OPEN), and is not proved here. In particular Q was built
from forcing 1 before beta, OLD-R, or tau entered; it was not selected
from a desired target difference.

## 4. A polynomial third-order increment operator

This section first works over Q with the infinite rationally defined
harmonic prefixes, and then states exactly which finite-field windows
inherit the identities. This avoids substituting N=-1/2 into an infinite
identity and treating it as an endpoint theorem.

Let E be the forward shift, E f(n)=f(n+1), and put

    F_n=3n(2n-1)d_n=sum_c phi_c(n)c^n.

The following integer polynomials are fixed:

    p_0(n)=-(216n^3+1548n^2+3882n+3965),
    p_1(n)=1512n^3+9324n^2+18822n+16325,
    p_2(n)=-2(1512n^3+7812n^2+12990n+12515),
    p_3(n)=8(216n^3+900n^2+1434n+1415).

They obey, for each of the three phases separately,

    sum_(j=0)^3 p_j(n)c^j phi_c(n+j)=0.                      (11)

One construction is the signed minors of the 3x4 matrix
M_(c,j)=c^j phi_c(n+j), multiplied by 128/9. Thus (11) follows from
the elementary cofactor identity; direct substitution gives three zero
polynomials. Consequently

    P_F=sum_(j=0)^3 p_j(n)E^j,       P_F F=0,
    T=sum_(j=0)^3 p_j(n)(n+j)(2n+2j-1)E^j,    T d=0.         (12)

The omitted common factor 3 does not affect the polynomial identity.
The coefficients are polynomial, so their reductions do not require any
inverse p_j(n). Some of these coefficients may vanish at finite-field
indices; no global finite-field propagation or uniqueness is asserted.

Since d_(n+1)=beta_(n+1)-beta_n, the explicit order-four prefix operator is

    P_beta=T(n+1,E)(E-1),
    P_beta beta(n)=sum_(j=0)^3 p_j(n+1)(n+j+1)(2n+2j+1)
                                  [beta_(n+j+1)-beta_(n+j)]=0.         (13)

Over Q these identities hold for the harmonic sequence on its natural
positive indices. In the actual finite field, (12) holds only for
1<=n<=N-3, and (13) only for 0<=n<=N-4, where all increments used lie
inside 1,...,N. An empty window asserts nothing. They do not supply the
missing increment at N+1. The separate finite terminal theorem is (4).

For comparison at infinity, the leading coefficient polynomial of P_F is

    216(z-1)(2z-1)(4z-1).

Denominator conjugation and shifting n do not change its roots. The
three prescribed increment phases are therefore 1,1/2,1/4, while (13)
adds one summation phase 1 and has phase roots 1,1,1/2,1/4. These are
characteristic-zero operator invariants, not eigenvalues inferred from
samples in F_p. The three increment modes are rationally independent:
in a rational-coefficient relation the largest nonzero positive phase
dominates every smaller one at integer infinity, which forces its rational
coefficient to vanish, then forces the others to vanish. Thus the
order-three increment operator is minimal over Q(n): the first three
Casoratian columns have a nonzero determinant, namely the cofactor for
p_3 up to its fixed nonzero scale. No such minimality
is asserted for a finite vector in F_p.

## 5. Literal OLD-R has a different fourth-order phase polynomial

Use the unchanged rational constructor

    b_i=2^(-i)(1/6)_i(1/3)_i/(i!)^2,
    D_r=2^(r-1)(r-1)!^2/[18(5/6)_r(2/3)_r],
    Htri_n=sum_(r=1)^n [1+6(n-r)]D_r,
    R_n=2sum_(i=1)^n b_i Htri_i, R_(-1)=R_0=0,
    J_n=R_n-R_(n-1)=2b_n Htri_n.

Here Htri differs from the harmonic H above. The frozen certificate gives
Htri_n-2Htri_(n-1)+Htri_(n-2)=D_n+5D_(n-1), and the third-order J equation

    alpha_n J_(n+1)+bcoef_n J_n+gamma_n J_(n-1)+delta_n J_(n-2)=0,

with the literal integer-polynomial coefficients in the OLD-R paper. Their
leading terms, divided by that of alpha, are respectively

    1, -2, 5/4, -1/4.

Hence the J phase polynomial is

    z^3-2z^2+5z/4-1/4=(z-1)(z-1/2)^2.

Substituting J=Delta R adds the actual summation factor z-1. The existing
fourth-order R certificate therefore has phase polynomial

    (z-1)^2(z-1/2)^2,                                    (14)

whereas the beta certificate has (z-1)^2(z-1/2)(z-1/4). Equal order four
does not identify these two displayed operators. If an operator is
conjugated by a nonzero scalar r(n) in Q(n), then the coefficient of E^j
is multiplied by r(n+j)/r(n) (or its inverse). That quotient tends to 1
at infinity; multiplication of the whole operator by a rational scalar
also preserves its phase roots. Therefore these two displayed certificates
cannot be obtained from one another by a scalar rational gauge at the same
index. This is the exact scope of the phase comparison. It excludes neither
reindexing, a two-index transform, multiple carriers, a common left multiple,
nor an inhomogeneous finite-field certificate. In particular it is not a
global no-go for (OPEN), and does not assume either finite vector has a
minimal fourth-order recurrence.

The OLD-R terminal theorem remains R_(m+1)=R_m modulo p. It sets its next
increment to zero, not its independently fixed value R_m. The beta window
ends at N=3m, and its next increment is undefined under (1). These unequal
terminal mechanisms cannot be equated by continuing either interior rule.

## 6. Concrete legal comparison interfaces

There are two useful next interfaces, each independent of a target fit.

First, define the polynomial operator for the forward OLD-R increment
I_n=J_(n+1)=R_(n+1)-R_n explicitly by

    U=delta_(n+3)+gamma_(n+3)E+bcoef_(n+3)E^2+alpha_(n+3)E^3.

Let T_+=T(n+1,E). Both fourth-order certificates have the same right
summation factor E-1: P_beta=T_+(E-1), P_R=U(E-1). In the
Ore ring Q(n)[E], seek A and B of order at most three satisfying

    A T_+=B U.                                           (15)

Equating coefficients through E^6 is seven rational linear equations in
the eight coefficients of A,B. A nonzero solution exists by linear algebra;
both components must be nonzero because this ring has no zero divisors.
This yields a common left multiple M(E-1) of order at most seven, where
M=A T_+=B U. Clearing denominators produces polynomial identities. Such
clearing never grants division at roots in F_p, and all resulting terminal
corrections must be retained. Equation (15), or a smaller actual LCLM, is
a concrete next symbolic calculation. A common recurrence alone would
still need independently fixed sources and boundaries to prove (OPEN).

There is an immediate exact inhomogeneous interface, without solving (15).
Write u_0,...,u_3 for the four displayed coefficients of U and define

    F_c(n)=sum_(j=0)^3 u_j(n)c^(j+1)phi_c(n+j+1)
                                      /[3(n+j+1)(2n+2j+1)].

Then the actual fixed increments give

    P_R beta(n)=sum_c c^n F_c(n).                          (15a)

This is a coefficientwise source constructed from beta and the literal
OLD-R operator, not a scalar residual fit. Over the finite field its
legal window is 0<=n<=N-4. All denominators there are units; clearing
their product gives a polynomial source identity without licensing extra
indices or inverses of alpha, p_j, or the old P_n. The rational forcing
is explicitly nonzero in each of the three rational modes; the exact
factored coefficients are saved in `INHOMOGENEOUS_SOURCE_COEFFICIENTS.json`.
Where both original finite constructors are guaranteed by their existing
pins, the joint window is 0<=n<=m-3 and

    P_R(beta-R)(n)=sum_c c^n F_c(n).                       (15b)

This window may be empty. It follows only from n+4<=m+1<=N and does not
impose additional values beyond either fixed endpoint. Equations (15a,b)
are precisely the source that a simultaneous or inhomogeneous comparison
must carry, together with independent boundaries.

Second, the already frozen two-index coefficient transform supplies the
actual connection between the N-index Heun pairing and the m-index Gauss
triangle, rather than a conjectured same-index scalar gauge. Put

    a_k=(1/6)_k(1/3)_k/[(1/2)_k k!],
    Tbeta_k=sum_(j=0)^(2k) binom(2k,j)4^j(-3)^(2k-j) beta_(k+j),
    W_k=2^(-k)(1/2)_k Htri_k/k!, W_0=0.

For 0<=k<=m all denominators are units modulo p. The fixed coefficient
triangle h_n=g sum_(k+j=n) a_k binom(2k,j)4^j(-3)^(2k-j) gives

    sum_(n=0)^N h_n beta_n=g sum_(k=0)^m a_k Tbeta_k,
    OLD-R=2sum_(k=0)^m a_k W_k.                            (16)

The second equality follows from v_k=a_k(1/2)_k/k!, not from the target.
The remaining problem can therefore be studied as the actual two-index
source g Tbeta_k+2W_k, with k=0,m and j=0,2k retained, plus the already
fixed kappa and tau boundary. The original tau has its separately fixed
self-adjoint carrier E(t)=t(4t^2-3)C(w(t))/6 and exact boundary
P(a)E(a)Y'(a)=-tau. That carrier is not substituted for either of the
three sources (6).

A successful next unit must derive a flux, an inhomogeneous source identity,
or an independently determined nonzero residual from (10) or (16), including
all finite endpoints. It must not declare a terminal residual zero merely
because an adjoint was constructed. The scalar comparison (OPEN), LIFT,
weighted p^3 supercongruence, raw period normalization and full native X6
propagation all remain OPEN.

## 7. Verification boundary

`check_terminal_three_phase_interface.py` independently checks the Green
row expansion, the product-adjoint signs, source numerator cancellations,
the three polynomial mode identities, the beta shift construction, and the
leading OLD-R phase polynomial. Its only terminal substitution is the
symbolic N=-1/2 coefficient reduction; no prime or modular instance is
computed. An independent reviewer checks the finite Q argument and signs,
and a second reviewer checks the operator and gauge scope. These checks
support only the lemmas stated here. Frozen author checker execution and
target scalar comparison remain absent.
