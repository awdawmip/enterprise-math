# D25/LIFT — exact second-digit Cauchy tail-reflection reduction

Date: 2026-10-28 Asia/Hong_Kong.
Logical Research lane: `chatgpt-research-onhour-enterprise-math-20260923`, strictly separate from `chatgpt-hourly-enterprise-math-20260921`.
Mother: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`.
Publication: `TP2-B6F4FC938FF94941C1B7`.
Scientific frozen Source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).

**Classification:** AUTHOR-SIDE / PROVED EXACT ALL-PRIME CONGRUENCE (R2) / 611 FINITE CHECKS OF SEPARATE CONJECTURE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_H0B0_NOT_EXECUTED.

## 1. Exact question and consumed prior work

The original, *unchanged* 216 sequence and weighted finite sum are

\[
t_k=\frac{\binom{2k}{k}^{2}\binom{3k}{k}}{216^k},\quad
b_j=\frac{\binom{2j}{j}}{8^j},\quad
W_N=\sum_{k=0}^N(6k+1)t_k.
\]

Let \(B_j=\sum_{i=0}^jb_i\). The earlier **proved rational finite identity** (`fb5040cf85bc10a53fe5ae65d9536f5b7048f805`) and the earlier **proved universal p² boundary** (`8aa179dfa916a231a1e6e7a44d813aadac9dd901`) are consumed here, not recredited:

\[
S_N=H_N-K_N,\qquad
H_N=\frac12\sum_{k=0}^N(6k+1)t_kB_{N-k},
\quad K_{p-1}\equiv\frac{3p}{2}\pmod{p^2}
\]
for primes \(p\equiv1\pmod6\). The analytic source is Roman Le Lan, *Series for 1/π arising from Cauchy product*, arXiv:2604.03327 (2026-04-02), Conjecture 1. The finite identity follows from a coefficientwise formal hypergeometric transformation, with cutoff and sign retained.

**New smallest unfinished unit selected:** compute \(H_{p-1}\) modulo \(p^2\) without carrying the full \(p\)-length cumulative \(B_{p-1-k}\) through the second-digit comparison. A claimed proof of Le Lan's mod-p² conjecture is *not* an input.

## 2. New exact universal theorem (R2)

For any prime \(p=6m+1>3\), put \(N=p-1\), \(B=B_N\), and

\[
u_s=\frac{8^s}{(2s+1)\binom{2s}{s}}\in\mathbb F_p\quad(0\le s<2m),\qquad
U_k=\sum_{s=0}^{k-1}u_s,
\]
\[
\mathcal T_p=
\sum_{k=0}^{2m}(6k+1)(t_k\bmod p)U_k
\in\mathbb F_p.
\]

The \(\binom{2s}{s}\) denominator is a \(p\)-unit in the stated range. **For every** prime \(p\equiv1\pmod6\),

\[
\boxed{
2H_{p-1}\equiv B_{p-1}W_{p-1}+p\mathcal T_p\pmod{p^2}.
}\tag{R2}
\]

This statement does **not** require the unproved Cauchy congruence, nor an assumption \(W\equiv p\), nor an original H0/B0 computation.

**Proof.** The original binomial factorial valuations at \(p=6m+1\), \(0\le k\le6m\), are

\[
v_p(t_k)=0\;(k\le2m),\quad
1\;(2m<k\le3m),\quad
\ge2\;(k>3m).
\]

Also \(v_p(b_j)=1\) for \(3m<j\le6m\). For \(k>3m\), the term \((6k+1)t_k(B_{N-k}-B_N)\) vanishes modulo \(p^2\) by the valuation of \(t_k\). For \(2m<k\le3m\), the difference is a sum of \(b_j\) with \(j\ge3m+1\), so it is divisible by \(p\); its product with \(t_k\) again vanishes modulo \(p^2\).

For \(0\le k\le2m\), set \(j=p-1-s\), \(0\le s<k\). The factorial-reflection identity (Wilson) gives, **with the sign retained**,

\[
\frac1p\binom{2(p-1-s)}{p-1-s}
\equiv-\frac{(s!)^2}{(2s+1)!}\pmod p,
\]
and Fermat's theorem gives \(8^{-(p-1-s)}\equiv8^s\pmod p\). Thus

\[
\frac{b_{p-1-s}}p\equiv-u_s\pmod p,\qquad
B_{N-k}-B_N=-\sum_{s=0}^{k-1}b_{p-1-s}
\equiv pU_k\pmod{p^2}.
\]

Insert this difference into the exact definition:

\[
2H_N-B_NW_N=
\sum_{k=0}^{N}(6k+1)t_k(B_{N-k}-B_N).
\]

Only \(0\le k\le2m\) remains modulo \(p^2\); its sum equals \(p\mathcal T_p\), proving (R2). **QED.**

As a separate elementary check, Euler's criterion plus \(b_j\equiv(-1)^j\binom{(p-1)/2}{j}2^{-j}\pmod p\) for \(j\le(p-1)/2\) shows

\[
B_{p-1}\equiv\chi_2:=\left(\frac2p\right)\pmod p.
\tag{B1}
\]

Thus when \(p\mid W_{p-1}\), (R2) and the previously proved boundary imply

\[
\boxed{
2S_{p-1}\equiv\chi_2 W_{p-1}
+p(\mathcal T_p-3)\pmod{p^2}.
}\tag{R2S}
\]

This is a precisely scoped, observer-preserving compression modulo \(p^2\); it does not dispose of the high-digit terms needed modulo \(p^3\).

## 3. Exact link to the two frozen target classes

For each of the two **separately retained** classes \(p\equiv13,19\pmod{24}\), \(\chi_2=-1\). Consume the frozen first-unit reciprocity/source arithmetic \(W_{p-1}\equiv p\pmod{p^2}\) in its exact previously established scope. Then (R2S) yields

\[
\boxed{
S_{p-1}\equiv\frac p2(\mathcal T_p-4)\pmod{p^2}.
}\tag{Target}
\]

Consequently the original Le Lan/Sun Cauchy conjecture \(S_{p-1}\equiv p\pmod{p^2}\) for these target classes is **equivalent** to the exact finite-field obligation

\[
\boxed{\mathcal T_p\stackrel{?}=6\quad\text{in }\mathbb F_p.}\tag{NEXT}
\]

This is a strict mathematical reduction of the previous unsolved H-congruence to one finite sum with indices \(k\le (p-1)/3\). The equality \(\mathcal T_p=6\) has not been universally proved; no new standalone proof of D25/LIFT follows. For the other primes \(p\equiv1\pmod6\) the empirical \(\chi_2=+1\) branch has \(\mathcal T_p=0\); this is a separate unproved class-dependent pattern.

## 4. Reproducible exact finite checks

Companion: `research_notes/portable_direct/d25_cauchy_tail_reflection_guard_20261028.py`. It was **executed locally** with Python 3.13.5 using standard-library integer arithmetic. All **611 primes** \(p<10000\) with \(p\equiv1\pmod6\) passed the proved reflection identity, the earlier boundary identity and the *distinct conjectural finite predictions*. For \(p\le73\) and \(p=373\), separate full integer-binomial coefficients, original \(B,W,H,K,S\), and the signed reflection coefficients were independently cross-checked. These 611 cases verify the implementation and provide finite evidence only, never a proof for all primes.

At \(p=373\), modulus \(139129\):

\[
\chi_2=-1,\qquad
(B,W,H,K,S,\mathcal T)=(51100,373,70497,70124,373,6).
\]

Here \(2H\equiv B W+p\mathcal T\pmod{139129}\), and the target relation gives \(S\equiv373\pmod{139129}\). At the split control prime \(p=7\), the exact certificate is \((\chi_2,B,W,H,K,S,\mathcal T)=(1,22,7,28,35,42,0)\) modulo 49. The distinct character branches cannot be merged into a single unsigned value.

Program output terminates with `PASS_AUTHOR_SIDE_TAIL_REFLECTION_P2_AND_FINITE_CONJECTURE_CHECKS`. No Lean checker was run, and this is not a native divided-power calculation.

## 5. BRC, identity/Source boundary, and continuation

BRC resolution: **COMPOSE_APPLIED** to the already defined finite Cauchy/carrier family. Population is every \(p\equiv1\pmod6\), with source target labels \(13\) and \(19\pmod{24}\) preserved. Retained carrier \((p,k,j=p-1-k,t_k,b_j,B_j,6k+1,2j+1)\) includes index, signed weights, factorial valuation and finite cutoff. The observer is \(S\bmod p^2\) with its source-bound \(W,H,K\) ports. The new \(\mathcal T_p\) is an **exactly certified mod-p² repair port**, *not* an assertion that the complete original joint relation can be discarded at higher precision or after further operators. The arithmetic variables are external scalar observers embedded in research about the native six-dimensional discrete Heartbeat World; they are not a native coordinate plane or a proof of full X6 transport. P000 and ACTIVE worldview remain unchanged.

Source/recovery status (separate from mathematical proof): read-only bridge receipts `research-onhour-20261027-0501-recovery-r13` and `research-onhour-20261027-0507-dispatch-r13` remain the exact historical own requests (#6575 and #6576 in `awdawmip/kimi-query-bridge`). The former records ACTIVE *local* session `MCP-de3e5bafb24f43f4a5e6285e7601676a` and `source_authority_verified=false`, with no winning own CLAIM/run; the latter ultimately reads `FAILED/TimeoutExpired`. Current Sites `em_status` / `em_sites_connection_status` at 2026-10-28 01:58–02:00 +0800 report `research_authority_granted=false`, static read-only Site scope, `active_jobs=5/5`, and the native backend control source sync review gate. No new request has been dispatched, no Source session/CLAIM/open is asserted, and no other logical lane identity is used. Earlier neutral staging stays attributed to its original session; preserved pointer is not admission.

**Highest unchanged experimental frontier:** `awdawmip/enterprise-math#1559` is an OPEN support/intake for an actual native original-class \(p=373\) H0/B0 divided-power benchmark: \([X]U\bmod139129\), rank, semilinear Frobenius direction/normalization \(\eta\), signed odd Green/Hesse, original \(\kappa\), and \(\Delta_p-R_p\). Its owner path is a legitimately authorized native Source researcher or designated implementation maintainer; at the observed issue snapshot no executor had accepted ownership. Neither this note nor the finite Cauchy checks completes that native gate.

**Next exact work:** (1) native responsible executor obtains and runs the fixed #1559 object with raw versioned reproducible evidence and canonical claim/Source permission; (2) mathematical portable continuation tests a WZ/Clausen/CM0 proof of \(\mathcal T_p=6\) separately for \(p\equiv13,19\pmod{24}\), or finds a genuine counterexample; (3) only authorized Research lane session may publish a Source checkpoint/Result after fresh exact continuation/claim authentication. Do not redo the prior K-boundary proof, D24 UR, CM0, E3 auxiliary identities or the 611-regression set by default.

This author-side proof remains **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING** until Source-authorized formal submission and independent review. Task D25/LIFT/JT2 stays OPEN. Research lane and maintenance lane are distinct, and schedule/notification settings are unchanged.
