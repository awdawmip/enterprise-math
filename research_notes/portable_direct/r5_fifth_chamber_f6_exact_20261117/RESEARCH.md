# R5 fifth noise chamber — exact adaptive minimax for six unmarked errors

**Theorem (f=6).** In the frozen derived 954-event R5 integer scalar observer with 256 named closure-mask states, physical integer query budgets k = 214,...,314 and an adaptive policy whose observations are honest within absolute error η except for at most six arbitrary unmarked corruptions, the minimum worst-case total cost is

```
C*_6(eta) = 6435
```

for every real `L <= 2*eta < U`, where
`L = 25845652773852463277015040000` and
`U = 58182461585441404127941754880`.

The frozen scientific input is `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Exact count-table SHA256 is `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`.

## Lower bound: five true states, all 101 physical budgets

Restrict nature's true state to five genuine configurations
`H=(18,24,82,34,17)` but allow the algorithm **all 101 original budgets**. At the smallest admissible noise threshold `tau=L`, an exact-integer six-corruption Bellman minimax computes cost `6435`, inspecting `18019` memoized states. Actual command:

```sh
python VERIFY_R5_FIFTH_F4_LOWER.py 6
```

Actual output:

```json
{"f": 6, "cost": 6435, "state_count": 18019,
 "actions": [216, 223, 296, 214, 215, 221, 222]}
```

The seven action labels are equivalence-class representatives of all 101 budgets for this five-state lower instance; no query-budget restriction weakens the lower bound. A state restriction and smaller noise make the task no harder than the full instance. Thus `C*_6(tau)>=6435` for `tau>=L`.

## Upper bound: all 256 states, five physical budgets

At the highest integer-supported noise level `tau=U-1`, compute the inclusion-maximal normal-response hypothesis supports from the exact integer centers for budgets `216,223,296,214,215`. The ordered action file `actions_296.txt` is the same five physical actions in search order `296,223,216,215,214`, with SHA256 `e7af68961ab468ef8af90d6976a35435c71b8f27bacb0a67fd1d96dde0c182ac`.

The C++ exact bounded-cost feasibility recursion, with seven four-word tiers `S_0,...,S_6` and max cost 6435, returned:

```
F6_FEASIBLE=YES BUDGET=6435 STATES=5539141 DECISIONS=9043443
```

The *actually executed* C++ file has SHA256 `0266b2e43fafbe0170ebc86f999f8b442309056f89ede6f86c8b35f2349c9bc2`; the published source differs only by fixing its first-line comment from "five" to "six" (SHA256 `abc448c80ff21ff147d97d3a33e45095ddc41b92f2f8489d547da823c77211bb`). The C++ computational logic is unchanged. The separate repeat attempt was interrupted after seven million decisions and is not counted as verification.

For each candidate state and transcript, the tier `S_j` contains all true hypotheses consistent with exactly j corrupted observations. Under a query and compatible-normal-state mask A:
- `S'_0 = S_0 ∩ A`
- `S'_j = (S_j ∩ A) ∪ (S_(j-1) \ A)`, for j=1,...,6.

A success state has at most one possible true hypothesis across all tiers. The bounded recurrence is
`WIN(S,b)=OR_k AND_A WIN(S'(k,A),b-k)`, and fails when remaining b is below the cheapest physical query. It rejects zero-progress branches to ensure finite termination, tests all maximal answer supports, and caches exact 28-word states with monotone budget certificates. A YES proves a terminating adaptive strategy of worst cumulative cost at most 6435.

All centers are integers. At any real `tau<U`, each feasible honest-response support is contained in one allowed at `U-1`. Therefore the same constructed policy is valid uniformly on the entire half-open noise chamber, proving the matching upper bound.

Combining lower and upper gives `C*_6(tau)=6435`.

## Implication and verification scope

Together with the preceding f=0 through f=5 proofs, this extends the *derived-observer* exact identity to `C*_f=735+950 f` for every integer `0<=f<=6`. Compared to optimal fixed observations at f=6 (`735*(2*6+1)=9555`), adaptive queries save `3120` query-budget units.

The local lower Python checker and full256 upper C++ program were actually executed with exact integer masks; the published GitHub version is checked by immutable content readback rather than independent remote execution. The C++ output is a verified local decision procedure, not a separately materialized full policy tree. No independent mathematical reviewer has endorsed this claim. Status: `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`.

These conclusions concern the declared derived 256-state integer readout, not original native X6 geometry. P000 and the ACTIVE residual-worldview axioms remain unchanged.

## Reproduce

Use the frozen exact count table with SHA256 above. The program `BUILD_R5_F4_ACTIONS.py` in sibling directory `../r5_fifth_chamber_f4_full256_exact_20261117/` generates the five physical support families. Reorder the five action blocks as `296,223,216,215,214` for the proven fast search order, then run:

```sh
g++ -O3 -std=c++17 VERIFY_R5_F6_BOUNDED.cpp -o verify_f6
./verify_f6 actions_296.txt 6435
```

The `actions_296.txt`, original executed solver, frozen complete count table, lower checker and output logs are retained together in the standalone local reproduction package. The project research folder preserves theorem, exact result and source. No formal Task CLAIM / Result / Review is claimed; Activity Source semantic association remains pending.

## Next question

Find a matching all-256 upper certificate at `f=7`, or prove/disprove an analytic all-`f` extension under the same observer and noise model. Preserve the exact Source pins and model scope.
