# D25 — exact Legendre CM moment lift and nonzero second p-adic defect

Date: 2026-10-28, Asia/Hong_Kong. Research logical lane: chatgpt-research-onhour-enterprise-math-20260923 (not the maintenance conversation). Classification: **AUTHOR-SIDE / TWO EXACT RATIONAL IDENTITIES PROVED / EXPLICIT P373 OBSTRUCTION / EXECUTED EXACT MODULAR AND RATIONAL CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_EXECUTED**. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3**, unchanged.

Consumes existing author-side finite Legendre-moment bridge and CM0 Gauss two-node proof at commit 619e4d0040f1c90b87eaa1469870248aea5c70c8. Does not reuse or reopen accepted D24/UR or claim the original LIFT.

## Theorem A: exact even-Legendre CM divisor moment (over Q)

For all integers m>=1, n=2m, let P(x)=P_n(x) be the standard Legendre polynomial, s^2=1/2, D(x)=2x^2-1, a=P(s), c=P(0)=(-1)^m binom(2m,m)/4^m!=0, and d=P'(s)/(2s). Since P is even, a,d are rational. Set R(x)=(P(x)-a)/D(x), an even polynomial deg<=n-2, and

    K_m = integral_0^1 (1-x^2) R(x) P'(x)/x dx.

Then **K_m=1-a/c exactly in Q**.

Proof: R(x)=R(0)+x^2 S(x), deg S<=n-4, S=0 at n=2. The difference between K and R(0)J_n, with J_n=integral_0^1(1-x²)P'_n/x, is integral_0^1 x(1-x²) S P'_n = -integral_0^1 [x(1-x²)S]' P_n. Its boundary term vanishes and its derivative polynomial is even, degree<=n-2, so Legendre orthogonality on [-1,1], hence [0,1], gives zero. By (1-x²)P'_n=n(P_{n-1}-xP_n) and integral_0^1 P_{even}=0, J_{2m}=2m*integral_0^1 P_{2m-1}(x)/x dx. The standard three-term Legendre recurrence and the same orthogonality give I_{2m+1}=-(2m)/(2m+1) I_{2m-1}, I_1=1. Consequently J_{2m}=(-1)^{m-1}(2m)!!/(2m-1)!! = -1/P_{2m}(0)=-1/c. Since D(0)=-1, R(0)=c-a. Thus K_m=(c-a)(-1/c)=1-a/c. QED.

## Theorem B: exact factorization of the finite Legendre observer

Keep the previously source-typed finite Legendre construction A_m(z)=P_{2m}(sqrt(1-z/2)), F_m(z)=(1+6z d/dz)A_m(z)^2, Y=P²,

    Q_m(x)=[F_m(1)-Y(x)+3(1-x²)Y'(x)/x]/D(x).

We have F_m(1)=a²-6ad; at x²=1/2 the numerator is exactly zero. So Q_m is an even polynomial over Q, not an undefined rational function. Likewise the even polynomial

    C_m(x)=-R(x)+6*[(1-x²)P'(x)/x-d]/D(x)

exists because its numerator also vanishes at x²=1/2. Exact algebra (no reduction mod p) gives

    Q_m(x)=-P(x)R(x)+6(1-x²)R(x)P'(x)/x+a C_m(x).       (B1)

By deg R<n, integral_0^1 PR=0 exactly. Combining (B1) and Theorem A gives the second all-m identity

    I_m := integral_0^1 Q_m(x) dx = 6 + a*Lambda_m,
    Lambda_m := integral_0^1 C_m(x) dx - 6/c.            (B2)

These are rational-number identities; they neither rely on CM0 nor imply the original LIFT.

## Exact p² obstruction and Hensel port

For target p=6m+1 with p≡13 or 19 modulo24, the accepted CM0 states a=P_{2m}(sqrt(1/2)) ≡0 modp. All relevant denominators 2j+1 <=4m-1<p are p-units; c is a unit. Therefore a=p q_p modulo p², and

    K_m=1-p*q_p/c (mod p²),
    I_m=6+p*q_p*Lambda_m (mod p²).                    (B3)

The earlier mod-p identities K=1 and I=6 are valid, but deleting (B3)'s correction at mod-p² is invalid. Additionally the CM root in u=x² is simple: at u=1/2, if P and P' vanished modulo p, the Legendre differential equation (1-x²)P''-2xP'+n(n+1)P=0 and its differentiated equations force all derivatives zero. Since deg P=n<p and its leading coefficient is a p-unit, impossible. Hence d=G'_m(1/2) !=0 modp and the unique lifted root satisfies

    u_star = 1/2 - p*q_p/d (mod p²).                  (B4)

In 29 actually executed modular polynomial checks, the exact fixed p=373 result (p²=139129, m=62) was:

    a=17158=46*373, c modp=38, d modp=158,
    K=94743=1+254*373 mod139129,
    Lambda modp=72,
    I=122350=6+328*373 mod139129,
    u_star=1/2+283*373 mod139129.

Already at p19, I=348=6+18*19 modulo 361. Thus there are explicit exact counterexamples to a naive *one-more-digit lift of the auxiliary Legendre moment*, not to the actual original-216 LIFT.

A fully independent original weighted216 full sum at p373 (all n=0..372, weights 6n+1) gives W_373=373 mod373³. However I/6 = 66768=1+179*373 mod373². So the tempting undocumented scalar bridge W_373/373 = I_m/6 mod p² is **false**: the missing correction belongs to the actual original finite cutoff and weighted p-adic observer.

## Executed reproducible evidence, boundaries, next exact action

Companion standard-library script: research_notes/portable_direct/d25_cm_moment_lift_guard_20261028.py. It was actually executed on 29 primality-checked p≡1mod6 values up to373: polynomial divisibilities, (A), (B1), (B2), CM0 and simple-root p-adic assertions were exact modular operations; a separate Fraction-based evaluation checked all rational identities for m=1..10. Independent original216 full sum p373 gave W373=373 mod p³. Actual console marker: PASS_D25_CM_EXACT_MOMENT_LIFT_29_PRIMES. The all-m theorem strength is from the proof, not finite checks.

BRC retained carrier: original (p,n,6n+1,w_n), frozen Delta/R source-port identity, finite Cauchy/Legendre polynomial coefficients, CM root value a, c,d, quotient R, integral K/I and defect Lambda. Equality of the mod-p observer does **not** authorize erasure of the p² branch. This is typed external scalar arithmetic; P000 Heartbeat native six-dimensional Cell space, separately typed time and no native plane remain unchanged; no native X6 propagation or Frobenius claim follows.

Research continuation: original D25 target W_p≡p mod p³ uniformly for p≡13,19 mod24 and frozen Delta_p-R_p≡0 modp remains OPEN. Native issue #1559 is OPEN/PENDING_OWNER/NOT_EXECUTED: p373 original H0/B0 divided-power [X]U mod139129, actual module rank, semilinear Frobenius and eta, signed odd Green/Hesse, kappa and Delta-R must be produced by an authorized native executor. Site status research_authority_granted=false, code review upstream required, native new-job quota 5/5. No CLAIM/open/publish Source Result, independent review or native benchmark performed. Historical bridge #6575 pointer/#6576 failed request not replayed; old staging retained separate provenance.

**Next exact mathematical unit:** find a certified original p² finite-cutoff identity linking original W_p/p to I_m/6, retaining signed original terms, p-adic valuation bands and Lambda_m. Any candidate MUST reproduce the nonzero p373 difference 179*p. The current result must not be renamed the original LIFT proof.
