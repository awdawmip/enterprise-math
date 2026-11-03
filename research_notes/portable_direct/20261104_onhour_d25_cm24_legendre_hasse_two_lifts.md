# D25 — CM −24 / Legendre–Hasse exact comparison port (2026-11-04 +08)

**TASK_RESEARCH portable author derivation:** `AUTHOR-DERIVED / ALGEBRAIC IDENTITIES PROVED / EXTERNAL CM FACT APPLIED / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, **frozen scientific source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged**. This is a precise *comparison model and new discriminating fixed-373 second-digit test*, **not** the frozen original-class native H0/B0 computation or a Source checkpoint.

## Motivation / source separation

Already published and reused: original 216 coefficient `b_k=(1/2)_k(1/3)_k(2/3)_k/(k!)^3 * (1/2)^k`, signed weight `6k+1`; frozen D25 plus-class `Delta_p-R_p=0 (mod p)` is equivalent to `sum_(k=0)^(p-1) (6k+1)b_k=p (mod p^3)`. Earlier F4-glued four-source criterion and its exact boundaries remain the highest open p³ mathematical objective. We do not repeat them.

The published Chisholm–Deines–Long–Nebe–Swisher (2013) elliptic model for `d=3` is
`E_3(t): y^2+xy+(t/27)y=x^3`, with `lambda=-4t(t-1)`. At `lambda=1/2`, take the two conjugate roots `t^2-t+1/8=0` (equivalently `t=(1±1/sqrt(2))/2`). The matching `d=3, lambda=1/2, a=6` hypergeometric coefficients equal the original 216 coefficients. The original *native* fixed-class H0/B0 operator, semilinear basis and Frobenius normalization remain an independent source-bound identification obligation.

## Theorem 1 — exact CM comparison-class certificate

For the above model,
`c4=(9-8t)/9`, `Delta_E=t^3(1-t)/27^3`, hence
`j(E_3(t))=27(9-8t)^3/[t^3(1-t)]`.
Eliminating `8t²-8t+1` gives the two **exact algebraic integer** values
`j=2417472±1707264 sqrt(2)`, satisfying
`j²-4834944j+14670139392=0`.
This is precisely the standard Hilbert class polynomial `H_{-24}`, the maximal-order discriminant of `Q(sqrt(-6))` (lookup independently: https://fungrim.org/entry/20b6d2/ ). Thus E_3(t) has CM by discriminant −24. Its `t` and `1-t` are units and it has good reduction for primes `p>3`.

For any prime `p=6r+1≥7`, the CM criterion says E_3(t) is supersingular precisely when `(-6/p)=-1`, namely `p=13,19 (mod24)`; it is ordinary for `p=1,7 (mod24)`. The comparison is over the appropriate residue field: `8t²-8t+1` is irreducible mod p in the target classes, so t lives in `F_(p²)`, NOT `F_p`. The 2013 paper's Theorem 1 proves the original signed sum `mod p²` with sign `sgn * ((1-lambda)/p)`. For these two target classes `sgn=-1`, `((1-lambda)/p)=(2/p)=-1`, hence the already-accepted first digit `W_(p-1)=+p (mod p²)` follows from that source as a source-independent check. **The 2013 paper states the p³ strengthening as Zudilin's conjecture, not its theorem.**

## Theorem 2 — explicit finite Hasse/Legendre congruence

Complete the square: `Y=2y+x+t/27` gives
`Y²=f_t(x)=4x³+(x+t/27)²`.
The Hasse invariant at good odd p is the coefficient
`A_p(t)=[x^(p-1)]f_t(x)^((p-1)/2)`.
For `p=6r+1` its **exact rational coefficient formula** is
`A_p(t)=sum_(m=0)^(2r) binom(3r,m)4^m binom(6r-2m,m)(t/27)^m`.
Modulo p the factorial cancellation for `m≤2r` gives
`A_p(t)=sum_(m=0)^(2r) ((1/3)_m(2/3)_m/(m!)²)t^m
      =sum_(m=0)^(2r) binom(2r,m)binom(4r,m)t^m
      =Legendre_(2r)(1-2t) (mod p)`.
The final equality follows from `Legendre_n(1-2t)=2F1(-n,n+1;1;t)` and `2r+1=-4r (mod p)`.

Because `(1-2t)²=1/2`, we obtain the **all-prime exact class detector**
`Legendre_((p-1)/3)(1/sqrt(2))=0 (mod p) <=> p=13,19 (mod24)`
for all primes `p=1 (mod6)`; for ordinary classes `p=1,7 (mod24)`, the value is nonzero. This is the CM splitting condition read through a finite, original-`d=3` Legendre polynomial. The Hasse criterion and CM theorem are the external inputs; the explicit finite polynomial identifications are algebraically proved above. In the two target classes, the irreducible polynomial `8t²-8t+1` therefore divides `sum_(m=0)^(2r)binom(2r,m)binom(4r,m)t^m` **over F_p[t]**.

## New fixed-373 precise second-digit **nonidentification** witness

In the declared ring `R=(Z/373²Z)[t]/(t²-t+1/8)`, evaluate the **two particular integral lifts** of the same mod-p Hasse readout:

1. Literal elliptic Hasse coefficient `A_373(t)=[x^372](4x³+(x+t/27)²)^186`:
   `A_373(t)=112273+35808t=373(301+96t) (mod 139129)`.
2. Literal classical Legendre value `L_124(1-2t)=L_124(1/sqrt(2))`:
   `L_124=17158=373*46 (mod 139129)`.

Both reduce to zero modulo 373, **but their divided first jets differ**:
`(A_373/373) mod373=301+96t`, `(L_124/373) mod373=46`.
The coefficient `96t` is nonzero in the quadratic residue field. Thus the mod-p identity `A_p=Legendre_(2r)(1-2t)` cannot be lifted termwise to a canonical p² operator or native divided-power `[X]U` without specifying the actual integral lift, basis and normalization. This is a concrete, coefficient-level **information-loss witness** for the fixed-373 benchmark, not a claim that the benchmark was executed.

The exact R2 p-adic reflected dual and F4-glued four-source cancellation remain distinct: neither Hasse lift is silently substituted for frozen Delta, R, H, actual CM rank or semilinear Frobenius.

## Reproducibility and continuation

Companion standard-library Python checker `d25_cm_hasse_legendre_20261104.py` (same commit) uses two independent algorithms for the p² Hasse coefficient (direct binomial sum and literal polynomial powering), and verifies the Legendre polynomial both by its recurrence and a binomial sum. It checked **all 148 primes 7≤p≤2000, p≡1 mod6**: 77/77 inert target classes vanished and 71/71 split classes were nonzero. At p=13,19,37,373 the independent p² lifts agree exactly between algorithms. Fixed 373 was checked as the literal 139129-valued ring above; no float approximations.

BRC `COMPOSE_APPLIED`: carrier `(p, t, Z/p²[t]/(8t²−8t+1), operator, basis)`, observer `[x^(p-1)]f^((p-1)/2)` or `Legendre_(2r)`, future operation division by p. The mod-p observer projection loses precisely the lift-coordinate discrepancy `(301+96t)-46=255+96t`. Retain those distinct origin/operator labels, p-valuation and signed arithmetic before any scalar identification.

**Highest mother frontier unchanged:** F4-glued first-block signed Green/WZ cancellation for all p≡13,19 mod24 is OPEN; accepted D24 and known 2304 high tail stay consumed. **Next precise mathematical action:** check whether the *original frozen* H0/B0 definition/source identifies a native comparison morphism to the d=3 CM curve, and specify actual module rank, semilinear direction, lift and eta before a numerical equality can be tested. If no such morphism, preserve this as a sourced comparison candidate and continue F4-glued signed certificate independently. **Native experiment issue #1559** requires the actual original-class p373 `[X]U mod139129`, authentic semilinear Frobenius, rank, signed odd Green/Hesse and independent replication; **NOT_EXECUTED/PENDING_OWNER**.

**Control:** no new registration, claim, open, run, native Source checkpoint, Result or review. Historic exact request `research-onhour-20261031-0205-dispatch-r15` (#6633) stays definitively FAILED, never replayed. Sites status at 2026-11-03 16:00 UTC: `research_authority_granted=false`, `write_relay_enabled=false`; v0.6.11 control remains `UPSTREAM_CODE_REVIEW_REQUIRED`. This GitHub file is author-only evidence, not role-bound persistence. Research logical ID `chatgpt-research-onhour-enterprise-math-20260923` is source metadata only, not service session identity; maintenance `chatgpt-hourly-enterprise-math-20260921` is never used.

Sources: Chisholm et al., *p-Adic Analogues of Ramanujan Type Formulas for 1/π*, Mathematics 2013, Theorems 1–2, https://www.math.rwth-aachen.de/~Gabriele.Nebe/papers/Ramanujan.pdf ; discriminant -24 Hilbert class polynomial https://fungrim.org/entry/20b6d2/ ; exact frozen project source pin as above; prior current F4 and R2 author notes (do not promote them here).

## Theorem 3 — **new first-jet bridge directly to the frozen Gauss low port**

The accepted frozen CM0 source already uses the original low Gauss polynomial
`G_r(lambda)=sum_(k=0)^r binom(r,k)binom(2r,k)lambda^k
           =2F1(-r,-2r;1;lambda)`.
Meanwhile, the exact classical quadratic Legendre transformation yields
`L_r(lambda)=Legendre_(2r)(sqrt(1-lambda))
             =2F1(-r,r+1/2;1;lambda)`;
since the degree is even, this is a polynomial in lambda. **The two finite polynomials are congruent mod p, but their p² difference is now explicit**, rather than assumed to be equal:

For **every prime p=6r+1≥7 and all lambda in Z_(p)**,
`L_r(lambda)-G_r(lambda)
 = (p/2) * sum_(k=1)^r binom(r,k)binom(2r,k)lambda^k
                     * sum_(i=0)^(k-1) 1/(i-2r)   (mod p²).`  (JET)

**Proof.** The exact identity `r+1/2=-2r+p/2` gives, coefficientwise for each `k≤r`, `(-2r+p/2)_k=(-2r)_k prod_(i=0)^(k-1)(1+p/[2(i-2r)])`. All factors `i-2r` are p-units. Expanding that finite product to first order gives (JET), with no analytic limits, guess, numerical sign choice, CM assumption or new axiom. QED.

For lambda=1/2 at **p=373, r=62**, the two fully integral representatives are:
`G_62(1/2)=126820=373*340 (mod 139129)`;
`L_62(1/2)=17158=373*46 (mod 139129)`;
therefore `(L_62-G_62)/373 =79 (mod373)`, and the independent harmonic right-hand side of JET gives exactly **79**. At p=13,19,37 the corresponding harmonic jets are **8,17,25**. The new jet is a *specific original-Gauss ↔ Legendre repair coordinate*; it can enter subsequent second-digit source-mapping checks in the frozen F4 calculation without inventing a native Frobenius coefficient.

This supplies a **three-lift, source-labeled fixed-373 witness**:
`(A_373/373, L_124/373, G_62/373)=(301+96t, 46, 340)`
in `F_373[t]/(t²-t+1/8)`. All three reduce to the same zero **before division by 373**. A mod-p scalar match is insufficient for a p² Source or H0/B0 identification. The correction `79` is explicitly derived rather than fitted; at other primes the correction may vanish accidentally (e.g. p=193), without changing its scope.

**Executed check:** in addition to the Theorem 2 148-prime class regression, the companion program separately verifies (JET) on **all 148 primes p=6r+1≤2000** by computing the original finite-binomial `G_r`, the Legendre recurrence `L_r` and the harmonic-sum right side, modulo p². This is local exact arithmetic; native H0/B0 remains NOT_EXECUTED. Subsequent proof work should use this new exact repair coordinate where the original low port is compared to an elliptic CM/Legendre model, while retaining distinct F4-Green and signed-tail observers.
