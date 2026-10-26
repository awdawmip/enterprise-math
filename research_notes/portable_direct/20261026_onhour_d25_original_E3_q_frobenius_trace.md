# D25 / SECOND-DIGIT-LIFT — exact geometric q-Frobenius of the original d=3 elliptic CM curve

2026-10-26 · TASK_RESEARCH · author-side independently recomputed finite geometric certificate. Logical Research lane `chatgpt-research-onhour-enterprise-math-20260923`; distinct from CONTROL_PLANE_MAINTENANCE. Frozen scientific Source pin **`c47e13e4aba0e006366f989d6334d443f6333ae3`** is **unchanged**. Publication `TP2-B6F4FC938FF94941C1B7`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`.

**Classification: EXACT FINITE GEOMETRIC CERTIFICATE ON THE ORIGINAL E3 CURVE / AUTHOR CHECKED / UNREVIEWED / NOT_ADMITTED / NOT A SOURCE-NATIVE CHECKPOINT / NOT THE ORIGINAL H0/B0 [X]U BENCHMARK.** No new CLAIM, registered Researcher or independent review is asserted.

## One new original-object scientific unit: determine the degree-two geometric Frobenius sign, not merely its slope

Use the **original** elliptic family in Chisholm–Deines–Long–Nebe–Swisher, *p-Adic Analogues of Ramanujan Type Formulas for 1/π* (2013), §2 and §5.1:

Original exact curve: `E_3(t): y^2+x*y+(t/27)*y=x^3`, with `t=(2-T)/4`, `T^2=2` and `4*t*(1-t)=1/2`.

For a target prime `p == 13 or 19 (mod 24)`, `(2/p)=-1`; therefore `F_(p²)=F_p[T]/(T²-2)` is a field. The curve's Weierstrass discriminant is

`disc(E_3)=(t/27)^3*(1-t) != 0`,

so reduction is smooth for these primes. This is the actual elliptic `E_3(t)` model from the cited paper and the Source-frozen d=3 coefficient route; it is **not** the ordinary Hesse polynomial substituted for the still-unavailable original divided-power operator.

Let `q=p²`, `c=t/27`, and `D(x)=(x+c)²+4x³`. Completing the square in the Weierstrass equation gives an **exact** finite-field point-count identity:

`#E_3(F_q)=q+1 + sum_(x in F_q) chi_q(D(x))`.

For `z=a+bT`, the field norm is `N(z)=a²-2b²`, and the quadratic characters satisfy `chi_q(z)=chi_p(N(z))`, including `chi(0)=0`. Hence the sum can be evaluated by **enumerating all `p²` x-values with integer arithmetic**, without floating point, guessed Frobenius matrices, or the Hesse norm surrogate.

## Exact output and independent checks

| prime p | exact t in Fp² | signed character sum | #E3(Fp²) | trace a_(p²) |
|---:|---|---:|---:|---:|
| 13 | 7+3T | -26 | 144 | +26 |
| 19 | 10+14T | -38 | 324 | +38 |
| **373** | **187+93T** | **-746** | **138384** | **+746** |

The two minimal target residue classes have independent **direct y-enumeration** cross-checks for p=13 and 19. The primary p=373 result has an independent **full `F_(373²)` Euler-character exponentiation** cross-check, which does not use the norm/Legendre lookup. Both pipelines produce precisely 138384 points, including infinity. The (p=373) target field has `139129` x-values, and all are included (not a random sample).

Thus for **each of these three exact tested primes**, the **geometric q-Frobenius** `pi_q` of the *actual reduced elliptic curve* has Weil polynomial

`X^2-2*p*X+p^2=(X-p)^2`.

The endomorphism algebra of a supersingular elliptic curve over an algebraic closure is a division algebra. Hence the nilpotent `(pi_q-[p])^2=0` forces `pi_q=[p]`, not `[-p]`, **on this elliptic curve at these tested primes**. In particular, for p=373 the **unmodified geometric** q-Frobenius has precise sign +373, and the corresponding normalized geometric square is `pi_q/p=+1`, where that normalization is valid. This is an exact finite geometric identity with a standard endomorphism-algebra conclusion; it is **not** asserted uniformly for every target prime.

This fixes an input to any faithful comparison against the original curve's q-Frobenius. It does **not** identify the frozen H0/B0 divided-power module, nor does it license identifying the paper's chosen auxiliary degree-p² lift, quartic twist, or the provisional ordinary Hesse candidate with this unmodified geometric morphism. Different twists/normalizations may change the comparison; preserve that source distinction.

## Conditional normalization discriminator at p=373 (not a native H0/B0 comparison)

Consume (do not re-prove) the previous author source-aligned **ordinary** candidate `alpha=92060+21788T` modulo `373²=139129`, with `N(alpha)=122102` and first digit `131 mod 373`. **Only if** a later authenticated original-class identification proves (i) free rank-one sigma-semilinearity with coefficient `beta=eta*alpha`, and (ii) that its **normalized square** really equals the above unmodified geometric `pi_{373²}/373=+1`, the necessary scalar calibration is:

`N(eta)*122102 == 1 (mod 139129)` and hence **`N(eta) == 18818 (mod 139129)`**.

Here `122102*18818 mod 139129 = 1`; in the first digit `N(eta) mod373 =168`. This is a concrete **conditional** accepted-versus-rejected comparison target: any proposed `eta≡1 mod373` would be incompatible with that specific two-part identification, since `122102≡131≠1 mod373`. It does **not** prove the true `eta`, free rank-one structure, or operator type.

The `chi`, trace and norm projections drop the signed odd Hesse/Green and `kappa` ports. They **must not** be claimed to determine `[X]U` or the original `Delta_p-R_p` second digit. No Sun/A14(ii) conjecture, general p-adic LIFT, or experimental native divided-power completion is inferred.

## BRC and native/observer boundaries

**BRC resolution:** `COMPOSE_APPLIED` for a genuinely new source-typed geometric experiment (not a re-scan of the previously completed WZ/Green/weighted scalar). Population consists of the explicitly labeled p=13, p=19, p=373 fibers; carrier is the full original `E3(t)` equation, quadratic field basis, t, discriminant, exact signed character sum and operator type; observer is the q-Frobenius characteristic polynomial and endomorphism sign. Retain both CM source-conjugate ports and the actual model/twist when mapping to a future Frobenius matrix. Losslessly passing from the exact signed character sum to `#E` and `a_q` is justified for this observer, but **does not** preserve the later original `[X]U`, odd branch, `kappa`, or first/second p-adic scalar observers. `F_(p²)` is an external algebraic coefficient field, not the P000 six-dimensional native space or the complete three-dimensional slice.

**Executable independent evidence:** `research_notes/portable_direct/d25_E3_q_frobenius_point_count_20261026.py`, initially persisted at commit `738d0f1fd3e32dbd50463098332aed25bfe37fed`. Three exact cases PASS; independent y enumeration for p13/19 and independent Euler character enumeration for p373. No Sage/pari, remote CM machine or upload pointer is assumed.

**External source and precise type:** Chisholm et al. paper https://www.math.rwth-aachen.de/~Gabriele.Nebe/papers/Ramanujan.pdf, especially the E3 equation in §2 and the choice of lift / Proposition 16 on pp.17–20. The published supersingular proof chooses auxiliary lifts; *do not automatically equate those with unmodified geometric q-Frobenius*. The frozen Source has prior notes on the rank-one Hilbert–90 conditional comparator and the Proposition-16 quotient's missing second digit; both are consumed, not re-claimed as new mathematics.

## Exact continuation / unchanged original hard target

**Mother target remains OPEN:** (Delta_p-R_p=0mod p) for **all** `p≡13,19 mod24`, equivalent in the already source-aligned author reduction to `W_p≡p modp³`. This new finite **geometric** certificate neither proves LIFT nor gives its counterexample.

**Highest Source frontier (immutable, not replaced):** previously verified D25 checkpoint at `b58330b74576153cdadde5d80a3d92df3a819a0e`, `research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT/latest_checkpoint.json`; frozen original science pin unchanged. This note is independent author evidence `UNREVIEWED / NOT_ADMITTED`. Source's original 19 inherited native/scientific units, prior Green/p373 branches, WZ work, original UR/CM0 and old neutral staging remain distinct and **do not repeat**.

**Missing exact native acceptance evidence:** the *fixed original H0/B0 divided-power class* and its actual ([X]Umod373²), module rank, Frobenius direction/basis and degree-one-to-degree-two operator/twist bridge; source-proven (eta) or norm-(eta) precision; signed odd Green/Hesse observation; same-definition `kappa` and original `Delta_p-R_p`; independent review. The **next precise action** for the real native owner is to identify source-specific H0/B0/([X]U), record the q-Frobenius versus auxiliary (Phi)/twist correspondence and normalization, execute ([X]Umod139129), and only then test whether `pi_{373²}/373=+1` is its lawful comparator. Support owner pathway: existing #1559, `PENDING_OWNER`; **no executor was designated**.

**Research lane control state:** last verified recovery for `chatgpt-research-onhour-enterprise-math-20260923` has local provisional `MCP-de3e5bafb24f43f4a5e6285e7601676a` ACTIVE but `source_authority_verified=false`, historical contribution `EM-DIRECT-B63A06` not inherited, `claim=null`, `run=null`, preserved staging separate; request `research-onhour-20261026-1355-dispatch-r11` reached terminal `FAILED / TimeoutExpired` (#6529), not `NO_DISPATCH`. Current Sites read-only task request gave `CONTROL_QUOTA`. Do not claim/reopen/replay these mutations. Repair path remains existing #1539. **No Source-native checkpoint, Result/freeze, independent review, scheduler or notification modification.**
