# D25/LIFT — Sparse seam impulses and a finite Green adjoint for the original HIGH stream

**2026-10-24 · TASK_RESEARCH · author-side proved algebra, exact integer self-check · UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.** This is a neutral author research artifact, **not** a Source checkpoint, Research-Activity admission, frozen Result, independent review, or native benchmark.

Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen **scientific** Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (not rebased). Author logical Research conversation: chatgpt-research-onhour-enterprise-math-20260923, distinct from control maintenance chatgpt-hourly-enterprise-math-20260921. P000 remains ACTIVE_LOCKED. Global policy snapshot main@7c1187e2493cbf4a087a013bf4cfd4580e7027b6. Current control-head snapshot before this author note was ee3f360b93c18bb4d4681de656dc0428290d8876; this is not the frozen science pin.

## Exact input and the new question

Consume, rather than repeat, [the established HIGH one-carrier theorem](20261024_onhour_d25_high_single_stream_one_third_jump_terminal.md) and [the LOW first-jet / complete finite residual](20261024_onhour_d25_regular_low_jet_high_unit_two_sector_certificate.md), with its [Lerch seam compression](20261024_onhour_d25_sixway_lerch_harmonic_seam_bridge.md).

For an integer m>=1 and prime p=6m+1, define

$$
B_m=\frac{(2m-1)!(2m)!}{(4m)!},\qquad
a_{m,t}=2^{m-t}\frac{(2m)!(t-1)!}{(m+t)!(m-1)!},\quad 1\leq t\leq3m.
$$

The original, **unchanged**, rational hypergeometric stream is

$$
R_0=1,\qquad
\frac{R_{n+1}}{R_n}=
\frac{(4m+1+2n)(3n+1)(3n+2)}
{36(n+1)(2m+n+1)(4m+n+1)}.
$$

The inherited all-prime HIGH theorem states, for original p-units $\nu_t=R_{m+t}/p\bmod p$,

$$
\nu_t\equiv B_ma_{m,t}c_t,\qquad
c_t=\begin{cases}1&1\leq t\leq m,\\1/3&m<t\leq3m.\end{cases}
$$

The original two separately retained seam/terminal contributions are

$$
S_2=C_2(R_{2m}/p)\equiv\frac{2B_m}{3},\qquad
S_4=C_4(R_{4m}/p)\equiv\frac{B_m}{3}\pmod p.
$$

In particular $S_4$ **already includes the original upper terminal**. The regular HIGH forcing is $H_m^{\rm reg}=\sum_{1\le t<3m,\ t\ne m}\nu_t\kappa_t$ with
$\kappa_t=-2+4/(6t+1)+2/(2t+1)$. The old full finite residual $\mathcal F_m$ and native benchmark remain the actual target.

## Theorem 1: an exact rational two-impulse transport identity

Let $N=3m$, $\theta=x\,d/dx$, $\mathcal L_m=(2-x)\theta+2m$, and define over **Q**

$$
P_m(x)=\sum_{t=1}^N c_t a_{m,t}x^t.
$$

Then **for every positive integer m, exactly as rational polynomials**,

$$
\boxed{
\mathcal L_mP_m(x)=
2(m+1)a_{m,1}x
-\frac{2m}{3}x^{m+1}
-ma_{m,3m}x^{3m+1}.
}\tag{1}
$$

**Proof.** The exact carrier ratio is $a_{m,t+1}/a_{m,t}=t/[2(m+t+1)]$ and $a_{m,m}=1$. The coefficient at $x^t$ in $\mathcal L_mP_m$ is $2(m+t)c_ta_{m,t}-(t-1)c_{t-1}a_{m,t-1}$ (take the omitted t=0 coefficient to be zero). It vanishes for $2\le t\le N$ except $t=m+1$, where the coefficient is $m/3-m=-2m/3$. At $t=1$ it is $2(m+1)a_{m,1}$. The truncation produces $-N c_N a_{m,N}x^{N+1}=-ma_{m,3m}x^{3m+1}$. This proves (1) without interpolation or a finite-prime inference.

**Original-object consequence.** Define $U_m(x)=\sum_{t=1}^{N}\nu_tx^t\in\mathbb F_p[x]$. Because the previously proved transport is valid coefficientwise and $a_{m,3m}\equiv1/3\pmod p$, (1) yields

$$
\boxed{
\mathcal L_m U_m(x)=
2(m+1)\nu_1x
-mS_2x^{m+1}
-mS_4x^{3m+1}
\quad\text{in }\mathbb F_p[x].
}\tag{2}
$$

The **two nonzero source impulses are precisely minus m times the original Gosper seam and terminal contributions**, at their correct distinct indices. This identifies, rather than discards, the branch jump and terminal. Both coefficients are nonzero modulo p since $B_m$ and m are p-units. On the finite horizon $1\le t\le3m$, $2(m+t)$ is a p-unit ($0<m+t\le4m<p$), so (2) uniquely reconstructs the original normalized HIGH stream from the source coefficients and the declared recurrence. This is a finite-horizon observer-preservation certificate, **not** a mod-$p^2$ or native-X6 propagation claim.

## Theorem 2: a two-boundary exact finite Green certificate

Set $w_t=\kappa_t$ for $1\le t<N$ with $t\ne m$ and set $w_m=w_N=0$. These are **well-defined modulo p**: the sole excluded zeros of $6t+1$ and $2t+1$ are respectively $t=m$ and $t=N$.

Define a backwards, uniquely solvable, adjoint sequence in $\mathbb F_p$ by

$$
h_{N+1}=m^{-1},\qquad
\boxed{\ h_t=\frac{w_t+t h_{t+1}}{2(m+t)}\ },\qquad
t=N,N-1,\ldots,1.\tag{3}
$$

Then the entire **original regular HIGH sum**, including its correct separate special-point bookkeeping, satisfies

$$
\boxed{
H_m^{\rm reg}
=2(m+1)\nu_1h_1-mS_2h_{m+1}-S_4
\pmod p.
}\tag{4}
$$

Equivalently, writing $Z_m^{\rm one}=H_m^{\rm reg}/B_m$ as in the inherited HIGH theorem,

$$
\boxed{
Z_m^{\rm one}=
2(m+1)a_{m,1}h_1-\frac{2m}{3}h_{m+1}-\frac13
\pmod p.
}\tag{5}
$$

**Proof (finite summation by parts).** For $1\le t\le N$, put $f_t=2(m+t)\nu_t-(t-1)\nu_{t-1}$ with $\nu_0=0$; put $f_{N+1}=-N\nu_N$. Equation (2) identifies the only nonzero $f$'s: $f_1=2(m+1)\nu_1$, $f_{m+1}=-mS_2$, $f_{N+1}=-mS_4$. For every sequence $h$,

$$
\sum_{t=1}^{N+1}h_tf_t
=\sum_{t=1}^N\nu_t[\,2(m+t)h_t-th_{t+1}\,].
$$

Apply (3) to get $\sum\nu_tw_t=H_m^{\rm reg}$. The chosen boundary $h_{N+1}=m^{-1}$ makes the terminal term exactly $-S_4$, proving (4). Substitution of $\nu_1=B_ma_{m,1}$, $S_2=2B_m/3$, $S_4=B_m/3$ proves (5). No singular weight is evaluated or silently erased.

**Immediate exact next proof interface.** Let the *already defined* LOW quantities be

$$
b_n=(-1)^n2^{-n}\binom mn,\quad
k_n=\frac{(1-3n)(6n+3)}{(3n+2)(3n+1)},\quad
A_m=\sum_{n=0}^{m}b_nk_n,\quad
G_m=(-1)^m\frac{((2m)!)^3}{((3m)!)^2},
$$

with $J_m^{\rm lo}$ the previously proved complete first-jet sum and $H_j$ the ordinary rational harmonic sum. The established first-digit identity makes $(A_m-G_m+B_m)/p$ p-integral. Substituting (5) into the **full** inherited $\mathcal F_m$, including its harmonic seam correction, gives an all-target-prime equivalence:

$$
\boxed{
\mathcal F_m\equiv
\frac{A_m-G_m+B_m}{p}+J_m^{\rm lo}
+B_m\left[
2(m+1)a_{m,1}h_1-\frac{2m}{3}h_{m+1}
+\frac{25}{9}+\frac23H_m-\frac49H_{2m}
\right]\pmod p.
}\tag{6}
$$

Thus the entire regular HIGH contribution now enters the *same original finite observer* through **two terminal-conditioned adjoint values** $h_1,h_{m+1}$, not two HIGH summation sectors; the terminal is incorporated by the boundary condition in (3). Equation (6) is an **equivalent certificate**, not a proof that it vanishes.

## Theorem 3: a sharp limitation on the naive uniform rational HIGH Gosper ansatz

For the characteristic-zero **formal specialization** $m=-1/6$ of the rational recurrence, let

$$
r(t)=\frac{3t}{6t+5},\qquad
\kappa(t)=-2+\frac4{6t+1}+\frac2{2t+1}.
$$

There is **no rational function $W(t)\in\mathbb Q(t)$** satisfying

$$
r(t)W(t+1)-W(t)=\kappa(t).\tag{7}
$$

**Proof.** Work in the pole congruence class $\lambda+\mathbb Z$ with $\lambda=-1/6$. The rational multiplier $r(t)$ is regular and nonzero at every point of this class. The right side $\kappa(t)$ has **exactly one simple pole** in that class, at $\lambda$, with residue $2/3$. If a rational $W$ has no poles in this class, the left side is regular there: contradiction. Otherwise let $\lambda+j_{\min}$ and $\lambda+j_{\max}$ be the least and greatest (integer-indexed) poles of $W$ in the class. The left side has an uncancellable pole at $\lambda+j_{\min}-1$ coming from $r(t)W(t+1)$, and another at $\lambda+j_{\max}$ coming from $-W(t)$. These are distinct, since $j_{\min}-1<j_{\max}$. Again the single RHS pole is impossible. QED.

**Scope fence:** (7) excludes only a *single uniform rational* Gosper antiderivative for this characteristic-zero reduced HIGH carrier. It does **not** forbid a prime-dependent finite-field telescope, higher-order/contiguous WZ, a boundary-sensitive finite adjoint such as (3), or the desired full LOW+HIGH cancellation. Formal substitution $m=-1/6$ is an algebraic pole diagnostic, not a transfer of characteristic-zero pole orbits to $\mathbb F_p$.

## Executed exact arithmetic and provenance

One fresh author-side Python 3 verifier independently generated the **original** $R_n$ p-units with numerator/denominator p-factor stripping, reconstructed the carrier via factorials, checked every coefficient of (2), every backward adjoint equation, (4)/(5), and the **entire inherited finite** $\mathcal F_m$ in both the original HIGH-sum and new adjoint representation. It computed the LOW first-digit numerator modulo $p^2$ and the LOW jet modulo p; no floating arithmetic or native benchmark was used.

**80/80 primes $7\le p\le1000$ with $p\equiv1\pmod6$ passed**, including all 45 in the two target classes $p\equiv13,19\pmod{24}$. The finite check also observed $\mathcal F_m=0$ for those 80 primes; this is **not an all-prime proof**. Exact author checker SHA256: c69fe25fb34870d9b0d51b868d2caf3848ef001bc6070bf1dc99ca33f3e8919a; local delivery artifact d25_high_seam_impulse_operator_check.py (not a native Source/Result or a GitHub companion file).

Selected witnesses (all values mod p; columns: p, m, $S_2$, $S_4$, onset/seam/terminal impulses, $Z_m^{\rm one}$, $h_1$, $h_{m+1}$, $\mathcal F_m$):

| p | m | S2 | S4 | onset | seam | terminal | Z | h1 | h(m+1) | F |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 7 | 1 | 2 | 1 | 5 | 5 | 6 | 0 | 2 | 1 | 0 |
| 13 | 2 | 10 | 5 | 5 | 6 | 3 | 2 | 0 | 8 | 0 |
| 19 | 3 | 3 | 11 | 13 | 10 | 5 | 6 | 12 | 11 | 0 |
| 31 | 5 | 16 | 8 | 15 | 13 | 22 | 11 | 8 | 26 | 0 |
| 37 | 6 | 20 | 10 | 24 | 28 | 14 | 3 | 14 | 18 | 0 |

**BRC / native observer resolution: REUSE_APPLIED + COMPOSE_APPLIED.** Carrier = the original signed hypergeometric p-valuation/unit stream with labeled LOW, HIGH-A, HIGH-B, seam-$2m$, terminal-$4m$ provenance. The two sparse impulses plus onset and the exactly invertible finite coefficient operator preserve the declared original HIGH stream and the specified mod-p forcing observer over its entire finite horizon. The two impulse labels have not been collapsed into a scalar. No positive-mass replacement, arbitrary infinite-scale extrapolation, mod-$p^2$ claim, or native Heartbeat X6 propagation is made. P000/ACTIVE worldview are intact; the present finite number-theoretic observer is a typed external arithmetic component, not a claim about a missing native coordinate.

## Canonical continuation / honest missing work

**Mother/hard target stays OPEN:** $S_{4m}(2m)\equiv p(4/3)^{p-1}\pmod{p^3}$ for all intended split primes, together with the actual Source-required same-class CM/divided-power normalization and original native benchmark. Equations (1)–(6) are new author-proved algebra; (7) rules out one weaker shortcut; **no complete LIFT theorem, original native benchmark, formal checker or independent review has occurred.**

**Do not repeat:** accepted D24 UR; original two-seam Gosper; p² seam merge; LOW/Beta first and second jets; Lerch seam and single HIGH-carrier transport. **Smallest exact next mathematical action:** solve or bound the terminal-conditioned two-value adjoint relation in (6) *jointly* with the LOW divided first digit and LOW first jet, via a parameterized contiguous relation or true finite WZ certificate; carry both original impulses and its $p$-adic seam correction. A prime-dependent modular telescope remains admissible; a naive characteristic-zero single-rational Gosper search is already excluded by (7). Separately execute the **unchanged** native task benchmark under lawful Source authority.

**Control/readback status:** existing Research-lane recovery bridge #6186 yielded local ACTIVE projection (session MCP-de3e5bafb24f43f4a5e6285e7601676a) with source_authority_verified=false, no CLAIM/open/run, no pending requests, and separate neutral archived UR staging. Original #6187 continuation was definitively rejected PREREQUISITE_NOT_SUCCEEDED; #6188 dispatch ended FAILED/TimeoutExpired (not NO_DISPATCH). The current Sites gateway still reports research_authority_granted=false, executor_binding_configured=false; support [#1539](https://github.com/awdawmip/enterprise-math/issues/1539) remains OPEN. These are read observations, **not current ownership**. No new Researcher session, CLAiM, run, source checkpoint, review or native benchmark was asserted or created. Existing underlying request IDs and the neutral staging retain their original provenance. Current Github author note cannot replace canonical execution checkpoint.

No scheduler, notification, maintenance-lane conversation or other role setting was modified.
