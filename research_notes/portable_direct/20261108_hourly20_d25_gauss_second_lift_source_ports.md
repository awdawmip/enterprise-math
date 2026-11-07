# D25 — Exact Gauss second-lift source ports through modulo p^3

Date: 2026-11-08 (Asia/Hong_Kong). Role: TASK_RESEARCH author-side portable mathematics, REGISTER_PENDING, UNREVIEWED / NOT_ADMITTED. Lane: chatgpt-research-hourly-enterprise-math-20260923. Maintenance lane chatgpt-hourly-enterprise-math-20260921 is excluded.

Immutable research parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3. D24 accepted UR/JT0 first digit remains accepted. The actual second-digit LIFT \(\Delta_p-R_p=0\) for \(p\equiv13,19\pmod{24}\) remains OPEN. This note supplies an exact source-retaining Gauss expansion, not the full LIFT.

## Theorem — full three-stratum second-order p-adic Gauss expansion (proved)

Let \(p>3\) be prime, \(0\le u<v\le p-2\), \(\lambda,\mu\in\mathbb Z_{(p)}\), and put
\[
G_p(z)=\sum_{n=0}^{p-1}\frac{(-u+\lambda p)_n(-v+\mu p)_n}{(n!)^2}z^n,\qquad
Q(z)=\sum_{n=0}^{u}\binom un\binom vn z^n.
\]
All identities below are coefficientwise in \(\mathbb Z_{(p)}[z]/p^3\), with indices \(n<p\), so every stated denominator is a \(p\)-unit. Define the low stratum \(0\le n\le u\), single-zero stratum \(u<n\le v\), double-zero stratum \(v<n<p\). Write \(A_n=\sum_{j=0}^{n-1}(j-u)^{-1}\), \(B_n=\sum_{j=0}^{n-1}(j-v)^{-1}\), \(A_n^{(2)}=\sum(j-u)^{-2}\), \(B_n^{(2)}=\sum(j-v)^{-2}\) **only on the low stratum**, where they have no singular terms.

On the low stratum set \(q_n=\binom un\binom vn\),
\(l_n=q_n(\lambda A_n+\mu B_n)\), and
\[
s_{0,n}=\frac{q_n}{2}\left[(\lambda A_n+\mu B_n)^2-\lambda^2 A_n^{(2)}-\mu^2 B_n^{(2)}\right].
\]
On the single-zero stratum set
\[
t_n=\lambda\,\frac{(-1)^{u+n}u!(n-u-1)!\,v!}{(v-n)!(n!)^2},\quad
s_{1,n}=t_n\left[\lambda\sum_{\substack{0\le j<n\\j\ne u}}(j-u)^{-1}
+\mu\sum_{j=0}^{n-1}(j-v)^{-1}\right].
\]
On the double-zero stratum set
\[
s_{2,n}=\lambda\mu\,\frac{(-1)^{u+v}u!(n-u-1)!\,v!(n-v-1)!}{(n!)^2}.
\]
Every coefficient not belonging to a formula's stratum is zero. Then
\[
\boxed{G_p(z)=Q(z)+p\big(L(z)+T(z)\big)+p^2\big(S_0(z)+S_1(z)+S_2(z)\big)\pmod{p^3},}
\]
where \(L=\sum_{n\le u}l_nz^n,\ T=\sum_{u<n\le v}t_nz^n,\ S_i=\sum_ns_{i,n}z^n\).

**Proof.** For \(n\le u\), neither base Pochhammer factor vanishes. Logarithmically expand each of the two products to second order in \(p\), yielding \(q_n,l_n,s_{0,n}\). For \(u<n\le v\), the first Pochhammer product has exactly one zero factor \(j=u\), and the second has none: extract \(\lambda p\) and expand the remaining nonzero factors to first order, yielding \(pt_n+p^2s_{1,n}\). For \(v<n<p\), both products have exactly one zero factor: extract \(\lambda\mu p^2\), and their zeroth-order remaining product is \(s_{2,n}\). No coefficient of order \(<p^3\) remains beyond these strata. This is a complete finite-product argument independent of tested primes.

At an \(x\in\mathbb Z_{(p)}\) where \(Q(x)\equiv0\pmod p\), the *actual* Gauss lift satisfies the sharper source-aware identity
\[
\boxed{\frac{G_p(x)}p
\equiv\frac{Q(x)+pL(x)+pT(x)}p
+p\big(S_0(x)+S_1(x)+S_2(x)\big)
\pmod{p^2}.}
\]
The first quotient is well-defined, but it has its own second digit, so one must not discard it when reading the three new ports.

## Specialization and exact check

A (216): \(u=m=(p-1)/6,\ v=2m,\ (\lambda,\mu)=(1/6,1/3),\ x=1/2\). B3 (2304, \(p\equiv19\bmod24\)): \(u=k=(p-3)/8,\ v=3k+1\); B5 (2304 Euler, \(p\equiv13\bmod24\)): \(u=k=(p-5)/8,\ v=3k+1\). Both B classes use \((\lambda,\mu)=(1/8,3/8)\), \(x=1/9\), but must retain the original Euler source label.

An independent exact integer-modular checker evaluates every raw Gauss coefficient by *actual* \((1/6,1/3)\), \((1/8,3/8)\), or \((5/8,7/8)\) recurrence modulo \(p^3\), then compares it with the theorem's factorial/harmonic three strata. For all 94 primes \(p<2500\) in the two frozen residue classes and both A/B models, **214148 out of 214148 coefficients passed** (188 model runs), including the evaluated CM point. No floating point and no test of the original native H0/B0 is asserted.

Distinct source-port witnesses, with \(S_0,S_1,S_2\) understood modulo \(p\), are:
 
| prime/model | \(G_p(x)/p\bmod p^2\) | \(Q(x)/p\bmod p\) | \(L,T\bmod p\) | \(S_0,S_1,S_2\bmod p\) |
|---|---:|---:|---:|---:|
| 19/A | 84 | 6 | 6,15 | 3,18,10 |
| 19/B3 | 28 | 10 | 11,7 | 0,4,4 |
| 373/A | 65672 | 340 | 352,78 | 197,212,252 |
| 373/B5 | 36167 | 326 | 41,365 | 239,222,308 |

At \(p=373\), the sum of the A-side second-order ports is \(288\), whereas the B5-side sum is \(23\) modulo \(373\). This difference is a source-resolved *component*, not a claimed nonzero global LIFT residual. It cannot be cancelled or proved irrelevant until the actual Fricke/Cartier coefficient and Euler normalization are carried to the same precision.

## Small second result — second-digit gauge/lift dependence (proved)

Let first-digit coefficients \(t,r\in\mathbb F_p\) satisfy \(tg_A-rg_B=0\) where \(g_A=(G_A/p)\bmod p\), \(g_B=(G_B/p)\bmod p\). For arbitrary integer representatives \(\tilde t,\tilde r\) and any \(a,b\in\mathbb F_p\), replacing these by \(\tilde t+pa,\tilde r+pb\) changes the divided second-digit residual
\[
\frac{\tilde t(G_A/p)-\tilde r(G_B/p)}{p}\pmod p
\]
by **exactly** \(a\,g_A-b\,g_B\pmod p\). Proof: subtract the two numerators and divide by \(p\). For \(p=373\), the already source-verified first lifts are \(g_A=24,g_B=359\); a change \(\tilde t\mapsto\tilde t+373\) shifts this residual by \(24\). Thus a purported second-digit Fricke identity using only \(t,r\bmod p\) is not canonically defined; the next proof must specify geometric/p-adic lifts of its signed Fricke coefficients. This is a **representation/observer requirement**, not a counterexample to the canonical target.

BRC reuse: COMPOSE_APPLIED to the existing signed two-branch Fricke observer plus the previously proved q/L/T first lift and p³ Clausen/Euler sources. Carrier retains A/B3/B5, integer lift, low/single-/double-zero ports, Euler source, signed Frobenius branch and the chosen coefficients; collapsing to a scalar mod \(p\) loses the exact future divided operator. No new P000 axiom or accepted BRC theorem is asserted.

## Next executable problem and evidence boundary

Compute from the actual Fricke/CM transformation **canonical mod-\(p^2\) lifts** of the coefficients \(t,r\) and the signed eigenvector, including B5's Euler factor. Apply these fixed lifts to the above \(Q,L,T,S_0,S_1,S_2\) decomposition at \(p=19,373\); establish an identity with the already-published low-Gauss/Cartier/short-overflow ports \(\Gamma_p+E_A-E_B\), then seek a general isogeny/Cartier proof. Do not pick \(t,r\) second digits to force cancellation, or mistake the 373 external Gauss check for native benchmark #1559.

Latest native research lane original requests: em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13. On this run, both read-only receipts were WAITING_RESOURCE/EVENT_COLLECTION_IO, then each permitted reconcile of its **same request** returned QUEUED, not success or a claim. Old service session/claim/run/upload state remains UNKNOWN_PRESERVE, and no native checkpoint or review was made. Existing recovery owner: Enterprise Math issue #1558; native p373 issue #1559.