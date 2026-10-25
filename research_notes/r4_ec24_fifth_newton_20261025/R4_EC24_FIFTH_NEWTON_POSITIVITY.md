# R4-EC24 — Fifth-highest Newton coefficient: all-grade positivity

Date 2026-10-25. **Status: author-side exact symbolic proof, exact integer independent cross-check, no independent Driver review or native mathematical admission.**

## Fixed scope and source pins

GLOBAL_KNOWLEDGE_V1 main@3eb70ebb18d1593932f92ad3cbb5c88db052c82f; canonical startup/manual, EM TASK routing, P000 and ACTIVE worldview consulted. P000 original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matches startup projection. EM main baseline@c7bc883339bf4ad5693cbd652ff4a0f92514d328; current docs/PORTABLE_RESEARCH_PROTOCOL.md. Reused exact R4-EC23 predecessor: commit 3f331906a1b2fa68aa0787685051a4382d0ce5d5. GitHub actor awdawmip. Native owner query: CONTROL_QUOTA. Native session creation: STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Own author-side activity: RA-EMR4-20261025-2129-EC24FIFTH.

Only the **positive ordered binary affine auxiliary BRC clean-source kernel** is studied. There is no P000 X6, native three-dimensional slice, physics or heartbeat-time calculation. Native attribution remains pending.

## Theorem

Use the established exact series and Newton transform:

\[
E(x,u)=\frac{1-ux^2}{1-(1+u)x+2u^2x^4-u^3x^6},
\quad f_j(n)=[x^nu^j]E-[x^nu^{j-1}]E.
\]

\[
q_d(j)=\Delta^{j-d} f_j(2j+6)=[z^jt^d]\,H(z,t),\quad j\ge d\ge0,
\]

\[
H(z,t)=\frac{(1+t)^6(1-tz)(1-t(1+t)^2z)}
{1-(1+t)^2z+2t(1+t)z^2-t^2(1+t)z^3}.
\]

**For every integer c >= 4 and r in {0,1,2}, with d=3c+r, the fifth-highest monomial coefficient is strictly positive:**

\[
\boxed{[w^{c-4}]q_{3c+r}(3c+r+w)=K_r(c)/(c-4)!>0.}
\]

Let v=c-4>=0. The following lists give all integer coefficients in **descending degree order** of the exact numerator polynomial for K_r(v+4). Divide by the listed positive denominator.

* r=0, denominator 59875200, degree 12:

512, 52224, 2278144, 55925760, 859210176, 8740714752, 61096664992, 300865255680, 1051252030037, 2550829768674, 4057622275239, 3758453971650, 1487060467200.

* r=1, denominator 389188800, degree 13:

512, 59904, 3043456, 88573056, 1645740096, 20680875072, 182331631768, 1156175760168, 5337603511097, 17837089490649, 41933028620301, 65337904132371, 59694556519710, 23418268473600.

* r=2, denominator 2724321600, degree 14:

512, 68096, 3983616, 135466240, 2989338352, 45387630288, 491902888048, 3901000383280, 22970833500615, 100660578649631, 323999694536336, 741712955860695, 1134715553029521, 1023922580886450, 399045006360000.

All **42 numerator integers** and all three denominators are strictly positive. Thus K_r(c)>0 for all integers c>=4, without a finite-degree cutoff. Together with EC21–EC23, this proves positivity of the top five monomial coefficients in the applicable grades. It does **not** prove positivity of all Newton coefficients or full source-kernel unimodality.

## Exact finite symbolic derivation

Put y=1-z, and define

\[
\begin{aligned}
N_0&=(1+t)^6(1-t)(1-t(1+t)^2),\\
N_1&=(1+t)^6[t(1-t(1+t)^2)+t(1+t)^2(1-t)],\\
N_2&=t^2(1+t)^8,\\
Q_0&=1-2t,\ Q_1=2t-t^2,\ Q_2=t^2.
\end{aligned}
\]

Direct algebra gives the formal identity

\[
H(1-y,t)=\sum_{k\ge0}\frac{t^{3k}(1-y)^{3k}(N_0+yN_1+y^2N_2)}
{y^{k+1}(Q_0+yQ_1+y^2Q_2)^{k+1}}. \tag{1}
\]

For h=0,...,4, define

\[
R_h(c,r)=\sum_{\ell=0}^h[t^{r+3\ell}y^{h-\ell}]
\frac{(1-y)^{3(c-\ell)}(N_0+yN_1+y^2N_2)}
{(Q_0+yQ_1+y^2Q_2)^{c-\ell+1}}. \tag{2}
\]

Formula (2) is **finite**: the maximum t-degree is 14. For explicit rational-polynomial evaluation, set k=c-ell, p=k+1, and enumerate a=0,1,2 and i,s_1,s_2>=0 with a+i+s_1+2s_2=h-ell; sum

\[
\frac{(-1)^{i+s_1+s_2}(3k)_{\underline i}(p)_{s_1+s_2}}
{i!s_1!s_2!}
[t^{r+3\ell}]N_aQ_1^{s_1}Q_2^{s_2}(1-2t)^{-p-s_1-s_2}. \tag{3}
\]

The final coefficient comes from [t^m](1-2t)^{-p}=2^m(p)_m/m!, so each R_h is exact over Q[c], not an interpolation conjecture.

The previously established and independently reproduced integer recurrence yields [t^d]H=P_d(z)/(1-z)^{c+1}, with deg P_d <= d+c-1. The polynomial part of this fraction has z-degree at most d-2 and hence contributes zero to [z^{d+w}] for w>=0. Thus

\[
q_d(d+w)=\sum_{h=0}^{c}R_h(c,r)\binom{d+w+c-h}{c-h}. \tag{4}
\]

For h>=5 the summand has w-degree <=c-5. Writing e_m for the m-th elementary symmetric polynomial (e_0=1), the fifth-highest coefficient in (4) gives exactly

\[
\boxed{K_r(c)=\sum_{h=0}^{4}R_h(c,r)
\frac{e_{4-h}(d+1,\ldots,d+c-h)}{(c-h)_{\underline{4-h}}}.} \tag{5}
\]

Compute e_1,...,e_4 by the standard exact Newton relations
k e_k = sum_{i=1}^k (-1)^{i-1} e_{k-i} S_i,
where S_i=sum_{j=1}^{c-h}(d+j)^i. Substitute (2),(3) in (5), cancel rational functions, set c=v+4. The result is precisely the three numerator lists above. The companion code reproduces all coefficients symbolically, with exact rational arithmetic. Their strict positivity completes the proof for all c>=4.

## Independent exact integer check

For a=floor(d/3), put h_d(z)=[t^d]H(z,t)=P_d(z)/(1-z)^{a+1}. Multiply H by its defining denominator to obtain, with negative-index terms absent and binomial coefficients zero outside their usual range,

\[
\begin{aligned}
P_d(z)={}&(1-z)^a\{\binom6d-z(\binom6{d-1}+\binom8{d-1})+z^2\binom8{d-2}\}\\
&+2z(1-z)^{a-\lfloor(d-1)/3\rfloor}P_{d-1}(z)\\
&+z(1-z)^{a+1-\lfloor(d-2)/3\rfloor}P_{d-2}(z)
+z^3P_{d-3}(z). \tag{6}
\end{aligned}
\]

Then q_d(d+w)=sum_i [z^i]P_d(z) binom(d+w-i+a,a). The executable verifier reconstructs [w^{c-4}] from c+1 exact integer values using finite differences and signed Stirling numbers, independently of the Laurent-coefficient algorithm and the displayed numerator lists. All **63 cases**, c=4..24 and r=0,1,2, passed exact equality. For c=4 the values are **24836, 60172, 146475** for r=0,1,2. Archive extraction, fresh execution and byte-equal report regeneration also passed; these finite checks are separate from the universal algebraic proof.

## Research outcome and next question

Reuse decision: REUSE_APPLIED to the established BRC auxiliary kernel, EC21 pole order and EC23 finite Laurent extraction; no new BRC family or hidden native bridge asserted. The complete locally executed script, its full structured report and cold-start evidence are included in the downloadable author-side evidence ZIP. The same mathematical certificate is persisted in this research note.

EC25 should attempt the sixth-highest coefficient [w^{c-5}]q_{3c+r}(3c+r+w), c>=5, and search for an order-uniform positivity invariant. Still open are all low Newton coefficients, f_j(2j+s)>=0 for s=0..5, the fixed-transition six/seven-state control problem and X6 correspondence. No independent Driver review or formal Result/admission was performed.
