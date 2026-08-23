# Tool Discovery Result — Weighted Incidence Energy / Dirichlet Calculus

Researcher-ID: `EM-TDIE-88E8B1`

Task-ID: `RS-TD-IE-WEIGHTED-INCIDENCE-ENERGY-DIRICHLET-CALCULUS`

Owner branch:

`research/tool-weighted-incidence-energy-dirichlet`

Hard target:

`ENTERPRISE_WEIGHTED_INCIDENCE_ENERGY_TOOL_CLASSIFIED`

## 1. Frozen terminal result

Primary terminal classification:

`DOMAIN_SPECIALIZATION_ONLY`

Ownership recommendation:

`SUBTOOL_OR_EXTENSION_OF_LAPLACIAN`

Companion hard boundary:

`EXACT_NO_GO_FROM_BARE_INCIDENCE`

No new global tool family is accepted.

The positive mathematics is exact and useful, but it is useful only after adding explicit positive quadratic structure to a finite incidence carrier. In the admissible source packet, no second natural Enterprise domain with independently justified positive quadratic weights was found. Therefore the two-domain gate for a separate reusable Enterprise energy family fails.

Moreover, all accepted graph-potential / flow results factor through the weighted incidence operator and its induced weighted Laplacian

`L = B C B^T`

plus, when an explicit cycle/circulation witness is desired, the existing T3 typed incidence/circuit structure. Hence if the sibling Laplacian task accepts the same weighted-incidence / potential / source contract, this layer should be owned as a Laplacian subtool or extension, not as an independent energy family.

This ownership statement is structural. The sibling task's research return was not used as a premise.

## 2. Exact source baseline

The task was executed from the specified taskbook source and only its declared dependencies/source references were used.

| Source | Frozen reference | Role |
|---|---|---|
| taskbook | `research_tasks/TOOL_DISCOVERY_WEIGHTED_INCIDENCE_ENERGY_DIRICHLET_CALCULUS_20260823.md@c0663825763b33e629394e68066386da93675320` | controlling semantics / stop condition |
| toolbox registry | `enterprise_toolbox_registry.json@bd10bc351dbe7c90b47a3ffba3ef7796479170f5` | T3/T4/T8/T9 ownership and tool acceptance |
| method inventory | `research_method_inventory.json@bd10bc351dbe7c90b47a3ffba3ef7796479170f5` | current reuse surface |
| invocation policy | `tool_invocation_policy.json@bd10bc351dbe7c90b47a3ffba3ef7796479170f5` | anti-duplication / extend-vs-new-family rule |
| exact incidence source | `src/enterprise_math/collapse_incidence.py` blob `7af320f5a0c0bde90ba227f0eded044786e84060` | establishes that overlap witness counts are not energy |

The exact incidence source explicitly states that its Gram/shared-target and higher overlap counts are not identified with force, energy, probability, or thermodynamic entropy.

Therefore the highest semantic freeze is respected:

`BARE_INCIDENCE != ENERGY`.

## 3. Minimal positive semantic contract

The positive graph calculus requires all of the following extra structure.

### 3.1 Carrier

A finite vertex set `V`, finite edge set `E`, and an arbitrary auxiliary orientation.

Let `B` be the signed vertex-edge incidence matrix with:

- `-1` at the tail;
- `+1` at the head.

Orientation is auxiliary, not semantic.

### 3.2 Positive weights

A strictly positive conductance on every supported edge:

`c_e > 0`.

Write:

`C = diag(c_e)`.

Equivalently one may declare strictly positive resistance weights

`r_e = 1 / c_e`.

The reciprocal convention must be explicit.

### 3.3 Exact coefficient regime

The checker works over `Q` using exact `fractions.Fraction`.

The theorem statements require an ordered coefficient field/ring strong enough for the divisions actually used. Claims requiring Schur complements, unique minimizers, or reciprocal conductances require invertibility of the relevant nonzero weights/minors.

### 3.4 Potential semantics

A scalar potential is a function:

`u : V -> K`.

Define the Dirichlet quadratic form:

`D(u) = (B^T u)^T C (B^T u)`,

hence

`D(u) = u^T L u`

with

`L = B C B^T`.

No physical interpretation is inferred merely from this formula.

### 3.5 Flow/source semantics

A flow is:

`j : E -> K`.

With the incidence convention above, define source/outflow vector:

`q = -B j`.

The positive resistance inner product is:

`<x,y>_R = x^T C^{-1} y`.

The flow energy is:

`T(j) = <j,j>_R`.

The gradient/Ohm flow associated to `u` is:

`j_u = -C B^T u`.

Then:

`q = L u`.

### 3.6 Boundary semantics

A Dirichlet problem additionally requires an explicitly declared boundary set and fixed boundary values.

A fixed-source Thomson problem requires an explicitly declared source vector satisfying componentwise balance on each connected component.

Without these semantics there is no unique minimization problem to solve.

## 4. Exact structural laws

### 4.1 Orientation invariance — PROVED / CHECKED

Flipping an auxiliary edge orientation negates the corresponding column of `B`.

For potentials,

`(B^T u)_e`

changes sign but its weighted square does not.

Therefore:

`D(u)`

and

`L = B C B^T`

are invariant.

For flows, if the corresponding coordinate `j_e` is also negated, both:

`T(j)`

and

`q = -B j`

remain invariant.

### 4.2 Positivity and kernel — PROVED / CHECKED

For strictly positive conductances:

`D(u) = sum_e c_e (u_head - u_tail)^2 >= 0`.

For a connected carrier:

`D(u)=0`

iff `u` is constant.

For a carrier with `k` positive-weight connected components:

`dim ker L = k`.

This statement does not extend to arbitrary signed or zero weights.

### 4.3 Polarization — PROVED

Over characteristic not equal to two, the quadratic form determines the symmetric bilinear form:

`<u,v>_D = (D(u+v)-D(u)-D(v))/2`

and equivalently:

`<u,v>_D = u^T L v`.

This requires a symmetric quadratic-form semantics. A nonsymmetric interaction operator is not itself recovered as the gradient operator of its scalar quadratic expression.

### 4.4 Dirichlet principle — PROVED / CHECKED

Partition vertices into fixed boundary `S` and interior `I`.

With positive conductances, if every connected component meets `S`, then `L_II` is positive definite and the unique minimizer satisfies:

`L_II u_I = -L_IS u_S`.

Certificate:

- boundary values are exact;
- the interior Euler-Lagrange residual is zero;
- strict positivity on the boundary-zero variation space gives uniqueness.

If an interior connected component does not meet the boundary, constants on that component create non-uniqueness and `L_II` is singular.

### 4.5 Thomson principle — PROVED / CHECKED

For fixed feasible source vector `q`, minimize:

`T(j) = j^T C^{-1} j`

subject to:

`-B j = q`.

The feasible set exists only if `q` sums to zero on every connected component.

With positive conductances, the minimizer is unique and is a gradient flow:

`j_* = -C B^T u`

for a potential solving:

`L u = q`

up to componentwise additive constants.

Certificate:

- exact source constraint;
- exact gradient representation;
- orthogonality to every circulation.

### 4.6 Gradient/circulation orthogonal decomposition — PROVED / CHECKED

Let:

`Z = ker B`

be the circulation space.

Then under the positive resistance inner product:

`im(-C B^T) perp_R ker B`.

Indeed for every potential `u` and circulation `z`:

`<-C B^T u, z>_R = -u^T B z = 0`.

Finite-dimensional positive definiteness yields the direct sum:

`K^E = im(-C B^T) direct_sum_R ker B`.

Hence every flow splits uniquely as:

`j = j_grad + j_circ`

with the exact Pythagorean identity:

`T(j) = T(j_grad) + T(j_circ)`.

The circulation carrier/certificate is naturally compatible with T3; the weighted orthogonal projection requires the additional positive inner product.

### 4.7 Effective resistance/pairing — SUPPORTED ONLY WITH NETWORK-LIKE WEIGHT SEMANTICS

For vertices `a,b` in the same connected positive network, let:

`q = e_a - e_b`.

The effective resistance is the minimum unit-source flow energy:

`R_eff(a,b) = min{-Bj=q} T(j)`.

Equivalently, after grounding `b`, solve:

`L u = q`

and obtain:

`R_eff(a,b) = u_a-u_b`.

This is not defined by bare incidence alone. Rescaling conductances changes the value while leaving the unweighted carrier unchanged.

### 4.8 Schur/Kron reduction — PROVED / CHECKED UNDER INVERTIBILITY

Partition:

`V = S union I`.

If `L_II` is invertible, define:

`L_red = L_SS - L_SI L_II^{-1} L_IS`.

For fixed boundary vector `f`, the eliminated interior minimizer has energy:

`min_{u_I} D(f,u_I) = f^T L_red f`.

The reduced operator also gives the exact boundary response.

For positive graph Laplacians, invertibility is guaranteed when every eliminated connected component is pinned to the retained boundary. It fails for an eliminated component disconnected from the retained set.

## 5. Exact checker

Required executable:

`scripts/tool_discovery_weighted_incidence_energy_dirichlet_check.py`

The checker uses exact rational arithmetic only for theorem-level claims.

Frozen local execution summary:

```text
theorem_check_pairs=16
mismatch_count=0
global_tool_claim=NO
second_enterprise_weighted_domain=NOT_ESTABLISHED
classification=DOMAIN_SPECIALIZATION_ONLY
ownership_recommendation=SUBTOOL_OR_EXTENSION_OF_LAPLACIAN
ALL_EXACT_CHECKS_PASS
```

Coverage:

1. positive Dirichlet semidefiniteness and connected kernel;
2. potential/flow/source orientation invariance;
3. exact Dirichlet minimizer and exhaustive rational grid comparison;
4. Thomson minimizer and exact circulation orthogonality;
5. full gradient/circulation decomposition and Pythagorean identity;
6. series and parallel effective resistance;
7. Schur/Kron boundary-energy preservation;
8. disconnected kernel multiplicity;
9. zero-weight enlarged kernel / positive-API rejection;
10. negative-weight loss of positivity;
11. nonsymmetric operator obstruction;
12. bare overlap Gram versus Dirichlet-form semantics;
13. non-identifiability of effective resistance from bare incidence;
14. minimum-energy flow versus native shortest-path mismatch;
15. singular Kron elimination obstruction;
16. fixed-source component-balance obstruction.

Mismatch count is zero.

## 6. Hard negative boundaries and counterexamples

### 6.1 Bare incidence / overlap Gram called energy — REJECTED

Take the 0/1 incidence matrix:

`M = [[1,1],[1,0]]`.

Then:

`M^T M = [[2,1],[1,1]]`.

The off-diagonal `1` is exactly a shared-target witness count.

For the constant vector `(1,1)`:

`(1,1) M^T M (1,1)^T = 5`.

By contrast, a connected graph Dirichlet form must annihilate constant potentials.

Therefore even though `M^T M` is a perfectly valid positive semidefinite Gram form, the bare overlap Gram does not satisfy the defining constant-kernel semantics of a graph Dirichlet energy, and—more importantly—the source semantics explicitly says its entries are witness counts, not energy.

Verdict:

`BARE_OVERLAP_GRAM_AS_ENERGY = SEMANTIC_TYPE_ERROR`.

### 6.2 Negative conductance — positivity fails

One edge with:

`c=-1`

and potential values `(0,1)` gives:

`D(u)=-1`.

Therefore signed weights cannot silently enter the positive Dirichlet/Thomson API.

### 6.3 Zero conductance — extra kernel / singularity

One two-vertex edge with:

`c=0`

has zero Laplacian.

Kernel dimension is `2`, not the connected-positive-graph value `1`.

Therefore zero-weight edges must either be deleted from the positive support or handled by a separate semidefinite/singular contract.

### 6.4 Disconnected carrier — kernel multiplicity

Two disconnected positive edges on four vertices give:

`dim ker L = 2`.

A global statement "kernel = constants" is false unless connectedness is explicit.

### 6.5 Nonsymmetric interaction — not an undirected Dirichlet operator

Let:

`A = [[1,1],[0,1]]`.

The scalar quadratic expression:

`x^T A x`

depends only on:

`(A+A^T)/2`.

Its gradient is:

`(A+A^T)x`,

not generally:

`2Ax`.

Thus a nonsymmetric interaction cannot be treated as the operator induced by an undirected quadratic energy unless an additional symmetrization or different semantics is declared.

### 6.6 Effective resistance without conductance semantics — non-identifiable

The same single-edge unweighted incidence carrier can be assigned:

- `c=1`, giving `R_eff=1`;
- `c=2`, giving `R_eff=1/2`.

Therefore bare incidence does not determine effective resistance.

A unit-conductance convention would itself be additional declared semantic structure.

### 6.7 Minimum-energy flow is not a native shortest path

On a triangle with unit conductances and unit source/sink, the minimum-energy flow is:

`(1/3, 1/3, 2/3)`

across the two-edge route and the direct edge.

The native shortest-path unit flow is the direct edge only:

`(0,0,1)`.

The two objects differ, and the minimum-energy flow has lower quadratic flow energy by distributing current.

Therefore:

`MINIMUM_ENERGY_SOLUTION != NATIVE_GEOMETRIC_SHORTEST_PATH`.

### 6.8 Kron reduction with unpinned eliminated component — undefined in the claimed form

If the retained boundary is disconnected from an eliminated positive component, `L_II` is singular.

The Schur complement formula requiring `L_II^{-1}` is not available.

### 6.9 Fixed source without componentwise balance — infeasible

If a disconnected component has nonzero total prescribed source, no flow can satisfy the divergence/source equation.

### 6.10 Thermodynamic or physical promotion — rejected

A finite positive quadratic form is a mathematical energy functional in a declared variational sense.

It is not thereby:

- physical energy;
- thermodynamic free energy;
- probability;
- entropy;
- force.

Those interpretations require additional domain semantics not present here.

## 7. Dedup / ownership audit

| Surface | Existing ownership | Weighted-energy relation | Verdict |
|---|---|---|---|
| T3 Typed Incidence Circuit | signed cycle/cocircuit, cut, path-defect certificates | `ker B` circulation structure can be certified by T3; positive `C`, orthogonal projection, Dirichlet/Thomson minimization are extra | reuse T3 for structural cycle/cut witnesses; do not rename T3 as energy |
| T4 Finite Fiber Capacity / Collision-Minima | fiber capacity/collision counts | no quadratic positive-form semantics | no overlap beyond possible source carrier |
| T8 Relation Observable / Spectrum | relation branching/collision spectra; capacity-weighted invariants exist | capacity weighting is not independently a PSD quadratic form or variational energy | no promotion to energy |
| T9 Holonomy / Gluing | route dependence / cocycle / loop transport obstruction | holonomy is typed transport defect, not quadratic energy | strictly distinct |
| sibling Laplacian/chip-firing candidate | expected owner of discrete Laplacian/potential machinery if same weighted contract is accepted | all positive graph energy theorems factor through `B,C,L`, with flow duality and Schur complements as the variational face | preferred placement is Laplacian subtool/extension if contract matches |
| T3 + Laplacian composition | cycle certificates plus weighted operator solve | sufficient for typed circulation witnesses plus weighted minimization | preferred composition route for explicit circuit certificates |

Important ownership conclusion:

The exact positive API is not independent of the weighted Laplacian. It is generated by the same declared weighted incidence data:

`(B,C) -> L=B C B^T`.

The flow side is the dual quadratic problem under `C^{-1}` and the same incidence constraint.

Accordingly, there is no convincing reason in the present evidence to register a sibling global "energy family".

## 8. Sibling Laplacian comparison boundary

The sibling task's positive result was not assumed or read as a premise.

Independent structural comparison gives the following contract split.

### If sibling Laplacian accepts

- weighted signed incidence `B`;
- positive conductance/resistance data;
- potential solve under fixed boundary/source data;
- exact quadratic-form/minimization certificate;
- Schur/reduced-Laplacian semantics;

then this entire graph-energy surface should be classified:

`SUBTOOL_OR_EXTENSION_OF_LAPLACIAN`.

### If sibling Laplacian is narrower

For example, if it accepts only integer chip configurations, legal firing, stabilization, odometers, cokernels, and least-action certificates without positive rational weight / flow-inner-product semantics, then this task identifies a narrower graph-domain weighted variational specialization that may extend that family.

Even in that case, the present packet still does not pass the two-domain gate required for a new global energy family.

Therefore the terminal classification remains:

`DOMAIN_SPECIALIZATION_ONLY`

with preferred future ownership under the Laplacian family.

## 9. Two-domain reuse gate

### Application A — weighted graph path/flow skeleton: ESTABLISHED

The checker establishes:

- exact weighted path Dirichlet minimization;
- exact triangle Thomson minimization;
- gradient/circulation orthogonality;
- effective resistance;
- Kron reduction.

This is one legitimate weighted domain.

### Application B — distinct Enterprise weighted defect/relation system: NOT ESTABLISHED

No second natural domain with independently declared positive quadratic semantics was found in the admissible source packet.

In particular:

- `collapse_incidence.py` has unweighted 0/1 incidence and witness counts and explicitly rejects energy semantics;
- the method inventory contains capacity-weighted relation invariants, but their semantics concern capacity/gcd/translation structure, not a declared PSD quadratic penalty;
- no admissible source supplied an independently meaningful precision-defect squared penalty, reliability metric, conductance, resistance, or chain/cochain inner product.

The taskbook gives examples of what a second domain could look like, but inventing such weights solely to pass the acceptance gate is forbidden.

Therefore:

`SECOND_NATURAL_WEIGHTED_ENTERPRISE_DOMAIN = NOT_ESTABLISHED`.

Consequent downgrade:

`DOMAIN_SPECIALIZATION_ONLY`.

## 10. Classical prior-art discipline

The following mathematical content is classical:

- weighted graph Laplacians;
- graph Dirichlet forms;
- Dirichlet principle;
- Thomson principle;
- electrical-network effective resistance;
- gradient/circulation orthogonality;
- finite-dimensional weighted Hodge-like decomposition;
- Schur complements;
- Kron reduction.

No theorem novelty is claimed.

The Enterprise contribution in this return is limited to:

1. a strict semantic gate separating bare incidence/witness counts from energy;
2. an exact input contract for when quadratic-energy terminology is legal;
3. exact obstruction cases;
4. an exact rational regression checker;
5. ownership/dedup classification against T3/T4/T8/T9 and the Laplacian candidate;
6. refusal to manufacture a second weighted domain.

Therefore:

`DECLARED_WEIGHTED_ENERGY_INTERFACE != NATIVE_ENERGY_PRIMITIVE`.

## 11. API classification

The taskbook's candidate API is classified as follows.

| API | Status | Exact boundary |
|---|---|---|
| `VALIDATE_WEIGHTED_INCIDENCE` | supported in domain specialization | must verify signed incidence typing and positive weights for positive theorems |
| `BOUNDARY` / `COBOUNDARY` | existing incidence structure / T3-adjacent | not energy by itself |
| `WEIGHT_MATRIX` | supported | explicit `C` or `C^{-1}` semantics required |
| `DIRICHLET_ENERGY(u)` | supported | positive weighted graph contract |
| `FLOW_ENERGY(j)` | supported | positive resistance inner product required |
| `LAPLACIAN_FROM_ENERGY` | supported | `L=B C B^T` in symmetric graph mode |
| `GRADIENT_FLOW` | supported | `j=-C B^T u` |
| `CIRCULATION_SPACE` | reuse T3 / exact `ker B` | no weight needed to define the space |
| `ORTHOGONAL_DECOMPOSE` | supported | requires positive resistance inner product |
| `DIRICHLET_MINIMIZER` | supported | boundary pinning / `L_II` invertibility |
| `THOMSON_MINIMIZER` | supported | feasible component-balanced source |
| `MIN_ENERGY_CERT` | supported | Euler-Lagrange + orthogonality exact certificate |
| `EFFECTIVE_RESISTANCE` | supported only in network-like weighted semantics | not from bare incidence |
| `KRON_REDUCE` | supported | exact Schur invertibility / boundary semantics |
| `OBSTRUCTION` | supported | zero/negative/nonsymmetric/singular/missing-semantics cases |

This API is not registered as a new global family.

## 12. Final theorem/status ledger

| Claim | Status |
|---|---|
| bare incidence determines energy | REFUTED |
| overlap Gram witness count is automatically Dirichlet energy | REFUTED |
| positive weighted graph incidence defines a PSD Dirichlet form | PROVED |
| connected positive graph potential kernel is constants | PROVED |
| disconnected positive graph kernel dimension equals component count | PROVED |
| orientation invariance | PROVED |
| exact polarization under characteristic != 2 | PROVED |
| Dirichlet fixed-boundary minimizer | PROVED WITH PINNING CONDITIONS |
| Thomson fixed-source minimizer | PROVED WITH FEASIBILITY CONDITIONS |
| gradient/circulation orthogonal decomposition | PROVED WITH POSITIVE INNER PRODUCT |
| effective resistance | SUPPORTED ONLY WITH NETWORK WEIGHT SEMANTICS |
| Schur/Kron reduction | PROVED WITH INVERTIBILITY CONDITIONS |
| negative weights preserve positive energy | REFUTED |
| zero weights preserve connected-kernel theorem | REFUTED |
| nonsymmetric interaction is automatically an energy operator | REFUTED |
| minimum-energy flow is a native shortest path | REFUTED |
| finite quadratic form is automatically thermodynamic/physical energy | REFUTED |
| second natural Enterprise weighted domain exists in admissible packet | NOT ESTABLISHED |
| new global weighted-energy family passes acceptance gate | REJECTED |
| preferred ownership under matching Laplacian contract | SUBTOOL_OR_EXTENSION |
| strongest frozen terminal classification | DOMAIN_SPECIALIZATION_ONLY |

## 13. Required artifacts

Created:

1. `research_notes/TOOL_DISCOVERY_WEIGHTED_INCIDENCE_ENERGY_DIRICHLET_RESULT_20260823.md`
2. `scripts/tool_discovery_weighted_incidence_energy_dirichlet_check.py`

Optional reusable source module:

`NOT CREATED`.

Reason:

The acceptance gate for a new global tool family was not met, so creating a reusable source module would prematurely harden a domain specialization into a separate tool surface.

## 14. Freeze

Hard target:

`ENTERPRISE_WEIGHTED_INCIDENCE_ENERGY_TOOL_CLASSIFIED`

Status:

`CLOSED`.

Frozen terminal classification:

`DOMAIN_SPECIALIZATION_ONLY`.

Preferred dedup placement if/when the sibling Laplacian contract matches:

`SUBTOOL_OR_EXTENSION_OF_LAPLACIAN`.

Permanent semantic no-go:

`BARE_INCIDENCE != ENERGY`.

Stop condition reached. No separate energy family is created.
