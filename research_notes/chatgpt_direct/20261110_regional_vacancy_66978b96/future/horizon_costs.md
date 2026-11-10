# Exact holding-horizon cost in the two-cluster family

## Proposition and original model

Let `b >= 3`, `B = 2^b`, `r = B-2`, `M = B-1`, and `k = r/2`.
Use the inherited three-target compiler with target 0's legal full keys
`1,...,M`. Initially all sources are absent. Request slots `0,...,k-1`
retain key 2, and the remaining `k` slots retain key 3. Every round executes

```text
reserve target 0 -> bind slot 0 to target 0 -> release source member 1
```

Compare the inherited single-point controller with the tracked-region
controller implemented here. Count all original BRC core primitive commands,
including conflict checks, real vacancy reads, creation, shared-key writes,
business binding and release. The same holding wrapper, when applied to the
entire process, adds the same cost to both sides.

For `T` rounds define

\[
\Delta(T)=C_{\rm region}(T)-C_{\rm point}(T).
\]

The exact difference is

\[
\boxed{\Delta(1)=0,\qquad
\Delta(T)=2\lfloor T/2\rfloor-8(k-1)\quad(T\ge2).}
\]

This is a comparison for the stated preparation and repeated operation family.
The general empty-region invariant and cumulative observation bound supply the
algorithms' correctness; this additional formula decides their original-command
cost ordering when this process and its horizon are given.

## Why the first observation is shared

At the root, both parity groups contain `k` initial request labels. Target 0
has `k` even and `k+1` odd legal residues. Only the odd branch has a strict
candidate deficit. Reading the next bit of its `k` key-3 labels sends them all
to low prefix `11`; low prefix `01` is empty. Both controllers therefore read

\[
2k+k=3k
\]

actual bits and create full key 1. The entire class

\[
P=\{1,5,9,\ldots,B-3\}
\]

has been proved free of old references. The tracked region preserves this class.
After binding key 1 in slot 0, it records one occupied point in `P`.

## Subsequent selections and the one extra observation episode

For the single-point controller, round 2 has `k+1` odd labels and `k-1` even
labels. The even branch is the only strict-deficit branch. Its untouched
`k-1` key-2 labels must reveal their next bit; all have bit 1, so low prefix
`00` is empty and key 4 is selected. This costs exactly `k-1` new vacancy
reads. These are the last new reads in the entire process.

After this binding, slot 0 holds key 4. The odd branch becomes deficient again;
its `01` class is empty and key 1 is selected. When slot 0 instead holds key 1,
the even `00` class is empty and key 4 is selected. All relevant initial labels
have already revealed the two needed bits. Induction therefore gives

\[
K_{\rm point}(j)=\begin{cases}1&j\text{ odd},\\4&j\text{ even}.\end{cases}
\]

The tracked region has only slot 0 inside `P`. Once key 1 is bound, its first
remaining legal point is 5. Binding 5 removes slot 0's final reference to 1,
restoring 1. Hence

\[
K_{\rm region}(j)=\begin{cases}1&j\text{ odd},\\5&j\text{ even},\end{cases}
\]

and it needs no further vacancy read. For `b=3`, `P={1,5}`; both points belong
to this fixed target's legal set. For `b>=4`, the same selection argument holds
inside the larger class.

## Accounting for every primitive-word difference

Every inherited vacancy-bit reader has length 8, so the avoided episode saves
`8(k-1)` commands. The actual physical Boolean immediately before every
creation is 1: this is the last actual query result on the first two observed
episodes, and otherwise the successful conflict check's result.

With physical last bit 1, the creation suffix is

```text
clear the q shared-key cells
add the current-record cell and source relation
add one shared-key relation for every 1-bit of K
```

Its length is `q+2+popcount(K)`, where `q` is the full-key width. Consequently
creating key 5 costs exactly one more primitive command than creating key 4.

The existing addressed binding's exact length, for a present target, is

\[
8b+q+10+\operatorname{popcount}(K)+4(1-\operatorname{bit}_{b-1}(K)).
\]

Keys 4 and 5 have the same bit at position `b-1`, for every `b>=3`, and their
popcounts differ by one. Binding key 5 therefore costs exactly one more command
than binding key 4. Conflict checks and releases have identical lengths.
Odd rounds use key 1 on both sides. Each even round thus contributes exactly
two additional commands to the regional process.

There are `floor(T/2)` even rounds, and the extra single-point reading episode
occurs exactly when `T>=2`. This proves the displayed formula for every integer
`T>=1`.

The exact word construction used in this proof is in the inherited
`parent_bundle/parent/check_vacancy.py` and
`parent_bundle/parent/parent/check_addressed.py`; no alternative primitive or
free full-key inspection is introduced.

## What the known horizon decides

Put `T0=8(k-1)=4r-8`. For the stated original-command objective:

| Horizon | Cost ordering |
|---|---|
| `T=1` | Equal |
| `2 <= T <= T0-1` | Tracked region uses fewer commands |
| `T=T0` or `T=T0+1` | Equal |
| `T >= T0+2` | Single-point process uses fewer commands |

For six slots the two equality horizons are 16 and 17. For fourteen slots they
are 48 and 49. The regional process still uses fewer old-request observations
after either crossing; the crossing comes from repeated key writing.

This gives a concrete answer to the known-future question: a process with a
specified horizon can choose according to its actual original-command total.
The sparse-region control costs and temporary representation remain separately
charged when those resources are part of the chosen objective.

## Actual primitive execution

`check_horizon_costs.py` executes the original BRC programs, checks every API
boundary, and compares every cumulative prefix through `T=18` for `r=6` and
through `T=50` for `r=14`. It saves per-round selected keys, three actual word
lengths, actual vacancy reads and cumulative totals in `horizon_costs.json`.
This is four completed original-kernel runs and 68 prefix comparisons.

The repeated ordinary word lengths exposed by those runs are:

| r | Operation using key 1 | Operation using key 4 | Operation using key 5 |
|---:|---:|---:|---:|
| 6 | create+conflict 23; bind 44 | create+conflict 23; bind 40 | create+conflict 24; bind 41 |
| 14 | create+conflict 24; bind 53 | create+conflict 24; bind 53 | create+conflict 25; bind 54 |

Release has length 11 in these instances. The first shared query adds 72 or
168 commands respectively. The single-point second round adds 16 or 48 more
commands, exactly as the formula requires. The general quantifier in the
proposition is supported by the word-construction argument above; the actual
execution covers the declared two finite preparations and horizons.
