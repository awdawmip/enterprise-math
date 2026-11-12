# X6 signed-triad rotations: exact descent criterion and minimal common-depth repair

Status: DRIVER_MATHEMATICAL_AUDIT / EXACT SCOPED ALGEBRA / NOT_NATIVE_RESULT_ADMISSION  
Date: 2026-11-12 (+08)  
Parent: `RS-X6-NATIVE-ROTATION-DYNAMICS` / `PO-X6-UPPER-STRUCTURE-20260906`  
Contribution: a new Driver proof and repair, building on prior X6 native signed-Cell, joint min-zero observer, and the Driver-authored candidate triad C6 group. It does not claim an independent native review, an actual FCC carrier for all 20 coordinate triples, or time/force dynamics.

## 1. Frozen data and question

Use the native signed Cell displacement group `G=Z^6` (relative to a chosen Cell anchor), its diagonal subgroup `Delta=Z D`, `D=(1,1,1,1,1,1)`, and the full joint relative observer
`q(z)=can6(z)=z-(min_i z_i)D`. The twenty min-zero triple coordinate observers jointly determine exactly `G/Delta`, but not the common integer depth. Write uniquely `z=r+hD`, with `r=q(z)` and `h=min_i z_i`.

The previously constructed candidate rotations generate the signed permutation group `B6=(C2)^6 ⋊ S6` after adjoining the existing pure `S6` skeleton, and the triad-only group `H=(C2)^6 ⋊ A6`. We ask: **which signed permutations admit a well-defined transformation of the depth-forgetting relative observer, and how much information repairs the others?**

Every signed permutation is written
`(gz)_i = epsilon_i z_{pi(i)}`, where `pi in S6`, each `epsilon_i in {+1,-1}`. The signs here are ordered by output coordinate, not by input axis.

## 2. Exact quotient-descent theorem

**Theorem 1.** There exists a unique function `bar_g:G/Delta -> G/Delta` with `q(gz)=bar_g(q(z))` for every `z in G` if and only if all six signs `epsilon_i` are equal. Its complete symmetry group inside `B6` is

`K = {+I,-I} × S6 ≅ C2 × S6`, of order `2·6! = 1440`.

**Proof.** A linear automorphism descends to `G/Delta` iff `g(Delta)=Delta`; equivalently, `gD` is a generator of `Delta` up to sign, i.e. `gD=±D`. But `gD=(epsilon_1,...,epsilon_6)`, so this is equivalent to constant signs. Conversely, for `g=pi`, `q(pi z)=pi q(z)`, and for `g=-pi`, `q(-pi z)=max_j(q(z)_j)D-pi q(z)`, so both descend. These give precisely the stated direct product and count. QED.

The triad-generated group has unsigned projection `A6`, hence

`H ∩ K = {+I,-I} × A6`, of order `2·360=720`.

Consequently **22320 of 23040** triad-generated signed transformations do not descend to the joint depth-forgetting observer, despite being exact full-native Cell automorphisms. This is a precise observer-equivariance distinction, not a disproof of any native transformation.

## 3. Optimal repair and exact two-readout recovery

**Theorem 2.** For any signed permutation `g`, the pair `(r,h)` determines its transformed relative observation by

`q(gz)=can6(g r+h epsilon)`, where `epsilon=gD`.

If `epsilon` has both signs, then for every **fixed** `r` the map
`h -> can6(g r+h epsilon)` from `Z` into the relative observer is injective. In particular no finite-valued side channel can suffice for *all* integer depths; retaining the single unbounded integer common depth `h` is sufficient and information-optimal in the precise sense that any exact uniform repair must distinguish each possible `h` on a fixed observer fiber.

Moreover, if both the initial and transformed min-zero readouts `r=q(z)`, `r'=q(gz)` are observed and `epsilon_p=+1`, `epsilon_n=-1`, then the lost original depth is recovered exactly:

`2h = (r'_p-r'_n) - ((g r)_p-(g r)_n)`.

**Proof.** The formula follows from `z=r+hD` and linearity. Min-zero normalization subtracts only a common scalar, so the difference of output coordinates `p,n` equals `(g r)_p-(g r)_n+2h`. Thus distinct integer depths have distinct transformed readouts, and rearrangement proves the displayed recovery formula. A finite alphabet cannot inject all `Z` into distinct future relative observations, while `h` itself realizes the map. QED.

For uniform signs, Theorem 1 gives the sharper zero-extra-depth outcome. Therefore **the exact depth requirement for a fixed signed permutation is zero integer coordinates if its signs are uniform, and one retained integer depth if its signs are mixed**, with the indicated all-integer, all-fiber guarantee. This statement concerns the spatial relative observer only; BRC branch identity, path history, time, force and triadic relations have their own independent retention requirements.

## 3a. Exact finite-path-horizon repair: sharp side-channel capacity

The unbounded-depth necessity in Theorem 2 concerns all of `Z^6`. There is also an exact **positive finite-horizon result** when a full, unrestricted signed primitive word of length `M` is known. Here "unrestricted" explicitly permits immediate reversal; this theorem does not apply unchanged to a no-backtracking BRC subpopulation.

For fixed `r=can6(z)`, put `f_r(h)=sum_i |r_i+h|`. A signed primitive word of exact length `M` with endpoint `z=r+hD` exists **if and only if**

`f_r(h) <= M` and `M-f_r(h)` is even.

Necessity follows from unit-step `L1` distance and step parity; sufficiency follows by taking any shortest signed-axis path and adding exactly `(M-f_r(h))/2` cancelling adjacent step pairs. Since there are **six** coordinates,

`f_r(h) ≡ sum_i (r_i+h) ≡ sum_i r_i (mod 2)`

for *every* integer `h`. Thus the parity gate is independent of depth. If `M-sum_i r_i` is odd, no such length-`M` word exists at all. Otherwise the admissible depths are precisely

`I_{r,M}={h in Z: f_r(h)<=M}`,

a finite contiguous integer interval (possibly empty), because `f_r` is convex, integer-valued and tends to infinity at both ends.

For sorted observer coordinates `r_(1)<=...<=r_(6)`, the exact minimum over depth is

`f_min(r)=r_(4)+r_(5)+r_(6)-r_(1)-r_(2)-r_(3)`,

attained by every integer `h` in `[-r_(4),-r_(3)]`. Hence the interval is nonempty exactly when the parity gate holds and `M>=f_min(r)`.

**Theorem 3 (sharp fixed-horizon information capacity).** Suppose `I_{r,M}` is nonempty, with `L=|I_{r,M}|`, and `g` is a fixed mixed-sign signed permutation. Knowing the pair `(r,M)` and an auxiliary side channel, one can predict `can6(gz)` for *every* unrestricted length-`M` word precisely if the side channel can distinguish all `L` admissible depths. The optimal number of additional labels is therefore `L`, and a fixed-length binary coding requires exactly `ceil(log2 L)` bits (zero bits if `L=1`). 

**Proof.** Every admissible `h` occurs as an endpoint of such a word, by the preceding parity/shortest-path construction. For mixed-sign `g`, Theorem 2 shows that their transformed relative observations are pairwise distinct, yielding the `L)-label lower bound. The interval endpoints can be computed exactly from `r,M`; encoding the position of `h` in the interval gives the matching upper bound. QED.

Example: `r=(0,0,0,0,0,0)`. With even `M`, `f_r(h)=6|h|`, and the exact number of admissible depths is `L=2 floor(M/6)+1`; with odd `M` there are none. At `M=6`, the depths are `-1,0,1` (three labels, two bits); at `M=12`, they are `-2,-1,0,1,2` (five labels, three bits). A fixed time/step horizon can thus compress the required common-depth residual to a finite sharp code, while no uniformly finite code suffices over unbounded horizons.

Supplementary exact checks: for all `3367` min-zero vectors in `{0,1,2,3}^6` and all `M=0,...,21` (74074 cases), the sorted-coordinate minimum, parity gate and contiguous feasible-depth interval agreed with direct integer evaluation. The algebraic argument, not this check, proves Theorem 3.

## 4. Concrete C6 witness and two possible uses

The candidate `R_123` sends `e_1->e_2, e_2->e_3, e_3->-e_1` and fixes the other three axes. Its sign vector is `(-1,+1,+1,+1,+1,+1)`, so it does not descend. For native states `z_0=(0,0,0,0,0,0)` and `z_1=D`, both have the same initial relative observer `q(z_0)=q(z_1)=0`, but

`q(R_123 z_0)=0`,  
`q(R_123 z_1)=(0,2,2,2,2,2)`.

This witness establishes an actual failure of observer-fiber constancy for the candidate rotation.

Positive uses within the declared model:
1. An **exact lossless observer bridge** for all native signed-permutation candidate rotations is `(r,h)`; the common depth already belongs to the frozen six-axis spatial composite and introduces no seventh spatial axis.
2. A **two-time/readout reconstruction** is available: for any one mixed-sign rotation, knowing consecutive relative observations plus the named native operator recovers the previously hidden depth by the formula above. This may be useful when a future heartbeat/time transition supplies those two typed observations, but does not by itself assert a valid heartbeat evolution law.

Theorem 1 and 2 are *quotient/fiber certificates*. They do not imply that an arbitrary signed permutation is an admissible physical rotation or transforms complete decorated packets; those remain separate parent-task questions.

## 5. Checks, source binding and next discriminating work

The proofs are general exact algebra for signed permutations of the frozen six axes. Supplementary exact integer checks:
- All `6! · 2^6 = 46080` signed permutations were enumerated; exactly `1440` preserve the equivalence of `0` and `D`, matching Theorem 1 and proving the necessary condition completely on this finite group.
- Tested `5000` random integral states / signed-permutation configurations with exact arithmetic: every transformed min-zero readout matched the `(r,h)` formula; every mixed-sign case reconstructed `h` exactly from the two readouts. These random checks are not the general proof.

Pinned scientific sources:
- `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` (Cell torsor, `Delta`, observer, prior authorship).
- `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md` (existing local carrier and path provenance, original researcher `EM-FREE-7D3C9A`).
- `research_notes/driver/2026-11-12_x6_signed_triad_c6_group_and_brc_path_fiber_action.md` (preceding candidate group proof and BRC fiber action; same Driver/shared-context contribution).
- Current `p000_reality_foundation.json`, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json` (type and information-loss constraints).

Next: test a *typed decorated* map `(Cell, depth, path phase/history, time and triadic state)` for actual chosen native rotation transitions, retaining the relevant residuals. Separately test whether any selected observer/time transition supplies the two time-indexed quotient readouts with trustworthy operator registration. Do not infer Native Result acceptance, CLAIM, full mother-objective closure, or a physical time law from this scoped algebra.
