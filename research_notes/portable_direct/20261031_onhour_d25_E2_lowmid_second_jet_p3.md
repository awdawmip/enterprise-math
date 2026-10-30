# D25 SECOND-DIGIT-LIFT — exact p³ harmonic-jet resolution of the original 216/E.2 low–middle carry

2026-10-31 Asia/Hong_Kong. Portable author-side research by onhour logical lane \`chatgpt-research-onhour-enterprise-math-20260923\`. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`. Frozen scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` **unchanged**. P000 ACTIVE_LOCKED and account ACTIVE worldview unchanged. Classification: **AUTHOR-SIDE / EXACT p³ COEFFICIENT THEOREM / EXECUTED 166-PRIME REGRESSION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NO_NATIVE_H0B0_RUN**.

## Selected unfinished question, scope and predecessors

The accepted/consumed first-digit D24/UR and distinct Van Hamme E.2 theorem establish, under the frozen inert-prime input, that \`D0+D1 ∈ p² Z_(p)\`. The onhour source \`20261031_onhour_d25_E2_first_digit_dependency_closure.md\` proves this **by composition**, not by re-proving the parents. Another Research lane's \`20261031_hourly_d25_e2_four_port_first_digit_bridge.md\` independently gives the **first-order** four-port formula; it is not our contribution and is not reproduced here. The onhour factorial inverse-moment source \`20261031_onhour_d25_inverse_moment_factorial_wz.md\` is consumed unchanged.

The exact remaining scientific target is a proof (or falsifier), for all primes \`p ≡ 13,19 (mod 24)\`, of
\[
\frac{D_0+D_1}{p^2}+\mathcal I_p\equiv0\pmod p.
\]
We now resolve the **unexpanded low/middle quotient** into a *complete second-order p-adic harmonic jet* with nonzero, independently retained ports. This is a new exact arithmetic interface, **not** a proof of the remaining cancellation.

Define \`p=6l+1\`, \`m=2l\`, \`h=3l\`, \`q=4l\`, and keep the original source labels
\[
a_n=\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3},\quad
b_n=(-1)^n\frac{(1/3)_n^3}{(n!)^3},
\]
\[
D_0=\sum_{n=0}^m(6n+1)(a_n-b_n),\qquad
D_1=\sum_{n=m+1}^{h}(6n+1)a_n.
\]
Every denominator appearing below is a p-unit. All equalities before reduction are in \`Z_(p)\`.

## Theorem A — complete p³ jet for each low coefficient

For \`0≤n≤N<p\`, put
\[
d_N(n)=\sum_{r=N-n+1}^{N}\frac1r,\qquad
d_N^{[2]}(n)=\sum_{r=N-n+1}^{N}\frac1{r^2}.
\]
For \`0≤n≤m\`, put
\[
t_n=(-1)^n 2^{-n}\binom hn\binom mn\binom qn,\qquad
v_n=\binom mn^3,
\]
\[
L_n=-\frac12d_h(n)-\frac13d_m(n)-\frac23d_q(n),
\quad
J_n=\frac14d_h^{[2]}(n)+\frac19d_m^{[2]}(n)+\frac49d_q^{[2]}(n).
\]
Then, for **every** prime \`p=6l+1≥7\`,
\[
\boxed{a_n\equiv t_n\left[1+pL_n+\frac{p^2}{2}(L_n^2-J_n)\right]\pmod{p^3},}
\tag{A}
\]
\[
\boxed{b_n\equiv v_n\left[1-p\,d_m(n)
+\frac{p^2}{2}\left(d_m(n)^2-\frac13d_m^{[2]}(n)\right)\right]\pmod{p^3}.}
\tag{B}
\]

*Proof.* The **exact** factorization for \`n≤N<p\`,
\[
(-N+\alpha p)_n=(-N)_n\prod_{r=N-n+1}^{N}(1-\alpha p/r),
\]
has product expansion \`1-\alpha p d_N+p²\alpha²(d_N²-d_N^{[2]})/2\` modulo p³. Apply separately to \`1/2=-h+p/2\`, \`1/3=-m+p/3\`, \`2/3=-q+2p/3\`. Logarithmic collection of their cross-terms yields \`L,J\`; the factorial signs yield \`t_n\`. For \`b_n\`, all three factors are \`-m+p/3\`; their combined first-log coefficient is \`-d_m\` and combined squared-log coefficient is \`d_m^{[2]}/3\`, with the external \`(-1)^n\` cancelling the triple factorial sign. QED.

## Theorem B — complete p³ jet for the once-crossed original middle strip

For \`n=m+j,\ 1≤j≤l\`, set
\[
u_n=\frac{m!(j-1)!}{3n!2^n}\binom hn\binom qn,\qquad
Z_n=\frac{H_{j-1}-H_m}{3}-\frac12d_h(n)-\frac23d_q(n).
\]
Then
\[
\boxed{a_n\equiv p\,u_n(1+pZ_n)\pmod{p^3}.}
\tag{C}
\]
*Proof.* Extract the single zero factor \`p/3\` from
\[
(1/3)_{m+j}=\prod_{r=0}^{m+j-1}(-m+r+p/3).
\]
The earlier \`m\` factors contribute \`(-1)^m m! (1-pH_m/3)\`, the later \`j-1\` positive factors contribute \`(j-1)!(1+pH_{j-1}/3)\`, modulo p² after extracting \`p/3\`. The two un-crossed factors supply \`-p\,d_h/2\` and \`-2p\,d_q/3\`; \`m\` is even, so the sign is positive. Division by \`2^n(n!)^3\` and factorial simplification prove (C). QED.

## Theorem C — three independent source ports and legitimate carry

Define the following *explicit finite rational sums*, without assuming any unproved vanishing:
\[
\begin{aligned}
F_0&=\sum_{n=0}^{m}(6n+1)(t_n-v_n),\\
F_1&=\sum_{n=0}^{m}(6n+1)\bigl(t_nL_n+v_nd_m(n)\bigr)
 +\sum_{n=m+1}^{h}(6n+1)u_n,\\
F_2&=\frac12\sum_{n=0}^{m}(6n+1)\left[
t_n(L_n^2-J_n)-v_n\left(d_m(n)^2-\frac13d_m^{[2]}(n)\right)\right]\\
&\quad+\sum_{n=m+1}^{h}(6n+1)u_nZ_n.
\end{aligned}
\tag{D}
\]
Substituting (A), (B), (C) term by term proves **unconditionally**
\[
\boxed{D_0+D_1\equiv F_0+pF_1+p^2F_2\pmod{p^3}.}
\tag{E}
\]
For the **frozen target classes**, *consuming* the previously discharged first-digit theorem \`D0+D1∈p²Z_(p)\` (and NOT asserting it from (E)), we obtain \`F0+pF1∈p²Z_(p)\`. Therefore both quotients exist and
\[
\boxed{\frac{D_0+D_1}{p^2}
\equiv\underbrace{\frac{F_0+pF_1}{p^2}}_{C_{01}}
+\underbrace{F_2}_{\text{genuine second jet}}\pmod p.}
\tag{F}
\]
This is a **complete** p³ resolution of the low/middle carry. Combining, without taking ownership of, the prior factorial high-strip result
\[
\mathcal I_p\equiv \frac1{12h!(2m)!m!}
\sum_{j=1}^{l}(1-6m-6j)
\frac{2^{m+j}((m+j-1)!)^3(l-j)!(m-j)!}{(j-1)!}\pmod p
\]
makes the remaining *joint* target
\[
\boxed{C_{01}+F_2+\mathcal I_p\stackrel?{\equiv}0\pmod p.}
\tag{G}
\]
The residue \`C_01\` is a **carry observer**, not a termwise \`mod p\` value. Applying an early mod-p quotient to \`F0\` or \`F1\` would lose information. Both original and E.2 labels, their valuation, the signed \`6n+1\` operator, and the middle-strip zero crossing are retained.

## Executed independent checks and information-loss witness

Executed \`research_notes/portable_direct/d25_e2_lowmid_harmonic_jet_20261031.py\` with Python stdlib exact modular integer arithmetic for **all 166 primes p≤5000 with p≡13,19 (mod24)**. At each prime it reconstructed \`a_n,b_n\` by **different rational recurrences** mod p³ and independently checked every low coefficient (A),(B), every middle coefficient (C), combined identity (E), legal divisibility/carry (F), and the previously proved high-strip residual. Six representative primes were also cross-checked against the *original integer-binomial* weighted 216 sum, independent of the rational recurrence.

| p | C_01 | F_2 mod p | (D0+D1)/p² | I_p | total mod p |
|---:|---:|---:|---:|---:|---:|
|13|3|0|3|10|0|
|19|13|16|10|9|0|
|37|35|19|17|20|0|
|43|29|22|8|35|0|
|67|64|12|9|58|0|
|373|247|233|107|266|0|

At p=373, **247+233=480≡107**, and **107+266=373≡0**. The second-order jet is **nonzero at 165 of 166** checked target primes, and the first/middle carry port is also nonzero at 165 of 166; the high strip is nonzero at all 166. Consequently, **discarding the second-order jet is a provably invalid computation** already at p=19 and p=373. These are exact finite counterexamples to that shortcut, not an all-prime proof of (G). Terminal marker: \`PASS_D25_E2_LOWMID_HARMONIC_JET target_primes 166\`.

## BRC and native/source separation

**BRC COMPOSE_APPLIED** for this specific signed finite scalar: carrier \`(p,n,source in {original216,E2}, valuation, signed (6n+1), rational factorial unit, low-jet L/J, middle-crossing Z, carry C01, second jet F2, high-strip I)\`. Future operations are signed aggregation, p-adic division *after* divisibility, harmonic/difference transformation and finite WZ/CM comparison. A port-only collapse at first derivative is UNSAFE for the actual second digit: p373 has independently nonzero F2. This is external p-adic combinatorics and not an original X6/H0/B0 native operation.

Existing native original-class p373 benchmark \`awdawmip/enterprise-math#1559\` is **OPEN/PENDING_OWNER/NATIVE_NOT_EXECUTED** (same-class H0/B0 divided-power [X]U mod 139129; actual rank, semilinear Frobenius direction/eta, original odd Green/Hesse and kappa, independent validation). No native evaluator or authorized executor is claimed, no scalar surrogate is called a native benchmark. Source recovery \`awdawmip/kimi-query-bridge#6632\` shows no owned run; original dispatch \`#6633\` ended \`FAILED / UPSTREAM_CODE_REVIEW_REQUIRED\`; this run read originals and **did not replay** any refused mutation. No current legitimate Source CLAIM/OPEN/checkpoint/freeze/Result/review established. Historical protected staging remains separate. Formal activity \`REGISTER_PENDING / SYNC_DEBT\`, author-side Git persistence not Source admission.

## Next exact research operation

Find an authentic **joint** finite WZ/CM certificate that couples *all three* ports \`C01,F2,I\`, rather than hoping any of their independently nonzero residues vanish. Start by differentiating a parameterized finite 216/E.2 transformation **through the p² term**, carrying its boundary terms and source labels, and test candidate telescopers against the p19 and p373 nonzero-jet witnesses before claiming a uniform identity. Separately, native authorized owner must accept and actually execute original #1559; preserve its object/normalizations/precision unchanged.

**NOT proved:** infinite-class cancellation (G), original SECOND-DIGIT-LIFT, authenticated native H0/B0, formal Source task acceptance, independent review or Lean checker pass.
