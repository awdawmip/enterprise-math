# D25: directed Gauss–Green boundary transfer across the original 216 H2 band

Date: 2026-11-03 (+08). Status: **AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This portable research note is not a native checkpoint, claim, run, Result, review, or source admission.

Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`; parent \`ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION\`. Logical Research lane \`chatgpt-research-hourly-enterprise-math-20260923\`; do not conflate with the separate maintenance lane. This note consumes and extends existing source-preserving H2 transport and the previously established Green recurrence; it changes no frozen input.

## The new unit: two p-adic singular boundary transfers

For each prime p=6r+1 >=7, let

\[
b_k=\frac{(2k)!(3k)!}{(k!)^5\,216^k},\qquad
a_k=2^k b_k,\qquad B_k=(6k+1)b_k,
\]
\[
Q_t=\frac{(2t-1)(3t-2)(3t-1)}{18}.
\]

The following are congruences of p-adic units after the displayed p powers have been divided out:

\[
\boxed{\frac{b_{3r+1}}{p^2}\equiv-\frac1{18}\frac{b_{3r}}p\pmod p},
\qquad
\boxed{\frac{b_{4r+1}}{p^3}\equiv\frac12\frac{b_{4r}}{p^2}\pmod p}.
\]

For the original **directed signed** terms, the corresponding two edge couplings are

\[
\boxed{\frac{B_{3r+1}}{p^2}\equiv\frac19\frac{B_{3r}}p\pmod p},
\qquad
\boxed{\frac{B_{4r+1}}{p^3}\equiv-\frac12\frac{B_{4r}}{p^2}\pmod p}.
\]

The valuation profile at the two edges is exactly (1,2) and (2,3) for the unweighted coefficients, and the displayed signed weights are p-units. These constants do not depend on p or on a choice of factorial representative.

**Proof.** The original exact coefficient ratio is
\[
\frac{b_{k+1}}{b_k}=\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}
=\frac{Q_{k+1}}{2(k+1)^3}.
\]
At k=3r, the unique numerator factor divisible by p is 2k+1=p. Hence
\[
\frac1p\frac{b_{3r+1}}{b_{3r}}
=\frac{(9r+1)(9r+2)}{36(3r+1)^3}
\equiv-\frac1{18}\pmod p,
\]
using r=-1/6 modulo p. At k=4r, the unique numerator factor divisible by p is 3k+2=2p. Hence
\[
\frac1p\frac{b_{4r+1}}{b_{4r}}
=\frac{2(8r+1)(12r+1)}{36(4r+1)^3}
\equiv\frac12\pmod p.
\]
Legendre's factorial valuation formula gives v_p(b_{3r})=1, v_p(b_{3r+1})=v_p(b_{4r})=2, and v_p(b_{4r+1})=3. The signed edge factors modulo p are respectively (6(3r)+1,6(3r+1)+1)=(-2,4) and (6(4r)+1,6(4r+1)+1)=(-3,3). Multiplying these ratios yields 1/9 and -1/2. QED.

## Green homogeneous propagation with exactly one incoming source unit

For 3r+1 <= k <=4r, define U_k=b_k/p^2 mod p; define L=b_{3r}/p mod p. For 3r+1 <= m <4r, set
\[
\rho_m=\frac{(2m+1)(3m+1)(3m+2)}{36(m+1)^3}\pmod p.
\]
All factors in the denominators are p-units and \rho_m is nonzero on this open interior. The entry theorem and the original ratio imply
\[
\boxed{U_k=-\frac{L}{18}\prod_{m=3r+1}^{k-1}\rho_m\pmod p}.
\]
In particular the prior high-band scalar H2 is exactly the directed finite Green transfer of the single *lower-band boundary source* L:
\[
\boxed{
\frac{H_2(p)}{p^2}\equiv-\frac{L}{18}
\sum_{k=3r+1}^{4r}(6k+1)
\prod_{m=3r+1}^{k-1}\rho_m\pmod p,
}
\]
where H2(p)=\sum_{k=3r+1}^{4r}B_k and an empty product is 1.

This is a source-preserving factorization: it separates the actual incoming p-adic factorial unit L from the finite, p-dependent signed response. It uses no high-band factorial evaluation after the entry unit is known. It is an equality of finite field expressions, not the unproved mother congruence.

To expose the *same* Gauss–Green operator as in the previously published finite Clausen defect, put V_k=2^kU_k=a_k/p^2 mod p. For every 3r+2 <= t <=4r,
\[
\boxed{t^3V_t-Q_tV_{t-1}=0\pmod p}.
\]
At the entry t=3r+1, division of the **exact** recurrence t^3a_t=Q_ta_{t-1} by p^2 gives the sourced boundary injection
\[
\boxed{t^3\,\frac{a_t}{p^2}
\equiv\frac{Q_t}{p}\,\frac{a_{t-1}}p\pmod p}.
\]
At the exit t=4r+1, division by p^3 similarly gives
\[
\boxed{t^3\,\frac{a_t}{p^3}
\equiv\frac{Q_t}{p}\,\frac{a_{t-1}}{p^2}\pmod p}.
\]
The terminal ratios are a_{3r+1}/p^2=-a_{3r}/(9p) mod p and a_{4r+1}/p^3=a_{4r}/p^2 mod p. Hence the H2 strip is a homogeneous sector of the *existing* Green recurrence with explicit, oriented p-adic transition ports at either end. This is a compositional reuse of the original Gauss/Green operator, not a new named operator.

## Exact computational certificate, scope and next unit

A Python-standard-library **independent source factorial-unit** check ran for all 148 primes p=6r+1, 7<=p<=2000; 22,952 high-band indices. It compared the entry, each recurrence term, signed endpoints, exit, and the independent previously proved p-j factorial H2 transport. All passed. The five exact (p, H2/p^2 mod p) witnesses were (7,5), (13,10), (19,9), (37,20), (373,266). The executable compact checker is \`research_notes/portable_direct/d25_green_boundary_transfer_compact_20261103.py\`; the extended executed test also exists as an author-side local artifact. No native 373 experiment is asserted.

**BRC carrier/observer:** preserve the original b factorial source, directed index k, valuation layer 1/2/3, incoming unit L, two oriented edge factors, homogeneous Green propagation and signed H2 observer. At fixed p, the H2 scalar determines the boundary unit L whenever the explicit transfer factor is nonzero; the 148-prime exact scan found no zero transfer factors, while a general nonvanishing proof remains open. If future operations require the directed interior terms, preserve L, p and the full Green propagation rather than the scalar alone. The new finite unit map is \`COMPOSE_APPLIED\` to existing Gauss Green and H2 source, under the precise mod p observer and finite p range. No P000 or ACTIVE worldview modification and no mathematical admission.

**Next smallest scientific unit:** solve or sharply characterize a p-dependent *adjoint/telescoping certificate* against the homogeneous recurrence t^3V_t-Q_tV_{t-1}=0, with the entry +1/9 and exit -1/2 signed port conditions and the prior Green signed-prefix forcing. Test proposed double-index certificate including all endpoint terms at p=13,19,373. Only then compare the complete fixed-parameter \(\Delta_p-R_p\) second carry; retain any nonzero remainder. The frozen mother objective remains
\[
W_p(1)=\sum_{k=0}^{p-1}(6k+1)b_k\equiv p\pmod{p^3},
\quad p\bmod24\in\{13,19\}.
\]

**Control state:** on the 2026-11-03 status read, native 0.6.11 still reports \`UPSTREAM_CODE_REVIEW_REQUIRED\`, \`research_authority_granted=false\`, \`executor_binding_configured=false\` and active quota 5/5. Recovery #6637 was verified as successful historical read-only recovery with no own live run/unopened claim/unpublished uploads; #6638 ended \`FAILED\` with upstream code review required. Neutral staging preserves original hashes; no new research CLAIM, OPEN, Source checkpoint, freeze, Result or review was attempted by this note. Control remediation remains the existing issue #1558, not a new competing owner.
