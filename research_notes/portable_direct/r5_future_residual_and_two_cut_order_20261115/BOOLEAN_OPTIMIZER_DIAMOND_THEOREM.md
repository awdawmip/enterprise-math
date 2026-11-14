# R5 optimizer Boolean diamond: simultaneous gap closure creates no new optimal center families

Date: 2026-11-15. Frozen input pin `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Scope: the frozen 954-event **derived** integer-coordinate radius-two indexed-center observer, budgets `K=214..221`, cuts 8 and 9 (zero-based original gap indices), all other 26 closure backgrounds B. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

This theorem supplies a structural explanation for the direct-offline maxmin equality in the companion `JOINT_CLOSURE_EXACT_MAXMIN_THEOREM.md`.

## Main theorem

Let `O_B(K)` be the complete family of minimum-total-distance center-index sets of size K under closure set B; let `B8=B∪{8}`, `B9=B∪{9}`, `B89=B∪{8,9}`.

For **every** integer K=214,...,221 and every B excluding cuts 8 and 9, the following are **exact set equalities of labeled center-index families**:

```
O_B8(K) ∩ O_B9(K) = O_B(K)
O_B8(K) ∪ O_B9(K) = O_B89(K)
```

Thus these four optimizer families form an exact Boolean diamond over the center-index language. Closing both gaps introduces **no optimal center set that is absent from both single-gap-closed optimizer families**. This is stronger than a coincidence of optimizer counts or one selected optimal path.

### Proof by finite exact language cardinalities

The previously saved R5 complete-optimizer support theorem reduces all 28 closure variables at K214..221 to E={3,8,9,10,27}; its quotient preserves **complete labeled optimum families**, not only optimal costs. Holding 8 and 9 open leaves exactly 8 effective B over {3,10,27} for each of eight K values: **64** cases representing every assignment of the other 26 original closure variables.

Closing an additional gap only shortens (or preserves) distances between any two original event indices, so any center-index set's total nearest-center distance weakly decreases. The earlier exact constant-optimum-cost theorem yields equal `J(K)=2134-5K` for all four closure masks in this budget interval. Hence the monotone optimizer inclusions `O_B⊆O_B8,O_B9⊆O_B89` and `O_B⊆O_B9` follow; the checker additionally verifies inclusion directly on every rank-labeled optimizer-language DAG.

For each original-mask effective case, `VERIFY_R5_BOOLEAN_OPTIMIZER_DIAMOND.py` constructs the exact complete optimal path languages via the same frozen generator and integer Bellman prefix/suffix optimality DP. Because each center-index set is uniquely ordered, the number of distinct optimizer sets equals the number of complete source-to-tail center paths. The checker evaluates each path count as a Python arbitrary-precision integer (no floating-point conversion). To calculate `|O_B8 ∩ O_B9|` **exactly**, it intersects the optimizer languages' rank-labeled vertex sets and all consecutive-rank edge sets, then counts full paths of the intersected DAG: a path belongs to both languages iff every one of its labeled edges belongs to both.

For all 64 cases the verified integers satisfy simultaneously

```
|O_B8 ∩ O_B9| = |O_B|
|O_B89| = |O_B8| + |O_B9| - |O_B8 ∩ O_B9|.
```

The direct optimizer inclusions and finite cardinality equalities establish the two family **set** equalities. This covers all effective masks by complete exact enumeration, and all 28 original bits via the previously proved optimizer-family quotient theorem.

**Sample K=214, B=∅** (center-set counts, not individual centers):

```
|O_B|        =   71,400,940,037,117,596,391,178,240,000
|O_B8|       =  243,953,211,793,485,121,003,192,320,000
|O_B9|       =  991,679,722,737,744,394,321,920,000,000
|O_B89|      =1,164,231,994,494,111,918,933,934,080,000
|O_B8 ∩ O_B9| = |O_B|.
```

Verified result: `PASS_R5_BOOLEAN_OPTIMIZER_DIAMOND`, 64 complete effective-background cases. Full count JSON: **22,684 bytes**, SHA-256 `0135e3df400dfd3470b8110382ee91cf1120d99d12f20830a25b876246aad0c3`, exactly reproducible by the committed adjacent program. The proof's conditional basis is the prior exact optimizer-family support theorem, the optimizer-DAG completeness semantics and the constant-cost theorem; independent mathematical review remains outstanding.

## Consequence: exact joint maxmin without new minimax computation

For any nonempty finite set families A,C,D and any distance `d`, the directed Hausdorff functional satisfies

```
H(C∪D,A)=max(H(C,A),H(D,A))
where H(X,A)=max_{x∈X}min_{a∈A} d(x,a).
```

Apply this general identity to `A=O_B`, `C=O_B8`, `D=O_B9`, and the indexed-center replacement metric `d(S,T)=|S\T|`. The **union equality** above implies, for all declared R5 cases,

```
D_89(K,B)=max(r_8(K,B),r_9(K,B)).
```

The prior exact single-cut table then yields D=7 (K214), 6 (K215), 6 or 5 at K216 depending on cut10, and 5 at K217..221. This **structural independent derivation** agrees with all 64 previously run direct offline Pareto maxmin computations and full-new-witness old-language checks.

For comparison, inclusion of languages alone is insufficient for this identity. Take abstract K=2 center sets `A={{1,2}}`, `C=A∪{{1,3}}`, `D=A∪{{2,4}}`, `E=C∪D∪{{3,4}}`. Both individual directed distances to A equal 1, but `H(E,A)=2` because of the novel jointly available set {3,4}. The **absence of new joint-only optimizers** is precisely the meaningful structural property measured in R5. This abstract example is not asserted to arise from radius-two geometry.

## Reproduction and next objective

From this directory, run `python VERIFY_R5_BOOLEAN_OPTIMIZER_DIAMOND.py > BOOLEAN_DIAMOND_OUT.json`. It imports the adjacent, fully saved `VERIFY_R5_JOINT_CLOSURE_OFFLINE.py` generator and exact optimizer functions. The output includes **all 64 sets of five exact arbitrarily large integer cardinalities**, labeled by K and effective-background mask. The numerical observation is more informative than merely sampling optimal center paths.

Next: determine a general sufficient **geometric or matroid-like structural condition** for the two-cut Boolean optimizer diamond, and find minimal concrete derived-radius-two counterexamples where the joint closure creates genuinely new center sets. Independently review previous common-anchor factorization and optimizer-DAG completeness before considering task/Result promotion. Preserve P000 native X6 and observer transfer separation.
