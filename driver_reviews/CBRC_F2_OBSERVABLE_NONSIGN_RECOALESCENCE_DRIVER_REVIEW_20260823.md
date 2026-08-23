# Driver Review — CBRC F2 Observable Non-Sign Recoalescence

Status: `DRIVER_ACCEPTED_WITH_SCOPE_NARROWING`
Date: `2026-08-23`
Driver-ID: `EM-DVR-CBRC-F0-7C3A21`
Reviewed task: `RS-CBRC-F2-OBSERVABLE-NONSIGN-RECOALESCENCE-FORWARD-CLASSIFICATION`
Accepted owner branch: `research/cbrc-f2-observable-nonsign-recoalescence-forward-classification`
Accepted owner head: `3d566b2801c2530f8c1bf9c18e97f10a71bc5c36`
Taskbook source: `9866e523b7e7f134497d8aca9ba2b6a093600257`
Blind input source: `155297ab859e4207634dae75566c89ca1a430000`

## 1. Driver verdict

`CBRC_F2_ACCEPTED_WITH_SCOPE_NARROWING`

Accepted primary research verdict:

`F2_F1_CARRIER_OBSERVABLE_READOUT_FAMILY`

Hard target:

`OBSERVABLE_NONSIGN_RECOALESCENCE_MINIMAL_EXTENSION_CLASSIFIED = ACCEPTED`

No Foundation promotion is authorized.

## 2. Accepted theorem-level core

Write the accepted F1 carrier as

`C1 = Z e ⊕ <tau | 3 tau = 0>`

with

`R(n,a)=(n,a+n)`, `J(n,a)=(-n,-a)`, `S(n,a)=(n,-a)`.

The F2 owner packet proves the common-action orbit classification. In particular,

- `0=(0,0)` is a singleton orbit;
- nonzero pure torsion `{(0,1),(0,2)}` is a distinct orbit;
- all six signed/transported elementary occurrences belong to one elementary orbit.

The minimal relative-recoalescence discriminator is therefore exact:

`e + J e = 0`,

while

`e + J R e = -tau != 0`.

Thus absolute non-sign labels can remain scalar-invisible on one branch while unequal relative transport can change the aggregate orbit of two same-terminal branches.

This establishes **compatibility/existence of relative observability on the accepted F1 carrier**. No carrier enlargement is required for the F2 operational conditions.

## 3. Accepted readout-family classification

Under O1–O10, scalar readouts are orbit functions. The minimal constraints are:

- zero orbit has value `0`;
- elementary orbit has normalized value `1`;
- nonzero pure-torsion orbit has some value `t>0` to satisfy relative sensitivity;
- higher orbit values remain largely free subject to nonnegativity and the declared invariances.

The packet correctly exhibits inequivalent exact witnesses, including a support-type readout and a fully orbit-separating readout. Therefore:

`F2_READOUT_EXISTS = true`

but

`F2_READOUT_UNIQUE = false`.

The nonuniqueness is theorem-relevant and must not be hidden by choosing a preferred downstream formula.

## 4. Scope narrowing — what F2 does NOT derive

F2 does **not** derive that nature uses any such readout.

O10 `NONSIGN_RELATIVE_SENSITIVITY` is an operational requirement supplied by the F2 taskbook. The owner result proves O10 is compatible with O1–O9 on `C1`; O1–O9 alone do not force O10.

Therefore F2 does not establish:

- a physical amplitude;
- a probability law;
- a norm, square law, or inner product;
- quantitative fringe/intensity interpolation;
- local branch mixing;
- a wave equation or continuum dynamics;
- that the pure-torsion orbit must receive any particular positive scalar beyond `t>0` once O10 is imposed.

In particular, the support readout witness shows how weak the present observability claim is: qualitative orbit separation already satisfies F2. This is acceptable for F2 but is a hard boundary for successor work.

## 5. Selector audit accepted

The F2 selector analysis is accepted:

- tagged/unmarked upper bound only bounds parameters;
- zero-separation and monotonicity still leave large families;
- linear finite-copy scaling is incompatible with observable order-three torsion because `3 tau=0` would force `rho(tau)=0`;
- no independently derived nontrivial local mixing exists in the F2 blind input.

This last point is the key successor trigger.

## 6. Evidence / integrity review

Accepted owner head is five commits ahead of the taskbook source and behind by zero. The diff contains only the required F2 reports, checker, and evidence manifest.

Manifest reports:

- checker mismatch count: `0`;
- deterministic checker digest: `8d3a47d9f755826dce69c8a198ef0092bfb668a630c7737a3b864b60227f92d3`;
- depth checked: `4`;
- three-alternative cases: `216`;
- target-leak audit: `PASS`.

Dedicated audit states that only the blind F2 packet was used as mathematical input before freeze. No full F1 counterfactual section, R063/R064/R065 mathematics, downstream coherent-wave work, or external quantum/wave formalism was used.

Driver accepts the target-leak boundary.

## 7. Successor routing decision

Do **not** open a stage whose goal is “derive Born/square/C4/complex amplitude.” That would be target leakage.

The load-bearing unresolved question is earlier:

> Can a native, reversible, genuinely branch-mixing split/recoalescence operation be derived/classified under typing, choice independence, information preservation, and scalar conservation; and if such mixing exists, what minimal carrier and scalar law are jointly forced?

The next stage must therefore classify a **mixing + conservation extension**, with no preselected coefficient system or readout exponent.

The F1 torsion carrier must be treated only as one accepted upstream candidate; if observable scalar conservation plus genuine mixing kills it, that is an admissible result.

## 8. Final Driver labels

`F2_RELATIVE_ORBIT_OBSERVABILITY = ACCEPTED`

`F2_F1_CARRIER_ENLARGEMENT_REQUIRED = NO`

`F2_SCALAR_READOUT_FAMILY = ACCEPTED_NONUNIQUE`

`F2_PHYSICAL_READOUT_DERIVED = NO`

`F2_LOCAL_MIXING_DERIVED = NO`

`F2_WAVE_OR_BORN_CLAIM = NOT_AUTHORIZED`

`NEXT_GATE = REVERSIBLE_MIXING_PLUS_SCALAR_CONSERVATION_FORWARD_CLASSIFICATION`
