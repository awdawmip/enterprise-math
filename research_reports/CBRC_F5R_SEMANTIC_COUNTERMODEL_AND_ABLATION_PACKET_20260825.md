# CBRC F5R — Semantic Countermodel and Ablation Packet

Status: `FINAL_FROZEN`
Researcher-ID: `EM-CBRC-F5R-8120F1`

## 1. Semantic models

All models are bookkeeping models for the exact F5R implication question. They do not propose a canonical carrier.

Let the toy carrier be

`C = Z × (Z/2)`

with additive law `(n,t)+(m,s)=(n+m,t+s mod 2)`, embedded old generator `e=(1,0)`, and forgetful map

`pi(n,t)=n e`.

The second coordinate is only a finite kernel tag used to witness exact independence. It is not interpreted as phase, norm, inner product, or any downstream structure.

### Model S-A witness — candidate true under added branch-to-witness semantics

Use the reversible conserving map on two marked slots whose old-coordinate block is

`A = [[2,1],[-1,0]]`.

Keep kernel tags unchanged. `det(A)=1`, and the inverse old-coordinate block is integral.

On `(e,0)` the outputs have old projections

`(2e,-e)`.

Thus both marked outputs are nonzero after forgetting. If each marked output is additionally required to refine concrete old Path-formal support carrying a nonzero old coefficient, the candidate is derived.

### Model S-B witness — candidate false with exact reversible kernel branch

Define

`M_B((n,t),(m,s))=((n,t),(m,s+n mod 2))`.

`M_B` is its own inverse. On `((1,0),(0,0))` it returns

`x=(1,0)`, `y=(0,1)`.

Properties:

- `x != 0`, `y != 0` in `C`;
- `pi(x)=e`, `pi(y)=0`;
- exact retraction `pi(e)=e`;
- total old signed coefficient preserved;
- total old Boolean support preserved;
- reversible before marker erasure;
- marker slots remain distinguishable;
- no old support is resurrected by the kernel-only branch;
- Path-formal provenance may remain attached to the genuinely old-supported branch.

This is the minimal exact independence witness against per-branch nondegeneracy.

### Model S-C witness — total-only recovery

Use the same `M_B`, but impose only

`pi(x)+pi(y)=e`.

The condition holds, yet `pi(y)=0`. Hence total recovery is strictly weaker than per-branch recovery.

## 2. Minimal `(1,1)` Path-formal fiber audit

The allowed native sources give two distinct concrete words:

- `X_i X_j`;
- `X_j X_i`.

They have one common typed terminal and the same component trace `(1,1)`.

Therefore:

- Path-formal basis-witness count = `2`;
- natural-number augmentation = `2`;
- Boolean terminal support = `1`.

This exact witness fiber does not canonically identify either later marked coefficient slot with one of those concrete words. Making that identification for every retained marked branch is an extra semantic rule.

## 3. Implication witnesses

The S-B witness simultaneously falsifies each proposed implication below while keeping the listed premise true:

1. `retraction => per-branch nonzero` — false because `pi(0,1)=0`;
2. `reversibility => per-branch nonzero` — false because `M_B` is an involution;
3. `total old coefficient preservation => per-branch nonzero` — false because projections are `(e,0)`;
4. `old Boolean support preservation => per-branch nonzero` — false because total old support remains present through `x`;
5. `no-resurrection => per-branch nonzero` — false because the zero-projection branch resurrects no old support;
6. `marker identity => per-branch nonzero` — false because slot identity and old projection are independent notions;
7. `typed locality => per-branch nonzero` — false because both slots may be assigned the same allowed local type while one occupies kernel state.

Path-formal provenance retention also fails to imply the candidate unless strengthened so that every marked branch is itself required to refine at least one concrete Path-formal witness with nonzero old coefficient.

## 4. Strongest conserving substitute

Under the separately imposed total old-coordinate conservation equation

`pi(x)+pi(y)=e`,

a proof by contradiction gives

`pi(x) != 0 or pi(y) != 0`.

Maximality witnesses:

- S-B shows `both nonzero` is not forced;
- S-A shows `exactly one nonzero` is not forced.

Thus the exact strongest two-branch nonzero-count statement under conservation is `at least one`.

Without total old-coordinate preservation, the allowed source abstraction gives no nontrivial projection statement beyond the codomain typing of `pi`.

## 5. Mandatory ablations

| Ablated item | Status of candidate | Exact effect |
|---|---|---|
| branch-to-concrete-witness correspondence | `INDEPENDENT` | This is the only tested strengthening that can turn S-A into a derivation; deleting it admits S-B directly |
| conservative retraction `pi` | `MEANINGLESS` | the predicate `pi(x)!=0 and pi(y)!=0` is not defined |
| no-resurrection | `UNCHANGED_INDEPENDENT` | S-B already satisfies no-resurrection, so removing it cannot rescue derivability |
| reversibility | `UNCHANGED_INDEPENDENT` | S-B is reversible already; removing reversibility only enlarges the model class |
| total old-coefficient preservation | `UNCHANGED_INDEPENDENT`, weaker substitute lost | candidate was already independent; the derived `at least one` result is no longer available |
| old Boolean support preservation | `UNCHANGED_INDEPENDENT` | S-B already preserves old support; removal does not alter the counterexample |
| marker identity/provenance retention | `UNCHANGED_INDEPENDENT / INTERPRETATION_WEAKER` | the slotwise formula remains evaluable, but its interpretation as retained branch survival becomes less semantically anchored |

## 6. Deterministic model evidence

Pushed checker:

`scripts/cbrc_f5r_validate_forgetful_branch_semantics.py`

Remote/executed Git blob SHA:

`b83995d4d1bf00db3d078fcb349ef5ed5223f8a4`.

Result:

- `PASS`;
- mismatch count `0`;
- deterministic digest `14201c39734a17782aa7dabb48a22c0e97fc72a002f6f78578cf3645869d9a97`;
- `(1,1)` Path-formal count `2`, N-augmentation `2`, Boolean terminal support `1`;
- S-A projection pair `(2,-1)`, candidate true;
- S-B projection pair `(1,0)`, candidate false;
- S-C total-only recovery true with candidate false;
- all seven mandatory ablations covered.

## 7. Rank-boundary consequence

The S-B witness has exactly the projection pattern tolerated by the accepted F4 torsion loophole: one old-supported output and one projection-zero nonzero enriched output.

Therefore the weaker `at least one nonzero` theorem does not eliminate the rank-one loophole. A rank lift follows only after adding the stronger per-branch nondegeneracy rule, and is therefore `CONDITIONAL_ON_NEW_AXIOM`.

## 8. Final classification

Primary verdict:

`F5R_NEW_AXIOM_REQUIRED`.

Secondary exact statement:

`TOTAL_OLD_COORDINATE_CONSERVATION => AT_LEAST_ONE_MARKED_BRANCH_HAS_NONZERO_OLD_PROJECTION`,

but this weaker statement does not kill the accepted F4 torsion loophole.
