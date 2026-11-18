# Fifth R5 chamber: f=8 exact lower certificate and all-f saturated bitplane theorem

**Frozen scientific source**: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. This note extends Draft PR #2427's complete 256-state, 101-query, fifth noise-chamber R5 scalar experiment and does not change native X6/P000 state or source firewall. Observer table SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`.

## New exact lower certificate for eight unmarked errors

Let `C*_f(tau)` be the least worst-case cumulative physical budget of a finite adaptive tree identifying a named original closure mask, given up to `f` arbitrary unmarked wrong scalar answers; a normal real readout is within error `eta=tau/2` of the integer `N_h(k)`. The 101 legal budget values are `k=214..314` and there are 256 named masks.

In the fifth noise chamber

`25845652773852463277015040000 <= tau < 58182461585441404127941754880`,

`C*_8(tau) >= 8335`.

**Proof.** Restrict to the genuine five-mask subset `(18,24,82,34,17)`. At the left endpoint of the real-noise chamber, compute all maximal compatible response supports at each of all 101 budgets, retaining the cheapest query among identical support families. Bellman recursion over nine disjoint tiers, where tier j is the subset of five hypotheses with exactly j past mismatches, returns root minimax cost exactly 8335. This is a finite exhaustive minimax on the smaller true-population game, not a heuristic; 54,719 memoized states and seven unique cheapest response-support families were examined. The original 256-hypothesis game is at least as difficult as this restricted game, and increasing tau can only enlarge possible normal-response sets. Therefore the bound is valid throughout the chamber.

The already saved all-f descending-query construction yields `C*_8(tau) <= 735+951*8 = 8343`. Thus `8335 <= C*_8(tau) <= 8343`; exact eight-error optimality is still open.

The local exact lower command `python VERIFY_R5_FIVE_STATE_LOWER.py 8`, with the frozen 101-budget table and the previously saved `VERIFY_R5_FIFTH_F2_ALL256.py` response-support generator, returned:

```json
{"f":8,"cost":8335,"state_count":54719,"actions":[216,223,296,214,215,221,222]}
```

## Universal bitplane theorem (exact finite-hypothesis observer automata)

For any finite named hypothesis population of size n, any nonnegative integer f, any query/answer compatibility language depending only on the named hypothesis and query, let the transcript discrepancy for h be `ell_h=min(f+1,number of answers incompatible with h)`. Sentinel `f+1` means eliminated.

Set `w=ceil(log2(f+2))`. The entire vector of `ell_h` has an exact encoding into **w Boolean bitplanes of n bits each**. For every answer compatibility support A, define the alive mask E = {h : ell_h != f+1}, and update only outside A by `ell'_h=min(f+1,ell_h + 1_{h not in A})`. This update admits a bitwise ripple-carry implementation: `carry_0=(~A)&E`, `P'_j=P_j XOR carry_j`, and `carry_{j+1}=P_j & carry_j` using *old* P_j, with eliminated lanes held fixed. Since only live counts <= f are incremented, `ell'_h <= f+1 < 2^w`; no carry leaves the top bitplane.

**Proof.** Binary positional expansion of each bounded integer `ell_h` is injective into w bits. At each h, ripple carry computes ordinary addition by either zero or one, except on eliminated lanes where the increment is forced to zero; hence the invariant holds by induction on the number of queries. Feasibility and terminal uniqueness depend only on whether at least two `ell_h <= f`; thus the compressed representation is bisimilar to the original `f+1` disjoint tiers for every future sequence of compatible readouts in this declared scalar language. This is *not* a claim to compress the full native X6 relational/provenance state.

For f=8, w=4 still suffices: the eliminated sentinel is binary `1001`, recognized as `P_3 & P_0 & ~P_2 & ~P_1`. For f=7, the sentinel is `1000`; hence the earlier specialized f7 checker used `P_3` as elimination bit. That shortcut is not correct at f>=8 unless a proper equality-to-sentinel mask is used.

**Verification scope:** The executable Python reference `VERIFY_GENERAL_BITPLANE.py` ran 500 randomized exact transitions for every f from 0 to 20, 256 hypotheses each, total 10,500 state transitions (2,688,000 individual hypothesis updates); seed `20261117`. It checked exact equality of every bitplane and all eliminated lanes against explicit integer counters. Output: `PASS_GENERAL_SATURATED_BITPLANES_F0_F20`. This finite regression supports the universal algebraic proof but does not itself prove it.

## Authority and unresolved work

Project status: `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`. This is independently preserved portable research in Draft PR #2427; no R5 formal CLAIM, native Result/Review, P000/worldview promotion or protected Activity checkpoint is asserted. Next: compute the 256-hypothesis upper strategy at f=8 using the equality-to-sentinel four-plane update; determine whether the lower value 8335 is attainable, or raise the lower bound.
