# D25/LIFT R53–R54 — shifting the exact Green boundary removes the exceptional fourth-order pole

2026-10-27 (Asia/Hong_Kong). Portable author-derived research for the hourly TASK_RESEARCH lane `chatgpt-research-hourly-enterprise-math-20260923`; not a maintenance-lane or independent-review output. Mother objective `D25/LIFT/JT2` stays OPEN. Exact Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. **Frozen scientific Source pin:** `c47e13e4aba0e006366f989d6334d443f6333ae3` (distinct from mutable control HEAD).

Status: `AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY`. These results concern the original rational W/S sources and a freely varying, labelled two-source observer; they are not the original six-channel Hasse, H0/B0, native p=373 experiment, canonical Source checkpoint or a proof of W/S supercongruence.

## Exact input and observer scope

Reuse R47–R52 at their original proven scope, without recrediting them. For each integer `k>=0`,

\[
w_k=\frac{(6k+1)(2k)!(3k)!}{(k!)^5 216^k},\qquad
s_k=\frac{(8k+1)(4k)!}{(k!)^4 2304^k},
\]

\[
a_k=\frac{(6k+7)(2k+1)(3k+1)(3k+2)}{36(6k+1)(k+1)^3},\quad
b_k=\frac{(8k+9)(2k+1)(4k+1)(4k+3)}{288(8k+1)(k+1)^3}.
\]

Let `D_k=a_k-b_k`, so R47 gives

\[
D_k=\frac{(2k+1)P(k)}{288(k+1)^3(6k+1)(8k+1)},\quad
P(x)=2688x^4+6160x^3+4456x^2+1166x+85.
\]

Fix a prime `p>=13` with `p≡1 (mod 6)`, and put

\[
N=\left\lfloor\frac{3p-1}{4}\right\rfloor+1.
\]

Here `N+2<p`. For any **free** labelled `(U,V)∈Z_p^2`, write `A_j=w_j/w_1`, `B_j=s_j/s_1`, and define `d_j=A_jU-B_jV`. The unchanged factorial trajectory is the special choice `(U,V)=(w_1,s_1)=(7/18,3/32)`. For `j=N,N+1,N+2`, Legendre valuation and the original linear weights give

\[
v_p(A_j)=v_p(B_j)=3,\quad a_j,b_j\in\mathbb Z_p^\times
\quad(j=N,N+1).
\]

Write `A_{j,0}=A_j/p^3`, `B_{j,0}=B_j/p^3` (units) and `x_j=d_j/p^3`. The two-endpoint matrix is

\[
\binom{x_j}{x_{j+1}}=
M_j\binom UV,\quad
M_j=\begin{pmatrix} A_{j,0}&-B_{j,0}\\ a_jA_{j,0}&-b_jB_{j,0}\end{pmatrix},
\qquad \det M_j=A_{j,0}B_{j,0}D_j.
\tag{*}
\]

The source labels, signs, integer valuations and declared future readout `U-V` are all retained.

## R53 — universal one-rank desingularization, with an exact shifted Green formula

**Theorem R53.** For every target prime above,

\[
\boxed{v_p(D_{N+1})=0.}
\tag{53.1}
\]

Consequently, the **authentic shifted endpoints** `(d_{N+1},d_{N+2})` give a bijective integral observation interface

\[
\boxed{M_{N+1}\in\mathrm{GL}_2(\mathbb Z_p).}
\tag{53.2}
\]

Let `A^+=A_{N+1}`, `B^+=B_{N+1}`, `D^+=D_{N+1}`. The exact finite Green endpoint representation for the fixed low-rank observer `U-V` is

\[
\boxed{U-V=\widetilde Q_{N+1}d_{N+1}
              +\widetilde Q_{N+2}d_{N+2},}
\tag{53.3}
\]

\[
\widetilde Q_{N+1}
=\frac{a_{N+1}/B^+-b_{N+1}/A^+}{D^+},\qquad
\widetilde Q_{N+2}
=\frac{1/A^+-1/B^+}{D^+}.
\]

The pole order is exactly three in the vector sense:

\[
\boxed{v_p(\widetilde Q_{N+1}),v_p(\widetilde Q_{N+2})\ge-3,
\quad\min\{v_p(\widetilde Q_{N+1}),v_p(\widetilde Q_{N+2})\}=-3.}
\tag{53.4}
\]

This includes `p=139,199,277`, where the earlier, equally authentic but **different boundary choice** `(d_N,d_{N+1})` has an exact fourth-order pole (R51). Thus that fourth-order cost belongs to the specified boundary observer, not to every Green representation of `U-V`.

**Proof of (53.1).** The formula for `N` gives `N+1≡5/4 (mod p)` if `p≡1 (mod 4)` and `N+1≡7/4 (mod p)` if `p≡3 (mod 4)`. The denominator `288(k+1)^3(6k+1)(8k+1)` and factor `2k+1` in `D_k` are units at `k=N+1`: after replacing `k` by `5/4` or `7/4`, their possible prime divisors are among `3,5,7,11,17,23`, with `17,23≡5 (mod 6)`, and the other relevant candidates either below 13 or in the wrong mod-6 class.

The remaining numerator has exact rational values

\[
\boxed{P(5/4)=\frac{108395}{4}=\frac{5\cdot7\cdot19\cdot163}{4},}
\]
\[
\boxed{P(7/4)=\frac{295985}{4}=\frac{5\cdot59197}{4}.}
\]

When `p≡1 (mod 4)`, the prime factors `7,19,163` are all `3 (mod 4)` and `5<13`, so `p\nmid P(5/4)`. When `p≡3 (mod 4)`, both `5` and `59197` are primes `1 (mod 4)`, so `p\nmid P(7/4)`. Primality of 59197 follows by integer trial division through `floor(sqrt(59197))=243` and is included in the exact executable certificate. This proves `D_{N+1}` is a unit for every target prime, not only the finite test set.

The units `A_{N+1,0}`, `B_{N+1,0}` and (*) prove (53.2). Algebraic inversion yields (53.3): subtracting `b_{N+1}d_{N+1}` and `a_{N+1}d_{N+1}` from `d_{N+2}` recovers `D^+ A^+U` and `D^+ B^+V`. The row vector `(1,-1)` is primitive in `Z_p^2`; right-multiplication by `M_{N+1}^{-1}∈GL_2(Z_p)` preserves primitiveness. Hence `p^3(\widetilde Q_{N+1},\widetilde Q_{N+2})` is integral with at least one unit entry, giving (53.4). These coefficients are also the R50 finite-adjoint `c_1=1` Green boundary with horizon advanced one rank; no new input or source replacement is needed. QED.

## R54 — optimal rank-versus-precision trade-off at the three exceptional primes

**Theorem R54.** The normalized pair matrix `M_N` has Smith invariants over `Z_p`

\[
\boxed{\operatorname{SNF}(M_N)=\operatorname{diag}(1,p^{\lambda_p}),\qquad
\lambda_p=\begin{cases}1,&p\in\{139,199,277\},\\0,&\text{other target primes}.\end{cases}}
\tag{54.1}
\]

For an arbitrary precision target `t>=1` and all free inputs `(U,V)∈Z_p^2`:

* The pair `(x_N,x_{N+1})\bmod p^{t+\lambda_p}` determines the entire labelled source state modulo `p^t`. In the ordinary class `\lambda_p=0`, two consecutive normalized rank observations at precision `t` already suffice.
* At each exceptional prime, **two** normalized observations modulo `p^t` do **not** determine even the specific readout `U-V\bmod p^t`. One extra precision digit `t+1` is sufficient and necessary for universal recovery from these two ports.
* Alternatively, the **three** consecutive normalized observations `(x_N,x_{N+1},x_{N+2})\bmod p^t` recover the full state with *no extra digit*, since the last two form the unit matrix in (53.2). Three is the shortest consecutive window **starting at N** with this property at the exceptional primes.

In terms of unnormalized original endpoints, the exact resource trade is

\[
\boxed{
\text{two ranks }(N,N+1)\text{ at raw precision }p^{t+4}
\quad\text{or}\quad
\text{three ranks }(N,N+1,N+2)\text{ at raw precision }p^{t+3}.
}
\tag{54.2}
\]

**Proof.** The first row of `M_N` contains units `A_{N,0},B_{N,0}`; its determinant has `p`-valuation `\lambda_p` by R51. Standard elementary integral row/column operations give (54.1). Its inverse has entries with valuation at least `-\lambda_p`, proving sufficiency.

At an exceptional prime let `h=(B_{N,0},A_{N,0})∈Z_p^2`. Then `(M_Nh)_1=0` exactly and `(M_Nh)_2=D_NA_{N,0}B_{N,0}∈pZ_p`. R51's exact noncollision residues

\[
(A_{N,0},B_{N,0})\bmod p=
(130,8)_{139},\;(99,62)_{199},\;(131,81)_{277}
\]

imply `(1,-1)h=B_{N,0}-A_{N,0}` is a unit. Replacing any source state by itself plus `p^{t-1}h` keeps the first two observations identical modulo `p^t` but changes `U-V` modulo `p^t`. That is a concrete fiber witness for the necessity of the extra digit and of a third rank at fixed precision. R53 gives the length-three sufficiency, including all `t` and all possible free source pairs. Multiplying normalized observations by `p^3` yields (54.2). QED.

The optimality statement is **observer- and horizon-specific**: it concerns full free-source recovery and the `U-V` readout. The unchanged factorial trajectory has fixed `U,V`; its numerical samples illustrate the coordinate, not an extra unknown initial condition. Neither theorem creates a native Hasse/Frobenius certificate or rules out a larger WZ compensation using the original six channels.

## Exact executed checks and exceptional witnesses

The Python-stdlib verifier `20261027_hourly_d25_shifted_green_endpoints_r53_r54_check.py` was actually executed locally. It uses exact integer prime-unit factorial arithmetic, `Fraction` transitions and modular inverses; it checks the polynomial evaluations/factorizations, primality through 59197, and all **79 target primes `13<=p<1000`**. Assertions cover both original source recurrences, `D_N` exception classification in the finite domain, universal shifted `D_{N+1}` nonvanishing on that domain, the Green identity, full source recovery, and the R54 exceptional kernel witness. Its Git blob identity is `499a08b9f843870813c822e1a557df8225c63a8c`, matching the executed local file.

For the unchanged factorial trajectory, let `x_j=(w_j-s_j)/p^3\bmod p` and `\widetilde c_i=p^3\widetilde Q_i\bmod p`. The script returned:

| p | N | D_N mod p | D_(N+1) mod p | x_N | x_(N+1) | x_(N+2) | c_(N+1) | c_(N+2) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 139 | 105 | 0 | 134 | 100 | 102 | 70 | 48 | 94 |
| 199 | 150 | 0 | 94 | 70 | 36 | 180 | 15 | 167 |
| 277 | 208 | 0 | 94 | 27 | 42 | 195 | 209 | 44 |

Every row verifies `c_(N+1) x_(N+1)+c_(N+2)x_(N+2)=(w_1-s_1) mod p`. Generality of R53/R54 comes from the proofs, not the finite tests. No independent reviewer, formal proof assistant or original-class native p=373 experimental result was used.

## BRC, preservation and exact next scientific unit

`BRC COMPOSE_APPLIED` to the **signed labelled two-source carrier** `Z_p^2`, the actual diagonal evolution, and the future readout `U-V`. Invariant-factor/jet analysis identifies the precise fiber discarded by the first two normalized observations at `139,199,277`. A third authentic rank is an alternative to an extra digit, while both original W/S source identities remain distinct. These are external arithmetic coordinates; no unprovided X6-to-slice embedding, hidden third coordinate, or native-heartbeat time law is claimed. ACTIVE P000 and worldview remain untouched.

**New portable frontier:** R53 universal one-step shifted Green boundary and strict third-order pole; R54 exact two-port/three-port precision-window optimality, including labelled indistinguishability witnesses. **Do not repeat:** R47 recurrence, R49 general four-observation exception, R50 finite Green kernel, or R51/R52 particular-pole and divided-difference results as new work.

**Next exact unit:** use R53's *shifted authentic boundary* in the full R23 low-half `p^2` discrepancy and R36 PF-Green/Hasse setting. Determine which genuine finite Green bulk/source term is introduced when its boundary is moved by one rank; preserve R38–R42 W2/W3/S2/S3 valuations, six fixed `z=2` J/E channels, finite endpoints, positive infinity and Frobenius data. Seek source-labelled unchanged-input WZ cancellation or a narrow exact obstruction at `p=13,19,139,181,199,277,373`. The original H0/B0, `[X]U mod p^2`, `eta/kappa`, p=373 native experiment and independent Driver review remain to be executed under their actual permissions.

**Native control/identity boundary:** As observed in the own-lane recovery `awdawmip/kimi-query-bridge#6622` and exact continuation `#6623` at 2026-10-27 19:58 +08, there was no own winning CLAIM, authorized OPEN/run or unpublished upload. The historical Source-persisted checkpoint and last-claim predecessor differ, tracked under `awdawmip/enterprise-math#1558`. Preserve old service session/staging and request history; do not replay a rejected `continuation_prepare`. This author's GitHub note is not a Source `publish_checkpoint`, Result, review or Research-Activity registration; register its event on the next legal write/readback.
