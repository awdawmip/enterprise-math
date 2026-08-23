# CBRC F2 — Observable Non-Sign Recoalescence Forward Classification Return

Researcher-ID: `EM-CBRC-F2-CB605B`  
Task-ID: `RS-CBRC-F2-OBSERVABLE-NONSIGN-RECOALESCENCE-FORWARD-CLASSIFICATION`  
Owner branch: `research/cbrc-f2-observable-nonsign-recoalescence-forward-classification`  
Taskbook source: `9866e523b7e7f134497d8aca9ba2b6a093600257`  
Blind mathematical input source: `155297ab859e4207634dae75566c89ca1a430000`  
Raw-freeze status: `F2_RAW_FREEZE_COMPLETE`

## 1. Primary verdict

`F2_F1_CARRIER_OBSERVABLE_READOUT_FAMILY`

Hard target:

`OBSERVABLE_NONSIGN_RECOALESCENCE_MINIMAL_EXTENSION_CLASSIFIED`

The accepted F1 carrier is already relatively observable. No carrier enlargement is required.

The visibility is not on the same-sign two-path aggregate. It occurs on the opposite-sign two-path recoalescence:

`e + J R e = e - (e + tau) = -tau != 0`

while the old sign-dark aggregate is

`e + J e = 0`.

The nonzero pure-torsion aggregate and zero are not identified by the required common `R/J/S` actions, so O1–O9 allow a scalar readout that distinguishes them. O10 is therefore realizable.

The scalar law is not unique.

## 2. Exact carrier/action model used

Write each coefficient as

`z = n e + a tau <-> (n,a)`, with `n in Z`, `a in Z/3Z`.

From the blind input:

- `R(n,a) = (n, a+n)`;
- `J(n,a) = (-n,-a)`;
- `S(n,a) = (n,-a)`.

All second coordinates are modulo `3`.

No additional coefficient multiplication, bilinear form, power rule, or external model is introduced.

## 3. Orbit-space theorem

Let `G=<R,J,S>` act on `C1`.

### Theorem F2-O

The `G`-orbits are exactly:

1. `Omega_0 = {(0,0)}`.
2. `Omega_T = {(0,1),(0,2)}`.
3. For every `r>0` with `3 not| r`:
   `Omega_r = {(±r,a): a in Z/3Z}`.
4. For every `r>0` with `3 | r`, there are exactly two orbits:
   - `Omega_r^0 = {(±r,0)}`;
   - `Omega_r^T = {(±r,1),(±r,2)}`.

### Proof

`R^k(n,a)=(n,a+kn)`.

If `3 not| n`, multiplication by `n` permutes `Z/3Z`, hence common transport is transitive on all three `a` values. `J` changes the sign of `n`, while `S` reverses `a`; therefore the orbit is determined only by `|n|`.

If `3 | n`, common transport acts trivially on `a`. `S` exchanges `a=1` and `a=2`, and `JS` changes `n` to `-n` while preserving `a`. Thus `a=0` is one orbit and `a!=0` is one orbit for each `|n|`.

For `n=0`, the same argument gives the zero singleton and the nonzero torsion pair.

This exhausts `C1`.

Deliverable status:

`F1_CARRIER_RELATIVE_OBSERVABILITY_ORBIT_SPACE_CLASSIFIED`

## 4. One- and two-elementary classification

Every elementary occurrence has the form

`J^s R^k e`, with `s in {0,1}`, `k in Z/3Z`.

All six signed/transported elementary occurrences lie in `Omega_1`.

For two elementary alternatives there are exactly three `G`-orbit classes:

1. same sign: `Omega_2`;
2. opposite sign with equal transport: `Omega_0`;
3. opposite sign with unequal transport: `Omega_T`.

For the exact O10 comparison:

| `s` | `k` | aggregate `e + J^s R^k e` | orbit |
|---|---:|---|---|
| 0 | 0 | `(2,0)` | `Omega_2` |
| 0 | 1 | `(2,1)` | `Omega_2` |
| 0 | 2 | `(2,2)` | `Omega_2` |
| 1 | 0 | `(0,0)` | `Omega_0` |
| 1 | 1 | `(0,2)` | `Omega_T` |
| 1 | 2 | `(0,1)` | `Omega_T` |

Therefore:

- same-sign non-sign transport is necessarily invisible under O5;
- opposite-sign unequal transport can be visible;
- O10 is possible on `C1`.

## 5. Exact readout-family classification

Any O5–O7 invariant scalar readout is exactly a function on the orbit set above.

Let

- `f_0 = rho(Omega_0)`;
- `t = rho(Omega_T)`;
- `u_r = rho(Omega_r)` for `3 not| r`;
- `v_r^0 = rho(Omega_r^0)` for `3 | r`;
- `v_r^T = rho(Omega_r^T)` for `3 | r`.

Then O1–O10 are equivalent to the following scalar constraints:

- `f_0 = 0`;
- `u_1 = 1`;
- `t > 0`;
- every remaining `u_r, v_r^0, v_r^T` is an arbitrary nonnegative scalar.

O4 remains a separate tagged bookkeeping rule: two still-distinguishable elementary alternatives have tagged total `2`. It imposes no equality between that tagged total and the unmarked aggregate readout.

Thus the readout is infinitely nonunique.

### Exact witness A — support readout

`rho_A(z)=0` for `z=0`, and `rho_A(z)=1` for every nonzero `z`.

This satisfies O1–O10 and has `rho_A(tau)=1`.

### Exact witness B — orbit-separating readout

Define:

- `rho_B(0)=0`;
- `rho_B(Omega_T)=2`;
- `rho_B(Omega_1)=1`;
- for `r>=2`, `3 not|r`, set `rho_B(Omega_r)=4r`;
- for `3|r`, set `rho_B(Omega_r^0)=4r+1`, `rho_B(Omega_r^T)=4r+2`.

This also satisfies O1–O10 and separates every `G`-orbit.

The witnesses are inequivalent, e.g. on `(2,0)`:

`rho_A(2,0)=1`, while `rho_B(2,0)=8`.

### Faithfulness classification

- Pointwise faithfulness on raw coefficient states is impossible because O5–O7 intentionally identify all states in one `G`-orbit.
- Orbit-faithful readout is possible; witness B is explicit.
- O10 forces the nonzero pure-torsion orbit to be distinguishable from zero.
- Orientation inside `{tau,-tau}` is necessarily invisible under O6/O7.
- Other nonzero orbits may still be assigned zero unless an extra zero-separation principle is imposed.

Deliverable status:

`NONSIGN_RECOALESCENCE_READOUT_EXISTENCE_CLASSIFIED`

## 6. O1–O10 status table

| condition | status on `C1` | exact reason |
|---|---|---|
| O1 `NULL_ZERO` | PASS | set `rho(Omega_0)=0` |
| O2 `ELEMENTARY_NORMALIZATION` | PASS | set `rho(Omega_1)=1` |
| O3 `ABSOLUTE_NONSIGN_INVISIBILITY` | PASS / redundant | on elementary states it follows from O2+O5+O6 |
| O4 `DISTINGUISHABLE_ALTERNATIVE_ADDITIVITY` | PASS | separate tagged rule gives `1+1=2` |
| O5 `COMMON_TRANSPORT_INVARIANCE` | PASS | `rho` is constant on `R`-orbits |
| O6 `GLOBAL_SIGN_INVARIANCE` | PASS | `rho` is constant on `J`-orbits |
| O7 `REVERSAL/SERIALIZATION_INVARIANCE` | PASS | `rho` is constant on `S`-orbits; aggregate addition is order-independent |
| O8 `AGGREGATE_PRESENTATION_INDEPENDENCE` | PASS | `rho` takes only the erased aggregate coefficient as input |
| O9 `COMPOSITION_COMPATIBILITY` | PASS | the same full-domain orbit function is used after every finite composition |
| O10 `NONSIGN_RELATIVE_SENSITIVITY` | PASS iff `t>0` | `e+JRe=-tau in Omega_T`, whereas `e+Je=0` |

## 7. Observable-minimal carrier result

F2 uses an observable-extension order that first respects the already accepted F1 rank-primary extension order and only then compares observability cost.

For carriers tied at the F1 structural level, compare the following observability vector:

`K_obs = (delta torsion-free rank, new additive generators, new defining relations, finite forgetful-kernel size, elementary transport-orbit size, extra multiplication/bilinear structure flag, forced scalar distinctions on the minimal two-path fiber)`.

For `C1`:

- torsion-free rank increase: `0`;
- new additive generators: `1` (`tau`);
- new defining relations: `1` (`3 tau=0`);
- finite forgetful kernel: `3`;
- elementary `R`-orbit size: `3`;
- extra multiplication/bilinear structure: `0`;
- minimal two-path carrier orbit classes: `3` (`Omega_2`, `Omega_0`, `Omega_T`);
- scalar classes forced distinct by O1+O10: at least `2` (`Omega_0` versus `Omega_T`).

The blind packet already freezes `C1` as the least F1 conservative finite non-sign reversible enrichment under the accepted rank-primary extension order. Since `C1` itself satisfies O10, no carrier strictly below that accepted F1 minimum can be F2-observable: such a carrier cannot even satisfy the upstream non-sign transport requirement.

Therefore `C1` remains minimal after observability is added.

No omitted F1 counterfactual carrier was read or used.

Deliverable status:

`OBSERVABLE_NONSIGN_MINIMAL_CARRIER_FAMILY_CLASSIFIED`

## 8. Finite-path / refinement extension theorem

For a finite same-terminal fiber, write branch `i` as

`c_i = J^{s_i} R^{k_i} e`.

Let `epsilon_i=(-1)^{s_i}`.

After marker erasure the aggregate is

`Z = sum_i c_i = (N,A)`

with

`N = sum_i epsilon_i`

and

`A = sum_i epsilon_i k_i mod 3`.

This formula is derived only from the additive carrier and composition of powers of `R`.

### Common transport

Adding a common transport `t` to every branch gives

`A -> A + tN mod 3`,

exactly matching

`R^t(N,A)=(N,A+tN)`.

Hence:

- if `3 not| N`, common transport removes every `A` distinction;
- if `3 | N`, `A` survives common transport, while O7 identifies `A` with `-A`.

Thus finite-fiber scalar orbit structure is:

- one `A`-class for every `N` not divisible by `3`;
- two `A`-classes (`A=0`, `A!=0`) whenever `N` is divisible by `3`.

### First appearance

The first possible non-sign scalar behavior already occurs with two alternatives:

`N=0`, `A!=0`.

At three alternatives, same-sign fibers can have `N=±3`, so an additional optional `A=0` versus `A!=0` distinction becomes available. O10 does not force that higher-fiber distinction, but the full readout family allows it.

### Required structural checks

- depth-3 serial composition: powers of `R` add modulo `3`;
- depth-4 serial composition: same;
- commuting composition: `R^a R^b = R^b R^a = R^{a+b}`;
- at least three alternatives: aggregate formula above is permutation-independent;
- marker refinement: tagged subfamilies can be retained, then erasure uses associative/commutative addition;
- branch swap: aggregate unchanged;
- reversal: `A -> -A`;
- common transport: `A -> A+tN`;
- sign-only recovery: setting all `k_i=0` gives the old signed aggregates; in particular two same-sign elementary alternatives give `(2,0)` and opposite equal-sign labels give `0`.

The last item recovers the F0 constructive/dark algebraic examples only; no scalar value beyond the frozen F0 facts is imported.

Deliverable status:

`OBSERVABLE_NONSIGN_FINITE_FIBER_EXTENSION_CLASSIFIED`

## 9. Readout-selector dependency classification

No additional selector is promoted to a foundational rule.

### Selector S1 — unmarked/tagged upper bound

Candidate principle:

For any presentation by `m` elementary alternatives,

`rho(sum_i c_i) <= m`.

For the minimal torsion witness, the shortest presentation has two elementary alternatives, hence

`0 < t <= 2`.

This reduces but does not select `t`.

Ablation countermodel: choose an otherwise valid orbit readout with `t=3`.

### Selector S2 — zero separation

Candidate principle:

`z!=0 => rho(z)>0`.

This forces every free orbit parameter to be positive, but still leaves infinitely many readouts.

Ablation countermodel: an O1–O10 readout may set, for example, one nonzero `Omega_3^0` value to `0` while retaining `t>0`.

### Selector S3 — monotonicity in the emergent integer coordinate

Candidate principle:

Within a fixed orbit type, increasing `|n|` cannot decrease the scalar.

This restricts the sequences `u_r`, `v_r^0`, `v_r^T`, but does not determine them.

Ablation countermodel: set `u_2=5`, `u_4=1`; all O1–O10 remain valid.

### Selector S4 — linear finite-copy scaling

Candidate principle:

For every positive integer `m`,

`rho(m z)=m rho(z)`.

This is incompatible with observable order-three torsion:

`3 tau=0`

would imply

`0=rho(0)=rho(3 tau)=3 rho(tau)`,

contradicting O10's `rho(tau)>0`.

Therefore this selector does not choose a scalar law on `C1`; it rejects the observable torsion mechanism itself.

### Additional local mixing

No independent nontrivial local mixing operation is present in the blind whitelist. Introducing one as a selector in F2 would be an extra mathematical preload, so it is not used.

Deliverable status:

`READOUT_SELECTOR_DEPENDENCY_CLASSIFIED`

## 10. Mandatory ablation summary

| ablation | result |
|---|---|
| remove O3 | no widening on the declared elementary domain; O3 is implied by O2+O5+O6 |
| remove O4 | unmarked family unchanged; tagged two-alternative total becomes a free bookkeeping parameter |
| remove O5 | same-sign states `(2,0)` and `(2,±1)` may split; non-sign visibility can be manufactured there |
| remove O6 | `+n` and `-n` aggregate classes may split beyond the normalized elementary orbit |
| remove O7 | minimal two-path result unchanged, but a reversal-sensitive split first appears at `|n|=3`, `a=1` versus `a=2` |
| remove O8 | two presentations with the same aggregate may receive different scalars; provenance becomes observable |
| remove O9 | depth-indexed/readout-table rules can disagree on the same coefficient at different composition depths |
| remove O10 | `rho(n,a)=|n|` satisfies O1–O9 but sends nonzero pure torsion to the same scalar as zero |
| remove minimal-carrier requirement | `C1` may be enlarged by an inert `Z/2` summand while preserving the same F2 witness |

Detailed countermodels are in the dedicated ablation packet.

## 11. Deterministic checker

Required checker:

`scripts/cbrc_f2_validate_observable_nonsign_forward.py`

It uses exact integer/mod-3 arithmetic and checks:

- action identities;
- exact `R/J/S` orbit theorem on `n in [-9,9]`;
- all one- and two-elementary aggregate states;
- the full minimal relative-transport table;
- two inequivalent exact readouts;
- depth-3 and depth-4 serial composition;
- commuting transport composition;
- all `216` three-alternative signed/transport label triples;
- branch permutations;
- common transport and reversal;
- marker-erasure associativity;
- sign-only recovery;
- every mandatory ablation countermodel.

Theorem/enumeration mismatches: `0`.

Deterministic digest:

`8d3a47d9f755826dce69c8a198ef0092bfb668a630c7737a3b864b60227f92d3`

The finite enumeration is regression evidence only; the infinite-domain classification is proved by the orbit theorem above.

## 12. Unresolved assumptions / exact scope

1. Minimality is claimed relative to the accepted F1 rank-primary extension order supplied in the blind packet. F2 does not reconstruct omitted F1 carrier families.
2. O4 is intentionally separate tagged bookkeeping. No conservation equation equating tagged total and unmarked recoalesced scalar is present in O1–O10.
3. O9 requires one scalar function on the full coefficient domain, but it does not itself impose additive or multiplicative scaling of scalar values.
4. No principle in the whitelist selects a unique value of `t` or the higher-orbit parameters.
5. No physical interpretation is asserted.

## 13. Acceptance labels

`F1_CARRIER_RELATIVE_OBSERVABILITY_ORBIT_SPACE_CLASSIFIED`

`NONSIGN_RECOALESCENCE_READOUT_EXISTENCE_CLASSIFIED`

`OBSERVABLE_NONSIGN_MINIMAL_CARRIER_FAMILY_CLASSIFIED`

`OBSERVABLE_NONSIGN_FINITE_FIBER_EXTENSION_CLASSIFIED`

`READOUT_SELECTOR_DEPENDENCY_CLASSIFIED`

`TARGET_LEAK_AUDIT_PASS`

Primary verdict:

`F2_F1_CARRIER_OBSERVABLE_READOUT_FAMILY`
