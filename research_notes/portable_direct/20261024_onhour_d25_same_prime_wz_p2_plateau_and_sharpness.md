# D25/LIFT — same-prime WZ first-digit transport, second-digit plateau, sharpness

**2026-10-24, TASK_RESEARCH author-side exact proof. UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.** Not an authorized Source checkpoint, native benchmark, formal Result or independent review. Parent RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Author's logical Research lane: chatgpt-research-onhour-enterprise-math-20260923, **not** the maintenance lane chatgpt-hourly-enterprise-math-20260921.

**Inherited exact WZ source:** c7fb90fd7ec451a954b553b963dd85d4ec99fc96:research_notes/portable_direct/20261024_onhour_d25_original_endpoint_all_m_wz_five_tail.md. The present theorems use its original term, quartic polynomial and exact all-rank WZ identity; they do not re-credit or alter them.

For integer \(r,n\ge0\), define
\[
A_r=\frac{(6r)!}{3^{6r}((2r)!)^3},\quad R_{r,0}=1,\quad
\frac{R_{r,n+1}}{R_{r,n}}=
\frac{(4r+2n+1)(3n+1)(3n+2)}{36(n+1)(2r+n+1)(4r+n+1)},
\]
\[
T_{r,n}=A_r(6n+12r+1)R_{r,n},\quad S_r=\sum_{n=0}^{4r}T_{r,n}.
\tag{1}
\]
The immutable WZ certificate has an explicit integer quartic \(P(r,n)\) and
\[
g(r,n)=\frac{4nP(r,n)}{9(n+2r+1)(n+4r+1)(n+4r+2)(n+4r+3)(6n+12r+1)}.
\]
It proves the **exact rational** moving-terminal equality
\[
\boxed{S_{k+1}-S_k=T_{k,4k+1}g(k,4k+1)+\sum_{j=1}^4T_{k+1,4k+j}.}
\tag{2}
\]
All five labelled terms are kept.

## Theorem A — a same-prime upper-half first-digit transport

For **every prime** \(p=6m+1\) and every integer \(\lceil m/2\rceil\le k\le m-1\),
\[
\boxed{S_{k+1}\equiv S_k\pmod p,\qquad S_m\equiv S_{\lceil m/2\rceil}\pmod p.}\tag{A}
\]
The prime \(p\) stays FIXED while the auxiliary rank \(k\) varies.

**Proof.** From (1),
\[
R_{r,n}=\prod_{j=0}^{n-1}\frac{(4r+2j+1)(3j+1)(3j+2)}
{36(j+1)(2r+j+1)(4r+j+1)}.\tag{3}
\]
At \((r,n)=(k,4k+1)\) and all \((r,n)=(k+1,4k+s),1\le s\le4\), the numerator includes **two** factors \(p\), one at \(j=2m\) from \(3j+1=p\), another at \(j=3m-2r\) from \(4r+2j+1=p\). Both indices belong to the respective \([0,n-1]\), even if they coincide. The prefactor \(A_r\) is a \(p\)-unit because \(r\le m\). Factors \(j+1\le4m<p\) and \(2r+j+1\le6m=p-1\) in the denominators are \(p\)-units. The final denominator family \(4r+j+1\) begins below \(p\) and ends at most \(8k+8\le8m<2p\); **at most one** factor is divisible by \(p\). Thus all five *unweighted* \(T\)'s have valuation at least 1.

At \(n=4k+1\), the denominator factors of \(g\), apart from the unit 9, are
\[
6k+2,\;8k+2,\;8k+3,\;8k+4,\;36k+7.\tag{4}
\]
The first, second and fourth are even and less than \(2p\), hence \(p\)-units. The last is \(1\bmod6\), strictly between \(3p\) and \(6p\), so cannot equal \(4p\) or \(5p\). The only possible \(p\)-denominator is \(8k+3=p\). At this exceptional resonance the *old* boundary has \(4k+n=8k+1=p-2\), hence no \(p\)-denominator and **two** uncancelled \(p\)-numerators. It absorbs the possible one-factor denominator of \(g\). All five terms in (2) belong to \(p\mathbb Z_{(p)}\), proving (A). QED.

## Theorem B — refined second-digit plateau

For the same primes, if
\[
\boxed{\left\lceil\frac m2\right\rceil\le k\le\left\lfloor\frac{3m-4}{4}\right\rfloor,}\tag{5}
\]
then every individual one of the five WZ terms in (2) belongs to \(p^2\mathbb Z_{(p)}\); therefore
\[
\boxed{S_{k+1}\equiv S_k\pmod{p^2}.}\tag{B}
\]
**Proof.** (5) implies \(8k+8\le6m=p-1\). Every denominator factor in both original recurrence streams is then strictly below \(p\). The two numerator \(p\)-factors identified above survive, giving \(v_p(T)\ge2\) for all five terms. The first four denominators of \(g\) in (4) are below \(p\). The fifth satisfies \(3p<36k+7<5p\), with residue 1 modulo 6, whereas its only candidate multiple \(4p\) has residue 4. Hence \(g\) is \(p\)-integral. Apply (2). QED.

Consequently the five-component **third-digit** carrier
\[
c_{p,k}=p^{-2}\left[T_{k,4k+1}g(k,4k+1)+\sum_{j=1}^4T_{k+1,4k+j}\right]\bmod p
\]
is defined on interval (5), and \((S_b-S_a)/p^2\equiv\sum_{k=a}^{b-1}c_{p,k}\pmod p\) for ranks in the plateau. The nonzero third digit is an essential BRC observer and cannot be thrown away to claim the original mod-\(p^3\) target.

## Precise sharpness and executed checks

At the prescribed-class prime \(p=37,m=6\), plateau (5) consists of \(k=3\):
\[
S_3\equiv45214,\quad S_4\equiv43845\pmod{37^3},\quad
\boxed{S_4-S_3\equiv36\cdot37^2\pmod{37^3},\ v_{37}=2.}
\]
All five normalized \(p^{-2}\) terms are \((8,8,20,19,18)\bmod37\), summing to 36. Thus no unconditional \(p^3\) plateau follows. Immediately **outside** it at \(k=4\):
\[
S_4\equiv37,\quad S_5\equiv740\pmod{37^2},\quad
\boxed{S_5-S_4\equiv19\cdot37\pmod{37^2},\ v_{37}=1.}
\]
This also refutes extending the \(p^2\)-stationary interval by one rank in general; neither witness refutes the frozen original LIFT conjecture.

At \(p=211,m=35\), the eight \(p^2\)-stationary rank changes \(k=18,\dots,25\) have exact ordered normalized digits
\((109,148,89,22,3,49,191,116)\), summing to \(94\bmod211\). Independently \(S_{18}\equiv2938597,\ S_{26}\equiv7123571\bmod211^3\), so \((S_{26}-S_{18})/211^2\equiv94\pmod{211}\). This is fixed-prime transport, not a proof for \(S_{35}\).

**Author-side exact verification:** The accompanying executable reconstructs the original rational product with signed \(p\)-valuations and modular \(p\)-unit factors, keeping the five WZ pieces distinct and checking the original \(S\)-difference modulo \(p^3\). Among primes \(p\le1000\), \(p\equiv1\bmod6\), it passed **3,027** upper-half transitions in **79** primes; **1,471** of them satisfy Theorem B in **76** primes; the other **1,556** satisfy Theorem A. The \(p=37\) witnesses were independently checked by exact Fraction arithmetic. Finite checks are not the universal proof: the all-prime factor argument above is.

**BRC: COMPOSE_APPLIED / REUSE_APPLIED.** Typed fixed prime, rank, integer numerator factors, valuations and five-source provenance; keep \(p,p^2,p^3\) readouts distinct. No native X6/Heartbeat result is inferred. P000 ACTIVE_LOCKED.

**Current execution boundary:** Gateway 0.6.11 Sites identity reports research_authority_granted=false. Exact continuation request em-r-onhour-t11-continuation-read-20261024 returned CONTROL_QUOTA; its receipt lookup returned CONTROL_REQUEST_NOT_FOUND. No valid Researcher session, winning CLAIM, open/run, formal checkpoint/Result or review was obtained. Existing support issue awdawmip/enterprise-math#1539 remains the owner path; historical #6186/#6187/#6188 were not reissued, nor any maintenance lane borrowed. Three older staged UR sources remain independent of the accepted D24 Result.

**Highest new author frontier:** Theorems A and B, the full five-term third-digit transport, exact sharpness counterexamples. **Unfinished mother target:** prove or refute original \(S_m\equiv p(4/3)^{p-1}\pmod{p^3}\) on prescribed prime classes, complete CM/divided-power same-class comparison and unchanged native benchmark, with proper Source admission. **Next smallest unit:** for \(k>\lfloor(3m-4)/4\rfloor\), track the unique \(p\)-denominator in the late tail and possible resonance \(8k+3=p\); derive a compensated normalized \((S_{k+1}-S_k)/p\bmod p\) creative-telescoping certificate to connect the early plateau to terminal rank \(m\). Do not repeat inherited WZ, completed LOW/HIGH or accepted D24.