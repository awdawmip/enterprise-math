# Phase B — Exact theorem comparison of the frozen P0/P1 weak bridge

Researcher-ID: `EM-NTP1B-911AF5`
Task: `RS-NATIVE-TRISECTOR-P0P1-ARITHMETIC-BRIDGE`
Publication: `TP2-BD39D919E5642BECBE87`

Status: `PHASE_B_FROZEN / PRIMARY_VERDICT_WEAKER_FOUNDATION_BRIDGE`

## 0. Predecessor Phase-A authority

The authoritative Phase-A freeze pre-existed this continuation on `main`:

`research_returns/NATIVE_TRISECTOR_P0P1_ARITHMETIC_BRIDGE_FOUNDATION_GENERATIVITY_RETURN_20260826.md`

blob `87d5d961e5f87f882bee86337e366f4c89979658`.

It froze, before theorem-side comparison:

- the P0/P1 trace grade `g(T_{a,b})=a+b`;
- sector shells `Sigma_r^(ij)`;
- the glued global shell cardinality `|Sigma_r^E|=3r` for `r>=1`;
- active-axis swap involution `tau_ij`;
- even-shell fixed trace `T_{m,m}`;
- odd-shell unordered central pair `{T_{m,m+1},T_{m+1,m}}`;
- realization multiplicity `binom(r,a)`, envelope `K_r`, and parity defect `beta_r=r mod2`;
- the exact obstruction to one distinguished global balance lane and to an ordered member of the odd central pair.

The present Phase B preserves that freeze and compares it to the admitted theorem package without back-editing Phase-A premises.

## 1. Theorem-side objects compared

After the Phase-A freeze, the admitted theorem package and supporting exact shell theorem were opened.

At `s=3`, the theorem-side shell allocator has:

- three cyclic half-open blocks, each of length `r`;
- total shell cardinality `3r`;
- consecutive shell serialization with base `B_r=1+3r(r-1)/2`;
- a designated central block `sigma_*=1`;
- central side position `t=h+ceil(r/2)`;
- central filament `F_3(H,r)=H+(3r^2+eps(r))/2`;
- longitudinal breaker classification and breaker-coprime capacity from that filament;
- an even-shell transverse readout whose `h=0`, `r=2m` point is the equal-coordinate midpoint and whose C3 unfolding is the bouquet `6m^2-2m+1, 6m^2+1, 6m^2+2m+1`.

## 2. Exact recovery table

| theorem-side role | frozen native P0/P1 object | Phase-B status |
|---|---|---|
| `s=3` shell size `3r` | glued transition shell `Sigma_r^E`, `|Sigma_r^E|=3r` | `EXACT_CARDINALITY_RECOVERY` |
| three length-`r` shell blocks | three sector trace paths with shared-axis endpoint deduplication | `EXACT_UNPOINTED_BLOCK_FAMILY / SERIALIZATION_NOT_NATIVE` |
| parity scalar `eps(r)` | `beta_r=r mod2` | `EXACT_SCALAR_RECOVERY` |
| even-shell central position `r=2m,t=m,h=0` | unique `tau_ij` fixed trace `T_{m,m}` | `EXACT_LOCAL_CENTRAL_POINT_RECOVERY` |
| odd-shell `t=ceil(r/2)` | unordered native pair `{T_{m,m+1},T_{m+1,m}}` | `EXACT_POINTING_OBSTRUCTION` |
| global named central block `sigma_*=1` | three-lane/sector torsor | `EXACT_GLOBAL_SELECTOR_OBSTRUCTION` |
| consecutive integer label `N_3(r,t,sigma)` | no Phase-A native serialization | `MODEL_SPECIFIC_N1_N2_READOUT` |
| central filament scalar after serialization | native shell growth + native central-set skeleton | `CONDITIONAL_EXACT_RECOVERY_AFTER_READOUT` |
| even-shell C3 bouquet carrier | three native sector balance fixed points at `r=2m` | `EXACT_CARRIER_RECOVERY / INTEGER_LABELS_CONDITIONAL` |
| Joukowski lane polynomials / extremal saturation | no native polynomial-label map | `MODEL_SPECIFIC_READOUT` |
| universal breaker `q_b` | no P0/P1 breaker relation | `NOT_DERIVED` |
| breaker capacity `k_*=2q_b-1` | no same-strength native capacity relation | `NOT_DERIVED` |

## 3. Shell allocator: exact native quotient, not exact theorem serialization

The theorem's native specialization has three half-open blocks of length `r`, hence exactly `3r` positions.

The frozen Phase-A bridge independently derives the same shell size from three sector-local trace shells of `r+1` points by deduplicating the three shared physical axis traces:

`3(r+1)-3 = 3r`.

Moreover, each local shell is naturally the finite trace chain

`T_{0,r},T_{1,r-1},...,T_{r,0}`

and adjacent sector chains share their axis endpoints. Thus the glued native shell supplies the theorem's **unpointed three-block shell skeleton**.

What it does not supply at P0/P1 strength is the theorem's block-by-block consecutive integer serialization, its choice of which cyclic block is `sigma=0,1,2`, or an absolute first integer label.

Therefore:

`NATIVE_SHELL_SKELETON = DERIVED`;

`THEOREM_SERIALIZED_SHELL_ALLOCATOR = CONDITIONAL_READOUT`.

## 4. Quadratic shell-growth term is explained natively

From the exact native shell cardinality,

`sum_{u=1}^{r-1} |Sigma_u^E| = sum_{u=1}^{r-1} 3u = 3r(r-1)/2`.

This is exactly the nonconstant cumulative-shell term in the theorem's

`B_r=1+3r(r-1)/2`.

Hence the coefficient `3` and the quadratic shell-growth skeleton are native consequences of the tri-sector trace bridge. The leading `+1` and the interpretation as an absolute consecutive integer label belong to the theorem-side serialization/readout and are not promoted by this equality.

## 5. Central location: exact even-shell recovery

For even grade/shell `r=2m`, Phase A derives a unique active-axis-swap fixed trace

`T_{m,m}`.

The theorem-side cross-route identification independently states that on even shell `r=2m`, the `h=0` central coordinate has

`t=ceil(r/2)=m`

and is exactly the equal-coordinate midpoint of a sector side.

Thus the two constructions coincide at object level:

`P0/P1 BALANCE FIXED TRACE T_{m,m}`

`=`

`THEOREM EVEN-SHELL h=0 EQUAL-COORDINATE CENTRAL POINT`

once the theorem's shell readout is applied.

This is a nontrivial native bridge into the admitted theorem carrier and is why the full task verdict is not `MODEL_SPECIFIC_ONLY`.

## 6. Odd shell: exact point-selector obstruction

For odd shell `r=2m+1`, Phase A derives exactly the unordered central pair

`{T_{m,m+1}, T_{m+1,m}}`.

The active-axis swap `tau_ij` exchanges the two members while preserving every frozen P0/P1 observable and every realization multiplicity.

The theorem serialization instead chooses

`t=ceil(r/2)=m+1`.

Under the swapped presentation this is the opposite member of the native pair. Therefore the theorem's one-sided odd-shell central point is not definable at current P0/P1 strength.

Knowing the native scalar

`beta_r=eps(r)=1`

does not repair this: NSA-13 forbids using scalar invariance to promote an unproved pointed object. The parity bit tells us there are two central members; it does not choose which active component receives the extra unit.

This gives the exact obstruction:

`ODD_SHELL_ORIENTED_CENTRAL_FILAMENT_SECTION_NOT_P0P1_DEFINABLE`.

## 7. Why this blocks the full longitudinal breaker bridge

The theorem's longitudinal filament is

`F_3(H,r)=H+(3r^2+eps(r))/2`

on all shell parities, and the first-breaker classification/capacity is a theorem about that serialized one-dimensional integer family.

The frozen native bridge determines:

- shell grade `r`;
- coefficient `3` through shell growth;
- parity `eps(r)` as a scalar;
- the central object uniquely on even shells;
- only an unordered central pair on odd shells.

It does **not** determine the one-sided odd-shell section or the absolute consecutive integer serialization needed to obtain that exact integer sequence from P0/P1 alone.

Consequently the universal-breaker object and its `k_*=2q_b-1` capacity do not descend to current P0/P1 at the same semantic strength.

This is not a claim that no future native breaker construction exists. It is an exact obstruction to the current theorem-side bridge as presently typed.

## 8. Even-shell transverse carrier survives the obstruction

The theorem's exact C3 bouquet/filament identification uses only even shells `r=2m` and the `h=0` equal-coordinate midpoint. On this locus the native balance point is unique, so the odd-shell selector obstruction disappears.

Therefore the frozen bridge gives an exact native carrier for the theorem's transverse even-shell central locus.

After adding the theorem's explicit consecutive integer serialization/readout, this carrier maps exactly to

`6m^2-2m+1`,

`6m^2+1`,

`6m^2+2m+1`.

The integer polynomial labels and their Joukowski/divisibility analysis remain model/readout layer; the **equal-coordinate C3 carrier locus** is the native consequence.

This is a second nontrivial portion of the admitted closure reached by the weaker bridge.

## 9. Breaker/capacity mismatch and the tempting `9`

Phase A has two native counting scalars that might be confused with theorem capacity:

- realization multiplicity envelope `K_r=binom(r,floor(r/2))`;
- global shell cardinality `|Sigma_r^E|=3r`.

Neither is the theorem's breaker-coprime capacity.

In particular `|Sigma_3^E|=9` is an exact integer coincidence, but no native theorem relates shell grade `3` to breaker channel `q_b=5` or identifies shell cardinality with the maximal breaker-coprime run. Promoting this coincidence would violate same-semantic-strength admissibility.

Freeze:

`NATIVE_SHELL_9 != THEOREM_BREAKER_CAPACITY_9 AS_SEMANTIC_OBJECTS`.

Likewise `K_r` is a path-realization fiber count and no equality with `2q_b-1` is established.

## 10. Dependency map after exact comparison

```text
CURRENT P0/P1
  |
  +-- three sectors + trace composition
  |      -> grade shell Sigma_r^E
  |      -> |Sigma_r^E|=3r
  |      -> cumulative 3r(r-1)/2
  |
  +-- active-axis swap tau
  |      -> even fixed trace T_{m,m}
  |      -> odd unordered central pair
  |      -> beta_r = r mod 2
  |
  +-- exact native weak bridge
         |
         +--> theorem shell skeleton at s=3            [EXACT QUOTIENT/CARRIER]
         +--> even h=0 equal-coordinate central point  [EXACT]
         |
         X--> named global block sigma_*=1             [needs torsor section]
         X--> odd oriented member t=ceil(r/2)           [needs side/orientation choice]
         X--> absolute consecutive integer labels      [model/readout]

ADDED THEOREM READOUTS
  -> F_3(H,r) serialized filament
  -> hyperbola/Joukowski finite-field structures
  -> breaker q_b and capacity k_*
  -> extremal 5,7 and closure 9,35,105,53
```

The dependency direction stays one-way. The successful arithmetic theorem constrains/validates the weak bridge but is not copied back into P0/P1 premises.

## 11. Minimality

The weakest currently identified additions are separated by role:

1. **global shell pointing** — one section of the three-sector/block torsor if a named `sigma_*` object is required;
2. **odd local orientation** — one choice distinguishing the two members of every odd central pair, coherently under shell transport, if the exact `ceil(r/2)` longitudinal filament is required;
3. **serialization readout** — a shell-by-shell/block-by-block consecutive integer ranking with absolute normalization if the theorem's exact integer labels are required;
4. **breaker semantics** — an independently defined native relation/functional if `q_b` and `k_*` are to be promoted beyond conditional theorem readouts.

The first two are genuine choice/pointing data absent from the frozen P0/P1 bridge. The third is an N1/N2-style arithmetic readout. The fourth is a stronger semantic object not supplied by counting coincidences.

## 12. Primary verdict

Freeze exactly one task-level primary verdict:

`WEAKER_FOUNDATION_BRIDGE`.

Reason:

- a genuine native P0/P1 bridge exists independently of theorem-side formulas;
- it recovers the exact `3r` shell skeleton, parity scalar, and even-shell `h=0` equal-coordinate central carrier used by the admitted theorem;
- these are nontrivial theorem-facing consequences, so `MODEL_SPECIFIC_ONLY` is too weak;
- the bridge does not recover the full pointed/serialized longitudinal filament or breaker/capacity semantics, so `DERIVED_NATIVE_BRIDGE` is too strong;
- exact selector obstructions exist for the stronger objects, but they do not kill the surviving invariant shell/balance bridge, so the most informative task-level verdict is the explicitly permitted weaker-bridge outcome rather than collapsing the entire task to `EXACT_DEFINABILITY_OBSTRUCTION`.

No Foundation promotion or mutation follows automatically.
