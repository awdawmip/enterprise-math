# Enterprise Math R34 — Exact arc-max floor-sum and source-select prefix compiler

Date: 2026-11-10. Frozen science: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Parent: R33 Draft PR #1935 (`18d43c744aaed7041e5f7e87f98d278489b6aa57`), R32 Draft PR #1929 (`87fdeff1cba7055f50a5fd8dadaad390476d9da1`). Scope: the auxiliary irrational-circle S23/AV observer; author-side derivation and exact finite tests.

## 1. New theorem — source-indexed arc maxima by floor sums

Fix irrational \(\theta\in(0,1)\) and \(m\ge2\). The historical partition consists of arcs \(I_{a,b}\) from \(\{a\theta\}\) clockwise to \(\{b\theta\}\), with \(a,b\in\{0,\ldots,m-1\}\) consecutive in phase order. Define \(w_{a,b}=1\) when \(\{a\theta\}>\{b\theta\}\), otherwise \(0\). For any nonnegative source index \(t\),

\[
 {\bf1}_{I_{a,b}}(t)=\lfloor (t-a)\theta\rfloor-\lfloor(t-b)\theta\rfloor+
 \lfloor a\theta\rfloor-\lfloor b\theta\rfloor+w_{a,b}.
\]

The interval is left-inclusive, right-exclusive. Therefore the exact number of gap-left-endpoint sources in an integer interval \([\ell,r)\) is

\[
 C_{a,b}(\ell,r)=F(r-\ell,\theta,(\ell-a)\theta)-
 F(r-\ell,\theta,(\ell-b)\theta)
 +(r-\ell)(\lfloor a\theta\rfloor-\lfloor b\theta\rfloor+w_{a,b}),
\]
where \(F(s,\theta,z)=\sum_{k=0}^{s-1}\lfloor k\theta+z\rfloor\). On a fixed rational parameter endpoint \(\theta=T/D\), each sum is an exact signed Euclidean floor sum with integer inputs. In a rational open enclosure \((L,U)\), the same counts throughout \((L,U)\) are certified by the stronger branch condition \(\lfloor dL\rfloor=\lfloor dU\rfloor\) for every shifted index difference \(d=t-a,t-b\) in the queried range, together with stable historical phase ordering. This rules out every interior phase collision. For the frozen prefix, the exact finite check passes for all \(-127\le d\le389\); the portable checker enforces this. For a generic parameter interval with possible interior collisions, split at the finitely many rational collision values first.

Let \(a/q<\theta<c/j\), \(cq-aj=1\), be Farey neighbors at a stage with \(q,j\le n\le q+j\), and set \(u=q\theta-a\), \(v=c-j\theta\), \(w=u+v\). The gaps of the first \(n\) cutpoints have disjoint left-source index classes:

* \(0\le t<n-q\): length \(u\).
* \(n-q\le t<j\): length \(w\).
* \(j\le t<n\): length \(v\).

For each historical arc \(I\), count each class with \(C_I\). The arc's largest remaining gap is precisely the largest available length among \(u,w,v\); the risk is

\[
 \boxed{R_n=1-\sum_{I\in\mathcal H_m}
 \max\bigl(\{u:C_I(0,n-q)>0\}\cup
 \{w:C_I(n-q,j)>0\}\cup
 \{v:C_I(j,n)>0\}\bigr).}
\]

If an arc contains more than one maximal gap, the count and the last source index preserve that tie/provenance. The last source is obtained by binary-search rank/select using \(C_I(t,r)\), without enumerating all source phases.

**Proof.** Write \(x_t=\{t\theta\}\) and expand the floor identity; the difference of the two shifted floors is the indicator of the clockwise arc, with the wrap correction. Summation yields the count formula. The standard three-gap successor map in Farey coordinates has successors \(t+q,t+q-j,t-j\) on precisely the three index ranges above and displacements \(u,u+v,v\), respectively. Every gap lies in exactly one historical arc, selected by its left endpoint. The maximum formula follows arcwise. Since source indices are integers in a known interval, a count query on any suffix identifies whether a source exists there; monotone bisection yields its maximum. QED.

## 2. New theorem — one arc event per Farey stage, plus an exact boundary correction

Fix an entire Farey stage of integer \(n\), \([n_0,n_1]\) with constant neighbors \(a/q<c/j\) and \(n_1=q+j\). At its first position \(n=n_0\) the long gaps have left-source indices \([n_0-q,j)\). For each original historical arc with at least one such gap, let

\[
 t_I=\max\{t\in[n_0-q,j):\{t\theta\}\in I\}.
\]

Then the only positive increment from this arc strictly *after* stage entry occurs at

\[
 \boxed{n_I=q+t_I+1,\qquad \Delta_I R=\min(u,v).}
\]

The source \(n-q\) is removed in increasing order as \(n\) advances, so its last long gap disappears when \(n=q+t_I+1\). Before that event \(w\) remains maximal, and afterward the new split produces \(u\) and \(v\), whose maximum is \(\max(u,v)\). Hence the exact fall in the arc maximum is \(w-\max(u,v)=\min(u,v)\). Every arc contributes at most one such interior-stage event; coincident event indices are aggregated by source count. At a new Farey stage entry \(n_0>m\), the change \(R_{n_0}-R_{n_0-1}\) is obtained from two independent floor-sum arc-max queries. This explicitly handles the cross-stage boundary rather than attributing it to the new stage's long-gap deletion.

Thus the entire risk-increment function over finitely many stages can be compiled from stage boundaries, at most \(m\) rank/select queries per stage, and exact amplitude expressions. The method requires no future-cutpoint phase sort or per-\(n\) update loop in the compiler. If a stage has no interval-interior events, its boundary check still applies.

## 3. Frozen S23/AV result

On

\[
 \frac{262204504569236716045286}{10^{24}} < \theta <
 \frac{262204504569236716045287}{10^{24}},
\quad m=128,
\]

the first three Farey stages are \([128,164]\) with \((a,q,c,j)=(27,103,16,61)\), \([165,225]\) with \((43,164,16,61)\), and \([226,389]\) with \((43,164,59,225)\).

Exact floor-sum/select returns **36, 60 and 127** interior-stage source events, respectively. The stage boundaries 165 and 226 each contribute a positive event, giving **225** positive prefix increments from **223 selected sources + two boundary queries**, directly coalesced into just four maximal increment runs:

| n | \(\Delta R_n\) |
|---|---|
| 129–164 | \(16-61\theta\) |
| 165–292 | \(164\theta-43\) |
| 293–328 | \(0\) |
| 329–389 | \(164\theta-43\) |

The compiler never iterates all 261 prefix update positions. An independent oracle **does** reconstruct all 261 complete phase partitions at both rational endpoints as a regression; its results agree exactly with the floor-sum risk query at each \(n\). This distinction is deliberate: generation is bulk, validation exhaustive finite.

Using R33's exact quotient-prefix Farey jumps for the following stages and R31's applicable two-block source-age theorem for later stages, the complete horizon \(128\le n\le10^{12}+128\) produces **78 Farey stages, 28 quotient decisions, 148 later positive blocks, 298 maximal affine runs**. The canonical R32 fixture comparison is byte-for-byte identical, with SHA-256 `2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6`. Final value:

\[
 \boxed{R_{10^{12}+128}=-4017401528447+15321634290944\theta.}
\]

Extra generic finite regressions on the same enclosure give exact agreement of the floor-sum arc-risk formula and a separate direct-sort oracle for **101 positions each** for \(m=64\) and \(m=256\). The rank/select theorem applies for every historical \(m\) where the stated phase/Farey conditions hold; the S23 164-window/two-block optimization is a separate special input result.

## 4. Reproducibility and bit cost

`VERIFY_R34_PORTABLE.py` is a standalone Python 3 standard-library exact-parameter checker of the 3-stage bulk prefix plus the 298-run compiler and output digest. `VERIFY_R34.py` is the fully independent local regression checker (261 separate phase sorts), preserved in the conversation artifact. `VERIFY_R34_GENERAL.py` tests \(m=64,256\). All listed tests were actually executed with integer arithmetic.

For an arc, each class-presence query is at most two Euclidean floor sums; a last-source query requires \(O(\log n)\) such counts. With \(m\) historical arcs and \(S\) Farey stages, the generic source-selection operation count is \(O(mS\log N\log D)\) Euclidean integer divisions, plus historical-arc phase ordering, Farey-stage generation and output integration; this is a loose arithmetic-operation upper bound when all \(m\) sources require last-select in each stage. The frozen fast path uses only 3 prefix stages and 223 successful source selects, then two constant-size blocks per eligible later stage. Bit operands scale with the parameter denominator \(D\), the index horizon \(N\), and coefficient size; division is not treated as unit bit cost. The raw input must furnish a certified rational enclosure, and exact affine outputs retain their integer bit lengths.

This is an author-side mathematical/engineering result under the frozen auxiliary observer. No shared Task CLAIM, formal independent mathematical review, native X6 transfer or physical calibration has been claimed.

## 5. Next unit

1. Generalize stage-boundary source/tie changes to a provably output-sensitive and collision-aware compiler without input-specific 164-age structure; test longer \(m=64,256\) horizons and distinct certified irrational enclosures.
2. Improve the bound by caching common floor-sum transforms across historical arcs and by combining all source selections into an offline batched rank/select structure.
3. Independently review the historical arc indicator with exact endpoint/collision treatment, the Farey boundary correction, the long-gap source deletion claim and full bit cost; only then consider formal project admission.
