# X6 radix heartbeat: six-axis scale dynamics with exact residuals

Researcher-ID: `EM-DIRECT-AD0416`
Research-Activity-ID: `RA-37C0A30C7B1F5A338F03D186`
Progress-Event-ID: `brc-x6-radix-heartbeat-20260919-AD0416`
Session: `chat-local-reciprocal-ceec8bd1559acdf8c10ebc9b` (existing local key, not a platform ID).
Status: `RESEARCH_CONSTRUCTION / SCOPED_DERIVATIONS / EXECUTED_CHECKS / NOT_FOUNDATION`.
User question: “如果是立体六轴场呢，把时间作为缩放心跳”.
Read pins: GLOBAL_KNOWLEDGE `1373e725ef7ffeea666ef2da46aad5bba270c6b2`; Enterprise Math `a6ef14fdc1dec284f9ca40875ae3acfb85e1b4b7`.
No formal Task-ID/CLAIM, independent review, Foundation/worldview edit, physical time calibration, or Nollm production change.

## 1. Model and nonclaims

Use the accepted raw relative Cell chart Z^6, signed primitive directions +/-e_i, and the S6 positive-axis permutation skeleton from `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`. Six native axes are not three Euclidean axes counted twice. Internal signed coordinates are not final nonnegative Cell addresses. The chosen chart anchor is not an ontic center. Cyclic permutation here is an admitted finite coordinate skeleton, not a classification of all native rotations or a physical rotation-angle law.

Time t is an ordered discrete update index. A scale program and phase p(t) are derived controls, not a seventh spatial coordinate. When the program repeats, scale alone does not recover t or direction of travel. A scalar redraw that scales all geometry and all query radii equally changes no scale-invariant incidence; actual coarse/fine operations or interactions must be declared. No instantaneous global movement of all stored Cells or constant work per full field is implied.

## 2. Six staggered integer beats instead of fractional Cell moves

For integer b>=2 define the injective index-b lattice map

A_b(z1,z2,z3,z4,z5,z6)=(b*z6,z1,z2,z3,z4,z5).

It has determinant -b and A_b^6=b I. Every coordinate is multiplied by b exactly once during six beats. For 1<=j<=5, (A_b^j)^T A_b^j has j diagonal entries b^2 and 6-j entries 1; the intermediate component-metric anisotropy is bounded by b. This uses the accepted component quadratic readout, not a new native angle convention.

Proof: apply the cyclic shift six times; each input component crosses the single b multiplier once. The same tracking proves the intermediate Gram formula. For b=2, each microbeat has lattice index2, and a sixbeat block has index64 and scalar length multiplier2. A simultaneous 2I update instead has index64 immediately. Neither this work nor elapsed wall time automatically becomes cheaper; staggering distributes the branching and arithmetic over time.

The effective index-based length multiplier per microbeat is b^(1/6), but an individual beat is NOT a conformal fractional dilation. b=2 is an exact diagnostic choice, not a new mandatory Nollm scale or a measured natural constant. The construction generalizes to d axes with A_b^d=b I; six is supplied by the declared native space, not selected by this identity.

## 3. Exact contraction and reconstruction

For any integer point z, let (q,r)=divmod(z1,b). Define

C_b(z)=(z2,z3,z4,z5,z6,q), residue r in {0,...,b-1}.

Then z=A_b C_b(z)+r e1. This works for negative coordinates with Euclidean residues. The lifted contraction z -> (C_b(z),r) is a bijection Z^6 -> Z^6 x {0,...,b-1}; contraction without r is b-to-1.

After six contractions, the coarse coordinate is componentwise floor(z/b), and the chronological six residues are exactly z_i mod b, i=1..6. Reverse the stored residue list during synthesis. At b=2 a coarse address has64 fine antecedents; one address plus six bits distinguishes them. After k complete coarse blocks, exact arbitrary recovery requires b^(6k) residue possibilities, or ceil(6k log2 b) worst-case bits. This is coordinate precision information, not a seventh axis, a fixed-memory theorem, or a semantic index. A common global clock phase cannot encode independently varying residues of every point.

Example: z=(17,-3,0,4,5,6) gives q=(8,-2,0,2,2,3), r=(1,1,0,0,1,0); z=2q+r exactly.

## 4. Pure pulse, interaction, and time phase

A sixbeat outward A_b program followed by the inverse program on its image returns every point. More generally, analyze six times preserving residues, then synthesize without changing anything: the endpoint map is identity. This creates no new stored information or useful memory by itself. Time still advances and path-formal traces can differ.

A nontrivial heartbeat has the declared form Synthesis o U o Analysis, with U an actual input, local interaction or residue-preserving update. For example U(q,r)=(q+e1,r) produces z -> z+b e1; at b=2 the example above returns (19,-3,0,4,5,6). The coarse operation is geometrically local in the coarse chart; lifting it spans b fine steps. This is not instantaneous physical transport or a semantic relevance claim.

Phase is needed even before adding inputs. Let x0=e6, x_j=A_2^j e6 for j=0..6, then retrace to x0 in six inward beats. Twelve temporal states have seven distinct current positions. Position 2e1 occurs once going outward and once inward; the next positions are 2e2 and e6 respectively. The unchanged T6 predictive compiler returns block counts (7,12,12,12) for horizons0..3. Thus position-only coalescence is not future-safe on this finite pulse. t or its relevant phase must survive; scale magnitude alone is insufficient. Full cycle count is needed only if the observer includes absolute age/nonperiodic inputs. Existing resource budgets remain separate and do not automatically reset with a pulse.

## 5. Actual BRC composition

When a coarse point is given WITHOUT its residue, the refinement relation has b alternatives:

E_b(q)={A_b q+r e1: r=0,...,b-1}.

If the task declares equal normalized positive weights, use BRC atoms [1/b,A_b,r e1]. This is real coarse-to-fine ambiguity, not invented branching on the deterministic residue-retaining inverse. For six b=2 refinements, the original EffectHistogram computes64 paths,64 distinct points 2q+u with u in {0,1}^6, each weight1/64 and total mass1. With per-branch weight1 the count/mass is64 instead; normalization must be declared. Possible fine candidates are not64 newly asserted memories. Full memory identity/payload is not reconstructed by a coordinate histogram.

REUSE_EXECUTED: complete current `src/enterprise_math/brc_transport.py`, `brc_histogram.py` and `predictive_quotient.py` were reused byte-identically from the prior supplied bundle and checked against current Git blob SHAs. T5 mixed-radix helper `euclidean_digits` is used for the exact division. T0/T5/T6/S6 source laws are composed; no new top-level tool family or automatic tool admission.

## 6. The first genuine new compression boundary

Expansion packets above have fixed affine effects, so the existing28-entry degree-two X6 moment lease applies. Integer contraction is residue-dependent; the same unconditional closure does not follow.

Embed two unit-mass measures along e1:
mu=(delta_-e1+delta_e1)/2;
nu=delta_-2e1/8+3 delta_0/4+delta_2e1/8.

Their complete degree<=2 spatial moments agree. One C_2 step sends the e1 component to the final axis after floor division. The last-coordinate means become -1/2 and0, and second moments1/2 and1/4. Thus equal28-entry input summaries have distinguishable next moments.

An exact ONE-STEP repair is to retain residue-conditioned matrices
M_r=sum_{z1 mod b=r} mu(z) [z;1][z;1]^T.

Within residue r the map C_2 is the affine rational readout z -> A_2^-1(z-r e1), restricted to its integer residue domain. If H_r is its homogeneous matrix, then
M_out=sum_r H_r M_r H_r^T.

This follows by substituting the exact affine formula separately on each fiber. At b=2 it uses two symmetric7x7 matrices, i.e.56 rational entries, as a sufficient diagnostic summary; minimality is NOT claimed. Both witnesses and100 random finite measures match explicit contraction exactly. These56 entries do NOT close arbitrary later contractions: further steps can need joint residues or finer digits, and bit sizes grow. Safe closure requires a declared horizon/operation language or adaptive exact refinement. Signed centered moments are algebraic observations, not signed positive branch mass.

## 7. Execution and publication scope

`verify_heartbeat.py` runs10 check groups:3 complete source blob identities; sixbeat closure for b=2,3,5,7;15625 exhaustive signed sixbeat roundtrips;1000 random signed multiscale roundtrips;64-point fiber inventory; actual BRC normalized refinement/moment agreement; actual T6 phase distinction; contraction moment counterexample and100 residue-conditioned repairs; pulse interaction/identity witness; invalid inputs and no-free-residue-loss checks (related assertions grouped in the output). All passed. General formulas rely on the proofs above, not finite enumeration.

Source SHA1s: brc_transport.py be1debe367263931bd5e93fd750be3ed54624fe1; brc_histogram.py 9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1; predictive_quotient.py f27d9ddf908f5b07051acfaf0c69f359d499b98b. The standalone bundle carries a clearly identified minimal prime-valuation dependency excerpt, not a full holonomy-module execution claim. In a project checkout use PYTHONPATH=src.

Classical comparison checked: Garcia Garcia, Hernandez-Medina and Perez-Villalon, Filter Banks on Discrete Abelian Groups, arXiv:1603.03330 (2016), discusses polyphase and perfect-reconstruction structures. No novelty claim for companion-like dilation matrices, radix analysis/synthesis or conditional moments. This work proposes their typed six-axis heartbeat/BRC application, not a proven physical mechanism or semantic memory improvement.

## 8. Next bounded experiment

Use this exact six-axis pulse as baseline, add ONE geometry-derived interaction U, and compare no pulse, lossless pulse and explicitly lossy coarse observation at equal operation budgets. Preserve identity, weights, phase and only the justified residue scope. Measure adjacency/coverage changes, retained state and failed future predictions; do not call ordinary redraw or irreversible accidental loss memory formation. Do not rewrite Nollm production geometry or replay the already verified5/7 or Bridge-budget experiments.
