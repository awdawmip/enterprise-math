# R5: exact fifth-noise-chamber adaptive minimax with five unmarked errors

**Claim.** Fix the derived 954-event R5 scalar observer at scientific pin `435e77af0d180eac32bd1f9c4c464bc4010b7551`. There are 256 named closure masks, 101 integer physical query budgets `k=214,...,314`, and integer readout centers `N_h(k)`. Honest real readouts obey `|y-N_h(k)| <= eta`; at most `f=5` readouts may be arbitrary, unmarked corruptions. Query policies may adapt to previous readouts; cost is the worst-case sum of all queried k. Let

- `L=25845652773852463277015040000`
- `U=58182461585441404127941754880`
- `tau=2 eta`.

For **every real** `L <= tau < U`, the exact minimax cost is

`C*_5(tau)=5485`.

In conjunction with the earlier author-verified f=0..4 results, the formula `C*_f=735+950 f` is now established for integer `f=0,...,5` in this noise chamber.

## Exact matching lower and upper certificates

**Lower, all 101 original actions:** restrict the true state to the five genuine named closure masks `H=(18,24,82,34,17)` and set `tau=L`. The Python exact-integer Bellman solver with six error tiers reports `value=5485`, `memo_states=9281`, and lists the seven cheapest inequivalent action families representing the full 101 budgets. Restriction of hypotheses and decrease of noise may only make the identification problem easier; hence the full 256-state minimax is at least 5485 for every `tau>=L`. The 101-budget lower must not be replaced by a lower calculation constrained to the five upper-bound actions.

**Upper, all 256 original states:** retain 256 states and allow only the five physical budgets `(216,223,296,214,215)`. At `tau=U-1`, generate every inclusion-maximal normal-response support from the **exact** frozen integer count table. The resulting compact four-word answer-mask file SHA-256 is `091d7f80f6cb7b0983fb2a3659c4e9a334d53d99746b5523c24cdc9a138b0925`. The independent C++ bounded-budget recursive search (not the earlier numerical-value solver) reports:

```
F5_FEASIBLE=YES BUDGET=5485 STATES=2444218 DECISIONS=2585992
```

A separate run with the action ordering `(296,223,216,215,214)` also gives:

```
F5_FEASIBLE=YES BUDGET=5485 STATES=1615546 DECISIONS=2500534
```

The cache uses full-state equality, six tiers of four `uint64_t` words, and monotone budget certificates. All comparisons and readout calculations use integers.

**Correctness of the bounded recursion:** `S_j` holds hypotheses consistent with the transcript having exactly `j` corruptions for `0<=j<=5`. For a query k with maximal normal support A, update

`S'_0=S_0 intersection A`; `S'_j=(S_j intersection A) union (S_(j-1) setminus A)` for `1<=j<=5`.

Success is `|union S_j|<=1`. Otherwise `WIN(S,b)` is the disjunction over available k of the conjunction of `WIN(S'(k,A),b-k)` over every maximal response support A. The solver explicitly rejects a zero-progress response `S'=S` and fails once `b<214`; therefore a returned YES induces a finite winning decision tree of total cost at most b. A smaller normal-response support (including an arbitrary out-of-range readout with empty support) is dominated by a maximal one because it requires at least as many corruptions of each surviving hypothesis. Exhaustion of maximal supports therefore covers every real or corrupt readout.

All centers are integers. Every support possible for a real `tau<U` is included in a support possible at `U-1`; hence the computed winning policy remains valid throughout the entire half-open chamber. The matching bounds establish `5485`.

## Reproduction and scope

Frozen full count table SHA-256: `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. The previously published generator is [BUILD_R5_F4_ACTIONS.py](../r5_fifth_chamber_f4_full256_exact_20261117/BUILD_R5_F4_ACTIONS.py); it reads the frozen table and generates `f4_actions.txt`. Use the C++ source in this directory with:

```sh
python BUILD_R5_F4_ACTIONS.py EXACT_R5_ALL_101_BUDGETS.json f4_actions.txt
g++ -O3 -std=c++17 VERIFY_R5_F5_BOUNDED.cpp -o verify_f5
./verify_f5 f4_actions.txt 5485
```

The all-101-budget Python lower recurrence and the source count table are preserved as prior R5 material; the complete stand-alone reproducer, exact count table, action masks and executed logs are also available in this turn's handoff ZIP. An independent reviewer has not yet examined the proof. Status `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`.

This statement concerns the declared **derived integer scalar observer**, not a new native six-dimensional P000/BRC physical law. Branch publication provides scientific preservation and does not confer Task CLAIM, Result/Review acceptance, or Activity checkpoint authority.

## Next open unit

At `f=6`, the five-state lower certificate with **all 101 budgets** has already returned `6435` (18,019 memoized states). A complete full-256-state upper certificate at cost `6435` remains open; a bounded exploratory run was interrupted before proving either outcome. The previously constructed general upper `735+951f` gives `C*_6<=6441`. A smaller action-policy certificate or an all-f analytic induction is the priority next step.
