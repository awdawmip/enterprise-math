# R061 Stage 3 — Symmetry No-Go and Axiom Matrix

Researcher-ID: `EM-R061S3-2F9622`

## No-go A — symmetric spectrum scalar cannot recover every directed origin value

The origin-to-`+E1` segment has `(ell_f,ell_r)=(1,sqrt(2))`. The origin-to-the carrier-opposite `E1` vertex has the swapped ordered pair `(sqrt(2),1)`. Both have the same orientation-free spectrum `{1,sqrt(2)}`.

Therefore any symmetric scalarization `F(ell_f,ell_r)=F(ell_r,ell_f)` takes the same value on both. It cannot equal the forward directed origin gauge on both segments, because that would require the same scalar to be both `1` and `sqrt(2)`.

## No-go B — symmetry + translation invariance + full origin-gauge recovery

Assume a scalar `d` has endpoint symmetry, translation invariance on the coordinate-vertex lattice, and `d(O,Q)=ell(O->Q)` for every native vertex `Q`.

Let `U` be one `+E1` tick and `V` the vertex one carrier step opposite `E1`. Then `ell(O->U)=1`, `ell(O->V)=sqrt(2)`.

Translation invariance gives `d(V,O)=d(O,U)=1` because `V->O` is the translated `+E1` displacement. Symmetry gives `d(O,V)=d(V,O)=1`, contradicting full origin-gauge recovery `d(O,V)=sqrt(2)`.

So these three properties are jointly impossible under the frozen Stage 2 premises.

## No-go C — exact agreement with both directed trace norms

For translated `3-4-5`, `ell(P->Q)=5`, `ell(Q->P)=sqrt(17)`. A single symmetric scalar cannot be exactly equal to both directed trace gauges on the same unordered segment. The unit step gives the smaller witness `1` versus `sqrt(2)`.

## What is not proved impossible

The requirements “positive-axis unit scalar equals 1” and “orientation-free 3-4-5 scalar equals 5” alone do not prove that every imaginable symmetric `F` is impossible. An ad hoc `F` could be engineered to hit two calibration points; such a rule would still require new structure and would not be uniquely derivable.

## Candidate compatibility matrix

| Candidate | Symmetric metric | Unit=1 | 3-4-5=5 | Full directed-origin recovery | New choice |
|---|---|---|---|---|---|
| `d_max` | yes | no (`sqrt(2)`) | yes | no | choose `l_inf` |
| `d_sum` | yes | no (`1+sqrt(2)`) | no | no | choose `l_1` |
| `d_mean` | yes | no | no | no | choose `l_1` + scale |
| `d_2` | yes | no (`sqrt(3)`) | no (`sqrt(42)`) | no | choose `l_2` |
| unit-normalized `d_max` | yes | yes | no | no | choose norm + scale |
| unit-normalized `d_2` | yes | yes | no | no | choose norm + scale |

No row is promoted to native canonical status.
