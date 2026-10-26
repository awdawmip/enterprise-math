# D25 — original E3 geometric q-Frobenius sign, uniformly fixed by CM and rational 3-torsion

**2026-10-26. TASK_RESEARCH portable author proof, UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0 / NOT_SOURCE_CHECKPOINT.** Mother Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin **`c47e13e4aba0e006366f989d6334d443f6333ae3`** unchanged. Research-onhour logical lane `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance). This is a new application of standard CM/torsion facts to the actual fixed E3 curve, not an originality claim for those classical facts.

## Uniform theorem (new scope versus the prior three-prime geometric certificate)

Put `K0=Q(sqrt(2))`, `t=(2-sqrt(2))/4`, and take the **original** curve of Chisholm–Deines–Long–Nebe–Swisher, `E3(t): y²+xy+(t/27)y=x³`. For every prime `p≡13,19 (mod 24)`, its good reduction at the unique place of K0 over p is `E_p/F_(p²)`. Let `pi_(p²)` be its **unmodified geometric q-Frobenius**, q=p², not an independently selected quartic-twisted, normalized or auxiliary lift.

**Theorem (every target prime):**
```
pi_(p²) = [+p] in End_(F_(p²))(E_p),
#E_p(F_(p²)) = (p−1)²,
a_(p²)(E_p) = +2p,
pi_(p²)/p = +1 in the rational endomorphism algebra.
```

The earlier author note `20261026_onhour_d25_original_E3_q_frobenius_trace.md` established these equalities **only** by exhaustive point counts at p=13,19,373. This proof covers **all** target primes and consumes rather than recredits those counts.

## Proof

**(1) Exact model, CM recognition, good reduction.** Write `c=t/27`. The Weierstrass invariants yield
```
disc(E3)=c³(1−27c)=(t/27)³(1−t),
j(E3)=27(9−8t)³/(t³(1−t))
     =2417472+1707264 sqrt(2).
```
These are exact identities in Q(sqrt2); `t(1−t)=1/8` and t is a p-unit, so the discriminant is nonzero modulo every target p>3. Direct exact substitution gives
`j²−4834944j+14670139392=0`, the standard Hilbert class polynomial `H_(−24)`. Therefore E3 has CM by the maximal order of `F=Q(sqrt(−6))`, whose fundamental discriminant is −24. The standard CM Galois-action theorem defines all geometric CM endomorphisms over `K0 F=Q(sqrt2,sqrt(−6))`; this is classical input, not a source-new axiom.

**(2) Field and descent of CM endomorphisms.** For p≡13,19 mod24, quadratic reciprocity yields
```
(2/p)=−1,    (−6/p)=−1,    p≡1 (mod 3).
```
Thus K0 has residue field `F_(p²)`, while adjoining sqrt(−6) *does not enlarge this residue field*: every nonzero Fp element is a square in F_(p²). All CM endomorphisms consequently reduce to endomorphisms **defined over F_(p²)**. Since p>3 is unramified and inert in F, Deuring CM reduction makes E_p supersingular. The geometric endomorphism algebra is the quaternion algebra `B_(p,∞)` containing F.

**(3) CM centralizer determines the sign pair.** The q-Frobenius commutes with all endomorphisms defined over `F_q`; in particular with the embedded F. The centralizer of a quadratic field inside a quaternion algebra is that field, hence `pi_q∈F`. Its endomorphism degree, i.e. field norm, equals `q=p²`. As p is inert in F, the only algebraic integers of F with norm p² are `u p` with u a unit; `O_F^×={±1}`. Thus `pi_q=[+p]` or `pi_q=[−p]`. No finite point count or ordinary Hesse candidate is used in this deduction.

**(4) The original torsion observer selects +.** The actual Weierstrass equation contains `P=(0,0)` rational over K0 and hence over F_q. Its tangent is y=0, with triple intersection x³=0 at P. Therefore P has *exact* order three because p≠3. Frobenius fixes this rational point, `pi_q(P)=P`. As `p≡1 mod3`, `[+p]P=P` while `[−p]P=−P≠P`. So the sign is uniformly positive. The characteristic polynomial is `(X−p)²`; the trace and count follow. □

This is a hand proof invoking classical CM recognition/reduction/centralizer theorems. It has not been independently reviewed or formally checked, and its precision scope is **geometric q-Frobenius alone**.

## Exact independent arithmetic checks and discriminating new evidence

The attached `research_notes/portable_direct/d25_E3_uniform_q_frobenius_torsion_check_20261026.py` uses stdlib integer/Fraction arithmetic, verifies the j identity and H_(−24) polynomial, and exhaustively counts `E3(F_(p²))` directly from the original equation, for every x in `F_p[T]/(T²−2)`. With `c=t/27`, completing the square gives `D(x)=(x+c)²+4x³`, and `chi_(p²)(D)=chi_p(N(D))`. Thus `#E(F_q)=q+1+Σ_x chi_(p²)(D(x))` is an exact finite identity. Actual local execution:

| p | q | signed character sum | #E(F_q) | trace |
|---:|---:|---:|---:|---:|
| 13 | 169 | −26 | 144 | 26 |
| 19 | 361 | −38 | 324 | 38 |
| 37 | 1369 | −74 | 1296 | 74 |
| 43 | 1849 | −86 | 1764 | 86 |
| 61 | 3721 | −122 | 3600 | 122 |
| 67 | 4489 | −134 | 4356 | 134 |
| 211 | 44521 | −422 | 44100 | 422 |
| 373 | 139129 | −746 | 138384 | 746 |

New finite comparison cases are p=37,43,61,67,211; previous p=13,19,373 are consumed and not re-counted as research novelty. The checker is **not** a formal validator of classical CM facts and **not** a native H0/B0 experiment.

## Native benchmark consequence and exact non-completion

The uniform geometric sign is an input/normalization discriminator: a faithful Source identification of **unmodified** geometric q-Frobenius must produce `pi_q/p=+1` for all target p. At p=373, if (conditional ONLY) native H0/B0 is free rank one σ-semilinear with coefficient `beta=eta*alpha`, `alpha=92060+21788T`, `N(alpha)=122102 (mod139129)`, **and** native normalized square is certified identical to the unmodified geometric `pi_q/p`, then necessarily
```
N(eta)*122102 ≡ 1 (mod139129),
N(eta) ≡ 18818 (mod139129).
```
This p=373 conditional two-digit calibration was **already documented** in the earlier finite geometric note; its scalar digits are consumed, not claimed new. What is new is the uniform positive sign of the *geometric input*. The 2013 paper explicitly uses an auxiliary multiplication by `−p` after a quartic twist in the supersingular comparison. This does **not** contradict the theorem for the **unmodified** original curve and may not be equated to it without a verified twist/coordinate/source map. The scalar norm does not retain the odd signed observer or kappa.

**BRC: COMPOSE_APPLIED.** Typed carrier is (original E equation, labelled K0 place, CM endomorphism algebra, q-Frobenius, rational point P of order 3). CM norm/valuation alone merges two sign branches ±p; retaining original P supplies a minimal observer separating them for p≡1 mod3. This reduction preserves the geometric Frobenius sign and exact integer trace, but does **not** preserve the later `[X]U`, signed odd Green/Hesse, eta second digit or kappa ports; no P000 X6/3D native transfer is claimed.

**D25/LIFT/JT2 remains OPEN.** Required actual original fixed-class native H0/B0 divided-power `[X]U mod373²`, rank, Frobenius normalization/twist/direction, signed odd Green/Hesse, exact kappa and `Delta−R`, and independent review are still **NOT_EXECUTED / PENDING_OWNER** via existing issue #1559. The highest Source-native checkpoint belongs to a different lawful Research owner and is not replaced by this file. A current read-only Site exact continuation request returned `CONTROL_QUOTA`; own older Research-onhour recovery #6528 has `source_authority_verified=false`, no claim/run; original dispatch #6529 is terminal FAILED/TimeoutExpired, not NO_DISPATCH. No claim, Source Research activity, run, checkpoint, Result, freeze, Driver review or old staging promotion is asserted. Classification `REGISTER_PENDING / SYNC_DEBT / UNREVIEWED / NOT_ADMITTED`; no maintenance identity used. Repair ticket #1539 remains separate.

**Next exact action:** source-authenticate the original divided-power H0/B0 evaluator and its fixed `[X]U` observer, then execute it at p=373. Identify and prove the map from native Frobenius/twist to the **unmodified** geometric q-Frobenius before applying the + sign; otherwise report typed comparator mismatch. Independently retain odd Green/Hesse and original kappa, verify two-digit eta if rank-one identified, then Source checkpoint under a genuinely authorized Researcher. No repeat of CM0/UR, finite 100k scalar scan or prior signed Clausen/Green auxiliaries. Schedule, scientific pin, P000 and notification settings unchanged.

**Sources:** Chisholm et al. original E3 and proposition (2013), https://www.math.rwth-aachen.de/~Gabriele.Nebe/papers/Ramanujan.pdf ; Hilbert `H_−24`, https://fungrim.org/entry/20b6d2/ ; consumed finite E3 note above; frozen taskbook `research_tasks/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT_610cb297.md@c47e13e4...`; native intake https://github.com/awdawmip/enterprise-math/issues/1559 ; control repair https://github.com/awdawmip/enterprise-math/issues/1539 .
