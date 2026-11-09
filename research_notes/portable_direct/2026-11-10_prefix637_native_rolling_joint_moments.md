# PREFIX-637: Exact rolling first/second multi-pattern counts on the original native BRC action graph

**Date:** 2026-11-10 Asia/Shanghai. **Research mode:** author-side exploratory TASK_RESEARCH, no formal CLAIM/Result/review. **Frozen scientific input:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. **Continuation:** PREFIX-635 (multi-pattern moments) and PREFIX-636 (noncommutative two-stack sliding avoidance transfer, PR #1917, head `32ba9fd2e52d6537cfb326a0bc2a4b49443a1488`).

**Native Researcher-ID:** `EM-X6-AB58FD`; **Research-Activity-ID:** `RA-74D5A1F6AC6B480BF13ED09E` (Source session-start main@`d5b422aafcb734da39ebbd8192953e3f8f3047d6`, verified). No formal CLAIM was acquired.

## Statement and typed scope

Work within the declared restricted, original-labelled BRC observation graph with 48 STAR phases, 96 ports, 576 original actions, source weights `(1,1,1,1,0,0)`, a nonnegative rational gated action family, and four-point input `d=e4+e11+e14+e32` of rational intensity `lambda>0`. This is an observer/path-fiber carrier inside P000's native signed X6, not a new native plane, a replacement for the six spatial axes, or a claim of a full physical rotation law. Every step and action ID remains ordered; the quotient is only for the stated pattern-count observers. Time indexes transition order rather than a seventh spatial axis.

For an arbitrary finite family of action-ID words `P_1,...,P_p`, form the Aho–Corasick DFA, transition `delta(q,a)` and output indicators `h_i(q,a)∈{0,1}` indicating a word occurrence completed by the current original action. For each path `pi` in a length-`L` suffix window, let `C_i(pi)` count occurrences including overlaps and let `w(pi)` be its original exact nonnegative weight. Define six coordinates for `p=2`:

```text
(z,u0,u1,v00,v01,v11)
  = (sum w, sum w*C0, sum w*C1,
     sum w*C0^2, sum w*C0*C1, sum w*C1^2).
```

**Theorem (exact rolling moment transfer).** Encode each original labelled edge `a` of weight `w` and completed-pattern mask `(h0,h1)` by

```text
E_a=(w, w*h0, w*h1, w*h0^2, w*h0*h1, w*h1^2).
```

For two chronological operators/moment aggregates `A=(z,a,b,c,d,e)` and `B=(Z,A,B,C,D,E)`, define

```text
A ⊙ B = (
  z*Z,
  a*Z + z*A,
  b*Z + z*B,
  c*Z + z*C + 2*a*A,
  d*Z + z*D + a*B + b*A,
  e*Z + z*E + 2*b*B
).
```

Add aggregates coordinatewise, and combine edges of the same ordered source/product-state and target/product-state by addition, **after classifying each original action ID**. For nonnegative rational gates (including zero gates), these sparse `96S × 96S` matrices, composed with `⊙` and ordinary matrix summation, give the exact six moment sums for any finite window. This multiplication is associative and is generally noncommutative at matrix level. The original FIFO two-stack transfer queue can therefore maintain rolling window products using `O(L+W)` matrix compositions for an initial `L`-step window and `W` successive windows, and `O(L)` stored matrices. An update has amortized `O(1)` matrix compositions, with worst-case `O(L)` at a stack transfer.

**Proof.** For two concatenated path fragments, `C_i(uv)=C_i(u)+C_i(v)` when the DFA state at the join is retained: a hit crossing the join is assigned to the transition where the word ends. Expand the first and second powers of these sums and multiply independent path weights. This gives the displayed six-coordinate product, which is the degree-two jet of the product of formal moment generating series `exp(sum_i x_i C_i)`; associativity follows from series multiplication in the degree-2 truncated polynomial ring. Summing over the path-fiber gives the matrix product. The two-stack FIFO invariant preserves the chronological product even though matrices may not commute. Each appended operator is transferred at most once, giving the amortized composition bound. The construction holds at `Z=0` for raw moment sums; probabilities and normalized covariance require `Z>0`. The argument extends to `p` patterns with `1+p+p(p+1)/2` coefficients and `O(p²)` field operations per coefficient product. QED.

**Complexity account.** Write `D=96S`. With dense matrix multiplication, the conservative arithmetic bound is `O((L+W)D³p² + WD²p²)`; stored aggregates use `O(LD²p²)` field elements. Step construction needs `O(576S)` action processing, and fresh entrance/exit BRC states must be maintained or recovered using their original semantics. If beginning from only the 48-phase endpoint, PREFIX-629/630 decoding and minimum history registers are separate inputs and costs. Rational numerator/denominator bit lengths, matrix sparsity, output format, and the full original-input conversion remain separately chargeable. The bound is **matrix-product count**, not evidence of wall-clock speedup over sparse per-window dynamic programming.

## Exact native computation and new overlap witness

The attached standalone `PREFIX637_rolling_native_joint_moments.py.gz.b64` reconstructs the original graph and tests patterns

`P0=(485,316,52,174)`, `P1=(52,174)`.

These have an inclusion relationship: each P0 occurrence includes a P1 occurrence. The lifted algorithm also distinguishes whether there are **additional** P1 occurrences along a path carrying P0.

For all-one gates, `t=4,L=6,n=11,lambda=5/4`, the exact aggregate is:

```text
Z=26880
mass*C0=400
mass*C1=2560
mass*C0^2=400
mass*C0*C1=410
mass*C1^2=2600
E[C0]=5/336
E[C1]=2/21
Cov(C0,C1)=781/56448 > 0.
```

In particular `sum_pi w(pi) C0(pi)*(C1(pi)-1)=10` exactly. For `L=4`, the corresponding raw values are `Z=6720, u0=10, u1=280, v01=10`: there is no extra P1 hit conditioned on P0 in that shorter window. This cleanly discriminates overlapping-history multiplicity that a boolean "ever hit" observer cannot supply.

**Reproducible checks:** 15 groups; 87 exact successive windows; 18 windows checked additionally against fully enumerated original action sequences, allowing at most 24,192 explicitly enumerated paths under the prior PREFIX-631 counting bound; and all 87 windows also checked against a *fresh independent native action-by-action DP*. Gate families comprise all ones, rational varied gates, periodic zero gates, and all-zero gates. The 7-state AC DFA and 576 original action IDs are enumerated in the executable file; no floating point is used. All tested comparisons passed.

| Historical case | Windows | FIFO matrix products | Naive per-window aggregate products |
|---|---:|---:|---:|
| n=26, L=6, all-one | 17 | 33 | 85 |
| n=30, L=7, rational | 20 | 40 | 120 |
| n=34, L=5, periodic zeros | 26 | 44 | 104 |

These counts validate the amortized **aggregate composition** behavior for the implemented cases. The independently regenerated DP is a correctness oracle, not a measured speed comparison.

## Artifact validation and how to reproduce

Files in this directory:

- `PREFIX637_rolling_native_joint_moments.py.gz.b64`: gzip+base64 of executed Python 3 checker, raw SHA256 `6df9da5647d265ecdc456591e5e208daa977ccab9d1ce5247b1b7acbea725a3e`.
- `PREFIX637_rolling_joint_moments_results.json.gz.b64`: gzip+base64 complete 15-group/87-window evidence, raw SHA256 `ae77bda96f61b5d0aa848ac148c547b2235f444ccf3dc2cb2743fe6f341dc790`.

Decode with Python's `base64.b64decode` then `gzip.decompress`; compare SHA256 of raw decoded bytes to the above. To rerun in bounded memory/time, use `python PREFIX637_rolling_native_joint_moments.py base`, then each of `long1`, `long2`, `long3` **in a separate process**, then `python PREFIX637_rolling_native_joint_moments.py merge`. `merge` checks four group certificates and writes the aggregate JSON. The combined output is `ALL_ASSERTIONS_PASS 87 explicit 18 path_upper 24192`. The three long groups were also separately executed against the unchanged scientific calculation functions; their saved exact JSON was incorporated into the combined result. No claim is made for a formal verifier, an independent Driver review, or a formal native Result.

## Mother-question relation and next discriminating work

This theorem delivers a reusable **typed query-preserving path-fiber composition** for two count observers. The formal upper-X6 rotation task additionally asks for arbitrary-oriented-triad signed C6 generators, their global generated group and operation-safe full native Cell/path lifts. The exact remaining question for this line is whether a smaller invariant quotient of the `96 × S` product system is closed under all allowed gate sequences *and* retains the first/second motif-count jet after further native composition. Find either a constructive lumping/bisimulation certificate for the selected original action family or a minimal pair of states whose current moments coincide but separate after an allowed continuation. Preserve source action IDs, incoming phase, branch and history type when testing any quotient.

**Evidence level:** author-proved algebraic theorem + local exact native computational tests; independent mathematical review/promotion pending. **P000/worldview:** unchanged.
