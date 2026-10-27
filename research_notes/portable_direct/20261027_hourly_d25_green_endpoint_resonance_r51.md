# D25/LIFT R51 — Exact prime resonances of the two-endpoint Green observer

2026-10-27, Asia/Hong_Kong. Portable TASK_RESEARCH author proof. Logical lane chatgpt-research-hourly-enterprise-math-20260923; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; D25/LIFT/JT2 parent OPEN. Frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Classification AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Original sources and exact observer

Reuse the rational factorial terms and the R47/R50 second-order recurrence, without modifying their provenance:

$$
w_k=\frac{(6k+1)(2k)!(3k)!}{(k!)^5 216^k},\qquad
s_k=\frac{(8k+1)(4k)!}{(k!)^4 2304^k},\qquad d_k=w_k-s_k.
$$

Let \(a_k=w_{k+1}/w_k,\ b_k=s_{k+1}/s_k,\ a_0=7/18,\ b_0=3/32\). R47 provides

$$
a_k-b_k=\frac{(2k+1)P(k)}{288(k+1)^3(6k+1)(8k+1)},\quad
P(x)=2688x^4+6160x^3+4456x^2+1166x+85.
$$

Choose only the R50 Green observer \(c_1=1\), with all other weights zero. For \(p\ge13,\ p\equiv1\pmod6\) prime and \(N=\lfloor(3p-1)/4\rfloor+1\), its coefficients satisfy
\(d_1=-C_Nd_N-C_{N+1}d_{N+1}\) and \(d_1=85/288\).
This is an arithmetic rank observer with two retained W/S source labels, not a native X6 spatial coordinate.

## Theorem R51: three and only three stronger prime poles

For every such target prime, the unique rational Green coefficients for this observer satisfy

$$
\boxed{\min\{v_p(C_N),v_p(C_{N+1})\}=
\begin{cases}
-4,&p\in\{139,199,277\},\\
-3,&\text{all other target primes}.
\end{cases}}
$$

For each of the three exceptional primes, both coefficients have valuation exactly \(-4\). For each other target prime, both have valuation at least \(-3\), and at least one has valuation exactly \(-3\).

**Proof.** Each of \(w,s\) solves R47's homogeneous rank-two recurrence. Apply the finite Green identity to each separately. Since
\(D_N=w_Ns_{N+1}-s_Nw_{N+1}=w_Ns_N(b_N-a_N)\ne0\)
over \(\mathbb Q\), the two Green coefficients are uniquely given by Cramer's rule:

$$
\boxed{C_N=\frac{-a_0s_{N+1}+b_0w_{N+1}}{D_N},\qquad
C_{N+1}=\frac{a_0s_N-b_0w_N}{D_N}.}\tag{R51-C}
$$

For \(p\equiv1\pmod4\), \(N=(3p+1)/4\); otherwise \(N=(3p+3)/4\). Legendre's formula and the actual unit linear weights give
\(v_p(w_N)=v_p(s_N)=v_p(w_{N+1})=v_p(s_{N+1})=3\).
Indeed \(N,N+1<p\), the factorial \(2k\) contributes one factor of \(p\), \(3k\) two, and \(4k\) three, for both \(k=N,N+1\). The original 6k+1 and 8k+1 weights at both endpoints are p-units for all target \(p\ge13\). Every rational denominator in the displayed formula for \(a_N-b_N\) is likewise a p-unit. Thus

$$ v_p(D_N)=6+v_p(P(N)). $$

The exact endpoint congruences are

$$
P(N)\equiv P(1/4)=3047/4=(11\cdot277)/4\pmod p,\quad p\equiv1\pmod4,
$$
$$
P(N)\equiv P(3/4)=27661/4=(139\cdot199)/4\pmod p,\quad p\equiv3\pmod4.
$$

The factor 11 lies outside \(p\equiv1\pmod6\). All remaining exceptional factors 139,199,277 are primes in this class. For these three, the exact values of \(P(N)/p\pmod p\) are respectively 108,106,78, all nonzero. Consequently \(v_p(P(N))=1\) at precisely these three primes and zero for all other target primes.

For a nonexceptional p, both numerators of (R51-C) have valuation at least 3. If both had valuation at least 4, write \(U=w_N/p^3,\ V=s_N/p^3\) and reduce their equations modulo p. The second gives \(b_0U=a_0V\); after substitution the first gives \(a_0(b_N-a_N)V=0\). Since each factor is a unit, this is impossible. At least one numerator therefore has valuation 3, proving the \(-3\) minimum.

For the three exceptional primes, exact p-free factorial calculation yields:

| p | N | P(N)/p mod p | w_N/p³ mod p | s_N/p³ mod p | (b₀w_N-a₀s_N)/p³ mod p |
|---:|---:|---:|---:|---:|---:|
| 139 | 105 | 108 | 66 | 105 | 3 |
| 199 | 150 | 106 | 138 | 68 | 162 |
| 277 | 208 | 78 | 251 | 224 | 224 |

The last entries are all nonzero. Since \(a_N=b_N\pmod p\) and this common residue is a unit, both Cramer numerators have valuation exactly 3. Meanwhile the denominator has valuation 7, so each coefficient has valuation \(-4\). QED.

## Corollary: exact loss of one p-adic precision digit

Put \(\varepsilon_p=1\) for p=139,199,277, and 0 otherwise. If two endpoint inputs are independently approximated but the exact coefficients \(C_N,C_{N+1}\) are retained, a uniform worst-case-sharp sufficient absolute precision for recovering \(d_1\bmod p^t\) is

$$ \boxed{d_N,d_{N+1}\pmod {p^{t+3+\varepsilon_p}}.} $$

Equivalently, normalized endpoint inputs \(d_N/p^3,d_{N+1}/p^3\) need precision \(p^{t+\varepsilon_p}\). Thus the mod-p³ observer needs original endpoints through p⁶ ordinarily, and p⁷ at the three resonant primes. Sharpness here means independent endpoint perturbations, not that original factorial trajectories can vary freely.

## Author checks, BRC typing and continuation

The companion Python standard-library exact script checks all 44 primes \(13\le p\le500,\ p\equiv1\pmod6\): every Cramer identity, factorial valuation, difference polynomial, Green coefficient pole and the three exceptional unit certificates. Executed result: PASS. Generality follows from the proof, not the finite test.

BRC COMPOSE_APPLIED to the typed signed two-source arithmetic carrier; preserves integer rank, W/S provenance, p-adic valuation and the declared endpoint observer. The extra resonance digit is a precision/residual fact, not a new Heartbeat World spatial dimension. P000, ACTIVE worldview and original six Hasse labels are untouched.

Do not recredit R47 source recovery, R48 high-high valuations, R49 finite-window exception or R50 Green existence. Next mathematical unit: insert R23's original low-half p²-divided W/S discrepancy into R50 and R36 PF Green observations, along with R38–R42 high-rank source transfers, preserving R51's exceptional precision. Look for a genuinely unchanged-input additive WZ telescoper at p=13,19,181,373; retain finite and positive-infinity boundaries. H0/B0, [X]U mod p², Frobenius eta/kappa, native p=373 experiment and independent Driver review remain OPEN.

No current winning CLAIM/open/native checkpoint has been read back for this lane. This GitHub proof is portable author evidence only. Preserve predecessor session, staging and original requests; control repair is tracked by Enterprise Math Issue #1558. Research-Activity event awaits its own lawful registration/readback.
