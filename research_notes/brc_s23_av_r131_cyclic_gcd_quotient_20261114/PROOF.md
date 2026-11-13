# R131 — Exact cyclic gcd quotient and interval-lift certificates for the S23 observer

Date: 2026-11-14 (Asia/Shanghai). Research mode: author-side auxiliary mathematics. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

Predecessors: R127 periodic fiber at `72f6de415d45fbd9a0a3bfde7aae36ccc99d0b93`; R129 event theorem at `ddef5881c7e9996fbc08c6f48cd0c387606d035d`; R130 sparse trace/persistent index at `7040bd2b6f134ea105f75370f0e35f1294818b64`.

## Exact mathematical scope

Let `m>=1`, `x,l,h in Q`, `l<h`, and `A,d,E in Z`. For integer `0<=i<m`, put

`S_i(theta)=1[{x+(A+i*d)*theta} < {E*theta}]`

on the open interval `I=(l,h)`; braces denote the ordinary fractional part, and a strict inequality is used. This is the previously defined S23 *auxiliary observer*. The parameter theta is an auxiliary mathematical phase parameter, not automatically native heartbeat time.

Set `g=gcd(|A|,|d|,|E|)`, taken nonnegative, and for `g>0` put `a=A/g`, `b=d/g`, `e=E/g`. Define a canonical circular observer for `0<=eta<1` by

`W_i(eta)=1[{x+(a+i*b)*eta} < {e*eta}]`.

**R131.1 (exact periodic quotient).** If `g>0`, then for every real theta and every i,

`S_i(theta)=W_i({g*theta})`.

In particular, `1/g` is a period of the *complete joint word*. If `g=0`, then `A=d=E=0` and `S(theta)` is identically the all-zero word. The asserted period need not be the least period.

*Proof.* Write `g*theta=k+eta` with `k in Z, 0<=eta<1`. Both `(A+i*d)*theta=(a+i*b)(k+eta)` and `E*theta=e(k+eta)` differ from their eta expressions by integers. Fractional parts, including their strict comparison and endpoint equalities, are identical. When g=0, the right fractional part is zero, so no coordinate can be one. QED.

## R131.2: one circular sparse event trace covers every interval

Inside `eta in (0,1)`, form the finite union of isolated integer roots of

`e*eta`, `x+(a+i*b)*eta`, and `x+(a+i*b-e)*eta` for all i.

As in R129, a zero slope contributes no isolated crossing, even if the affine expression is identically integral. Let its distinct ordered cuts be `0<c_1<...<c_q<1`. Store (i) the special `W(0)` state, (ii) the `q+1` open-cell states, and (iii) all `q` singleton-cut states. R130's sparse `D_cut/D_right` deltas and its persistent index may be used directly on the interval (0,1); the special origin word is one extra root.

The circular trace is **exact** at all real phases. It has at most `2q+2` distinct words, where

`q <= T_g := |e| + sum_{i=0}^{m-1} (|a+i*b|+|a+i*b-e|)`.

This bound counts isolated roots using the fact that an affine map of (0,1) with nonzero integer slope s crosses at most |s| integers. The initial and origin word require at most 2m bit evaluations, and the two sparse cut/right probes require exactly `2*sum_c |J(c)|` further bit evaluations. Root construction/sorting costs `O(T_g log(T_g+1))` rational comparison operations in a straightforward implementation. The persistent-index bound of R130 then yields `O(log(q+1)+log(m+1))` comparison/tree steps for one bit query, **in addition** to exact `eta={g*theta}` arithmetic. Fraction coefficient bit lengths and full-word output cost are separate.

*Proof.* By R129, no bit changes off these isolated roots. R130's per-cut argument applies verbatim within (0,1), and the eta=0 word is evaluated separately; hence the trace includes every boundary-only state. The number of singleton and open states is `1+q+(q+1)=2q+2`. The root bound and update count follow by summing actual slope crossings and R130's affected-coordinate sets. Together with R131.1 this proves exactness on every interval, regardless of how many periods it spans. QED.

## R131.3: integer-lift criterion and rational witnesses for arbitrary open I

Write `L=g*l`, `H=g*h`. A canonical singleton phase `c in [0,1)` occurs at a theta in I exactly when

`exists k in Z: L-c < k < H-c.`

The least possible k above the lower bound is `k0=floor(L-c)+1`; membership is thus equivalent to `k0 < H-c`. A corresponding exact rational witness is `theta=(k0+c)/g`.

For an *open* canonical phase cell `(a0,b0) subset (0,1)`, some eta in that cell and some theta in I share that phase exactly when

`exists k in Z: L-b0 < k < H-a0.`

Set `k0=floor(L-b0)+1`. The cell is reachable exactly when `k0 < H-a0`. Then choose

`eta = (max(a0,L-k0)+min(b0,H-k0))/2`,
`theta=(k0+eta)/g`.

The midpoint is rational, lies strictly in both open constraints and therefore is a certified word witness. Filtering the circular cut/segment states by these two criteria gives **exactly the distinct words attained on (l,h)**, without enumerating any repeated periods.

*Proof.* The equation `g*theta=k+eta` is equivalent to `L<k+eta<H`. Fixing eta=c yields the singleton condition. If eta ranges over (a0,b0), the open intervals `(a0,b0)` and `(L-k,H-k)` overlap precisely when `k>L-b0` and `k<H-a0`. In either case the least integer above the lower bound proves the existence criterion and the displayed witness. Each W state is constant on its cell; the exact equality of R131.1 finishes the proof. QED.

**Endpoint corollary.** If `h-l>1/g`, every phase in [0,1) is represented by I; if `h-l=1/g`, exactly the single phase `{g*l}` is absent. The strict endpoint condition is therefore fully represented, including the case where the missing phase carries a cut-only word.

**Sharp endpoint example.** For `m=1, x=A=d=0, E=1, g=1`, the circular word is zero at eta=0 and one at every `0<eta<1`. The open interval `I=(0,1)` attains only the one-word, whereas `I=(-1/2,1/2)` attains both. Thus the cyclic origin is a genuine singleton-only state and must be filtered with the strict integer-lift criterion rather than unconditionally included for an interval of exactly one period.

## R131.4: exact event replication across aligned complete periods

Suppose `g>0` and `E!=0`. Let `q` be the number of **distinct** normalized interior event roots in (0,1), and let `r in Z, n>=1`. The direct R129 event set in the open aligned interval

`I=(r/g,(r+n)/g)`

has **exactly**

`|C_I| = n*q + n - 1 = n*(q+1)-1`

distinct cuts. Indeed, each normalized interior event `c` has precisely n distinct lifts `theta=(r+j+c)/g` for `j=0,...,n-1`. The other direct roots occur only at phase `eta=0` and hence at the `n-1` internal period seams `theta=(r+j)/g, j=1,...,n-1`. Every such seam is included because `E*theta=e*(r+j)` is integral and `E!=0`, i.e. it is an isolated integer crossing of `E*theta`. The two classes are disjoint and exhaustive by the normalized affine root construction. QED.

For the scaling family below, `g=K`, `q=44`, `r=0`, `n=K`, so the *exact* dense event count is `45K-1`; the final benchmark verifies the values 44,89,179,359,719,1439,2879,5759 for `K=1,...,128` on the declared doubling grid. For `K=10^80`, this is an exact mathematical count of the direct-cut enumeration obligations, without executing that enormous enumeration. The quotient still uses 44 interior cuts and its single explicitly retained phase-zero state.

## Efficiency domain and limitation

For `(A,d,E)=(3K,K,2K)` and `x=1/7,m=7,I=(0,1)`, the direct R129 root *upper bound* is `72K`, whereas the circular quotient bound is `72` and the actual distinct interior cuts are `44`, for all positive integers K. On the tested family `K=1,2,9,256,10^10,10^80`, the quotient retained 36 realized words and performed 168 exact single-bit evaluations, including the origin state. This is an algebraically proved input-family scaling gain in event count; measured runtime is not asserted. With gcd=1 but very large coprime coefficients, this construction may still have a huge normalized event count, so R126/R127 coefficient-independent feasibility remains a useful alternative.

## Verification and reproducibility

Companion code is `check_r131.py.gz.b64` (gzip+base64 text; decode with `base64 -d check_r131.py.gz.b64 | gzip -d > check_r131.py`). It uses Python 3 standard-library `fractions.Fraction`, integer floor/ceil and no floating point. Execute `python check_r131.py`. It compares independently generated unquotiented integer-crossing events with the quotient-lift words, validates every returned rational witness, checks the indexed phase word against direct evaluation at rational sample points and rechecks integer-root cuts. Its `verification_r131.json` companion reports the exact covered test families and results.

Observed code result: `R131_CYCLIC_QUOTIENT_PASS`; 207 independent sweep instances, 4,236 verified realized rational witnesses, 6,375 direct-bit phase query comparisons, 8,367 lifted-cut comparisons, and six scaling factors through 10^80. Finite tests assess the implementation within that coverage; R131.1–3 are the algebraic statements proved above.

This material remains an external mathematical reduction of an auxiliary S23 observer. No native Cell/Link/Port authorization, physical rotation or residual attribution is inferred. It does not change the protected P000 or frozen scientific input.

## Next discriminating unit

Develop a **hybrid controller** choosing among: (i) R131 period-quotiented sparse events for large common gcd or long intervals; (ii) R127 modular two-integer feasibility when a short integer relation is present; (iii) R126 three-integer feasibility when normalized slopes remain huge and coprime. Compare exact bit complexity and concrete time/memory on a shared family, including singleton-cut witness recovery, and distinguish candidate-query cost from complete-word enumeration.
