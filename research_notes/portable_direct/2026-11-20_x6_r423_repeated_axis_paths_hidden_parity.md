# X6 r423 — Exact calibrated orbit fibers for positive paths with repeated axes and invisible parity reservoirs

Date: 2026-11-20. **Author-side proved finite-group theorem, with finite exact spot checks.** This is a scoped extension of r422, not native Cell/Port/time dynamics, independent Native Review, Result admission, or a replacement for P000.

## Provenance and question

Continuation of the original RESEARCH_DRIVER logical mathematical line `EM-DVR-DEBB5E`. Direct predecessors: r422 at `enterprise-math@706fdc60b44686c1ffa0dadd32ccd25883339196:research_notes/portable_direct/2026-11-20_x6_r422_ordered_provenance_vs_frame_orbit_exact_calibration.md` (six distinct positive axes); r421 at `enterprise-math@d93ca915ec93201bbcb1a889441834352a11ebd7:research_notes/portable_direct/2026-11-20_x6_s6_compatible_third_parity_kernel_and_minimal_orbit_witnesses_r421.md` (all three index-two signed-frame groups). Original X6 sources and authors remain with their existing researchers; this result adds a new repeated-letter comparison.

Question: when a labelled positive native-axis word may repeat some axes and omit others, how many such exact words can share one *calibrated static frame orbit*? How does an axis absent from both history and calibration change group parity constraints?

## Exact model and theorem

Take the signed alphabet `{±e_1,...,±e_6}` and global letterwise signed-permutation action of
`B_6=(C_2)^6 ⋊ S_6`. Let `p(g)=sgn(pi)` and `q(g)=prod_i epsilon_i`; define
`G_S=ker q`, `G_A=ker p`, `G_+=ker(pq)`, and `D=ker p ∩ ker q`.

Fix any vector `c=(c_1,...,c_6) ∈ N_0^6`, with total `n=sum c_i`. Let `W_c` comprise **all distinct ordered positive-axis words** with exactly `c_i` occurrences of `e_i`; `|W_c|=n!/prod_i c_i!`, including `n=0`. Fix a positive calibration suffix `s` whose set of distinct occurring axes is `S ⊆ {1,...,6}`. Observation is the orbit of the **whole concatenated word** `O_G(u)=[us]_G`, restricted to the domain `u∈W_c`. It is not an endpoint-only observation, a rearrangement of the suffix, or a claim of native physical rotation.

Set, for every integer `t≥1`,
`m_t=#{i∉S : c_i=t}`,
`P=prod_{t≥1}(m_t!)` (an empty product is 1), and
`r=#{i∉S : c_i=0}`.
Let `E(P)=P/2` when `P>1`, and `E(1)=1`.

**Theorem.** For every `u∈W_c`, its observer fiber inside `W_c` has cardinality

```
F_B6(c,S) = F_GS(c,S) = P
F_G+(c,S) = P       if r >= 1; otherwise E(P)
F_GA(c,S) = F_D(c,S) = P if r >= 2; otherwise E(P).
```

Thus **every nonempty fiber has the same size**. Its minimum extra *fixed-length* tag to recover the exact labelled word from the calibrated orbit is `ceil(log2 F_G(c,S))` bits, and the number of orbit observations represented in `W_c` is `|W_c|/F_G(c,S)`. No claim about variable-length expected coding, output size of the orbit itself or physical legal history is included.

### Proof

Equality `[us]_G=[vs]_G` for `u,v∈W_c` means that one `g∈G` acts letterwise and maps `us` to `vs`. Because the suffix is literally fixed, `g(e_i)=e_i` for every `i∈S`. Each positive label with `c_i>0` occurs in the prefix and must map to another positive label; hence its sign is positive. Count-vector equality forces the permutation to send the set of indices with any given **positive** count `t` to itself; already calibrated labels are individually fixed. The possible effective permutations of used, uncalibrated labels form exactly
`P_group=prod_{t≥1} S_{m_t}`, of order `P`.

The remaining `r` indices are absent from both prefix and suffix. Their internal permutations and signs have no observable effect on `us`. Every effective permutation in `P_group` is realizable in `B_6` and `G_S`, by assigning positive signs on all indices. In `G_+`, an odd effective permutation can be parity-balanced by one negative sign on an unseen index iff `r≥1`; without such an index, only even effective permutations are allowed. In `G_A` and `D`, an odd effective permutation can be parity-balanced by transposing **two unseen indices** iff `r≥2`; otherwise the effective permutation must be even (and positive signs suffice for `D`).

If `P>1`, one of the positive-count blocks has at least two labels, so `P_group` contains an odd permutation and its alternating kernel has index two. If `P=1`, both the full and parity-even effective groups are trivial. Finally, the effective action on `W_c` is free: a permutation that fixes a word containing every used label must fix all those labels, while only unobserved indices may remain movable. Its orbit therefore has exactly the stated effective group order, independently of `u`. The tag lower bound follows by counting a fiber; indexing each fiber attains it. QED.

### Consequences and sharp examples

| Positive count vector `c` | Calibrated set `S` | `r` | `P` | `B6, GS` | `G+` | `GA, D` |
|---|---|---:|---:|---:|---:|---:|
| (1,1,1,1,1,1) | ∅ | 0 | 720 | 720 | 360 | 360 |
| (1,1,1,1,1,0) | ∅ | 1 | 120 | 120 | 120 | 60 |
| (1,1,1,1,0,0) | ∅ | 2 | 24 | 24 | 24 | 24 |
| (1,1,1,1,0,0) | {5,6} | 0 | 24 | 24 | 12 | 12 |
| (2,2,3,3,4,4) | ∅ | 0 | 8 | 8 | 4 | 4 |

The second row is a **one-hidden-axis parity witness**: `G_+` and `G_S` give the same full 120-word orbit, but `G_A` splits it into two 60-word orbits. The third row is a **two-hidden-axes parity witness**: even `G_A` can realize every permutation of four used labels by compensating odd parity with a transposition of two unseen labels. Calibrating precisely those two absent labels (fourth row) removes this freedom without changing the prefix family.

For `c=(1,1,1,1,1,1)` and `S={1,...,k}`, this formula reduces exactly to r422's `(6-k)!` versus `(6-k)!/2` (with the 0/1-remaining-axis convention). For paths with fewer distinct observed axes, applying the full-support parity formula can be wrong.

### Exact finite verification and limitations

A direct Python enumeration of all `6!·2^6=46,080` signed permutations, filtered by suffix fixation and exact positive count-vector preservation, was compared to the formula on **22 explicit/random-seeded** `(c,k)` pairs (10 fixed examples and 12 generated with seed 7, `c_i∈{0,1,2,3}`, `k∈{0,...,6}`, `S={1,...,k}`). All 22 cases agreed for each of the five groups. The proof above is general for every nonnegative six-component `c` and every positive calibration suffix; the finite check is corroboration, not the proof.

This is an algebraic reference-frame **orbit of ordered signed letters**. Neither a positive occurrence-count vector nor the group orbit supplies native triadic closure, branching multiplicity, Cell/Port incidence, temporal legality, active physical rotation, or the correct observer quotient. Native transfer must select those typed definitions and their actual legal language. An omitted axis is an information-theoretic parity reservoir in this model, not an extra native rotation generator.

Status: one new author-side proof subunit; no new Native Result, independent review, Source/Activity linkage, formal Task closure or mother-objective closure.