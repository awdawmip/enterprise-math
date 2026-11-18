# R5: sharp adaptive unmarked-error costs for all f in four noise chambers

**Date:** 2026-11-17; **frozen science pin:** `435e77af0d180eac32bd1f9c4c464bc4010b7551`. **Claim:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Model and exact theorem

The frozen scalar integer observer has 256 masks `h=0,...,255` and 101 query budgets `k=214,...,314`, with integer centers `N_h(k)` and query cost `k`. Intact observations may be any real `y` satisfying `|y-N_h(k)|<=eta`. Up to `f` observations can be replaced arbitrarily without a mark; `f` is **any nonnegative integer**. The next budget can depend on prior observations. A strategy must identify the mask for every allowed observation/fault transcript. Set `tau=2eta`, and let `C_f(tau)` be minimum worst-case cumulative budget.

| Chamber | tau in [L,U) | Budgets ascending a,b,c | Exact C_f(tau) |
|---|---|---|---|
| 1 | [0, 76289178155959966960189440) | (214,223,294) | `731+945f` |
| 2 | [76289178155959966960189440, 3133722521542003559403356160) | (214,223,295) | `732+946f` |
| 3 | [3133722521542003559403356160, 13883516118328421520506880000) | (214,223,296) | `733+947f` |
| 4 | [13883516118328421520506880000, 25845652773852463277015040000) | (215,223,296) | **`734+949f`** |

The new lower-bound argument replaces the earlier `f=0..20` finite Bellman verification by an **all-f symbolic adversary**, and the new fourth-chamber witness yields a further exact interval.

## Upper bound (all nonnegative f)

For each triple `a<b<c`, exact comparison of all 32,640 unordered pairs proves that the joint three-center signature is injective and has max-coordinate gap at least the listed right endpoint U.

More strongly, for the order `c,b,a`, the **conditional center gap** is at least U at every stage among states sharing the centers established at earlier stages. This distinction matters in chamber 4: the *global* distinct-center minimum at budget 215 is `23132306865806134864773120000`, below U, but the **conditional** minimum after decoding budgets 296 and 223 is `25845652773852463277015040000 = U`. The complete conditional-gap comparison across 256 states is included in the exact verifier.

At each budget k, within the current known fiber, the intact reading determines exactly one center symbol because `2eta<U`. With r errors remaining, repeat k until one reported center symbol occurs r+1 times; that symbol is true. If t other reports preceded it, they account for at least t actual errors, so the remaining allowance drops to `r-t`. This costs `(r+1+t)k`, with `0<=t<=r`.

For the ordered suffix `a`, the maximum is `(2r+1)a`. For suffix `b,a`, the inequality `b<=2a` gives `(r+1)b+(2r+1)a`. For `c,b,a`, using `c<=b+2a`, the worst-case recurrence is exactly `F(r)=S+r(S+a)` where `S=a+b+c`. Decoding all three true symbols identifies the unique one of 256 masks. This proves each displayed upper bound for arbitrary f.

## Lower bound: delayed-fork star adversary (all nonnegative f)

At a chamber's *inclusive* lower endpoint L, choose four actual masks `(h0,h1,h2,h3)`. Define `W_j={k : |N_hj(k)-N_h0(k)|>L}`, for j=1,2,3. The exact verifier establishes:

1. The three nonempty W_j are pairwise disjoint, with respective lowest costs a,b,c.
2. At each of all 101 k, the center-value diameter of `{h0,h1,h2,h3}\{h_j}` if `k in W_j`, or of all four if `k` is in no W_j, is at most L.

Hence at every `tau>=L`, the corresponding intact real-observation intervals have a **common zero response** for the non-target group. A targeted leaf also has a valid **one response**. An adversary can restrict the experiment to a star-oracle alphabet: `0` is allowed intact for every non-target hypothesis; `1` is allowed intact for the target leaf; any incompatible answer consumes at most one unmarked-error allowance for that hypothesis. Queries outside the three supports can be made entirely uninformative. This is a legitimate *subexperiment* of the full real-valued observation problem, not a claim that the four masks equal the full state.

For an arbitrary adaptive decoder, answer 0 until only **one leaf j** remains compatible with <=f errors. Each of the two eliminated leaves required at least f+1 support queries, because only its own W_i can make a 0 answer inconsistent with it. The remaining leaf has experienced `n<=f` zero outcomes in W_j.

From then on, answer 1 to the next **f** W_j queries, followed by 0 to the next **f-n+1** W_j queries; on other query types continue answering 0. Until the final answer, the center has at most f mismatches (from the f ones), while leaf j has at most f mismatches (from its prior n zeros plus the subsequent zeros). Therefore **neither can yet be eliminated** and a guaranteed decoder cannot stop. This requires at least 2f+1 W_j queries total. Counting the two eliminated supports yields a transcript costing at least

`(f+1)(S-k_j)+(2f+1)k_j = S+f(S+k_j) >= S+f(S+a)`.

This matches the upper bound with no restriction on f and no induction from finite experiments.

## Exact four-mask witnesses and execution

- Chambers 1,2,3: `(16,17,80,32)`.
- Chamber 4: **`(18,24,82,34)`**; strong-support windows are `215..221` (7), `223..290` (68), `296..312` (17). The maximum within-nontarget center diameter over the entire 101-budget domain equals the chamber's left endpoint `13883516118328421520506880000`.

The old chamber-1–3 four-mask witness has minimum early support budget 214 at the fourth boundary, and thus lacks the stronger fourth-chamber lower bound. The new witness closes this gap.

The accompanying Python certificate verifies frozen complete-table SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`, 25,856 integer counts' dimensions, all 101 window/group checks per chamber, the 32,640 pair signature comparisons per chamber, and conditional-gap margins for the staged decoder, entirely using exact integer arithmetic. The locally executed original checker printed `PASS_R5_FIRST_FOUR_CHAMBERS_UNIVERSAL_F_STAR_CERT`.

## Evidence, scope and continuation

This is an **exact derived scalar-observer** result under the declared noise and corruption model, not a full-state BRC/X6 equivalence or claim that a scalar quotient preserves native path, source and signed-port histories. The four-state witness is a restricted adversarial observer proving an actual 256-state lower bound without collapsing the underlying research state.

**Unresolved:** In chamber 5, `tau in [25845652773852463277015040000,58182461585441404127941754880)`, the previous one-center/three-leaf witness search yields no leaf with earliest distinguishing budget 216. A richer multi-pair adversary or a different adaptive strategy may be necessary. Also test joint erasure+unmarked corruption and observer-safe BRC provenance enhancements.

Recompute with `python VERIFY_R5_ADAPTIVE_ALL_F_STAR.py EXACT_R5_ALL_101_BUDGETS.json`. The full immutable frozen source table is already preserved in the R5 reproduction packs; this increment reuses that exact source and does not recopy it. Activity association, a formal CLAIM and independent reviewer acceptance are separate administrative/scientific events.
