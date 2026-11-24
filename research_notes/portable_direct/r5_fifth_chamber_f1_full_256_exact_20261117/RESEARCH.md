# R5: fifth noise chamber, one unmarked error — full 256-state exact optimum

**Frozen scientific input:** `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
**Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
**Observer scope:** derived scalar integer counts only; no assertion of native path/port information recovery.

## Theorem

For 256 masks, budgets k in {214,...,314} with positive query cost k, normal real observations |y-N_h(k)| <= eta, and at most one unmarked arbitrarily corrupted reading, write tau=2eta. Throughout the entire fifth chamber

```
L = 25845652773852463277015040000 <= tau
tau < U = 58182461585441404127941754880
```

the minimum, over all deterministic adaptive decision trees that must identify the true mask, of the worst-case total query budget is **exactly 1685**.

This closes the previously recorded 1685–1686 gap for f=1. It applies to *all* 256 masks; the earlier five-mask restriction was a lower bound only.

## Finite proof by monotonic sandwich

1. At tau=L, restrict the adversary to five masks H=(18,24,82,34,17). Exhaustive exact minimax yields C_H(L,1)=1685, giving the full-population lower bound C_256(tau,1)>=1685 for tau>=L.
2. All count centers and query costs are integers. For any real tau<U, every center pair with difference <=tau also has integer difference <=U-1. Hence every response-compatibility set at tau is contained in one at tau=U-1.
3. At tau=U-1, exact minimax over the full 256 masks gives C_256(U-1,1)=1685. The associated finite decision policy is a constructive upper certificate, and applies for all smaller tau.
4. Combining the two bounds gives equality throughout the chamber.

## Exact response and Bellman semantics

For query k and response y, candidate mask h is uncorrupted-compatible iff |y-N_h(k)|<=eta. Such sets are precisely center subsets covered by closed intervals of length tau. Maximal sets suffice for an adversary: replacing an answer by a containing maximal set can only increase the set of viable hypotheses. Every maximal set occurs among the windows [v,v+tau], v an observed center value. Queries with identical maximal-response families are interchangeable; the smallest k dominates all larger costs.

For one permitted unmarked arbitrary error, represent a belief state by two disjoint bitsets (A,B): A holds masks compatible with zero errors; B holds masks compatible with exactly one error. For a maximal answer set S,

```
A' = A & S
B' = (B & S) | (A & (~S & MASK256))
```

where MASK256=(1<<256)-1. Terminal cost is zero when |A union B|<=1. Otherwise, the minimum exact worst-case remaining budget obeys

```
V(A,B) = min_k { k + max_S V(A',B') }.
```

An action for which an answer leaves (A,B) unchanged is omitted since the adversary can repeat it indefinitely. All remaining branches have a strictly decreasing bounded uncertainty potential, so the memoized recursion is finite.

At L on H, 133 Bellman states and 7 distinct budget-family representatives were inspected; root V=1685. At U-1 on all 256 masks, 17,945 Bellman states and 12 distinct budget-family representatives were inspected; root V=1685. Both use exact Python integers. The earlier f=1 five-state result is recovered independently.

## Reproduce and evidence

Run:
```
python VERIFY_R5_FIFTH_F1_EXACT_ALL_MASKS.py EXACT_R5_ALL_101_BUDGETS.json
```

The frozen full 101-budget, 256-mask table is supplied in the previous R5 reproducibility packs. Required SHA-256: `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. The script verifies that digest and full index/domain. Expected status: `PASS_R5_FIFTH_CHAMBER_F1_FULL_256_EXACT_1685`.

The authored full-256 policy DAG was separately generated locally: 4,240 reachable nonterminal states, 17,945 evaluated Bellman states, 251,434-byte JSON policy, SHA-256 `369ea769a9314ba895f7828c46d5634dd651c428170dffe23e9ad49ab580ddf4`. The stand-alone verifier reconstructs the exact minimax and does not require trusting this policy file.

## Research continuation

Next: determine f=2 full-population optimum and, more generally, the all-f behavior (previous lower 735+950f for 0<=f<=10; upper 735+951f). Test whether the f=1 strategy's economy persists under two faults. This work does not modify P000, Source Result/Review, task owner, or CLAIM. Activity association requires its own authenticated Source route.
