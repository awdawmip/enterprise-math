# PREFIX577-R6 — Full six-axis + gate symmetry is exactly C2; exact observer rank 49

**Date:** 2026-11-08 UTC. **Status:** AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. This is neutral author-side research evidence, not Source Result, CLAIM, checkpoint, Driver review, or mathematical admission.

**Frozen scientific source:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`; exact native `PREFIX565_positive_marginal_certificate.py` original Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`, read again this turn. Prior author trivariate `(K,R5,R6)` theorem: `research_notes/portable_direct/2026-11-08_prefix577_r6_gate_pair_joint_law_all_depth_author_portable.md` (blob `ed2ce868d5e39ef96f85cb327acaf1b51190b2e5`); that predecessor science is reused, not counted again.

## Theorem 1: complete coordinate-permutation symmetry group of the full seven-variable law

In the frozen **zero-root** native four-STAR model, 48 phases, 96 ports, six labeled equiprobable actions per port, uniformly random initial port, let `R_i(n)` count reward on each of the six native axes and `K(n)` the gate count. Define

`F_n(x1,...,x6;y) = E[y^K(n) product_i x_i^R_i(n)]`.

The subgroup of `S6` permuting the six reward coordinates (keeping gate fixed) which preserves `F_n` for **every n>=0** is **exactly {id,(5 6)} ≅ C2**. In particular, swapping R5 and R6 preserves the *complete joint distribution conditional on the first four axes and gate*, for every finite path length. The claim is a precise model-internal polynomial identity, not an arbitrary-root or arbitrary-start result.

### Exact exclusion of all 718 other permutations

For one labeled step, the 576 full-port path counts with `K=0` are: axis1=93; each of axes2..6=96. The remaining three paths have `K=1` and reward axis1. Hence any law-preserving permutation fixes axis1 (only 120 candidates remain).

At two steps, the exact full seven-variable `K=1` counts are: pair(1,3)=18, pair(1,4)=pair(1,5)=pair(1,6)=6, and no pair containing axis2. With axis1 fixed, axes2 and3 are therefore fixed. At `n=2,K=0`, pair(3,4) has count 0 while pair(3,5) and pair(3,6) have count 288 each. So axis4 is fixed, leaving only the optional swap of axes5 and6. All coefficients here count six-action paths from all 96 ports, and the probability normalization is `96*6^n`. Explicit exact integer enumeration of all 720 permutations gave **600** failures already at n=1, another **118** at n=2, and the two stated survivors; a concrete unequal-coefficient witness was saved for each rejected permutation.

### All-n constructive proof of (5 6)

Form the tagged union of a 96-state automaton carrying each original edge monomial `y^gate prod_i x_i^ri` and a second 96-state copy carrying the same edges but with reward axes5,6 exchanged. Preserve every native port, all six labeled actions, parallel multiplicities, gate, and the first four reward coordinates.

Refine the 192 tagged states by their exact integer multiset of `(all-six-reward+gate increment, previous destination color)`. From the one-class partition, the class counts are **1→7→36→47→51→51**; the final **51 classes** are stable. Every class has the same labeled six-action outgoing multiset to the final classes for every member, and occurs with **equal cardinality in both tagged halves**. The common row-equitable transfer has **165 distinct nonzero labeled transition terms** over `Z[x1,...,x6,y]`.

Write `q_C(0)=1`, `q_C(n+1)=sum_D B_CD q_D(n)`. All native ports in the same class have the identical exact path generating polynomial `q_C(n)` by induction. Equal class multiplicities on both sides yield `F_n(x1,...,x6;y)=F_n(x1,...,x4,x6,x5;y)` for **every integer n>=0**. This all-n proof uses row-equitable transfer, not extrapolation from finite tests.

## Theorem 2: the 51 quotient-class response polynomials have exact rank 49 over Q

Class numbers refer solely to the certificate's deterministic sorted-signature numbering. Exact all-n polynomial identities are

`q_40 - q_41 - q_46 + q_48 = 0`, and
`q_40 - q_42 - q_46 + q_50 = 0`.

Let `v_0=e40-e41-e46+e48`, `v_1=e40-e42-e46+e50`. For each of the **seven** possible native monomial action labels `w`, exact integer checks on the 51-state quotient give `v_0^T B_w=v_1^T B_w=0` entrywise, and `v_0^T 1=v_1^T 1=0`. Hence the two independent full-length response relations hold for all n, giving rank≤49.

Across path depths `n=0,...,5`, the 51 class response vectors generate 250 distinct `(n,monomial)` observation columns. Delete rows 48,50 and select 49 of those columns: the **49×49 integer minor has determinant 931620375 modulo the prime 1000000007**, so rank≥49 over Q. Thus rank **equals 49**, with precisely the two displayed all-horizon relations. This is *linear response rank*, not an asserted minimal positive stochastic automaton.

For any rational (or real) initial port distribution μ, define `D_C(μ)=sum_{u:normal_class(u)=C}μ_u - sum_{u:swapped_class(u)=C}μ_u`. The complete seven-variable path law is (5 6) invariant for **all n** if and only if `D(μ) in span(v_0,v_1)`. Necessity comes from the exact rank-49 finite-horizon minor and sufficiency from the all-n annihilator identities.

**Nonuniform constructive example:** `μ(16)=μ(40)=1/2`, zero elsewhere; exact class pairing is normal(16)=1, swapped(16)=9, normal(40)=9, swapped(40)=1. Then D=0 and the complete joint law is (5 6) symmetric for every horizon. A *single* port16 is not symmetric (known n=1 witness).

## Reproducibility and provenance

The standalone portable research package prepared this turn contains the original frozen-edge implementation imported from the preceding verified author bundle, prior 576-row edge snapshot, two standard-library Python proof/certificate generators, their generated JSON certificates, complete mathematical explanation and continuation. The package was independently re-extracted and both generators re-executed with byte-identical certificates.

- Full axis/gate C2 certificate (includes every rejected permutation's witness and complete 51-state quotient), SHA-256 `4f5fdfce3958306bc08336443a966f59cec5cd1a17f15b68004eebc146682e47`.
- Rank49 certificate (exact transition annihilators, selected minor indices/determinant and two-port example), SHA-256 `fd65919d655e88c15d7c78ea50a4f55b2b39ab99499c361547ad430fcaeb8098`.
- Local portable ZIP (eight files), SHA-256 `c4432671aef91e0c06cec011eb7e15ddf94c04b7a29a1f503b2042ddbbf98810`, **not claimed to be GitHub-published or Source-uploaded**.

**Research identity/authority:** Existing historical local researcher designation `EM-DIRECT-3EE30C` is not an authenticated Source session. Current read-only Gateway `em_status` fails with `BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE` and `operation_sent=false`. Sites local status `CONFIGURED_NOT_LIVE_VERIFIED`, `backend_connected=false`, `research_authority_granted=false`. No Source session/claim/open/checkpoint/Result/review has been created, resumed or reclassified through this author note.

**Separate UR V2 obligation:** the actual original 4-file bundle must have 94687 bytes and SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`. Original bytes not recovered in this turn. Four historical authenticated predecessor evidence files and D24 RR/DR remain separate and retain their provenance. No UR mathematical proof was repeated or surrogate bundle published.

**Next:** Recover *own* native recovery_status and outstanding request receipts when the approved backend becomes usable; exact continuation/claim authority precedes any formal write. For `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`, fully read back current task inputs and use predecessor `completed_units=[]`. Scientific extension: characterize minimal-support nonuniform initial laws using the rank49 class criterion or test different frozen roots with separate source/observer pins. Do not duplicate other owners' research, claim independent review or edit the task scheduler.
