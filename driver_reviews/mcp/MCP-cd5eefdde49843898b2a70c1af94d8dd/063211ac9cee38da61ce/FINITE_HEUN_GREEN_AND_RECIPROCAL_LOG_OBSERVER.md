# Finite Heun Green identity, exact cokernel, and reciprocal log observer

Status: ROOT-DIRECTED LOCAL PAPER AUXILIARY / FINITE LEMMAS PROVED / FINAL
OLD-R COMPARISON OPEN. Prepared 2026-10-12. Native Researcher identity,
claim, Run, Source publication and operational Result are UNKNOWN: this
paper asserts none. No prime is instantiated, no prior prime campaign is
repeated, and no checker from the frozen author unit is executed.

The input is the already frozen finite Heun coefficient recurrence and the
already frozen, fully normalized CM observer. This paper does not rederive
the original two-index Heun certificate or the OLD-R constructor.

## 1. Frozen inputs and notation

Let p=6m+1>3 be prime and N=3m=(p-1)/2. Work in F_p, or its quadratic
extension where needed. All equations with N=-1/2 mean reduction modulo
p, not a characteristic-zero substitution into a finite sum. Write

    A_n=(n+1)(2n+1), B_n=10n^2+5n+1, C_n=4n(2n-1),
    (Lh)_n=A_n h_(n+1)-B_n h_n+C_n h_(n-1).

The frozen input is a nonzero sequence h_0,...,h_N with Lh=0 on 0,...,N,
h_(-1)=h_(N+1)=0, and

    h_0=g=binom(3m,m) != 0,
    y(u)=sum_(n=0)^N h_n u^n,
    Y(t)=y(t^2),  y(1)=y(1/4)=1.

The endpoint evaluations are the existing finite pullback evaluations:
w(1)=w(1/4)=0 and V(0)=1. They are not fitted normalizations.

The frozen target remains exactly

    Gamma(a)+sum h_n K_n(a)+OLD-R+6tau=0,

where a^2=1/2, a^p=-a, K and Gamma are the original fixed quantities in
sections 7 and 9 of the input paper. OLD-R and tau remain independent
constructors. This paper never assigns either from the target difference.

## 2. General finite Green identity, including all four end coefficients

For arbitrary coefficients, sequences h,f, and any integer interval
0,...,N, define the formal adjoint

    (L* f)_n=A_(n-1) f_(n-1)-B_n f_n+C_(n+1) f_(n+1),

and the flux

    J_n=A_n f_n h_(n+1)-C_(n+1) f_(n+1) h_n.

Direct expansion gives the exact row identity

    f_n(Lh)_n-h_n(L* f)_n=J_n-J_(n-1).

Consequently

    sum_(n=0)^N [f_n(Lh)_n-h_n(L* f)_n]=J_N-J_(-1).       (G)

No inverse coefficient or assumption about an extended solution is used.
In the present finite modular problem the four end coefficients are

    A_(-1)=0, C_0=0, A_N=0, C_(N+1)=0.

Indeed 2N+1=p and C_(N+1)=4(N+1)(2N+1). Hence both boundary fluxes
vanish, for arbitrary values of any formally extended sequence. There is
no hidden contribution from f_(N+1), h_(N+1), f_(-1), or h_(-1):

    sum f_n(Lh)_n = sum h_n(L* f)_n.                       (G0)

In particular, for the frozen homogeneous sequence h,

    sum_(n=0)^N h_n(L* f)_n=0                             (G1)

for every finite vector f. A claimed inhomogeneous adjoint certificate
must respect this cokernel obstruction. The vanishing of an endpoint
flux is not the value of an independently defined observable.

## 3. Forward and reverse units, terminal equations, and exact rank

For 0<=n<N, both n+1 and 2n+1 are nonzero modulo p. Thus A_n is a
unit and the first N equations determine h_1,...,h_N uniquely from h_0:

    h_(n+1)=[B_n h_n-C_n h_(n-1)]/A_n.

At n=N, the forward coefficient is zero and cannot be divided out. The
remaining coefficients reduce to B_N=1 and C_N=4, so the actual terminal
condition is

    h_N=4h_(N-1).                                        (H-end)

For 1<=n<=N, C_n is a unit: n is nonzero and 2n-1 lies between 1 and
p-2. Therefore reverse propagation from a specified h_N is legitimate,
using (H-end) first and then the rows n=N-1,...,1. The remaining n=0
condition is h_1=h_0. No reverse step divides by a terminal zero.

As a finite (N+1)x(N+1) matrix, L has kernel dimension at most one by
forward uniqueness. The frozen h is nonzero and satisfies all rows,
including the terminal row, so its kernel has dimension exactly one and
L has rank N. This assertion uses the supplied finite homogeneous
solution, rather than assuming that the terminal row is redundant for
an arbitrary recurrence.

The crucial exact identity is

    C_(n+1)=4 A_n.

Put rho_n=4^(-n). For any vector z one has, including both endpoints,

    L*(rho z)_n=rho_n (Lz)_n.                            (S)

This follows from A_(n-1)rho_(n-1)=rho_n C_n and
C_(n+1)rho_(n+1)=rho_n A_n. In matrix notation, with D=diag(rho_n),
L^T D = D L. In particular the adjoint null vector is exactly

    f_n=rho_n h_n.

There is no second independent finite adjoint mode. Its initial and
terminal equations are respectively f_1=f_0/4 and f_N=f_(N-1).
For n<N, its forward divisor C_(n+1)=4A_n is a unit.

## 4. Necessary and sufficient solvability, and the explicit residual

For any prescribed finite forcing kappa, the equation

    L* f=kappa on every row 0,...,N

is solvable if and only if

    sum_(n=0)^N h_n kappa_n=0.                          (C)

Necessity is (G1). Sufficiency follows because L* has rank N, so its
image is an N-dimensional subspace contained in the N-dimensional
annihilator of the nonzero vector h. This is the exact finite statement;
it does not assert that a solution is low order or has a useful closed
form.

One can also expose the obstruction without a dimension argument. Choose
f_0 arbitrarily and solve the first N adjoint rows forward:

    f_(n+1)=[kappa_n+B_n f_n-A_(n-1)f_(n-1)]/C_(n+1),
    0<=n<N.

At n=0 the coefficient of f_(-1) is zero. Define the unfulfilled terminal
residual by

    r=kappa_N-f_(N-1)+f_N.

Then the first N rows agree, while the last row differs by r. Applying
(G1) gives the exact identity

    sum h_n kappa_n=h_N r.                             (R)

The value h_N is a unit. For example the frozen leading coefficient is
(-16)^m binom(2m,m), whose factorial arguments are all below p. Thus the
terminal residual vanishes exactly when (C) holds. Changing f_0 adds a
homogeneous adjoint vector and does not change r.

This construction is an explicit evaluation algorithm for the same
obstruction. Constructing f from a forcing containing the desired target,
and then declaring its terminal residual zero, is not a proof. In
particular, L* f=K would require sum h_n K_n=0; the actual frozen target
instead includes the separately fixed Gamma, OLD-R, and 6tau. Dropping
those terms changes the question.

## 5. Reciprocal finite coefficients, derived without new prime data

Reduction at N=-1/2 gives three exact coefficient symmetries:

    A_(N-n)=C_n/4, B_(N-n)=B_n, C_(N-n)=4A_n.

It follows directly, row by row, that

    z_n=4^n h_(N-n)

also solves Lz=0. For example the transformed row is 4^n times the
original row at N-n, with the forward and reverse terms interchanged.
The vanishing end coefficients cover the two extreme rows. By the
one-dimensional kernel, z=c h for a scalar c. Its polynomial is

    z(u)=(4u)^N y(1/(4u)).

This is a polynomial identity after expansion; it does not evaluate at
a pole. Euler's identity gives 4^N=2^(p-1)=1. Evaluation at u=1 and
the frozen y(1)=y(1/4)=1 therefore gives c=1. Hence

    h_(N-n)=rho_n h_n, h_N=h_0,
    y(u)=(4u)^N y(1/(4u)).                            (P)

These are exact finite consequences of the supplied recurrence and its
fixed two endpoint values, not novelty claims or additional hypotheses.
As a consistency corollary, at u=1/2 equation (P) gives
y(1/2)=2^N y(1/2). For p=13 or 19 mod24, (2/p)=-1, so y(1/2)=0.
This recovers CM0 at the same finite scope; it establishes no p^2 or
p^3 comparison, period normalization, or LIFT statement.

## 6. Reciprocal finite logs and a one-function observer

For 0<=j<=p-1, let L_j(x)=sum_(r=1)^j x^r/r, and let L=L_(p-1).
For every nonzero x in the working field and 0<=n<=N, complementing
the last 2n indices in L gives

    L_(2(N-n))(x)=L(x)+x^p L_(2n)(1/x).                 (F0)

Proof: the omitted tail is indexed by r=p-s, 1<=s<=2n, and
x^(p-s)/(p-s)=-x^p x^(-s)/s. All denominators stay in 1,...,p-1.

Define independently, from the frozen h,

    F(x)=sum h_n L_(2n)(x),
    G(x)=sum rho_n h_n L_(2n)(x).

Use (P), reverse n to N-n, and apply (F0). Since sum h_n=y(1)=1,

    G(x)=L(x)+x^p F(1/x).                              (F1)

The function F is a polynomial with F(0)=0. Its degree is at most p-1,
and its derivative is exactly

    F'(t)=sum h_n [1-t^(2n)]/(1-t)
         =[Y(t)-1]/(t-1).                              (F2)

Thus F is the original normalized finite integral J_1. The quotient is
a polynomial because Y(1)=1, and its degree is at most p-2. The
primitive of degree <=p-1 with F(0)=0 is unique: no integration divides
by p, and a polynomial in that degree range with derivative zero is a
constant. No missing Frobenius constant is silently selected.

## 7. Exact reduction of the frozen CM observer

Substitution of (F1) into the existing K_n formula eliminates every
rho-weighted sum. The eight original terms give, before adding Gamma,

    sum h_n K_n(a)
      = F(1)-5F(-1)/3-2F(1/2)/3-4F(-1/2)
          +(4a+2)F(a)+(2-4a)F(-a)+C_R,

where the constant is independently evaluated from the finite logs as

    C_R=(16a+14)q_2/3-6q_3+(4a-2)L(-a).

Here use the frozen exact constants

    L(-1)=L(2)=-2q_2, L(-2)=2q_2-3q_3,
    L(-2a)=-2aL(-a), a^p=-a.

For clarity, the four weighted terms transform as

    G(-2)=L(-2)-2F(-1/2),
    G(2)=L(2)+2F(1/2),
    G(-2a)=L(-2a)+2aF(-a),
    G(-1)=L(-1)-F(-1).

Adding the fixed Gamma=-8(1+2a)q_2/3+3q_3-4aL(a)+2L(-a)
therefore yields the exact, simpler observer

    Omega := Gamma+sum h_n K_n(a)
      = 2q_2-3q_3-4a[L(a)-L(-a)]
          +F(1)-5F(-1)/3-2F(1/2)/3-4F(-1/2)
          +(4a+2)F(a)+(2-4a)F(-a).                    (O)

Omega is a name for the already fixed observer, not an assignment of
OLD-R or tau. In particular the final target remains

    Omega+OLD-R+6tau=0,                               (OPEN)

and is not proved by (O). Formula (O) retains every fixed constant and
endpoint. It replaces the eight weighted log interfaces by one canonically
normalized F at six points, making a subsequent Green comparison more
direct. Its conjugate is obtained with the same marked choice replaced
by a -> -a. No individual marked summand is declared base-field-valued.

## 8. Independent check of the parent scalar observer and its update

The parent next-unit author supplied a further scalar normal form for
independent checking. Define two different, explicit finite sums

    ell_n(u)=sum_(r=1)^n u^r/r,
    O_n(u)=sum_(r=1)^n u^r/(2r-1).

The exact even/odd identity is

    L_(2n)(t)=ell_n(t^2)/2+O_n(t^2)/t, t!=0.

All denominators are units for n<=N. Using this identity on every
term of (O), and a^2=1/2, gives the completely base-field formula

    Omega=C_fixed+sum h_n Bobs_n,
    C_fixed=2q_2-3q_3-8O_N(1/2),

    Bobs_n=2ell_n(1/2)+8O_n(1/2)
               -ell_n(1)/3+8O_n(1)/3
               -7ell_n(1/4)/3+20O_n(1/4)/3.             (O-scalar)

The notation Bobs distinguishes this kernel from the recurrence
coefficient B_n=10n^2+5n+1. Both names are fixed formulas, not values
obtained from the desired zero. In particular Bobs_0=0.

The coefficients are independently checked as follows. The pair of
arguments 1,-1 contributes -ell_n(1)/3+8O_n(1)/3. The pair 1/2,-1/2
contributes -7ell_n(1/4)/3+20O_n(1/4)/3. The marked pair a,-a
contributes 2ell_n(1/2)+8O_n(1/2). Finally,
L(a)-L(-a)=2O_N(1/2)/a, so its constant contribution is
-8O_N(1/2). This explicitly checks the disappearance of a without
declaring each marked term scalar separately.

For every 1<=n<=N, direct subtraction of the six defining finite sums
gives the exact rational update

    Bobs_n-Bobs_(n-1)
       =[(6n+1)+6(6n-1)2^(-n)+(6n+7)4^(-n)]
                                               /[3n(2n-1)]. (Delta)

The constant numerator arises from -(2n-1)+8n=6n+1; the 2^(-n)
numerator from 6(2n-1)+24n=6(6n-1); the 4^(-n) numerator from
-7(2n-1)+20n=6n+7. Every denominator in (Delta), including the
n=N denominator, is a unit. Continuing it to n=N+1 would divide
by 2n-1=p and is not licensed. The remaining target is exactly

    C_fixed+sum h_n Bobs_n+OLD-R+6tau=0,

still OPEN. This scalar normal form and its update are useful fixed
inputs for a later inhomogeneous adjoint or simultaneous finite flux;
the present cokernel criterion does not establish that comparison.

## 9. What an elementary log-adjoint prefactor actually produces

This optional identity records both exceptional endpoints; it is not a
certificate of (OPEN). Fix x!=0 and put f_n=rho_n L_(2n)(x). For
1<=n<N, exact shifted finite logs give

    (L* f)_n=rho_n[-6n L_(2n)(x)+E_n(x)],

    E_n=(n+1)x^(2n+1)+(2n+1)x^(2n+2)/2
                      -4n x^(2n-1)-2(2n-1)x^(2n).

The full endpoint-corrected formula on 0,...,N is

    (L* f)_n=rho_n[-6n L_(2n)(x)+E_n(x)
                      -2 delta_(n,0)-(N+1)x^p delta_(n,N)].  (E)

At n=0 the true value is x+x^2/2; the formal interior expression has
an additional 2, which is removed. At n=N the forward coefficient is
zero. The apparently cancelled forward log update would require the
undefined 1/p term; its spurious remainder (N+1)x^p must be removed.
The displayed formula is instead checked from the actual terminal row.
This shows concretely why continuing a log-shift formula past N is not
licensed even when multiplying coefficients appear to cancel p.

More generally, treating the log as a formal independent component,
the coefficient of L_(2n)(x) in L*(rho_n P(n)L_(2n)(x)) is
rho_n (LP)(n). For a nonzero characteristic-zero polynomial P of
degree d, LP has degree d+1 with leading coefficient -6(d+1) times
that of P. Therefore a single polynomial-prefactor symbolic ansatz
cannot produce a nonzero constant log coefficient. This restricted
observation does not exclude rational, multiple-log, finite-field
interpolation, or higher-order certificates, and is not a general
impossibility theorem for the actual kernel.

## 10. Validation and reusable output

The accompanying independent symbolic script checks only coefficient
identities, exact Green expansion, terminal reductions, reciprocal
coefficient identities, finite-log endpoint cancellations, and the
observer constant reduction. It instantiates no prime, imports no
frozen author checker, and provides no evidence for (OPEN).

Reusable finite tools proved here: the all-boundary Green identity,
the exact rank/cokernel criterion and residual, the adjoint null mode
rho h, the reciprocal coefficient identity, the reciprocal finite-log
transform, and the one-function fixed observer (O). The parent's
scalar normal form (O-scalar) and update (Delta) are independently
confirmed from (O).

Still open: comparison with the independently frozen OLD-R and tau;
LIFT and the weighted p^3 supercongruence; full native X6 propagation;
raw CM period normalization. The parent mathematical objective remains
open and no formal state-machine completion is claimed.
