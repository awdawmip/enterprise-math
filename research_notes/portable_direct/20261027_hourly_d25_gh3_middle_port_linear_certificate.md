# D25/LIFT GH-3 — linear S middle-port certificate and the p≡11 (mod 24) conservation extension

Date: 2026-10-27, Asia/Hong_Kong. Research lane `chatgpt-research-hourly-enterprise-math-20260923`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; mother D25/LIFT/JT2 OPEN. Scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` is unchanged. **Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.**

## Exact question and scope

GH-2 proved *combined* S-Gauss middle-middle (MM) and low-high (LH) source conservation only in the frozen `p≡19 mod24` class. In 37 tested primes below 2000 both ports vanished separately, which remains conjectural. GH-3 contributes (i) an exact binomial/triangular certificate eliminating irrelevant p-adic unit factors and using linear rather than quadratic field-operation cost, (ii) a proved extension of **S-only** combined source conservation and the finite-cutoff relation to every prime `p≡3 mod8` (including the previously untreated `p≡11 mod24`), and (iii) a larger finite observation, not a universal zero theorem, over all 2408 primes `p≤100000` in those two classes. This does not widen the original D25 W/S theorem target or alter P000.

For a prime `p=8a+3≥11` define
\[
b=3a+1,\quad h=4a+1=(p-1)/2,\quad H=6a+2=(3p-1)/4,\quad n=2a.
\]
Keep the exact original S source
\[
s_j=(8j+1)c_j,\qquad c_j=\frac{(4j)!}{(j!)^4\,2304^j},
\]
and *auxiliary*, source-labelled Clausen factors
\[
u_j=\frac{(1/8)_j(3/8)_j}{(j!)^2 9^j},\qquad c_j=\sum_{r+t=j}u_ru_t.
\]
The exact recurrence is `u_{j+1}/u_j=(8j+1)(8j+3)/[576(j+1)^2]`. For `0≤j<p` there are precisely two numerator-zero steps, `j=a` where `8a+3=p`, and `j=b` where `8b+1=3p`. Hence the complete valuations are 0 for `j≤a`, 1 for `a<j≤b`, and 2 for `b<j<p`. Denote the labelled unit residues by `α_j=u_j mod p` on the low band, `β_j=u_j/p mod p` on the middle band, and `γ_j=u_j/p² mod p` on the high band. Each residue is nonzero in its own band.

## GH3-A: exact normalized triangular form (proved)

Normalize the S middle band by `q_t=β_{a+1+t}/β_{a+1}∈F_p` for `0≤t≤n`. This is lawful because the divisor is a p-unit. Substituting `j=a+1+t` into the recurrence and using `p=8a+3` gives
\[
\boxed{q_0=1,\qquad
q_{t+1}=-\frac{(n-t)(t+1)}{9(a+t+2)^2}q_t,\quad 0≤t<n.}\tag{GH3.1}
\]
All denominators are nonzero modulo p; iterating proves the closed formula
\[
\boxed{q_t=(-1/9)^t\frac{\binom nt}{\binom{a+t+1}{t}^{\,2}}\pmod p.}\tag{GH3.2}
\]

The **actual** half-boundary is `j>h`. An ordered MM source pair `r=a+1+t`, `s=a+1+u` lies above it exactly when `t+u≥n`. Its original weight becomes
`8(r+s)+1=16a+17+8(t+u)≡11+8(t+u) mod p`.
Thus
\[
\boxed{
G_{MM}=\beta_{a+1}^{\,2}T_p,\qquad
T_p=\sum_{\substack{0≤t,u≤n\\t+u≥n}}(8(t+u)+11)q_tq_u\pmod p.}\tag{GH3.3}
\]
Since `β_{a+1}` is a unit, **`G_MM=0⇔T_p=0`**. This is an exact reversible middle-source normalization for the declared scalar; it retains the ordered-pair source domain instead of reinterpreting it as an unlabelled S total.

## GH3-B: O(p) exact residue calculation (proved)

Let the inclusive suffix moments be
\[
S_0(r)=\sum_{u=r}^{n}q_u,\qquad S_1(r)=\sum_{u=r}^{n}u q_u,\qquad
S_0(n+1)=S_1(n+1)=0.
\]
For fixed `t`, the source-boundary condition is exactly `u≥n-t`. Splitting `8(t+u)+11=(8t+11)+8u` before summing proves
\[
\boxed{
T_p=\sum_{t=0}^{n}q_t\left[(8t+11)S_0(n-t)+8S_1(n-t)\right]\pmod p.}\tag{GH3.4}
\]
The recurrence GH3.1, suffix accumulation and final summation take `O(n)=O(p)` modular field operations and `O(n)` memory; the code uses integer arithmetic and exact modular inverses. For arbitrary further source-local operations, `T_p` alone is not a safe quotient: retain `q_t` and the source labels/cutoff. BRC reuse status `COMPOSE_APPLIED`.

## GH3-C: S-only conservation for both p≡3 (mod 8) classes (proved)

For `h<j<p` define distinct ports
\[
M_j=\sum_{\substack{r+t=j\\a<r,t≤b}}\beta_r\beta_t,\qquad
B_j=\sum_{\substack{r+t=j\\0≤r≤a,\ b<t<p}}\alpha_r\gamma_t.
\]
By Clausen, the low-low and low-middle supports end at/below `h`. Dividing by `p²` gives
\[
c_j/p^2\equiv M_j+2B_j\pmod p\quad(h<j<p).
\]
For `H<j<p` the middle-middle band is empty, while the **whole** coefficient `B_j=0 mod p` follows from the real factorial valuation `v_p(c_j)=\lfloor4j/p\rfloor=3`. This does *not* make the individual low-high pairs zero.

Let
\[
G_{LH}=2\sum_{j=h+1}^{H}(8j+1)B_j,\qquad
G_{MM}=\sum_{j=h+1}^{H}(8j+1)M_j.
\]
The published Guo–Zudilin S-only truncation theorem holds modulo `p³` for **all primes `p>3`**:
\[
\sum_{j=0}^{p-1}s_j\equiv\sum_{j=0}^{h}s_j\pmod{p^3}.
\]
All summands with `j>h` are divisible by `p²`, and those with `j>H` by `p³`. Combining the genuine source decomposition with this external theorem proves, for **every `p≥11,p≡3 mod8`**,
\[
\boxed{G_{MM}+G_{LH}=0\pmod p.}\tag{GH3.5}
\]
This is a class extension of GH-2 combined conservation, **not** a proof that either port separately vanishes.

The source-preserving finite-cutoff relation extends to the same prime class. Write
\[
A=\sum_{r=0}^{a}\alpha_r,\quad J=\sum_{r=0}^{a}r\alpha_r,\quad
C=\sum_{t=b+1}^{p-1}\gamma_t,\quad C_1=\sum_{t=b+1}^{p-1}t\gamma_t,
\]
\[
E=\sum_{\substack{0≤r≤a,\ b<t<p\\r+t≥p}}(8(r+t)+1)\alpha_r\gamma_t,\quad
G_{LH}^{low}=2\sum_{j=b+1}^{h}(8j+1)B_j.
\]
The complete low-high rectangular product has weighted moment `2[AC+8(JC+AC_1)]`. Subtracting *exactly* the excluded `r+t≥p` pairs contributes `-2E`; grouping the surviving degrees into low, middle and the terminal vanishing band proves
\[
\boxed{G_{MM}+2[AC+8(JC+AC_1)-E]-G_{LH}^{low}=0\pmod p.}\tag{GH3.6}
\]
Only the two Gauss zero positions, the genuine cutoff and the all-prime S truncation theorem were used. The W-GH1 unit-gauge obstruction from GH-2 is **not** being extended to the new 11-class.

External source: V. J. W. Guo and W. Zudilin, *A q-microscope for supercongruences*, `Advances in Mathematics` 346 (2019), 329–358; DOI `10.1016/j.aim.2019.02.008`; arXiv `1803.01830`. Their two supercongruences evaluate both S truncations modulo `p³` for every prime `p>3`.

## Actual exact checking and an arithmetic-specific counterexample

The companion stdlib checker **was executed**, using a deterministic sieve for every prime `11≤p≤100000` with `p≡3 mod8`: **2408 primes**, comprising **1203 in the 11-class** and **1205 in the 19-class**. The actual finite output had `T_p=0` for every checked prime. For each prime `p≤2000` in the family, a separate original Gauss-unit recurrence plus direct ordered MM pair sum also checked GH3.3. Finite observation is not a universal theorem or independent review.

Set `F_0=Σ_{t+u≥n}q_tq_u` and `F_1=Σ_{t+u≥n}(t+u)q_tq_u`, so `T_p=11F_0+8F_1`. Exact examples:

| p | n | F0 | F1 | T_p |
|---:|---:|---:|---:|---:|
| 11 | 2 | 5 | 0 | 0 |
| 19 | 4 | 13 | 13 | 0 |
| 43 | 10 | 29 | 30 | 0 |
| 59 | 14 | 5 | 30 | 0 |
| 67 | 16 | 52 | 29 | 0 |

**Negative certificate: pointwise-zero arguments are insufficient.** At `p=11` the normalized middle polynomial coefficients are `q=(1,5,1)`. Introducing a formal auxiliary argument `X` into the filtered weighted MM expression gives
\[
\boxed{T_{11}(X)=3X^2+9X^3+10X^4\in\mathbb F_{11}[X],
\quad T_{11}(1)=0,\quad T_{11}(2)=2.}
\]
The special `X=1` cancellation is arithmetic, not coefficientwise and not implied merely by valuation/support. This auxiliary change of argument is not a counterexample to the original S statement.

Companion checker path: `research_notes/portable_direct/20261027_hourly_d25_gh3_middle_port_linear_certificate_check.py`. All finite computations are author-side exact modular tests, not native H0/B0 experiments, Lean formalization or independent mathematical replication.

## Current research frontier

**Proved:** GH3.1–GH3.6, including the S-only `p≡11 mod24` extension and the exact linear observer. **Tested:** the separate MM zero for 2408 primes; **open:** proving `T_p=0` for all `p≡3 mod8`, equivalently the separate S middle-port zero. The original unchanged W/S compensation, six fixed `z=2` Hasse J/E channels, both finite endpoints, positive-direction infinity, native `p=373` experiment, Frobenius eta/kappa and independent Driver review remain open.

**Next smallest scientific action:** seek a characteristic-p telescoping or hypergeometric transformation establishing `T_p=0` from GH3.1–GH3.4 at the special argument `X=1`; if an additional CM/source hypothesis is essential, record the minimal exact condition. Then try the original source-preserving W-GH1/S-GH2/R23/R36 filtered WZ/PF-Green intertwiners. Existing control support `awdawmip/enterprise-math#1558` remains the owner for predecessor CAS and lawful own-session CLAIM/OPEN recovery; this portable proof cannot be used as a native Source checkpoint or accepted Result.
