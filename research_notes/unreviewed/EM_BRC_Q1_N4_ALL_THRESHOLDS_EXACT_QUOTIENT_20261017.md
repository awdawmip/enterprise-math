# Auxiliary BRC Q=1, n=4: exact universal-threshold observation quotient (UNREVIEWED)

**Status:** `UNREVIEWED / NOT_ADMITTED`. Four *labeled mass sources*, **not** native spatial axes of P000. Fixed control reads: GLOBAL_KNOWLEDGE_V1 main `7ad1c71bc449991d4b8f2613e5cfbafdd5344534`; Enterprise Math main `fae8314f1a792633c018b12b8206c51c95a4d294`. Extends the unreviewed three-source research, without repeating it.

## Theorem (symbolic proof plus finite replayed certificates)

The action protects one label p; an adversary secretly resets exactly one other label k≠p to 0; the action then returns b=1[sum of remaining masses≥T]. A finite feedback policy stops at any history; Safe(P,x) means **every** hidden-reset path ends with nonzero mass. States are equivalent if Safe agrees for every finite adaptive policy.

For all integer T≥1 and any unbounded nonnegative integer x,y∈N₀⁴, define the **proper** operational profile

```
Π°_T(x) = ((1[x_i>0])_{i=0..3},
           (1[Σ_{i∈U}x_i ≥T])_{∅≠U⊊{0,1,2,3}}).
```

Then the following is **exact** in the declared auxiliary model:

```
x ~_T y    <=>    Π°_T(x)=Π°_T(y)

A_4(1,T) = 16 (T=1), 81 (T=2), 148 (T=3),
           210 (T=4), 241 (T=5), 263 (T>=6).
```

Every inequivalent pair has a safe-versus-unsafe feedback policy requiring **at most four reset actions**. The 4-step existence claim has an explicit finite certificate proof, not an unverified general search extrapolation.

## Proof: profile sufficiency, truncation and transfer

Every feedback occurs **after** at least one reset, so its surviving set U of original labels is always proper. Its bit is precisely Π°'s bit for U. Terminal safety is determined by the surviving labels and positivity bits. Thus equal Π° yields equal full feedback trees and universal terminal safety. Clipping coordinates with C_T(x)_i=min(x_i,T) does not change these predicates, giving a finite quotient of unbounded integer masses.

Crucially, **policy semantics depend only on the abstract Π° bits, not on the numerical T**. A feedback policy that separates two Π° signatures at T=6 separates those same signatures whenever realized at any other T.

The full-set threshold bit must *not* be included in an allegedly minimal operational profile. For any n≥2, T≥n+1, x=(1,…,1) and y=(T-n+1,1,…,1) have different full-set bits but are observationally equivalent: every post-reset feedback is 0 and every reset-mask positivity pattern agrees. For n=4,T=5 the concrete example is (1,1,1,1)~(2,1,1,1).

## Proof: all feasible signatures are already present at T=6

At T≥2 classify each coordinate as 0 / L∈[1,T−1] / H≥T. Given exactly m low labels, the other 4−m independently choose zero or high. Let f_m(T) be the realizable subset-threshold patterns on m low labels (if m=4 omit its full subset). Then

```
#Π°_T = Σ_{m=0}^4 binom(4,m) 2^(4−m) f_m(T).
```

For m=0,1 the value is 1. For m=2 a single pair bit gives at most 2. For m=3 the three pair bits and triple bit have at most 9 patterns (any winning pair forces the triple winning). For m=4, six pairs define a graph: an alternating rectangle with winning disjoint edges ab,cd and losing cross pairs ac,bd is impossible, since the winning inequalities sum to ≥2T while the losing ones sum to <2T. The exact 64-graph enumeration leaves 46 labeled graphs. For each graph every triple containing a winning pair must win; other triple bits offer a combinatorial upper bound.

| Winning pair edges | Graphs | Unforced triples | Maximum profiles |
| ---: | ---: | ---: | ---: |
| 0 | 1 | 4 | 16 |
| 1 | 6 | 2 | 24 |
| 2 | 12 | 1 | 24 |
| 3 (triangle) | 4 | 0 | 4 |
| 3 (star) | 4 | 1 | 8 |
| 4 | 12 | 0 | 12 |
| 5 | 6 | 0 | 6 |
| 6 | 1 | 0 | 1 |
| **Total** | **46** | | **95** |

Exact integer witness enumeration at T=6,7,8,9,10,11 realizes *each* of all 95 four-low patterns with coordinates in [1,T−1]. For any T≥6 write T=6k+r (k≥0, 6≤r≤11); for any particular pattern take x(T)=k·x(6)+x(r). Each winning sum stays ≥T and each losing integer sum remains ≤5k+r−1<T. The coordinate bounds also persist. Thus f₄(T)=95 for **every** T≥6. The same constructive additive argument establishes f₃(T)=9 for T≥4 (base thresholds 4…7) and f₂(T)=2 for T≥3 (bases 3…5). The small thresholds are finite integer enumerations:

| T | f0 | f1 | f2 | f3 | f4 | # profiles |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | — | — | — | — | — | 16 |
| 2 | 1 | 1 | 1 | 1 | 1 | 81 |
| 3 | 1 | 1 | 2 | 5 | 12 | 148 |
| 4 | 1 | 1 | 2 | 9 | 42 | 210 |
| 5 | 1 | 1 | 2 | 9 | 73 | 241 |
| ≥6 | 1 | 1 | 2 | 9 | 95 | 263 |

Thus **every** proper profile feasible for *any* positive integer T has a concrete representative at T=6.

## Proof: explicit separation certificates for the 263 abstract profiles

Take the lexicographically first x∈{0,…,6}⁴ for each of the 263 profiles. For all 263·262/2 = **34,453 unordered pairs**, a C++ solver generated a *specific* orientation and at most four (protected p, bad-path hidden reset k, feedback b) triples. This defines a policy: follow the specified feedback trunk; stop immediately on every alternative feedback bit. The chosen bad hidden-reset path ends with zero mass. An independent Python interpreter enumerates **all** hidden resets of the safe representative and checks that every branch stops nonzero. The interpreter validates the bad path and full pair coverage, and does not call the solver. **34,453/34,453 validated**.

Orientation reversed: 865 pairs. Policy lengths: 0→262, 1→693, 2→3,200, 3→9,832, 4→20,466. The representative table SHA256 is `4b6bef7e8ab5ea1e4f72d82d89e47731731ab424c1de9d9b48ccf2ae246260f7`; full 34,453 JSONL certificates SHA256 `bd8d0ea163654e82a4b39231cc87cc0c3861238f1d6ede478cff70baf21bf405`. Full evidence and independently runnable sources were generated locally. A separate orbit classifier exhaustively checked all T=1..8 (at T=6, **270,725 = 210 identical + 2,835 same proper profile + 267,680 distinguishable**, no cross-proper-profile blind spots).

Because every possible profile occurs at T=6, these 34,453 independently replayed policies prove minimality at **every T** by the threshold-independent transfer principle, completing the exact count and 4-step bound. This universal conclusion does **not** rely on enumerating arbitrarily large thresholds.

## Reproduction and limits

Main local evidence: `profile_count_constructive.py` (all 95 patterns and additive base witnesses); `n4_constructive_threshold_witnesses.json`; `brc_q1_n4_certificate_generator.cpp`; `profiles_T6.tsv`; `profile_separation_34453.jsonl`; `verify_independent_policies.py`; `independent_replay_audit.json`; and an independent `brc_n4_proper.cpp` orbit classifier. Sources and full ZIP are conversation evidence; GitHub persistence of this note must be verified by separate readback. No native P000 transfer, current Source CLAIM, Result or Driver approval is implied.

**Native control:** current MCP identity is read-only; task enumeration returned `CONTROL_QUOTA`, and session start returned `STATIC_READONLY_SCOPE_DENIED`. Therefore current active owner could not be verified and formal Research Activity/CLAIM/Result/Driver review were not performed. This is an independent, unreviewed mathematical workstream, not a takeover of any active task.

**Next:** n=5, smallest T supporting genuinely different **proper-subset** profiles with permanent feedback equivalence; distinguish these from false blinds caused only by the unobservable full-set bit. Also shrink the 34,453 finite proof to a symbolic family of policies and seek independent Driver review.
