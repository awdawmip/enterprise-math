# Stage510-B — Sharp uniform saturation of opaque public-source counts

Date: 2026-11-08 (Asia/Shanghai).
Status: author-side mathematical proof, strict finite-family counterexamples, exact integer implementation checks. Independent Driver review and native acceptance pending.

## Inputs, precise scope, and provenance

Frozen scientific inputs: GLOBAL_KNOWLEDGE `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; frozen P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Parent Stage509-B: `94f52374ed15a2a8cb41a7bf8b5aca163e8c1370` / `PROOF_STAGE509B.md`. Current behavioral rules were separately refreshed from the main branches on 2026-11-08. Do not alter frozen science pins.

The mathematical model is a finite sequence of tagged native X6 unit directions, not a native physical trajectory. Each token is `(identity,direction,source)` where directions are the 12 signed `±E_i` for `i=1..6`, and source is `O` or `P` (public). The complete BRC joint-relation observer is `F(w)=(n,D,E)` with signed displacement `D∈Z^6` and all 144 *ordered* adjacent-pair counts `E_(a,b)`. Endpoint directions can be recovered from `D,E`, and the exact BRC concatenation operation preserves them without discarding path-junction information.

Future grammar, at most `h` steps: `POP`, `DELETE2` (third from right), `INSERT2(c)` (insert a new P token before the last two), `SET_END(r,c)` for `r∈R`, and `DELETE_KTH_PUBLIC(k)` for `k∈S`. The sets `R⊂N_0`, `S⊂N_{>0}` are finite; operations obey length/rank legality; `c` ranges over the full twelve-direction alphabet. Operation validity and every post-prefix complete observer are retained.

The Stage509 direct-touch mask `D_h(w)` is computed from the *actual initial tagged identity skeleton*: it consists of all original identities that any legal future operation at depth strictly less than `h` can directly delete or direction-update. All those tokens are stored explicitly, as are inserted tokens. Other contiguous original gaps are indivisible and store their exact `F`. The Stage509 proved evaluator uses exact `#P` for each gap. Its insertion proof relies on `DELETE2`: any original third-from-last token serving as an insertion boundary would also be a direct `DELETE2` target at the same pre-action skeleton.

## Theorem 510.1 — Public source counts saturate sharply

Let `h≥0`. If `S` is nonempty let `K=max(S)` and `T=max(0,K−1)`. For each opaque original gap `g`, replace its exact public count `p(g)` by the **saturated count**

```
p_T(g) = min(p(g), T).
```

Keep the full `F(g)` and all direct-touch singletons exactly as in Stage509. For every initial tagged word and every future sequence of at most `h` grammar operations, this compressed representation reproduces (1) each operation's legality, (2) each selected rank-public target, and (3) all future `F` readouts. It never splits or edits an opaque gap.

When `S` is empty, no public count is needed. At `K=1`, `T=0`: **no opaque-gap public-count bits are needed after the exact original direct-touch mask is computed**. For `K≥2`, each opaque gap's extra count uses at most `ceil(log2 K)` bits (values `0,...,K−1`), independent of total history length. Other BRC relation-summary costs remain unchanged. The count operation is a saturated additive monoid `a ⊕ b = min(T,a+b)`, which is associative.

### Proof

Stage509 ensures every original token actually deleted or direction-updated in any legal future prefix is an explicit singleton. INSERT2 boundaries also remain available, through the independent DELETE2-target argument. It therefore suffices to show that replacing exact public counts by `p_T` preserves all ranked-deletion *legality and target selection* at any reachable pre-action state.

Scan the current pieces from right to left for `DELETE_KTH_PUBLIC(k)`, where `k≤K`. At entry to any piece let `r` be the still-needed rank (`1≤r≤k≤K`). A singleton source tag is exact. For an opaque gap `g` of actual count `p`, there are three possibilities.

1. The requested token is to the right: the scan never enters this gap.
2. The requested token is to the left, or does not exist: the scan passes the gap only if `p<r≤K`; therefore `p≤K−1=T` (for `K≥1)), so `p_T=p`. The scan subtracts the exact count, retaining the exact residual rank and/or correctly detecting rank illegality.
3. The requested token is in the gap: this is impossible at a reachable pre-action state. Such an original token would be directly deleted in the legal future rank operation and hence would belong to `D_h(w)`; it would have been an explicit singleton rather than in an opaque gap.

Thus the saturated scan performs the same legal rank action or the same rejection as the uncompressed tagged word. Other operations use exact length and explicit directly touched singletons; insertion creates an explicit P token. Opaque gaps are never split, so their saturation values remain unchanged during any operation. The BRC ordered-edge concatenation law supplies exact `F` at every step. Induction on prefix depth proves the theorem, including `h=0` and `K=1`. QED.

**Important ordering:** `D_h` must first be computed using the actual individual provenance tags; saturation is applied only *after* that mask is formed. Saturated counts are not an adequate substitute for exact original provenance when synthesizing `D_h`.

## Theorem 510.2 — The uniform threshold K−1 is sharp for K≥2

For any `K≥2`, take `h=1`, `n=K+5`, `R={n−1}`, `S={K}` and use the identical full direction word for two histories. Let `x` have P labels at indices `{0,1,...,K−1}`; let `y` have P at `{0,1,...,K−2}`; all other labels are O. Their direct-touch masks are identical:

```
D_1(x) = D_1(y) = {0, n−3, n−1}.
```

Indeed `SET_END(n−1)` touches index 0, DELETE2 touches `n−3`, POP touches `n−1`, and the legal ranked operation in `x` also targets already-exposed index 0. The sole nonempty opaque interior gap has `K−1` P in `x` and `K−2` P in `y`. Any cap `T≤K−2` therefore identifies the two full compressed records, including directions, 144 ordered-edge counts, exposed source tags, and truncated gap count.

Yet `DELETE_KTH_PUBLIC(K)` is legal for `x` and illegal for `y`. Consequently every uniform cap smaller than `K−1` fails for this representation family. `K=1` has the minimal nonnegative cap `T=0`. This proves sharpness **uniformly across horizons and alphabets** by the included `h=1` family; it does not claim every fixed `h>1` needs the same cap.

## Typed BRC reuse and exact calculation

Applied interface: Stage509's associative full-direction BRC relation summary with 6 exact signed-integer displacement coordinates, 144 complete ordered adjacency counts, exact endpoints derivable from `F`, and current-source provenance; the saturation is a separate finite provenance-count monoid. This is a quotient certified for the specified future-operation/observer language. It is not a claim about physical heartbeat time.

A self-contained Python standard-library checker `REPRO_STAGE510B.py` and its actual `STAGE510B_EXECUTED.json` output verify:
- 1,043 initial histories, including an exhaustive 2-direction × 2-source-tag finite domain through length 4, with three specified grammar settings, plus 20 full-12-direction histories of lengths 19/28.
- 15,801 enumerated identity/tag skeleton states; 31,145 paired future-prefix nodes; 35,646 exact legality comparisons; 30,102 full-F transitions (all 144 directed coordinates).
- Six independently constructed strict lower-cap collisions for `K=2,...,7`.
- All assertions passed in Python exact-integer arithmetic. These tests corroborate the general proof but do not replace it.

The primary Stage510 question, a non-exponential exact synthesis of `D_h(w)`, remains open. This stage completes its independent saturation subproblem; high-rank/low-horizon saturation may permit further **instance-dependent** compression.

## Next scientific unit

Stage511-B: compute a **gap-specific** smallest sufficient public-count quotient using reachable rank scans while avoiding raw future-tree enumeration where possible. Derive a polynomial or fixed-parameter symbolic transformer for the exact original direct-touch mask `D_h` under mixed positional operations and adaptive public-ranked deletion, reporting full preprocessing cost. Continue the separate heterogeneous repeated-edge, 12-direction/144-relation Euler–BRC exact rank/unrank complexity and reproducible benchmarking objective.

Review and native Source Result: unconfirmed, not promoted.
