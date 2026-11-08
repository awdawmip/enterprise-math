# PREFIX577-R6 — exact all-depth joint law symmetry for the native BRC gate and axes 5/6

Date: 2026-11-08 UTC. Status: TASK_RESEARCH author-side exact result; UNREVIEWED / NOT_ADMITTED.
Frozen science pin: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Immutable original native kernel: `PREFIX565_positive_marginal_certificate.py`, Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41` (read directly by GitHub blob ID this turn).
Author continuation: prior order-eight scalar moment result in `research_notes/portable_direct/2026-11-08_prefix577_r6_orthogonal_gate_fourth_cumulant_author_portable.md`, blob `85c81c0c224818848122636ea0f3fa81e40d0eff`. This note strengthens that earlier author result.

## Exact theorem

On the frozen 96-port native zero-root X6-BRC chain (six equiprobable labeled actions per port), initialize the native port uniformly among all 96. Let K_n be the accumulated gate count and R_{5,n}, R_{6,n} the corresponding native-axis rewards after n labeled steps. For **every** integer n≥0 and every pair of nonnegative integers a,b,

`P(K_n=a, R_{5,n}=b) = P(K_n=a, R_{6,n}=b).`

Equivalently, the full two-variable probability generating polynomials satisfy, coefficientwise,

`E[x^(K_n) y^(R_{5,n})] = E[x^(K_n) y^(R_{6,n})]`.

Hence all finite-length joint mixed moments, mixed cumulants and scalar readouts of these two bivariate observations agree, at every finite n and all orders. This subsumes the previously checked order-eight scalar equality for K+R5/K+R6 without re-claiming that earlier work.

## Finite exact proof via Cayley–Hamilton over Z[x,y]

For i=5,6 define the 96×96 matrix over the commutative polynomial ring Z[x,y]:

`A_i(x,y)[u,v] = Σ_{e:u→v} x^(k(e)) y^(r_i(e))`,

where **each** of the six original labeled actions is counted separately and native gate/axis edge increments are used unchanged. Let `1` be the 96-component ones vector and

`P_n^(i)(x,y) = 1ᵀ A_i(x,y)^n 1`.

Coefficient (a,b) of this polynomial counts all 96-start labeled length-n paths with gate count a and R_i count b. Dividing by exactly 96·6^n gives the stationary-start bivariate probability distribution.

Put `U(x,y)=A_5(x,y) ⊕ A_6(x,y)`. This is a 192×192 matrix over Z[x,y]. The scalar polynomial difference `D_n=P_n^(5)-P_n^(6)` is a fixed linear readout of `U^n`. Because Z[x,y] is commutative, Cayley–Hamilton applies: with `χ_U(t)=t^192+c_191(x,y)t^191+…+c_0(x,y)`,

`D_(n+192) = - Σ_(j=0)^191 c_j(x,y) D_(n+j)`.

Thus exact coefficientwise equality of `D_n=0` for the **192 lengths n=0,…,191** proves `D_n=0` for all n≥0. The recurrence is a formal polynomial identity, with no floating-point or extrapolation error.

An arbitrary-precision GMP C++ program enumerated the full joint path-count coefficient dictionaries separately for i=5 and i=6 at **every n=0,…,191** and found exact equality of every coefficient. At n=191, both polynomial supports contain **3,049** (gate count, axis count) pairs; the total coefficient mass exactly equals `96*6^191`, a 151-digit integer. The final run explicitly returned `PASS_ALL_192_BIVARIATE_POLYNOMIALS; CH_DIM_192; EXACT_Zxy`.

A separate Python implementation re-derived the native edges and checked every bivariate coefficient at all depths n=0,…,64, in exact integer arithmetic. Its regression JSON SHA-256 is `c0cb43fe1feef3334ddc84665e8bb6d83aa272bb065c89e00060102acdcb222d`. The original kernel's `STARS, PHASES, NEXT, ACTIONS, TARGET, sg, edge` definitions were compared against the present frozen model, preserving the gate and 576 labeled edges.

## Explicit scope witness

The uniform-start condition is substantive. At **fixed source native port 16**, phase `(0,1,-6)` and bit 0, every one of the six possible single actions has `(K,R5)=(0,0)` but `(K,R6)=(0,1)`. The full joint equality is an ensemble equality, not an assertion of pointwise equality at each start.

## Reproducible evidence and continuation

Conversation-local reproducible bundle: `PREFIX577_R6_GATE_PAIR_FULL_JOINT_LAW_PORTABLE_20261108.zip`, 27,049 bytes, SHA-256 `b6b54546e8b82d00a359ae4999007bb851aec868eb8b37975e025b5f980dd900`, containing:

- the complete expanded mathematical theorem and proof (`PREFIX577_R6_GATE_PAIR_FULL_JOINT_LAW_THEOREM_20261108.md`);
- exact GMP C++ polynomial checker (`exact_joint_gate_pair_all_distribution_gmp.cpp`, SHA-256 `fe93d1ceb78426153b5bab15de541bbe6124351c1943fc097d0c393747647f5a`);
- the 576 labeled frozen edges (`native_edge_snapshot.csv`, SHA-256 `c2691e652d07d9a819b3cb3d1f79eb1797f3ee1aa8a4b4906dcd83b48353d138`);
- exact program output, independent Python checker/JSON, prior pinned native derivation and scalar polynomial crosscheck.

The bundle is a **conversation-local** portable artifact; its digest does not assert Source publication. This GitHub document is neutral author-side persistence, not native session/CLAIM/run/checkpoint, mathematical admission, independent review or Result.

The Source `em_status` read in this turn still returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE` with `operation_sent=false`. Current Source owner/session/recovery remains to be authenticated; no mutation or new dispatch was attempted. Original UR V2 debt is separate: locate the exact 94,687-byte four-file object with SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`, then add only lawful writer/provenance/checkpoint. Do not re-prove UR or substitute four older files for the original bundle. On current-input seed, perform complete input readback and preserve predecessor `completed_units=[]`.

**Next scientific question:** extend this common 37-state weighted quotient to additional native joint observers, with current owner/dedup checks before Source-bound work. **Next control action:** reconcile the original request and exact Source continuation after authentic backend recovery before any owner mutation. Prior identifiers are provenance, not permissions.

## Stronger constructive proof: common 37-state exact weighted quotient

The 192-depth polynomial/Cayley–Hamilton verification above has an additional, much smaller, independent structural explanation. Construct the **disjoint tagged union** of the two 96-state native weighted automata, one with labeled-edge weights `x^gate y^R5` and the other `x^gate y^R6`. Refine the initial one-class partition by the exact multiset of triples `(gate_increment,axis_increment,destination_class)`, counting parallel labeled edges, and retain the previous class ID on each refinement to enforce monotonic splitting. The class counts evolve as:

`1 → 3 → 8 → 21 → 33 → 37 → 37 (stable)`.

This produces a **common 37-class row-equitable partition** of the 192 tagged states. For any two states in one class, the multiset of their six labeled successors, grouped by the increment pair and destination class, is exactly equal. The quotient therefore defines **one 37×37 transfer matrix B(x,y) over Z[x,y]** shared by both original automata. Independently, the exact certificate verifies that **every quotient class has the same number m_C of original ports on the axis-5 side and axis-6 side** (the sums are 96 per side).

Let q_C(n;x,y) be the generating polynomial of paths of length n from any state in C. Because the partition is row-equitable, q_C(0)=1 and q_C(n+1)=Σ_D B_CD(x,y) q_D(n). Consequently the stationary pooled polynomials satisfy

`P_n^(5)(x,y)=Σ_C m_C q_C(n;x,y)=P_n^(6)(x,y)`

for **all n≥0 by direct induction**. This is a constructive all-depth joint-law proof that needs no 192-length check; the earlier polynomial certificate is a separate exact regression.

The full exact 37-class and 109 distinct weighted-quotient-entry certificate is `weighted_bisimulation_37_certificate.json`, SHA-256 `1015c0cb22658a376b341f3554bc4b903e8f8990326c3384e986ab1ab821b299`; stdlib-only construction is `gate_pair_weighted_bisimulation_37.py`, SHA-256 `56365f573c342869a558fa29a021cc112d24283cdfda4483487549675e378c6f`. Both are in the updated **15-file** conversation-local portable bundle (SHA-256 `b6b54546e8b82d00a359ae4999007bb851aec868eb8b37975e025b5f980dd900`). The expanded local theorem includes the full exact proof and explicit fixed-port counterexample. This author-side evidence is still unreviewed/not admitted; Source claim/session/writer status is separately gated.

## Strongest exact result: full trivariate gate/axis5/axis6 exchangeability

A further exact structural extension proves, for the **same frozen 96-port, six-action zero-root model** with **uniform initial native port**, the complete three-variable identity

`E[x^(K_n) y^(R5_n) z^(R6_n)] = E[x^(K_n) y^(R6_n) z^(R5_n)]`

for **every integer n ≥ 0**, as an identity in Q[x,y,z]. Thus for every n,k,a,b≥0,

`P(K_n=k,R5_n=a,R6_n=b)=P(K_n=k,R5_n=b,R6_n=a)`.

The full trivariate joint law is invariant under swapping axes five and six while keeping the gate observation fixed. This strictly strengthens the preceding all-depth bivariate theorem and all earlier finite-order gate-pair moment equalities.

**Exact constructive proof:** Take the disjoint union of two 96-state native transfer automata, weighted by `x^k y^r5 z^r6` and `x^k y^r6 z^r5` on corresponding labeled native actions. Refine by the full exact monomial-labeled successor multisets `(k,r5_or_swapped,r6_or_swapped,target_class,multiplicity)`, retaining old class ID to make splitting monotone. The partition sizes are `1→4→13→21→33→37→37` and stabilize at **37 weighted row-equitable classes**.

Each class has identical full labeled action-count/target-class signature for every member and occurs **the same number of times in both 96-state halves**. It therefore induces one common 37×37 polynomial transition matrix over Z[x,y,z] and one identical starting class weight vector. The all-one terminal vector is common. Exact induction on path length gives equality of the two weighted path-generating polynomials for all n≥0. The final quotient has **109 distinct weighted transition entries**.

A stdlib-only verifier recomputes all class memberships, edge-label multiplicities, equal class frequencies and stability; complete certificate `trivariate_swap_37_certificate.json` SHA-256 `7cd96d8b837aac3b397afa51a654d9bc825a675be185f319c0c6dc557bde715e`. An independent direct exact integer polynomial regression verifies coefficientwise swap symmetry for **every n=0,…,40**, checking total mass `96·6^n`; regression certificate SHA-256 `1eb7d03aa9d02101f86c4a56e4aaa376f37f3c35637a4d6cd264c3a979a9f141`. These source/code/certificate files and the expanded complete proof are contained in the updated **15-file** conversation-local ZIP (27,049 bytes), SHA-256 `b6b54546e8b82d00a359ae4999007bb851aec868eb8b37975e025b5f980dd900`.

The condition of a uniform initial native port is material: at fixed port 16 already at length one, R5=0 and R6=1 for all six labeled actions (and K=0). This is exact author proof evidence under the pinned kernel, not canonical Source admission or a live owner checkpoint.

**Next differentiating frontier:** classify whether the same weighted-quotient mechanism extends to additional pairs or subgroups of all six native axes, while keeping the gate; first consume the current authenticated Source continuation/owner to avoid duplicate research. UR V2 original-bundle provenance debt and native Source authorization recovery are unchanged.
