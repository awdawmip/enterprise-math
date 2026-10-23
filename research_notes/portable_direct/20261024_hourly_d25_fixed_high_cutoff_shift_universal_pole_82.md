# D25/LIFT — Source-fixed HIGH cutoff shift: universal nonzero p-adic pole −82

2026-10-24 | TASK_RESEARCH | **TWO NEW ALL-TARGET-PRIME THEOREMS / ELEMENTARY FACTORIAL CERTIFICATE / EXACT AUTHOR SELF-CHECK / UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

Mother Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Actual author research logical lane chatgpt-research-hourly-enterprise-math-20260923, distinct from maintenance. No native claim, authorized run, Source checkpoint, Result, review or math admission is asserted.

Inherited mathematical inputs, not newly credited: the original fixed HIGH forcing with both sectors from research_notes/portable_direct/20261024_onhour_d25_regular_low_jet_high_unit_two_sector_certificate.md, and the independently derived two generating-polynomial cutoff shifts from research_notes/portable_direct/20261024_hourly_d25_source_fixed_high_beta_euler_transport.md. The present **new** unit derives the *exact source-fixed p-pole of their combination*, proves an all-prime binomial identity and proves the pole is never zero.

## 1. Fixed-source rational carrier and the correct cutoff observer

For integer m>=1 let p=6m+1 be prime. Preserve the original, fixed-weight HIGH scalar

\[
Z_m=\sum_{s=1}^{m-1}a_{m,s}k_s^A-\frac1{24}\sum_{s=1}^{2m-1}c_{m,s}k_s^B,
\]

\[
a_{m,s}=2^{m-s}\frac{(2m)!(s-1)!}{(m+s)!(m-1)!},\qquad
c_{m,s}=2^{1-s}\frac{(2m+1)!(m+s-1)!}{m!(2m+s)!},
\]

\[
k_s^A=\frac{4(1-2s)(3s+1)}{(2s+1)(6s+1)},\qquad
k_s^B=\frac{(2-3s)(6s+1)}{3s(3s+1)}.
\]

**Keep p=6m+1 fixed** when evaluating \(Z_{m+1}-Z_m\). This is an auxiliary cutoff/rank operation on the same original Source-imposed rational port family, NOT a claim that the new m+1 expression is already the original D25 forcing at p'=6(m+1)+1. The original n=2m seam and n=4m terminal are preserved in the older D25 endpoint identity, not freely redefined by this cutoff.

The inherited **exact Q coefficient transports** of the old s branches are

\[
\rho^A_{m,s}=\frac{a_{m+1,s}}{a_{m,s}}=\frac{4(2m+1)(m+1)}{m(m+s+1)}\quad(1\le s\le m-1),
\]

\[
\rho^B_{m,s}=\frac{c_{m+1,s}}{c_{m,s}}=\frac{2(2m+3)(m+s)}{(2m+s+1)(2m+s+2)}\quad(1\le s\le2m-1).
\]

New endpoints are
\[
\gamma_m=a_{m+1,m}=\frac{4(m+1)}m,\qquad
\eta_m=c_{m+1,2m}=\frac{(2m+3)!(3m)!}{2^{2m-1}(m+1)!(4m+2)!},
\qquad
\theta_m=c_{m+1,2m+1}=\frac{3m+1}{2(4m+3)}\eta_m.
\]

Hence the exact rational identity, without erasing either source-fixed sector, is

\[
\begin{aligned}
Z_{m+1}-Z_m={}&
\sum_{s=1}^{m-1}(\rho^A_{m,s}-1)a_{m,s}k_s^A
-\frac1{24}\sum_{s=1}^{2m-1}(\rho^B_{m,s}-1)c_{m,s}k_s^B\\
&+\gamma_m k_m^A
-\frac{\eta_m}{24}k_{2m}^B
-\frac{\theta_m}{24}k_{2m+1}^B .
\end{aligned}\tag{SHIFT}
\]

## 2. Theorem A: the p^{-1} residue is confined to two Source-fixed boundary ports

**Theorem A.** For every prime p=6m+1>=7, \(Z_m\in\mathbb Z_{(p)}\), \(v_p(Z_{m+1})\ge-1\), and

\[
\boxed{p(Z_{m+1}-Z_m)\equiv -80-\frac{\eta_m}{8}\pmod p.}\tag{P-A}
\]

**Proof.** In both old-s sums, original a/c rational coefficients, k-denominators and the rho denominators are all p-units (for the stated source-fixed ranges). Thus their contributions are p-integral.

The new A-boundary hits **exactly** the \(6s+1=p\) pole:

\[
k_m^A=\frac{4(1-2m)(3m+1)}{(2m+1)p},
\qquad p k_m^A\equiv4\pmod p,
\qquad\gamma_m\equiv-20\pmod p.
\]

So its p^{-1} residue is \(4(-20)=-80\).

The first new B-boundary hits the **different** \(3s+1=p\) pole:

\[
k_{2m}^B=\frac{(3-p)(2p-1)}{(p-1)p},
\qquad p k_{2m}^B\equiv3\pmod p.
\]

Its source-fixed coefficient \(-\eta_m/24\) contributes \(-\eta_m/8\).

The last B endpoint is **not** another 1/p pole:
\[
k_{2m+1}^B=-\frac{p(2p+5)}{(p+2)(p+3)}.
\]
For m>=2, theta is a p-unit, so theta times this last k lies in \(p\mathbb Z_{(p)}\). At the *exceptional forward cutoff* p=7,m=1, \(\theta_1=1/14\) is not a p-unit, but \(k_3^B=-133/90\), giving \(\theta_1k_3^B=-19/180\in\mathbb Z_{(7)}\). In all cases this endpoint is p-integral and cannot contribute to the principal pole. Multiply the exact SHIFT by p and reduce to obtain (P-A). QED.

## 3. Theorem B: a new elementary all-target-prime factorial/binomial congruence

**Theorem B.** For **every** prime p=6m+1>=7,

\[
\boxed{\eta_m\equiv16\pmod p.}\tag{ETA-16}
\]

**Proof.** Directly simplify the exact factorial ratio:

\[
\eta_m=\frac{2(2m+3)}{(4m+1)4^m}\,Q_m,
\qquad
Q_m=\frac{(2m)!(3m)!}{m!(4m)!}
=\frac{\binom{3m}{m}}{\binom{4m}{2m}}.
\tag{Q}
\]

Reflect the m factors in the denominator of \(Q_m\) against p=6m+1:
\(p-(3m+j)=3m+1-j\). Therefore in \(\mathbb F_p\),

\[
Q_m=
\frac{\prod_{j=m+1}^{2m}j}{\prod_{j=3m+1}^{4m}j}
\equiv(-1)^m\frac{((2m)!)^2}{m!(3m)!}
=(-1)^m\frac{\binom{2m}{m}}{\binom{3m}{m}}.
\tag{REFLECT}
\]

Since the **actual integer** \(3m=(p-1)/2\) reduces to \(-1/2\) modulo p,

\[
\binom{3m}{m}
\equiv\binom{-1/2}{m}
=(-1)^m\frac{(1/2)_m}{m!}
=(-1)^m\frac{\binom{2m}{m}}{4^m}\pmod p.
\tag{HALF}
\]

All denominators are p-units for m>=1. Combining these identities proves the extra universal finite-field factorial relation

\[
\boxed{Q_m=\frac{\binom{3m}{m}}{\binom{4m}{2m}}\equiv4^m\pmod p.}\tag{Q4}
\]

Insert Q4 into the **exact** expression for eta, then use m≡−1/6:

\[
\eta_m\equiv\frac{2(2m+3)}{4m+1}
\equiv\frac{2(8/3)}{1/3}=16\pmod p.
\]

There are **no** extra small-prime exceptions: \(16\bmod7=2\) and \(16\bmod13=3\), agreeing with their true finite-field residues. This proves (ETA-16). QED.

## 4. Sharp all-prime fixed-HIGH obstruction — no target exception

Theorems A and B yield, for the **fixed original source-defined rational HIGH coefficients**,

\[
\boxed{p(Z_{m+1}-Z_m)\equiv-82\pmod p
\quad\text{for all primes }p=6m+1\ge7.}\tag{POLE-82}
\]

Since \(82=2\cdot41\), and neither prime divisor of 82 lies in the class p≡1 mod6,

\[
\boxed{v_p(Z_{m+1}-Z_m)=-1\quad\text{for every target prime}.}\tag{SHARP}
\]

This is a **uniform nonzero boundary-pole theorem**, not a counterexample to the original LIFT. A prospective finite-difference/WZ elimination of the *full fixed* D25 forcing must supply genuine counterbalancing contributions with principal p-residue \(+82\) if it includes this HIGH cutoff operation. No arbitrary auxiliary coefficient can be fitted to remove the source-fixed ports.

The original \(B_m=(2m-1)!(2m)!/(4m)!\) is p-integral and a unit. With this **old** normalization held fixed,

\[
pB_m(Z_{m+1}-Z_m)\equiv-82B_m\pmod p.
\tag{BPOLE}
\]

This is **not** a formula for \(B_{m+1}Z_{m+1}-B_mZ_m\); changing the normalization needs a separate proof. At p=7, \(B_2\) is not p-integral, giving a further specific reason not to conflate these observers.

## 5. Exact checks, provenance and next original research action

An independent Python Fraction calculation built *all* old and new original finite sums from factorials and rational k weights, then compared \(p(Z_{m+1}-Z_m)\bmod p\), eta mod p, and the claimed \(-82\) residual. All **80 primes p=6m+1 below 1000** passed. Sample tuples \(p:(\eta_m\bmod p,\ p(Z_{m+1}-Z_m)\bmod p)\) were

\[
7:(2,2),\quad13:(3,9),\quad19:(16,13),\quad
31:(16,11),\quad67:(16,52),\quad
211:(16,129),\quad613:(16,531).
\]

These are author-side finite checks; the infinite-prime assertion derives from the exact SHIFT and the elementary full modular proof, **not** from numerical extrapolation. At p=211 the previously proved adjustable auxiliary HIGH seam pair has vanishing residue, but this **different source-fixed HIGH cutoff observer** has residue 129 !=0. Their coefficients, carriers and operations are distinct, so the two conclusions are compatible.

Typed BRC reuse: **COMPOSE_APPLIED / REUSE_APPLIED**, not execution of native BRC. Carrier retains separately the A and B sector branch labels, signed rational weights, p-valuations, original \(-1/24\), two indispensable new poles s=m and s=2m, and the subtle s=2m+1 terminal. The observer is the fixed-p cutoff shift, and the proven residue captures information erased by naive summed or generic-k compression. No positive mass or full native X6 theorem is asserted.

**Next smallest unfinished original question:** combine the *unchanged Source-fixed* LOW first jet and its m-transport with this now-exact HIGH p-pole, the \((A-G+B)/p\) term, n=2m and n=4m seam/terminal, and genuine Fermat/harmonic correction. Construct a terminating finite-difference/WZ certificate for the actual D25 finite obstruction mod p, or isolate a genuine counterexample; **do not** equate the auxiliary cutoff for m+1 to an original different-prime forcing. The native D25 Source additionally still lacks the exact source-specific CM/divided-power class, semilinear map direction, omega+6 nabla_lambda omega comparison, leading normalization and same-class bridge. This proof supplies none of those native inputs.

Evidence classification **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**; parent LIFT OPEN; frozen science Source pin unchanged; same logical Research lane, existing support issue #1558 and original automation schedule/notifications preserved.
