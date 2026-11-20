# X6 r422 — Ordered-path provenance versus calibrated frame orbits: exact six-axis family

2026-11-20 · Scope: **author-side exact finite group theorem / cross-line semantic audit**, not an independent Native Review or native triadic-dynamics acceptance. Logical contributor: existing RESEARCH_DRIVER line `EM-DVR-DEBB5E`, same shared scientific context as r411–r421. Preserve original contributors to the upper-structure S6 and signed-cube results.

## Sources and the question being distinguished

1. The upper-structure S6 semidirect interface, original researcher `EM-EMF6D046-5A2844`, immutable GitHub `ca9d35a5c2a3a79ca503de6e2e7c646a3be49354`, `research_artifacts/mcp/RS-X6-UPPER-STRUCTURE-INTEGRATION/MCP-c618a61189764f23846a391a08518a1a/0bf4c36b9aefb57d9d89/X6_UPPER_S6_STEP_HOLONOMY_INTERFACE_20261117.md`.
2. Signed-cube endpoint and ordered-provenance separation, original researcher `EM-X6-C7A253`, immutable GitHub `a52bd9f517bc8c7597dffa2d25d5474330eddae7`, `research_artifacts/mcp/RS-X6-UPPER-STRUCTURE-INTEGRATION/MCP-6634360390c64e0788a1307fbc6d5fcb/71d2bc196dd5a406531e/X6_UPPER_SIGNED_CUBE_QUOTIENT_AND_PROVENANCE_LOWER_BOUND_20261120.md`.
3. Driver's conditional signed-frame candidate comparison r419–r421; specifically r421 `d93ca915ec93201bbcb1a889441834352a11ebd7`, `research_notes/portable_direct/2026-11-20_x6_s6_compatible_third_parity_kernel_and_minimal_orbit_witnesses_r421.md`.

The upper-source 720 distinct six-step order histories and the frame-quotient comparison are compatible: **distinguishing labelled histories** and **distinguishing histories modulo a globally chosen reference frame** are different observer specifications. The following proves an exact calibration tradeoff without replacing either source claim.

## Proposition: exact orbit fibers for the full six-axis positive-order family

Let `A={e_1,...,e_6}` be positive primitive axis letters and let
`W={e_{pi(1)}...e_{pi(6)} : pi in S_6}`, where all 720 words are distinguished by their fixed labelled order. Their translation endpoints all coincide at `sum_i e_i` relative to a fixed Cell anchor.

For `k=0,...,6`, fix the common positive calibration suffix `s_k=e_1...e_k`, with `s_0` empty. Let `O_{G,k}(w)=[w s_k]_G` be the **full ordered concatenated word orbit** under one common letterwise signed-permutation element. A word-orbit equality is not equality of endpoints, and the suffix is not separately transformed or freely re-chosen.

Compare five abstract candidates acting on signed letters:
`B_6=(C_2)^6 ⋊ S_6`;
`G_S=ker(s)`;
`G_A=ker(p)`;
`G_+=ker(ps)`;
`D=ker(p)∩ker(s)`,
where `p=sgn(pi)` and `s=∏ sign_i`. The positive sign-preserving `S_6` skeleton is included in `B_6` and `G_S`.

**Exact theorem.** Every nonempty `O_{G,k}` fiber inside `W` has uniform cardinality

```
F_{B6}(k)=F_{GS}(k)=(6-k)!,
F_{GA}(k)=F_{G+}(k)=F_D(k)=a(6-k),
a(m)=m!/2 when m>=2; a(0)=a(1)=1.
```

Therefore the minimum *additional fixed-length side-information bits* that permit labelled recovery of every `w in W` from its observed calibrated orbit are exactly `ceil(log2 F_G(k))`; the quotient observation has `720/F_G(k)` distinct orbit values on this family.

| suffix labelled axes k | unrestricted positive-permutation fiber B6 / GS | side bits | even-permutation fiber GA / G+ / D | side bits |
|---:|---:|---:|---:|---:|
| 0 | 720 | 10 | 360 | 9 |
| 1 | 120 | 7 | 60 | 6 |
| 2 | 24 | 5 | 12 | 4 |
| 3 | 6 | 3 | 3 | 2 |
| 4 | 2 | 1 | 1 | 0 |
| 5 | 1 | 0 | 1 | 0 |
| 6 | 1 | 0 | 1 | 0 |

### Proof

If `g(w s_k)=w' s_k` as labelled ordered signed letters, then the suffix forces `g(e_i)=e_i` for `i<=k`. Every axis appears in `w` and every letter in `w'` is positive, so `g` maps every positive axis letter to a positive axis letter. **All six sign flips are therefore positive** on the entire action; `g` reduces to a pure permutation fixing each labelled suffix axis. The residual permutation is in `S_{6-k}` for `B_6, G_S`, and in `A_{6-k}` for `G_A,G_+,D`. Conversely every such residual permutation lies in the stated corresponding group and maps `W` to itself while fixing the suffix.

The action of each residual permutation group on `W` is free: a permutation fixing an ordered word containing all six different letters fixes every axis, so it is the identity. Each orbit hence has size the exact order of its residual group. A fixed-length code selecting one element in each orbit requires at least `ceil(log2 |orbit|)` bits by pigeonhole and is attained by indexing that orbit; the number of orbit classes is `720/|orbit|`. This proves all entries, including `k=5,6`, when the residual permutation group is trivial.

A complete finite-domain crosscheck enumerated all `6!=720` ordinary axis permutations, tested suffix fixing for every `k=0,...,6`, partitioned them by even/odd permutation and confirmed the stabilizer orders, orbit sizes and quotient counts: for `S_{6-k}`, orbit counts `1,6,30,120,360,720,720`; for `A_{6-k}`, `2,12,60,240,720,720,720`. This finite verification agrees with the independent group-theoretic proof.

## Consequences for existing claims and follow-up

* The upper signed-cube source's **10-bit bound** is exact for reconstructing six-step order with *fixed labelled axes and no separate quotient calibration*. It is not contradicted by the fact that `W/S_6` is a singleton: that singleton is an **unlabelled orbit observation**, not a lossless encoding of 720 labelled histories.
* After calibrating three fixed positive axes, the remaining worst-case ambiguity **within this complete-positive-permutation family** is 6 paths / 3 bits for `G_S` (or `B_6`), versus 3 paths / 2 bits for `G_A,G_+,D`. These are strictly scoped below the r421 free-signed-word worst-case 24-element/5-bit stabilizer result. Group size alone would have missed the family-specific parity distinction.
* Distinguish: (a) exact labelled provenance; (b) reference-frame-invariant provenance; (c) endpoint-only readout; and (d) legal triadic, Branch/Port/time continuation. Their state lower bounds are not interchangeable. In particular, an observer specified only up to S6 frame may require **zero** extra order bits on this family, whereas reconstructing a specific labelled order still needs ten bits with no suffix.
* Next concrete scientific test: take actual permitted native event words (not merely the formal six-step spatial words), the exact Source-specified observer and calibrated suffix; compute their *restricted legal* orbit fibers and check future-right-context congruence. A particular frame transformation may be a valid passive relabelling or an admissible dynamical rotation; the Source operator must decide which equivalence is physically meaningful.

All theorem claims here are algebraic within the exact finite signed-letter action, not P000 alteration, mathematical Result intake, review admission or Task closure. No existing owner or research attribution is reassigned.
