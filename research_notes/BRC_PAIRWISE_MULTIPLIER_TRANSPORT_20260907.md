# BRC Pairwise Multiplier Transport — Round 7

Status: `PROVED PAIRWISE ROOT/REMAINDER TRANSPORT / ONE-ROOT PRIORITY STREAM / LOW-COST N-SHADOW ROUTING NEGATIVE / FINITE PERFORMANCE BENCHMARK`
Date: `2026-09-07`
Parents: `t0.brc_multiplier_transition`, `t0.brc_multiplier_priority_jump`, `t0.brc_mod8_sparse_transition`

## 1. Question

Round 6 established a useful structural multiplier order and exact direct jumps from
the single m=1 BRC state. Round 6 also asked whether N-visible low-cost shadow
coordinates could choose a better multiplier order.

Two distinct results emerged:

1. simple N-dependent shadows did **not** add stable routing information beyond a
   fixed learned order in the finite train/validation study;
2. the structural order itself can be executed more cheaply by transporting each
   exact state directly from the previously tested multiplier instead of restarting
   every candidate from m=1.

The second result is exact and is toolized here.

## 2. Negative result: cheap N-shadow routing

Training population:

- every p<q among the 143 primes in [101,997];
- 10,153 semiprimes.

Validation population A:

- 20,000 deterministic p<q samples from primes in [1009,4999], seed 20260906.

Validation population B:

- 30,000 deterministic p<q samples from primes in [5003,19997], seed 20260907.

All rankings used the current exact static odd-N representative set

`m mod 8 in {0,1,3,5,7}`,

so there are 62 candidates through m=100.

A globally learned fixed greedy order trained on the first population achieved:

- validation A mean/median first-hit rank: about `10.588 / 7`;
- validation B: about `11.086 / 7`.

The best simple adaptive feature tested was the initial BRC phase quartile

`floor(4*R/(2J+1))`.

Its cell-specific trained orders gave:

- validation A: about `10.654 / 7`;
- validation B: about `11.098 / 8`.

Other tested shadows included `N mod M`, `J mod M`, `R mod M`,
`(J mod M,R mod M)`, and products with phase bins. None improved both independent
validation populations over the fixed learned control.

**Kill decision:** do not promote these low-cost shadow coordinates as an adaptive
multiplier router. This is a finite negative result, not a theorem of statistical
independence.

The current N-independent structural priority remains preferable as a production
default because it is prior-free, interpretable and already independently
validated.

## 3. Pairwise transport theorem

Assume an exact source state

`m*N = J^2 + R`, `0 <= R <= 2J`.

Let the target multiplier be t and put

`beta = sqrt(t/m)`.

Choose the canonical dyadic precision B so that

`J < 2^(B-1)`,

and define the exact lower dyadic scale

`A = floor(2^B * beta)`.

Use the lower root candidate

`q = floor(A*J/2^B)`.

Because

`0 <= beta - A/2^B < 2^-B`,

we have

`0 <= beta*J - q < J/2^B + 1 < 3/2`.

Write

`sqrt(mN)=J+delta`, `0<=delta<1`.

Then

`sqrt(tN)=beta*(J+delta)`

and therefore

`sqrt(tN)-q < beta + 3/2`.

The candidate is a lower bound because `q<=beta J<=sqrt(tN)`. Hence the exact
integer target root is recovered only by upward BRC basin crossings.

A safe integer correction bound is

`ceil(sqrt(t/m)) + 1`.

Consequences:

- if `t<m`, at most **2** corrections;
- for `1<=m,t<=100`, at most **11** corrections.

## 4. Root-free remainder update in both directions

Let

`d=q-J`.

Then

`tN-q^2`
`= R + (t-m)N - d(2J+d)`.

This identity remains exact when `d<0`, so downward multiplier jumps need no
special square-root path.

Starting from candidate `(q,G)`, while

`G >= 2q+1`

perform

`G <- G-(2q+1)`,
`q <- q+1`.

At exit,

`q=floor(sqrt(tN))`,
`G=tN-q^2`.

No root of `tN` is materialized.

## 5. Why pairwise execution matters

The Round-6 structural order is deliberately nonmonotone, for example it begins

`1, 96, 45, 48, 63, ...`.

The previous direct-jump interface correctly reached each target from m=1, but
it discarded the already known exact state after every failed candidate.

Pairwise transport instead executes

`1 -> 96 -> 45 -> 48 -> 63 -> ...`

and carries `(J,R)` forward along that actual priority path.

This preserves exactly the same multiplier ranking and factor-search semantics.

## 6. Production implementation issue discovered

The current pre-Round-7 implementation of

`prioritized_odd_multiplier_states(n)`

iterates `direct_multiplier_jump_from_one(n,m)` for every priority candidate.
That function materializes `initial_multiplier_root_state(n)` internally.
Consequently the implementation can repeat the N-dependent initial root even
though the Round-5 theorem says a stream needs only one initial root.

The new pairwise priority surface enforces the intended invariant:

`one initial root -> all later priority states by exact transport`.

This is an implementation/performance issue, not a mathematical correctness
failure of the direct-jump states.

## 7. Validation

Reference regression for the new subtool includes:

- exact all-pairs transport on the 62 representative multipliers for odd N<160;
- random bidirectional source/target checks at 128..8192 bits;
- exact reconstruction against direct integer roots;
- downward-jump correction bound <=2;
- global m,t<=100 correction theorem;
- structural priority sequence state equality;
- a mocked call-count certificate that the complete pairwise priority sequence
  materializes `initial_multiplier_root_state(n)` exactly once.

Independent research harness checks on a wider small-N range observed no failure.
The largest correction count seen in the all-pair experiment was 10; the tool
registers only the proved bound 11.

## 8. Finite performance

Two baselines were separated:

1. `current-priority-sequence`: emulates the current sequence API, including
   repeated m=1 initial-root materialization;
2. `optimized-direct-from-one`: an idealized control that caches m=1 once but
   still computes every priority state independently from that base;
3. `pairwise-chain`: the new state-to-state transport along the structural order.

On 500 deterministic random odd N values per bit size, full priority-stream
timings gave approximately:

| N bits | current / pairwise | optimized-direct / pairwise |
|---:|---:|---:|
| 128 | 1.55x | 1.25x |
| 256 | 1.83x | 1.22x |
| 512 | 2.22x | 1.41x |
| 1024 | 2.27x | 1.25x |
| 2048 | 2.24x | 1.21x |
| 4096 | 2.14x | 1.07x |

Constructed probable-prime semiprimes with guaranteed m<=100 immediate hits
also preserved a roughly 1.16x--1.32x gain over the optimized direct-from-one
control in the tested 128..2048-bit cohorts.

These are Python/environment finite timings, not asymptotic complexity claims.

## 9. Relation to the newer mod-8 sparse stream

The pairwise theorem and `t0.brc_mod8_sparse_transition` solve different
execution problems:

- mod-8 sparse transition is best for an increasing representative stream and
  compiles exact one/two-step transitions with zero extra checked-in table;
- pairwise transport is best for a nonmonotone priority permutation and allows
  both upward and downward multiplier moves.

They share the same retained BRC state `(root,remainder)`. Neither requires
Boolean-support recovery or a new top-level BRC family.

## 10. Boundary / next attack

- Exact finite integer transport only.
- Current executable boundary remains multiplier <=100 because it inherits the
  production table/router horizon.
- Pairwise scale constants are cached runtime data, not a new checked-in payload.
- Difference-of-squares / multiplier-Fermat / Lehman factoring remains classical.
- No asymptotic factorization speedup is claimed.
- The tested simple N-dependent BRC shadows are not promoted.

The next high-value target is the **>100 multiplier horizon**: remove the current
O(M) checked-in/cached predictor dependence while preserving bounded local BRC
corrections, or find a sparse multiplier family whose factor-ratio coverage per
tested state beats a full Hart/Lehman-style scan.
