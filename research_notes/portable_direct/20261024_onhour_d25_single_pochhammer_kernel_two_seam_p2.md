# D25/LIFT — One Pochhammer carrier for both regular high sectors and both original seams, through p²

2026-10-24 | TASK_RESEARCH / portable original rational mathematics | **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NOT A SOURCE CHECKPOINT**.

Mother: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. The **frozen scientific Source pin remains** c47e13e4aba0e006366f989d6334d443f6333ae3. Logical provenance: \`chatgpt-research-onhour-enterprise-math-20260923\`, separate from both maintenance and another hourly Research lane. Account-level knowledge read: verified \`main@1a5c1a6d2833f3441c46eba5c5d01427b3e299ca\`, GLOBAL_KNOWLEDGE_V1; P000 projection and canonical blob matched, ACTIVE_LOCKED. Project control and frozen science are distinct pins.

**Source debts:** no current authenticated Researcher writer, own Source claim/run/checkpoint/Result, independent review, or original native benchmark. Historical own bridge issues #6186/#6187/#6188 were read without replay (#6188 FAILED/TimeoutExpired). Support #1539 remains OPEN; the read-only Sites connection reports \`research_authority_granted=false\`. This is independent author evidence, not a formal continuation/claim.

## Consumed science and unchanged target

Use the **original**, previously established recurrence and exact Gosper two-seam scalar:

\[
R_0=1,\quad \frac{R_{n+1}}{R_n}
=\frac{(6n+1+2p)(3n+1)(3n+2)}
{12(n+1)(3n+2+p)(3n+1+2p)},\qquad p=6m+1 \text{ prime}.
\]
\[
k_n=\frac{(1-3n)(6n+3)}{(3n+1)(3n+2)},\quad
K_{p,n}=\frac{(2p+1-3n)(6n+2p+3)}
{(3n+p+2)(3n+2p+1)}.
\]
\[
\mathcal K_p=
\sum_{\substack{0\le n<4m\\n\ne 2m}}K_{p,n}R_n+
\alpha_p R_{2m}/p+\beta_p R_{4m}/p,\qquad
\alpha_p=\frac{(p+2)(4p+1)}{3(2p+1)},\quad \beta_p=3-2p.
\]

The true still-open LIFT endpoint is \(\mathcal K_p\equiv G_m\pmod{p^2}\), where \(G_m=(-1)^m((2m)!)^3/((3m)!)^2\). Earlier author derivations proved the equivalence of this divided endpoint and the original unaltered EP target. The two seams and the original terminal are **inside** \(\alpha,\beta\), not dispensable. The previously published LOW-JET and two high factorial sectors are reused here, not re-proved or claimed anew.

## Theorem A — exact global deformation and exceptional jumps

Define the **single** terminating-prefix hypergeometric carrier by
\[
c_0=1,\quad c_{n+1}=\frac{6n+1}{12(n+1)}c_n
=\frac{(1/6)_{n+1}}{2^{n+1}(n+1)!},\quad 0\le n<4m.
\]
Then \(v_p(c_n)=0\) for \(0\le n\le m\) and \(v_p(c_n)=1\) for \(m<n\le4m\). Define p-integral rationals
\[
u_j=\begin{cases}
-\dfrac1{3m+2}-\dfrac2{3m+1},&j=m,\\[2mm]
\dfrac2{12m+1}-\dfrac1{6m+2},&j=2m,\\[2mm]
\dfrac2{6j+1}-\dfrac1{3j+2}-\dfrac2{3j+1},&j\notin\{m,2m\},
\end{cases}
\qquad U_n=\sum_{j=0}^{n-1}u_j.
\]
All denominators of \(u_j\) for \(0\le j<4m\) are p-units, including the substituted exceptional values. Put \(\lambda_n=3\) if \(m<n\le2m\), otherwise \(\lambda_n=1\). **For every target prime and every \(0\le n\le4m\):**
\[
\boxed{\frac{R_n}{c_n}\equiv\lambda_n(1+pU_n)\pmod{p^2}.}\tag{MASTER-RATIO}
\]

**Proof.** Divide the given recurrence by the recurrence for \(c\), obtaining the *exact* factor
\[
\frac{R_{j+1}/R_j}{c_{j+1}/c_j}
=\frac{6j+1+2p}{6j+1}
 \frac{3j+2}{3j+2+p}
 \frac{3j+1}{3j+1+2p}.
\]
For ordinary \(j\), expand its three p-unit factors as \(1+pu_j\bmod p^2\). At \(j=m\), the first factor equals **exactly 3**, and the two remaining factors give \(1+pu_m\); at \(j=2m\), the last factor equals **exactly 1/3**, and the others give \(1+pu_{2m}\). No \(j=4m\) transition occurs before the original endpoint. Multiplying the finite factors proves MASTER-RATIO. There is precisely one numerator p-factor in \(c_{m+1},\ldots,c_{4m}\), with no p-factor in their denominators: the valuation statement and all modular divisions are justified. QED.

In particular the formerly exceptional jump follows **automatically**:
\[
\frac{R_{2m+1}}{R_{2m}}\equiv
\frac13\frac{c_{2m+1}}{c_{2m}}
\equiv-\frac1{24}\pmod p.
\]
This bridges the two prior high heads without conflating their labels.

## Theorem B — complete original divided sum becomes one kernel, both seams retained

For \(0\le n\le m\), let
\[
d_n=\frac2{1-3n}+\frac2{6n+3}-\frac1{3n+2}-\frac2{3n+1},
\qquad
L_m^\ast=\sum_{n=0}^m c_nk_n(U_n+d_n).
\]
Define a **single coefficient sequence on the full original index range**
\[
w_{m,n}=1+2\,\mathbf1_{\{m<n<2m\}}+\mathbf1_{\{n=4m\}},
\quad
M_m^\ast=\sum_{n=0}^{4m}w_{m,n}c_nk_n.
\]
At \(n=2m\) and \(n=4m\), \(k_n\) alone has p-valuation \(-1\), but \(c_nk_n\) is a **p-integral unit**. These are legitimate retained seam terms, not forbidden p-inversions. Define
\[
E_m^\ast=\frac{c_{2m}}p(4+2U_{2m})+
          \frac{c_{4m}}p(6+3U_{4m})\in\mathbb Z_{(p)}.
\]

**For all target primes** the entire original two-seam scalar satisfies the exact p²-precision congruence
\[
\boxed{\mathcal K_p\equiv M_m^\ast+p(L_m^\ast+E_m^\ast)\pmod{p^2}.}\tag{WHOLE-KERNEL}
\]
In particular \(M_m^\ast-G_m\in p\mathbb Z_{(p)}\), and the *still-open* LIFT is rigorously equivalent to **one finite obstruction**
\[
\boxed{\mathcal K_p\equiv G_m\pmod{p^2}
\iff
\frac{M_m^\ast-G_m}{p}+L_m^\ast+E_m^\ast
\equiv0\pmod p.}\tag{ONE-OBSTRUCTION}
\]
This is a new target-preserving identity, **not** a proof that the obstruction vanishes.

**Proof, including both seam coefficients.** On the low range \(n\le m\), direct expansion of the given \(K_{p,n}\) gives \(K_{p,n}\equiv k_n(1+pd_n)\bmod p^2\). MASTER-RATIO yields
\[
K_{p,n}R_n\equiv c_nk_n[1+p(U_n+d_n)]\pmod{p^2}.
\]
On the two ordinary high ranges \(m<n<2m\) and \(2m<n<4m\), \(c_n\) has p-valuation 1, \(K_{p,n}\equiv k_n\bmod p\), and MASTER-RATIO has leading multipliers 3 and 1 respectively; thus the entire high portion equals \(\sum w_{m,n}c_nk_n\bmod p^2\). Crucially, the exceptional \(n=2m,4m\) are **not** included in these ordinary assertions.

For the original first seam, \(R_{2m}/p=3(c_{2m}/p)[1+pU_{2m}]\bmod p^2\). Direct first-order p-expansions give
\[
3\alpha_p\equiv2+5p,\qquad
p k_{2m}=\frac{(2-p)(2p+1)}{p+1}\equiv2+p\pmod{p^2}.
\]
Therefore
\[
\frac{\alpha_pR_{2m}/p-c_{2m}k_{2m}}p
\equiv(c_{2m}/p)(4+2U_{2m})\pmod p.
\]
At the **second** seam and retained terminal,
\(R_{4m}/p=(c_{4m}/p)[1+pU_{4m}]\bmod p^2\);
\[
\beta_p=3-2p,\qquad
2p k_{4m}=
\frac{(3-2p)(4p-1)}{2p-1}\equiv3-8p\pmod{p^2}.
\]
Hence
\[
\frac{\beta_pR_{4m}/p-2c_{4m}k_{4m}}p
\equiv(c_{4m}/p)(6+3U_{4m})\pmod p.
\]
Adding low, ordinary highs, both seam terms proves WHOLE-KERNEL. The inherited first-digit identity \(A_m-G_m+B_m\in p\mathbb Z_{(p)}\), or simply its already proved first-digit counterpart with the above lossless rewriting, establishes \(M_m^\ast-G_m\in p\mathbb Z_{(p)}\); dividing the congruence once by p gives ONE-OBSTRUCTION. QED.

### Exact author computation and observer scope

A separate Python 3 \`fractions.Fraction\` program **reconstructed \(R_n\) from the original recurrence**, reconstructed \(c_n\) independently, checked MASTER-RATIO for *every* \(0\le n\le4m\), checked every regular original term through p², and separately recomputed both exact original seam coefficients and the full WHOLE-KERNEL. Tested the 13 representative primes \(p=7,13,19,31,37,43,61,73,79,97,103,109,127\); **all checks passed**. Both \(p\equiv13,19\pmod{24}\) target classes are represented. The original finite target happened to have zero residual on these inputs, but this finite fact is explicitly **not** used as proof.

| p | \((M^\ast-G)/p\bmod p\) | \(L^\ast\bmod p\) | \(E^\ast\bmod p\) | sum |
|--:|--:|--:|--:|--:|
| 7 | 5 | 3 | 6 | 0 |
| 13 | 9 | 6 | 11 | 0 |
| 19 | 15 | 7 | 16 | 0 |
| 31 | 8 | 19 | 4 | 0 |
| 37 | 11 | 28 | 35 | 0 |
| 61 | 25 | 33 | 3 | 0 |
| 97 | 21 | 95 | 78 | 0 |
| 127 | 121 | 47 | 86 | 0 |

Executable author checker is preserved as the user-visible file \`/mnt/data/enterprise_math/d25_master_kernel_bridge_check.py\` during this turn (not a GitHub file, not a native benchmark). The proof and actual witness table above are the versioned research record.

### BRC, source separation, and next mandatory science

**BRC: REUSE_APPLIED / COMPOSE_APPLIED** for the actual finite rational arithmetic. Carrier = the single signed Pochhammer stream \(c_n\), exact integer index and p-valuation, the original range labels, the p-unit jump factors \(3\) and \(1/3\), two seam poles, original terminal coefficient, and the first p-adic jet \(U_n\). Observer = the original fully combined \(\mathcal K_p\) through p². WHOLE-KERNEL is a proved safe quotient *for this observer only*, not for third digits, native X6 dynamics, independent provenance, or a live Source publication. No component is erased merely because its scalar first digit happens to cancel.

**Do not repeat:** D24 accepted UR, original Gosper, LOW-JET, original two high sectors, square seam transport, all-prime p² seam merger, six-block Lerch, later independent two-port \(A_m\) recurrence or third-digit seam reports. They are consumed as provenance, not new results. Old three staged UR fragments remain source-separated.

**Precise next science:** attack ONE-OBSTRUCTION *as a single index-family*, not by yet another unrelated second-order moment. The common \((1/6)_n/(2^n n!)\) ratio permits an exact finite contiguous/WZ Ansatz. Preserve both explicit p-integral pole residues \(E^\ast\) and the 3-weight interval at \(m<n<2m\); seek a bounded finite difference whose boundaries are precisely at \(n=m,2m,4m\) and whose terminal equals \(G_m\), or a rigorous obstruction. Native D25 CM/divided-power representative, same-class comparison and original benchmark still require actual Source execution; the current Site identity cannot publish a native checkpoint. The responsible recovery path is the existing issue #1539, not a new scheduler or borrowed maintenance identity.

**Continuation packet:** mother and immutable source pin above; last portable author frontier = WHOLE-KERNEL; completed exact units = MASTER-RATIO and WHOLE-KERNEL; remaining target = ONE-OBSTRUCTION vanishing for every target prime plus required native proof/experiment and independent review; no Source session/claim/run/request was created here; historic own bridge request IDs are unchanged (#6186–#6188). Resume these results without redoing them and first reconcile current Source authority before any role-bound mutation.