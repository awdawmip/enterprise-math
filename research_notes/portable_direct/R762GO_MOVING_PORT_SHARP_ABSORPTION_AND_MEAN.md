# R762GO — Sharp eight-event absorption bound and certified mean hitting time in the moving-Port STAR candidate

**Project:** Enterprise Math / RS-X6-TRIADIC-CLOSURE-DYNAMICS  
**Scientific source:** frozen task pin `857280d1012943290d141d1317179c40ec3cbdf8`; P000 `4e318b1a978a4c4e26817752354cdd3e63ebee87`.  
**Prior frontiers:** R762GM (moving Port, PR #2828, commit `961479945c690fd07277ce30fba01c1f8edbe552`); R762GN (absorption, PR #2831, commit `0567ebf90fa66b60ca4a9e7e90e262e9f7bb89cb`).  
**Evidence status:** author mathematical derivation plus an exact complete finite-state checker; **NOT_REVIEWED**.  
**Scope:** explicitly constructed signed K4-STAR semidirect *candidate*; no assertion that its Port gate is the native `TRIADIC_CLOSURE_E` permission predicate.

## Model and source semantics

Label K4's six edges in order `01,02,03,12,13,23`. Set `G = Z^6 ⋊ A6` with multiplication `(x,p)(y,q)=(x+p·y,pq)`. Four named STAR rotations `C_v` are 3-cycles of the three edges incident to vertex `v`. At orientation `p`, the named Port is `p(01)`. An event chooses either endpoint `v` of that Port and a sign `s in {-1,+1}`, then applies the branch `(s H_v,C_v^s)`. Thus there are exactly four equiprobable BRC **source words** at every event. The semidirect Cell translation, event order and positive multiplicity of signed words remain separate typed data.

Let `O = {p in A6 : p(01)=23}`, the absorbing orientation set of R762GN, and `τ = inf{m >= 0 : p_m in O}` for a walk starting at identity. Here absorption is about *orientation only*. No Cell projection is used to infer a signed physical cancellation. R762GN established `|O|=60`; 350 orientations are reachable from identity, of which 290 are outside O.

## Theorem A — sharp eight-event conditional survival bound on the reachable transient set

For every orientation `p` that is reachable from identity and lies outside O, the number of its length-eight permitted event words that avoid O throughout is at most **39,652**, out of `4^8=65,536` source words. The bound is attained at the reachable orientation

`p*=(0,2,1,4,3,5)`.

Consequently, for every nonnegative integer `m`,

`Pr(τ>m+8 | τ>m) <= 39652/65536 = 9913/16384`

whenever the conditioning event has positive probability, and

`Pr(τ>m) <= (9913/16384)^floor(m/8).`

This bound improves the R762GN uniform three-event estimate `(63/64)^floor(m/3)` for sufficiently large horizons, and the new eight-event coefficient is **optimal uniformly over reachable, nonabsorbed orientation states**.

### Proof

Enumerate the 360 even permutations of six labelled edges as distinct orientation states, and define the four directed successor edges by the Port-gated STAR events. A breadth-first traversal from identity gives exactly 350 reachable states. Every transition out of O remains in O, so the transient reachable set `T=Reach(id)\O` is forward-invariant until absorption.

For each orientation `p`, define integers `F_0(p)=1` for `p notin O`, `F_0(p)=0` for `p in O`, and recursively

`F_{n+1}(p) = 1_{p notin O} sum_{v in endpoints(p(01))} sum_{s in {-1,+1}} F_n(p C_v^s).`

Inductively `F_n(p)` counts precisely the ordered length-`n` signed BRC words that have not entered O. The complete finite-state calculation gives

`max_{p in T} F_8(p)=39652`, attained only at `p*`, while `F_8(id)=38036`.

A shortest path to `p*` is encoded as the branch-choice index sequence `[0,3,0,2,0]` (indices 0–3 mean first/second endpoint of the current Port, with negative branch before positive branch). The verifier reconstructs the entire path and checks its nonabsorbed orientations. Therefore the maximum applies to an orientation actually attainable from the initial condition.

Given survival up to time `m`, every conditional orientation lies in T. Its next eight permitted event choices are equiprobable, so the conditional survival probability is at most `39652/65536`. Applying the Markov property at consecutive eight-step block boundaries proves the horizon bound. Equality of the one-block coefficient is witnessed by `p*`. **QED.**

## Theorem B — finite mean and a rigorously certified numerical interval

The mean first absorption time satisfies the exact bound

`E[τ] <= 8/(1-9913/16384) = 131072/6471 < 20.256` events.

More sharply, the exact BRC dynamic program at horizon `N=400` proves

`12.9394684528142641906014700978616 < E[τ] < 12.9394684528142642040268420357575`.

This interval has width below `1.343 × 10^-17`. In particular, rounding to 15 decimal places yields `12.939468452814264`.

### Proof and complete numerical certificate

Let `S_m` be the number of allowed length-`m` source words from identity that never enter O. Then

`Pr(τ>m)=S_m/4^m`, hence `E[τ]=sum_{m>=0} S_m/4^m`.

Theorem A bounds the geometric eight-step blocks by `q=9913/16384`, so the expectation is at most `8 sum_{j>=0} q^j=8/(1-q)`.

For the sharp interval put `N=400` and the exact integer

`U_N = sum_{m=0}^{N-1} S_m 4^{N-m}`.

Integer forward dynamic programming on the 360-state orientation graph produces `U_N` and `S_N` (the decimal integers are recorded in the machine-readable evidence). The exact lower bound is `U_N/4^N`; the remaining tail is bounded by

`0 <= E[τ]-U_N/4^N <= (S_N/4^N) * 8/(1-q)`.

All arithmetic before decimal rendering is over integers or exact rational numbers. The checker prints both rational inputs and outwardly enclosed decimal endpoints. The displayed strict interval uses weaker rounded-out endpoints than these rational bounds, and is therefore a mathematically certified enclosure. **QED.**

## Verification scope and checks

Run `python3 research_notes/portable_direct/R762GO_VERIFY.py` (standard library only). The script checks: all 360 even permutations and 1,440 signed transition entries; `|O|=60`, closure of O; reachability 350, reachable transient states 290; complete 8-step `F_8` over each transient state; unique maximum 39,652 and attaining orientation and path; the independent **forward** source-word recurrence versus **backward** recurrence for every horizon `0..20`; established R762GN counts `S_12=6,534,252` and `S_16=1,118,196,052`; exact `N=400` tail enclosure. The JSON output in `R762GO_EVIDENCE.json` records the exact rational numerators/denominator and observations.

The finite enumeration proves the exact finite maximum because every member of its declared finite domain is examined; the unbounded-horizon probability and expectation results follow from the stated recurrence and Markov-block argument, not from extrapolating a finite plot.

## Boundary and next science

The candidate's absorption law is a structural residual of **orientation and named Port updating**, not a claim about physical irreversible motion. Converting these results into native `TRIADIC_CLOSURE_E` requires an exact, signed and source-preserving Cell/Link/Port license and an observer map on the frozen P000 substrate. The separate R762GM/GN open question—whether a full affine joint return `(±D,id)` is legal—remains unresolved.

Next discriminating research: (1) derive a native typed Port/Link update and test whether O remains closed; (2) study first-return depth residue classes under the actual license, or isolate a counterexample to the moving-Port assumption; (3) use the exact orientation kernel to obtain an asymptotic spectral survival certificate without discarding BRC word provenance.

**Storage:** immutable research proof, checker and exact evidence on one GitHub research branch/Draft PR. No formal Task CLAIM, protected PROGRESS, independent review or P000 promotion is asserted by publication.
