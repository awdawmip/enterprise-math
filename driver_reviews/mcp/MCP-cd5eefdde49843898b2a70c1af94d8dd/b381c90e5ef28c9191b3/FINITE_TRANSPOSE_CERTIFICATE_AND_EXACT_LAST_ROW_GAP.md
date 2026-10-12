# Independent finite transpose certificate and the exact last-row gap

Status: ONE BOUNDED LOCAL FUNCTIONAL UNIT / FINITE RANK, ZERO-SEED
FUNCTIONAL CERTIFICATE AND INDEPENDENT CANDIDATE PROVED / TERMINAL
COMPARISON OPEN. Prepared 2026-10-12 UTC. Only this independent-check
directory is written. No prime, scalar fit, old checker, Source fetch,
chat action or native mutation occurs. Native identity is UNKNOWN.

## 1. The actual finite map, rank, and left null vector

Retain p=6m+1 in the frozen classes, m>=2, N=3m, h_0=h_N=g unit,
sum h=1, and y(1)=1. All polynomial spaces below are finite external
observers over F_p. Use exactly the existing H and T=H composed with
multiplication by (1-x). The finite H coefficient matrix on P_N is the
frozen Heun matrix, of rank N with kernel spanned by y.

Multiplication by 1-x injects P_(N-1) into P_N, with image q(1)=0.
Since y(1)=1, that image intersects ker H only at zero. Therefore

    BOX: T:P_(N-1) -> P_N is injective of rank N,
         image T=image H,
         ker T^T=span{w}, w_n=4^(-n)h_n, 0<=n<=N.       (1)

The last identity follows from H^T(diag(4^(-n))h)=0. It includes the
terminal endpoints; w_0=w_N=g. Thus T^T is surjective onto every finite
functional on P_(N-1). Surjectivity is not a comparison with F_CM.

Its exact monomial column is

    T x^n=n(2n-1)x^(n-1)-2(6n^2+4n+1)x^n
       +(18n^2+37n+20)x^(n+1)-4(n+2)(2n+3)x^(n+2).      (2)

Absent boundary terms are omitted. At n=N-1=-3/2, the highest
coefficient is zero, proving the stated codomain P_N. Hence its actual
transpose rows are

    (T^T f)_n=1_(n>=1)n(2n-1)f_(n-1)-2(6n^2+4n+1)f_n
       +(18n^2+37n+20)f_(n+1)
          -1_(n<N-1)4(n+2)(2n+3)f_(n+2), 0<=n<N.

The true last row is

    BOX: (T^T f)_(N-1)=6f_(N-2)-17f_(N-1)+5f_N.         (3)

There is no f_(N+1) term. The forward divisors 4(n+2)(2n+3) are units
for 0<=n<=N-2: n+2<=N and 2n+3<=p-2.

## 2. The genuine functional and the canonical zero-seed partial adjoint

For the fixed six-moment functional L define only its actual finite
coefficients lambda_n=L(x^n), 0<=n<N. They are the legal frozen beta
increments lambda_n=beta_(n+1)-beta_n, explicitly

    lambda_n=[(6n+7)+6(6n+5)2^(-n-1)+(6n+13)4^(-n-1)]
                                             /[3(n+1)(2n+1)].   (4)

Every denominator is a unit. The actual first and last values are

    lambda_0=101/12,
    BOX: lambda_(N-1)=26/3.                              (5)

The second uses only N=-1/2 in coefficients and the retained branch
2^(-N)=-1, 4^(-N)=1. No lambda_N is defined: its denominator would
contain p.

Construct a partial adjoint u from fixed zero seeds

    u_0=u_1=0,
    (T^T u)_n=lambda_n, 0<=n<=N-2.                       (6)

Solve each row for u_(n+2) by dividing by 4(n+2)(2n+3); its numerator is
the lower, diagonal and first-forward terms minus lambda_n. The lower
term is absent at n=0. This uniquely determines u_2,...,u_N using only
the actual functional and legal coefficients. In particular
u_2=-101/288. Neither seed uses L(D0), K, F_CM or a target discrepancy.

Its actual terminal defect is retained, rather than declared zero:

    epsilon=26/3-[6u_(N-2)-17u_(N-1)+5u_N],
    T^T u=lambda-epsilon e_top, e_top=delta_(n,N-1).     (7)

Factor T^T=M_(1-x)^T H^T. If b=H^T u, the first rows give
b_0=0 and b_n-b_(n+1)=lambda_n. Therefore b_n=-beta_n for 0<=n<N,
while the actual final value is b_N=epsilon-beta_N. Finite Heun
adjunction pairs b to zero against h, giving the exact obstruction

    BOX: g epsilon=sum_(n=0)^N h_n beta_n.               (8)

This value is not assumed zero or inferred from constructing u.

## 3. A whole-functional certificate without a fitted seed

Keep the actual fixed polynomial D0=(y-rho^m)/(1-x), with
rho=x(4x-3)^2, and the terminal observer T_m. If
v_n=[x^n]rho^m, then T_m=sum_(n=0)^N v_n beta_n and v_N=16^m.
The coefficient identity (1-x)D0=y-rho^m and finite summation by parts
give

    sum h_n beta_n=T_m-L(D0),
    [x^(N-1)]D0=16^m-g.

Define the actual source and its independently fixed zero-seed pairing

    s=T D0=2(4x-1)rho^(m-1), deg s=N-2,
    U_source=sum_(n=0)^N u_n[x^n]s.

Because b=H^T u pairs to zero against y and has exactly the terminal
coefficient described above, it proves

    U_source=-sum_(n=0)^N v_n b_n=T_m-16^m epsilon.

Combining with (8), using only unit 16^m, gives a genuine entire
functional certificate whose seeds are independent of the value:

    BOX: L(D0)=(g/16^m)U_source+(1-g/16^m)T_m.           (9)

This uses no inverse of 16^m-g and has no exception when that coefficient
vanishes. It is an exact representation of the whole six-moment
functional through the independently defined finite transpose source
pairing and its independently known terminal T_m. It does not evaluate
U_source against the original C/F_CM source.

## 4. The independent CM candidate and one precise unproved last row

Consume the preceding fixed common-kernel source and literal normalization
eta_N=-1/(18g^2). Define the independent scalar

    K=kappa+2W_m/g+F_CM/(9g^2)=kappa+OLD-R+6tau.          (10)

The equality follows from the frozen M_R-3tau=eta_N F_CM and
OLD-R=2W_m/g-2M_R. In particular K has independent old constructors;
it is not defined from L(D0), epsilon, or the desired comparison. Its
low r<=m, high r<=N and inherited Frobenius information remain fixed.

The old canonical constant-forcing Heun adjoint Q has Q_0=0,Q_1=1/4
and H^T Q=1-g^(-1)delta_N. The finite difference factorization proves

    T^T Q=g^(-1)e_top.                                   (11)

The honest independent candidate is therefore

    f_candidate=u-KQ,
    f_candidate,0=0, f_candidate,1=-K/4,
    T^T f_candidate=lambda-(epsilon+K/g)e_top.           (12)

Its first rows and seeds are independently fixed and valid. Its last
row is not proved by choosing those seeds. The exact remaining lemma
is the explicit finite identity

    BOX: 6u_(N-2)-17u_(N-1)+5u_N=26/3+K/g.              (OPEN) (13)

Equivalently epsilon=-K/g, or

    BOX: U_source=T_m+(16^m/g)K.                         (OPEN) (14)

These are the actual missing terminal/source comparisons, with every
quantity independently constructed before evaluation.

To challenge automatic inverse claims explicitly, the always-solvable
full transpose would instead use u+g epsilon Q. Its second seed would
be g epsilon/4=[T_m-L(D0)]/4. Using that seed to proclaim the desired
comparison simply hides the unknown functional in the seed. Likewise
the independent candidate (12) leaves exactly its displayed last row;
one cannot assert its closure from transpose surjectivity.

In fact the original density residual is precisely

    BOX: kappa+T_m+2W_m/g-L(D0)+F_CM/(9g^2)
           =K+T_m-L(D0)=g(epsilon+K/g).                 (15)

Since g is a unit, its vanishing is equivalent to (13), not proved by
the construction. The candidate and (9) give a sharp finite functional
certificate/gap; they supply neither zero nor a proved nonzero scalar.

## 5. Independent algebra challenge and boundaries

The new checker passed 31 exact checks: actual T columns and last row,
transpose difference factorization, left-null weight identity, genuine
lambda increment/first/last values, the zero-seed first update, generic
all-endpoint coefficient summation, Heun cokernel/source decompositions,
whole-functional certificate, independent K equality, Q terminal response,
candidate signs, and exact residual/source-gap equivalence. The generic
arrays do not instantiate a finite field or p=6m+1. No old checker is used.

The separate directed Root top-cutoff challenge subsequently adds 18 new
independent checks, documented in `ROOT_DIRECTED_TOP_CUTOFF_CHALLENGE.md`.
They verify the literal 16^m coefficient, independently fixed old triangle
T_m, retained top defect and its justified cancellation. Combined
independent verification is therefore 31+18=49 checks. This resolves the
cutoff bookkeeping challenge and does not prove the terminal identity.

All original m,N endpoints, g, fixed C/OLD-R/tau and all prior cubic,
odd-flux and finite-log corrections remain in their existing constructors.
No Source or native state is changed. The terminal identity (13), original
scalar comparison, LIFT, weighted p^3, period normalization and full
native X6 propagation remain OPEN.
