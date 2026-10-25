# D25/LIFT — complete Clausen-compatible Hasse cutoff through p²

2026-10-25. Follow-on mathematical unit to commit 632c88764249549565b632a976a5fd9e8d04c00a, which classified every intermediate p² Hasse port of the source-corrected Clausen family. TASK_RESEARCH: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; logical research conversation chatgpt-research-hourly-enterprise-math-20260923. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 untouched.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** The original CM/Frobenius experiment remains NOT_RUN. No new winning native CLAIM/open/checkpoint or formal mathematical admission is claimed.

## The previously unresolved high ports

For prime p=6m+1>=7, N=p-1, set c(x)=1/2-3x and

\[
\widetilde{\mathcal F}_p(x)=
\frac{(-x)_p(-2x)_p}{(c(x))_N N!},\qquad
\widetilde J_{k,p}=-[t^k]\widetilde{\mathcal F}_p(m+t).
\]

These are **signed Hasse coefficients of the endpoint forcing** from the exact corrected Gauss equation. The preceding first unit proved the formula for every k=n+2, 1<=n<=p-2, leaving k=p+1 and the tail k>=p+2. We now close both, producing a full classification of the infinite Hasse hierarchy modulo p².

Put

\[
A_p=
\frac{2(-1)^m m!(5m)!(2m)!(4m)!}{((6m)!)^2}
\in\mathbb Z_{(p)}^\times,
\]

write H_a=sum_{j=1}^a 1/j, let
q_p(a)=(a^{p-1}-1)/p for a=2,3, and let
W_p=((p-1)!+1)/p, the integer Wilson quotient.

## Theorem 1 — unique highest surviving port and explicit next digit

The endpoint coefficients satisfy

\[
\boxed{
\widetilde J_{p+1,p}\equiv
A_p\left[1+p\left(q_p(2)-q_p(3)+W_p-H_m-H_{2m}\right)\right]
\pmod{p^2}.}\tag{1}
\]

Here H_m,H_{2m} are evaluated in Z_(p), and only their reductions modulo p are needed in the p-multiplied correction.

**Proof.** Factor the fixed-source numerator forcing into
F_p(m+t)=A_p t²G(t) and its denominator correction
U_N(m+t)=U_N(m)E(t), with G=1+sum g_nt^n and E=1+sum e_nt^n. The first unit proved G≡(1-t^N)^2 and E≡(1-t^N)^(-1) modulo p and U_N(m)≡1 modulo p³. For every 1<=n<=N-1, g_n=e_n=0 modulo p. At n=N, the exact Newton recurrences therefore reduce modulo p² to

\[
N g_N\equiv-S_N,\quad N e_N\equiv T_N,\quad
\widetilde J_{p+1,p}\equiv A_p\frac{S_N-T_N}{N}\pmod{p^2},\tag{2}
\]

because all mixed positive-degree products in [t^N](GE) are p²-multiples. The sums are

\[
S_N=
\sum_{\substack{-m\le h\le N-m\\h\ne0}}h^{-N}
+2^N\sum_{\substack{-2m\le h\le N-2m\\h\ne0}}h^{-N},\quad
T_N=3^N\sum_{j=1}^N(j-p/2)^{-N}.
\]

The exact p-unit reflection expansion, valid at N=p-1 because N is p-invertible, yields

\[
S_N\equiv(1+2^N)H_N^{(N)}
-Np\left(H_m^{(N+1)}+2^NH_{2m}^{(N+1)}\right)\pmod{p^2},
\]

\[
T_N\equiv3^N\left(H_N^{(N)}+\frac{Np}{2}H_N^{(N+1)}\right)\pmod{p^2}.
\]

Now H_N^(N+1)=H_N^(p)≡H_N^(1)=0 modulo p, while H_m^(p)≡H_m and H_(2m)^(p)≡H_(2m) modulo p. Fermat quotients satisfy
1+2^N-3^N≡1+p(q_p(2)-q_p(3)) modulo p². Also

\[
H_N^{(N)}=\sum_{j=1}^N j^{-N}
\equiv N-p\sum_{j=1}^N q_p(j)
\equiv N-pW_p\pmod{p^2}.
\]

The last congruence uses the multiplicative Fermat-quotient law and Wilson's theorem:
q_p(N!)=sum q_p(j) modulo p, and N!=-1+pW_p implies (N!)^N≡1+pW_p modulo p². Substitute, divide by the unit N≡-1 modulo p, and obtain

\[
\frac{S_N-T_N}{N}
\equiv1+p(q_p(2)-q_p(3)+W_p-H_m-H_{2m})\pmod{p^2}.
\]

Inserting in (2) proves (1). QED.

## Theorem 2 — complete infinite tail truncates modulo p²

\[
\boxed{\widetilde J_{k,p}\equiv0\pmod{p^2}
\quad\textbf{for every integer }k\ge p+2.}\tag{3}
\]

This covers all high ranks, including the previously surviving fixed-denominator rank 2p. The bound is genuinely precise: at p=7, the unsigned corrected forcing has [t^9]Ftilde_7(m+t)=196=4(7²) modulo 7³, so k=p+2 need not vanish modulo p³. The signed value is -196 mod343 =147.

**Proof by p-local polynomial divisibility (not a finite sample extrapolation).** Over R=Z_(p), set

\[
P(t)=(-m-t)_p(-2m-2t)_p,\quad
D(t)=((1/2-3m-3t)_N)N!
=N!\prod_{j=1}^N(j-p/2-3t).
\]

D has degree N with p-unit leading coefficient, distinct p-integral roots t_j=(j-p/2)/3 for j=1,...,N. Their pairwise differences (j-k)/3 are p-units. At each root, x_j=m+t_j=(2j-1)/6 lies in Z_(p). Both (-x_j)_p and (-2x_j)_p contain among their p consecutive factors one divisible by p (since x_j and 2x_j each have a residue in F_p). Thus

\[
P(t_j)\equiv0\pmod{p^2}\quad\text{for all }j=1,\dots,N.
\]

Perform Euclidean division by D modulo p², legitimate because its leading coefficient is a unit: P=QD+R, deg R<N, deg Q<=2p-N=p+1. Since R(t_j)=P(t_j)=0 mod p² at N pairwise unit-separated roots, the Vandermonde evaluation matrix is invertible over Z/p². Hence R=0 modulo p². Since also D(0) is a p-unit, dividing by D as a formal power series shows Ftilde=P/D=Q modulo p², with Q of degree <=p+1. Thus all coefficients at k>=p+2 vanish modulo p². QED.

## Complete low-through-high Hasse classification

The source has an exact double zero at t=0; its signed k=2 coefficient is -A_p modulo p² because U_N(m)≡1 modulo p³. The preceding unit supplies every k=n+2 in 3<=k<=p. Equation (1) gives k=p+1, and (3) gives all k>=p+2, without unclassified high-rank ports.

This theorem applies to the **Clausen-corrected denominator family** only. It does not transfer the fixed-denominator all-Hasse formula into a genuine parameterized Clausen identity without its extra denominator source, and it does not identify auxiliary source involution with native Frobenius.

## Reproducible exact checks, BRC reuse and next research step

The companion pure-Python integer checker recomputes exact Taylor forcing coefficients modulo p² and the independent factorial/Fermat/Wilson/harmonic expression. All 35 primes p≡1 mod6, 7<=p<=373 pass the high port, low port and bounded upper-tail comparison; it checks **806** k>p+1 instances, plus the exact p=7 modulo-7³ sharpness witness. Actual output: PASS primes=35 high_port_formula=35 beyond_p_plus_one_zero_mod_p2=806 p7_t9_unsigned_mod343=196 AUTHOR_CHECKED_NOT_ADMITTED. Universal tail theorem derives from polynomial quotient/Vandermonde argument, not the finite checks.

BRC resolution **COMPOSE_APPLIED**: preserve signed source polynomial, parameter and denominator provenance, Hasse extraction rank and p-valuation before quotient. Here the polynomial-remainder theorem certifies that high-tail compression is safe *exactly at mod p²* for all Hasse coefficient observers. The p=7 mod p³ witness certifies that the same compression is unsafe at the next valuation horizon; this is a structural observation-dependent residual, not a failure of the model.

**Next executable mathematical unit:** Use this complete corrected-Hasse forcing classification together with the genuine parameterized Clausen symmetric-square and the ordered signed reflected corner to derive or refute the all-prime cross-source identity for LIFT. The hard congruence B_01,p + A_2 H_0/72 - T_jet,p = 0 is still unproved. Authentic same-original-class crystalline H0/B0, [X]U modulo p², Frobenius/eta orientation and kappa remain absent; native CM experiment NOT_RUN. Mother objective remains OPEN.

Canonical control status at the time of author derivation: same logical Research session has read-only continuation and a SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED checkpoint, but its saved predecessor claim differs from actual latest claim. No authorized own current run; issue #1558 remains controller-owned. These portable files are not source-native checkpoint or predecessor completed owner research. Scheduler, service identity and frozen Source pin were not mutated.
