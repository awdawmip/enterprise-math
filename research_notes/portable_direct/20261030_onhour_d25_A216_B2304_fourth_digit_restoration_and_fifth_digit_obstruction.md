# D25 / SECOND-DIGIT-LIFT — exact fourth-digit restoration and fifth-digit obstruction

Date: 2026-10-30 Asia/Hong_Kong. Status: AUTHOR-SIDE / PROVED FACTORIAL LEMMA / EXACT FIXED-PRIME COUNTEREXAMPLE / FINITE CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.

Research lane: chatgpt-research-onhour-enterprise-math-20260923; separate from maintenance chatgpt-hourly-enterprise-math-20260921. Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3, unchanged**. No current own native session, winning claim, execution run, formal checkpoint, Result or review receipt verified.

## Original object and proved prior

Let p>3 be prime and work over Z_(p). Define the exact original coefficients

\[
a_n=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}
=\frac{(2n)!(3n)!}{(n!)^5 216^n},\qquad
b_n=\frac{\binom{2n}{n}^{2}\binom{4n}{2n}}{2304^n}
=\frac{(4n)!}{(n!)^4 2304^n}.
\]

\[
A_p=\sum_{n=0}^{p-1}(6n+1)a_n,\quad
B_p=\sum_{n=0}^{p-1}(8n+1)b_n,\quad
D_p=A_p-2B_p+p\left(\frac{-3}{p}\right).
\]

Guo–Zudilin, *A q-microscope for supercongruences*, Advances in Mathematics 346 (2019), 329–358, equations (2),(3), proves that the two B truncations at p-1 and (p-1)/2 are each congruent to p(-3/p) mod p^3. See https://arxiv.org/abs/1803.01830. This was already used in the prior project note 20261030_onhour_d25_B2304_half_tail_regular_source_port.md; the B high-half aggregate cancellation is **prior art**, not a new proof in this turn.

## New general p-local block lemma

For p≥5 prime, 0≤q<p, 0≤r<p, put H_r=Σ_{j=1}^r 1/j mod p and Wilson quotient W_p=((p-1)!+1)/p mod p. Then

\[
\boxed{\frac{(qp+r)!}{p^q}\equiv
(-1)^q q!\,r!\left[1+qp(H_r-W_p)\right]\pmod{p^2}.}\tag{F}
\]

**Proof:** After extracting the q multiples of p, the exact product is

\[
q!\prod_{j=0}^{q-1}\prod_{s=1}^{p-1}(jp+s)
\prod_{s=1}^{r}(qp+s).
\]

Each completed block is (p-1)![1+jpH_{p-1}] mod p²; the elementary pairing s↔p-s gives H_{p-1}=0 mod p, so all these corrections vanish mod p². The last partial block is r!(1+qpH_r) mod p². Since (p-1)!=-1+pW_p, its q-th power is (-1)^q(1-qpW_p) mod p². Multiplication proves (F). All divisions use p-units.

## New fourth-digit three-port restoration

For p=6m+1≥7, define n0=(p+1)/2 and n3=floor((3p-1)/4). Keep the distinct signed ports

\[
A_>=\sum_{n=4m+1}^{p-1}(6n+1)a_n,\quad
B_{(2)}=\sum_{n=n0}^{n3}(8n+1)b_n,\quad
B_{(3)}=\sum_{n=n3+1}^{p-1}(8n+1)b_n.
\]

Pointwise, v_p(a_n)=3 in A_>, v_p(b_n)=2 in B_(2) and v_p(b_n)=3 in B_(3). By (F),

\[
\boxed{\frac{A_>}{p^3}\equiv
-2\sum_{n=4m+1}^{p-1}(6n+1)
\frac{(2n-p)!(3n-2p)!}{(n!)^5 216^n}\pmod p.}\tag{A3}
\]

Define a mod-p² finite sum whose denominators are p-units:

\[
U_{p,2}=\sum_{n=n0}^{n3}(8n+1)
\frac{2(4n-2p)!}{(n!)^4 2304^n}
[1+2p(H_{4n-2p}-W_p)]\pmod{p^2}.\tag{U2}
\]

By (F), B_(2)/p²=U_(p,2) mod p². The previously proved Guo–Zudilin half-tail cancellation and the pointwise p³ divisibility of B_(3) imply B_(2)=0 mod p³, so U_(p,2)=0 mod p; divide its representative 0,...,p²-1 by p. Thus

\[
\boxed{\frac{B_{(2)}}{p^3}\equiv \frac{U_{p,2}}p\pmod p,\quad
\frac{B_{(3)}}{p^3}\equiv
-6\sum_{n=n3+1}^{p-1}(8n+1)
\frac{(4n-3p)!}{(n!)^4 2304^n}\pmod p.}\tag{B3}
\]

This is one digit deeper than the previously completed B-REG (which is only a mod-p zero statement). It preserves signed original source labels/indexes and does not substitute for H0/B0.

For p=6m+1, let the previously established p³ minimal bridge be the exact rational expression

\[
D_p^{min}=p+\sum_{n=0}^{3m}\big[(6n+1)a_n-2(8n+1)b_n\big]
+\sum_{n=3m+1}^{4m}(6n+1)a_n.
\]

**Exact partition identity** (no congruence assumption):

\[
\boxed{D_p=D_p^{min}+A_>-2(B_{(2)}+B_{(3)}).}\tag{T}
\]

The older MIN-BRIDGE is correct modulo p³. Equations A3/U2/B3 restore the discarded residue when a fourth digit is requested. Direct integer-binomial source readings, each quotient mod p, are:

| p | Dmin/p³ | A>/p³ | B(2)/p³ | B(3)/p³ | resulting D/p³ mod p |
|---:|---:|---:|---:|---:|---:|
| 13 | 0 | 5 | 3 | 6 | 0 |
| 19 | 2 | 4 | 6 | 16 | 0 |
| 373 | 55 | 278 | 234 | 119 | 0 |

For p373, the discarded tail carries residue 278−2(234+119)=318 mod373, cancelling the reduced expression's 55. It is unsafe to promote the p³ minimal expression to p⁴ by deleting individual source ports.

## New rigorous fifth-digit obstruction

The formerly observed p⁴ bridge has a strict p⁵ obstruction in BOTH frozen target classes. Independently calculating the original integer binomial sums modulo 13^5=371293 gives

\[
A_{13}\equiv276835,\quad B_{13}\equiv195546,\quad
\boxed{D_{13}\equiv257049=9\cdot13^4\not\equiv0\pmod{13^5}.}
\]

For p=19,

\[
A_{19}\equiv603611,\quad B_{19}\equiv1865667,\quad
\boxed{D_{19}\equiv1824494=14\cdot19^4\not\equiv0\pmod{19^5}.}
\]

For the diagnostic p=373, the scalar quotient is D_373/373^4=174 mod373. Thus a universal p⁵ strengthening is **disproved by explicit fixed-prime exact arithmetic**. Neither p³ nor p⁴ is refuted.

The separate executable checker d25_bridge_digit5_boundary_guard_20261030.py ran using Python standard-library exact modular integers. It exhausted all 667 primes 5≤p<5000, including 166 frozen targets. In that **finite** range D_p is zero mod p⁴ at every prime, while D_p is zero mod p⁵ only for p=5,7. Those exhaustive finite observations are not a universal proof of p⁴ or a global classification of p⁵ exceptions. Two independent implementations (p-unit recurrences and original binomial sums) agree for 5,7,11,13,19,373. A3/U2/B3 were cross-checked against direct binomial source-port arithmetic at 45 primes p<500 congruent to 1 mod6 and again at p373: 46 cases.

## Exact continuation and native-obligation separation

Mother scientific hard target remains the original **D_p=0 mod p³ for all p≡13,19 mod24**. Continue by constructing a cross-model finite-hypergeometric/WZ or p-adic CM bridge at precisely that required precision using the already established B2304 result. Higher p⁴ or disproved p⁵ strengthening is not a required assumption. The signed three-port formulas are reusable if the chosen route needs fourth-digit error control.

The independent highest-priority native benchmark https://github.com/awdawmip/enterprise-math/issues/1559 was observed open on 2026-10-30 and has no confirmed owner. Its required original p373 H0/B0 divided-power [X]U mod139129, native module rank, real semilinear Frobenius/eta, odd signed Green/Hesse, κ, Δ−R and independent replication remain to be executed by a genuinely authorized native researcher. These scalar A/B computations are not a native experiment.

Control read in this run: Site research_authority_granted=false and write_relay_enabled=false; own checkpoint-list query returned ACCESS_DENIED. No recovery_status tool is exposed by this MCP surface. Do not infer a legal Source session/CLAIM/run or any Result admission. Prior pending requests should be reconciled by original IDs before any reissue. Work preserved in the repository is author-side scientific material only.
