# D25 | Exact CM quadratic-twist bridge between the original 216 and published 2304 families (2026-11-03)

**Evidence class:** AUTHOR-DERIVED / PROVED EXACT ALGEBRA / FINITE EXACT CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. This is author-side math, not native Source checkpoint, formal Result, independent review, or the native H0/B0 experiment.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research logical conversation `chatgpt-research-onhour-enterprise-math-20260923` is distinct from the maintenance conversation. Previous author-side checkpoint: `80f47c5080f82e11f23708516aa337f3504ff261`.

## Exact selected mother-goal dependency

D24 accepted first digit and previously proven original frozen R/Clausen port establish that for primes p ≡13,19(mod24) the D25 goal Δ_p−R_p=0(mod p) is equivalent to the ORIGINAL weighted 216 congruence

    W216(p−1) = Σ_{k=0}^{p−1} (6k+1) (1/2)_k (1/3)_k (2/3)_k /(2^k (k!)^3)
              ≡ p (mod p^3).                      [OPEN]

Guo--Zudilin, *A q-microscope for supercongruences*, Adv. Math. 346 (2019), DOI:10.1016/j.aim.2019.02.008, proves the DIFFERENT original 2304 sum

    S2304(p−1) = Σ_{k=0}^{p−1} (8k+1) (1/4)_k (1/2)_k (3/4)_k /(9^k (k!)^3)
              ≡ p (-3/p) (mod p^3).

For both D25 target classes the published right-hand side is p. This note derives their exact elliptic **geometric** relationship and its signed character defect, not an identity between truncated weighted hypergeometric sums.

## Theorem A — exact quadratic twist in K=Q(sqrt2)

Put s=√2, t3=(2−s)/4, t4=(3−2s)/6, and d=3s. Use precisely the Chisholm--Deines--Long--Nebe--Swisher (2013), *p-Adic Analogues of Ramanujan Type Formulas for 1/π*, DOI:10.3390/math1010009, §2 elliptic families

    E3 : y²+xy+(t3/27)y = x³,
    E4 : y² = x(x²+x+t4/4).

Their published period-parameter convention is λ=−4t(t−1); direct calculation gives λ3=1/2 and λ4=1/9. These are exactly the unweighted hypergeometric parameters inside original W216 and S2304.

The four nontrivial invariant formulas in Q(s) are:

    c4(E3)=(5+2s)/9,     c6(E3)=−(12+7s)/27,
    c4(E4)=10+4s,       c6(E4)=−28−24s,
    Δ3=t3³(1−t3)/27³,  Δ4=t4²(1−t4).

Direct rational arithmetic in Q(s) proves

    c4(E4)=d² c4(E3),   c6(E4)=d³ c6(E3),   Δ4=d⁶ Δ3,
    j(E3)=j(E4)=2417472+1707264√2.

An explicit isomorphism after adjoining u with u²=d is

    x4=d(x3+1/12)−1/3,
    y4=u³(y3+(x3+t3/27)/2).

PROOF: square-completing E3 gives (y3+(x3+t3/27)/2)²=x3³+(x3+t3/27)²/4. Substitute the displayed x4 into x4³+x4²+(t4/4)x4 and compare polynomial coefficients of 1,x3,x3²,x3³. All four coefficients equal the corresponding coefficients of d³[x3³+(x3+t3/27)²/4], by exact Q(s) arithmetic. The displayed y4 then gives the claimed isomorphism. The invariant equalities independently certify its quadratic-twist type. No prime enumeration is required. QED.

## Theorem B — opposite twist sign in the two D25 target classes

For every target prime p≡13 or19 (mod24), put k=Fp[s]/(s²−2)=F_(p²). Let a_(p²)(E)=p²+1−#E(k), the **external** elliptic Frobenius trace (not native H0/B0).

Then

    a_(p²)(E4) = χ_k(d) a_(p²)(E3),
    χ_k(d) = { −1 if p≡13(mod24); +1 if p≡19(mod24) }.

PROOF: Under the above affine x-variable bijection, the two completed-square cubic RHS are related by multiplication by d³ times a square. Their quadratic-character point-count sums therefore differ by χ_k(d). Since s^p=−s, Norm_(k/Fp)(d)=(3s)(−3s)=−18. Hence χ_k(d)=(−18/p)=(−2/p); supplementary quadratic reciprocity yields exactly the two stated signs. Good reduction holds for these p>3 from the displayed discriminants. QED.

This is a **uniform exact signed elliptic-trace theorem**, but NOT a proof that the original truncated weighted W216 and S2304 sums are equal (or related by χ) modulo p³: an additional original-source p-adic *period/readout/normalization* bridge is essential. In particular, equality of j or of elliptic traces alone is insufficient for the D25 acceptance claim.

## Executed exact independent evidence

The companion Python standard-library script checks in Fraction arithmetic over Q(√2): both λ parameters, shared j, all invariant scaling, and all four cubic-isomorphism coefficients. It then exhaustively counts both curves' points over F_(p²) using exact quadratic-character evaluation for each of six primes. All PASS:

| p | p mod24 | χ_k(d) | a_(p²)(E3) | a_(p²)(E4) |
|---:|---:|---:|---:|---:|
| 13 | 13 | −1 | 26 | −26 |
| 19 | 19 | +1 | 38 | 38 |
| 37 | 13 | −1 | 74 | −74 |
| 43 | 19 | +1 | 86 | 86 |
| 109 | 13 | −1 | 218 | −218 |
| 373 | 13 | −1 | 746 | −746 |

At p=373, cardinality F_(p²)=139129 coincides numerically with the native benchmark coefficient modulus; this external point-count is **NOT** the original-class divided-power [X]U mod139129, native rank, semilinear Frobenius eta, odd Green/Hesse or kappa. Finite checks are regression evidence for the separate exact theorem.

BRC / Enterprise-coordinate resolution: **COMPOSE_APPLIED**. Source carriers: E3/λ3 versus E4/λ4 plus original W216/S2304 ordered truncated coefficients. Preserved coordinates: (t3,t4,d,p-class,χ,curve-family,field). Proved observer: j and F_(p²)-point traces. Pending future observer: original weighted W216 modulo p³ including signed boundary, normalization and p-adic division. The ellipse models are external auxiliary arithmetic, not a P000 native plane or an X6 spatial proof.

## Next exact action / control handoff

Prioritized small scientific unit: find/prove a p³-level **finite, weighted, cutoff-preserving period or WZ transport** from the published S2304 p³ theorem at λ4=1/9 to the ORIGINAL 216 weighted sum at λ3=1/2, with both 13/19 character branches, unit/normalization and the known nonzero original p² high tail. The existing signed original Cauchy L+U−T route remains available as an independent approach. Do not redo D24 CM0/UR, scalar F216 p² source, broad finite stress, or the previous one-jet Cauchy observations.

Native support #1559: OPEN on read 2026-11-03, no assignee; benchmark remains PENDING_OWNER / NOT_EXECUTED. Responsible path is authenticated native H0/B0 executor or designated maintainer, with acceptance on exact p373 original module rank, [X]U mod139129, eta, signed odd κ, and independent reproduction.

The actual native em_status request in this run returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE`, `operation_sent=false`; therefore new recovery_status/continuation, authenticated session, CLAIM/run, Source checkpoint, Result, review or pre_final were not obtained. Original historical request `research-onhour-20261031-0205-dispatch-r15` remains for future receipt/reconcile; no mutation replay. The on-hour schedule, activation and notifications were not modified.

Sources: 2013 exact elliptic family and λ convention https://www.math.rwth-aachen.de/~Gabriele.Nebe/papers/Ramanujan.pdf ; published 2019 S2304 theorem https://arxiv.org/abs/1803.01830 ; previous D25 author notes `research_notes/portable_direct/20261102_onhour_d25_cm_scalar_theorem2_discharge.md` and `research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md`.
