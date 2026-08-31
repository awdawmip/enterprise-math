# R041 — Native Surface Horizon Quotient Calculus: First Semantic Checkpoint

Status: `IN_PROGRESS / BEHAVIORAL_KERNEL_FROZEN / FIRST_COMPACT_OPERATIONAL_REDUCTION / NOT_CANONICAL`  
Researcher-ID: `EM-R041-7C3A91`  
Task: `RS-R041-NATIVE-SURFACE-HORIZON-QUOTIENT-CALCULUS`  
Source taskbook base: `39e9cccb6d30a31e9e5c567414637eb6b03a4599`  
Frozen dependency: R039 Draft PR #524 head `c484fb85385b8498982aaa939171957588c836d7`  
CI: `CI_NOT_REQUIRED_FOR_RESEARCH`

## 0. Checkpoint verdict

R041 starts by separating three objects that were easy to conflate after R039:

1. **exact-h terminal answer quotient** — only the set of terminal `S` values at one exact depth matters;
2. **cumulative/nested future quotient** — all depths `0..h` matter, so horizon extension must refine the kernel;
3. **branch-aware operational quotient** — the state must expose enough successor structure to continue exact execution.

The first exact search already gives two strict negative boundaries:

- exact-h terminal quotients are **not** monotone in `h`; equality at `h+1` need not imply equality at `h`;
- terminal sufficiency is strictly weaker than operational sufficiency, already at very small FCC/HCP clusters.

A new structural positive result also survives:

> R039's full exterior cone `J_h` stores more incidence than any `h`-step addition-only surface trajectory can see.  All edges internal to the last operational layer `L_{h-1}` are dead for horizon `h`, and the explicit layer tags are reconstructible.  Removing both yields a strictly smaller exact operational carrier `K_h`.

For the one-cell cluster, the induced-edge reduction is substantial:

| world | h | `J_h` edges | `K_h` edges | removed |
|---|---:|---:|---:|---:|
| FCC | 1 | 24 | 0 | 24 |
| FCC | 2 | 204 | 108 | 96 |
| FCC | 3 | 648 | 432 | 216 |
| FCC | 4 | 1476 | 1092 | 384 |
| HCP | 1 | 24 | 0 | 24 |
| HCP | 2 | 216 | 108 | 108 |
| HCP | 3 | 684 | 444 | 240 |
| HCP | 4 | 1560 | 1128 | 432 |

No minimality claim is made for `K_h`; it is the first strict structural reduction of `J_h` in this task.

---

## 1. Frozen typed signatures

Let `T_h(C)` be the Boolean support of absolute terminal surface values after **exactly** `h` legal additions.

Let

`CT_h(C) = (T_0(C), T_1(C), ..., T_h(C))`

be the cumulative terminal signature.

For the branch-aware Boolean operational language, use attachment count `k` as the action label; this is equivalent to the surface increment because

`Delta S = 12 - 2k`.

Define recursively

`B_0(C) = (S(C),)`

and

`B_{h+1}(C) = ( S(C), { (k_C(x), B_h(C union {x})) : x in F(C) } )`,

where the braces are Boolean set semantics.  Multiplicity/provenance variants are deliberately not identified with this carrier.

For any declared signature `Sigma`, the exact behavioral relation is

`C ~_Sigma D  iff  Sigma(C)=Sigma(D)`.

Its quotient is definitionally the coarsest exact answer quotient for that declared language.  The nontrivial research question is whether this kernel admits a smaller structural/updateable realization than an explicit future table.

### R041-T1 — nested-language horizon refinement

If the future language at horizon `h` is literally included in the language at horizon `h+1`, then

`~_{h+1} subseteq ~_h`.

For cumulative terminal signatures this is immediate because `CT_h` is a projection of `CT_{h+1}`.

**Scope correction:** this theorem does **not** apply to raw exact-h terminal languages `T_h`, because `T_h` is not a projection of `T_{h+1}`.

---

## 2. Exact-h terminal quotients can coarsen again

### R041-CE1 — FCC same `T_3`, different `T_2` at `N=4`

The FCC clusters

```text
A=((0,0,0),(0,1,-3),(1,0,-1),(1,1,-2))
B=((0,0,0),(0,1,-1),(1,-1,0),(2,-1,1))
```

have the same current surface

`S(A)=S(B)=42`

and the same exact three-addition terminal support

```text
T_3(A)=T_3(B)
={58,60,62,64,66,68,70,72},
```

but

```text
T_2(A)={52,54,56,58,60,62}
T_2(B)={54,56,58,60,62}.
```

Thus equality at exact horizon three does not recover exact horizon two.

### R041-CE2 — HCP same `T_2`, different `T_1` at `N=4`

Under the frozen R039 HCP implementation,

```text
A=((0,0,0),(0,0,1),(0,1,0),(1,1,0))
B=((0,0,0),(0,0,1),(0,0,2),(0,1,0))
```

satisfy

`S(A)=S(B)=40`,

```text
T_2(A)=T_2(B)={50,52,54,56,58,60},
```

but

```text
T_1(A)={44,46,48,50}
T_1(B)={46,48,50}.
```

The HCP crystallographic completeness caveat inherited from R039 remains in force; this is exact relative to the frozen contact/symmetry implementation.

### Consequence

“Horizon precision increases with h” is only meaningful after the future languages have been nested by construction.  Exact-depth answer quotients can refine, coarsen, or cross as `h` changes.

The bounded class counts make the point visible without any witness selection.  At FCC `N=4`:

```text
#T_2 classes = 10
#T_3 classes = 9
#CT_2 classes = 12
#CT_3 classes = 14
```

So exact-depth class count decreases while the cumulative nested quotient correctly refines.

---

## 3. Terminal sufficiency is not operational sufficiency

### R041-T2 — canonical branch-aware operational signature

For the declared Boolean surface-trajectory language, `B_h` is recursively executable by construction: choosing a stored `(k, child)` branch emits `Delta S=12-2k` and leaves the exact remaining `B_{h-1}` state.

Conversely, any exact branch-aware representation for this same typed language must distinguish states with different `B_h` signatures.  Thus equality of `B_h` is the exact depth-`h` behavioral kernel for this branch-aware operational semantics.

This is a standard finite-depth transition-system/bisimulation-style construction; R041 does not claim novelty for the generic construction.  The project-specific content is the native-surface specialization, exact witnesses, structural carriers, and correlation/storage gap.

### R041-CE3 — FCC terminal/operational gap at `N=3,h=2`

```text
A=((0,0,0),(0,1,-1),(1,-1,0))
B=((0,0,0),(0,0,2),(0,1,1))
```

satisfy

```text
S(A)=S(B)=32
T_1(A)=T_1(B)={38,40,42}
T_2(A)=T_2(B)={44,46,48,50,52},
```

but

`B_2(A) != B_2(B)`.

The difference is successor correlation: the union of two-step terminal answers is identical, but the answer set available after a **particular first attachment class** is not.

Exhaustive FCC search through `N<=3` finds no smaller-cluster witness; `N=1,2` each have only one symmetry class.

### R041-CE4 — HCP terminal/operational gap already at `N=2,h=2`

The two frozen HCP `N=2` classes

```text
A=((0,0,0),(0,1,0))
B=((0,0,0),(0,0,1))
```

have

```text
S=22
H=((1,14),(2,4))
T_1={30,32}
T_2={36,38,40,42}
```

in common, but

`B_2(A) != B_2(B)`.

Thus the basal/interlayer memory that R039 saw in the local alphabet is invisible to two-step terminal support yet visible to recursive execution.  `N=2` is the first nontrivial HCP size, so this is cluster-size minimal under the frozen model.

---

## 4. Order-free terminal contact-score factorization

R039-T8 already proved, for a final added set `A`,

`S(C union A)-S(C)=12|A|-2(E(C,A)+E(A))`.

R041 packages the exact terminal information as the **contact-score spectrum**

`Omega_h(C) = { E(C,A)+E(A) : |A|=h, C union A connected }`.

Then

`T_h(C) = { S(C)+12h-2q : q in Omega_h(C) }`.

This gives three different precision objects immediately:

- exact-h terminal support: `T_h` itself is the coarsest answer token;
- current+terminal language: `(S, Omega_h)` is an exact factorizing carrier;
- best-only language: only `max Omega_h = Lambda_h` is needed.

So the same native surface state has different coarsest quotients for `terminal support`, `best`, and `operational trajectory`; none is the absolute “surface precision”.

---

## 5. `J_h` has horizon-dead incidence

Recall R039's exterior layers

```text
L0(C)=F(C)
L_{r+1}(C)=N(L_r) minus C minus earlier layers.
```

`J_h` stores the induced contact graph on `L0 union ... union L_{h-1}`, layer tags, and initial `k_C` on `L0`.

### Lemma 5.1 — activation depth

A cell in `L_r` needs at least `r+1` additions before it can be occupied.

- lower bound: one legal addition can advance the occupied component by at most one exterior layer;
- upper bound: a contact path from `L0` to that cell gives a legal order of length `r+1`.

Hence a cell in `L_{h-1}` can occur only as the **last** addition of an `h`-step trajectory.

### Lemma 5.2 — last-layer internal edges are invisible

No legal trajectory of length at most `h` can contain two occupied vertices from `L_{h-1}`.  Therefore an edge with both endpoints in `L_{h-1}` can never contribute to

- legality of a selected prefix; or
- the attachment count of any selected cell within the declared horizon.

All such edges may be deleted.

### Lemma 5.3 — layer tags are reconstructible

After deleting only `L_{h-1}`-internal edges:

- `L0` is exactly the set of vertices with positive initial weight `k_C`;
- for every remaining vertex, its layer is its graph distance from `L0` in the retained exterior graph.

The deleted edges are same-layer edges at maximal depth and lie on no shortest path needed to establish the layer of a vertex.

### R041-T3 — activation-pruned operational cone `K_h`

Define `K_h(C)` to retain only:

1. `S(C)` when absolute `S` is observed;
2. vertices `L0 union ... union L_{h-1}`;
3. initial weights `k_C(x)` on `L0` and zero on deeper vertices;
4. all exterior contact edges **except** edges internal to `L_{h-1}`.

Do not store explicit layer tags.

Given a chosen prefix `A_t`, compute

`k_t(x)=k_C(x)+#{y in A_t : y~x}`.

By Lemmas 5.1–5.3, every edge that can contribute to this formula before the horizon is retained, every legal candidate through the horizon is present, and no deleted edge can ever be queried.  Therefore `K_h` reproduces the exact legal transition relation and all `S` trajectories through horizon `h`.

So

`J_h -> K_h -> B_h`

are exact factor maps for the declared addition-only Boolean surface trajectory language.

`K_h` is strictly smaller than `J_h` whenever `L_{h-1}` contains an internal edge.  The singleton FCC/HCP counts in §0 certify strictness for `h=1..4`.

This theorem does **not** extend to deletion legality, provenance semantics, or horizons larger than the declared `h`.

---

## 6. Bounded quotient class counts

These counts are exact under the frozen symmetry implementations.  They measure semantic class count, not serialized bytes.

### FCC

| N | states | S | H | R2bar | T1 | T2 | T3 | CT2 | CT3 | B1 | B2 | B3 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | 4 | 2 | 4 | 4 | 3 | 3 | 4 | 3 | 4 | 3 | 4 | 4 |
| 4 | 20 | 4 | 17 | 20 | 9 | 10 | 9 | 12 | 14 | 9 | 17 | 20 |
| 5 | 131 | 5 | 67 | 131 | 19 | 18 | — | 29 | — | 19 | 69 | — |

Two immediate lessons:

- at `N=5`, one-shot `T_2` needs only `18` classes while `R2bar` distinguishes all `131` states;
- the branch-aware operational `B_2` needs `69` classes — much richer than terminal `18`, but still far below `R2bar=131` in class count.

Thus R039's `R2bar` is an exact constructive sufficient statistic for its declared task, not a minimal horizon-2 quotient.

### HCP

| N | states | S | H | R2bar | T1 | T2 | CT2 | B1 | B2 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 2 |
| 3 | 9 | 2 | 7 | 9 | 4 | 5 | 5 | 4 | 7 |
| 4 | 57 | 4 | 29 | 57 | 10 | 10 | 14 | 10 | 33 |

HCP `N=2` is especially sharp: terminal semantics collapses the two embeddings completely, while operational depth two separates them.

---

## 7. R039 regression status

This checkpoint consumes rather than redoes R039.

| R039 object | R041 classification at this checkpoint |
|---|---|
| `S` | current scalar only; known one-step unsafe |
| `H` | one-step multiplicity carrier; not generally operational for longer horizons |
| `R2bar` | two-step terminal sufficient; empirically very nonminimal in bounded class count; known N=6 non-Markov / horizon-4 kill |
| `Lambda_h` | exact `Fh-best` score via `max Omega_h` |
| `J_h` | fixed-h operational sufficient, but now proven structurally reducible to `K_h` |
| `K_h` | R041-new strict operational reduction; minimality open |
| `B_h` | canonical branch-aware behavioral signature for the declared Boolean surface-trajectory semantics |

R039's FCC N=6 same-`R2bar` / different `T_4` witness remains a mandatory regression and is not superseded by the smaller terminal-vs-operational witnesses above.

---

## 8. Hypothesis dispositions after pass 1

- `H1 HORIZON_REFINEMENT`: **NARROWED / PROVED FOR NESTED LANGUAGES / FALSE FOR RAW EXACT-h**.
- `H2 TERMINAL_VS_OPERATIONAL_GAP`: **POSITIVE**, with FCC `N=3,h=2` and HCP `N=2,h=2` witnesses.
- `H3 FINITE_EXTERIOR_CONE_SUFFICIENCY`: **R039 POSITIVE; R041 STRICTLY COMPRESSED** to `K_h`.
- `H4 DEEP_INTERIOR_COLLAPSIBLE`: **POSITIVE in addition-only fixed-h scope**, inherited from R039 and strengthened by last-layer edge pruning.
- `H5 STRICT_CORRELATION_HIERARCHY`: **SUPPORTED, not yet globally proved**; `T/B` and R039 `R2` witnesses show multiple strict separations.
- `H6 COMPACT_R3_EXISTS`: **POSITIVE in structural sense**: `K_3` is strictly smaller than full `J_3` and operationally exact.  A much smaller correlation quotient of `K_3` remains open.
- `H7 SURFACE_BRC_SAFE_IFF_FUTURE_SIGNATURE_EQUAL`: **generic Boolean behavioral-kernel direction frozen; surface BRC matrix pending**.
- `H8 PRECISION_COST_PARETO`: **SUPPORTED** by class-count separation; serialized-size/update-cost Pareto still pending.

---

## 9. Prior-art boundary

The generic facts

- “equal declared future signatures” define the coarsest exact answer quotient;
- nested observation languages induce partition refinement;
- the recursive `B_h` object is a finite-depth behavioral/bisimulation-style signature;

belong to standard transition-system / automata semantics.  R041 makes no novelty claim for them.

The R041-specific mathematical residue in this checkpoint is:

1. exact native FCC/HCP witness placement for the typed separations;
2. the exact-h nonmonotonicity correction to the horizon-refinement hypothesis;
3. the surface-specific `J_h -> K_h` activation-budget pruning theorem;
4. exact bounded quotient counts quantifying how much `R2bar` over-resolves terminal/operational behavior.

A literature-rooting pass is still required before any novelty-facing promotion.

---

## 10. Validation

Independent executable: `quotient_engine.py`.

Focused tests: `7/7 PASS`.

Checked mechanically:

- FCC exact-h nonmonotonicity witness;
- HCP exact-h nonmonotonicity witness;
- FCC terminal/operational gap;
- HCP terminal/operational gap;
- `K_h` versus direct trajectory support for FCC/HCP fixtures at `h=1,2,3`;
- singleton FCC/HCP `J_h -> K_h` edge counts for `h=1..4`;
- contact-score factorization.

The machine-readable bounded results are in `CHECKPOINT_RESULTS.json`.

No theorem-critical floating point is used.  No CI/workflow status was queried.

---

## 11. Next frontier

The next pass should not enlarge plain cluster enumeration first.  The highest-value question is now:

> **How far can `K_3` be quotiented while remaining recursively exact?**

Concrete attack order:

1. canonicalize `K_3` as a weighted abstract exterior graph and compare its bounded class count with `B_3`;
2. test whether pairwise frontier-overlap/incidence data suffices to factor `B_3`;
3. if not, extract the first exact collision and identify the minimal triple/shared-future-cell correlation missing from the pairwise carrier;
4. repeat the first failure order in HCP;
5. only then build the state-size/update-cost Pareto and surface-BRC recoalescence matrix.

The provisional answer to the mother question is already sharper:

> **Yes, “precision for future h” can be made exact as a typed behavioral kernel — but there is no single horizon scalar.  Exact-depth terminal, cumulative terminal, and recursively executable precision are different quotients.  In the native surface world, the required relation information can be bounded structurally by an activation-pruned exterior cone, and the first strict correlation debts are now explicit.**
