# D25/LIFT — Frozen Hesse lambda to signed E3 Gauss–Manin transport and observer (2026-11-12)

**Classification:** TASK_RESEARCH author-side exact geometric connection theorem; algebraically proved; exact modular checks EXECUTED for five target primes. **UNREVIEWED / NOT_ADMITTED / NATIVE H0/B0 [X]U NOT_RUN.**

## Authority, mother problem and provenance

- Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7.
- Frozen science: awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3, exact prior return research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md (verified blob cf36004694dc2c8c9134e2e1e989c076b88e4c03), which defines source Hesse H_lambda and lambda^(-3)=u=(2-T)/4, T^2=2.
- Own logical lane: chatgpt-research-onhour-enterprise-math-20260923; prior Source-signed Researcher EM-ENTERPRISE-9C9163 and same-session run RUN-d3deee35d5e9e40b9358ebbb. Existing successful checkpoint: bridge issue #6790, native Source commit 22db600561aab8d8aa1569e9c449d86562774961. No new author/reviewer identity claimed.
- Reuse without recrediting: D24 accepted UR/JT0, original 19 native predecessors, Green units, earlier Hesse-PF reflection, exact E3 Gauss–Manin matrix and Hesse geometric scaling (existing proof 70ab1ac40fd144f475839115d326506a03b0aaa1). Their last note left the source lambda-to-v differential observer as an explicit missing bridge.

## Theorem: exact lambda-coordinate and signed-port assignment

Let p be a prime with p ≡ 13 or 19 (mod 24), and R_r=(Z/p^r Z)[T]/(T^2-2). Let lambda be a chosen unit with lambda^3=4+2T, and choose r0 in R_r with r0^2=-3. Both roots exist and lift uniquely from a specified residue root since p>3. Put t=lambda^3, d=t-1, s=r0*lambda and

    u=lambda^(-3)=(2-T)/4,
    w=1-u=1-lambda^(-3)=(2+T)/4,
    dw/dlambda=3*lambda^(-4)=c.

For the *frozen source Hesse* curve H_lambda: x^3+y^3+z^3-3 lambda xyz=0 and the E3 family E_w: y^2+xy+(w/27)y=x^3, the established short-Weierstrass isomorphism uses s: (X_H,Y_H)=(s^2 X_E,s^3 Y_E).

**Signed port:** H_lambda matches E_(1-u)=E_w, not E_u. Applying sigma(T)=-T sends lambda to bar(lambda) with bar(lambda)^3=4-2T, and w to v=u=(2-T)/4; hence the original E_v geometric model matches **H_(bar lambda)**. This fixes the conjugate-j mismatch observed previously, without identifying the two Hesse models as the same signed port.

The invariant differentials and full rank-two bases obey

    e_E=(e_H) G,   G=diag(s,s^(-1)),
    omega_E=6 e0_E=3s omega_H,   omega_H=2 e0_H.

Here the row (e0,e1) denotes the ordered basis and coordinate columns multiply on the right.

## Exact source lambda Gauss–Manin transport

Reuse the full matrices already proved on the respective smooth families:

    M_E(w)=1/[12w(1-w)] * [[4w-3,8w-9],[1,3-4w]],

    M_H(lambda)=
      [[-3lambda^2/(4d), 3lambda(t+8)/(4d)],
       [-1/(12d),       3lambda^2/(4d)   ]].

With the derivative d/dlambda (not the t-derivative or a logarithmic operator), the exact *two-column* identity is

    c M_E(w) = G^(-1) M_H(lambda) G + G^(-1) dG/dlambda,
    G^(-1) dG/dlambda=diag(lambda^(-1), -lambda^(-1)).

Proof: w=d/t, so w(1-w)=d/t^2; c=3/(lambda*t); s^2=-3lambda^2. The right-hand matrix entries are

    (t-4)/(4lambda d), -(t+8)/(4lambda d),
    lambda^2/(4d),     -(t-4)/(4lambda d)

in row-major order. Direct substitution in c M_E gives these four expressions identically. All denominators are units for the stated primes and source points. This is an algebraic family-level identity, not a numerical fit.

**Exact frozen signed Hesse observer transport:** for Omega_H=omega_H+6 nabla_(d/dlambda) omega_H, the H-basis coefficients are

    [Omega_H]_H = (2-9lambda^2/d, -1/d)^T.

The matching E_w-basis coefficients are G^(-1)[Omega_H]_H. Equivalently, differentiating omega_H=omega_E/(3s) gives the explicit Leibniz correction

    Omega_H = (1/(3s)) *
      [ (1-6/lambda) omega_E + 6c nabla_(d/dw) omega_E ].

Thus **omega_E+6 nabla_w omega_E** is not a direct replacement for the source **omega_H+6 nabla_lambda omega_H**. The factor 1/(3s), the -6/lambda term, the source lambda root and the sign sigma all affect the original fixed observer.

The source-lambda cyclic basis has determinant

    det(omega_H, nabla_lambda omega_H) = -1/(3d).

For the matching E_w basis,

    det(omega_E,nabla_lambda omega_E) = 9lambda^2/d;

on the frozen CM port t^2=8d this equals 72/lambda^4. Both are p-adic units for every target prime. A future native Frobenius matrix must respect this complete cyclic basis and the above derivative-gauge transport.

## Exact executed p^2 certificate

The stand-alone integer checker operates directly in R_2 with pair coordinates (a,b) for a+bT, modular inverse by norm a^2-2b^2, an explicit cube-root search in F_(p^2), Newton/Hensel lift modulo p^2, and a separately lifted r0^2=-3. It asserts all four connection-gauge entries, both signed-observer coefficients, the complete source lambda-coordinate and both cyclic determinants for p=13, 19, 37, 43, 373. **All five passed**; no floating-point or unexecuted native evaluator was used.

At p=373, modulus 139129, choose the actual frozen source branch lambda ≡ 56+19T mod373. Its unique lift selected by this residue is

    lambda = 91441 + 93269 T,  lambda^3=4+2T;
    r0=89697, s=50569+122723 T;
    w=69565+104347 T, c=109225+125015 T.

Full observer (coefficient pair notation (a,b) for a+bT):

    [Omega_H]_H = (22053+60478T, 139126+2T)^T,
    [Omega_H]_(E_w) = (104561+38876T, 60927+11227T)^T.

Both routes (direct H matrix and E-side Leibniz rule) yield the same E-coordinate vector. The exact cyclic determinants are

    det Q_E^lambda = 117078+78651T,
    det Q_H^lambda = 139128+46377T            (mod139129).

The original E_v signed chart uses the conjugate root bar(lambda)=91441+45860T and the conjugated observer entries, with the fixed original E_v Gauss–Manin matrix from the previous note. The geometric Frobenius/CM source sign and quadratic twist remain independent information.

**Reproducible code:** tools/check_d25_lambda_e3_connection_bridge_20261112.py, immutable initial code commit 9f1e505d95409239c6827ba944d5a7ae74c47b40, Git blob 375290abd5257d313b671f75eb4e22ddb2eacfe7, SHA256 8bc11cbf160678098992097112eb34f6c39da08ca730aa649e9ba572fe043e27. Exact code bytes were executed locally and remotely read back as the same blob.

## Next smallest unmet native unit

The p373 **original same-class H0/B0 divided-power [X]U modulo139129**, actual native module rank, genuine sigma-semilinear Frobenius in that source H0/B0 basis, eta, signed kappa and Delta_p-R_p remain **NOT_RUN / OPEN**, with support issue awdawmip/enterprise-math#1559 PENDING_OWNER. The new theorem completes the source Hesse lambda to geometric E3 parameter/differential-map sub-obligation; it does not complete the H0/B0 to de Rham basis comparison. A qualified native executor must now deliver the actual H0/B0 matrix and operator with its source pin; compare both columns through the explicit lambda-derivative gauge and conjugate signed ports; then independently replicate and compare kappa/Delta-R for both residue classes.

**Status:** AUTHOR_PROVED / FIVE_EXACT_MODULAR_REGRESSIONS_EXECUTED / SOURCE_COORDINATE_BRIDGE_COMPLETE / UNREVIEWED_NOT_ADMITTED / NATIVE_BENCHMARK_NOT_RUN.
