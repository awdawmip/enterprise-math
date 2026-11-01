# D25/LIFT — signed Clausen R boundary: exact holonomic coefficient bridge

2026-10-31. AUTHOR-DERIVED / EXACT-RATIONAL-PROVED / FINITE-FIELD-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.
Research logical lane: chatgpt-research-hourly-enterprise-math-20260923 (separate from CONTROL_PLANE_MAINTENANCE).
Parent Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3, unchanged; P000 ACTIVE, no native X6 theorem transfer.

## Inherited exact source and unsolved objective

For p=6ell+1, p mod 24 in {13,19}, the original 216 sum is

    A_p = sum_{n=0}^{p-1} (6n+1) binom(2n,n)^2 binom(3n,n)/216^n.

The frozen mother target A_p = p (mod p^3) remains OPEN. The prior source-faithful first-jet finite Green reduction at commit 5c051e16f7e2154d2988a0d276b0aa76f14b50a2 gives the *unproved-to-vanish* scalar

    (A_p-p)/p^2 = (L0*N0-1)/p + L0*N1 -12*2^(-3ell)*E_p - R_p (mod p).

The ORIGINAL signed Clausen overdegree boundary R_p (identified by prior source jet proof at commit 3380c77a4d5c5556d7c63698c274e8a5f537aa55) is

    R_p = 2 sum_{i=1}^ell g_i sum_{a=1}^i (1+6(i-a))*c_a (mod p),
    g_i=binom(ell,i)*binom(2ell,i)/2^i,
    c_1=1/10, c_{a+1}/c_a=36*a^2/((6*a+5)*(3*a+2)) for a<ell.

Neither this note nor the prior Green note identifies E_p with R_p. At p=373, E_p=1 and R_p=196.

## Theorem 1 — exact rational signed coefficient bridge and discrete Green

For ANY positive integer ell, construct c_a by the displayed rational recurrence, and set
    C_ell(z)=sum_{a=1}^ell c_a*z^a,
    G_ell(z)=sum_{i=0}^ell binom(ell,i)*binom(2ell,i)*z^i,
    Ghat_ell(z)=z^ell*G_ell(1/(2z)),
    K(z)=(1+5z)/(1-z)^2.

The following are IDENTITIES OVER Q, not statistical patterns:

    Rcal_ell = 2*[z^ell] Ghat_ell(z)*C_ell(z)*K(z)
             = 2 sum_{i=1}^ell g_i sum_{a=1}^i (1+6(i-a))*c_a.        (A)

Set q_0=q_{-1}=c_0=0 and q_i=[z^i] C_ell(z)*K(z). Then

    q_i - 2q_{i-1} + q_{i-2} = c_i+5c_{i-1},   1 <= i <= ell.         (B)

Define running moments P_i=sum_{a<=i}c_a and Q_i=sum_{a<=i}a*c_a. Then

    q_i = (1+6i)*P_i - 6Q_i,
    Rcal_ell = 2 sum_{i=1}^ell g_i*q_i.                              (C)

Thus the original double-index signed R observer admits O(ell) arithmetic using TWO exact rational moments, retaining its original signs and W=1+6theta weight.

Proof: K(z)=1/(1-z)+6z/(1-z)^2=sum_{d>=0}(1+6d)z^d. Ghat_ell(z)=sum_i g_i*z^(ell-i). Extracting the z^ell coefficient forces i=a+d and gives (A), with weight 1+6(i-a). Multiplication of q(z)=C(z)K(z) by (1-z)^2 gives (B). Expanding the inner sum linearly into count and first index moment gives (C). No formal infinite series needs evaluation at an analytic singular point.

## Theorem 2 — one terminal source for a finite third-order holonomic input

With theta=z*d/dz, define F_ell(z)=10 C_ell(z)/z=sum_{n=0}^{ell-1}f_n*z^n and f_0=1. Its exact rational coefficients satisfy

    f_n/f_{n-1} = 2*n^2/((n+5/6)*(n+2/3)),   1<=n<ell.

It is the degree < ell truncation of the classical series 3F2(1,1,1;11/6,5/3;2z) and obeys the EXACT finite polynomial identity

    [theta*(theta+5/6)*(theta+2/3)-2z*(theta+1)^3] F_ell
       = -20*ell^3*c_ell*z^ell.                                     (D)

The companion g_ell(z)=G_ell(z/2)=sum_i g_i z^i obeys

    [theta^2-(z/2)*(theta-ell)*(theta-2ell)] g_ell = 0.             (E)

Proof: for 1<=n<ell the coefficient of z^n in the left side of (D) is n(n+5/6)(n+2/3)f_n-2n^3 f_(n-1)=0. The constant vanishes. The terminal coefficient, where f_ell=0, is -2ell^3 f_(ell-1)=-20ell^3 c_ell; no higher coefficients occur. For (E), use i^2g_i=((i-1-ell)(i-1-2ell)/2)*g_(i-1), with the terminating factor i-1-ell=0 when i=ell+1.

At p=6ell+1>=7, 10, 6a+5 and 3a+2 (1<=a<ell) are p-units; reducing these rational identities mod p recovers the PREVIOUSLY PROVED original overdegree R_p, with no new independent replacement definition. The exact finite terminal source is not assumed to vanish, and is not the E_p Green/Hesse source.

## Verification, scope, BRC

The included standalone Python verifier was ACTUALLY EXECUTED with exact integer/Fraction arithmetic and F_p reductions, checking all 94 p=1 (mod 6) primes 7<=p<=1200 (including 52 frozen-class primes). It separately derives the original t^2 Gauss parameter jet and sums W-weighted overdegree monomials with the original n=i+k BEFORE reduction, independently of the proposed moments. It checks original R double sum, O(ell) transfer, finite difference recurrence, forced ODE, Gauss companion, and exact rational coefficients for ell=1,...,8. All PASS.

Anchor (p,R_p mod p, -20ell^3 c_ell mod p):
(13,0,3), (19,12,11), (37,11,28), (67,21,48), (373,196,259).
Marker: PASS_D25_SIGNED_R_HOLONOMIC_PAIRING_AND_SOURCE_JET_EXACT.

BRC COMPOSE_APPLIED with typed carrier (original 216 denominator, prime p, overdegree k=p-a, Gauss i, signed W=1+6(i-a), p^2 valuation, c_a, g_i, finite truncation source). Two moments P_i and Q_i are sufficient ONLY for the declared signed-R observer; they cannot reconstruct the entire jet, E_p, native H0/B0 or future arbitrary operators. This is external finite p-adic algebra, NOT P000-native six-axis physical mathematics.

## Unfinished work / exact continuation

The original mother target is still OPEN. Next: seek a genuinely source-faithful finite WZ/adjoint identity combining the ORDER-THREE FORCED F_ell operator and ORDER-TWO GAUSS g_ell operator with rational signed kernel K(z), the DISTINCT finite first-jet Green E_p, and both integer-carry and first-jet ports. Check nonzero p=19,67,373 and retain source pins/signs; do not assume E_p=R_p, portwise zero or universal target congruence. Required scalar remains (L0*N0-1)/p + L0*N1 -12*2^(-3ell)*E_p - R_p = 0 mod p.

Native p=373 divided-power H0/B0, [X]U mod 139129, rank, semilinear Frobenius/eta, signed Green/Hesse and independent replay remain PENDING under enterprise-math#1559; no native experiment is claimed here. Gateway 0.6.11 source control at this read has research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5, CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED; old session and protected neutral staging are untouched, no new CLAIM/OPEN, Source checkpoint, Result or admission. Existing control support issue #1558 remains responsible; this is author-side source publication only.
