# CBRC F6 — Minimal Rank-Two Conservative Carrier Classification Return

Researcher-ID: `EM-CBRCF6-D694C8`

Task-ID: `RS-CBRC-F6-MINIMAL-RANK-TWO-CONSERVATIVE-CARRIER-CLASSIFICATION`

Taskbook source: `e5d3c761e291b3193ccbbd85a4a2b05c70338141`

Blind mathematical source: `research_inputs/CBRC_F6_BLIND_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_PACKET_20260825.md@d0991001455a0a40a50f66ac6c14595448d29f21`

Owner branch: `research/cbrc-f6-minimal-rank-two-conservative-carrier`

Status: `FINAL_FROZEN`

Primary verdict:

`F6_UNIQUE_MINIMAL_RANK_TWO_CARRIER_AND_UNARY_CLASS`

Hard target:

`MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_AND_UNARY_TRANSPORT_CLASSIFIED`

Scope: Coherent-BRC **working-extension** only. No statement below promotes the F5 working axioms to canonical Foundation truth.

## 0. Executive result

The issued F6 assumptions force a unique least additive rank-two carrier up to isomorphism preserving the typed upstream embedding and old projection:

`C_min = Z e ⊕ Z f ⊕ <tau | 3 tau=0>`.

No torsion beyond the inherited nonzero order-three `tau` is forced. Every extra finite torsion group is lexicographically worse before unary data are considered.

On this unique least carrier, all projection-covariant additive lifts of the inherited `R,J,S` relations form exactly `22` raw parameter solutions and exactly `6` typed gauge-equivalence classes. Exactly one of those six classes admits a complement generator `f0` on which

`R(f0)=J(f0)=S(f0)=f0`.

Because this class adds **no unary action at all** on the one newly forced free summand, while every other class carries an unavoidable sign or torsion-shear invariant, the issued target-independent minimality order selects it uniquely.

Thus the least F6 object is the direct additive extension of the frozen upstream layer by one unary-trivial infinite cyclic summand. This description is purely additive and does not name or presuppose any downstream rank-two number system.

## 1. Epistemic boundary and raw freeze

The publication-liveness gate was satisfied before mathematics:

- execution stamp commit: `a741fe611e62fbf54f9c5462ffb9f4a450f49d86`;
- remote owner branch was verified to resolve exactly to that commit before the blind packet was opened;
- stamp fields included `phase=STARTED_BEFORE_MATH`, `carrier_verdict=null`, `math_source_read_before_stamp=false`.

Before raw freeze, the only mathematical source read or used was the blind packet pinned above. Checkpoint A / raw freeze was materialized at:

`e8903934f01af9fade5979ebf2507b763b6aea50`.

No historical F1 torsion-free counterfactual, R063/R064/R065/FQ, downstream coherent-wave research, external quantum mechanics, complex/quadratic carrier target, root-of-unity selector, ring/field/multiplication, norm/inner product/quadratic law, or two-slot mixing target was used.

The separate audit concludes:

`TARGET_LEAK_AUDIT_PASS`.

## 2. Q1 — rank-two additive carrier normal form

Let `C` be a finitely generated abelian additive carrier of torsion-free rank exactly `2`, containing the frozen upstream

`j(C1)=Z e ⊕ <tau | 3tau=0>`

and carrying an additive retraction

`pi:C->Z e`

with `pi(e)=e`, `pi(tau)=0`.

### 2.1 Retraction splitting

Since `pi` is a retraction, the inclusion of `Z e` splits it, so

`C = Z e ⊕ K`, where `K=ker(pi)`.

The torsion-free rank of `K` is exactly `1`. Hence the structure theorem gives

`K ≅ Z f ⊕ T`

for a finite abelian group `T`. Because every torsion element is killed by `pi`, the embedded `tau` lies in `T` and has exact order `3`.

Therefore every allowed carrier has normal form

`C ≅ Z e ⊕ Z f ⊕ T`

with a distinguished element `tau in T` of order `3`, and with

`pi(e)=e`, `pi(f)=0`, `pi(T)=0`.

Conversely every pointed finite abelian group `(T,tau)` with `ord(tau)=3` produces such a carrier. Two carriers are isomorphic preserving `j` and `pi` iff their pointed torsion groups `(T,tau)` are isomorphic.

Thus the full nonminimal carrier classification reduces exactly to finite pointed torsion data.

### 2.2 Primitive old generator

The explicit primitive hypothesis is redundant once `pi` is typed. If the old free class satisfied `e=d x` with `|d|>1`, then applying the integer coefficient of `pi` would give `1=d k`, impossible. Hence a retraction onto `Z e` already forces `e` primitive.

### 2.3 Minimal torsion

The upstream embedding forces at least the nonzero order-three subgroup `<tau>`. Nothing forces more torsion: take

`T=<tau>≅Z/3`.

This already supports valid inherited unary extensions, so any larger finite torsion group loses at the second step of the issued lexicographic order before unary details can compensate.

Therefore the unique least additive carrier is

`C_min = Z e ⊕ Z f ⊕ <tau | 3tau=0>`.

### 2.4 Complement gauge and automorphism group

Normalize `f in ker(pi)`. Every typed automorphism fixing the embedded upstream layer pointwise and preserving `pi` is

`g_{eps,a}(e)=e`,
`g_{eps,a}(tau)=tau`,
`g_{eps,a}(f)=eps f+a tau`,

with `eps in {+1,-1}` and `a in Z/3`.

Hence the relevant typed gauge group has six elements and is

`(Z/3) ⋊ {±1}`

with the sign acting on the torsion shift by inversion.

This establishes:

`F6_RANK_TWO_ADDITIVE_CARRIER_NORMAL_FORM_CLASSIFIED`.

## 3. Q2 — conservative-extension notions

The blind packet deliberately does not assume a retract `r:C->C1`. Three strengths are distinct.

### 3.1 Embedding-only

Require the primitive embedded upstream `C1` but do not type a particular old projection. The same abstract additive normal form exists. Primitivity of the old free class guarantees that some integer retraction onto `Z e` exists, but no particular kernel is yet part of the data.

### 3.2 Old-signed-retraction

Typing `pi:C->Z e` selects `K=ker(pi)` and normalizes the new free generator into that kernel. It does not require extra torsion and therefore does not change the least carrier.

### 3.3 Full-upstream retract

A bare additive retract

`r:C->C1`, `r j=id_C1`

exists iff there is a homomorphism

`phi:T->Z/3`

with `phi(tau)=1`. This occurs iff

`tau notin 3T`.

Necessity is immediate because every map to `Z/3` kills `3T`. Conversely, if the class of `tau` in `T/3T` is nonzero, choose an `F3`-linear functional sending it to `1` and compose with `T->T/3T`.

Therefore a pointed cyclic torsion example

`T=Z/9`, `tau=3g`

admits the upstream embedding and old projection but no full upstream retract. The least torsion `T=<tau>≅Z/3` automatically admits one.

### 3.4 Are choices of `r` real data?

On `C_min`, every bare retract has

`r(f)=m e+b tau`, `m in Z`, `b in Z/3`.

If projection compatibility

`pi1 r=pi`

is imposed, then `m=0`, leaving `r(f)=b tau`. The three values of `b` are related by the allowed complement torsion shift and do not create distinct carrier classes.

If instead a non-projection-compatible bare retract is itself frozen as typed structure, `|m|` survives complement orientation and is genuine extra retract data. F6 therefore does **not** select or require a particular full retract; existence at the minimum is automatic and choosing one would add avoidable structure.

This establishes:

`F6_CONSERVATIVE_EXTENSION_NOTIONS_CLASSIFIED`.

## 4. Q3 — exact inherited unary `R/J/S` lifts

Work now on the unique least carrier `C_min`. Since the maps restrict to the frozen upstream layer,

`R(e)=e+tau`, `R(tau)=tau`,
`J(e)=-e`, `J(tau)=-tau`,
`S(e)=e`, `S(tau)=-tau`.

Projection covariance forces the image of `f` to have zero `e`-coordinate. Automorphism invertibility forces its free `f` coefficient to be `±1`. The order-three relation for `R` then forces that coefficient to be `+1`.

Hence every possible lift has the exact form

`R(f)=f+r tau`,
`J(f)=delta f+j tau`,
`S(f)=sigma f+s tau`,

where

`r,j,s in Z/3`, `delta,sigma in {+1,-1}`.

### 4.1 Exact arithmetic constraints

Evaluating the relations on `f` gives the complete congruence system in `Z/3`:

`J^2=id  <=>  (delta-1)j=0`,

`S^2=id  <=>  (sigma-1)s=0`,

`JR=RJ  <=>  (1+delta)r=0`,

`SRS^-1=R^-1  <=>  (sigma-1)(s-r)=0`.

No further constraints arise from `e` or `tau`, because those are exactly the frozen upstream maps.

The four sign sectors are therefore:

| `delta` | `sigma` | constraints | raw solutions |
|---|---|---|---:|
| `+1` | `+1` | `r=0`; `j,s` arbitrary | 9 |
| `+1` | `-1` | `r=0`, `s=0`; `j` arbitrary | 3 |
| `-1` | `+1` | `j=0`; `r,s` arbitrary | 9 |
| `-1` | `-1` | `r=j=s=0` | 1 |

Total: `22` raw lifts.

### 4.2 Gauge action

Under the typed complement change

`f -> eps f+a tau`,

simultaneous conjugation sends

`r -> eps r`,
`j -> eps[j+a(delta+1)]`,
`s -> eps[s+a(sigma+1)]`

in `Z/3`.

This action preserves the sign sector and yields exactly six equivalence classes.

A convenient set of representatives is:

| class | `(delta,sigma;r,j,s)` | unavoidable new unary datum |
|---|---|---|
| `U0` | `(+1,+1;0,0,0)` | none |
| `U1` | `(+1,+1;0,0,1)` | nonzero relative `J/S` torsion offset |
| `U2` | `(+1,-1;0,0,0)` | `S` free sign |
| `U3` | `(-1,+1;0,0,0)` | `J` free sign |
| `U4` | `(-1,+1;1,0,0)` | `J` free sign plus nonzero `R` torsion shear |
| `U5` | `(-1,-1;0,0,0)` | both free signs |

For the `(+,+)` sector the invariant is `s-j` up to overall sign, giving zero/nonzero. For `(-,+)`, after gauging `s` to zero, `r` is invariant up to sign, again giving zero/nonzero. The other two sign sectors each form one orbit.

### 4.3 Free-quotient information

Modulo torsion, every valid lift satisfies

`R_bar(f)=f`,
`J_bar(f)=delta f`,
`S_bar(f)=sigma f`.

Thus the new free direction cannot carry a genuine order-three unary orbit. At free-quotient level it is forced to be **fixed/sign-only**. Any further finite distinction among the six classes comes from torsion-coupled shear data, not from a nontrivial order-three action on the new free plane.

This establishes:

`F6_INHERITED_UNARY_TRANSPORT_LIFTS_CLASSIFIED`.

## 5. Q4 — minimal carrier and unary class

The issued minimality order is applied in order, not retrospectively.

### Step 1 — preserve upstream

The nonzero order-three `tau` and frozen unary restrictions are retained exactly.

### Step 2 — minimize additional torsion

`T=<tau>≅Z/3` is feasible. Every larger pointed finite torsion group is therefore strictly dominated.

### Step 3 — minimize new additive generators/relations

Torsion-free rank two requires one new free direction and no relation on it. `C_min` has exactly that.

### Step 4 — minimize additional unary structure/data

Among the six lift classes, `U0` is uniquely characterized by the invariant property:

> there exists a complement generator `f0 in ker(pi)` such that `R(f0)=J(f0)=S(f0)=f0`.

Hence `U0` adds no unary action on the new free summand. Every other class has an unavoidable nontrivial sign or torsion-shear invariant in every allowed complement. Therefore `U0` is strictly least in additional unary structure/data.

### Step 5 — canonical description

The least object is described basis-independently as the frozen upstream additive/unary object direct-summed with one infinite cyclic summand on which all inherited unary maps act trivially. No downstream target resemblance is used.

Therefore the least carrier/unary object is unique up to typed isomorphism.

This establishes:

`F6_MINIMAL_RANK_TWO_CARRIER_UNARY_CLASSIFIED`.

## 6. Q5 — upstream relative structure preserved

For every one of the six minimal-carrier unary equivalence classes, and hence in particular for the unique least class, the restriction to the embedded upstream layer is exact.

The two frozen relative identities remain:

`e+J e = e-e = 0`,

while

`R e=e+tau`,
`J R e=-e-tau`,

so

`e+J R e=-tau != 0`.

The direct-sum presentation has one torsion relation only, `3tau=0`; therefore neither `e` nor `tau` is newly collapsed. The checker confirms the Smith data

`free rank = 2`, `torsion invariants = [3]`.

For every one of the `22` raw valid lifts, the exact checker evaluates all words in `R,J,S` of length at most `4` on the embedded generators `e,tau` and compares them with the frozen upstream maps. This is `121` words per lift, `2662` word/lift checks, and `5324` generator comparisons. All match exactly.

No multiplication operation exists in the model or checker.

This establishes:

`F6_UPSTREAM_RELATIVE_STRUCTURE_PRESERVED`.

## 7. Mandatory ablations

All required one-at-a-time ablations are frozen in

`research_reports/CBRC_F6_CARRIER_COUNTERMODEL_AND_ABLATION_PACKET_20260825.md`.

Summary:

- primitive old generator: `REDUNDANT_GIVEN_PI`;
- preserve order-three `tau`: essential; otherwise the relative witness collapses;
- old retraction `pi`: removing the typed projection admits integral `e`-shear classes;
- full upstream retract: not used for the least class; stronger away from the minimum;
- `R^3=id`: essential; without it `R(f)=-f` is possible;
- `JR=RJ`: essential; without it `R(f)=f+tau`, `J(f)=f` is possible;
- `SRS^-1=R^-1`: essential; without it `R(f)=f+tau`, `J(f)=S(f)=-f` is possible;
- old-projection covariance: essential; without it `S(f)=3e-f` survives all unary group relations;
- no-extra-torsion preference: essential for uniqueness; otherwise `C_min⊕Z/m` gives infinitely many carrier types.

## 8. Deterministic checker evidence

Required checker:

`scripts/cbrc_f6_validate_minimal_rank_two_conservative_carrier.py`

Checkpoint-B checker commit:

`e673df1842fd371a66fb827c1f6b8d8a5e02c487`

Remote Git blob SHA-1:

`be8f34e8d10bd934497439d8fabd231b82480020`

Executed byte sequence Git blob SHA-1:

`be8f34e8d10bd934497439d8fabd231b82480020`

Therefore the executed checker was byte-identical to the pushed checker.

Byte count: `17810`.

Checker SHA-256:

`682c3ba50ede00bf5cad9ea948e03b8542f1d8a0ded927c2aef34664bd2e9b2a`.

Deterministic stdout SHA-256:

`1cf4c992156d34f12183d7b160805c332e31b146704d3f0bea96429a8e329e7e`.

Result:

`PASS`, exit code `0`, theorem/model mismatches `0`.

Coverage includes SNF witnesses, bounded primitive embeddings, all `22` finite unary parameter cases, all `6` equivalence classes, exact relation checks, gauge canonicalization, upstream witness, depth-4 typed composition, and every required ablation.

## 9. Q6 — final verdict and unresolved frontier

Primary verdict:

`F6_UNIQUE_MINIMAL_RANK_TWO_CARRIER_AND_UNARY_CLASS`.

The unique least F6 class is:

- additive carrier: `Z e ⊕ Z f ⊕ <tau | 3tau=0>`;
- typed old projection: `pi(e)=e`, `pi(f)=pi(tau)=0`;
- inherited upstream action unchanged;
- least unary action on the new free complement: `R(f)=J(f)=S(f)=f` up to typed gauge.

Genuine structure versus presentation freedom:

- genuine: nonzero order-three `tau`, one added free rank, old projection, six total unary-lift isomorphism classes, and the unique unary-trivial minimum;
- presentation only: complement orientation `f->-f`, torsion shifts `f->f+a tau`, and projection-compatible full-retract choice `r(f)=b tau` if such a retract is chosen at all.

What remains unresolved, and is intentionally **not** opened here:

- any two-slot mixing classification;
- scalar laws or coefficient multiplication;
- ring/field/module structures beyond the already used additive group;
- norms, inner products, quadratic or square laws;
- splitter/Fourier/Hadamard targets;
- readout laws, continuum limits, or wave structures;
- whether a future authorized mixing stage adds constraints that select or exclude any nonminimal unary class.

F6 stops before all of those questions.

## 10. Acceptance labels

`F6_RANK_TWO_ADDITIVE_CARRIER_NORMAL_FORM_CLASSIFIED`

`F6_CONSERVATIVE_EXTENSION_NOTIONS_CLASSIFIED`

`F6_INHERITED_UNARY_TRANSPORT_LIFTS_CLASSIFIED`

`F6_MINIMAL_RANK_TWO_CARRIER_UNARY_CLASSIFIED`

`F6_UPSTREAM_RELATIVE_STRUCTURE_PRESERVED`

`TARGET_LEAK_AUDIT_PASS`

`MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_AND_UNARY_TRANSPORT_CLASSIFIED`

Final primary verdict:

`F6_UNIQUE_MINIMAL_RANK_TWO_CARRIER_AND_UNARY_CLASS`
