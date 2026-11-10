# Original BRC integration: arbitrary observed bits and weighted evidence

## Runtime path

`check_cost_aware_kernel.py` reuses the prior compiler, all original primitive
words, the original non-reserve API, and the maintained label/alias tree.
Its reserve path executes the original conflict check and the original creation
suffix selected by the **actual** Boolean immediately before creation.

Three changes carry the new behavior:

1. `read_bit(label, bit, reason)` invokes the original eight-command bit reader
   at any bit position. Each initial label has a mask/value pair of actually
   observed bits. A high-bit observation does not pretend that lower bits were
   read. If later fallback reaches an already observed bit, it advances the
   low-prefix grouping without another physical read or a fictitious Boolean
   register update.
2. A homogeneous observed high bit certifies the opposite half-region. The
   implemented `MaskedRegionEvidence` preserves exact per-slot marks and
   multiplicities through bind/copy/drop. The main family uses its weighted
   sparse range-minimum tree; it has zero full-candidate reference comparisons.
3. An optional finite-horizon `Planner` consumes only current per-slot
   mask/value observations. Its read actions run the original bit reader;
   its creation action runs the original conflict and creation words. Actual
   binding fills slot zero's known residue for the next round.

All exact request-table inspection is below the module's verification boundary.
Whole original matching, answers, two identity representations, old prefix
counts, arbitrary observed bits, and masked regional occupancy are checked at
every API boundary. Every physically read initial `(slot, bit)` pair is unique.

The weighted target interval is compiled once per declared target; each has at
most two modulus blocks. Original full-key width and target-library construction
remain explicit. Main region updates and queries have the selector's O(b)
word-operation bound. Fallback retains a visibly counted O(Mr) masked-candidate
reference search when observations outside the low-prefix tree require it.
The original low-prefix traversal, weighted-tree visits, and candidate-prefix
comparisons are separate counters. This is not a claim of uniformly O(b)
fallback over arbitrary masks.

## Actual key-dependent word length

Let `q` be complete-key width, `b` the residue width, and `L` the actual Boolean
before creation. The original creation suffix length is

\[
q+2+\operatorname{popcount}(K)+4(1-L).
\]

The addressed binding of a present source has length

\[
8b+q+10+\operatorname{popcount}(K)+4(1-\operatorname{bit}_{b-1}(K)).
\]

Thus the key-dependent creation/binding/release part is

\[
w_b(K)=2\operatorname{popcount}(K)+4(1-\operatorname{bit}_{b-1}(K)).
\]

`kernel_word_lengths.json` checks 162 creation-word lengths (both L values)
and executes 81 addressed bindings for every target/key in the stated
one-, two-, six-, and fourteen-slot compilers. Release and conflict-check
lengths are included in actual process totals rather than absorbed into w.

## Two-cluster preparation and exact cost

For `r=2^b-2`, `b>=3`, half of the initial requests retain full key 2 and half
retain key 3. Each round creates target 0, binds slot 0, and releases source
member 1. Directly reading bit `b-1` of every slot proves `[B/2,B)` empty with
exactly r real reads. Execute those reads before the already required source
conflict check; its success supplies physical L=1. The weighted region then
alternates full keys `B/2, B/2+1` with no additional old observation.

With the inherited three-target compiler, the complete total is

\[
C(T)=8r+(8b+2q+41)T-(T\bmod2).
\]

Here `q=b+2`, so it is also `8r+(10b+45)T-(T mod 2)`.
Moving this initial high-bit probe after the conflict check adds exactly four
commands once, because its final observed value is 0 and the original creation
suffix must clear that physical result. Both orders were actually executed.

| r | rounds | old point | old region | high-half weighted | high-half reads |
|---:|---:|---:|---:|---:|---:|
| 6 | 1 | 150 | 150 | 122 | 6 |
| 6 | 8 | 696 | 688 | 648 | 6 |
| 6 | 32 | 2520 | 2536 | 2448 | 6 |
| 14 | 1 | 256 | 256 | 196 | 14 |
| 14 | 8 | 920 | 880 | 792 | 14 |
| 14 | 32 | 3032 | 3016 | 2832 | 14 |

`kernel_family.json` executes seven declared strategies at r=6,14 and
T=1,2,8,32 (56 original-kernel runs), with the exact cumulative formulas checked
at every actual prefix. The older even-first and common-odd-entry expansion
strategies remain in the comparison. Under the shared odd-class first query,
the weighted expansion-minus-no-expansion difference is zero at T=1 and
`8*(r/2-1)-4*floor(T/2)` thereafter. All primitive commands, including unfavorable
probe episodes, are retained in the results.

## Failure, aliases, physical results and protection

Eight focused cases cover mixed high bits, opposite empty half, aliases and
last-reference restoration, source execution retaining request identity,
nonempty residue zero, empty binding, an initially blocked source, and an
existing source that must preserve its original creation.

On six initial full keys 1 through 6, the high-bit probe cannot certify an empty
half. The inherited guaranteed traversal completes with 15 total physical
reads, including a cached high bit promoted into a low prefix without rereading
it. If the first source is blocked, the six earlier probe reads are fully
charged and the original conflict result is returned.

The protected execution uses the original holding interval in both gate phases:
371 body commands plus the unchanged 31-command wrapper, hence 402. Each phase
attempts a complete competing bind at all 372 body boundaries; each is blocked
while the holder owns the interval, and the bind succeeds after real handoff.
This is the stated boundary-attempt schedule.

The doubled original primitive sequence also passes every one of its 468
single-omission positions, checking endpoint, adaptive word, initial bit-read
set, and final masked region. No broad earlier enumeration is repeated.

## Finite-horizon planner executed on every declared preparation

`kernel_minimax.json` uses the parent's exact mask-state Bellman planner.
Every residue-zero old request is represented by the **nonempty** complete key
B, and every other residue x by full key x. Thus all B^r preparations actually
exist in the original compiler. Every chosen round binds slot zero and releases
the corresponding source. Planned bit queries precede the required conflict
check, so successful creation has physical L=1.

| slots | target sequence | complete preparations | fixed business cost | planner worst variable cost | actual worst total |
|---:|---|---:|---:|---:|---:|
| 2 | (0) | 16 | 62 | 28 | 90 |
| 2 | (0,1) | 16 | 127 | 34 | 161 |
| 3 | (0,1,2,0) | 64 | 251 | 64 | 315 |

For each of the 96 preparations, actual original-command cost minus fixed
business cost equals the exact control replay and is at most the planner
value. Each maximum has an actual witness. The cost model includes eight
commands per observed bit and w(K) per selected key; it keeps full business
constants separate rather than treating them as free.

A further execution acquires the high-half evidence with two real reads for
two old key-1 requests, then asks the planner to create targets 0 and 1. It
chooses keys 3 and 6, for 151 commands and two old-bit reads. The myopic weighted
selector chooses 2 then 4, for 159 commands and three reads. The next target
changes the useful first safe key. This conditional, already-acquired-evidence
example is distinct from minimizing the worst cost over entirely unknown
initial residues.

## Reproduction

From a package root containing the unchanged prior dependencies:

```bash
python optimization/check_cost_aware_kernel.py family --output replay_family.json
python optimization/check_cost_aware_kernel.py regressions --output replay_regressions.json
python optimization/check_cost_aware_kernel.py minimax --output replay_minimax.json
```

The other modes are `word_lengths`, `protected`, `omissions`, and `future_plan`.
The scientific status is author derivation with the explicitly scoped original
BRC executions and finite control checks recorded in the corresponding files.
