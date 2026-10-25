# D25/LIFT — all middle Hasse cutoff ports at one additional p-adic digit

Date: 2026-10-25. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Research conversation chatgpt-research-hourly-enterprise-math-20260923, not the maintenance lane. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 retained.

**Status:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY, with no claim to a new native Source checkpoint, CM experiment, independent check, full-X6 theorem, or all-target-prime supercongruence.

## Research increment beyond the previous fourth-jet note

The existing all-Hasse theorem proves that the cutoff source over F_p is supported only at derivative orders 2, p+1 and 2p. The subsequent third-jet p² work and the prior immediate fourth-jet p² note determined two individual previously vanishing ports. **This note gives one closed formula for *every* intermediate Hasse forcing order 3 through p, at precision p²**, leaving higher characteristic-p surviving ports separately typed.

Let p=6m+1>=7 be prime, N=p-1. In the p-integral rational polynomial model, define

\[
\Phi(x,z)=\sum_{r=0}^{p-1}\frac{(-x)_r(-2x)_r}{(r!)^2}z^r,\quad
\theta=z\,d/dz,\quad
\mathcal L_x=\theta^2-z(\theta-x)(\theta-2x).
\]

Its **exact** cutoff forcing is \(\mathcal L_x\Phi=-F_p(x)z^p\), where
\[
F_p(x)=(-x)_p(-2x)_p/((p-1)!)^2.
\]
Set \(J_{k,p}=-[t^k]F_p(m+t)\) (the boundary forcing of the *full* parameter-dependent operator equation). Write \(H_a^{(q)}=\sum_{j=1}^a j^{-q}\in\mathbb Z_{(p)}\).

**All-middle-port theorem:** for every integer \(1\le n\le p-2\),

\[
\boxed{
J_{n+2,p}\equiv
2\left[
\frac{1+2^n}{n}H_{p-1}^{(n)}
-(-1)^n p\left(H_m^{(n+1)}+2^nH_{2m}^{(n+1)}\right)
\right]\pmod{p^2}.
}\tag{A}
\]

Every right-hand side is divisible by p. Thus each characteristic-p *invisible* intermediate Hasse port has a completely determined first p-adic leakage and can be normalized by p. At z=1/2 the corresponding forcing is \(J_{n+2,p}2^{-p}\equiv J_{n+2,p}/2\pmod{p^2}\) **only after** the proven p-divisibility. No theta derivatives are discarded before point observation.

The formula's n=1 row reproduces the already published third-jet p² fact, using Wolstenholme \(H_{p-1}\equiv0\pmod{p^2}\); n=2 reproduces the preceding fourth-jet identity \(J_{4,p}=5H_{p-1}^{(2)}-2p(H_m^{(3)}+4H_{2m}^{(3)})\). These are **consumed checks, not re-credited novelty**. The genuinely new quantified interval is n=3,...,p-2, the whole remaining middle hierarchy.

## Proof by normalized product and Newton identity

The Pochhammer factors vanish exactly once each at x=m. Factor
\[
F_p(m+t)=A_pt^2 G(t),\quad A_p\in\mathbb Z_{(p)}^\times,\quad A_p\equiv2\pmod p,
\]
with
\[
G(t)=\prod_{\substack{-m\le h\le p-1-m\\h\ne0}}(1-t/h)
\prod_{\substack{-2m\le h\le p-1-2m\\h\ne0}}(1-2t/h).
\]
All denominators h and all indices n below are units mod p². Write \(G(t)=1+\sum_{n\ge1}g_nt^n\) and
\[
S_n=\sum_{\substack{-m\le h\le p-1-m\\h\ne0}}h^{-n}
+2^n\sum_{\substack{-2m\le h\le p-1-2m\\h\ne0}}h^{-n}.
\]

The previously proved exact finite-field Frobenius factorization yields
\[
F_p(m+t)\equiv2(t^p-t)^2\pmod p,\qquad
G(t)\equiv(1-t^{p-1})^2\pmod p.
\]
Hence \(g_n\equiv0\pmod p\) for all \(1\le n\le p-2\). The formal logarithmic derivative of G, equivalently the standard Newton identity for elementary symmetric polynomials, gives
\[
ng_n=-\sum_{j=1}^n S_jg_{n-j},\quad g_0=1.
\]
Induction mod p shows \(S_n\equiv0\pmod p\) throughout the same range. In the identity mod p², all terms with \(j<n\) therefore contain a product of two p-multiples and vanish, so
\[
ng_n\equiv-S_n\pmod{p^2},\qquad
J_{n+2,p}=-A_pg_n\equiv\frac{2S_n}{n}\pmod{p^2}. \tag{B}
\]

For any \(1\le n\le p-2\), reflecting the final k terms of a harmonic sum gives
\[
H_{p-1-k}^{(n)}+(-1)^nH_k^{(n)}
\equiv H_{p-1}^{(n)}-(-1)^n n p\,H_k^{(n+1)}
\pmod{p^2}.
\]
Apply this once with k=m and once with k=2m, multiplying the second by \(2^n\):
\[
S_n\equiv (1+2^n)H_{p-1}^{(n)}
-(-1)^n n p(H_m^{(n+1)}+2^nH_{2m}^{(n+1)})
\pmod{p^2}.
\]
Substitute into (B) to obtain (A). The elementary finite-field power-sum relation shows \(H_{p-1}^{(n)}\equiv0\pmod p\) in precisely the stated range, confirming the valuation. QED.

The range stops at n=p-2 on purpose: at n=p-1 the normalized product has its first nonzero mod-p coefficient and the linear p² truncation is no longer valid. The original high Hasse ports p+1 and 2p remain as separately conserved sources.

## Exact computational certificate

The adjacent pure-Python checker directly builds *all* coefficients \(g_1,\ldots,g_{p-2}\) from the integer-local-factor product modulo \(p^2\), derives each power sum \(S_n\) independently by iterating modular inverses, and checks both the harmonic-complement expression and equation (A). It performs the complete interval for **all 35 primes p≡1 (mod6), 7≤p≤373**, plus first 12 intermediate orders each for p=1327 and p=19963, giving **6,115 checked (p,order) pairs**, all PASS. Finite checks illustrate and cross-validate; the general theorem follows from the algebra above.

## BRC/Research/frontier semantics

The intermediate Hasse vector may be compressed to zero **only at mod-p observer precision**, not at mod-p² with subsequent source-sensitive composition. Preserve signed terminal cutoff, Hasse order, p-valuation, rank p-1, 2^{-p} readout and specific source algebra until the next allowed quotient. This is an external finite-polynomial observer model; no unspecified mapping to the native six-dimensional Heartbeat World or a crystalline CM module is asserted.

Old SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED D25 checkpoint, claim/contributor history and true original-class next_action remain intact. No source continuation_prepare, CLAIM, OPEN, checkpoint, review, freeze or session_close is performed by publishing this portable note. The prior CONTROL predecessor/claim mismatch remains for the existing Issue #1558 maintenance path; D25/LIFT/JT2 mother objective remains OPEN.

**Next smallest scientific step:** compare the explicitly sourced full middle-jet vector (including ranks beyond four) against the genuinely corrected Clausen denominator/directional source at the *same* rank and signed observer. Test whether a rankwise telescoping identity exists before inferring the all-target-prime statement. Exact original-class H0/B0, [X]U mod p², Frobenius direction/eta and kappa remain required, and native CM experiment remains NOT_RUN.
