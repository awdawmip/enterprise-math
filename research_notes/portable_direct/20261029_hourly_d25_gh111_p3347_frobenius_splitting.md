# D25/LIFT GH-111 — exact low-degree Frobenius orbits in exceptional 3347 fiber

2026-10-29 Asia/Hong_Kong. Author-side finite-field certificate: AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Research lane chatgpt-research-hourly-enterprise-math-20260923. Mother D25/LIFT/JT2 OPEN. Frozen Source c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

## Input

Use GH-110's separately reconstructed reflected polynomial R=R_3347 over k=F_3347, deg R=1673, with exact zero-fiber ramification 837[0]+2[9]. Let Q(z)=R(z)/(z^837(z-9)^2). GH-110 proves Q is squarefree of degree 834 and that the geometric and arithmetic groups of R(z)-t equal S_1673.

## GH-111 exact finite-field theorem

Define g_k(z)=monic gcd(Q(z), z^(3347^k)-z), for k=1,...,12. The exact degrees are:

    k:         1  2  3  4  5  6  7  8  9 10 11 12
    deg g_k:   0  0  0  0  5  0  0  0  0 15 11  0

Consequently Q has precisely one irreducible factor of degree 5, one of degree 10, one of degree 11 and no other factors of degree at most 12. All remaining irreducible factors have degree at least 13, with combined degree 808. The zero fiber of R has exactly two F_3347-rational points (0 and 9), and the other 834 geometric points have extension degrees at least 5.

Explicit irreducible factors, coefficients from constant term to leading coefficient:

    f5  = [2592, 980, 2615, 2622, 1784, 1]
    f10 = [3295, 1706, 2801, 2889, 2143, 3308, 2998, 2805, 557, 3178, 1]
    f11 = [1639, 1293, 1437, 1494, 324, 2374, 1556, 3110, 1714, 1336, 448, 1]

These three polynomials divide Q exactly.

## Proof and exact coverage

Over F_p, z^(p^k)-z is the product of all monic irreducible polynomials whose degree divides k, each to multiplicity one. Because Q is squarefree, gcd(Q,z^(p^k)-z) picks out exactly its irreducible factors whose degrees divide k. The degree-5 gcd must be one quintic; degree-10 gcd contains this quintic and one decic, since degrees 1,2 are absent. Degree-11 gcd contains exactly one degree-11 factor, because no degree-1 factor exists. The remaining gcd degrees exclude all other degrees at most 12. The sibling-dependent Python standard-library script, executed with exact modular polynomial Frobenius powering and gcds, asserts every degree and the displayed factor coefficients and divisibility. All checks PASS. This is a rigorous fixed-field certificate conditional on reviewing the code/arithmetic, not a general prime-family result or an independent CM explanation.

BRC COMPOSE_APPLIED: preserve the three distinct sources (original GH-3 truncation, reflected tail, Hasse polynomial), point multiplicity, extension degree and Frobenius orbit before summing to a scalar R(9). The p3347 exceptional zero is isolated among rational zero-fiber points while 26 further geometric points occupy three explicitly computed Frobenius orbits. This classical auxiliary field chart is not a native-X6 claim; P000/ACTIVE worldview remain unchanged.

## Remaining objective and control

Next action: obtain an independent CM/Jacobi/WZ/Frobenius character-sum evaluation that predicts R_3347(9)=0; separately continue GH-92 on original T_(p,9)=0 mod p. The current Gateway status/profile call reported BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false, so there is no newly verified current native CLAIM/OPEN/Source checkpoint. Old requests/staged evidence are preserved; Enterprise Math #1558 is the control support owner. Publication here is author portable evidence, not scientific admission.
