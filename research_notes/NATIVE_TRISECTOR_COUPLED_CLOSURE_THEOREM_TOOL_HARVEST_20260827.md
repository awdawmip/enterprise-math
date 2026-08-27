# Native tri-sector coupled closure — theorem and tool harvest

Status: `NO_NEW_MATHEMATICS / THEOREM_ALREADY_ADMITTED / TOOL_EXTRACTION_CANDIDATE`

Date: `2026-08-27`

Source theorem:
`research_notes/NATIVE_TRISECTOR_COUPLED_CLOSURE_AUDITED_RESEARCH_THEOREM_NODE_20260826.md`

Research admission authority:
`driver_reviews/NATIVE_TRISECTOR_COUPLED_CLOSURE_CANONIZATION_DRIVER_DISPOSITION_20260826.md`

Foundation disposition:
`FOUNDATION_COMPATIBLE / NOT_FOUNDATION_GENERATIVE / NOT_FOUNDATION_ADMITTED`.

## 1. Theorem extraction

No new theorem is introduced by this harvest. The admitted theorem is decomposed into three reusable theorem-facing assertions.

### T-A — extremal centered-lane uniqueness

For odd `s>=3` in the controlled comparator family:

- lower prime extremal saturation at `q=2s-1` forces `(s,q)=(3,5)`;
- upper prime extremal saturation at `q=2s+1` forces `(s,q)=(3,7)`;
- both occur at `s=3`.

Authority: admitted research theorem; external classification `NO_DIRECT_MATCH_FOUND` for this exact centered-lane extremal statement.

### T-B — unique longitudinal/transverse closure

Assume an odd universal breaker `q_b` with

`k_*=2q_b-1`

and the audited bound

`q_b<=5`.

Then simultaneous matching

`k_*-4=2s-1`,

`k_*-2=2s+1`

uniquely gives

`(s,q_b,k_*)=(3,5,9)`.

Authority: admitted research theorem. The closure algebra is elementary after the hypotheses; the research-specific content is the coupling of the independently supplied longitudinal/transverse mechanisms.

### T-C — native specialization

The current native allocator supplies

`s=B=3`.

Therefore T-A and T-B close on the native scalar with exact typed consequences

`M_9=35`,

`3M_9=105`,

`3M_9+1=106=2*53`.

This is downstream of the current Foundation value `3`; it is not a Foundation derivation of three-ness.

## 2. Tool extraction decision

The toolbox rule is binding:

`NEW_THEOREM != NEW_TOOL`.

The current result does not justify a new global tool family such as `T13`. The extracted reusable surface is therefore one Prime-domain operator composed from already available finite-field/symmetry mechanisms.

Method-inventory classification:

`DOMAIN_OPERATOR`.

Candidate method ID:

`domain.prime.native_trisector_coupled_closure`.

Executable owner module:

`src/enterprise_math/native_trisector_coupled_closure.py`.

## 3. Public certificate API

### `split_hyperbola_orbit_certificate(B,C,q)`

Returns exact odd-prime-field data for

`B(y^2-x^2)=C`:

- `q-1` point certificate;
- independent-sign orbit partition;
- Burnside orbit-count cross-check;
- Legendre sign data;
- one-orbit flag and explicit `q<=5` capacity implication.

Boundary: support only. A one-orbit result does not invent universal-breaker semantics.

### `odd_sector_lane_certificate(s,q)`

Returns exact finite data for

`Lambda_s(a)=-sa-1/(2a)`:

- image and image-size formula;
- centered target lane residues;
- fiber sizes;
- saturation/equality flags;
- lower/upper extremal classification;
- consistency with the admitted `(3,5)/(3,7)` uniqueness theorem.

Boundary: for `s!=3` this is comparator arithmetic, not native higher-sector geometry.

### `coupled_closure_certificate(s,q_b)`

Returns:

- `k_*=2q_b-1`;
- the two transverse boundaries `2s-1,2s+1`;
- exact boundary-match flags;
- whether `q_b<=5` places the input under the admitted uniqueness theorem;
- `M_k`, `s*M_k`, local obstruction and terminal odd prime factor;
- native typed meanings when the admitted solution `(3,5,9)` is reached.

Boundary: the caller must already supply the semantic fact that `q_b` is an odd universal breaker.

### `native_trisector_coupled_certificate()`

One-call regression/readout certificate for the admitted native node. It combines:

- lower `q=5` lane saturation;
- upper `q=7` lane saturation;
- `q=5` one-sign-orbit support and `q=7` nonbreaker control;
- exact `(3,5,9)` closure;
- typed chain
  `3 -> (5,7) -> 9 -> 35 -> 105 -> 53`.

It explicitly reports:

`THEOREM_STATUS = AUDITED_RESEARCH_THEOREM / DRIVER_ADMITTED`,

`FOUNDATION_STATUS = REVIEW_COMPLETED_NOT_ADMITTED`,

and

`novelty_claim = false`.

## 4. Non-toolized proof content

The following remain theorem/proof facts and are not separately toolized:

- the second-moment proof yielding the `q|75` and `q|21` obstructions;
- the literature-search result `NO DIRECT THEOREM-STATEMENT MATCH FOUND IN THE AUDITED LITERATURE SET`;
- the Foundation dependency-direction argument;
- historical genealogy of the bouquet `105`.

These do not have a stable reusable input/output API beyond the certificate operator above.

## 5. Regression surface

New regression file:

`tests/test_native_trisector_coupled_closure.py`.

It covers:

1. exact sign-orbit counts for `q=5,7,13,53`;
2. native lower/upper lane fibers (`1:2:1` and `2:2:2` as sorted multiplicities `[1,1,2]` and `[2,2,2]`);
3. active extremal counterexample scan through odd `s<=101`, preserving only `(3,5)` and `(3,7)`;
4. admitted `(3,5,9)` closure and `35,105,53` arithmetic;
5. the out-of-hypothesis comparator `(s,q_b)=(5,7)`, which satisfies the raw boundary equations but is explicitly outside the admitted `q_b<=5` uniqueness bound;
6. input/domain guards.

## 6. Registry posture

Prime-method supplement:

`src/enterprise_math/prime_method_inventory_native_trisector_coupled_closure.json`.

General reuse addendum:

`research_method_inventory_addenda/20260827_native_trisector_coupled_closure_harvest.json`.

Current extraction posture:

`TOOLBOX_INTEGRATION_CANDIDATE / VALIDATED_WIP_ADAPTER_ONLY`.

Do not mark `CANONICAL_TOOL_READY` until Driver reviews the executable extraction as a tool surface. The mathematics itself is already admitted and is not reopened by that review.

## 7. Recommended Driver disposition

`ADMIT_DOMAIN_OPERATOR` if executable regressions and inventory/reference-integrity checks pass.

Do not create a new global T-family. The stable abstraction is the existing Prime Toolkit / domain-operator layer, with T7-style finite symmetry and classical Joukowski machinery retained as support dependencies.
