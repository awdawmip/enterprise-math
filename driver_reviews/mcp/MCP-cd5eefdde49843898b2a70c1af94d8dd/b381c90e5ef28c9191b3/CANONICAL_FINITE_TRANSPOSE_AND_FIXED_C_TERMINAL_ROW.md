# Canonical finite transpose and the single fixed-C terminal row

Status: ONE DIRECTED LOCAL AUXILIARY UNIT / NONCIRCULAR WHOLE-FUNCTIONAL
EVALUATION AND EXACT CANDIDATE CERTIFICATE PROVED / SPECIFIED TERMINAL
IDENTITY UNPROVED / ORIGINAL SCALAR TARGET OPEN. Prepared 2026-10-12 UTC.
Root owns Driver direction, formal state and Source custody. Local author
and helper identities are UNKNOWN; no native Task, Claim, Run, identity,
accepted Result or mathematical Source acceptance is created or asserted.
The finite operators are external classical auxiliary observers; native X6
and separately typed time retain their previous meaning. No prime instance,
fit, old checker, rational ansatz, Source query or remote write is used.

This unit acts on the actual whole six-moment functional, rather than on
another coefficient tail alone. A canonical finite recurrence, with two
fixed zero seeds, evaluates L(D0) through its last row. Combining it with
the independently fixed OLD-R/C scalar gives a concrete adjoint candidate
whose first N-1 rows are proved and whose only remaining row is written
explicitly with the full C tail. The last row is not proved here. In
particular neither existence of an inverse nor a fitted adjoint seed is
offered as the missing scalar proof.

## 1. Frozen actual quantities and the finite map

Consume the preceding density and reciprocal-D units, their proofs and
Root's directed reviews. Intake verified 110 deduplicated inherited frozen
paths and separately pinned the subsequent combined Root review; all old
bytes are preserved. Retain p=6m+1 prime in classes 13 or 19
modulo 24, m>=2, N=3m, and all original conditional premises. Work in F_p.

    h_0=h_N=g=binom(3m,m) != 0, sum h_n=1,
    y(x)=sum_(n=0)^N h_n x^n=gA(rho(x)),
    rho=x(4x-3)^2, A(z)=sum_(i=0)^m a_i z^i,
    sum a_i=1/g, y(1)=1.

The actual prefix density and its prescribed forcing are already proved:

    D0=[y-rho^m]/(1-x), deg D0<=N-1,
    s=T D0=2(4x-1)rho^(m-1), deg s<=N-2.                 (1)

The quotient is polynomial; its leading coefficient is
d_(N-1)=16^m-g, with no assumption that this difference is nonzero.
The entire target in the last density paper is

    L(D0)-F_CM/(9g^2)=kappa+T_m+2W_m/g.                 (OPEN) (2)

Here L is the unchanged six I/J moments; T_m is the fixed beta observer of
rho^m, not a freely selected scalar. OLD-R, W_m, C, tau and F_CM retain
their independent constructors.

Let P_d denote polynomials of degree at most d, paired coefficientwise
with a dual vector. The supplied Heun operator and its product operator are

    H=2x(x-1)(4x-1)d^2+(20x^2-15x+1)d+(4x-1),
    T=H composed with multiplication by (1-x)
     =-2x(1-x)^2(4x-1)d^2
       +(1-x)(36x^2-19x+1)d-2(12x^2-10x+1).

H:P_N -> P_N has kernel span(y), by the already proved Heun recurrence
and its unit forward coefficients. Multiplication by (1-x) maps P_(N-1)
injectively onto the hyperplane of P_N vanishing at 1. Since y(1)=1,
its image intersects ker H only at zero. Consequently

    BOX: T:P_(N-1) -> P_N is injective, rank T=N,
         im T=im H, ker T^transpose=span(4^(-n)h_n).    (3)

The last equality consumes the existing exact Heun symmetrization.
The rank statement alone does not evaluate (2).

For f=(f_0,...,f_N), the exact transpose row indexed 0<=n<=N-1 is

    (T^transpose f)_n
      =n(2n-1)f_(n-1)-2(6n^2+4n+1)f_n
        +(18n^2+37n+20)f_(n+1)
        -4(n+2)(2n+3)f_(n+2).                          (4)

At n=0 the absent lower term has zero coefficient. At n=N-1 the
absent upper term has zero coefficient; reduce its coefficients only,
using N=-1/2, to obtain the actual terminal row

    BOX: (T^transpose f)_(N-1)=6f_(N-2)-17f_(N-1)+5f_N. (5)

There is no f_(N+1), no division by its zero coefficient and no discarded
boundary. Equivalently T^transpose=M^transpose H^transpose, where
(M^transpose u)_n=u_n-u_(n+1).

## 2. The prescribed moments and a fixed zero-seed recurrence

For 0<=n<=N-1 the actual row is lambda_n=L(x^n). In terms of the
unchanged beta increments it is lambda_n=d_(n+1), where

    d_r=[6r+1+6(6r-1)2^(-r)+(6r+7)4^(-r)]/[3r(2r-1)],
    beta_j=sum_(r=1)^j d_r, beta_0=0.                   (6)

This follows directly from all six prescribed I/J terms. All denominators
r and 2r-1 are units through r=N. In the target classes, Euler's criterion
gives 2^N=-1, hence 2^(-N)=-1 and 4^(-N)=1. Thus

    lambda_0=101/12, lambda_(N-1)=26/3.                 (7)

Define a new finite dual vector R without using L(D0), the desired target
or a scalar fit: set R_0=R_1=0, then solve only rows 0,...,N-2 of (4):

    R_(n+2)=[n(2n-1)R_(n-1)-2(6n^2+4n+1)R_n
              +(18n^2+37n+20)R_(n+1)-lambda_n]
                          /[4(n+2)(2n+3)].             (8)

Each divisor is a unit: n+2<=N and 2n+3<=p-2. In particular
R_2=-101/288. The terminal discrepancy is the *computed* scalar

    delta=26/3-[6R_(N-2)-17R_(N-1)+5R_N].              (9)

It is not assumed zero. The complete exact finite row statement is

    T^transpose R=lambda-delta epsilon_(N-1).           (10)

Thus delta is determined from the prescribed moments by legal finite
rows, with no reference to an unknown target value.

## 3. Whole-functional evaluation, and the provenance of its seed

Let Q be the *old*, independently constructed canonical Heun dual:

    Q_0=0, H^transpose Q=1-g^(-1)epsilon_N.

Its first row gives Q_1=1/4. The actual terminal defect is retained;
applying M^transpose gives

    BOX: T^transpose Q=g^(-1)epsilon_(N-1).             (11)

There is a noncircular complete transpose certificate, constructed from
the already computed delta, namely

    F=R+g delta Q, F_0=0, F_1=g delta/4,
    T^transpose F=lambda.                              (12)

This proves existence by actual legal rows, not by naming an inverse.
Its seed is nevertheless a whole observer quantity, which must not be
silently replaced by the desired scalar. Here is its exact provenance.
Put u=H^transpose R. Since u_0=0 and its consecutive differences are
lambda_n on n<N-1,

    u_j=-beta_j (j<N), u_N=-beta_N+delta.

Finite Heun duality with the supplied y, including its terminal row,
gives 0=<h,u>=-sum h_j beta_j+g delta. Hence

    g delta=sum_(j=0)^N h_j beta_j
            =sum_(n=0)^(N-1) lambda_n sum_(j=n+1)^N h_j. (13)

The last expression is the actual finite h-tail pairing obtained by
exchanging sums, not an independent evaluation of the target. The
normalization uses h_N=g and sum h=1 exactly. Replacing g delta by
-kappa-OLD-R-6tau would assert the open scalar target.

The terminal source in (1) is -H rho^m. Write M=16^m (a unit). Its
literal coefficient duality, with no derivative integration, gives

    <Q,s>=M/g-1,
    <R,s>=T_m-M delta,
    L(D0)=<F,s>=T_m-g delta.                            (14)

For the second identity, pair H^transpose R=-beta+delta epsilon_N
with rho^m: its beta pairing is exactly the old fixed T_m, and its
last coefficient is M. These are genuine whole-functional evaluations
from the prescribed zero-seed recurrence. They remain valid when M=g;
no division by M-g is used. They do not yet evaluate delta in the fixed
reciprocal-D/C kernel.

An explicit coefficient-only form of the new known source pairing is

    <R,s>=2 sum_(l=m-1)^(N-2) R_l[4b_(l-m)-b_(l-m+1)],
    b_j=binom(2m-2,j)4^j(-3)^(2m-2-j) if 0<=j<=2m-2,
        and b_j=0 otherwise.                           (15)

It uses no high or undefined moment. Equation (14) also yields the
exact formula L(D0)=(g/M)<R,s>+(1-g/M)T_m.

The terminal matching in (14) is essential, and was explicitly challenged
by Root. The frozen cubic has leading coefficient 16, so
[rho^m]_N=4^(2m)=16^m, and (10) paired with the actual D0 gives
L(D0)=<R,s>+(16^m-g)delta. Independently, the *old* observer is

    T_m=sum_(j=0)^(2m)binom(2m,j)4^j(-3)^(2m-j)beta_(m+j)
       =<beta,rho^m>
       =L((1-rho^m)/(1-x)).

Its two triangle endpoints and all moment denominators were established
in the frozen fixed-triangle paper, section2; this is not a definition
from the current target. Pairing H^transpose R=-beta+delta epsilon_N
with the independent terminal polynomial proves
<R,s>=-<H^transpose R,rho^m>=T_m-16^m delta. Thus the full
16^m delta term cancels explicitly, and is never dropped. The separate
challenge/correction record preserves Root's review and acknowledgement.

## 4. A fixed-C candidate, retaining the entire low and high kernel

Consume the existing reciprocal-D reflection, literal Wilson
normalization eta_N=-1/(18g^2), and M_R-3tau=eta_N F_CM.
Define the following scalar only from the *already independent* quantities:

    K=kappa+2W_m/g+F_CM/(9g^2)
     =kappa+OLD-R+6tau.                                 (16)

This equality is a proved old constructor comparison: M_R=W_m/g-OLD-R/2.
It does not use (2) or assign C, tau or F_CM from a residual.

For clarity, the actual fixed-kernel expression used in (16) is

    F_CM=sum_(r=1)^m e_(N-r) q_r/(r t_r)
          -6V'_* sum_(r=1)^N e_(N-r) E_(r-1)^adj(1/2),
    q_r=(t_m/g)[1+6(m-r)]
               -sum_(i=r)^m a_i t_i[1+6(i-r)],
    E_(r-1)^adj(c)=sum_(j=0)^(r-1)e_j c^j,
    e_j=(2/3)_j(5/6)_j/[(3/2)_j j!], 0<=j<N.            (17)

Both cutoffs in (17) are literal: reciprocal-D contributes r<=m,
the fixed C double prefix contributes *all* r<=N. In particular the
range m<r<=N is retained. No e_N is introduced, no C or derivative is
inverted, and V'_* is the unchanged V'(1/2). The old fixed-C identity
C_*=(4/(9g^2))sum_(r=1)^N e_(N-r)E_(r-1)^adj(1/2) and
tau=-C_*V'_*/4 verify its tau term directly.

Now the concrete prescribed adjoint candidate is

    J=R-KQ, J_0=0, J_1=-K/4.

Its seed uses only the independent original constructors in (16)-(17),
not L(D0), delta, the target value, or a fitted scalar. Equations (10)-(11)
prove every one of its rows, including its precise terminal defect:

    BOX: T^transpose J=lambda-(delta+K/g)epsilon_(N-1).  (18)

In particular the first N-1 rows are fully proved. This is an explicit
candidate certificate, not a claimed complete one. A complete certificate
exists from (12), but its seed is g delta/4; asserting that this equals
-K/4 would be the unproved comparison. Adding any multiple of
4^(-n)h_n, the sole null direction in (3), changes none of the rows or
the discrepancy. The terminal equation cannot be fixed by that freedom.

## 5. Exactly one remaining finite identity

The precise new remaining lemma is the following actual last row, with
R fixed by the legal zero-seed recurrence (8) and every C/OLD-R term
fixed before the comparison:

    BOX: 6R_(N-2)-17R_(N-1)+5R_N
      =26/3+kappa/g+2W_m/g^2
        +(1/(9g^3))sum_(r=1)^m e_(N-r)q_r/(r t_r)
        -(2V'_*/(3g^3))sum_(r=1)^N
                              e_(N-r)E_(r-1)^adj(1/2).  (UNPROVED) (19)

This is a specific finite row identity, not a request to prove existence
of an inverse, and not a universal rational ansatz. Its residual is
delta+K/g. The exact original normalized scalar residual is

    kappa+sum h beta+OLD-R+6tau
      =kappa+T_m+2W_m/g+F_CM/(9g^2)-L(D0)
      =g(delta+K/g).                                   (20)

Equivalently, the independent known-source kernel comparison to prove is

    <R,s>=T_m+(16^m/g)[kappa+2W_m/g+F_CM/(9g^2)].       (UNPROVED) (21)

Equations (15) and (17) make both sides finite and explicit. Since 16^m
and g are units, (19), (21), completion of the candidate (18), and the
original scalar comparison are equivalent. None is proved or disproved
by the current unit. This finite row is the precise mathematical gap.

All old Frobenius corrections stay in force: the actual odd top moment
has its 16^m term, the fixed full-log complement and terminal Q defect
remain, and the independently defined cubic b_p and density d_p tails
are neither dropped nor assigned zero. The present coefficient-dual
calculation does not recover a high-degree polynomial from its derivative;
it therefore makes no new Frobenius integration choice. Any subsequent
proof comparing (19) with a pulled-back C concomitant must retain those
actual tails. It is insufficient to keep only r<=m in (17), to fit J_1,
or to infer its terminal row from surjectivity of T^transpose.

## 6. Verification and scope

The new main script passes 85 exact symbolic checks: product/monomial
rows, transpose coefficient duality, the actual top row, all three phases
of the prescribed lambda, canonical forward rows over Q with no prime
or terminating full solution, Q/candidate/source signs, the complete
fixed-C kernel scalar, exact generic source endpoints, literal cubic
leading coefficients, old triangle observers and generic quotient/observer
terminal matching. The proof of
rank is conditional on the already supplied finite y and unit recurrence;
no characteristic-zero terminating Gauss solution is substituted.

The independent helper passes 31+18=49 new exact checks and derives and challenges
the rows, rank, zero seeds, source evaluation, fixed-K candidate and actual
terminal lambda in its own new files. The combined new verification is
85+49=134 checks, including its separate directed Root top-cutoff challenge.
This is directed collaborative verification, not a blind
native peer-review claim. Final pins and the post-work byte audit accompany the
Root handoff. The scalar target and all mathematical parents remain OPEN;
no further unit is started before Root consumes this one.
