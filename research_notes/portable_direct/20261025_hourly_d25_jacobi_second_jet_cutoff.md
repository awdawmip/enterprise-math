# D25/LIFT — exact cutoff forcing in the second terminating Jacobi parameter jet

Date: 2026-10-25 (Asia/Hong_Kong). TASK_RESEARCH portable, author-side proof. Logical Research lane: chatgpt-research-hourly-enterprise-math-20260923, distinct from CONTROL_PLANE_MAINTENANCE. Formal Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged.

**Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** Neither a canonical CLAIM/run/checkpoint nor a native divided-power, Frobenius, or CM experiment. The original LIFT/JT2 claim remains OPEN.

## Exact source and first question

Consume (do not re-credit) the frozen scalar Jacobi interface from research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md, and the accepted first-digit UR/JT0 result. The parent explicitly retains the finite-cutoff second parameter derivative Phi_xx in G_p modulo p^2. This unit determines its previously unisolated **top-degree forcing term**, including its universal mod-p coefficient.

Fix an integer m>=1 and N=6m. Define the exact rational polynomial family

    Phi_m(x,z) = SUM_(n=0)^N b_n(x) z^n,
    b_n(x) = (-x)_n (-2x)_n / (n!)^2,

and a hypergeometric differential operator

    L_x = z(1-z)d_z^2 + [1+(3x-1)z]d_z - 2x^2.

At x=m define F_0=Phi_m(m,z), F_1=d_x Phi_m(m,z), F_2=d_x^2 Phi_m(m,z). All equalities in the first theorem are exact in Q[z].

## Theorem 1 — exact inhomogeneous second-jet boundary equation

For every m>=1,

    L_m F_0 = 0,
    L_m F_1 + (3z d_z - 4m)F_0 = 0,
    L_m F_2 + 2(3z d_z - 4m)F_1 - 4F_0
        = -20 m^2 b_N''(m) z^N,                        (J2)

where the endpoint has the explicit nonzero rational value

    b_N''(m) =
       4(-1)^m m! (2m)! (4m-1)! (5m-1)! / ((6m)!)^2.

**Proof.** The untruncated coefficient recurrence is

    (n+1)^2 b_(n+1)(x)=(n-x)(n-2x)b_n(x).

The coefficient of z^n in L_x of the truncated series vanishes for n<N. At n=N the term containing b_(N+1) is deliberately absent, yielding the exact endpoint identity

    L_x Phi_m(x,z)=-(N-x)(N-2x)b_N(x)z^N.

Both Pochhammer factors in b_N contain separate simple zeros at x=m, one at n-index j=m and one at j=2m. Therefore b_N(m)=b_N'(m)=0, whereas b_N''(m) is the displayed factorial product, obtained by differentiating both zero factors. Differentiate the exact operator identity 0,1,2 times at x=m. Since d_x L_x=3z d_z-4x and d_x^2 L_x=-4, the first two endpoint defects vanish, while the second is -[(N-m)(N-2m)]b_N''(m)z^N=-20m^2 b_N''(m)z^N. QED.

This identifies three *source-labelled derivative ranks*: n<=m may contribute at order 0; m<n<=2m first appears at order 1; and 2m<n<=6m first appears at order 2. At the terminal rank N=p-1, discarding the double-zero source because its value and first derivative vanish would erase the nonzero forcing in (J2).

## Theorem 2 — all-prime universal finite-field boundary coefficient

Let p=6m+1 be a prime (hence p>=7). Reduction is legitimate in Z_(p) because every n! with n<=p-1 is a p-unit. The endpoint satisfies

    b_(p-1)''(m) = 4/[(m+1)(2m+1)] = 36/5 (mod p).

Indeed, Wilson factorial complements pair (5m-1)! with (m+1)! and (4m-1)! with (2m+1)! in the exact expression from Theorem 1; signs cancel. Here m+1=5/6 and 2m+1=2/3 (mod p). Since -20m^2*(36/5)=-4 (mod p), Theorem 1 gives the **universal source boundary defect**

    L_m F_2 + 2(3z d_z-4m)F_1 -4F_0 = -4 z^(p-1) (mod p).    (B)

This is a proved all-eligible-primes coefficient identity, not a finite-prime extrapolation. It describes the exact frozen terminating Jacobi parameter jet Phi_xx; it is not an all-prime proof of LIFT.

## Theorem 3 — one full p^3 moment anomaly at the original source parameter

Put

    f_p(z)=SUM_(n=0)^(p-1) [(1/6)_n(1/3)_n/(n!)^2] z^n,
    r_n=(1/6)_n(1/3)_n/[2^n(n!)^2],
    g=SUM r_n, d=SUM n*r_n, M2=SUM n^2*r_n,
    h=g+12d,

all with n=0,...,p-1 and exact rational arithmetic first. This f_p is Phi_m(x,z) at x=-1/6, not at x=m; the distinction is essential.

The truncated recurrence gives

    L_(-1/6) f_p(z)
      = -(p-5/6)(p-2/3)b_(p-1)(-1/6) z^(p-1).

The factors (1/6)_(p-1) and (1/3)_(p-1) each contain exactly one p. Strip these two p factors before reducing. By Wilson, the nonzero factors (6j+1) for j=0,...,p-2 except j=m multiply to 1/5 modulo p; the corresponding nonzero (3j+1) except j=2m multiply to 1/2. Since 18^(p-1)((p-1)!)^2=1 (mod p),

    b_(p-1)(-1/6)/p^2 = 1/10 (mod p).

Consequently

    L_(-1/6) f_p(z) = -(p^2/18) z^(p-1) (mod p^3).

At z=1/2, the differential operator is

    L_(-1/6) f_p(1/2)=f_p''(1/2)/4+f_p'(1/2)/4-f_p(1/2)/18.

Using f_p'(1/2)=2d, f_p''(1/2)=4(M2-d), and 2^(p-1)=1 (mod p), we obtain the **uniform exact source-moment certificate**

    18 M2 - 9d - g = -p^2 (mod p^3),                    (M)

equivalently

    72 M2 - 3h - g = -4p^2 (mod p^3).                  (M-h)

The full signed, rank-labelled second moment is essential: reducing the defect modulo p^2 erases its nonzero next digit. The identity provides a deterministic consistency port for future exact G_p=g/p and h observations but does **not** determine the target Delta_p-R_ref,p.

## Source, BRC, and theorem-strength audit

The exact population is the ordered coefficient ranks n=0,...,p-1 and the original signed rational amplitudes b_n; state retains derivative order (0,1,2), cutoff N and p-adic valuation. The permitted operations are parameter differentiation, finite recurrence, signed weighted sums and reduction after exact p-factor extraction. The observer is the top-degree z^N coefficient modulo p and the moment relation modulo p^3. This is BRC COMPOSE_APPLIED in the explicit source/jet/valuation carrier sense; no native BRC or CM software was executed. Boolean support or mod-p-only totals would not preserve the future differentiated cutoff operation.

Author checker: research_notes/portable_direct/20261025_hourly_d25_jacobi_second_jet_cutoff_check.py. It independently checks all coefficients of three polynomial identities in exact Fraction arithmetic for m=1..6; verifies the endpoint factorial identity; then checks (B) and (M)/(M-h) with integer modular recurrence for 83 eligible primes (including 373 and 1327), all PASS. This is author arithmetic, not independent review. The universal theorem claims rest on the displayed algebra.

**Remaining mother-target obligation.** The formal D25 LIFT condition is Delta_p=(G_p h-1)/p congruent R_ref,p=Q_p/p^2 mod p for p=13 or 19 (mod24). Here R_ref,p is the *reflected Clausen corner*, not g. Theorems (B)/(M) do not establish this congruence or native Frobenius. The missing discriminating step is a genuine same-original-class derivation of the divided-power Frobenius/parameter connection and/or a signed telescoper relating this derivative-jet forcing to Delta_p-R_ref,p without replacing it by a higher moment. Frozen science Source, native checkpoint, contributor histories, original support fault and prior accepted units remain unchanged.

Native continuation readback 2026-10-25: recovery request r11recovery20261025t1516hk01; continuation request r11cont20261025t1520hk01; full receipt pages r11receiptraw20261025t1522hk01 and r11receiptraw20261025t1526hk02. They confirm persisted_checkpoint.state=SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED, no winning current CLAIM/run, last_claim_id MCP-d0d70cd041b01e5db192870a versus continuation.expected_previous_claim_id MCP-87631b892b41fa18d799f2d8. No continuation_prepare replay, CLAIM, OPEN, native checkpoint, Result, review or PRE_FINAL authority is claimed here.
