# CM24 enlarged carrier: generic zero seed and complete endpoint ledger

Status: ONE PURE-PAPER UNIT. Generic seed, complete finite terminal forcing,
and the normalized endpoint vector are determined. The seed scalar is fixed
by the strict source, not freely adjustable. A separate outside-block scalar
is necessary for the carrier endpoint B(1). The fixed C/tau/F_CM target and
all mathematical parents remain OPEN.

Reviewer provenance: UNKNOWN local nonauthor helper
/root/cm24_extension_paper_check; same Root-delegated directed NONBLIND
continuation. Root retains direction and all original owners are preserved.
No Task, Claim, Run, branch, Native acceptance, Source write, mathematical
script, prime check, sample, old checker or Green execution was made.
The three earlier review originals are unchanged. This unit reads the
complete 12020-byte frozen specification locally, verifies its given hash,
and uses the already proved review chain as exact dependencies.

## 1. Actual enlarged objects and the full gauge equation

Work over the declared F_p, p=6m+1 prime in classes13/19mod24, m>=2,
N=3m=(p-1)/2. Keep original rho leading16, C, tau, F_CM, all beta
components and the complete original half-prefix tail unchanged. Here

    q=x(x-3)^2/4,
    D*=z(1-z)d^2+(3/2-5z/2)d-5/9,
    degree B<=p-2, B_N=0, F'=D*B,
    W_B=x^(-N)(x-3)B(q)/24, P_B=Pi_(0..N) W_B.

This is an enlarged formal carrier, not the original degree<N carrier.
Its coefficients above N are retained, even though its coefficient at N
is zero. The finite Laurent projection is the same actual central cut.

For completeness the full gauge equation does extend to every finite B.
Let a=2x(x-1)(x-4), b=5x^2-15x+4, w=x^(-N)(x-3)/24. Since -N=1/2
as a field scalar, formal differentiation at the actual Laurent exponents
gives

    w'=x^(-N)(x-1)/(16x),
    w''=x^(-N)(x+1)/(32x^2),
    q'=3(x-3)(x-1)/4, q''=3(x-2)/2,
    q(1-q)=-x(x-3)^2(x-1)^2(x-4)/16.

The three chain-rule coefficients, by finite polynomial expansion, are

    a w(q')^2 = -x^(-N)q' q(1-q),
    a(2w'q'+wq'')+b wq' = -x^(-N)q'(3/2-5q/2),
    a w''+b w'+(x-1)w = (5/9)x^(-N)q'.

Thus J W_B=-x^(-N)q'F'(q) for arbitrary finite B. No formal exponent is
reduced or identified with another exponent. The already reviewed universal
projection identity Pi J=J Pi therefore gives the actual central equation

    J P_B=S,
    S_n=-[x^(N+n)]q'F'(q), 0<=n<=N.                      (1)

Because degree F'<=p-2, the already reviewed legal primitive argument gives
S_N=0. This is raw forcing before zero-seed normalization, not deletion of
a normalized class-dependent terminal term.

## 2. Generic seed and every finite forcing row

Consume the frozen fundamentals

    phi_n=4^(-n)h_n/g, h_0=h_N=g (unit), J phi=0,
    psi_0=0, psi_1=1, J psi=4 epsilon_0-4 epsilon_N.

The origin row of J phi gives phi_0=1 and phi_1=1/4. Preserve the actual
new carrier's P_0 and P_1 and define

    A=P_0,
    c=4P_1-P_0=S_0,
    gamma=P_1-P_0/4=c/4.

The generic normalized response is precisely

    Z=P_B-A phi-(c/4)psi.                                  (2)

It has Z_0=Z_1=0. Its complete finite forcing, with y_n=S_n for 1<=n<N,
is

    J Z=S-c epsilon_0+c epsilon_N
       =(0,y_1,...,y_(N-1),c).                            (3)

No old t_0/4 coefficient is assigned to the new B. That special coefficient
is recovered only if this carrier's actual c is separately proved to equal
t_0. Neither B_N=0 nor raw S_N=0 proves such equality.

## 3. The scalar c is uniquely fixed by the complete strict source

Let a_k=(2k+1)(k+1), b_k=-(10k^2+5k+1), and d_k=4k(2k-1) be the
monomial coefficients of J. Its finite row n is

    (J P)_n=a_(n-1)P_(n-1)+b_n P_n+d_(n+1)P_(n+1).

The fixed submatrix with rows0,...,N-1 and columns1,...,N is lower
triangular with diagonal d_(n+1)=4(n+1)(2n+1), all units. Consequently
rank J>=N. Its nonzero phi kernel gives rank J<=N, so rank J=N.

The vector h_n=4^n g phi_n is a left kernel. Indeed, for each column k,
the left-kernel expression, divided only by the unit 4^k g, is

    4a_k phi_(k+1)+b_k phi_k+(d_k/4)phi_(k-1)
      =d_(k+1)phi_(k+1)+b_k phi_k+a_(k-1)phi_(k-1)=0.

The boundary columns use a_N=d_0=0. This does not divide any internal
h coefficient. The left kernel is one-dimensional and h_0=g is nonzero.
Apply it to the complete raw source (c,y,0) in (1):

    g c+sum_(n=1)^(N-1) h_n y_n=0,
    c=-sum_(n=1)^(N-1) h_n y_n/g.                         (4)

Thus c must be retained or reconstructed for the complete boundary ledger,
but it is not an extra independent source coordinate once all y is kept.
No source-preserving adjustment of F' or B can freely change c. A compressed
source observer may discard it only if its declared future language and
paid reconstruction still preserve this signed weighted sum.

## 4. Exact normalized endpoint vector

Because 4^N=1 and h_N=g, phi_N=1. Its homogeneous top row gives
phi_(N-1)=1. Let eta denote the actual canonical value psi_N; eta is a
fixed basis value, not a selectable parameter. The top row of J psi gives
psi_(N-1)=eta-4. The top row of J P_B equals S_N=0, hence

    E=P_N=P_(N-1).

Equation (2) therefore gives the complete adjacent endpoint vector

    Z_N     =E-A-c eta/4,
    Z_(N-1)=E-A-c eta/4+c.                               (5)

Its signed terminal difference is Z_(N-1)-Z_N=c, exactly (3).
No assertion of a free E or A is needed for this result.

The already frozen Green formula supplies a useful equivalent ledger,
without any new solve or execution. Define

    Q_psi(y)=sum_(j=1)^(N-1) 4^(j-1)psi_j y_j.

Using G(N,j)=4^(j-1)(phi_j eta-psi_j) and (4), the unique zero-seed
response has

    Z_N=-c eta/4-Q_psi(y),
    E-A=-Q_psi(y).                                      (6)

Thus normalized endpoints are fixed weighted functionals of the complete
strict source and the retained canonical basis, not additional freely
chosen boundary data. Computing these sums and the basis has paid costs.

## 5. Actual half-source and class-19 bookkeeping

Keep the frozen old half-prefix source t with t_N=0 and
t_0=(chi_3-1)/6. Its own normalization has terminal t_0, including the
actual class-19 value -1/3. For the actual missing strict source

    v_n=-beta^h_n-t_n,
    c_h=sum_(n=1)^(N-1) h_n beta^h_n/g,

equation (4) yields

    c_v=c_h-t_0.                                       (7)

The terminal of the old normalized response plus the new correction is
t_0+c_v=c_h, which is precisely the canonical terminal of the actual
zero-seed half response. This is linear source-response bookkeeping; it
does not provide the independent fixed-target endpoint mechanism.

If an additional proposed mechanism requires correction terminal zero,
the exact remaining weighted-compatibility obligation is

    sum h_n v_n=0, equivalently c_h=t_0.                 (8)

More generally a prescribed correction terminal b requires
sum h_n v_n=-g b. Such equalities cannot be achieved by changing a
source-preserving carrier. Neither (8) nor an identification of c_h with
an old class-dependent terminal is proved here. The original class-19
term is explicitly present rather than silently copied or canceled.

## 6. The full carrier endpoint needs a different scalar observer

The normalized central endpoint in (5) is different from B(1), the carrier
endpoint appearing in the original constructor comparison. Central data
alone cannot recover B(1), even with degree<=p-2 and B_N=0. The exact
countervariation delta B=1 satisfies all these carrier constraints and

    delta W=x^(-N)(x-3)/24,
    Pi delta W=0,

since its only exponents are -N and1-N, both negative. It changes B(1)
by1 while preserving every P_n, raw/normalized source, seed and central
endpoint. Its forcing changes by the legitimate constant -5/9; it is
not a countervariation of the original singleton frozen forcing.

For a precise endpoint-only observer retain the full finite outer blocks

    W_-=sum_(k<0)[x^k]W_B x^k,
    W_+=sum_(k>N)[x^k]W_B x^k,
    Omega_B=W_-(1)+W_+(1).

Because q(1)=1 and W_B(1)=-B(1)/12, the complete endpoint identity is

    B(1)=-12(P_B(1)+Omega_B).                            (9)

Thus one extra scalar Omega_B is sufficient for the future language
consisting only of B(1) and its fixed scalar multiples, given the complete
central P_B. The countervariation proves that an observer distinguishing
this outside endpoint contribution is necessary on the enlarged ambient
family. Omega is not freely assigned from a desired target; it is the
actual evaluation of retained outer blocks. Different endpoints, jets or
coefficient recovery need their own full observers. The old lower-block
observer alone is not asserted complete for the enlarged family.

The actual raw seed A is still retained: normalization alone does not
authorize deleting it for future recovery of P_B(1) or B(1).
Both outer blocks are kept in (9); original half-prefix terms 2m<r<=N
and the enlarged coefficients above N are not declared zero. Equation (9)
is an exact ledger, not a new independently forced transport for Omega_B,
nor a proof connecting it to fixed C/tau/F_CM. That connection, together
with any additionally required weighted terminal compatibility, is the
precise remaining mathematical interface.

## 7. Custody and scope

The full original specification is Source1b5ba622d8cef73128d86ae61414f95924c4fe20,
research_notes/CM24_HALF_SOURCE_CUSTODY_20261013_FBF223/HALF_PREFIX_ADJOINT_AND_BRANCH_CORRECT_GREEN_SOURCE.md,
12020B SHA256929d1800105eae1419046ca41c1f54746633c1909cd87346b020057591736659.
Its matching complete local cold file was read in this unit. Root's latest
review-chain Source reference is6152f02ed6420b243e812f39b55f013ffc502ce4;
this helper uses the unchanged local exact originals and performs no new
remote write or claim of independent Source custody.

These are classical finite-field auxiliary readout identities with signed
joint source, central/outer blocks, tails and boundaries retained. No
native dimension, physical propagation, Working Truth/Foundation, measured
performance or free arithmetic claim follows. Metadata times are separate
from mathematical objects. Fixed C/tau/F_CM and every parent remain OPEN.
