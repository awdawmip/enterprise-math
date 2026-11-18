# R749SUW — Uniform fixed-offset exact square-root theorem for the named WBRC two-Port observer

Date: 2026-11-18, Asia/Shanghai. Status: `AUTHOR_EXACT_NOT_REVIEWED`. Independent portable continuation of R749SUT–R749SUV (Draft PRs #2736/#2739/#2742); not a native X6 task return, Result or Review.

## Frozen input and object

Frozen science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md` (WBRC-T30–T32). This is its **auxiliary, positive-integer, named two-Port Q=+1 observer**, not a native X6 Cell/Link/Port event. Current behavioral rules were read separately; no frozen scientific input or P000 premise is changed.

For integers `t>=3`, `c>=0`, put `B=t^2+c`, `M=B-1`. The legal unordered population is

\[
2\le x\le y,\quad n=xy\le B,\quad n-x-y\ge1.
\]

Their exact labeled reconstruction (one of the port orientations) is

\[
(a,u,v,d)=(n-x-1,n-1,n-x-y,n-y-1),\qquad ad-uv=1,\quad Q=u+v-a-d=1,
\]

and the feedback score is

\[
\tau(x,y)=F(n,s)=(n-1)[(n-1)^2-(n-1)s+n],\qquad s=x+y.
\]

All unordered winners are retained, hence independent valid diagonal/off-diagonal label permutations can be restored exactly. The integer score is a positive-rational BRC-derived observer, not a license to erase individual path provenance in a richer observer.

## Theorem A — complete candidate reduction for every offset

For **every** integer `t>=3` and `c>=0`, the full set of unordered maximizers is obtained by comparing the legal square pair `(t,t)` with the following finite set and retaining all ties:

For each integer `j=1,...,c` and `h=1,...,3j-1`, define

\[
N=t^2+j,\quad S=2t+h,\quad \Delta_{j,h}=S^2-4N=4th+h^2-4j.
\]

If `Delta>=0` is a perfect square `r^2`, `S-r` is even, and

\[
x=\frac{S-r}{2}\ge2,\quad y=\frac{S+r}{2}\ge x,\quad N-S\ge1,
\]

include `(x,y)` with its exact integer score. There are **at most**

\[
\boxed{\sum_{j=1}^c(3j-1)=\frac{3c^2+c}{2}}
\]

integer-square-root tests. For `c=0`, the unique winner is `(t,t)`.

Consequences: an exact optimizer for every fixed offset `c` uses `O_c(1)` integer arithmetic and integer-square-root operations, independently of `t`; for variable `c`, the stated construction uses `O(c^2)` such operations (not a claim about bit complexity, which includes large-integer multiplication/square roots and output). It returns every unordered tie. The optimal product satisfies `t^2<=n*<=t^2+c`, so the gap `B-n*` lies in `{0,...,c}`.

### Proof (A1): square pair wins uniquely over all n<=t^2

The square pair is legal for `t>=3` and has score

\[
T_0=(t^2-1)(t^2-t-1)^2>0.
\]

For any legal `x,y` with `n<=t^2`:

- If `s>=2t`, note `s<=n-1` by legality and `F(n,s)` is strictly increasing in `n` on the admissible interval because
  \[\partial_nF=3(n-1)^2-2s(n-1)+2n-1>0.\]
  It is strictly decreasing in `s`. Hence `F(n,s)<=F(t^2,s)<=F(t^2,2t)=T_0`, with equality only at `n=t^2, s=2t`, i.e. `x=y=t`.
- If `s<=2t-1`, the integer AM–GM inequality yields `n<=floor(s^2/4)<=t(t-1)`. Each of the three positive integer factors `n-1`, `n-x-1`, `n-y-1` is strictly smaller than the corresponding `t^2-1`, `t^2-t-1`, `t^2-t-1` square factors. Hence `F(n,s)<T_0`.

Thus every non-square maximizer has `n=t^2+j`, `1<=j<=c`.

### Proof (A2): uniform score cutoff in the factor sum

For `n=t^2+j>t^2`, AM–GM forces integer `s>=2t+1`, so write `s=2t+h`, `h>=1`. At fixed `n`, `F(n,s)` is strictly decreasing in `s`. Direct expansion gives the **exact polynomial identity**

\[
\begin{aligned}
T_0-F(t^2+j,2t+3j)
&=j\left[4t^3-2t^2-4t+1+j(3t^2+2t-4)+2j^2\right]\\
&>0\qquad(t\ge3,\ j\ge1).
\end{aligned}
\]

Every candidate with `h>=3j` scores strictly below the square pair. Hence only `1<=h<=3j-1` can maximize. A pair with specified `N,S` exists exactly when its quadratic `z^2-Sz+N=0` has the stated nonnegative square discriminant, integer parity and legality. Each admissible `(j,h)` gives at most one unordered pair, so testing the stated finite set is both sound and complete. □

## Theorem B — zero-gap family and exact sparsity order

For every fixed integer `c>=1`, define `Z_c(T)` as the number of `t` with `3<=t<=T` such that at least one optimizer has `xy=t^2+c` (gap zero). Then

\[
\boxed{Z_c(T)=\Theta_c(\sqrt T)}.
\]

For the explicit infinite subfamily

\[
\boxed{t=k(k+1)+c,\quad k\ge1},
\]

the **unique** unordered optimum is the zero-gap pair

\[
\boxed{(x,y)=(t-k,t+k+1)},\qquad xy=t^2+c.
\]

### Proof (B1): explicit family is optimal

For such `t,k,c` the pair is legal: `x>=2`, `x<=y`, and `n-s=t^2+c-(2t+1)>=1` since `t>=3`. Its sum `2t+1` is the smallest possible integer sum for a pair with product strictly exceeding `t^2`. Against any other `n` in `(t^2,B]`, monotonicity of `F` (increasing `n`, decreasing `s` on the legal range) yields `F(n,s)<=F(B,2t+1)` with equality only if both `n=B` and `s=2t+1`; that quadratic has one unordered factor pair. Against all `n<=t^2`, Theorem A1 gives `F<=T_0`, while

\[
F(t^2+1,2t+1)-T_0=(t-1)(2t^3-2t^2-3t-1)>0\quad(t\ge3).
\]

Monotonicity then gives `F(B,2t+1)>T_0`. This pair is uniquely optimal. The family contributes `\sqrt(T)+O_c(1)` admissible parameters.

### Proof (B2): matching upper bound

Any zero-gap optimum has `j=c`, hence by Theorem A `s=2t+h` for some `h in {1,...,3c-1}`. For fixed `h`, existence requires an integer `r>=0` satisfying `r^2=4ht+h^2-4c`; for each `r` at most one `t` is possible. When `t<=T`, `r<=sqrt(4hT+h^2)`, giving `O_c(sqrt T)` choices after summing over the finitely many `h`. Combined with B1, this proves the stated order. □

Thus zero-gap parameters have zero natural density inside the fixed-offset `t` sequence, yet occur infinitely often. This is a statement for this integer observer; no physical-native X6 frequency is inferred.

## Corollary — square-plus-three (`c=3`) in 15 exact root tests

With `B=t^2+3`, enumerate only `(j,h)` from `(1,1..2)`, `(2,1..5)`, `(3,1..8)`, which totals **15** tests for every `t>=3`. Scores and all ties follow Theorem A. The possible optimal gaps are precisely a subset of `{0,1,2,3}`; each value occurs (examples `t=3` gap 0, `t=4` gap 1, `t=18` gap 2, `t=11` gap 3).

The simple explicit zero-gap family `t=k(k+1)+3` realizes `(t-k,t+k+1)`. Additional zero-gap instances arise from other discriminant roots; the complete decision is given by the 15-test algorithm, without requiring a closed list of quadratic progression overlaps.

## Independent exact verification (reproducible)

The companion Python-stdlib program `R749SUW_FIXED_OFFSET_ROOT_CERT.py` computes all scores with exact integers and uses `math.isqrt` only. It returned `PASS` for:

- **371** fully exhaustive domains: `3<=t<=55`, `0<=c<=6`, enumerating every legal unordered factor pair, independently of the new cutoff;
- **18,000** full smaller-factor endpoint-oracle domains: `3<=t<=1802`, `0<=c<=9`, independently scanning every `x` and its maximally admissible `y=floor(B/x)`;
- **49,998** square-plus-three instances: `3<=t<=50000`, all 15 root positions per input, checking valid score/legality and all ties;
- **25,000** exact polynomial identity/positivity checks and **1,500** explicit zero-gap family tests for `1<=c<=15,1<=k<=100`;
- large arbitrary-precision examples up to `t=10^24`, `c=25`.

On `3<=t<=50000, c=3`, the winning gap counts were `gap 0: 960`, `gap 1: 620`, `gap 2: 360`, `gap 3: 48,058`; no unordered ties in this sampled range. These finite observations are separate from the infinite proofs. The JSON companion stores all large values as decimal strings and gives exact validation coverage.

## Reuse, authority, next work

This theorem advances the fixed-offset question left open in R749SUV and is a direct exact integer application of the frozen positive-rational labeled WBRC Port observer; it reuses the R749SUT/SUU/SUV score formulation without altering their source. Transfer to **all nonstandard** two-Port maxima requires the upstream R749SUO author theorem about `Q=+1` (when `M>=116`), whose independent review remains pending. The named observer preserves port labels; a richer native provenance/time observer would require its own retention/bridge proof. No Task CLAIM, native X6 Result or independent review is asserted.

Further concrete questions: (i) reduce the `O(c^2)` discriminant tests to an output-sensitive or `O(c)` exact bound; (ii) classify all quadratic progressions contributing to `c=3` zero-gap cases and compute the exact leading constant, accounting for overlaps; (iii) analyze whether the fixed-offset normal form can feed the general `O(M^{1/4})` quotient-plateau optimizer as a fast branch without changing its full input complexity.
