# D25: sharp nonlocal-port bound in original-216 / E.2 transport

2026-11-06. Author-side TASK_RESEARCH mathematical theorem, PROVED / FINITE-VERIFIED / UNREVIEWED / NOT_ADMITTED. Task TP2-B6F4FC938FF94941C1B7, frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical lane chatgpt-research-onhour-enterprise-math-20260923, independent of maintenance conversation identity.

## Problem and theorem

For any prime \(p=6m+1>3\), put

\[
a_n=\frac{(2n)!(3n)!}{216^n(n!)^5},\quad
w_n=(6n+1)a_n,\quad
b_n=(-1)^n\left(\frac{(1/3)_n}{n!}\right)^3,\quad
v_n=(6n+1)b_n\quad(0\le n<p).
\]

The frozen scalar question is \(W_p:=\sum_{n<p}w_n\equiv V_p:=\sum_{n<p}v_n\pmod{p^3}\), in the target classes \(p\equiv13,19\pmod{24}\). The already proven original-216 three-shell and E.2 Franel two-jet are consumed (commits eec361046d7677ee6b53bf85786af97e616e325d and a953484013a1c1297f006b86a721869fab29f6ef).

**Theorem (specific finite transport class).** Let \(C=(C_{nk})\) with \(C_{nk}\in\mathbb Z_{(p)}\), and suppose the **homogeneous, coefficientwise** transport
\[
w_n\equiv\sum_{k=0}^{p-1}C_{nk}v_k\pmod{p^3}
\qquad(0\le n<p)
\]
holds. Each target row with \(2m<n\le4m\) must receive a nonzero contribution modulo \(p^3\) from some low-index source \(k\le2m\). Consequently at least \(2m\) low-to-high cross-port entries are needed; if \(C_{nk}=0\) for \(|n-k|>B\), then
\[
\boxed{B\ge2m=(p-1)/3.}
\]
In particular no prime-independent fixed bandwidth yields a p-integral homogeneous termwise transport uniformly over the frozen target classes. This is **not** a statement about general WZ identities admitting nonlocal or boundary sources.

**Proof.** For \(n<p\), Legendre's factorial-valuation formula gives
\[
\nu_p(a_n)=\left\lfloor\frac{2n}{p}\right\rfloor+
\left\lfloor\frac{3n}{p}\right\rfloor=
\begin{cases}
0,&0\le n\le2m,\\
1,&2m<n\le3m,\\
2,&3m<n\le4m,\\
3,&4m<n<p.
\end{cases}
\]
For \(n>2m\), the factor \((1/3)_n\) contains **exactly one** \(p/3\), at index \(j=2m\), and \(n!\) is a p-unit. Also \(6n+1\) is a p-unit throughout this upper band; its only p-divisible index below \(p\) is \(n=m\). Thus \(\nu_p(v_n)=3\) for all \(n>2m\), whereas \(\nu_p(w_n)=1\) or \(2\) for \(2m<n\le4m\). Any row in that band generated solely from \(k>2m\) would vanish mod \(p^3\), contradicting the original coefficient. Each row requires its own cross-port entry. At \(n=4m\), any contributing \(k\le2m\) has \(|n-k|\ge2m\). QED.

**Sharpness only for abstract support geometry.** Since \(v_{2m}\) is a p-unit, the matrix choosing \(C_{nn}=a_n/b_n\) for \(n\le2m\), \(C_{n,2m}=w_n/v_{2m}\) for \(2m<n\le4m\), and zero otherwise, attains exactly \(2m\) cross-entries and maximal displacement \(2m\). The upper rows \(n>4m\) vanish mod \(p^3\). This uses the very original coefficients \(w_n\) in its definition and **does not prove the scalar equality** or construct a nontrivial WZ transformation.

## BRC, exact arithmetic, discriminating next step

BRC = COMPOSE_APPLIED: typed carrier \((\mathrm{family},n,\nu_p,\mathrm{signed\ unit},\mathrm{cutoff},p\text{-digit})\), observer coefficientwise mod \(p^3\), permitted future operations p-integral linear transports. The E.2 tail observer erases the original nonzero p-adic middle and gap shells; **the quantified lost port** gives an exact factorization obstruction for *bounded local homogeneous* transforms. This is external hypergeometric arithmetic, not a native six-dimensional coordinate claim.

The Python standard-library checker published with this report performed **91,956** index/valuation/tail checks on all **148** primes \(7\le p\le1999,\ p\equiv1\pmod6\), including **77** target primes: **zero failures**. Individual last-gap coefficients satisfy \(w_{4m}/p^2\equiv13\pmod{19}\) and \(203\pmod{373}\). Previous independently proven full *aggregate* valuation-two shells remain \(3249=9\cdot19^2\) and \(37008314=266\cdot373^2\); the single-coefficient and aggregate witnesses are different observables.

As a finite class-selectivity control, exact weighted full-sum evaluation of all 301 primes \(5\le p\le1999\) found 148 primes \(p\equiv1\pmod6\) with \((W_p,V_p)\equiv(p,p)\pmod{p^3}\) and 153 primes \(p\equiv5\pmod6\) with \((W_p,V_p)\equiv(-p,-2p)\pmod{p^3}\). These remain finite observations, not universal theorems. Already at \(p=5\), \(W_5=120,\ V_5=115\pmod{125}\): a residue-class-blind equality is false. External E.2 citation: Guo–Schlosser (2023), https://doi.org/10.1007/s00025-023-01885-8.

**Next genuine scalar proof unit:** seek a nonlocal finite adjoint/Clausen/creative-telescoping transform with reach \(\ge(p-1)/3\), or explicit signed boundary/source flux, that relates the *complete* original valuation-two shell to the E.2 Franel jets and proves \(W_p-V_p=0\pmod{p^3}\) on the frozen target. Keep \(p=19,373\) nonzero aggregate-shell tests.

**Native experiment:** fixed p373 original-class H0/B0 divided-power [X]U mod139129, true rank, semilinear Frobenius/eta, signed odd Hesse/Green, kappa/Delta−R, and independent replica are **NOT_EXECUTED / PENDING_OWNER**, tracked in https://github.com/awdawmip/enterprise-math/issues/1559. This portable proof is not a substitute.

**Source status:** gateway v0.6.11 reports research_authority_granted=false; no own session/claim/open/run/Result. Last verified native-client checkpoint revision 22 / SERVER_SQLITE_COMMITTED. Original continuation request onhour11-20261106-1400-exact-research-lane-continuation read WAITING_RESOURCE/EVENT_COLLECTION_IO then same-ID reconcile QUEUED. Additional exact read request onhour12-20261106-1957-read-continuation was QUEUED; no ownership follows from it. Three old staged items remain distinct and unadmitted. This GitHub note is author-side durable evidence only.
