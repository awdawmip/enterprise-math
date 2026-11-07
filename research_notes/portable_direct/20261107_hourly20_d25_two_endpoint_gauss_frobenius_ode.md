# D25 — Universal two-endpoint Frobenius forcing for the normalized Gauss tails
2026-11-07 · TASK_RESEARCH · **AUTHOR-SIDE EXACT ALGEBRA / FINITE VERIFIED / UNREVIEWED / NOT_ADMITTED**.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3. Hourly20 logical lane (historical reported identifier) chatgpt-research-hourly-enterprise-math-20260923 is separate from maintenance chatgpt-hourly-enterprise-math-20260921 and parallel onhour. Current Source identity is not verified.

## Consumed, not repeated
This unit **uses** the author-side p² fold 6cb6a01eccee001775e3aacadcb34961048157e5 and the separate onhour p³ projected fold 36b2cab4deb92e75008f244d377359a3de33d547 plus factorial normalized-tail kernels 50346cde208fb05673de7e7ed367f4998f200a1b. Those existing theorems are not claimed anew. The new result is an exact operator-level source representation with universal upper boundary and uniqueness.

## Definitions and theorem
Work in F_p[z] for primes p>3. Let θ=z d/dz and L_(a,b)=θ²-z(θ+a)(θ+b). For p=6m+1, set (a,b)=(1/6,1/3) and
R_A(z)=Σ_(n=2m+1)^(p-1) [( (1/6)_n (1/3)_n/(n!)² )/p² mod p] z^n.
Then, coefficientwise **including degree p**,

    18 L_(1/6,1/3) R_A =
       (-1)^m / binom(2m,m) * z^(2m+1) - z^p.              (A)

For p=8k+3 use (a,b)=(1/8,3/8); for p=8k+5 use (a,b)=(5/8,7/8). Put
R_B(z)=Σ_(n=3k+2)^(p-1) [( (a)_n (b)_n/(n!)² )/p² mod p] z^n.
Then both classes satisfy

    (64/3) L_(a,b) R_B =
       -1/binom(3k+1,k) * z^(3k+2) - z^p.                (B)

The Euler multiplier (1-z) for the 8k+5 2304-series is retained **outside** this Gauss operator. Both upper boundary charges are exactly -z^p after normalization, independent of p or the B-class. The lower injection charges and exponents are different and nonzero. Each R is uniquely determined by its lower injection and the stated support  h<=degree<p.

## Proof
If R=Σ_(n=h)^(p-1)r_n z^n, the coefficient of L_(a,b)R at degree n is
n²r_n-(n-1+a)(n-1+b)r_(n-1), with r_(h-1)=r_p=0. The exact Gauss recurrence annihilates all interior coefficients h<n<p. The factorial kernels give the lower coefficients
h²r_h=(-1)^m/[18 binom(2m,m)] (A),
h²r_h=-3/[64 binom(3k+1,k)] (B).
Wilson's theorem gives (p-1-t)!≡(-1)^(t+1)/t! mod p; hence the terminal coefficients are
r_(p-1)=1/[18(m+1)(2m+1)] (A) and
r_(p-1)=3/[64(k+1)(3k+2)] (B).
Because a,b≡-m,-2m in (A), and {a,b}≡{-k,-(3k+1)} in either (B), the degree-p coefficients are respectively -1/18 and -3/64. Scaling proves (A),(B). For h<n<p, n² is a p-unit, so the recurrence uniquely constructs the R coefficients from h²r_h. QED.

## Residual interpretation and next unit
The universal -z^p boundary is a preserved Frobenius source. At a nonzero F_p evaluation point z^p=z while θ(z^p)=0: the scalar and derivative observers carry different information. The normalized operator source is shared; the lower source, index, Euler flag, Fricke observation coordinate and underlying Gauss operator remain distinct. These relations can be fed into the existing p³ weighted bridge (G_A-G_B)/p² + E_A-E_B (mod p) without collapsing the projected overflow. They do **not** prove this bridge.

Next exact scientific action: insert both forced ODEs into the two Fricke parameter pullbacks; seek an adjoint/gauge identity matching the two lower forcing monomials while preserving the Euler multiplier and two evaluation coordinates. Test p=13,19,43,67,373, then try to prove W_p=p mod p³ for p=13,19 mod24. Mother objective Δ_p-R_p=0 mod p remains OPEN.

## Executed exact verification
The companion script independently regenerates the Gauss coefficients mod p³, reconstructs the normalized tail using only the forced ODE, and verifies every coefficient through degree p. All tested primes p<=2500 passed: A:178, B3:93, B5:96. Representative lower/upper coefficients (p,stream,lower,upper): (13,A,10,5),(13,B5,4,3),(19,A,1,1),(19,B3,12,5),(373,A,155,145),(373,B5,17,134). Author-side proof is independent of the finite checks; p373 native H0/B0 remains a separate unperformed experiment.

Native status probed 2026-11-07T12:23Z: em_status BACKEND_IDENTITY_OR_VERSION_MISMATCH (operation_sent=false); Site CONFIGURED_NOT_LIVE_VERIFIED / research_authority_granted=false. Preserve unknown original requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13, old session/claim/run/staging UNKNOWN/PRESERVE, registration REGISTER_PENDING, and support issue #1558. No native checkpoint, independent review, Source admission or Result asserted.
