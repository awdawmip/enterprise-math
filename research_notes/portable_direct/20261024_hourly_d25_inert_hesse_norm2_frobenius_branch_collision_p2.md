# D25/LIFT — normalized inert Hesse parameter to every p-adic digit and the exceptional mod-p CM branch collision

2026-10-24. **Portable author research / UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT.**

Mother task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Logical Research lane: chatgpt-research-hourly-enterprise-math-20260923. **No present winning CLAIM/open/run or native D25 CM benchmark is asserted.**

## Scientific question and exact provenance

The [frozen accepted parent interface](https://github.com/awdawmip/enterprise-math/blob/c47e13e4aba0e006366f989d6334d443f6333ae3/research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md) uses t²=1/2, u=(1-t)/2 and the Hesse cubic E_lambda: X³+Y³+Z³−3 lambda XYZ=0, with lambda^(-3)=u, discriminant −24 and the two CM j-values 2417472 ± 1707264 sqrt(2). Its second-digit LIFT still requires a genuine same-prime divided-power representative, directed Frobenius/connection action, fixed H0/B0 and [X]U mod p². Existing WZ/HIGH/Cauchy jets are separate auxiliary observers, not this input.

The new work below settles a **strictly smaller, exact source-parameter subproblem**, without inferring the missing divided-power operator: construct a chosen Hesse lambda coherently mod p^N for every target p, resolve its coefficient Frobenius orientation, and classify precisely where the two CM j-branches merge under a mod-p observer yet separate at the next digit.

## Theorem 1 — uniform normalized Hesse parameter in the inert quadratic coefficient algebra

For any prime p ≡ 13 or 19 (mod 24) and N≥1 set

R_N=(Z/p^N Z)[T]/(T²−2),  sigma(a+bT)=a−bT,
u=(2−T)/4,  y=u^(-1)=4+2T.

Then R_1=F_(p²), sigma mod p is the ordinary p-power Frobenius and sigma is its unique Z/p^N-linear ring-automorphism lift on this unramified quadratic algebra. There exists **exactly one** lambda_N in R_N such that

(1) lambda_N³ = 4+2T,
(2) lambda_N sigma(lambda_N) = 2.

These normalized roots are compatible under R_(N+1) -> R_N. They therefore define an unambiguous p-adic element lambda in Z_p[T]/(T²−2) *after the sign of T has been declared*, with

lambda^(-3)=u, sigma(lambda)=2/lambda.

Proof. Both target classes have p≡1 mod3 and (2/p)=−1. Thus R_1 is the quadratic field, and sigma(T)=−T agrees with T^p, by Euler's criterion. Since y sigma(y)=(4+2T)(4−2T)=8,

y^((p²−1)/3)=(y^(p+1))^((p−1)/3)=8^((p−1)/3)=2^(p−1)=1.

The cyclic group F_(p²)^× therefore contains exactly three roots of lambda³=y. Their norms c in F_p satisfy c³=8, so c=2 zeta with zeta³=1; multiplying lambda by each cubic root of unity zeta' in F_p multiplies its norm by (zeta')². This permutes all three possible norms and proves existence and uniqueness of norm 2.

At a normalized root lambda_1, derivative 3 lambda_1² is a unit (p≥13). The ordinary simple-root Hensel argument in the complete unramified Z_p-algebra gives exactly one compatible lift for every N. Its norm cubed equals 8; its norm is congruent to 2 modulo p, and 2 is the unique lift of that root of X³−8 because 12 is a p-unit. Thus the norm is exactly 2 mod p^N at every N. Finally sigma(lambda)=2/lambda follows by dividing the norm identity. No analytic approximation, change of prime, extra cubic coefficient extension, or Frobenius on de Rham cohomology is assumed. QED.

## Theorem 2 — exact CM j-values, exceptional collisions, and a second-digit branch witness

Let E_lambda be the Hesse cubic over R_N using Theorem 1's lambda. It has smooth reduction for every target p: lambda³−1=3+2T and its norm is (3+2T)(3−2T)=1, hence the Hesse discriminant factor is a unit. The standard Hesse j-formula and an exact calculation in Z[T]/(T²−2) yield

j(E_lambda) = 27 y (y+8)³/(y−1)³
            = 2417472 − 1707264 T,

sigma(j)  = 2417472 + 1707264 T.

Their trace is 4834944, their product is 14670139392, so they satisfy **the same frozen discriminant −24 Hilbert class polynomial**

j² − 4834944 j + 14670139392 = 0.

The exact branch difference and polynomial discriminant factor as

j − sigma(j) = −3414528 T = −2^9·3^3·13·19 T,
Disc(H_−24)=2^19·3^6·13²·19².

Because T is a unit in R_N, these identities prove the following complete statement for the stated prime classes:

* p=13 and p=19: j and sigma(j) **coincide modulo p but are distinct modulo p²**, with exact p-adic valuation 1 of the difference.
* Every target p>19: the difference is already a p-adic unit and the two branches are separated modulo p.

At each exceptional prime, retaining the normalized second-digit difference gives the explicit nonzero source-labeled witness

(j−sigma(j))/p ≡ 9T (mod p),  for p∈{13,19}.

Thus a mod-p-only j observer is **not future-operation-sufficient** for selecting the conjugate CM deformation at these two original LIFT primes: it erases a provably nonzero second-digit branch residual. This does not claim that a j-value by itself fixes a Hesse differential, CM action, p-adic Frobenius on divided powers, or a unique original JT2 representative. QED.

## Exact author verification, including Hensel coefficients

Represent a+bT as the pair (a,b), multiply by (a,b)*(c,d)=(ac+2bd,ad+bc), reduce componentwise modulo M. For each p, first find the unique pair (a0,b0) mod p with a0²−2b0²=2 and (a0+b0T)³=4+2T. Put q=p², D=[(4+2T)−(a0+b0T)³]/p mod p and delta=D/(3(a0+b0T)²) mod p. Then lambda_2=(a0+b0T)+p delta. Recheck lambda_2³=y, N(lambda_2)=2, sigma(lambda_2)=2/lambda_2 and the rational Hesse j formula modulo q.

Exact integer/modular arithmetic was executed for p=13,19,37,43,61,67,211; all four equalities passed. Selected independently reconstructed pairs:

| p | lambda_1=(a0,b0) mod p | lambda_2=(a,b) mod p² | j=(a,b) mod p² | sigma(j)=(a,b) mod p² |
|---:|:---:|:---:|:---:|:---:|
| 13 | (7,11) | (111,128) | (96,143) | (96,26) |
| 19 | (4,8) | (61,312) | (216,266) | (216,95) |
| 211 | (43,94) | (8061,29001) | (13338,29055) | (13338,15466) |

At p=13, j−sigma(j)=117T mod169, so the quotient is 9T mod13. At p=19 the difference is 171T mod361, giving 9T mod19. These are author exact checks, *not* an independent review or a native CM/divided-power benchmark; the general theorem is the finite-field/Hensel/algebraic calculation above.

## BRC / Enterprise observer contract

BRC resolution: **COMPOSE_APPLIED** to the signed, branch-labeled p-local carrier (p, T-sign, R_N, lambda_N, sigma(lambda_N), j, sigma(j), v_p(j−sigma(j))). Allowed operations: reduction modulo p, coefficient conjugation, Hensel lift, j evaluation and comparison modulo p². The information-losing map (j,sigma j) -> (j mod p) fails to preserve the follow-on second-digit comparison at p=13,19; the witness 9T must be retained together with its source branch. This is algebraic scalar/CM input work inside Enterprise Math's fixed P000 X6 ontology; it does not purport to construct a native X6 dynamical process or to turn positive branch mass into signed cancellation.

## Remaining exact D25/LIFT input and next executable unit

**Newly settled:** the same-specialization Hesse lambda coefficient parameter exists without a cubic field extension, admits a compatible norm-2 normalization to precision p² (indeed all N), and has a precisely oriented coefficient Frobenius sigma(lambda)=2/lambda. The p=13/19 j collision shows concretely why a mod-p j-only interface can lose an essential second digit.

**Still open and not inferred:** choose the actual Source-bound CM/divided-power primitive class and H0/B0 de Rham basis on this explicit E_lambda (including twist and differential), construct its p-adic crystalline/Frobenius/connection matrix and [X]U modulo p², prove the chosen direction/semilinearity and leading normalization of the exact kappa or omega+6 nabla_lambda omega observer, then compare **that same typed source** with frozen Delta_p−R_p. The algebraic sigma on R_N is only the **coefficient** Frobenius lift; it is not that native operator. The next discriminating step is to express the already-frozen Hesse invariant and derivative in the normalized lambda coordinate, retain the T-orientation and (at p=13/19) 9T branch residual, and determine what additional H0/B0 data are needed for [X]U mod p². Avoid repeating WZ/HIGH third/fourth jets and old all-prime scans.

Scientific scope: exact algebraic theorem plus seven finite author spot checks. Independent review NOT_RUN; native CM benchmark NOT_RUN; no promotion or Source checkpoint. Parent D25/LIFT remains OPEN; immutable scientific Source pin is unchanged.
