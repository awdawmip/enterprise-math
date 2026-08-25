# CBRC F5AR — Axiom Countermodel and Ablation Packet

Status: `CHECKPOINT_A_COUNTERMODEL_PACKET`
Date: `2026-08-25`
Researcher-ID: `EM-CBRCF5AR-7E8B04`
Task-ID: `RS-CBRC-F5AR-INDEPENDENT-BRANCH-ONTOLOGY-AXIOM-ADMISSION-REPLICATION`

This packet gives exact finite witnesses for strictness, failed converses, refinement closure, kernel compatibility, signed cancellation and mandatory ablations.

## 1. Toy notation

A rooted refinement tree uses integer old projections on active branch records.

A branch label

`b : p / S / type`

means:

- old projection `p`;
- old-witness support metadata `S`;
- `type=old` if `RefOld(b,w)` is explicitly declared;
- `type=child` if it is only a refinement child and has no inherited direct old-link declaration.

Every active branch in the toy models carries a nonzero enriched coefficient state. Therefore a branch may have `p=0` only by carrying nonzero enrichment-kernel content.

An off-branch kernel state is written

`k != 0, pi(k)=0, k notin B_active`.

Truth vectors are ordered:

`[A0,A1,A2,A3,A4]`.

## 2. M01 — accepted F5R kernel-branch witness

Tree:

```text
r : +1
├── a : +1 / {r} / old
└── b :  0 / empty / old     (enriched state nonzero)
```

Family total is `+1`.

Truth vector:

`[false,false,true,false,false]`.

Uses:

- `A2 !=> A0`;
- `A2 !=> A1`;
- `A2 !=> A3`;
- `A2 !=> A4`;
- total old-coordinate conservation does not close the zero-child loophole;
- nonzero enriched-state survival does not imply nonzero old projection.

This is the F5R independence pattern. The kernel tag is bookkeeping only.

## 3. M02 — exact signed family cancellation

Tree:

```text
r : +1
├── a : +1 / {r} / old
└── b : -1 / {r} / old
```

Truth vector:

`[true,true,false,true,true]`.

Uses:

- `A0 !=> A2`;
- `A1 !=> A2`;
- `A3 !=> A2`;
- `A4 !=> A2`;
- individual branch faithfulness does not imply nonzero descendant-family aggregate.

This is also the smallest witness that an unqualified A2 is not signed-cancellation-neutral.

## 4. M03 — depth-2 loss of faithfulness

Tree:

```text
r : +1
├── a : +1 / {r} / old
│   ├── c : +1 / {r} / child
│   └── d :  0 / empty / child   (enriched state nonzero)
└── b : +1 / {r} / old
```

No hereditary `RefOld` propagation is assumed from `a` to `c,d`.

Truth vector:

`[true,true,true,false,false]`.

Uses:

- `A0 !=> A4`;
- `A1 !=> A4`;
- `D_1 !=> D_2`;
- composition/refinement functoriality is load-bearing for all-depth closure.

Minimality:

A binary depth-2 countermodel must contain root, two first-generation children and two children of one refined branch: 5 tree nodes. Therefore this witness is size-minimal under binary refinement.

## 5. M04 — all-depth projection faithfulness without witness-support metadata

Tree:

```text
r : +1
├── a : +1 / empty / old
└── b : -1 / {r} / old
```

Truth vector:

`[true,false,false,true,true]`.

Uses:

- `A4 !=> A1`;
- `A3 !=> A1`;
- nonzero old projection does not reconstruct concrete witness-support metadata.

The absence of support data is ontological, not a zero coefficient.

## 6. M05 — faithful active branches plus harmless off-branch kernel state

Tree:

```text
r : +1
├── a : +2 / {r} / old
└── b : -1 / {r} / old
```

Off active-branch type:

`k != 0, pi(k)=0`.

Truth vector:

`[true,true,true,false,true]`.

Uses:

- `A1 !=> A3`;
- `A4 !=> A3`;
- A3 is stronger than needed to close F4;
- hidden/kernel enrichment may exist off active branch type while every active old-refining branch remains faithful.

The active pair also conserves the old total:

`2 + (-1) = 1`.

## 7. M06 — global projection reflection without old-support metadata

Tree:

```text
r : +1
├── a : +2 / empty / old
└── b : -1 / empty / old
```

No nonzero kernel state exists.

Truth vector:

`[true,false,true,true,true]`.

Uses:

- `A3 !=> A1`;
- A3 supplies projection nondegeneracy but cannot create witness-support data.

## 8. M07 — recursive conservative extension with kernel retained off type

Tree:

```text
r : +1
├── a : +2 / {r} / old
│   ├── c : +4 / {r} / child
│   └── d : -2 / {r} / child
└── b : -1 / {r} / old
```

Off type:

`k != 0, pi(k)=0`.

Each split conserves old projection:

`2 + (-1) = 1`;

`4 + (-2) = 2`.

Truth vector:

`[true,true,true,false,true]`.

Uses:

- consistency of A0 with total conservation;
- consistency of hereditary all-depth faithfulness;
- exact model showing A3 is unnecessary;
- structural contraction/expansion witness.

Contract the subtree `a -> {c,d}` back to already existing ancestor `a`. A4 remains true and local conservation remains true.

Expand again. A4 remains true.

## 9. M08 — pre-erasure faithful branches with post-erasure exact cancellation

Use two signed old occurrences:

```text
r+ : +1 -> b+ : +1 / {r+} / old
r- : -1 -> b- : -1 / {r-} / old
```

The two branch records may reach the same typed terminal.

Before erasure:

`p(b+)=+1`, `p(b-)=-1`.

Both are faithful.

After marker erasure/recoalescence:

`z = b+ + b-`

has old projection zero.

The resulting zero aggregate is not re-declared as a member of `B_active`.

Uses:

- exact signed cancellation remains legal;
- same-terminal recoalescence does not imply nonzero final support;
- branch faithfulness is a pre-erasure typed condition.

Necessary typing lesson:

If `z` were automatically reclassified as an active retained old-refining branch, A0/A1/A4-style nondegeneracy would conflict with exact cancellation. Therefore marker erasure must terminate the branch-faithfulness domain.

## 10. M09 — minimal `(1,1)` commuting diamond

Canonical path-formal fiber:

```text
w1 = Xi Xj
w2 = Xj Xi
```

They are:

- distinct concrete path witnesses;
- same native component trace `T_(1,1)`;
- same typed terminal cell;
- Path-formal count `2`;
- N multiplicity `2`;
- Boolean terminal support `1`.

This witness is unchanged by every admitted branch-ontology rule in this packet.

The rule acts on the enrichment/marked-branch layer only.

## 11. Complete pairwise nonimplication table

The only strict implications among A0–A4 are:

`A1 => A0`;

`A3 => A4 => A0`.

Every other ordered pair fails.

| Claimed implication | Countermodel |
|---|---|
| A0 => A1 | M04 |
| A0 => A2 | M02 |
| A0 => A3 | M05 |
| A0 => A4 | M03 |
| A1 => A2 | M02 |
| A1 => A3 | M05 |
| A1 => A4 | M03 |
| A2 => A0 | M01 |
| A2 => A1 | M01 |
| A2 => A3 | M01 |
| A2 => A4 | M01 |
| A3 => A1 | M04 or M06 |
| A3 => A2 | M02 |
| A4 => A1 | M04 |
| A4 => A2 | M02 |
| A4 => A3 | M05 |

Strictness of valid implications:

- `A1 => A0` is strict by M04;
- `A4 => A0` is strict by M03;
- `A3 => A4` is strict by M05.

## 12. Finite-depth ladder

For `D_d := nonzero old projection on every active descendant through depth d`:

`D_1=A0`;

`D_{d+1} => D_d`;

`A4 = forall d D_d`.

Smallest binary-comb witness for

`D_d !=> D_{d+1}`

has

`2d+3`

tree nodes.

Construction:

- keep every projection nonzero through depth `d`;
- refine one depth-`d` leaf;
- set one depth-`d+1` child projection to zero;
- keep its sibling nonzero.

Therefore no fixed finite-depth checker establishes A4 as a theorem. The deterministic checker enumerates all ternary projection assignments `{-1,0,+1}` on binary combs through depth 4 only as evidence.

## 13. Necessary and sufficient closure condition

Define local hereditary faithfulness `LHF`:

For every reachable active branch `b` with `p(b)!=0`, every child `c` of every authorized retained refinement of `b` satisfies `p(c)!=0`.

Then on finite refinement trees:

`LHF <=> A4`.

Direction `LHF => A4` is induction on depth.

Direction `A4 => LHF` is obtained by extending any reachable history by one authorized split; the children are leaves of that finite extension.

To derive `LHF` from an A1-style direct old-link rule, add a branch genealogy/root map

`rho : B_active -> W`

with

`Parent(c,b) => rho(c)=rho(b)`,

and require the projection clause on every `rho`-typed active branch.

Without this new functorial data, M03 remains legal.

## 14. Minimal F4 closure theorem

Elementary observable data are two old projections `(p1,p2)`.

Required invariance: branch marker relabeling.

A marker-symmetric rule closes the F4 zero-child loophole iff it excludes all pairs with either coordinate zero.

The weakest such predicate is

`p1 != 0 and p2 != 0`.

Therefore A0 is exactly minimal in the marker-symmetric elementary class.

Counterexamples to weaker properties:

| Weaker property | Passing zero-child witness |
|---|---|
| both enriched outputs nonzero | M01 |
| at least one old projection nonzero | M01 |
| family sum nonzero | M01 |
| total conservation | M01 |
| nonempty old witness support only | modify M01 by attaching `{r}` support to zero branch |
| one named branch must be nonzero | relabel branches in M01 |

## 15. Mandatory ablations

### Ablation 1 — active-branch type restriction

Remove the type restriction and demand nonzero old projection of every nonzero enriched state.

Result: rule becomes A3-like.

M05/M07 fail only because of harmless off-branch kernel state.

Loophole closure: yes.

Conservativity over enriched models: worsens.

Signed cancellation: exact zero aggregate still possible, but nonzero kernel residue after cancellation is forbidden.

Interpretability: overstrong.

### Ablation 2 — concrete-witness support data

Remove `SuppOld(b)!=empty` from A1.

Result: A1 reduces to projection-only `A1pi`.

M04 shows projection faithfulness can hold without support metadata.

Loophole closure: unchanged.

Conservativity/ontology: improves.

Cancellation: unchanged.

Conclusion: support metadata is not load-bearing for F4 closure.

### Ablation 3 — nonzero signed old projection

Keep old-support metadata but remove `p(b)!=0`.

Attach `{r}` to the zero-projection branch in M01.

The support-only rule passes while the F4 pattern survives.

Loophole closure: fails.

Conclusion: this clause is load-bearing.

### Ablation 4 — leafwise closure

Use only A0.

M03 passes A0 and fails at depth 2.

Elementary F4 closure: preserved.

Arbitrary-depth closure: lost.

### Ablation 5 — descendant-family closure

Remove A2-style nonzero family total while retaining per-branch A4.

M02 becomes legal.

Elementary/leafwise loophole closure: preserved.

Signed-cancellation neutrality: improves.

Conclusion: A2 is not load-bearing for branchwise faithfulness.

### Ablation 6 — total old-coordinate conservation

Use elementary projections `(1,1)` for root `+1`.

A0 holds while conservation fails.

Loophole closure: preserved.

Conclusion: conservation is orthogonal.

### Ablation 7 — signed-cancellation compatibility

If compatibility is removed, one may impose A2 or a global post-recoalescence nonzero rule.

M02/M08 are then excluded.

Loophole closure can still hold, but canonical signed completion loses a permitted behavior.

Conclusion: unacceptable ablation.

### Ablation 8 — translation/relabeling covariance

A rule such as “marker `m1` must be nonzero” can pass the original ordering of M01 while ignoring the zero-projection branch.

Swap marker names and the semantic status changes.

Loophole closure: noncanonical / label-dependent.

Conclusion: covariance is load-bearing for minimality.

### Ablation 9 — composition/refinement functoriality

A0 remains true on M03 but the depth-2 branch fails.

Elementary closure: preserved.

A4: lost.

Conclusion: functoriality is exactly what distinguishes restricted admission from all-depth admission.

## 16. Admission packet conclusion

Strongest exact findings:

`A0 = minimal elementary marker-symmetric loophole closer`.

`A0 !=> A4`.

`A1 !=> A4` without hereditary old-link transport.

`A2` does not close the zero-child loophole.

`A3` is unnecessary because M05/M07 close the loophole while retaining off-type kernel states.

`A4` is the all-depth closure schema and requires hereditary refinement ontology or an equivalent local rule.

Recommended admission:

`F5AR_ADMIT_RESTRICTED_ELEMENTARY_RULE_ONLY`.

No rank-two carrier, complex/quadratic structure, phase group, norm, inner product, square law, downstream wave object or F6 answer is used or constructed.
