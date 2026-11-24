# R5: 16-hypothesis exact f=8 five-budget strategy
Date: 2026-11-18 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Frozen scientific pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Frozen 256×101 integer center count table SHA-256: `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`.
Predecessor H15 exact certificate: commit `e08b0da17c83e2258b5bccca7e193ca801ca87f4`.

## Mathematical claim
In the radius-two indexed-center scalar observer derived from the 954-event dataset, physical query k ranges over 214,...,314 and costs k. A good reading differs by at most η from its integer hypothesis center N_h(k); up to eight observations can instead be arbitrary and unlabeled. Define τ=2η and the fifth noise chamber
L=25845652773852463277015040000 ≤ τ < U=58182461585441404127941754880.
For the sixteen *named* actual closure configurations
H16=(18,24,82,34,17,0,1,2,3,144,208,255,50,66,4,5),
the optimal guaranteed-identification worst-case total query cost is
**C₈(H16;τ)=8335 for every real τ∈[L,U).**
At least five distinct physical budgets are needed to achieve 8335, and the budgets {214,215,216,223,296} suffice. Repeated/adaptive use of these budgets is permitted.

## Proof of the exact value
The pinned H15⊂H16 certificate gives C₈(H15;L)=8335. Restricting any H16 strategy to H15 cannot raise its cost; hence C₈(H16;τ)≥8335 for all τ≥L.
For the opposite direction, at τ=U−1 the exact pinned center counts produce the maximal-support action masks in `ACTIONS_H16_PLUS_5.txt`; `GENERATE_H16_ACTIONS.py` independently reconstructs and verifies these from the frozen count table. With f=8 use the truncated mismatch counts e_h∈{0,...,9} (9 is eliminated), packed as sixteen 4-bit fields in one uint64_t. For every response-support mask S, e_h increases by one if h is still alive and h∉S. Terminal states with ≤1 alive hypothesis cost zero. For nonterminal state e, exact minimax recurrence is V(e)=min_k(k+max_S V(T_{k,S}(e))), discarding a k permitting a stationary successor (strictly positive query costs ensure it cannot minimize a finite worst case). Only maximal supports are required: smaller response supports eliminate at least as many hypotheses, so are never worse for the observer. Each maximal support appears among center windows of width U−1 starting at a stored center. Nonstationary transitions strictly increase at least one live mismatch count, giving finite acyclic recursion.
The source C++17 solver applied to these five actions completed and wrote:
`EXACT_RESTRICTED n=16 f=8 V=8335 states=23851087 actions=5`
on 23,851,087 memoized states. This establishes an upper bound at U−1. Because the centers are integers, the same action supports dominate every real τ<U, proving the same upper bound throughout the chamber. Combine with the H15 lower bound for equality.
The H12⊂H16 earlier exact four-budget minimax lower bound is 8343 throughout the chamber. It proves no strategy using ≤4 distinct budgets can attain 8335. Our five-budget construction shows sufficiency.

## Added scalar support structure
At budgets 214,215,216, new hypothesis h=5 contributes its own singleton maximal-support mask 32768, while old maximal supports are retained. At budgets 223 and 296, its membership produces maximal masks 53755 and 57824. These are exact observer-relative masks, not an erasure or lossless compression certificate for original X6 joint paths, signed branches, provenance or ports.

## Execution evidence and limits
The integer generator verified the SHA-256 of the full frozen count input; no floating-point overlap test was used. Exact action masks, executed C++ source and stdout are in this directory. A parent timeout watcher was detached to keep the already-running calculation alive; the child solver completed and printed its terminal line, but no separate outer exit code is available. Local archive includes the complete 1,549,048-byte source count table and SHA-256 manifest. GitHub references the same pinned source table and preserves standalone action data so the C++ proof calculation is reproducible without refetching the table. Independent reviewer admission is pending.

## Next question
Determine whether the exact f=8 value 8335 persists after adding h=6 (17th named configuration), ideally using general four-bit-plane state storage rather than n≤16 uint64 packing. For the full 256-state task, the current fifth-chamber range is 8335≤C₈*≤8343. No formal Task/CLAIM/Result/Review or native X6 full-state equivalence is asserted by this independent research note.
