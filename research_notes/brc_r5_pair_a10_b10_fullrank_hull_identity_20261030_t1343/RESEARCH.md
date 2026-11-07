# R5 — A sparse two-node lift with **equal full-rank four-observer convex hulls**

**Date:** 2026-10-30 (Asia/Shanghai). **Scope/status:** author mathematical proof, exhaustive exact-rational Carathéodory certificates, unreviewed, not natively admitted. Auxiliary finite two-measure stopping model, not a native Heartbeat/X6 dynamics or external physical claim.

## Frozen provenance and retained contracts

* GLOBAL_KNOWLEDGE_V1 canonical `main@5f1ec1f4e9565307ebc0c7be4a14faa909463a60`, read for this run: `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, ACTIVE `我眼中的世界.md`, P000 V4 and applicable research rules.
* Enterprise Math canonical `main@72298ad74a277018c9eda7640abb788b14a77b1d`: `AGENTS.md`, portable-research protocol and control authority. Proof predecessor (unmerged PR #1663): `abcd9b8ebc5c50ff0eaf51574221cdea8eedd00d`, `research_notes/brc_r5_rank4_single_node_no_go_20261030_t1240/{RESEARCH.md,VERIFY.js}`.
* P000 remains unmodified. P/Q history masses, source and likelihood-ratio collisions remain distinct until the declared four-stop readout. Formal observer coordinates in R^4 are external auxiliary statistics, not an assertion of a two-dimensional native plane or native X6 embedding.
* Native canonical owner query returned `CONTROL_QUOTA`, and the directed context reported `authority_granted=false`; GitHub preservation has no Source CLAIM/Result/review/admission effect.

## Exact model

Use the 14-node tree, parent map and positive integer P/Q masses in `VERIFY.py`; masses have common denominator 360. The level-two collision is A1/B1 and level-three collision A11/B11, under the key `(time,Pmass/Qmass)`. A FULL policy has 14 local stop variables. A seedless LR policy uses 12 shared time-LR keys. All variables range over [0,1], and all policies stop by t=4.

Set `eta=1/1000`, and for a stop at node `(t,h)`, writing `L=P(h)/Q(h)`, define

```
p_delta(t,h) = 1/5 + t/20 + (t+1)/(100L) + delta * 1_{h=A10 or h=B10}
q_eta(t,h)   = 2/5 - t/30 + (t+2)L/200 + eta * 1_{h=A11 or h=B11}.
```

No perturbation applies at mandatory t=4. All terminal error probabilities are strictly inside (0,1) for `-41/100 < delta < 57/100` (the intersection of the two altered-node constraints; every unaltered error is strictly legal). In particular delta = +/-1/1000 are exactly verified. Let `(eP,eQ,TP,TQ)` be terminal P/Q errors and P/Q expected stop times.

For any deterministic mask let `z_h` indicate reaching and stopping at node h. Use the mass-weighted integer statistics

```
r = 15*z_A11 + 20*z_B11
x = sum_{t<=3,h} (4-t)*Pmass(h)*z_h
 y = sum_{t<=3,h} (4-t)*Qmass(h)*z_h
s = 30*z_A10 + 20*z_B10.
```

Their expectations define the same statistics for real behavioral stopping. Change of measure gives the *exact* affine observation map

```
TP = 4 - x/360 ; TQ = 4 - y/360
 eP = 21/100 + TP/20 + TQ/100 + delta*s/360
 eQ = 41/100 + TP/200 - TQ/30 + eta*r/360.
```

For every `delta != 0` and `eta != 0`, this map is invertible on R^4. Therefore four-observer convex-hull equality and affine rank are equivalent to those of `(r,x,y,s)`. In particular there is no small-delta approximation.

## Theorem — full rank and all-signed equality for a two-node lift

**For every real `delta` satisfying `-41/100 < delta < 57/100` and `delta != 0`, with eta fixed to 1/1000, the convex hulls of all FULL and seedless LR four-observer real behavioral-policy images are exactly equal, and their common affine dimension is four.** This result settles *only* the convex-hull part of the four-observer mother question for this concrete lift; the actual (nonconvexified) real behavioral images have not been shown either equal or unequal.

### Fully finite rational certificate

1. Each policy evaluates a multiaffine function in its own independently parameterized time-information stopping decisions: a sample trajectory visits each key at most once. Product interpolation over its behavioral hypercube expresses every real-policy observation as a convex combination of the observations of deterministic binary policies of the same class.
2. The deterministic FULL class contains 2^14=16,384 masks and 647 distinct `(r,x,y,s)` vectors; the LR class contains 2^12=4,096 masks and 272 distinct vectors. Every LR deterministic policy has a corresponding FULL policy, proving `conv(LR) ⊆ conv(FULL)`.
3. `R5_PAIR_A10_B10_CERT.jsonl` contains **all 647 distinct FULL vectors**, each with a representative FULL mask and a convex representation by **at most five** LR deterministic masks. `VERIFY.py` constructs the complete deterministic sets itself, requires exact set equality of the 647 distinct vectors with the certificate keys, verifies LR observations directly for each mask, and checks every displayed nonnegative rational weight, exact sum one and four exact coordinate equalities. Therefore `conv(FULL) ⊆ conv(LR)`.
4. The five LR masks `(0,1,2,128,256)` have `(r,x,y,s)` rows `(0,0,0,0)`, `(0,360,720,0)`, `(0,720,360,0)`, `(0,30,45,30)`, `(35,70,35,0)`. Their oriented four-dimensional affine determinant is **408240000**, proving full affine rank four.

Example: the FULL mask 15858 has `(r,x,y,s)=(0,810,585,30)`, equal to **one half** each of LR masks 130 and 134. This is one of the 647 identities, not a substitute for exhaustive coverage.

### Computational coverage versus mathematical scope

`VERIFY.py` uses only Python standard-library `Fraction`, exact integers, a 24-term integer determinant, and JSON parsing. It executes all 16,384 FULL and 4,096 LR masks; validates conservation of both laws and precisely the two LR collisions; checks terminal probabilities at delta=+/-1/1000; checks all 647 ≤5-point mixtures exactly; verifies nonzero rank determinant. Its actual executed stdout is in `EXACT_OUTPUT.txt` and ends in `PASS_EXACT_R5_PAIR_A10_B10_RANK4_HULL_EQUALITY`.

For discovery only, the author used floating-point LP to propose sparse mixture supports, followed by exact rational reconstruction. **No floating-point LP or numerical hull enumeration is needed by the final certificate checker.** The proof of the real-policy convex-hull statement is the exact finite certificate plus the mathematical multiaffine interpolation lemma and the invertible affine map, not finite real-policy sampling. The parameter generalization uses the *same* exact observer-polytope proof for all nonzero admissible delta; no parameter sampling is involved.

No independent Driver review, formal mechanized theorem checker, novel-prior-art determination, native Source CLAIM or Research Result acceptance is claimed.

## Next decisive unit

Determine whether the **actual real behavioral observation images**, *without randomizing between entire policies and without a persistent seed*, are identical for this full-rank A10+B10 model. A certified inequality would finish the mother target's existence requirement; if the images are equal, record a constructive surjection or certified semialgebraic equality and search a different two-node lift. A feasible approach is to exploit independent A10/B10 time-3 actions and the shared A1/B1 time-2 action, eliminate private stop variables, then derive exact rational polynomial feasibility (quantifier elimination, interval-certified SOS, or a finite topological degree certificate). A failed numerical solver or a failed sufficient face-star condition **does not** prove nonmembership. Keep the two collisions, positivity, and actual four observer semantics fixed.
