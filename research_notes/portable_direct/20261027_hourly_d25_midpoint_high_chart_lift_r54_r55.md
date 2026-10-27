# D25/LIFT R54–R55 — integral cross-rank chart and optimal lift-observer precision

Date: 2026-10-27 Asia/Hong_Kong. Author-side portable research for independent ordinary TASK_RESEARCH logical lane \`chatgpt-research-hourly-enterprise-math-20260923\`; not CONTROL_PLANE_MAINTENANCE. Mother D25/LIFT/JT2 OPEN; Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`. Frozen **scientific** Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`, not replaced by later control commits. Classification \`AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY\`.

## Exact inputs, attribution and provenance

Consume without recrediting: R23's **proved** source-labelled full/half and high-tail reduction; R47's exact W/S one-step rational transitions; R50's finite Green two-endpoint identity; R51's three exceptional high-high determinant primes; R52's lossless divided-difference endpoint jet; the separate on-hour Research lane's exact midpoint two-port theorem; and the newly published R53 theorem that the *actual original low-half observer* avoids exceptional fourth-order Green poles. The already proved companion **full and half** supercongruences are due to Guo–Zudilin, *A q-microscope for supercongruences*, Adv. Math. 346 (2019), 329–358, arXiv:1803.01830. The D24 accepted first digit is used **only in its frozen p ≡ 13,19 (mod 24) target scope**.

For each prime \(p=6m+1\ge13\), set \(h=3m=(p-1)/2\) and \(N=\lfloor(3p-1)/4\rfloor+1\). The original unchanged rational sources are

\[
 w_k=\frac{(6k+1)(2k)!(3k)!}{(k!)^5\,216^k},\qquad
 s_k=\frac{(8k+1)(4k)!}{(k!)^4\,2304^k}.
\]

Write \(a_k=w_{k+1}/w_k\), \(b_k=s_{k+1}/s_k\), where (R47)

\[
 a_k=\frac{(6k+7)(2k+1)(3k+1)(3k+2)}
 {36(6k+1)(k+1)^3},\qquad
 b_k=\frac{(8k+9)(2k+1)(4k+1)(4k+3)}
 {288(8k+1)(k+1)^3}.
\]

Define the **actual** midpoint units \(u_*=w_h/p,\ v_*=s_h/p\in\mathbf Z_{(p)}^\times\), and the **free labelled two-source carrier** \((u,v)\in\mathbf Z_p^2\) via \(W_k(u)=w_k\,u/u_*\), \(S_k(v)=s_k\,v/v_*\) for every original rank \(0\le k<p\). At the original source trajectory \((u,v)=(u_*,v_*)\), these are exactly \(w_k,s_k\); no coefficient, cutoff, source label or input is modified there. The free variation is used **only to prove observer sufficiency and its impossibility witnesses**, not to replace the original supercongruence.

## R54 — explicit unimodular gluing of midpoint and high-high Green charts

Let

\[
 a'_h=a_h/p,\quad b'_h=b_h/p,\quad \delta=a'_h-b'_h,\qquad
 c=\frac{w_N}{p^3u_*},\quad d=\frac{s_N}{p^3v_*}.
\]

The consumed midpoint theorem gives \(a'_h\equiv1/9,\ b'_h\equiv5/108,\ \delta\equiv7/108\pmod p\); hence \(\delta\) is a unit for every specified \(p\ge13\). The consumed R51 valuation theorem gives \(c,d\in\mathbf Z_p^\times\), and

\[
 \lambda=v_p(a_N-b_N)=
 \begin{cases}
 1,&p\in\{139,199,277\},\\
 0,&\text{all other primes }p\equiv1\pmod6,\ p\ge13.
 \end{cases}
 \qquad e=(a_N-b_N)/p^\lambda\in\mathbf Z_p^\times.
\]

Retain **two different charts** on the same source-labelled carrier:

\[
 M_0=\frac{W_h-S_h}{p}=u-v,\qquad
 M_1=\frac{W_{h+1}-S_{h+1}}{p^2}=a'_h u-b'_h v;
\]

\[
 J_0=\frac{W_N-S_N}{p^3}=cu-dv,\qquad
 J_1=\frac{(W_{N+1}-S_{N+1})-a_N(W_N-S_N)}
 {p^{3+\lambda}}=edv.
\]

**New cross-rank chart theorem.** For all stated primes and every free integral pair, both \(M=(M_0,M_1)\) and \(J=(J_0,J_1)\) are unimodular coordinate charts, and the exact transition is

\[
 \boxed{
 \begin{pmatrix}J_0\\J_1\end{pmatrix}
 =\frac1\delta
 \begin{pmatrix}
 da'_h-cb'_h&c-d\\
 -ed a'_h&ed
 \end{pmatrix}
 \begin{pmatrix}M_0\\M_1\end{pmatrix},\qquad
 \det T=\frac{cde}{\delta}\in\mathbf Z_p^\times.}
 \tag{R54}
\]

**Proof.** The midpoint row matrix is \(\bigl(\begin{smallmatrix}1&-1\\a'_h&-b'_h\end{smallmatrix}\bigr)\), with determinant \(\delta\). It has inverse \(u=(M_1-b'_hM_0)/\delta\), \(v=(M_1-a'_hM_0)/\delta\). The high chart matrix is \(\bigl(\begin{smallmatrix}c&-d\\0&ed\end{smallmatrix}\bigr)\), with unit determinant \(cde\); its second row follows by subtracting \(a_NJ_0\) from the raw second endpoint. Multiplication yields (R54) and proves integral invertibility. This is an **exact \(p\)-adic identity**, not merely a mod-\(p\) match. The exceptional loss of one digit in the *raw* high pair is repaired by precisely the R52 divided-difference coordinate.

The midpoint result comes from another actual Research lane and remains attributed to its published proof; its appearance in (R54) is a new explicit **cross-lane mathematical composition**. The auxiliary rank \(k\) is not a native Enterprise X6 spatial axis.

## R55 — source-faithful scalar lift locus and sharp two-versus-three-digit bound

Now restrict the universal precision claim to the frozen target classes \(p\equiv13,19\pmod{24}\), \(p\ge13\). Write \(W_p=\sum_{k=0}^{p-1}w_k\), \(S_p=\sum_{k=0}^{p-1}s_k\), \(W_{\le h}=\sum_{k=0}^h w_k\), \(S_{\le h}=\sum_{k=0}^h s_k\). The accepted original W first digit gives \(W_p\equiv p\pmod{p^2}\), and published Guo–Zudilin gives \(S_p\equiv S_{\le h}\equiv p\pmod{p^3}\). R23 proves \(W_{>h}\in p^2\mathbf Z_p\), with the genuine W high-source \(U_p=W_{>h}/p^2\bmod p\).

For the **free but otherwise unchanged labelled trajectories** introduced above, the exact full scalar is

\[
 F_p(u,v):=\sum_{k=0}^{p-1}(W_k(u)-S_k(v))
 =p(Au-Bv),\quad
 A=\frac{W_p/p}{u_*},\quad B=\frac{S_p/p}{v_*}\in\mathbf Z_p^\times.
 \tag{55.1}
\]

For \(F_p\bmod p^3\), R23 additionally yields the **source-separated** coefficients

\[
 A\equiv\frac{W_{\le h}/p+p U_p}{u_*},\qquad
 B\equiv\frac{S_{\le h}/p}{v_*}\pmod{p^2}.
 \tag{55.2}
\]

Thus the exact congruence predicate on this specified free-state family is the graph

\[
 \boxed{F_p(u,v)\equiv0\pmod{p^3}
 \iff v\equiv B^{-1}Au\pmod{p^2}.}
 \tag{55.3}
\]

For the **original fixed** \(u=u_*,v=v_*\), this is precisely the still-open full W/S lift. Formula (55.3) does not assert that the fixed pair satisfies it.

**Optimal information theorem.** Among observers restricted to a specified two-port finite precision readout of this free-state family:

1. The **joint high jet** \(J=(J_0,J_1)\) modulo \(p^2\) is sufficient to decide (55.3), at every frozen target prime, because (R54) is a \(\mathrm{GL}_2(\mathbf Z_p)\) map. One joint-jet digit does not suffice: choose unit \(u=1,\ v=B^{-1}A\pmod{p^2}\), then change \(v\) by \(p\). Both jet readings agree modulo \(p\), while \(F_p\) changes by \(-p^2B\), a nonzero residue modulo \(p^3\). Hence **two digits are necessary and sufficient**.
2. Let \(Z=(Z_0,Z_1)\) denote the *raw*, uncorrected normalized high pair
\[
 Z_0=(W_N-S_N)/p^3,\quad Z_1=(W_{N+1}-S_{N+1})/p^3.
\]
 Its matrix is \(R=\bigl(\begin{smallmatrix}c&-d\\a_Nc&-b_Nd\end{smallmatrix}\bigr)\), with determinant \(cd(a_N-b_N)\) of valuation \(\lambda\). When \(\lambda=0\), **two raw digits** are necessary and sufficient by the same fiber witness and invertible-matrix argument. When \(\lambda=1\), **three raw digits** are sufficient: the inverse has exactly one \(p^{-1}\) factor, so \(Z\bmod p^3\) determines \((u,v)\bmod p^2\).
3. At the two frozen exceptional primes \(p=139,277\), **three raw digits are necessary as well**. The same precise statement also holds at the single outside-target exceptional prime \(p=199\), because an independent finite exact calculation there verifies \(W_{199}\equiv199\pmod{199^2}\); the published companion result supplies \(S_{199}\equiv199\pmod{199^3}\). This **single-prime extension** makes no all-prime D24 claim in class \(7\pmod{24}\).

**Sharpness proof at an exceptional prime.** On the free integral carrier, choose a unit base point \(u=1,\ v=B^{-1}A\bmod p^2\) satisfying \(F_p\equiv0\pmod{p^3}\). Perturb by

\[
 (\Delta u,\Delta v)=p(d\bmod p,c\bmod p).
\]

The new point remains unit-valued. Since \(a_N\equiv b_N\pmod p\), the two points have identical **raw** \(Z_0,Z_1\bmod p^2\). Yet their scalar difference is

\[
 \Delta F_p\equiv p^2(Ad-Bc)\pmod{p^3}.
\]

Because \(W_p/p\equiv S_p/p\equiv1\bmod p\),

\[
 \boxed{Ad-Bc\equiv-\frac{X_*}{u_*v_*}\pmod p,\qquad
 X_*=\frac{w_N-s_N}{p^3}\bmod p.}
\]

The complete exceptional set has original \(X_*=(100,70,27)\) at \(p=(139,199,277)\), respectively, **all nonzero**. Hence the two raw-mod-\(p^2\) readings are identical while one state satisfies the lift and the other does not. This proves the sharp three-digit lower bound for each specified exceptional prime, including unit amplitudes and arbitrary nonlinear decoders. It does not claim that the original fixed factorial trajectory is a false lift.

The result is a bridge from the actual R23 observable to *observer precision*, not an unchanged-input WZ proof. R53's cancellation of fourth-order poles for the true low-half scalar is consumed rather than recredited; the three raw normalized endpoint digits correspond to original endpoint precision \(p^6\), while the divided-difference joint jet retains the cancellation intrinsically and needs only two of its own digits.

## Exact checks, source firewall, BRC, recovery

A local Python standard-library modular checker (file below) was **actually executed**. It checked all **79** primes \(13\le p<1000,\ p\equiv1\pmod6\): midpoint and high factorial valuations and residues; both chart transitions and determinants; Guo–Zudilin full/half companion mod \(p^3\); direct original W first digit mod \(p^2\); genuine high W split; and at every exceptional prime, the *unit-to-unit source perturbation* witness and its unequal mod-\(p^3\) output. The latter author's finite \(p=199\) certificate is kept finite; universal claims use the algebraic proofs and the exact input scope. No Lean/native H0/B0, independent peer review or accepted Result was executed.

Selected \((p,h,N,J_0,J_1,\det T,U_p)\bmod p\):

| p | h | N | J0 | J1 | det T | W-high U |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 6 | 10 | 12 | 8 | 6 | 10 |
| 19 | 9 | 15 | 13 | 6 | 10 | 9 |
| 139 | 69 | 105 | 100 | 90 | 12 | 13 |
| 181 | 90 | 136 | 17 | 96 | 4 | 152 |
| 199 | 99 | 150 | 70 | 116 | 29 | 172 |
| 277 | 138 | 208 | 27 | 95 | 10 | 10 |
| 373 | 186 | 280 | 113 | 12 | 166 | 266 |

At the three sharp exceptional witnesses, the nonzero \((Ad-Bc,\Delta F_p)\) certificates are \((38,734198)\) at 139, \((39,1544439)\) at 199 and \((210,16113090)\) at 277. Every \(\Delta F_p=p^2(Ad-Bc)\bmod p^3\).

**BRC COMPOSE_APPLIED:** carrier consists of original labelled W/S amplitudes, their exact factorial provenance, the auxiliary ordered rank, \(p\)-adic valuation, signed midpoint and endpoint ports, the congruence predicate and declared future observation precision. The raw high observer erases one transverse digit precisely at the three R51 primes; the R52 joint difference restores it. Original Hasse six-source \(z=2\) channels, finite boundaries, positive-infinity source, P000 native X6 and ACTIVE worldview are retained **as separate tasks/interfaces**, not inferred from this two-dimensional auxiliary arithmetic chart.

**Durable frontier:** R54 proves a universal cross-rank \(\mathrm{GL}_2(\mathbf Z_p)\) gluing theorem; R55 proves a sharp, observer-specific **two joint vs three raw digits** requirement at the relevant exceptional primes. Both are author-side / unreviewed. Do not redo R23, R47, R50, R51, R52, the separate on-hour midpoint theorem or the new R53 genuine-half-pole cancellation.

**Next mathematical unit:** use (55.2) to seek a genuine unchanged-original-input telescoping identity for \(W_{\le h}/p+pU_p-S_{\le h}/p\) modulo \(p^2\); test whether R36's PF Green inverse supplies a source-compatible operator without identifying distinct carriers by fiat. Preserve \(p=139,199,277\), \(p=181,373\), all six fixed Hasse J/E labels and infinity. Native H0/B0 \([X]U\bmod p^2\), Frobenius semilinear rank/\(\eta/\kappa\), native \(p=373\) benchmark and independent Driver review remain parent acceptance obligations.

**Control at last read:** own stable Research logical ID as above, previous recovery #6622 and continuation #6623 both terminal read-SUCCEEDED but grant \`execution_authorized=false\`; previous own service session \`MCP-06f7ad61a8d841d9ba1ba1ef4d088d94\` has no observed own CLAIM/open/run; two neutral preserved-staging references remain. Current gateway status 0.6.11 still reports \`research_authority_granted=false\`, \`executor_binding_configured=false\`, native quota at five active jobs. Prior Source checkpoint/CLAIM predecessor mismatch remains with Enterprise Math #1558. These author GitHub files do **not** constitute a current canonical CLAIM, native \`publish_checkpoint\`, Research-Activity semantic event, Result or peer admission. Current activity semantic checkpoint remains \`REGISTER_PENDING\`; retain old request IDs and protected Source frontier.
