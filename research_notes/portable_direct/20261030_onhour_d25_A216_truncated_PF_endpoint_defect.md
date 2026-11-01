# D25 / SECOND-DIGIT-LIFT — exact truncated A216 differential endpoint obstruction

2026-10-30 Asia/Hong_Kong. Research lane \`chatgpt-research-onhour-enterprise-math-20260923\` (not maintenance); task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` unchanged. Evidence: AUTHOR-SIDE / ALGEBRAICALLY PROVED / FINITE EXACT CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.

## Exact truncation identity (proof)

Let m>=1, N=3m, a=-3m+T/2, b=-2m+T/3, c=-4m+2T/3, and
\[
F_{m,T}(z)=\sum_{n=0}^{N}\frac{(a)_n(b)_n(c)_n}{(n!)^3}z^n,\quad
\theta=z\,d/dz,\quad
\mathcal L_{m,T}=\theta^3-z(\theta+a)(\theta+b)(\theta+c).
\]
Then **exactly in rational polynomial algebra**
\[
\boxed{\mathcal L_{m,T}F_{m,T}(z)=-(N+a)(N+b)(N+c)
\frac{(a)_N(b)_N(c)_N}{(N!)^3}z^{N+1}.}\tag{PF1}
\]
For \(f_n=(a)_n(b)_n(c)_n/(n!)^3\), the recurrence \(n^3f_n=(n-1+a)(n-1+b)(n-1+c)f_{n-1}\) cancels each coefficient of \(\mathcal LF\) through degree N. Only the displayed cutoff term at \(N+1\) survives.

For primes p=6m+1>=7 put T=p, so \(a,b,c=(1/2,1/3,2/3)\). The *original* A216 unweighted coefficient
\[
a_n^{216}=\binom{2n}{n}^2\binom{3n}{n}/216^n
=\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}
\]
satisfies \(a_N^{216}=f_N(1/2)^N\). Also \((N+a)(N+b)(N+c)=p(9p^2-1)/72\). **Differentiation precedes evaluation** at z=1/2. Therefore
\[
\boxed{(\mathcal L_{m,p}F_{m,p})(1/2)
=-\frac{p(9p^2-1)}{144}a_{3m}^{216}.}\tag{PF2}
\]
The earlier author-side exact endpoint proof (project \`b22324e4deaa6fd0f443d753237446af180a10f1\`) establishes \(a_{3m}^{216}/p\equiv-2\chi_p\pmod p\) for \(\chi_p=(6/p)\). Hence
\[
\boxed{(\mathcal L_{m,p}F_{m,p})(1/2)/p^2
\equiv-\chi_p/72\not\equiv0\pmod p,\qquad p\equiv1\pmod6,\ p\ge7.}\tag{PF3}
\]
The denominator 72 is p-invertible and chi_p is ±1. Thus the naive *homogeneous* truncated Picard–Fuchs (3F2) differential equation at precision p^3 is **false for every prime in scope**. This is a mathematical proof-route exclusion, not a counterexample to the frozen LIFT.

## Relation to original signed lower port and next certificate

The actual signed low-port observation is \((1+6\theta)F_{m,p}(1/2)=A_{\rm low}\); the two-zone p-adic parameter jet \`research_notes/portable_direct/20261030_onhour_d25_A216_low_two_zone_padic_second_jet.md\` at commit \`866cf57e4ff5cb66f7d29e155cecee61a072c5df\` proves the n=2m zero-factor and both \(U_{2,\mathrm{int}}\), \(U_{2,\mathrm{cross}}\). Preserve those sources and the nonzero PF3 endpoint as distinct evidence. The required LIFT remains \((A_{\rm low}-p)/p^2+C_mH_m=0\pmod p\) for p≡13,19(mod24). A valid paired parameter-contiguous/WZ certificate must keep the inhomogeneous cutoff, the n=2m jet crossing and the earlier middle-kernel p-resonant boundary factor three; all-prime source cancellation remains unproved.

BRC COMPOSE_APPLIED: preserve index, signed 1+6theta readout, coefficient valuation, endpoint source and operation order before modulo-p observer. Homogeneous/total-only compression erases the measured nonzero boundary forcing. This is a p-local scalar relation, not native X6 or H0/B0 operator equivalence.

## Executed validation and provenance

Companion \`research_notes/portable_direct/d25_a216_truncated_picard_fuchs_boundary_guard_20261030.py\` (standard-library Python) actually ran the ORIGINAL A216 weighted coefficient recurrence, independent raw binomial integer endpoint, finite \(\mathcal L\) residual modulo p^3, and divided defect. **115/115 primes** 7<=p<1500, p≡1(mod6), passed PF2/PF3; e.g. p13 defect 2, p19 defect 5, p373 defect 57 modulo the respective p. Finite execution supports the algebraic proof, not an infinite-scope certification on its own.

Native benchmark #1559 (same original p373 H0/B0 divided-power \([X]U\bmod139129\), rank, semilinear Frobenius/eta, odd signed Green/Hesse, kappa, independent reproduction) remains separate and PENDING_OWNER; no surrogate. The 2026-10-30 Site status showed \`research_authority_granted=false\`, \`write_relay_enabled=false\`, and client checkpoint list ACCESS_DENIED. No Source session, claim, run, checkpoint, native Result, review or acceptance is asserted. P000, scientific pin and separate maintenance lane unchanged.
