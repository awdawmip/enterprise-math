# R284EB — Exact adaptive decision-tree cost of the nine-bit Port exception and a full-state short-circuit guard

Date: 2026-11-22 (Asia/Shanghai). Scientific status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**.

## Frozen source and evidence scope

Continue R284EA, using its exact nine-bit threshold theorem. Original immutable scientific input: `awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py`; blob SHA1 `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`; 65,536 original codewords SHA256 `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`. Direct predecessor R284EA theorem: `enterprise-math@bc66d7bdd3210f426dc38497e6c0368ab11ab292`.

This is a mathematical optimization of the **frozen auxiliary Boolean quotient-correction observer**. It retains the original full Port state, its joint provenance and frozen determinant. No native-X6 state compression, physical BRC evolution or general Port update claim is made.

Let `b=(Y,Z,U,G,H,R,B0,B1,B2) in {0,1}^9`, `w=(13,6,28,25,11,12,26,17,6)`, and `f(b)=1[sum(w_j*b_j)>=77]`. R284EA already proved that in the exceptional core class `u1=a=x=u2=w=b=2`, this expression is precisely the original quotient correction. The 512 nine-bit states are uniform and each appears twice as `B3` varies within the original 1024-state core class.

**Cost model.** One exact query reveals one original source bit; a query costs one unit. Queries can depend on previous answers. All 512 bit vectors are equiprobable. Boolean additions, comparisons and control branching are *not* charged. These are exact bit-probe counts, **not** execution time or memory-traffic measurements (in particular, all source bits might already occupy one machine word).

## Theorem 1: optimal mean bit-probe count

Among all deterministic, adaptive, exact decision trees for this nine-bit Boolean function, the exact minimum total number of bit queries across all 512 states is **2734**. Hence

\[\min\mathbb E[\mathrm{queries}]=\frac{2734}{512}=\frac{1367}{256}=5.33984375.\]

A fixed nonadaptive priority order with conditional early stopping attains this minimum: **U, B0, G, B1, Y, R, H, Z, B2**. Maintain the current sum `L` of positively observed weights, and the sum `M` of remaining weights. Terminate with `f=1` when `L>=77`, or with `f=0` when `L+M<77`; otherwise read the next source bit.

| Number of queried bits | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Number of nine-bit inputs | 128 | 96 | 48 | 80 | 76 | 42 | 42 |

Independent classification totals: 223 positive, 289 negative. Both the adaptive optimum and the fixed-order witness have the displayed histogram. Consequently the fixed-order strategy is already optimal **in expectation**, among all adaptive strategies under this distribution and cost model.

### Exact proof by exhaustive recurrence

A partial observation is a pair of disjoint index sets `(Z,O)` of observed zero and one bits. Let `F` be the free coordinates; `L=sum_{j in O}w_j`, `M=sum_{j in F}w_j`. If `L>=77` or `L+M<77`, no further query is needed. Otherwise, for the minimum **sum of reads over every completion** of this partial assignment,

\[C(Z,O)=2^{|F|}+\min_{j\in F}\left(C(Z\cup\{j\},O)+C(Z,O\cup\{j\})\right).\]

The recurrence follows by induction: any correct tree must first query one free coordinate; each of the `2^|F|` completions pays one query, and the two child subcubes partition the completions. The checker enumerates **all 3^9=19,683** ternary partial assignments and verifies `C(empty,empty)=2734`; it then separately tests the fixed-order tree on all 512 complete assignments and obtains 2734. Its certificate stores a SHA256 digest of the canonical ordered DP table so that the full recurrence is reproducible rather than a scalar-only assertion.

A separate recurrence `D(Z,O)=1+min_j max(D(Z∪{j},O),D(Z,O∪{j}))` gives sharp minimum worst-case depth **9**, with terminal depth zero. The fixed-order tree attains 9; under the lexicographic secondary total-cost tie breaker, minimax also achieves total 2734.

## Theorem 2: explicit full-state guard

On each of the original `2^16=65,536` Port source states, inspect the six core bits `(u1,a,x,u2,w,b)` in any fixed order, immediately returning correction zero if a bit is not 2. Only if **all six bits are 2**, execute Theorem 1's fixed nine-bit threshold strategy. The fourth upper bit `B3` is retained in the state and not queried by this guard. This implements the R284EA correction Boolean function on the entire frozen input population.

The number of source-bit queries has exact uniform-input expectation

\[\frac{63}{32}+\frac{1}{64}\cdot\frac{1367}{256}=\frac{33623}{16384}\approx2.05218505859375.\]

The first term is the expected number of six-core bit tests before the first failure (or all six pass). The second term accounts for the probability `1/64` that all six pass. Direct enumeration of all 65,536 inputs gives **134,492 total bit probes**, worst-case **15**, with 84 full states requiring all 15 probes. The complete histogram is in the certificate.

This is a **constructive bound** on the full correction guard. Whether any strategy interleaving the six core-bit tests with nine threshold-bit queries has lower expected cost remains open. The theorem optimizes the exception predicate only; R284DZ's quotient recovery, determinant formation, R284DS's arc observer and output decoding are separate costs.

## Reproduction and next frontier

Companion script: `R284EB_exact_optimal_nine_bit_readout_checker.py` (Python 3 standard library); it creates `R284EB_exact_optimal_nine_bit_readout_certificate.json`. Full checks: 19,683 ternary subcubes, 512 exact labels and two decision trees, 65,536 complete source Boolean assignments. Integer recurrence and comparison are exact; no floating-point arithmetic or formal proof assistant used. Independent review: `NOT_REVIEWED`.

Next: run a fair complete-pipeline benchmark including bit extraction, R284DZ seven-bit quotient, R284EA guard, determinant cost, R284DS event-envelope preprocessing/query and recovery. Test whether interleaved full 15-bit decision trees improve source-bit probe counts enough to affect practical performance. Keep the original joint-state and BRC/native correspondence scopes unchanged.
