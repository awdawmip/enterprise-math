# X6 r424 — Exact one-step future split of calibrated positive-path orbits

Date: 2026-11-20. Status: **author-side mathematical theorem**; a finite signed-frame and positive native-coordinate path result, not a complete native triadic/Cell-Port/time rotation law, an independent Native Review, or Native Result admission.

## Provenance and scope

New derivation in the existing RESEARCH_DRIVER logical mathematical line `EM-DVR-DEBB5E`, immediately from its already Source-published r423 (`enterprise-math@9af7cca8ab1c62471c6da1c446a7843956cb562a`), and r422 (`@706fdc60b44686c1ffa0dadd32ccd25883339196`). Preserve the separate original X6 research-author credits and r421 signed-group definitions. The primitive coordinate adjacency `T_j^+(z)=z+e_j` is Source-defined in `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` at task-fixed `a72226e2430ffa4786321ac86e7f0c599d5f0389` (blob `d5afee11cea0ace14a11f984e6374a95d399a953`). Group-orbit identification remains an abstract observer candidate, not physical native rotation admission.

## Exact theorem

Use the r423 symbols: positive count vector `c∈N_0^6`, all words `W_c` having those exact positive-axis occurrence multiplicities, a positive calibration suffix `s` with set of fixed axes `S`, and one of `G∈{B6, G_S, G_+, G_A, D}`. Let `F_G(c,S)` be the uniform restricted observer-fiber size from r423.

For an **identically appended future primitive positive step** `e_j`, inserted immediately *before* the fixed calibration suffix, define

```
O_G(u)       = [u s]_G,
O_G^j(u)     = [u e_j s]_G   (u∈W_c).
```

The new future observation refines the initial orbit partition. More exactly, every initial fiber splits into precisely

```
R_G(c,S;j) = F_G(c,S) / F_G(c,S ∪ {j})
```

distinct possible probed observations, all with the same multiplicity `F_G(c,S∪{j})`. Consequently the **sharp extra fixed-length information needed to predict this single common future probe from the initial observation** is

```
b_future_one_step(G,c,S;j) = ceil(log2 R_G(c,S;j)).
```

The factor `R_G` is always an integer. If `j∈S`, then `R_G=1`. If `j∉S` and `c_j=0`, a particularly sharp classification follows:

- `B6`, `G_S`: `R=1` always;
- `G_+`: `R=2` iff exactly **one** axis is absent from both history and suffix (`r=1`) and the uncalibrated equal-positive-count permutation group is nontrivial (`P>1`); otherwise `R=1`;
- `G_A`, `D`: `R=2` iff exactly **two** axes are absent from both history and suffix (`r=2`) and `P>1`; otherwise `R=1`.

This is a one-bit *future* parity witness, despite the probed axis being absent from the old history.

For a used uncalibrated axis (`j∉S,c_j=t>0`), let `m_t=#{i∉S:c_i=t}`. Then `P'=P/m_t` and `r'=r`; the displayed universal ratio evaluates the exact split without special cases. In the unrestricted full-permutation cases the split is `R=m_t`. A parity-restricted two-element class with no invisible parity compensator can instead have `R=1`, even when `m_t=2`.

### Proof

For `u,v∈W_c`, an equality `[u e_j s]_G=[v e_j s]_G` gives a *single* group element `g` that maps the ordered concatenated word to the other. Since the final future letter is literally the same positive `e_j` in both words, the same element must fix `e_j`; it also fixes every letter of `s`. Hence
`[u e_j s]_G=[v e_j s]_G` iff `[u(e_j s)]_G=[v(e_j s)]_G`, which by r423 is exactly the restricted orbit equivalence induced by the stabilizer of `S∪{j}`.

This subgroup is nested inside the original suffix stabilizer, so it refines each initial equivalence class. r423 proves both partitions have uniform fiber sizes `F_G(c,S)` and `F_G(c,S∪{j})`; each original fiber is a disjoint union of their smaller fibers. Therefore the exact number of distinct future classes inside one initial class is their integer ratio. Information-theoretic necessity is by the pigeonhole principle; assigning one tag to each of these classes is sufficient and achieves the fixed-width bit bound. For `c_j=0`, calibrating `j` decreases the number `r` of invisible axes by exactly one and leaves `P` unchanged; substituting the r423 parity formulas gives the sharp listed cases. QED.

## Concrete original-history pairs distinguishable by one native coordinate step

1. **Unique invisible axis / determinant-positive candidate `G_+`.**
   Let `c=(1,1,1,1,1,0)`, `S=∅`, `u=e1 e2 e3 e4 e5` and `v=e2 e1 e3 e4 e5`. Initially `u~v` in `G_+` via the odd transposition (12) together with a sign flip on the *unseen* axis 6. But `u e6` and `v e6` cannot be related in `G_+`: all six axes now appear positive, so no sign flip remains to compensate the odd permutation. Initial fiber 120, future fiber 60, split `R=2`: **one exact parity bit becomes visible**.

2. **Two invisible axes / even-permutation candidate `G_A` (also `D`).**
   Let `c=(1,1,1,1,0,0)`, `S=∅`, `u=e1 e2 e3 e4`, `v=e2 e1 e3 e4`. Initially `u~v` via even permutation (12)(56), which balances its parity on two unseen axes. Appending the common `e5` forces axis 5 fixed; with only axis 6 unobserved, the transposition (12) is no longer realizable in `G_A` or `D`. Initial fiber 24, future fiber 12, again `R=2`.

Both appended positive steps are legal **coordinate adjacency words** under the frozen spatial torsor. The counterexamples show that the corresponding *candidate static orbit quotient* is not a congruence for a fixed-labelled one-step continuation. They do not assert that these full words satisfy a native three-force event law.

## Independent exact checks and relation to earlier work

For the two witnesses, exact enumeration of all `6!·2^6=46,080` signed permutations confirms the five-group before/after fiber sizes:

| c, suffix, future | B6 | GS | G+ | GA | D |
|---|---:|---:|---:|---:|---:|
| five positive distinct axes; append unseen e6 | 120→120 | 120→120 | 120→60 | 60→60 | 60→60 |
| four positive distinct axes; append unseen e5 | 24→24 | 24→24 | 24→24 | 24→12 | 24→12 |
| counts (2,2,3,3,4,4); append used e1 | 8→4 | 8→4 | 4→2 | 4→2 | 4→2 |

The group proof establishes the complete formula for every `c,S,j`; these exact samples corroborate the sharpness witnesses. Unlike r418's unrestricted **common universal future probe** or r417's abstract future-equivalence DFA, r424 gives an exact *one-step refinement factor* for a fixed occurrence-vector path family with invisible-axis parity reservoirs.

For native transfer, the Source must specify whether the reference-frame group is a permitted **passive observer symmetry** or an **active transition**, and which Cell/Port/branch/time fields the observer carries. When the observer retains a fixed labelled future command `T_j^+`, the above algebra gives a precise no-collapse witness for the candidate orbit quotient, without changing the P000 spatial or triadic axioms.

Persistence/admission: author-side proof only. New Native Result accepted 0; formal Task closed 0; mother objective closed 0. Independent Native Review and Source/Activity association pending.