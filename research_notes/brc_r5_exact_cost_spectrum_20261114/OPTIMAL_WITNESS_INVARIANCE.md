# R5: Universal optimal-center witness-set invariance at K=292 and K>=315

Date: 2026-11-14. Author-side exact derived one-dimensional integer-event theorem; `NOT_REVIEWED`. Frozen scientific pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Companion: `RESEARCH.md` and `VERIFY_R5_COST_SPECTRA.py` in this directory.

## Statement

For a gap-closure set B⊆{0,...,27} let `Opt_B(K)` denote **the collection of event-index subsets S**, each of cardinality K, feasible at radius 2 and minimizing the sum of distances from each event to its nearest selected center. Center indices refer to the **same 954 original event labels** in all closure patterns.

**Theorem:** For every one of the 268,435,456 gap-closure patterns B,

```
Opt_B(K) = Opt_empty(K)   for K=292 and for all 315<=K<=954.
```

In particular, these budgets preserve the *entire set of optimal center-index witnesses*, not just optimal cost or the number of optimizers.

## Proof

Previous frozen R5 monotone-gap lemma proves that every feasible center-index subset before closing a gap remains feasible afterwards with **exactly the same total nearest-center cost**, for any radius-two-feasible subset. The companion cost theorem proves that `J_B(K)=J_empty(K)=J_all(K)` for every K>=214.

Therefore, for every B and K>=214,

```
Opt_empty(K) ⊆ Opt_B(K) ⊆ Opt_all(K).
```

The new exact counting certificate computes the cardinalities of the first and last sets from a *chosen-center path DP*, for all K=213,...,954. Their cardinalities agree for **K=292** and **every K=315,...,954**. The displayed inclusions between finite sets and equality of endpoint cardinalities then force equality of the actual sets for every B at those budgets. QED.

This makes no claim about BRC branch/provenance history or native six-axis states; the preserved witnesses are subsets of the original one-dimensional event **indices** for this fixed objective.

## Exact contrasting low-budget evidence

At K=214 the min total cost is exactly 1064 both before and after all 28 closures, but the optimal center-index-set counts differ:

```
|Opt_empty(214)| = 71400940037117596391178240000
|Opt_all(214)|   = 4573020854769248525038387200000
ratio             = 83005/1296 ≈ 64.0470679012.
```

This is a concrete information-loss witness: *equal minimal costs do not imply the same optimal-solution families*.

The full endpoint comparison across the **742 budgets K=213,...,954** finds exactly **101** budgets where the optimizer counts differ: every K=213,...,314 **except K=292**. The other 641 budgets have equal counts: K=292 and K=315,...,954. For K=213 the endpoint optimal costs differ; the all-closure count comparison there is only a separate numerical observation, not part of the monotone-set-inclusion proof.

Other exact endpoint checks:

| K | J_empty | J_all | Number of optimal center-index sets, empty | all |
|--:|--:|--:|--:|--:|
|292|744|744|247939829006869892620615680|247939829006869892620615680|
|314|678|678|34372089438980233382036766720000|34551159313954027401935585280000|
|315|675|675|402907218691036544772341760000|402907218691036544772341760000|
|954|0|0|1|1|

## Counting certificate

A selected center-index set `S={j_1<...<j_K}` determines exactly one increasing path of centers. Its cost is: the left prefix served by `j_1`, the sums of each event between `j_t` and `j_{t+1}` assigned to the nearer of the two adjacent chosen centers, and the right suffix served by `j_K`. Every radius-two-feasible subset corresponds to exactly one such path; no cluster tie-breaking multiplicity appears.

DP `F[k,j]` stores the least cost among paths of k centers ending at j; `N[k,j]` stores the count of such optimal paths. For each valid predecessor i<j and exact edge cost `e(i,j)`, minimize `F[k-1,i]+e(i,j)`; on strict improvement replace the count, and on ties sum predecessor counts. Minimize `F[K,j]+suffix(j)` over valid last centers j and sum tied counts. Integer arithmetic is exact. The resulting `N` counts distinct index subsets, not assignments or center locations after translation.

The implementation in `VERIFY_R5_OPTIMAL_WITNESSES.py` recomputes both endpoint counts for all budgets and checks the exact 101/641 split plus the K214 ratio. Its recurrence was independently compared with brute-force enumeration for 400 small random integer sequences of length 2 through 9, i.e. 2,200 exact `(sequence,K)` budget cases. All matched.

## Next discrimination

For K in 214,...,291 and 293,...,314, determine precisely which closure patterns create new optimal center-index subsets, and whether the 13 cost-inert gaps identified by the companion theorem are also *optimal-set-inert* under every other closure configuration. Proceed to minimal edit-distance distribution only after retaining the relevant actual witness sets. The native certificate/coordinate/prefix-query end-to-end benchmark remains a separate objective.
