# R059L GENERATION FREEZE — PATH COLLAPSE COUNTING KERNEL

Generation: `R059L`
Researcher-ID: `EM-R059L-5F9D05`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Status: `DRIVER_ACCEPTED / GENERATION_FROZEN`
Date: `2026-08-15`

## Frozen terminal owner head

`cd3978c8fdbaa0699b4fe22895fb3c74b7283c8a`

Stage E checkpoint artifact:

`R059L_STAGE_E_TAU_COFACTOR_CHECKPOINT.json`

Stage E completion disposition:

`R059L_PATH_COLLAPSE_COUNTING_KERNEL_COMPLETE_CANDIDATE`

No Stage F is authorized in R059L.

## Accepted foundation

R059L remains subordinate to:

- `PACKET_PATH_FOUNDATION.md`
- `packet_path_foundation.json`
- `FOUNDATIONAL_LOGIC.md`
- `foundational_logic.json`
- `native_semantics_admissibility.json`

Native path equality remains exact full ordered packet-history equality. Readout/fiber equality never changes native equality.

## Accepted stage chain

- Stage 0: unit-packet / path-only semantic freeze.
- Stage A: native path algebra; concatenation, reversal, event-count additivity, endpoint incidence; reversal is not cancellative inverse.
- Stage B: information-collapse readout DAG; directed transition multiplicity `T` does not reconstruct full history in general.
- Stage C: realizability fibers `F(T;s,t)` and collapse multiplicity `MU(T;s,t)=|F(T;s,t)|`; exact realizability conditions and reversal/relabeling fiber bijections.
- Stage D: native last-exit / local-order factorization and exact factorial-arborescence formula for `MU`.
- Stage E: exact integer cofactor computation of the arborescence factor.

## Frozen terminal theorem chain

For positive realizable finite transition table `T`, define:

- `ACTIVE(T)` as in frozen Stage C;
- `d_x = OUT_T(x)`;
- root `r=t` for `s!=t`, and `r=s` for positive closed `s=t`;
- integer matrix `K` on `ACTIVE(T)` by
  - `K[x,y] = -T(x,y)` for `x!=y`;
  - `K[x,x] = sum_{y!=x} T(x,y)`;
- `K^(r)` by deleting root row and root column.

Stage E proves natively, without external Matrix-Tree theorem as premise:

`TAU_r(T) = det(K^(r))`.

The proof expands the determinant into parent-choice data. Functional parent choices containing a non-root directed cycle cancel exactly by the finite Leibniz cycle-subset identity; rooted choices survive with coefficient `+1` and multiplicity weight `product_x T(x,p(x))`.

Combining with frozen Stage D:

`MU(T;s,t) = det(K^(r)) * d_r! * product_{x in ACTIVE(T), x!=r}(d_x-1)! / product_{x,y} T(x,y)!`.

Zero-transition branch remains:

- `T=0, s=t => MU=1`;
- `T=0, s!=t => MU=0`.

Exact determinant computation is integer/fraction-free (`Bareiss`); floating determinant, tolerance and round-to-integer are forbidden.

## Semantic status

The determinant/cofactor and `MU` are downstream exact N2 readout computations. They are not N0 ontology, geometry, probability, entropy, length, distance, or physical conservation quantities.

The following remain withheld:

- line / straightness / distance / length / shortest path / geodesic;
- edge / boundary / area / volume / angle / curvature;
- physical flow/current/divergence interpretation;
- raw-history cancellation or quotient;
- R057/R058S fitted geometry as native premise;
- C6 passage composition repair (`C6_PASSAGE_COMPOSITION_NOT_YET_WELL_TYPED`).

## Driver disposition

R059L has completed its intended path-collapse counting kernel. Further work on macroscopic stability, path-spectrum coupling, atomic/composite interaction, dynamic steady states, or physical calibration belongs to separate generations/lanes and must not mutate this frozen R059L generation.
