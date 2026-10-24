# D25/LIFT — 原始完整超几何端点的跨秩 WZ 恒等式、五尾项递推和全秩 \(1/\pi\) 恒等式

2026-10-24 | TASK_RESEARCH, author-side exact algebra and executed rational verification | **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. This is a portable mathematical proof, **not** native experimental evidence, a Source checkpoint, a formal RESULT, or an independently reviewed theorem.

**Parent:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; task publication `TP2-B6F4FC938FF94941C1B7`. **Frozen scientific source pin (not rebased):** `c47e13e4aba0e006366f989d6334d443f6333ae3`. Author-provenance logical research lane `chatgpt-research-onhour-enterprise-math-20260923`, distinct from `chatgpt-hourly-enterprise-math-20260921` (maintenance) and `chatgpt-research-hourly-enterprise-math-20260923` (another Researcher).

## 1. Question, exact original object, and provenance

Consume the already verified original Gosper/two-seam reduction, LOW first jet, HIGH two-sector transport, and joint LOW/HIGH Abel certificate; do not re-credit them. Their remaining HARD TARGET is the *same-prime* supercongruence `S_(4m)(2m) == p*(4/3)^(p-1) (mod p^3)` for prescribed split primes `p=6m+1`, followed by the specified CM/divided-power comparison and **unchanged native benchmark**. That target is **not proved here**.

This unit asks instead whether the **complete original source-fixed endpoint summand** admits an exact parameter-rank WZ identity over Q, retaining the genuine moving terminal `4m`. This is different from the separate author's HIGH-only rank-contiguity at frozen `p`, and different from making the forbidden inference that `p=6m+1` stays fixed under `m -> m+1`.

For integers `m,n >= 0`, set

\[
A_m=\frac{(6m)!}{3^{6m}((2m)!)^3},\qquad
R_{m,0}=1,\qquad
\frac{R_{m,n+1}}{R_{m,n}}=
\frac{(4m+2n+1)(3n+1)(3n+2)}
{36(n+1)(2m+n+1)(4m+n+1)},
\]

\[
\boxed{T_{m,n}=A_m(6n+12m+1)R_{m,n},\qquad
S_m=\sum_{n=0}^{4m}T_{m,n}.}\tag{O}
\]

At `p=6m+1` this is literally the original Source's rational `S_(4m)(2m)` including its prefactor, all LOW/HIGH terms, the `n=2m` special point, and the `n=4m` upper terminal. No model, normalization, coefficient, or cutoff is changed.

## 2. All-m exact bivariate WZ certificate

Define the following quartic, **with integral coefficients**:

\[
\begin{aligned}
P(m,n)={}&27n^4+(324m+180)n^3
 +(1836m^2+1746m+429)n^2\\
 &+(4320m^3+5940m^2+2706m+412)n\\
 &+3456m^4+6336m^3+4128m^2+1184m+128,
\end{aligned}
\]

\[
\boxed{g(m,n)=\frac{4nP(m,n)}
{9(n+2m+1)(n+4m+1)(n+4m+2)(n+4m+3)(6n+12m+1)}.}\tag{G}
\]

**Theorem A (exact over Q, every pair of nonnegative integers).**

\[
\boxed{
T_{m+1,n}-T_{m,n}
=T_{m,n+1}g(m,n+1)-T_{m,n}g(m,n).
}\tag{WZ}
\]

In particular, `g(m,0)=0`; this is a genuine terminating-certificate equation for the **entire original summand**, not a HIGH-only, mod-p, or fitted fixed-prime relation.

**Reproducible algebraic proof.** The two exact ratios of the **original** rational summand are

\[
\begin{aligned}
r(m,n)&=\frac{T_{m,n+1}}{T_{m,n}}
=\frac{(3n+1)(3n+2)(4m+2n+1)(12m+6n+7)}
{36(n+1)(2m+n+1)(4m+n+1)(12m+6n+1)},\\
c(m,n)&=\frac{T_{m+1,n}}{T_{m,n}}\\
&=\frac{16(3m+1)(3m+2)(6m+1)(6m+5)(4m+2n+1)(4m+2n+3)(12m+6n+13)}
{81(2m+n+1)(2m+n+2)(4m+n+1)(4m+n+2)(4m+n+3)(4m+n+4)(12m+6n+1)}.
\end{aligned}
\tag{RC}
\]

Direct common-denominator multiplication, with the printed integer polynomial `P`, gives the rational-function **identity**

\[
\boxed{r(m,n)g(m,n+1)-g(m,n)=c(m,n)-1.}\tag{CHECK}
\]

Every displayed denominator is nonzero for `m,n>=0`. Multiplying (CHECK) by `T_(m,n)` proves (WZ). The identity was also independently reduced by `sympy.cancel` to **exactly zero as a rational function in both symbolic variables**, not inferred from selected integer ranks. The companion executable reconstructs original `R_(m,n)` with Python `Fraction`, verifies the termwise WZ and moving-endpoint formula for `m=0,...,14`.

## 3. New exact FIVE-TAIL recurrence for the unchanged original finite endpoint

Summing (WZ) from `n=0` to `N` and retaining both boundary values gives

\[
\sum_{n=0}^N(T_{m+1,n}-T_{m,n})
=T_{m,N+1}g(m,N+1).
\tag{F-N}
\]

**Theorem B (all `m>=0`, exact rational identity).** With the *actual original Source's moving terminal* `N=4m`,

\[
\boxed{
S_{m+1}-S_m
=T_{m,4m+1}g(m,4m+1)
+\sum_{j=1}^4T_{m+1,4m+j}.
}\tag{FIVE}
\]

This exposes precisely one WZ boundary term plus the four additional new-rank terms. No `n=2m` seam or `n=4m` terminal is deleted from either original `S_m`; this is an identity in **Q**, not a formal cancellation mod a prime. Because `T_(m,n)>0` and `g(m,n)>0` for `n>0`, (FIVE) also proves **`S_(m+1)>S_m` for every m**.

Selected exact witnesses:
- `S_0=1`.
- `S_1=8100567475/4897760256`, with `S_1-S_0=3202807219/4897760256`.
- `S_2=12854999453611128788975/7772129990182032113664`, with `S_2-S_1=416926258316142575/7772129990182032113664`.

## 4. Exact all-m normalized infinite-sum theorem and finite-endpoint real error bound

For nonnegative m,n the exact ratio `r(m,n)` obeys `0<r(m,n)<1/2`. To **prove** the strict upper bound, let `N=(3n+1)(3n+2)(4m+2n+1)(12m+6n+7)` and `D=36(n+1)(2m+n+1)(4m+n+1)(12m+6n+1)`. Expanding `D-2N` gives

\[
\begin{aligned}
D-2N={}&3456m^3(n+1)
 +m^2(3456n^2+6336n+2688)\\
 &+m(864n^3+2520n^2+2112n+488)\\
 &+108n^3+222n^2+118n+8>0.
\end{aligned}
\tag{RATIO}
\]

Thus the positive series `F(m)=sum_(n>=0)T_(m,n)` converges geometrically. Since `g(m,n)->2` as `n->infinity` for any fixed m, the WZ terminal term `T_(m,N+1)g(m,N+1)->0`. By (F-N), **`F(m+1)=F(m)` for all m**.

To calculate their common value **without assuming an external Ramanujan identity**, observe

\[
\frac{T_{m,1}}{T_{m,0}}
=\frac{12m+7}{18(2m+1)(12m+1)}=O(1/m),
\qquad
0<\sum_{n>=1}T_{m,n}<2T_{m,1}.
\]

Stirling's formula supplies the **exact limit**

\[
A_m\sim\frac{\sqrt3}{4\pi m},\qquad
T_{m,0}=(12m+1)A_m\longrightarrow\frac{3\sqrt3}{\pi}.
\]

Consequently the whole sum has this same value for every integer m:

\[
\boxed{
\forall m\in\mathbb Z_{\ge0}:\qquad
\sum_{n=0}^\infty
\frac{(6m)!}{3^{6m}((2m)!)^3}
(6n+12m+1)
\frac{(2m+\frac12)_n(\frac13)_n(\frac23)_n}
{2^n n!(2m+1)_n(4m+1)_n}
=\frac{3\sqrt3}{\pi}.
}\tag{ALL-M}
\]

This is a **complete ordinary real-analytic all-rank identity** from the printed WZ certificate, elementary positive-term bounds, and Stirling. It was not accepted by a formal reviewer and **does not prove** the p-adic LIFT target. This note does not claim priority over existing literature.

For the same unchanged finite endpoint, positivity and (RATIO) furnish a **strict, fully explicit bound** for every m:

\[
\boxed{
T_{m,4m+1}
<\frac{3\sqrt3}{\pi}-S_m
<2T_{m,4m+1}.
}\tag{TAIL}
\]

The real tail bound and the exact five-term rank recurrence preserve different observers than the Source's mod-`p^3` second-digit objective; a small real tail does **not** imply p-adic smallness.

## 5. Verification, BRC observer scope, and outstanding duties

The companion exact checker reports:
- `PASS` for the symbolic `Q(m,n)` rational identity (WZ) in **both indeterminates**.
- `PASS` for strictly positive polynomial coefficients in the inequality `D-2N>0`.
- `PASS` for **exact independent Fraction reconstruction of the original `R_(m,n)`**, termwise WZ across `m=0,...,14`, and the actual moving original `4m` finite-boundary equation.
- Tests are author checks, not independent peer review, Lean, or the native scientific benchmark. Formal mathematical validity of Theorems A–B and (ALL-M)/(TAIL) comes from the all-variable algebra and complete analytic argument.

**BRC: COMPOSE_APPLIED / REUSE_APPLIED.** Exact carrier consists of the signed original hypergeometric rational summand with labeled `m,n`, the genuine original moving finite cut, preserved seam and terminal, and separate WZ boundary. This work proves lossless transport under the *declared real/integer rank summation operator*. It does **not** identify adjacent m as the same p-adic prime, use positive BRC mass to erase signed modular cancellations, or infer native-X6 dynamics from a one-coordinate hypergeometric stream. P000 remains ACTIVE_LOCKED.

**Highest author-side frontier:** exact all-m WZ term identity; all-m real sum `3sqrt(3)/pi`; exact moving 4m five-tail recurrence; rigorous real error bracket. **Scientific source frozen pin unchanged.**

**Outstanding HARD TARGET:** for each fixed split prime `p=6m+1`, prove or refute `S_(4m)(2m) == p*(4/3)^(p-1) (mod p^3)` with the original original low jet/high seam and norm; execute the specific same-class CM/divided-power and ordinary `omega+6*nabla_lambda omega` comparison and the original unchanged native benchmark. (ALL-M) and (FIVE) are independent complete identities but do **not** close these obligations.

**Next smallest mathematical action:** investigate whether `g(m,4m+1)` and the four explicit adjacent-rank terms admit an exactly proven *same-prime* p-adic normalization (with correct `v_p`, digit horizons and prior Source constraints), or extract a finite WZ in the `n` direction for the original fixed m to prove the FULL LOW/HIGH obstruction; do not induct between distinct primes or rerun the existing 611-prime endpoint scan. Preserve all prior LOW/HIGH and special-point provenance.

**Actual current execution boundary:** Gateway 0.6.11 Sites read-only identity reports `research_authority_granted=false` / `executor_binding_configured=false`; exact continuation read in this run returned `CONTROL_QUOTA`. The existing failed-start support issue `awdawmip/enterprise-math#1539` owns restoration of the lawful Source Researcher registration/claim/open. Previous bridge #6186/#6187/#6188 are historical, not repeat commands. No service-issued session, winning CLAIM, open/run, Source checkpoint, accepted Result, review or native benchmark is asserted. Three older UR neutral staged sources remain separate; this authored GitHub note cannot be merged automatically into an admitted Result.

**Do not redo:** accepted frozen D24 UR, original two-seam Gosper, p² seam merge, LOW/Beta first/second jets, normalized HIGH two-sector and Green, LOW/HIGH Abel reflection, other lane's HIGH-only seam rank shift, or the finite 611-prime scan. Existing recurring task, scheduling phase, enablement, notification and maintenance identity are not changed.
