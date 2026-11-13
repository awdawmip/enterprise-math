# PREFIX-636 (R2): Exact sliding-window native BRC action-pattern transfer queue

Author-side TASK_RESEARCH, 2026-11-10 (Asia/Shanghai). Researcher-ID `EM-X6-BDF1CC`; Research-Activity-ID `RA-95917859B085C0142E5E513C`. Formal X6 rotation Task-ID `RS-X6-NATIVE-ROTATION-DYNAMICS` is a broader, independently controlled target. This note is a durable author proof/experiment, not a formal Result or independent review.

## Scientific identity and scope

Frozen native scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. P000 V5, its six signed spatial axes and separately typed time, and the original 48 STAR phases, 96 ports and 576 original labelled BRC actions remain fixed. Source positive weights are `(1,1,1,1,0,0)`; one original action family uses a nonnegative gate `g`. Initial four-phase probe `d=e4+e11+e14+e32`, intensity `lambda>0`. The 96-port graph is a restricted typed BRC carrier/observer, not a substitution for the six-dimensional native Cell ontology.

This builds on PREFIX-633 (original action-ID DAG), PREFIX-634 (single pattern) and PREFIX-635 (Aho–Corasick multiple-pattern first/second moment and event query; PR #1912, immutable head `305fff0848138e1d03ba88b4d527eebdf8907602`).

## Theorem A: original-labelled weighted transfer

Fix a finite set of original action-ID pattern strings and its shared Aho–Corasick automaton with `S` states, output mask `h`, and transition `delta(q,action)`. Set `D=96*S` product states `(port,q)`. Define row-vector transfer matrix `T_F(g)` for a forbidden pattern-index set `F` as follows: for **each original labelled action** `a: s->d` with its actual BRC nonnegative weight `w_a(g)`, add this weight to matrix entry from `(s,q)` to `(d,delta(q,a))`, unless `h(delta(q,a)) ∩ F != empty`. Equal-source/destination actions are counted with their original multiplicity and classified by individual action ID *before* accumulation.

For an actual native state `r_t` at a window entrance, let `iota(r_t)` lift each port mass to automaton state zero. Then, for every finite window length `L>=1`, all nonnegative rational gate sequences and intensity `lambda>0`:

```
A_F(t,L) = iota(r_t) T_F(g_{t+1}) ... T_F(g_{t+L}) 1,
Z(t,L)   = sum_s r_{t+L}[s].
P(at least one pattern in F) = 1 - A_F(t,L)/Z(t,L)  if Z>0.
```

Here `A_F` is the total mass of full original labelled paths avoiding every pattern in `F`. Proof: induction on ordered action-ID prefixes; the transition follows exactly one deterministic AC state and the BRC factor is the product of original edge weights, so the summed row-vector coefficients coincide with exact path masses. Zero gates delete their zero-weight branches and are covered. For two patterns `i,j`, the simultaneous-hit mass is exactly `Z - A_{i} - A_{j} + A_{i,j}`. When `Z=0`, mass equalities remain meaningful, but conditional probabilities are undefined.

For count moments introduce the truncated polynomial ring
`R=Q[x_1,...,x_p]/(monomials of total degree>=3)`. Multiply every AC edge by the degree-two truncation
`exp(sum_i h_i x_i) = 1+sum_i h_i x_i + (sum_i h_i x_i)^2/2`. The chronological product over `R` yields a generating element `H(x)` whose derivatives at zero are:
```
H(0)=Z;
partial_i H(0)=sum_path w(path)*C_i(path);
partial_i partial_j H(0)=sum_path w(path)*C_i(path)*C_j(path).
```
For `i=j`, the second derivative accounts for the `2!` coefficient, including self-overlap. The proof is multiplication of truncated exponentials along each original action-labelled path, followed by sum over all paths. This algebraic extension is proved for any finite typed weighted automaton; the executable native certificate below validates **avoidance** operators, while rolling polynomial moments remain the next implementation unit.

## Theorem B: noncommutative rolling transfer with two-stack aggregation

The matrices compose in chronological order and generally do not commute. Maintain two stacks: the back stack stores the product of matrices bottom-to-top; the front stack stores products top-to-bottom. Append the new step matrix to back; remove the oldest matrix from front, reversing/back-transferring the entire back stack if front is empty. For a query, apply `iota(r_t)` first to the front aggregate, then to the back aggregate, and sum all terminal states. There is no need to materialize their combined cross-product matrix.

Every matrix is inserted into back once, transferred into front at most once and removed once. Thus over `W` successive length-`L` windows, the total number of matrix–matrix compositions is `O(L+W)` and queue storage is `O(L)` matrices. Single-update cost is amortized `O(1)` matrix compositions (worst-case `O(L)` during transfer). A balanced segment tree over a circular sequence gives worst-case `O(log L)` matrix compositions per update.

In the dense rational field-operation model, avoidance transfer costs `O((L+W)D^3 + W D^2)` for rolling products and root queries, and `O(LD^2)` storage. Constructing a one-step matrix costs `O(576S)` per incoming gate after AC preprocessing `O(576S)`. Updating the two actual native entrance/exit 96-port states costs `O(576)` per slide each, by the **original typed BRC step**, and provides `Z` without replay from initial time. For degree-two polynomial moments the number of ring coefficients is `1+p+p(p+1)/2`; a ring product requires `O(p²)` rational operations, giving a conservative `O((L+W)D³p²)` field-operation bound. Rational numerator/denominator bit lengths, full input conversion, initial `r_t` reconstruction, and dense matrix constants remain explicit separate costs. No universal wall-clock improvement follows just from transfer count.

If the first `r_t` comes from PREFIX-629/630 phase-only reconstruction using minimum extra gate memory, that exact decoder remains a separately charged initialization. Subsequent windows require actual newly arriving gates. No inversion of a zero-gate transition is needed.

## Complete original-native exact experiment

Standalone Python checker `PREFIX636_selfcontained_native_rolling_ac.py.gz.b64` rebuilds original 48 STAR phases, 96 ports, **576 enumerated original action IDs**, uses exact `Fraction`, and shares one 7-state AC automaton for:
```
P0=(485,316,52,174)
P1=(52,174)
```
It sets `F={P0,P1}` (union hit), maintains the exact front/back product queue and rolling `r_t,r_{t+L}`, and independently compares **every** output to a fresh per-layer original-labelled native avoidance DP. Zero-gate, rational-gate and all-one cases are included; the query does not expand exponential path sets.

Executed **12 groups, 182 exact window comparisons**, all assertions pass. For 70-gate all-one histories, exact matrix-composition counts and the first-window probability are:

| L | windows | rolling compositions | naive L-layer recomputation compositions | P(any motif) |
|---:|---:|---:|---:|---|
| 12 | 55 | 115 | 605 | 7673/172032 |
| 20 | 47 | 119 | 893 | 3723049/44040192 |
| 32 | 35 | 125 | 1085 | 8419288165/60129542144 |

All 9 short groups also pass, using `L=4,5,6` with 13 gates and three gate classes. Counts compare arithmetic **matrix compositions**, not wall-clock timings; sparse native per-layer DP can be faster at these finite sizes.

## Reproduce, integrity and open question

The two attachments are `gzip(UTF-8)` encoded as base64, each on one line; decode via `base64 -d | gzip -d`. The executable Python 3 file requires only the standard library.
- Uncompressed Python SHA256 `c26436f595c176eb5ec43b2909c3c0e5fbbed6cff75fc7f413c3efcf64889075`.
- Uncompressed complete JSON SHA256 `a869096e45d87e51109e86e0f1d52c0d835529985c4ac8dcf264d5fa4643544b`.
- Results status `ALL_ASSERTIONS_PASS`.

**Next exact test:** implement the second-order polynomial transfer and cross-check sliding first and second moments with PREFIX-635; then measure exact integer bit-length and sparse/dense memory/cost crossovers. This is a standalone author-side BRC-algorithm theorem and exact experiment, pending independent mathematical review.