# Fixed-triangle inhomogeneous fluxes with the genuine Frobenius terminal term

Status: LOCAL MATHEMATICAL RESEARCH / NEW FINITE SOURCE AND TERMINAL LEMMAS
PROVED / FIXED SCALAR COMPARISON OPEN. Prepared 2026-10-12 UTC.

This continues the two frozen local units listed in the byte audit. Native
Researcher, Task, Claim, Run, and accepted Result are UNKNOWN; the local
collaboration labels are not registered identities. No Source or native
write, provider query, prime instance, scalar fit, or repeated prime campaign
is claimed. The finite fields and operators remain external auxiliary
classical arithmetic observers. Native X6 and separately typed time retain
their established meanings. LIFT, the weighted p^3 supercongruence, raw
period normalization, and complete native X6 propagation remain OPEN.

The bounded advance is an actual source calculation through the *fixed*
two-index transform: the observer increment becomes two first-order
inhomogeneous moment systems, with only the endpoint phases 1 and 1/2.
Their polynomial fluxes are explicit below. The last odd-moment flux has
degree p and contributes a precisely determined Frobenius term. This is
not removable by multiplying an undefined next moment by a zero terminal
coefficient. A complementary finite Gauss adjoint carries these sources
and the unchanged OLD-R source into one endpoint-correct residual.
The residual's vanishing is not proved.

## 1. Independently checked inputs and literal normalization

Retain the conditional premises of the frozen self-adjoint Heun unit. Let
p=6m+1 be prime in the classes 13 or 19 modulo 24, N=3m=(p-1)/2, and work
over F_p. Then m>=2. The finite Heun sequence is still the literal
coefficient sequence of y(u)=V((1-u)(1-4u)^2), with

    A_n=(n+1)(2n+1), B_n=10n^2+5n+1, C_n=4n(2n-1),
    (Lh)_n=A_n h_(n+1)-B_n h_n+C_n h_(n-1)=0,
    h_(-1)=h_(N+1)=0,
    h_0=h_N=g=binom(3m,m) != 0, sum_(n=0)^N h_n=1.

In particular g is not replaced by 1. The preserved canonical Heun
constant-forcing adjoint has the actual full equation

    L*Q=1-g^(-1)delta_N, Q_0=0.

Its defect is still present, regardless of whether the Heun or Gauss
coordinate is used. The four zero endpoint coefficients, the Green sign,
the self-adjoint pullback and literal tau concomitant, the exact beta
increment, and all three saved coefficientwise OLD-R
operator sources were independently checked in the new script. The two
manifests and 36 pinned input/output entries passed a byte audit. No
frozen checker was read or executed. No AGENTS.md was found in the
applicable ancestor directories /, /workspace, or this local research
directory's parent.

The entire fixed observer remains

    Lambda+2q_3=kappa+sum_(n=0)^N h_n beta_n,
    kappa=2q_2-3q_3-8O_N(1/2),
    beta_n=2H_n(1/2)+8O_n(1/2)-H_n(1)/3+8O_n(1)/3
                                  -7H_n(1/4)/3+20O_n(1/4)/3,
    H_n(c)=sum_(r=1)^n c^r/r,
    O_n(c)=sum_(r=1)^n c^r/(2r-1).

OLD-R and tau retain their independent old constructors. Their comparison
is exactly

    kappa+sum h_n beta_n+literal OLD-R+6tau=0.              (OPEN)

## 2. The fixed triangle, not a same-index scalar gauge

Set

    a_k=(1/6)_k(1/3)_k/[(1/2)_k k!],
    b_(k,j)=binom(2k,j)4^j(-3)^(2k-j),
    z(x)=x(4x-3)^2,
    T_k=sum_(j=0)^(2k) b_(k,j) beta_(k+j), 0<=k<=m.

The frozen coefficient triangle, including both j endpoints, gives

    sum_(n=0)^N h_n beta_n=g sum_(k=0)^m a_k T_k,
    sum_(k=0)^m a_k=1/g.                                  (1)

The second equation follows by applying that same triangle to the literal
sum h=1; equivalently z(1)=1. It is not a new normalization. Every a_k
through k=m is a unit.

For any polynomial f(x)=sum_l f_l x^l define, only when the displayed
coefficient denominators are units,

    I_c(f)=sum_l f_l c^(l+1)/(l+1),
    J_c(f)=sum_l f_l c^(l+1)/(2l+1).                       (2)

Both objects lie in the base field. The latter can also be understood as
sqrt(c) times the canonical primitive of f(t^2) evaluated at sqrt(c),
but no square root is needed for definition (2).

The exact binomial relations sum_j b_(k,j)=1 and
sum_j b_(k,j)x^(k+j)=z(x)^k prove

    sum_j b_(k,j) H_(k+j)(c)=I_c((1-z(x)^k)/(1-x)),
    sum_j b_(k,j) O_(k+j)(c)=J_c((1-z(x)^k)/(1-x)).          (3)

For example H_n(c)=I_c((1-x^n)/(1-x)); the analogous equation for O
follows coefficient by coefficient. The quotient in (3) is polynomial
because z(1)=1. For k<=m its degree is at most 3k-1<=N-1. Thus all
I denominators are <=N and all J denominators are <=p-2. In particular
(3) is legal at k=m and establishes the fixed T_m without a forward
extension of beta.

Use the all-coefficient identity

    1-z(x)=(1-x)(1-4x)^2.

Put f_k(x)=(1-4x)^2 z(x)^k for 0<=k<m and define

    U_k=2I_(1/2)(f_k)-I_1(f_k)/3-7I_(1/4)(f_k)/3,
    V_k=8J_(1/2)(f_k)+8J_1(f_k)/3+20J_(1/4)(f_k)/3.

Subtract (3) at successive k. The new exact observer source is

    BOX: T_(k+1)-T_k=U_k+V_k, 0<=k<m.                    (4)

The degree is 3k+2<=N-1, so every denominator in (4) remains legal
through k=m-1. This last increment uses beta_N and no beta_(N+1).
The fixed initial data are

    T_0=0, U_0=-23/36, V_0=308/45,
    T_1-T_0=1117/180.                                    (5)

These numbers are direct polynomial moments of f_0=(1-4x)^2. None was
chosen from the scalar comparison.

## 3. Explicit first-order polynomial moment fluxes

Define the following polynomial coefficients; their exact expanded
versions are also saved in POLYNOMIAL_MULTIPLE_FLUX_COEFFICIENTS.json:

    D_H(k)=6(k+2)(3k+4)(3k+5),
    B_H(k)=27(k+2)(k+1)(2k+1),
    R_H(k,x)=(4x-3)[
       1152k^2 x^4-2016k^2 x^3+1080k^2 x^2-234k^2 x+18k^2
       +3456k x^4-5856k x^3+3000k x^2-618k x+45k
       +2560x^4-4224x^3+2112x^2-408x+18],

    D_O(k)=3(2k+3)(6k+7)(6k+11),
    B_O(k)=54(2k+3)(k+1)(2k+1),
    R_O(k,x)=2(4x-3)[
       2304k^2 x^4-4032k^2 x^3+2160k^2 x^2-468k^2 x+36k^2
       +6144k x^4-10560k x^3+5568k x^2-1188k x+90k
       +4032x^4-6832x^3+3588x^2-765x+54].

There are two exact identities, proved by substituting the displayed
polynomials and expanding their coefficients:

    partial_x[x z(x)^k R_H(k,x)]
             =D_H(k) f_(k+1)(x)-B_H(k) f_k(x),            (6)

    partial_t[t z(t^2)^k R_O(k,t^2)]
             =2[D_O(k) f_(k+1)(t^2)-B_O(k) f_k(t^2)].    (7)

More explicitly, after canceling the common z^k, (6) reduces to
x R_H'+R_H+k(12x-3)R_H/(4x-3)=(1-4x)^2(D_H z-B_H).
For (7) the canceled row is
x R_O'+R_O/2+k(12x-3)R_O/(4x-3)=(1-4x)^2(D_O z-B_O).
Each R is
divisible by 4x-3, so these are polynomial identities without a pole.
They are not obtained by division at an apparent critical point.

Canonical integration over the legal window 0<=k<=m-2 gives, for
c=1,1/2,1/4 separately,

    D_H I_c(f_(k+1))-B_H I_c(f_k)
                          =c z(c)^k R_H(k,c),            (8)
    D_O J_c(f_(k+1))-B_O J_c(f_k)
                          =(c/2) z(c)^k R_O(k,c).        (9)

The lower flux vanishes literally: both polynomial fluxes contain x or
t. The primitive in (6) has degree at most 3k+6<=N, and in (7) at
most 6k+11<=p-2. Thus no multiple of x^p or t^p is discarded in this
window. All D_H and D_O factors here are positive integers smaller
than p, apart from the units 2 and 3, so they are units. These equations
and the fixed initial moments determine U,V through their last legal
values. No roots of higher-order OLD-R operator coefficients are divided
out.

The six flux endpoint values simplify substantially:

    R_H(k,1)=27k+58,
    R_H(k,1/2)=9k^2+30k+26,
    R_H(k,1/4)=16,
    R_O(k,1)=2(54k+77),
    R_O(k,1/2)=36k^2+96k+67,
    R_O(k,1/4)=16.

Because z(1)=z(1/4)=1 and z(1/2)=1/2, combining (8)-(9) with the
literal U,V coefficients yields the small inhomogeneous systems

    BOX: D_H(k)U_(k+1)-B_H(k)U_k
       =2^(-k)(9k^2+30k+26)-9k-86/3,                    (10)

    BOX: D_O(k)V_(k+1)-B_O(k)V_k
       =2^(1-k)(36k^2+96k+67)+144k+656/3,               (11)

again only for 0<=k<=m-2. The source contains only the two *actual
transformed endpoint phases*, 1 and 1/2. This identifies a concrete
legal transform outside the earlier same-index scalar-gauge comparison.
It does not show that these sequences coincide with OLD-R, and does not
assume equal minimal recurrences.

The H-only polynomial relation (8) can separately be extended to
k=m-1 using the independently defined I_c(f_m): its primitive degree
is N+3<=p-1. This supplies no extension of beta or of the J moment.
We do not use that extra H-only value to manufacture T_(m+1).

## 4. The exact last odd moment and its Frobenius defect

At the actual last increment k=m-1, reduction modulo p gives
k=-7/6. The cleared odd-moment coefficients become

    D_O=0, B_O=8,
    R_T(x):=R_O(-7/6,x)=4(4x-3)(16x^2-8x-1).             (12)

The next J moment J_c(f_m) would contain a denominator 2N+1=p;
it is undefined under (2). Therefore setting D_O J_c(f_m)=0 is
not a legal terminal step.

Instead set G(x)=z(x)^(m-1)R_T(x). Its degree is N and its leading
coefficient is

    C_top=16^(m-1)*256=16^(m+1).

The genuine specialized polynomial equation (7) is

    (1+2x partial_x)G(x)=-16 f_(m-1)(x).                  (13)

It has one exceptional coefficient: (1+2x partial_x)x^N=0 because
2N+1=p. Remove that *explicit* top term and put
G_low=G-C_top x^N. Now degree G_low<=N-1, and the coefficientwise
identity

    J_c((1+2x partial_x)G_low)=c G_low(c)

is legal: every denominator 2l+1 for l<=N-1 is a unit. Apply it to
(13). The exact all-endpoint terminal theorem is

    BOX: 16 J_c(f_(m-1))
       =16^(m+1)c^(N+1)-c z(c)^(m-1)R_T(c).              (14)

Equivalently the odd polynomial flux t G(t^2) has degree p with
coefficient 16^(m+1) on t^p. Its derivative is -16 f_(m-1)(t^2),
but its canonical primitive is obtained only after removing that t^p
term. Formula (14) retains precisely that Frobenius difference. It is
not a choice of integration constant or a scalar target fit.

On the frozen marked branch, 2^N=-1 and 4^N=1. The three independent
endpoint evaluations R_T(1)=28, R_T(1/2)=4, R_T(1/4)=16 give

    J_1(f_(m-1))=16^m-7/4,
    J_(1/2)(f_(m-1))=-16^m/2-2^(-m-2),
    J_(1/4)(f_(m-1))=16^m/4-1/4.                         (15)

Consequently the literal combined final odd source is evaluated:

    BOX: V_(m-1)=(16^m-19)/3-2^(1-m).                    (16)

It follows that the actual top transformed observer increment is

    T_m-T_(m-1)=U_(m-1)+(16^m-19)/3-2^(1-m).             (17)

No assertion about T_(m+1) is made. Equations (14)-(17) are new finite
terminal values proved independently of OLD-R and tau, not a proof of
their comparison. The independent helper checked (12)-(16) by the
base-field coefficient argument above.

## 5. A shared finite Gauss adjoint for observer and literal OLD-R

The independently derived companion paper in independent-check proves
the following finite coefficient interface. It is repeated here to give
the exact residual a self-contained meaning.

Put lambda_k=9(k+1)(2k+1), mu_k=(6k+1)(3k+1). Then
lambda_k a_(k+1)=mu_k a_k for k<m. At k=m the literal finite operator
has zero row because mu_m=0 and there is no a_(m+1) term in the fixed
truncation. Its adjoint is

    (K*F)_k=1_(k>=1)lambda_(k-1)F_(k-1)-mu_k F_k.

Fix F from constant forcing alone by

    F_0=-1,
    F_k=[lambda_(k-1)F_(k-1)-1]/mu_k, 1<=k<m,
    F_m=0.

The last convention is irrelevant because mu_m=0. Every divided mu_k
for k<m is a unit. The all-endpoint Green identity and (1) force

    BOX: K*F=1-(g a_m)^(-1)delta_m.                       (18)

Its flux j_k=lambda_k F_k a_(k+1), for k<m, equals
-sum_(r=0)^k a_r; j_(-1)=j_m=0. Thus this coordinate has its own
literal normalized terminal defect, in addition to the preserved Heun
defect and the moment Frobenius term. None is assumed zero.

For any prescribed finite Ubar_0,...,Ubar_m, the product rule proves

    sum_(k=0)^m a_k Ubar_k
      =Ubar_m/g+sum_(k=1)^m a_k lambda_(k-1)F_(k-1)
                                      (Ubar_k-Ubar_(k-1)).           (19)

Its lower increment term is absent; its upper endpoint is Ubar_m,
not an extrapolated increment. Apply it to T and to the original
OLD-R coefficient source defined next.

Retain literally

    D_r=2^(r-1)(r-1)!^2/[18(5/6)_r(2/3)_r], 1<=r<=m,
    Htri_k=sum_(r=1)^k[1+6(k-r)]D_r,
    Ptri_k=sum_(r=1)^k D_r, Htri_0=Ptri_0=0,
    t_k=2^(-k)(1/2)_k/k!, W_k=t_k Htri_k, W_0=0.

The fixed old constructor is OLD-R=2sum_(k=0)^m a_k W_k. Its actual
source increment is

    Z_k:=W_k-W_(k-1)
       =t_k[D_k+6Ptri_(k-1)
                    -(2k+1)Htri_(k-1)/(2k-1)], 1<=k<=m.  (20)

This follows from Htri_k-Htri_(k-1)=D_k+6Ptri_(k-1) and
t_k/t_(k-1)=(2k-1)/(4k). It retains the r=k diagonal coefficient 1,
including D_m. At k=1, t_1=1/4, D_1=1/10, and Z_1=1/40;
both prefixes vanish. There is no division by a terminal zero and no
identification of R_m with the zero next increment R_(m+1)-R_m.

Combining (4), (19), and (20) gives the new exact multiple-source residual

    BOX: kappa+sum h_n beta_n+literal OLD-R+6tau
      =kappa+T_m+2W_m/g+6tau
       +sum_(k=1)^m a_k lambda_(k-1)F_(k-1)
                         [g(U_(k-1)+V_(k-1))+2Z_k].       (21)

All endpoints are fixed: n=0,N, k=0,m, j=0,2k, and r=1,m. The upper
odd term V_(m-1) has the explicit value (16); T_m is fixed by (3),
not by continuing (4). The canonical F predates beta, OLD-R, and tau.
Its terminal correction (18) is what gives T_m and 2W_m/g in (21).

The separately fixed self-adjoint tau carrier remains
E(t)=t(4t^2-3)C(w(t))/6, with

    P(t)=(t^2-1)(4t^2-1),
    P(a)E(a)Y'(a)=-tau,
    a^2=1/2, a^p=-a, w(a)=1/2.

That literal normalized boundary contributes 6tau to (21). It has not
been replaced by one of the moment or coefficient fluxes.

## 6. Exact remaining lemma and obstruction to an interior-only proof

Equation (21) is a proved identity for the *unchanged* scalar residual.
It is not a proof that the residual is zero, nor a proved nonzero scalar
residual. The unresolved comparison is now the following precise lemma:

    For the fixed sources U,V from (5),(10),(11),(16), the literal
    reciprocal-triangle source Z from (20), and the canonical F from
    (18), prove

    sum_(k=1)^m a_k lambda_(k-1)F_(k-1)
                   [g(U_(k-1)+V_(k-1))+2Z_k]
          =-kappa-T_m-2W_m/g-6tau.                         (22)

Here U,V are independently determined by their legal inhomogeneous
systems and canonical polynomial definitions; no source is a discrepancy
selected from (22). A successful next proof can use simultaneous fluxes
between (10)-(11), the reciprocal D system, and the existing reverse
Gauss carrier C. It must separately derive the right side from their
fixed boundaries, including the c^(N+1) term in (14), the g-dependent
coefficient defect in (18), and the original tau concomitant.

Two specific shortcuts are now algebraically ruled out. Constant
forcing on every row of either finite adjoint contradicts its nonzero
fixed total sum. Continuing (9) to its last row and declaring its next
term zero omits the degree-p contribution 16^(m+1)c^(N+1). These are
obstructions to those specified incomplete arguments, not impossibility
theorems for (22), finite-field certificates, or multiple carriers.

The prior characteristic-zero same-index phase mismatch is not a global
obstruction: the fixed triangle has explicitly changed its relevant
endpoint phases. Conversely, that change alone supplies no scalar value.
The rigorous output of this bounded unit is (4), (6)-(17), (18)-(21),
and the precise remaining lemma (22). The final target and all parents
remain OPEN.

## 7. Meaningful verification and independence scope

The main new symbolic script passed 124 exact checks: preserved input
Green and terminal coefficients, self-adjoint pullback and tau concomitant;
all three saved OLD-R forcing
coefficients; new binomial moment identities; both polynomial fluxes;
six endpoint flux values; the combined two-phase inhomogeneous sources;
fixed initial moments; and the terminal coefficient, degree, and odd
source simplification. Rational polynomial examples at k=0,...,5 only
corroborate the all-k proofs. No prime is instantiated and no scalar
comparison is fitted.

The independent helper derived the finite Gauss adjoint, literal OLD-R
increment and combined residual separately, then checked the moment
identity and the transmitted odd terminal formula in its own new script:
80 exact checks passed. The formula was transmitted before that terminal
review, so this is directed independent algebra checking, not blind
final peer review. Both scripts instantiate zero primes, import no
frozen checker, and claim no evidence for the vanishing in (22).

Input byte pins are rechecked after the unit is saved. Final local pins
and the root handoff include all new artifacts. No local research result
is presented as a Source publication, native claim, accepted operational
Result, or complete parent theorem.
