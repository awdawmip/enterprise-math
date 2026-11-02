# D25: Cauchy–Gauss Euler-defect factorization for all carry moments

2026-11-02 · TASK_RESEARCH · AUTHOR-DERIVED / EXACT-PROVED (conditional scope as stated) / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Mother task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3. D25 still asks for the original signed 216 sum $S_p\equiv p\pmod{p^3}$ for $p\bmod24\in\{13,19\}$, equivalently $\Delta_p-R_p\equiv0\pmod p$. This note proves a separate modulo-$p^2$ Cauchy-carry dependency.

## Exact definitions and source

Let $p=6r+1\ge7$ be prime, $\theta=z\,d/dz$, and work in $\mathbb Z_{(p)}[z]$. Each sum below is truncated at $0\le k<p$:
\[
U_p=\sum_k\frac{(1/6)_k(1/3)_k}{(k!)^2}z^k,\quad
V_p=\sum_k\frac{(5/6)_k(2/3)_k}{(k!)^2}z^k,
\]
\[
F_p=\sum_k\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3}z^k,\quad
B_p=\sum_k\frac{(1/2)_k}{k!}z^k.
\]
Writing $f_m=[z^m]F_p$, $b_j=[z^j]B_p$, preserve the ordered original Cauchy pair and the omitted high-degree triangle:
\[
C_p(z)=\sum_{m+j<p}f_mb_jz^{m+j},\qquad
J_t(z)=\sum_{\substack{m,j<p\\m+j\ge p}}(m+j)^tf_mb_jz^{m+j}
=\theta^t(F_pB_p-C_p),\qquad t\ge0.
\]
At $z=1/2$, $f_m2^{-m}=A_m=\binom{2m}m^2\binom{3m}m/216^m$, $b_j2^{-j}=B_j=\binom{2j}j/8^j$ (the $B_j$ in earlier D25 Cauchy notes). Formal Clausen and Euler identities give $F_\infty=U_\infty^2$ and $V_\infty=(1-z)^{-1/2}U_\infty=B_\infty U_\infty$, hence $C_p=[z^{<p}](U_\infty V_\infty)$. The 216 Cauchy origin is also in 20261102_hourly_r11_d25_cauchy_truncation_carry.md, citing Roman Le Lan arXiv:2604.03327v2, Eq. (3.2). No p-adic conjecture from that paper is assumed.

## Theorem A: full polynomial truncations modulo p²

For $0\le k<p$, the p-valuations of coefficients of $U_p$ are exactly 0,1,2 on intervals $[0,r]$, $[r+1,2r]$, $[2r+1,p-1]$. For $V_p$ they are 0,1,2 on $[0,4r]$, $[4r+1,5r]$, $[5r+1,p-1]$. Indeed the respective linear Pochhammer factors first pick up $p$ at $r+1,2r+1$ and $4r+1,5r+1$; $k!$ is a p-unit and no factor accumulates a second multiple for $k<p$.

Every index pair $i+j\ge p$ in $U_p^2$ has total valuation $\ge2$: pairs with each valuation at most 1 have $i+j\le4r<p$. Every such pair in $U_pV_p$ also has valuation $\ge2$: its only possible total valuations below 2 require $i\le r,j\le5r$ or $i\le2r,j\le4r$, both implying $i+j\le6r=p-1$. Formal source identities supply the coefficients of degree $<p$. Therefore **as entire polynomials, including high-degree tails**:
\[
\boxed{F_p\equiv U_p^2,\qquad C_p\equiv U_pV_p\pmod{p^2}.}
\]
This is not an inference from a finite prime experiment.

## Theorem B: exact Euler defect and every carry moment

Modulo $p$, $B_p$ has degree $\le3r$, $U_p$ degree $\le r$, $V_p$ degree $\le4r$. The infinite Euler identity and their total degree $<p$ establish the coefficientwise congruence $B_pU_p\equiv V_p\pmod p$. Thus the **coefficientwise p-integral polynomial**
\[
E_p(z)=\frac{B_p(z)U_p(z)-V_p(z)}p\in\mathbb Z_{(p)}[z]
\]
is defined without a fitting parameter. Combining Theorem A,
\[
F_pB_p-C_p\equiv B_pU_p^2-U_pV_p
=U_p(B_pU_p-V_p)=pU_pE_p\pmod{p^2}.
\]
Applying the p-integral differential operator $\theta^t$ proves **for every integer $t\ge0$**:
\[
\boxed{J_t(z)\equiv p\,\theta^t\!\left(U_p(z)E_p(z)\right)\pmod{p^2}.}
\]
The operator acts on the original high-index triangle: no term is rewritten as a completed predecessor or dropped at an unapproved precision.

The existing Wilson reflection $B_{p-s}/p\equiv-1/(4sB_s)\pmod p$ for $1\le s\le2r$ and the original 216/central-binomial valuation strata imply for all $t$:
\[
J_t(1/2)\equiv pK_t\pmod{p^2},\qquad
K_t=-\sum_{m=1}^{2r}A_m\sum_{s=1}^{m}\frac{(m-s)^t}{4sB_s}\pmod p.
\]
Indeed only $m\le2r,\ j=p-s,\ 1\le s\le m$ contribute with valuation exactly 1; all other high-triangle pairs are p²-zero. Consequently
\[
\boxed{K_t\equiv[\theta^t(U_pE_p)](1/2)\pmod p \quad (t=0,1,2,\ldots).}
\]

## Theorem C (explicitly conditional): closure of K0 and K1's new exact obligation

If $U_p(1/2)\equiv0\pmod p$, then product differentiation gives
\[
\boxed{K_0\equiv0,\quad
K_1\equiv(\theta U_p)(1/2)E_p(1/2),\quad
K_2\equiv(\theta^2U_p)(1/2)E_p(1/2)+2(\theta U_p)(1/2)(\theta E_p)(1/2)\pmod p.}
\]
Thus the previous unproved finite observation $K_1\equiv-1/2\pmod p$ is *equivalent under the same CM-root hypothesis* to the sharply testable Gauss-jet/Euler-defect unit condition
\[
\boxed{(\theta U_p)(1/2)\ E_p(1/2)\equiv-1/2\pmod p.}
\]
The universal CM-root premise and this local unit remain open; no unconditional proof of either is claimed. The CM root has a concrete characteristic-p form:
\[
U_p(z)\equiv\sum_{k=0}^r\binom rk\binom{2r}k z^k\pmod p.
\]

**BRC observer safety.** At a simple root $U(z_0)=0$, replacing an *abstract input* defect $E$ by $E+\lambda(z-z_0)$ preserves $K_0,K_1$ but changes $K_2$ by $2\lambda z_0\theta U(z_0)$; hence the declared second-order observer requires an $E$-derivative repair port. This scoped witness does not assert that the actual hypergeometric $E_p$ varies freely. For modulo-p² Euler moments, the original signed weighted pair $(m,j)$ and its one-carry source factor through the **typed** polynomial pair $(U_p,E_p)$; no stronger p³ or native X6 statement is inferred.

## Independent exact arithmetic and continuation

The executable standard-library script d25_cauchy_gauss_defect_20261102.py and its actual d25_cauchy_gauss_defect_20261102.log accompany this note. Full-degree coefficientwise polynomial checks for p=7,13,19,31,37,43,61 pass. Across **all 207 primes** p=1 mod6, p≤3000, original Cauchy rectangle/omitted triangle, its independent Wilson-reflected K0/K1/K2 kernels and the Gauss/Euler-jet factorization pass in Z/p²Z. Among them **107 target primes** p mod24∈{13,19} pass finite CM-root and K0=0/K1=-1/2 checks. These finite observations are not universal proofs.

Sample residues $(U(1/2),\theta U(1/2),E_p(1/2),K_0,K_1,K_2)$ modulo $p$:
- p=13: (0,7,12,0,6,8);
- p=19: (0,1,9,0,9,16);
- p=373: (0,294,229,0,186,77), with $294\cdot229\equiv186=-1/2\bmod373$;
- p=1171: (0,544,649,0,585,260).

Next precise mathematical actions: prove/disprove the CM root uniformly for p mod24∈{13,19}, then establish or refute the local Gauss/Euler unit $(\theta U_p)E_p=-1/2\bmod p$ using a finite-field/character-sum or WZ certificate, not interpolation. Lift to the original signed p³ objective only with source-resolved higher-precision corrections.

Research logical lane: chatgpt-research-hourly-enterprise-math-20260923. Native Gateway 0.6.11 observed 2026-11-02: SOURCE CODE_REVIEW_REQUIRED, error UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false. Historic recovery #6637 has no own live claim/run; exact continuation #6638 failed and was not replayed. This is **neutral author-side evidence**, not a Source checkpoint, CLAIM, OPEN, Result, freeze, review or admission. The P000 axioms, ACTIVE worldview and scientific pin remain unchanged.
