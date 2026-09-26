# Exact prefix-checkpoint / backward-row contraction

Author-executed bounded research, shared context, not an admitted Result.
Activity: RA-CAAAC604CB513AEA8BBC1DFC. This is a domain operator composed
from the actual ordered native instrument and typed modular columns.
It is not a new universal BRC family or a polynomial factoring algorithm.

For a fixed recorded prefix h of length i, the full unnormalized row obeys

    v_(j+1)(z) = [v_j(z) + (-1)^h_j T_j v_j(P_j^-1 z)]/2.

Retain the exact earlier prefix v_k as a sparse dictionary. Construct it
forward by contributing v_j(w)/2 to w and (-1)^h_j T_j v_j(w)/2 to P_j w.
Collisions are signed vector additions. To query v_i(z), recursively apply
the displayed identity down to k, with dictionary lookups at the leaves.
Every T_j is the actual temporal ordered word. All 61 coordinates are
retained unless an independently replayed full-word D6 codec applies.
No order, factors, multiplicative logarithms or ideal phase propagator are
used. This is the usual contraction/time-space idea applied to this exact
instrument; no worldwide priority claim is made.

## Induction and resumability

The forward construction is a relabelling of the two terms in the same
native recurrence. The checkpoint therefore equals the actual raw prefix
row map, including cancellations and dyadic denominators. Backward induction
then proves every returned row. Orthogonality is not needed for this row
identity, although it is required by the parent single-walker sampler.

Appending a measured bit never changes an earlier checkpoint. A request
shallower than the retained checkpoint is recomputed from v_0 rather than
using an invalid later state. Building a new checkpoint commits only after
an entire layer is finished. A budget interruption can discard partial work
but leaves the old checkpoint and sampler's uncommitted auxiliary coin
intact. Repeated work is charged again. This is live-object recovery, not a
durable cross-process cursor or a bounded probability of budget exhaustion.

## Cost, including the remaining exponential

Without exploiting collisions the checkpoint holds at most 2^k rows and
uses at most 2^k-1 forward input-row updates. A single depth-i query visits
exactly 2^(i-k+1)-1 recursion nodes in this implementation. Each non-leaf
applies up to i admitted native feedback words and combines complete rows.
Charge their actual application cost, D, integer bit lengths, modular
arithmetic, source admission and certificate storage separately.

At k=floor(i/2), this changes the naive unshared binary-query bound from
O(poly(i,D,b) 2^i) to O(poly(i,D,b) 2^(i/2)), conditional on polynomial native
word application cost at bit size b. A depth cap gives an explicit tradeoff.
Summing two point queries per readout round preserves the exponential
2^(t/2) factor up to polynomial overhead. At ordinary Shor width t about
2 log2 N it is still O(N) up to polynomial factors: it does not improve the
existing full-work-state worst-case bound or prove efficient dequantization.

Only row storage is bounded here. The actual modular-column caches,
positive-path observations and exported certificates can be larger and are
reported. No total-memory improvement follows from the checkpoint row count.

## Actual checks and measured tradeoff

`check_checkpoint.py` completed with 616 actual BRC core calls. For N=21,
a=2,t=4, all 31 bit prefixes (including zero-mass prefixes) and all 32 work
carrier labels were queried in each of D6 and D61: 992 exact complete-row
comparisons per dimension. Reference rows came from the actual selected
native instrument, not ideal QFT. The checkpoint and memoized single walkers
also gave identical events with the same auxiliary/local random tape.
Four invalid-input controls were rejected. Both an initial query-budget
interruption and an interruption during checkpoint construction resumed
correctly on the same live object.

One separate N=251,a=6,t=8 fixture used the certified full-D61 bank with
payload feecbc02808991f6d7b1e2c3179c8da2018b76901ef34c26ef0d28b65729dd5c.
It queried label 1 at fixed prefix (1,0,1,1,0,1,0). All four methods returned
the same exact row. The validation-only explicit current state had 125 rows.

| Checkpoint depth | Retained rows | Forward row inputs | Query nodes | Computed modular columns | Adder digit replays | Native feedback applications | One query seconds |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 255 | 135 | 54,436 | 11 | 0.07260 |
| 1 | 2 | 1 | 127 | 72 | 32,290 | 11 | 0.04088 |
| 2 | 4 | 3 | 63 | 42 | 23,684 | 12 | 0.02703 |
| 3 | 8 | 7 | 31 | 30 | 19,689 | 15 | 0.02110 |

Setup admission preceded the timed query; forward checkpoint work is inside
that timing. These are single observations, not a statistical speed claim.
More checkpointing reduced recursive and modular work but increased native
feedback applications. The fixture uses t=8 rather than default t=16 and is
an instrument test, not a factoring success-rate benchmark. Exact evidence,
source hashes, typed certificates and complete rows are in the result gzip.

The next mathematical target is to beat the 2^(i-k) label constraint
contraction using structure available without already knowing the order.
