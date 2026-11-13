# R26 — certified non-enumerative S23/AV risk via Farey successor and floor sums

Date: 2026-11-10 Asia/Shanghai. Author-side research, independent review pending. Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`, preserved. This is the S23/AV auxiliary irrational-circle observer with `m=128` historical cuts, not a native X6 dynamics claim. Continuation: R25 @ `7f2aff7df2ff1a5360362d106e14f9a9b4074fc7` (Draft PR #1900); previous independent affine-epoch comparator R16 file `AFFINE_RUNS_1T.tsv`.

## Exact input and risk functional

Fix any irrational `theta` in the strict rational interval

```
262204504569236716045286/10^24 < theta
 <262204504569236716045287/10^24.
```

For integers `n>=m>=2`, let `P_n={ {t theta}:0<=t<n }` on the oriented unit circle. Its `m` historical arcs `I=[{s theta},{e theta})` are the oriented consecutive arcs in `P_m`. Let `M_n(I)` be the length of the longest elementary gap of `P_n` contained in `I`. Then `R_n=1-sum_I M_n(I)` is the existing optimal whole-string error. The output is an **integer-affine expression** `R_n=A+B theta`, with a precise input interval on which its selected coefficients hold.

## Theorem 1 — certified three-translation successor permutation

Let `N=n-1`. Suppose reduced `a/i<c/j` are the consecutive Farey fractions of order `N` that contain `theta`, so that

```
a/i < theta < c/j;   i*c-j*a=1;
1<=i,j<n;            i+j>=n.
```

Write `u=i theta-a>0`, `v=c-j theta>0`, `w=u+v`. The clockwise successor of the phase labelled `t` is **exactly**

```
S(t)=t+i     for 0<=t<n-i,          length u
S(t)=t+i-j   for n-i<=t<j,          length u+v
S(t)=t-j     for j<=t<n,            length v.
```

Thus every elementary gap belongs to one of three integer-index ranges and has one of the three integer-affine lengths.

**Proof.** These three index pieces are disjoint and cover `0,...,n-1`, as `i+j>=n`. Their image intervals are respectively `[i,n)`, `[n-j,i)` and `[0,n-j)`, so `S` is a permutation. For every edge `t->S(t)`, its clockwise fractional displacement is the asserted positive value because `{i theta}=u` and `{-j theta}=v`. The edge lengths are in `(0,1)`: indeed `j u+i v=i c-j a=1`, which also gives `u+v<=1`; if the middle interval is nonempty, `i+j>n>=3`, hence `u+v<1`. Summing every edge displacement gives

```
(n-i)u+(i+j-n)(u+v)+(n-j)v = j u+i v = 1.
```

Every cycle in such a positive-forward permutation has an integer winding number at least one. Since the combined winding is one, there is one cycle with winding one. It visits each labelled phase once in increasing cyclic order, so no edge can skip an intermediate phase. Thus `S` is the true clockwise successor. QED.

The Farey bracket can be found by accelerated Stern–Brocot mediant jumps, stopping when `i+j>n-1` and checking the determinant. Both enclosing rational endpoints must lie **strictly inside the same Farey bracket** to certify the uniform frozen-theta claim.

## Theorem 2 — exact per-historical-arc population via Euclidean floor sums

For integer source index `s` and integer half-open range `[L,H)`, define

```
F_s(L,H)=sum_{t=L}^{H-1} (floor(t theta)-floor((t-s) theta)-floor(s theta)).
```

The summand equals `1_{ {t theta}<{s theta} }` identically, including all signed values of `t-s`. Therefore `F_s` counts sources in the range lying strictly below the phase `{s theta}`.

If historical arc `I=[{s theta},{e theta})` is nonwrapping, its source count in `[L,H)` equals `F_e-F_s`. If wrapping, it equals `(H-L)+F_e-F_s`. Endpoints and ties are exact: source label `s` is included and `e` excluded; irrationality implies distinct labelled phases.

For a rational `p/q` enclosed by the same Farey bracket, all `floor(k theta)` with `|k|<=n-1` are equal to the corresponding `floor(k p/q)`, because a change would cross a rational with denominator at most `n-1`. Consequently the above counts can be evaluated **exactly for all theta in the certified interval** via the Euclidean floor-sum identity

```
sum_{z=0}^{h-1} floor((p*z+b)/q),
```

with signed-offset normalization and Euclidean reduction; no loop over `h` terms is needed. The implementation uses Python integers and `Fraction` exclusively.

Apply these counts to the three source-index classes `[0,n-i)`, `[n-i,j)`, `[j,n)`. For each historical arc `I`, let the three counts be `C_u(I),C_w(I),C_v(I)`. Then

```
M_n(I)=max( {u:C_u(I)>0} union {w:C_w(I)>0} union {v:C_v(I)>0} ).
R_n=1-sum_{I in historical arcs} M_n(I).
```

This is a finite `m`-term **non-enumerative exact risk formula for arbitrary n** once the Farey bracket and theta representation are certified. It retains original source labels, separate equal gaps and their historical owners. For each arc, a proposed maximum coefficient pair is checked at *both* rational theta endpoints. Agreement gives a uniform exact `A+B theta` law over the entire interval; a disagreement requests parameter subdivision rather than an unsupported common affine expression.

For fixed `m=128` and the 24-digit rational enclosure, one query needs at most `3m` arc/range counts, each using a bounded number of Euclidean floor sums, after accelerated Stern–Brocot and historical sorting. The implemented process has work depending logarithmically on the exact rational denominator `q`, not on the number `n` of future cuts; its input precision, rational-bracket certification, bit lengths and `m`-term output construction remain included. It allocates no `n`-sized phase array, gap table, or epoch table.

## Theorem 3 — plateau endpoint certificate

For fixed historical arcs, adding a phase cut only subdivides an old gap. Therefore each `M_n(I)` is nonincreasing and `R_n` is nondecreasing. If two exact rank evaluations give `R_a=R_b` for `a<b`, then

```
R_t=R_a for every integer a<=t<=b;
Delta R_t=0 for a<t<=b.
```

This proves an entire plateau using **two** exact evaluations, independent of the number of insertions between them. The equality is an equality of integer-affine coefficients holding over the frozen theta enclosure.

Certified intervals using the new evaluator (left endpoint attained after a positive increment):

| constant-risk `n` endpoints | certified zero increments |
|---|---:|
| 322340 .. 476197 | 153857 |
| 476361 .. 630218 | 153857 |
| 630382 .. 1106579 | 476197 |
| **752555238039 .. 1000000000128** | **247444762089** |

The fourth interval is a 247.4-billion-insertion **finite** plateau. Its exact common risk is

```
R_n=-4017401528447+15321634290944 theta
```

throughout the displayed interval. The preceding insertion at `n=752555238039` has a strictly positive increment (both rational enclosure endpoints checked). The right endpoint is the declared trillion-future horizon `n=m+10^12`; no right-maximality beyond it is asserted.

These candidate endpoints were sourced from the older R16 epoch table; the proof of each plateau now uses the independent Farey/floor-sum endpoint computation plus monotonicity and does not rely on enumerating interior cuts.

## Actual local computation and cross-checks

The included standalone `VERIFY_R26.py` executed on the frozen rational theta interval. It independently reconstructs full phase partitions at small sizes. It passed exact agreement with direct sorting for **every integer n from 128 through 500** and at 30 selected earlier frontier/boundary positions. It also directly evaluated `n=10^6,2*10^6,10^8,10^9,10^10,10^11,10^12`; at `n=10^12` the bracket `165937423910/632854970141 < theta < 197323373351/752555238039` is certified, with 27 accelerated Stern–Brocot jumps.

The additional `CROSSCHECK_R16.py` read the pre-existing local `AFFINE_RUNS_1T.tsv` (298 rows, SHA-256 `2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6`) and checked **1,147 exact positions** spanning `128..10^12+128`, including every epoch boundary and adjacent points plus 250 deterministic random positions. All integer-affine coefficients matched. The comparison test is independent *implementation* evidence; the earlier table is not an independently reviewed theorem.

At the full horizon `n=1000000000128` the evaluator gives

```
(A,B)=(-4017401528447,15321634290944).
```

The program is exact integer/rational arithmetic throughout. The 1,147-position comparison ran in 18.814 seconds in the observed environment; a separate individual `10^12` evaluation was approximately 0.02 seconds. Those are local execution observations, not hardware-independent complexity guarantees.

## Scope, BRC reuse and next scientific question

This combines the established Farey/three-gap and Euclidean floor-sum interfaces with BRC-style **source-labelled historical fibres**. In this observer, the sufficient statistic for current risk is the three gap-type support flags per historical arc; when asking for provenance-sensitive downstream operations, preserve the individual counts and source-index ranges (the emitted `chosen` records), not just the final risk. `COMPOSE_APPLIED` for these precise existing mathematical interfaces; the new construction is the **application to this historical-arc risk functional**, with no new Foundation or shared-tool acceptance.

**Next problem:** derive a compressed symbolic *event/range generator* that computes the positions where these historical-fibre type-presence flags change, using interval rank/select and Farey-denominator jumps, and outputs maximal constant-increment epochs directly. Establish exact bit-operation bounds accounting for rational-input precision. Seek a closed explanation of the recurrent `67/36/61` and `q-164` patterns by quantifying which of the 128 historical arcs lose their winning gap type. Preserve the frozen input pin, source labels and pending independent mathematical review.

**Persistence state:** This author-side branch/PR is durable scientific evidence, not a shared-task CLAIM, Result/Review, Working Truth or Foundation promotion.
