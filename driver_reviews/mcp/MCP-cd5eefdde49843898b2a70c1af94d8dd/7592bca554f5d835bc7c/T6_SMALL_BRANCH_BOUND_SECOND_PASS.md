# T6 p17 order-one affine search: independent small-branch bound

Scope: Root-directed local paper preparation only. No claim, Result, Source write, remote action, identity, author-code read/execution, affine-path enumeration or prefix/full census was performed. This pass used the fixed p17 rational Gram-Schmidt entries and small static integer cross-comparisons only. All arrays and classical arithmetic retain their external auxiliary-model type; no HEARTBEAT_X6 native statement is promoted.

## Conclusion

The proposed bound of at most

`1 + 16 + binom(16,2) = 137`

feasible complete coordinate paths per affine class is valid under the certified exact Gram-Schmidt representation and the separate-side radius bound. Center dependence, deterministic tie-breaking and empty intervals do not invalidate the count.

The residue-specific static index-set filter strengthens it to at most 36 paths in any one class and at most 398 across all sixteen relaxed order-one classes. These are proved upper bounds, not observed candidate counts or arithmetic exclusions. No class has been searched in this pass; maximal p17 order one remains open.

## Exact proof

Fix coordinate order 15 down to 0. Let the exact orthogonal center at level `i` be

`c_i = h_i + sum_(j>i) n_j mu_(j,i)`.

The squared norm is the sum of nonnegative exact terms

`sum_i D_i (n_i+c_i)^2`

(or this sum plus another nonnegative orthogonal remainder, if a larger ambient space is used).

At any feasible prefix, the remaining radius is no larger than the original `R_r^2<=9,538,237`. Every certified `D_i>9,538,237`. Therefore its interval radius is strictly less than one, and every allowed integer is among

`floor(-c_i), ceil(-c_i)`.

Fix a deterministic nearest-integer rule, including the half-integer tie. Call that integer the preferred choice. Call the other *distinct* floor/ceil integer the away choice. If `-c_i` is integral there is no distinct away choice. If it is exactly halfway, the two distances are equal; one is still preferred by the declared tie-break and the other is away by definition.

For every away choice,

`|n_i+c_i|>=1/2`,

so its orthogonal contribution is at least `D_i/4`. The exact serialized entries satisfy

`3 min_i D_i > 4*9,538,237`.

Thus three away choices already exceed the full radius. Every feasible path contains at most two away indices.

For any fixed away-index set `S`, descending deterministically reconstructs at most one coordinate vector: higher coordinates fix the current center, and `S` fixes preferred versus away at the current level. Induction gives uniqueness even though centers depend on previous higher-level choices. Some sets generate no feasible vector, which only reduces the count. Feasible paths therefore inject into the sets of size zero, one or two, giving 137.

## Adversarial cases

- **Ties:** deterministic tie-breaking is mandatory. A tie does not create a third integer, and the away contribution remains exactly `D_i/4`. Do not describe the tied away choice as strictly farther.
- **Center dependence:** the center must be recomputed from the exact already-chosen higher coordinates. Uniqueness is recursive for a fixed index set; it does not assume the centers are fixed independently of branch choices.
- **Empty intervals:** if the preferred integer is outside the exact remaining-radius interval, no integer is inside, since it minimizes distance. An absent away integer or a failed exact norm inequality kills that index set; no substitute integer may be inserted.
- **Interval boundaries:** retain equality when testing `D_i(n_i+c_i)^2<=remaining radius squared`. The strict inequality is used only for the general radius-less-than-one and three-away exclusions.
- **Exact arithmetic:** count/prune with rational cross-comparisons. A floor-of-energy rejection score is not the exact energy for proving an away-index count, and floating square roots/ties must not choose candidates.
- **Signed budgets:** the Euclidean bound is only necessary. Every surviving vector must still undergo both original signed weighted-mass checks with their correct orientation.
- **Lower-prime completion:** a surviving vector is a relaxed p17 modular candidate, not a complete H0/H1–H6 collision. Retain it for exact lower-prime and full-observer completion. Emptiness would exclude the relaxed order-one class; survival alone proves neither a collision nor a T6 bound failure.

## Residue-specific static filter

For one order-one vertical atom with residue `r=1,...,16`, its exponent mass is

`a-1=17(r+17)-1=288+17r`.

Up to global sign, one q0 side retains 2331 and the other retains `2043-17r`, so

`R_r^2=2331^2+(2043-17r)^2`.

Every away set `S` must satisfy

`sum_(i in S) D_i <= 4R_r^2`.

This necessary condition can reject index sets before computing any centers. All sixteen singleton indices pass in each of the sixteen classes. Exact static pair comparisons yield:

| Residue r | R_r squared | Eligible pairs | Upper bound on complete paths |
| --- | ---: | ---: | ---: |
| 1 | 9538237 | 19 | 36 |
| 2 | 9469642 | 17 | 34 |
| 3 | 9401625 | 15 | 32 |
| 4 | 9334186 | 14 | 31 |
| 5 | 9267325 | 13 | 30 |
| 6 | 9201042 | 11 | 28 |
| 7 | 9135337 | 9 | 26 |
| 8 | 9070210 | 7 | 24 |
| 9 | 9005661 | 6 | 23 |
| 10 | 8941690 | 6 | 23 |
| 11 | 8878297 | 5 | 22 |
| 12 | 8815482 | 3 | 20 |
| 13 | 8753245 | 1 | 18 |
| 14 | 8691586 | 0 | 17 |
| 15 | 8630505 | 0 | 17 |
| 16 | 8570002 | 0 | 17 |
| Total | — | 126 | 398 |

These comparisons inspect only `16*binom(16,2)` fixed Gram-Schmidt pair sums. No affine representative, center, candidate path, prefix or census was evaluated.

## Fixed static input

`/workspace/em-owner-resume-20261011/new-round-20261011/t6-frozen-result-independent-preparation-20261012/source-inputs/research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/p17_q0_certificate.json`

SHA256: `fdf0b060d47bccd5b2a5095dc4b72d13b68476f49494eb4435b0b50dd30c65f6`.

There are sixteen exact rational `gram_schmidt_squared` entries. The minimum is at zero-based index 11:

`8350069911612335617606677214061177705401058080646556447012234889468081355909 / 480650972868542992444263969893692042421717754534280313801217347854273`.

The comparisons `all D_i>9,538,237` and `3 min(D_i)>4*9,538,237` were made by arbitrary-precision rational/integer arithmetic. The parent's separately completed certificate reconstruction is not repeated or claimed as this paper pass's execution.
