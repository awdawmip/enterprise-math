# D25/LIFT — cubic Fermat–harmonic reduction of the original ONE-CARRY CM/DP target

2026-10-24 | TASK_RESEARCH portable author-side proof and executed exact-integer regression | **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. This is not a Source run/checkpoint/Result, an independent review or a native benchmark.

**Scope and provenance.** Mother objective **RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT**, historical publication **TP2-B6F4FC938FF94941C1B7**, frozen scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** (unchanged). Research logical lane **chatgpt-research-onhour-enterprise-math-20260923** is distinct from maintenance **chatgpt-hourly-enterprise-math-20260921**. The exact original n-telescoper, two exceptional contributions, terminal, ONE-CARRY p³ jet, and its unproved CM/DP-BRIDGE were established earlier at **12ea426dd6796ce9492f3e550f2065f2565eb1f1**; the dual-path original 575-prime test at **c6ba00a05c04ef0bbf1fae4a2ec4a4df4aa06ca0** is consumed, not recredited. The other research lane's WZ old-edge/FIVE work remains separately attributed. This note solves a previously open exact *normalization subunit*, not the entire prime-only hard target.

## 1. Frozen source and explicit predecessor lemma

Let \(p=6m+1\) be prime, \(m\ge1\). Preserve the exact original source
\[
A_m=\frac{(6m)!}{3^{6m}((2m)!)^3},\quad R_{m,0}=1,\quad
\frac{R_{m,n+1}}{R_{m,n}}=
\frac{(4m+2n+1)(3n+1)(3n+2)}
{36(n+1)(2m+n+1)(4m+n+1)},\quad
S_m=A_m\sum_{n=0}^{4m}(6n+12m+1)R_{m,n}.
\]
Set
\[
G_p=\frac{4^{p-1}((2m)!)^3}{(p-1)!},\quad
U_p=\frac{R_{m,2m}}p,\quad
H_s=\sum_{j=1}^{s}\frac1j,\quad q_p(a)=\frac{a^{p-1}-1}{p}.
\]
All the displayed normalized units belong to \(\mathbb Z_{(p)}^\times\). The preceding, already proved ONE-CARRY identity is
\[
\frac{S_m}{pA_m}\equiv \mathcal L_p+U_p(1+p\eta_p)\pmod{p^2},
\qquad
\eta_p=\frac{19}{9}-\frac23H_{2m-1}-\frac13q_p(6),
\tag{OC}
\]
where the *unchanged regular part* is
\[
\begin{aligned}
\mathcal L_p&=\sum_{n=0}^{m}b_n K_0(n)[1+p(D_n+L_n)]\\
&\quad+p\sum_{\substack{m<n<4m\\ n\ne 2m}}K_0(n)u_n,\\
b_n&=(-1)^n\binom mn 2^{-n},\quad
K_0(n)=\frac{(1-3n)(6n+3)}{(3n+1)(3n+2)},\quad
u_n=R_{m,n}/p,\\
D_n&=\sum_{j=0}^{n-1}\left[\frac1{2(j-m)}-\frac1{3j+2}-\frac2{3j+1}\right],\\
L_n&=\frac2{1-3n}+\frac2{6n+3}-\frac1{3n+2}-\frac2{3n+1}.
\end{aligned}
\tag{REG}
\]
The original hard target is \(\frac{S_m}{pA_m}\stackrel?{\equiv}G_p\pmod{p^2}\), because \(A_m\) is a p-unit. Unlike an all-integer-rank identity, this targets **only prime p** in the frozen mod-24 classes.

## 2. New theorem A — exact rational one-carry/target ratio

**Theorem A.** For every integer \(m\ge1\), setting \(p=6m+1\) without assuming primality, the following identity holds *exactly over \(\mathbb Q\)*:
\[
\boxed{\displaystyle
\frac{U_p}{G_p}=
\frac{1}{2m\,24^{p-1}}
\prod_{a=1}^{2m-1}\left(1+\frac pa\right)
\prod_{a=1}^{2m}\left(1-\frac pa\right)^2.}
\tag{A}
\]
For the prime case, all product denominators are p-units; therefore
\[
\boxed{\displaystyle
\frac{U_p}{G_p}\equiv
\frac1{2m}\Big(1-p[H_{2m-1}+\frac1m+q_p(24)]\Big)
\pmod{p^2}.}
\tag{A2}
\]

**Proof.** The original, exact factorial formula at \(n=2m\), cancelling its single p-factor, gives
\[
U_p=\frac{(8m)!}{p\,216^{2m}((4m)!)^2}
=\frac{(p-1)!(2m-1)!}{216^{2m}((4m)!)^2}
\prod_{a=1}^{2m-1}\left(1+\frac pa\right).
\]
The second equality follows by splitting \(\prod_{j=p}^{p+2m-1}j\), extracting p, and rewriting the remaining factors. Since \(p=6m+1\) and \(2m\) is even, the exact factorial reflection
\[
(p-1)!=(4m)!(2m)!\prod_{a=1}^{2m}\left(1-\frac pa\right)
\]
holds (with positive sign). Divide the preceding formula by \(G_p=4^{p-1}((2m)!)^3/(p-1)!\), cancel \((4m)!\) and \((2m)!\), and use \(216^{2m}=6^{p-1}\). This proves (A). The first-order product expansions and \(24^{p-1}=1+pq_p(24)\) yield (A2). No p-divisible quantity is inverted.

## 3. New theorem B — cubic-root-of-unity harmonic evaluation

**Theorem B.** For every prime \(p=6m+1\),
\[
\boxed{\displaystyle H_{2m}\equiv-\frac32q_p(3)\pmod p.}\tag{B}
\]

**Self-contained proof.** Work in \(\mathbb Z[\omega]\), where \(\omega^2+\omega+1=0\) and \(\omega\ne1\). Then \((1-\omega)^2=-3\omega\). Since \((p-1)/2=3m\) and \(\omega^{3m}=1\),
\[
(1-\omega)^{p-1}=(-3)^{(p-1)/2}=1+pt
\]
for an integer \(t\), because \((-3/p)=1\) for primes \(p\equiv1\pmod6\). Expand
\((1-\omega)^p-(1-\omega)=pt(1-\omega)\) binomially in the ring modulo \(p^2\). The elementary congruence
\(\binom pk\equiv p(-1)^{k-1}/k\pmod{p^2}\) for \(1\le k\le p-1\) implies
\[
\sum_{k=1}^{p-1}\frac{\omega^k}{k}\equiv -t(1-\omega)\pmod p.
\]
Put \(S_a=\sum_{1\le k<p,\ k\equiv a\!\!\pmod3}1/k\).
Using \(\omega^2=-1-\omega\), compare coefficients of \(1,\omega\) in the free basis of \(\mathbb F_p[\omega]\): \(S_0-S_2=-t,\ S_1-S_2=t\). Also \(S_0+S_1+S_2=H_{p-1}=0\pmod p\). As \(p\ne3\), this gives \(S_1=t\). But the elements \(k\equiv1\pmod3\) are precisely \(k=p-3j\), \(j=1,\ldots,2m\), hence \(S_1=-H_{2m}/3\), or \(H_{2m}=-3t\). Finally \([(-3)^{(p-1)/2}]^2=3^{p-1}\) gives \(q_p(3)=2t\pmod p\). Combine the two equalities. QED.

## 4. New theorem C — explicit elimination of the exceptional carry from the target

Define the *target complement* \(C_p=G_p-U_p(1+p\eta_p)\). Then for **every prime** \(p=6m+1\),
\[
\boxed{\displaystyle
C_p\equiv G_p\left[
4+p\left(\frac{37}{3}-10q_p(2)+\frac72q_p(3)\right)
\right]\pmod{p^2}.}
\tag{C}
\]

**Proof.** From (A2), put \(B=H_{2m-1}+1/m+q_p(24)\). Then
\[
\frac{C_p}{G_p}\equiv 1-\frac1{2m}[1+p(\eta_p-B)]\pmod{p^2}.
\]
Use the *integer equality* \(2m=(p-1)/3\), so \(1/(2m)=3/(p-1)\equiv-3(1+p)\pmod{p^2}\). The result is
\[
\frac{C_p}{G_p}\equiv4+p\left[
\frac{82}{3}-5H_{2m-1}-q_p(6)-3q_p(24)
\right]\pmod{p^2}.
\]
The elementary Fermat-quotient multiplication rule gives
\(q_p(6)\equiv q_p(2)+q_p(3)\), \(q_p(24)\equiv3q_p(2)+q_p(3)\pmod p\).
Meanwhile (B) and \(1/(2m)\equiv-3\pmod p\) yield
\(H_{2m-1}\equiv3-\frac32q_p(3)\pmod p\).
Substitution gives precisely (C). This is a proved p²-scoped mathematical normalization, not a fit to numeric data.

### Precisely remaining original-prime criterion

Combining (OC), (C), and the p-unit status of \(A_m\) yields this **proved equivalence**:
\[
\boxed{\displaystyle
S_m\stackrel?{\equiv}p(4/3)^{p-1}\pmod{p^3}
\quad\Longleftrightarrow\quad
\mathcal L_p\stackrel?{\equiv}
G_p\left[
4+p\left(\frac{37}{3}-10q_p(2)+\frac72q_p(3)\right)
\right]\pmod{p^2}.}
\tag{CM/DP-REGULAR-ONLY}
\]
The question marks matter: **the right-hand prime-family congruence remains UNPROVED.** The exact special \(n=2m\), \(n=4m\), original terminal, and their valuations were conserved in (OC), (A)–(C); they have only been contracted for this named scalar output/precision observer. No native-X6 evolution/physical bridge is asserted.

The necessary first digit is
\(\sum_{n=0}^m b_nK_0(n)\stackrel?{\equiv}4G_p\pmod p\).
This separate congruence was observed in the regression but is not established for infinitely many primes. The next mathematical unit is a prime-dependent cubic-character/Jacobi or finite WZ proof for that exact first digit followed by the regular \(p\)-digit jet with both original HIGH branches.

## 5. Reproducibility, BRC and source truth

The companion standard-library checker **20261024_onhour_d25_cubic_fermat_one_carry_target_bridge_check.py** was executed locally: exact (A) checked with Python Fraction at **m=1,...,9**, and two arithmetic routes (original factorial p-factor stripping versus the independent product) confirmed (A2), (B), and (C) for **207/207 primes \(p\le3000,\ p\equiv1\pmod6\)**. It also separately recorded the **FINITE OBSERVATION ONLY** first-digit equality at 207/207, without promoting it to a proof. Witnesses \((p,m,G_p\bmod p^2,U_p\bmod p^2,\Xi_p\bmod p,C_p\bmod p^2)\): (7,1,27,38,4,31), (13,2,151,28,6,45), (19,3,141,280,1,355), (37,6,1248,511,16,441), (211,35,37915,11378,181,28858). These checks are author-side and are not the frozen native benchmark.

**BRC COMPOSE_APPLIED / REUSE_APPLIED:** carrier retains labeled source n-position, p-adic valuation/unit, LOW regular two-jet, both HIGH branches, exact exceptional product (A), and original terminal seam; output observer is the original signed endpoint modulo \(p^3\). Compression to \(\mathcal L_p\) uses an exact scalar identity at that precision only, not an assertion that discarded ports are equal under other observations. P000 and ACTIVE residual-faithful discrete worldview remain unchanged.

**Recovery frontier.** Highest previous immutable input: 12ea426dd6796ce9492f3e550f2065f2565eb1f1 original ONE-CARRY; newest new claims (A), (B), (C) and equivalent (CM/DP-REGULAR-ONLY), subject to independent review. Parent hard target **OPEN**. **Unfinished**: first digit and full regular second digit for *all target primes*, original same-class CM/divided-power normalization, Source-fixed unmodified native benchmark (NOT RUN / executor unverified), formal Source session/claim/run/checkpoint/Result, independent Driver review. Next precise action: prove or falsify the regular congruence (preferably via a cubic-character/Jacobi evaluation of \(\sum b_nK_0(n)\)); do not repeat previously completed HIGH/LOW lemmas or widen to composite q (known obstruction). Native recovery support **enterprise-math#1539** was previously open. Current site transport read reports no Researcher write authority; no old unknown request was replayed; no maintenance identity borrowed. No session_id, claim_id, run_id or new formal request receipt was obtained. Original research schedule, notifications and frozen scientific pin are not modified.
