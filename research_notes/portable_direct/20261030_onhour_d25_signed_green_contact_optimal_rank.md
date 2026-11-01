# D25 — Signed joint-strip Green kernel, exact diagonal contact, and optimal separation rank

Date: 2026-10-30 Asia/Hong_Kong. Status: AUTHOR-SIDE / PROVED EXACT FINITE KERNEL THEOREM / EXECUTED FINITE-FIELD CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7.
Research lane: chatgpt-research-onhour-enterprise-math-20260923, distinct from maintenance. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged.
This note is mathematical author evidence; it neither possesses a native CLAIM/run nor changes the Source task state.

## Original carrier consumed, without changing the observer

Let p=6m+1 be prime with p=13 or 19 (mod 24). Keep the original signed sources
beta_i = binom(m,i) binom(2m,i) / 2^i (1<=i<=m),
C_1=1/10, C_(a+1)/C_a=36 a^2/[(6a+5)(3a+2)] (1<=a<4m), computed in F_p.
The already proved two-strip joint signed observer is

  J_p = 2 sum_(i=1)^m beta_i sum_(a=1)^(4m) K(i,a) C_a,
  K(i,a) = (6a-1) if a<=i; 6i if a>i.

This is the original 20261030_onhour_d25_signed_joint_strip_four_port_obstruction.md, not a replacement definition of R_p. Its prior exact equality is J_p = 6 F_p W0 - R_p (mod p), with F_p=sum_(a=1)^(4m) C_a, W0=2 sum_(i=1)^m i beta_i and frozen original signed R_p.

## Theorem 1: canonical Green/contact factorization

For all positive integers i,a,

  K(i,a) = 6 min(i,a) - 1_{a<=i}
         = sum_(r=1)^m 1_{i>=r} [6 1_{a>=r} - 1_{a=r}]     (1)

whenever 1<=i<=m and 1<=a<=4m.

Define tail coordinates preserving their original indices:
  B_r = sum_(i=r)^m beta_i,
  D_r = sum_(a=r)^(4m) C_a   (1<=r<=m).
Then the complete signed joint observable admits an exact single-index coupled expression:

  J_p = 2 sum_(r=1)^m B_r (6 D_r - C_r) (mod p).         (2)

Proof. The identity min(i,a)=sum_(r>=1) 1_{r<=i}1_{r<=a} and
1_{a<=i}=sum_(r>=1)1_{a=r}1_{r<=i} gives (1). Reverse the *finite*
i,a,r sums, retaining beta_i and C_a, to obtain (2). No new modular
division occurs and no diagonal/source label is discarded.

For forward differences Delta_i f(i,a)=f(i+1,a)-f(i,a),
Delta_a f(i,a)=f(i,a+1)-f(i,a), the exact mixed source is

  Delta_a Delta_i K(i,a) = 5*1_{a=i} + 1_{a=i+1}.       (3)

Indeed Delta_i K=6*1_{a>=i+1}-1_{a=i+1}. Its forward a-difference
is precisely (3). Hence the nonseparable interaction has TWO
oriented diagonal contact positions (weights 5 and 1), not an
unrestricted bulk term. A separable sum F(i)+G(a) cannot reproduce
the kernel, because its mixed difference vanishes.

## Theorem 2: optimal separation rank of the original signed source matrix

Let K_m be the m by m leading block, K_m(i,a)=K(i,a) for 1<=i,a<=m.
Subtract row i-1 from row i for i=m,m-1,...,2; this determinant-one
operation yields upper triangular entries:
  0 for a<i, 5 for a=i, 6 for a>i.
Thus det(K_m)=5^m as an *integer identity*, and therefore K over F_p
has row rank exactly m for every target prime p (indeed every p!=5).

All beta_i and C_i (1<=i<=m) are p-units: i!, 2, 10 and all
displayed recurrence denominators are units in the target range.
Therefore the actual *weighted original signed source matrix*
  H(i,a) = 2 beta_i C_a K(i,a), 1<=i,a<=m,
has exact nonzero determinant
  det(H) = 2^m 5^m prod_(i=1)^m beta_i C_i  (mod p).    (4)

Consequently, any separable branchwise representation of the full
m by 4m weighted source matrix H(i,a) as
  sum_(j=1)^r u_j(i) v_j(a)
must have r>=m. Equation (1), with m terms, attains this lower bound.
In particular, a prime-uniform fixed-rank separable factorization
cannot preserve all of these original indexed source entries.

IMPORTANT SCOPE. This is a rank theorem for the complete indexed
matrix, not a lower bound for computing one contracted scalar J_p
when the specific beta and C recurrences are exploited. It does NOT
rule out a bivariate WZ, p-adic CM transform, recurrence-based
closed form, or an actual LIFT proof. The earlier rank-three
dynamic C/S/T recurrence is a different interface and is not
contradicted by this static two-source matrix rank.

## Exact executed finite-field witness

Ran the standalone Python standard-library checker
d25_signed_green_contact_kernel_guard_20261030.py for ALL 166 primes
13<=p<5000 with p=13 or 19 (mod 24). For every prime, separately
evaluated the original O(m^2) two-strip J, the Green-tail O(m)
expression, and 6F W0-R, checked nonzero weighted minor formula
and local mixed difference for m<=20. All passed.

  p   m   J   F   R   det(K_m)   det(H_m)  [mod p]
  13  2   9   8   0     12          7
  19  3  13  10  12     11          9
  67 11  30  29  21     66         47
 373 62   1 252 196    285         81

The general finite rank and contact identities follow from the
proof above, NOT from the finite checks. Numerical witnesses
apply only to their stated primes; ordinary finite arithmetic is
not native H0/B0 experimental execution.

## BRC / coordinate / continuation semantics

The carrier retains (original p,i,a,r, beta_i, C_a), the oriented
diagonal contact weights and the two tail coordinates. Allowed
observer is the original signed contraction J_p; equation (2)
is safe for this observer. For arbitrary future source-wise
operations, retain the full i,a labels or demonstrate an
appropriate factorization; a scalar sum is not lossless. These
arithmetic indices are NOT native six-dimensional coordinates,
and this theorem does not establish an H0/B0 transfer.

Mother goal: prove Delta_p-R_p=0 (mod p) on both frozen prime classes
via the original 216 weighted sum, not by changing R. Prior
three-valuation harmonic jet and five-port reduction remain intact.
Current smallest unresolved mathematical action: build a *joint*
finite-field/WZ/CM cancellation using the diagonal contacts (3) and
Green-tail formula (2) together with K0+6XW1+6(Y0+Y1)W0+X^2.
The original LIFT remains open; neither the diagonal rank proof nor
its numeric test is a surrogate completion.

Native distinct highest-priority benchmark #1559 remains original
fixed class p=373 H0/B0 divided-power [X]U mod 139129, module rank,
real semilinear Frobenius/eta, signed odd Green/Hesse, kappa,
Delta-R and independent reproduction. Its status at this read was
OPEN / PENDING_OWNER / NOT_EXECUTED; ordinary scalars above do not
satisfy this native requirement.

At 2026-10-30T15:59:13Z the Sites gateway returned
research_authority_granted=false, write_relay_enabled=false,
backend_connected=false; separate Site-bound client/credential
approval is required. Existing own Research-lane bridge issue #6581
and rejected #6582 are historical request records, not current
CLAIM/run authority. Do not replay their writes or adopt maintenance
or another conversation identity. No role-bound Source operation
is asserted by this author-side mathematical note.
