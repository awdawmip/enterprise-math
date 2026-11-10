# Exact key costs and weighted selection on certified bit-mask regions

Author derivation, 2026-11-10. Scientific parent:
`enterprise-math@9bb764203fcb2f1ec6ec5c82b76219f951c033f4`.
The code in `selector.py` uses already obtained absence evidence and recorded
slot effects. Its finite checks are in `selector_checks.py` and
`selector_results.json`. Actual BRC executions are supplied by the companion
kernel integration.

## 1. The original command objective

Let `b>=1`, `B=2^b`, `1<=M<=B`, and let the legal keys of target `t` be the
positive interval `A_t,...,A_t+M-1`, with `A_t=1+tM` in the inherited model.
Let `n` be the complete-key width. Consider one successful reserve, a binding
of its present source into one slot, and the fixed source release operation.
The actual Boolean immediately before the creation suffix is `L in {0,1}`.

The inherited compiler constructs:

* creation suffix length `n+2+popcount(K)+4(1-L)`;
* present binding length `8b+n+10+popcount(K)+4(1-bit_(b-1)(K))`;
* a source-conflict check and release word whose lengths are independent of
  the selected key within this target.

Thus, writing their fixed lengths as `S_t` and `D_t`, the complete round has
length

\[
S_t+D_t+8b+2n+12+4(1-L)+w_b(K),
\]

where

\[
\boxed{w_b(K)=2\operatorname{popcount}(K)
              +4(1-\operatorname{bit}_{b-1}(K)).}
\]

The first three expressions are exact lengths of the inherited words, not
cost surrogates introduced by this controller. Extra observation words add
their actual lengths. At a fixed observation endpoint, `4(1-L)` is common to
every eligible key, so minimizing `w_b` minimizes the complete round cost.
When comparing different observation programs their actual `L` and observation
costs remain part of the comparison.

The coefficient of bit `b-1` in the low residue is `2-4=-2`; every other bit
has coefficient `+2`. For example, with `b=4`, keys 1 and 9 have weights 6 and
4. Choosing the numerically first certified key therefore need not minimize
the original command count.

`check_original_word_weights()` compares this formula with 234 complete
compiler-produced round words, for both Boolean endpoints and every legal
key of the declared compilers. This component check inspects constructed
word lengths; physical execution is separately recorded.

## 2. Certified mask regions

A bit-mask region is

\[
P_{s,v}=\{x\in\{0,\ldots,B-1\}:x\mathbin{\&}s=v\},
\qquad 0\le s<B,\quad v\mathbin{\&}\neg s=0.
\]

The interface `acquire_mask(s,v)` consumes a proof that every nonempty saved
request has residue outside this set. It initializes all regional slot marks
to empty. Subsequent bind/copy/drop effects maintain exactly the same
per-slot marks and multiplicities proved in the parent region construction.
An occupied point is removed at reference count `0->1`, and is restored at
`1->0`.

Low-prefix regions are the case `s=2^ell-1`, `v=p`. A high half is `s=v=B/2`.
In particular, one observed highest-low-bit value `0` in every old request
certifies the high half. If all such observed values are `1`, the low half
is certified. The observer that supplies this certificate is responsible for
its actual reads; the weighted selector performs none.

Empty complete code 0 contributes no regional reference. Nonempty code `B`
has residue 0 and contributes when 0 belongs to the region. The target key
interval remains positive, so an absence certificate for residue 0 never
causes creation of the empty code 0.

## 3. Ordered free-bit coordinates

Write the free bit positions as

\[
f_0<f_1<\cdots<f_{d-1},
\qquad d=b-\operatorname{popcount}(s).
\]

Define

\[
\Phi(j)=v+\sum_{i=0}^{d-1}\operatorname{bit}_i(j)2^{f_i},
\qquad0\le j<2^d.
\]

**Lemma 1.** `Phi` is a strictly increasing bijection from this index interval
to the mask region.

*Proof.* The inverse reads the free positions. For `j<j'`, their highest
differing binary digit is 0 in `j` and 1 in `j'`. Its corresponding residue
position dominates the sum of every lower residue position, so
`Phi(j)<Phi(j')`. This proves both ordering and bijectivity. ∎

Consequently, the intersection of the mask region with an ordinary residue
interval `[a,z]` corresponds to the ordinary index interval

\[
[\rho(a-1),\rho(z)-1],
\qquad
\rho(y)=|\{x\in P_{s,v}:x\le y\}|.
\]

The code computes `rho` in at most `b` bit decisions. Reading `y` from its
most significant bit down, each permitted smaller branch contributes all
assignments of its remaining free bits. If the equal branch disagrees with
a fixed bit, it stops; otherwise the final equal assignment contributes one.
This is an exact count, with no enumeration of the region's points.

## 4. Sparse weighted range minima

If original bit `b-1` is free, it is the highest free index bit. The variable
part of the cost is

\[
g(j)=2\operatorname{popcount}(j)-4\operatorname{bit}_{d-1}(j).
\]

If bit `b-1` is fixed, the variable cost is simply
`g(j)=2 popcount(j)`; its fixed contribution is included with `v`.

`WeightedFreeIndexTree` is a sparse binary interval tree on `0,...,2^d-1`.
It stores the exact free count and best pair `(g(j),j)` for each allocated
node. A missing node denotes an entirely free interval. In a free aligned
interval, the fixed high digits determine a prefix cost. Set every free
positive-cost digit to 0, and the one negative digit to 1 if it is still free.
This yields the best pair directly. An all-blocked node stores count zero and
no best pair.

Point updates follow one path. Internal best pairs are obtained by taking the
minimum of the two children. Prefix costs are carried down the recursion,
so merging nodes does not repeatedly recompute a population count. Completely
free and completely blocked subtrees are coalesced.

**Lemma 2.** A point update visits at most `d+1` nodes. A range minimum visits
at most `4d+1` nodes, and returns an available index minimizing `(g(j),j)`.

*Proof.* An update takes one child at each level; the stored aggregate is
correct by induction. For a query, each fully contained node returns its
already exact minimum. At a fixed depth, only the nodes meeting the two range
boundaries can be partially intersected. Each such node generates at most two
next-level visits. With the root counted once, `1+4d` bounds all visited nodes.
The minimum over covered subranges is exactly the required interval minimum. ∎

There are at most `2^(d+1)-1` nodes, each using bounded indices, counts, costs
and pointers. Nodes are allocated only along modified paths. Initialization
of a newly certified mask class takes `O(b)` to record its free positions;
its entirely free tree has one implicit root and no point enumeration.

## 5. Complete-key carries are included

Write a key as `K=QB+x`, `0<=x<B`. Then

\[
w_b(K)=2\operatorname{popcount}(Q)
       +2\operatorname{popcount}(x)
       +4(1-\operatorname{bit}_{b-1}(x)).
\]

An interval of `M<=B` legal keys occupies at most two consecutive `Q` blocks.
`TargetWindow` stores each block's residue interval and
`2 popcount(Q)`. For each block, the rank map gives its mask-index interval;
one sparse query yields the best free index. Comparing the at most two
complete-key scores gives the overall optimum, with the smaller full key
as a deterministic equal-cost tie-break.

This treatment matters near a complete-key carry. For `b=3`, `M=8`, target
7 has legal keys `57,...,64`. In an empty even region, key 60 has residue 4,
the cheapest low-residue score; its full weight is 8. Key 64 has residue 0
and full weight 6, so the complete-key optimum is 64.

**Theorem 3.** Given the maintained free/occupied bitmap of a certified mask
region and a compiled target window, `select_key` returns a legal free full
key of minimum actual key-dependent round cost, or `None` exactly when there
is no such point. It uses `O(b)` word-level control work and performs no old
request observation.

*Proof.* Lemma 1 maps each legal block to exactly one index interval. Lemma 2
finds its exact variable minimum. The fixed-mask and high-block contributions
are constant inside that interval. Taking the minimum across all blocks is
therefore exactly the global legal minimum. ∎

`TargetWindow.make` is target preprocessing. It computes at most two
population counts of high complete-key quotients. For a complete-key width
`n`, a bitwise implementation charges `O(n)` work once per target window;
the compiler can retain the resulting metadata. The convenience selector
that builds a fresh window on each call includes this preprocessing again.
The quoted `O(b)` query bound uses the already compiled window.

Slot updates also cost `O(b)`: reference-count changes are indexed, the
free-bit pack uses at most `b` positions, and at most two point updates occur.
The per-slot/reference state and worst-case tree storage are
`O(r log(r+1))` bits when `B=O(r)`, as in the inherited `M=r+1` model.
Regional replacement clears touched marks and old allocated nodes; its work
is charged to their preceding updates, as in the parent construction.

## 6. Using all currently proved empty low prefixes

The optional `choose_observed_prefix` reference chooser traverses the
maintained low-prefix observation tree. A node with zero subtree count reached
through drained ancestors supplies one empty class. A node with a live label
in its own unclassified bucket blocks every descendant of that class, so the
chooser stops there. If its own bucket is drained, it visits its two children.

The visited zero-count nodes are disjoint maximal classes whose union is
exactly the residues excluded by all currently possible label completions.
Weighted selection in each class and a final minimum therefore produce the
cheapest point that this prefix information proves absent. This reference
route can visit `O(B)` nodes and use `O(Bb)` control work; the maintained
single-region route above has the smaller query bound.

The inherited observation tree conservatively retains a full code-0 label
at residue zero; this reference chooser retains that convention. The live
mask region has its separate exact nonempty-reference invariant.

## 7. Optimality for a repeated fixed target without new observations

Fix a target and a set `F` of at least two certified legal keys. The other
request slots stay outside `F`. Each round creates a key, writes that key into
one fixed slot, and releases the source. The new key must differ from the key
currently saved in that slot. The slot initially contains a key outside `F`.
Let `w1<=w2` be the two least weights of distinct keys in `F`.

**Theorem 4.** Over every `T>=0`-round sequence that uses only `F`, the minimum
sum of key-dependent original-command costs is

\[
\boxed{\lceil T/2\rceil w_1+\lfloor T/2\rfloor w_2.}
\]

It is attained by alternating two minimum-weight distinct keys, beginning
with the cheapest.

*Proof.* In each disjoint adjacent pair, the two keys differ, so its cost is
at least `w1+w2`. If `T` is odd, the remaining round costs at least `w1`.
Alternation attains every one of these bounds. ∎

The same greedy choice remains optimal when an initial previous key belongs
to `F`: if it is the chosen cheapest key, start with a cheapest distinct key;
otherwise start with the cheapest key. For the first case, appearances of
the cheapest key are at most `floor(T/2)`, because the first position is
unavailable to it and equal adjacent keys are forbidden. Every other position
costs at least the second minimum. Equal-weight ties preserve the same cost.

Thus no future-horizon estimate is needed for optimal key choice under this
fixed-target, fixed-evidence, single-overwritten-slot objective. Information
acquisition remains a separate decision that may enlarge `F` or change its
available pair.

Examples for `b>=3`, `H=B/2`, target 0 with keys `1,...,B-1`:

| Certified class | Two cheapest keys | Their weights |
|---|---|---|
| `x=1 mod4` | `H+1, 1` | `4,6` |
| `x=0 mod4`, `b>=4` | `H,H+4` | `2,4` |
| High half `H<=x<B` | `H,H+1` | `2,4` |

For `b=3`, the low `0 mod4` class contains only one legal target-0 key, 4;
the high half still contains both 4 and 5.

## 8. Changed future targets create a planning question

Let `b=2`, `M=3`, and let the certified region be `{2,3}`. The two target
intervals are `1..3` followed by `4..6`, with one overwritten request slot.
The cheapest first key is 2. It occupies the only second-target residue
available inside this region, so the regional selector then reports a miss.
Choosing key 3 first and key 6 second keeps both actions within the same
evidence, at key-dependent total cost 8.

The exact finite dynamic program in the checker records this witness.
It distinguishes the fixed-target theorem from a future sequence whose legal
sets change. The companion original-kernel experiment can charge the actual
fallback observation when the myopic selector misses.

## 9. Recorded finite evidence

The complete small-mask domain covers every fixed/free-bit mask and every
occupied subset for widths 1 through 3, with all positive key starts `1..4B`
and lengths `1..B`. It checks 464 occupancy profiles and 109,184 interval
queries, together with exact rank and restoration invariants.

Larger-mask samples cover widths 4 through 9 and full-key quotient carries.
Two-slot update checks exhaust all masks and complete codes `0..2B` for
widths 1 and 2, including copies, self-copies, overwrites, drops and nonempty
residue-zero keys. Empty-prefix and observed-prefix adapters have their own
declared domains in the JSON result. Fixed-target schedules are compared
with exact finite DP over all declared small key sets and horizons.

These counts are component/control evidence. The general statements above
are supported by their arguments; actual BRC execution results retain their
own recorded preparations, words, endpoints and cost units.
