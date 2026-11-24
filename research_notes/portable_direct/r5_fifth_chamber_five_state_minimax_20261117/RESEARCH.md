# R5 fifth noise chamber: five-state minimax obstruction

Date: 2026-11-17. Scientific freeze: 435e77af0d180eac32bd1f9c4c464bc4010b7551. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Model and scope

There are 256 masks, h=0,...,255; 101 admissible integer-cost budgets k=214,...,314; pinned exact integer centers N_h(k). An intact real-valued observation y has |y-N_h(k)| <= eta; at most f observations are arbitrarily corrupted without marks. Queries are adaptive, and total cost is the sum of their integer budgets. Let tau=2eta, and C_f(tau) be the minimum worst-case cost of identifying h.

This result concerns the frozen derived scalar observer; no native path/port provenance is compressed or declared reconstructible.

## New fifth-chamber bounds

Throughout L <= tau < U, where
L=25845652773852463277015040000 and
U=58182461585441404127941754880,
the following exact bounds hold for every integer f>=0:

734+949f <= C_f(tau) <= 735+951f.

For every integer 0<=f<=10, a stronger *proved lower bound* is

735+950f <= C_f(tau) <= 735+951f.

In particular C_0=735 (agreeing with the previous complete zero-fault phase diagram), and 1685 <= C_1 <= 1686. The upper bound is constructive; the finite-f lower bounds are from a fully exhaustive exact minimax computation on a specific five-state restriction. These one-unit and f-unit intervals are still open for full-256-state exact optimization.

## Universal upper bound

Choose budgets in descending order (296,223,216), sum 735. The exact 256-state conditional minima in that order are respectively
58182461585441404127941754880,
267753525139190986466918400000,
92195224223274674159616000000.
Each is >= U. At every stage, after restricting to the centers established in earlier stages, the true intact center symbol is uniquely determined when tau<U.

Repeat each query until an observed center-symbol has appeared r+1 times, where r is remaining corruption allowance; decrement r by the number of dissenting reports. For a<b<c, b<=2a and c<=b+2a, the worst-case cost of the descending three-stage policy is S+f(S+a), S=a+b+c. With a=216 this is 735+951f. Corrupted off-alphabet readings count as disagreements.

## Universal lower bound

Restrict to masks (18,24,82,34), a center and three leaves. At tau=L, the respective strong-distinguishability supports against mask 18 are pairwise disjoint and have minimum budgets (215,223,296). For each of the 101 budgets, the diameter of all nontarget center values is at most 13883516118328421520506880000 <= L. Hence an adversary can respond with a shared zero to all nontarget masks, while a target-specific response is available. The delayed-fork adversary needs f+1 queries in each of two supports and 2f+1 in the last, yielding 734+949f. Since greater tau only increases the observation ambiguity, the bound holds throughout the chamber.

## Stronger exact five-state finite lower bound

Use masks H=(18,24,82,34,17). At tau=L, for every possible real response to budget k, the compatible masks are precisely those whose closed intervals [N_h(k)-eta,N_h(k)+eta] contain that response. Their maximal compatible sets are obtainable by sliding an inclusive center-value window of width tau through the five exact integer centers. An answer with a proper subset is dominated for the adversary by its containing maximal answer. The 101 queries have seven distinct maximal-response families; retain their cheapest representatives.

For fixed f, a Bellman state is a vector e in {0,...,f+1}^5 recording the minimum number of corruptions needed for each hypothesis. A response with compatible-mask set A updates e_h to min(f+1,e_h+1[h not in A]). The terminal value is zero when at most one state has e_h<=f. Other states satisfy V(e)=min_k(k+max_A V(update(e,k,A))). A query admitting a response with no state change cannot improve the worst-case value and is excluded. This is a finite exhaustive recursion using exact integers and all permissible response classes.

The verifier returns five-state minimax values (735,1685,2635,3585,4535,5485,6435,7385,8335,9285,10235) for f=0,...,10, precisely 735+950f on this finite range. Restriction to H proves the same values as lower bounds for all 256 states. State-space coverage per f and exact response-family construction are recorded in RESULTS_R5_FIFTH_CHAMBER.json.

## Structural finding and continuation

Over all 32640 unordered pairs at tau=L, the earliest budget with |N_h(k)-N_j(k)|>L has exact histogram:
214:31104; 215:640; 223:512; 294:64; 295:256; 296:64.
In particular, no pair has earliest strong budget 216. A four-state disjoint-star certificate with early *minimum* 216 is therefore impossible using this particular earliest-difference template, although the constructed five-state coupled restriction restores one extra budget unit per corruption in the finite lower bound.

Next: seek an all-f symbolic version of the five-state 735+950f lower bound, and solve whether 735+951f or a lower adaptive cost is attained for full 256 states at f=1; then extend to mixed erasures. The full observer input remains pinned. The earlier four-chamber proofs and Activity remain unchanged; this branch preservation is not a formal Task CLAIM, Result, or independent review.

## Reproduce

Run: python VERIFY_R5_FIFTH_CHAMBER.py EXACT_R5_ALL_101_BUDGETS.json

Input SHA-256: 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b
Expected output: PASS_R5_FIFTH_CHAMBER_FIVE_STATE_MINIMAX_F0_TO_F10.
Input was previously preserved in the R5 complete reproduction packs; source is reused byte-for-byte.