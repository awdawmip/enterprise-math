# R85 — Incremental exact source certificates with persistent time-support reuse

Date 2026-11-12. **Author-side auxiliary rational circular-source research**, not native X6/BRC dynamics, a shared Task CLAIM, formal Result or independent Review. Frozen S23/AV science pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34` remains unchanged. Predecessor: R84 `f141f6157e7539c6806f1af8ccbd164cce94b3ab`; reuse R71/R72/R77/R82/R84 exact source semantics.

## Domain and exact oracle

Events are finite independent identities `(t,branch)`, with integer time `t`. Fix observer integer `j`, rational `x`, integer original labels `a,b`, and rational closed interval `I=[L,U]`. The directed, original-labelled half-open circular arc is `[{aθ},{bθ})`, empty for equal endpoints. Source membership `M_t(θ)` means `{x+(t-j)θ}` lies in that arc. Branch identity does not occur in this predicate but must remain in the full event registry. The complete **existential** interval decision here is `EXISTS_MEMBER(t,θ*)` with rational witness or `ALL_OUT` for every real parameter. This is not a complete latest-time-function or CHANGES certification.

For the exact single-time oracle assume stable, nonwrapping arc on `I`: `ka=floor(aθ)` and `kb=floor(bθ)` constant and `0 <= aθ-ka < bθ-kb < 1` for every θ in I. Write `α=x+(t-j)θ`, `A=aθ-ka`, `B=bθ-kb`. Then

```
M_t(θ) <=> exists integer k with α(θ)-B(θ) < k <= α(θ)-A(θ).
floor(min_I(α-B))+1 <= k <= floor(max_I(α-A)).
```

For each finitely many k, intersect `I` with exact rational affine constraints `α-A-k>=0`, `α-B-k<0`, retaining strict endpoint flags. Every nonempty rational interval contains an exact rational witness (a closed singleton or midpoint), and failure of every k certifies OUT on **all real θ**. Independent validation uses the R77 finite-critical-stratum alternative: enumerate all integer-level breakpoints of α, α-A, α-B, evaluate each breakpoint and one rational midpoint of every intervening open interval.

## Theorem R85.1: dynamic version transport

Fix the typed query signature `σ=(j,x,a,b,I)`, and keep the independent full event registry and distinct-time support `T(E)`. Store three kinds of evidence:

* `OUT(t,σ)`: the complete exact single-time oracle excluded t for every real θ in I.
* `IN(t,σ,θ*)`: an exact rational θ* in I such that t qualifies.
* `CERT(p/q,r,lo,hi,σ)`: an R71 sufficient phase-envelope exclusion for all integer times in the anchor residue `tp mod q=r` within [lo,hi], over I.

For an arbitrary sequence of source insertions, deletions, branch edits and historical-version queries, these entries remain correct for their stated time/residue/signature independently of the version's other events and its global GCD. A present source with an IN witness certifies EXISTS_MEMBER. If every present distinct time is covered by OUT or compatible CERT, the answer is ALL_OUT. For any uncovered time run the exact oracle and save its answer.

**Proof.** M_t for fixed σ is a predicate of t and θ, independent of the event collection, branch identities and global GCD. Its fixed-time positive/negative result therefore transports between versions. An R71 exclusion certificate universally excludes every time in its stated residue and envelope; R84's time-envelope containment theorem transports that certificate to any version whose relevant times remain inside. Each currently present time can use one of these proofs independently. A single positive witness makes the existential true; exhaustive negative coverage makes it false. Exact oracle evaluation of remaining times completes the disjunction. Older immutable versions use their own preserved supports. QED.

## Theorem R85.2: amortized exact-oracle bound

For one unchanged σ, let D be all distinct times ever encountered by the update sequence that were *not already covered by a compatible seeded certificate* on first relevant inspection. If each first exact evaluation is memoized, the total number of complete single-time oracle invocations over any number of versions is at most `|D|`. Branch-only edits, deletions and reinsertion of a previously classified time require **zero further** complete oracle calls.

**Proof.** Charge every exact oracle invocation to the previously unclassified time t. The memoized positive/negative result is immutable under fixed σ, so t cannot be charged again. An unreached time or a time covered by a group certificate is not charged. The claimed bound follows by injection into D. This is an oracle-call bound, not an assertion of sublinear total running time, bit complexity, memory or support-index update cost. QED.

For a newly added time beyond a cached class envelope it suffices to classify that time separately; all old negative proofs survive, even if a fresh convex envelope of the entire enlarged class fails its sufficient test. Thus this rule improves upon exclusively rechecking the new class's R71 hull. Full identity provenance remains accessible for later branch deletions.

## Precise interval refinement rule and counterexample

Under `I' subset I`, OUT and R71 CERT proofs remain sound. An IN witness is transferable **only if its θ* belongs to I'**; otherwise exact rechecking is needed. E.g. `t=40, j=x=0, a=1,b=2`, old `I=[1/4,31/120]` has a member at `θ=31/120` because `{40θ}=1/3` belongs to `[31/120,31/60)`. New `I'=[1/4,1/4+1/1200]` is ALL_OUT because `{40θ}` ranges in `[0,1/30]`, below the target lower endpoint `>=1/4`. Source, observer, labels, anchor, phase residue, or stability-domain changes require corresponding key/premise checks; no unrestricted cache transfer is allowed.

## Exact executable evidence

`check_r85.py` uses only standard-library `Fraction`, exact integer inequalities and independently constructed critical-stratum witnesses; output is `verification.json`. Deterministic seed 8520261112. Base query `θ0=1/16`, `I=[θ0-1/100000,θ0+1/100000]`, `j=x=0,a=4,b=8`. Seed two proved R71 phase-class exclusions of 20 initial distinct times in residues 0,12. Walk 244 versions comprising 80 branch-only edits, 40 deletions and 40 reinsertions, 40 newly added outer times and their duplicate branches, and a positive-time insertion/removal/reinsertion. Independently reclassify **all** current distinct times at each version with the exact oracle.

**Observed:** 244/244 exact interval decisions agree (242 ALL_OUT, 2 EXISTS_MEMBER). Full repeated oracle baseline: **6,602** invocations; incremental cache: **41**, plus two seeded R71 group certificates; 4,840 covered-time hits and 1,721 exact-verdict memo hits. A separate critical-stratum reference oracle agreed on 600 randomized bounded exact-rational instances, including singleton intervals. Positive-witness interval-shrink and R71 old-envelope expansion counterexamples both pass. This demonstrates oracle-call reuse in this finite workload; it does not measure CPU acceleration, AVL node/byte costs, big-integer bit cost or the latest-source CHANGES obligation.

## R86 continuation

Integrate signature-indexed unresolved/positive aggregates with R82's actual persistent AVL time-support and phase-group trees, retaining branch identities and immutable version paths. Test true latest-source STABLE/CHANGES certificates, branch-tie semantics, interval shrink, original-label boundary crossings via R77 strata, and per-version source GCD updates. Compare actual time, integer bit lengths, allocated/retained nodes and memory with R83 heap and R84 full-index implementations at the same mathematical output obligation. Preserve the frozen science pin. This author-side source grants no formal CLAIM, independent Review or Foundation promotion.
