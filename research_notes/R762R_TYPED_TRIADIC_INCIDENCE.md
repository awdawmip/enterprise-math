# R762R — An equivariant, source-typed six-step triadic incidence automaton

Status: **AUTHOR-SIDE EXACT CANDIDATE / NOT_REVIEWED**. Date: 2026-11-14 Asia/Shanghai. Parent task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, immutable publication `TP2-8B7E13C5904A2D6F1142`. Researcher `EM-X6-BE325A`, Activity `RA-52C39FF585349DD1C655DD1B`. Scientific input remains frozen at `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. This is a **constructive candidate local Cell/Link/Port incidence and phase evolution**. Its force-event admission against the actual native `TRIADIC_CLOSURE_E` and V29/V39 rules remains an open comparison.

## 1. Exact question

R762H established that a closed signed-native Cell path covering three distinct signed nearest-neighbor ports needs at least six steps and has 24 shortest witnesses, of which six are successive three-spoke excursions. R762K demonstrated a symmetry obstruction to a preferred source-independent cyclic direction. We now ask whether the six three-spoke witnesses support a **deterministic S6-equivariant typed time evolution** with a sharp minimal source-order memory, and whether future observations can recover that source order from coarse spatial currents.

The signed Cell carrier is the affine `Z^6` torsor fixed by P000 V5. Work at an arbitrary Cell `c` and a three-element set `T={u,v,w}` of distinct-axis signed unit directions `±e_i`. The six-axis permutation skeleton `S6` acts by relabelling the axes and the Cell chart; the signed directions' signs are not silently reversed by this physical symmetry. Give each direction its own nonzero, equal-quantum force-source identity and a Cell/Port incidence link `(c,c+p)`. The three sources are retained throughout the event, even when only one spatial excursion is currently moving.

The *ordered-lift fiber* is `Ord(T)`, the six bijections `ell=(p0,p1,p2)` ordering T. This carries a natural action `g ell=(g p0,g p1,g p2)`. Define an internal phase `t in {0,...,6}` and a moving path packet Cell `x`; this internal phase is not a seventh spatial coordinate.

## 2. A fully typed candidate event

For a given `ell`, define the six signed **primitive** native coordinate steps

```
w(ell) = (p0, -p0, p1, -p1, p2, -p2).
```

Let `x_0=c` and `x_{t+1}=x_t+w_t(ell)` for t=0,...,5. Each individual arrow is a signed single-axis Cell adjacency. Throughout, keep the three independent equal quanta, their signed source IDs, anchor c, three incidence links, ordered trace and branch multiplicity; the walker packet is an additional carrier, not a replacement for the force sources.

Define the *candidate completed incidence event* `E_star(c,T,ell)` by the exact certificate `x_6=c`, each of `c+p0,c+p1,c+p2` visited at its excursion phase, all three force quanta present and distinct-axis with pairwise `PERP_E`. In this explicit local model, the predicate holds for every `ell in Ord(T)`. This is a declared constructive force-incidence hypothesis, not a proof that the unimplemented native physical admission law accepts every T.

The candidate next-event update is

```
F(c,T,(p0,p1,p2)) = (c,T,(p1,p2,p0)).
```

All three force sources and spatial Cell remain intact, while the internal *order* rotates. The six microstep transitions and the one event-completion update are deliberately separately typed; there is no Euclidean three-vector cancellation, no composite diagonal primitive step and no ordinary clock-time calibration.

## 3. A sharp equivariant-selector theorem

**Theorem (uniform minimal deterministic order lift).** For a same-sign triad T of distinct native axes, no deterministic `S6`-equivariant operation can choose an ordered three-spoke witness from T alone. More strongly, any equivariant extended-state system over T that can output an actual total order of the three ports must have **at least six distinct internal states over T**. The `Ord(T)` construction attains six and extends consistently to all 160 signed distinct-axis triads.

*Proof.* The stabilizer of an all-positive (or all-negative) T in S6 contains S3 permuting the three selected axes. It fixes T setwise and acts freely transitively on the six total orders of T. A supposed equivariant order selector `f(T)` would have to be fixed by this stabilizer; no order is fixed by a nonidentity selected-axis permutation. For an extended internal-state fiber Y_T with equivariant output `h:Y_T -> Ord(T)`, the S3 orbit of any y has image the six distinct orders `h(g y)=g h(y)`. Consequently |Y_T|≥6. Conversely Y_T=Ord(T) gives an equivariant identity output and has six states. Uniform extension to mixed-sign triads needs no extra states. QED.

Only choosing a *cyclic orientation* (forgetting the starting source) needs two choices on an all-same-sign triad: the two cyclic-orientation classes. Picking an actual first source as well requires the full six-state ordered fiber. This distinction does not privilege an axis or invent an absolute orientation.

## 4. Native Cell return, hidden internal holonomy and repeatability

**Theorem.** The six-step candidate event returns to its original native X6 Cell and has zero rooted signed-edge current, but `F` acts nontrivially on the ordered source state. For each fixed T, its six ordered lifts form **two disjoint cycles of length three** under F. Across all signed distinct-axis triads, there are exactly **320 three-event cycles** on **960 ordered lifts**.

*Proof.* Each adjacent pair `(p,-p)` traverses the same native edge in opposite directions, so the Cell returns immediately at phases 2,4,6, and all rooted signed-edge currents cancel. The order update F is a nontrivial 3-cycle on an ordered triple: `F^3=identity` while F and F² are not identity. Six orders split into two `C3` orbits, distinguished by cyclic orientation. There are `binom(6,3)·2^3=160` signed triads, giving 160·6=960 ordered states and 160·2=320 cycles. QED.

Thus every completed candidate event remains repeat-admissible **under this declared candidate law**, and consecutive event order repeats after three events. It provides an explicit example of an internally nontrivial, covariance-preserving transport over a spatially closed Cell trace. This internal order transport is **not yet identified with the native V39 holonomy**; that comparison requires its actual field/Link transport law.

## 5. Exact temporal BRC observer theorem

Fix T. Let the coarse observer after any completed event retain only its native endpoint and rooted directed edge current `O_current=(c,j_X6)`. For every ordered star witness `j_X6=0`; repeated application of F leaves this observer constant over arbitrarily many completed events. Therefore **no finite or infinite sequence of completed-event current/endpoint snapshots distinguishes any of the six initial orders**. This is an exact future-operation counterexample to erasing source order.

Now declare a finer provenance-retaining observer `O_first` recording the identity of the first source whose port is visited during each event. For initial order `ell=(p0,p1,p2)` its observations under F are `p0,p1,p2,p0,...`.

**Theorem (sharp temporal repair).** One `O_first` observation has exactly three values with fibers of size two. The first two consecutive `O_first` observations identify all six initial source orders uniquely; two event rounds are necessary and sufficient to recover the ordered source state.

*Proof.* First observation supplies p0, leaving two possible orders of the remaining ports. Second observation supplies p1, and p2 is the unique remaining element of T. The pair (p0,p1) ranges over 3·2=6 distinct possibilities. One observation has at most three values and cannot distinguish six orders. QED.

This demonstrates an exact BRC joint-relation restoration through a *time-indexed source observer*, rather than endpoint or positive-mass inference. It is compatible with R762Q's principle that temporal observability depends on the actual update and the observer, but uses a different explicit native-coordinate incidence model.

## 6. Scope, verification and unresolved physical interface

`research_notes/R762R_VERIFY.py` exhaustively checks all 160 signed triads, all six ordered lifts each, all 720 axis permutations, every microstep's native adjacency, endpoint/current return, three-event source-order cycles, two-round identifiability, and equivariance. Its machine-readable expected output is `research_notes/R762R_EVIDENCE.json`; the finite exhaustive census is supported independently by the group-action and path proofs above.

This construction supplies a completely explicit **candidate Cell/Link/Port force-incidence automaton** and a sharp symmetry/minimal-memory result. The next scientific admission question is whether the actual P000-compatible `TRIADIC_CLOSURE_E` force event can be specified to agree with `E_star` (or which typed field/Link gate excludes it). For an admitted event, separately derive the true V29 PASS/TRANSFER rule and true V39 based transport, then check whether `O_first` descends through those real event updates. No numerical native residual, physical duration, force magnitude calibration, Result freeze, independent Driver approval or change to P000 is asserted.

Sources: frozen `p000_reality_foundation.json`, `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`, `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`; exact predecessors R762H PR #2288 (six star witnesses and path/current fibers), R762K PR #2297 (S6 orientation obstruction), R762Q PR #2328 (temporal observer parity criterion).
