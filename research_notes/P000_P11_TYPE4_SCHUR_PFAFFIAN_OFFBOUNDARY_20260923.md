# P000 P11 TYPE-4 Schur/Pfaffian obstruction frontier

Status: `NONCANONICAL_PORTABLE_RESEARCH_NOTE / NO_CURRENT_CLAIM / NOT_SOURCE_CHECKPOINT / NOT_RESULT / UNREVIEWED`

Task: `RS-P000-P11-DIAGONAL-ELLIPTIC-FIBER-PRIMITIVE-ARITHMETIC`

Publication: `TP2-FB7F5A1D6B6C6BCCD62D`

Frozen task/control source consumed: `52bf66ebb96dd0027b546ca08cb1922f353e35e7`.

Contributor lineage: `EM-DIRECT-C4D02C`, stable conversation `em-auto-staggered-20260923-r11`, service session `MCP-5ff2a3263c5c4ca2b556ebe8e47e5624`.

Research-Activity-ID: `UNKNOWN/PENDING` (no activity-registration mutation was available through the current ordinary-control surface; this note does not fabricate one).

This note persists three portable units produced while the canonical continuation had `execution_authorized=false`. It does not convert staged uploads into Source progress and must not be placed in predecessor `completed_units` merely because it exists on GitHub.

## Consumed interface; do not replay

Consume the same-session staged exact Weierstrass carrier

`W^2 = X(X-P^2)(X-Q^2)`,

uniform rational 2-torsion, labeled P/Q/R edge-local 2-descent, exact TYPE-4 / TYPE-5+ local images, the exact odd-local residue matrix `M(r,s)`, its alternating-form property, the canonical torsion radical `tau`, the TYPE-5+ second radical, and the TYPE-4 tripartite matching gate.

For TYPE-4 put

`a=|S_P^+|`, `b=|S_Q^+|`, `c=|S_R|`, `m=a+b`, `n=m+c`.

Order vertices as `U=P union Q` followed by `R`. Then over `F_2`

`M = [[C,H^T],[H,0_c]]`,

where `C` is the alternating selector-selector form (P-P and Q-Q blocks zero, P-Q block given by the exact Legendre-bit reciprocity matrix) and `H` is the R-to-selector cross-incidence matrix.

## Unit A — exact Schur/radical nullity formula

Choose any R-port `j` in `supp(tau)`, so `tau_j=1`. Delete row `j` from `H` and call the result

`H_j in F_2^((c-1) x m)`.

Delete row/column `j` from `M` and write

`N_j = [[C,H_j^T],[H_j,0_(c-1)]]`.

### Torsion splitting

After reordering `j` last, write `tau=(t,1)`. From `M tau=0`, the off-diagonal column of `M` is `N_j t`. Since `N_j` is alternating, `t^T N_j t=0`. An invertible congruence therefore splits

`M ~ N_j direct-sum [0]`,

hence

`k := nullity(M) = 1 + nullity(N_j)`.

### Exact solve

Let

`h=rank(H_j)`, `K=ker(H_j)`, `L=ker(H_j^T)`,

and let

`rho = rank(C restricted to K)`.

Solving `N_j(x,y)=0` gives

`H_j x=0`, `H_j^T y=Cx`.

Thus `x in K`; the second equation is soluble iff `Cx in im(H_j^T)=K^perp`, i.e. iff `x` lies in the radical of `C|_K`. For each admissible `x`, the solution fiber in `y` has dimension `dim L`. Therefore

`nullity(N_j)=(c-1-h)+(m-h-rho)`,

and the exact all-TYPE-4 formula is

`k = n - 2 rank(H_j) - rank(C|_(ker H_j)).`

Because the restricted form is alternating, `rho` is even. The final right-hand side is independent of the chosen tau-supported `j`, although `h` and `rho` separately need not be.

Consequently

`k=1`

iff `H_j` has full row rank and `C|_(ker H_j)` is nondegenerate. Writing

`d=m-c+1=dim ker(H_j)`

in the full-row-rank case, `d` must be even. Since `C` only couples P to Q,

`rho <= 2 min(a,b)`,

which recovers the prior block inequalities

`|a-b|+1 <= c <= a+b+1`.

On the old boundary `c=m+1`, `ker H_j=0` when `H_j` is invertible, and the formula reduces exactly to

`k=1 iff det_F2(H_j)=1`.

Thus the observer-safe repair coordinate away from the boundary is not the whole P-Q block blindly: it is the internal reciprocity form `C` restricted to the R-invisible selector kernel `ker H_j`.

Deterministic falsification only: direct exact F2 computation reproduced the prior `r<=150` census exactly. For every primitive opposite-parity TYPE-4 core with `2<=r<=500` (25,311 cores), the formula matched direct `nullity(M)` with zero failures. Across 140,959 tau-supported choices of `j`, the final value was j-independent and matched direct nullity with zero failures. These scans are regression, not proof.

Control-bridge staged artifact:
`p000_p11_type4_selector_schur_radical_nullity_formula_20260923.md`, final upload request `p000-schur-nullity-upload-20260923-r11-2151`, SHA-256 `845b93056cfe3df17ac5ad6d29efbb1c9c64635f6184c9df880d316df3ba2cba`, `source_published=false` at receipt.

## Unit B — exact off-boundary k=1 counterexample

The finite suggestion that `k=1` might force the boundary `c=m+1` is false.

Take the primitive opposite-parity TYPE-4 core

`(r,s)=(9126,9125)`.

Then

`A=18251`,
`B=166549500=2^2*3^3*5^3*13^2*73`,
`P=166567751=7*17^2*137*601`,
`Q=166531249=97*1153*1489`.

Hence

`S_P^+={17,137,601}`,
`S_Q^+={97,1153,1489}`,
`S_R={3,5,13,73,18251}`,

so `(a,b,c,m,n)=(3,3,5,6,11)` and

`d=m-c+1=2`.

This is genuinely off boundary: `c=m-1`.

The torsion R-vector is `(1,1,0,1,1)`, so choose `j=3`. With selector order

`U=(17,137,601,97,1153,1489)`,

the P-Q form is

```
C =
0 0 0 1 1 1
0 0 0 1 1 0
0 0 0 1 0 0
1 1 1 0 0 0
1 1 0 0 0 0
1 0 0 0 0 0
```

and the R-to-selector rows are

```
3:     1 1 0 0 0 0
5:     1 1 0 1 1 0
13:    0 1 0 1 0 1
73:    1 0 1 0 1 1
18251: 1 0 1 1 0 1
```

Deleting row 3 gives `rank(H_j)=4` and

`ker H_j = <v1,v2>`, where

`v1=(1,1,0,1,1,0)`,
`v2=(1,1,0,0,0,1)`.

The restricted form is

`[C|_K]_(v1,v2) = [[0,1],[1,0]]`,

so `rho=2`. Therefore

`k = 11 - 2*4 - 2 = 1`.

Direct rank of the full exact residue matrix gives the same answer; every other tau-supported choice `j in {5,73,18251}` again yields `rank(H_j)=4`, `rho=2`, and `k=1`.

Thus off-boundary `k=1` is arithmetically possible, and the P-Q repair coordinate is genuinely essential: dropping `C` away from the boundary destroys the decisive information.

Conditional only on the previously staged exact descent implication `k=1 -> rank E(Q)=0 -> no strict-P11 point`, this core supplies an off-boundary rank-zero obstruction. That implication is consumed as staged evidence here and is not promoted by this note.

Control-bridge staged artifact:
`p000_p11_type4_offboundary_k1_exact_counterexample_20260923.md`, final upload request `p000-offboundary-k1-upload-20260923-r11-2158`, SHA-256 `49830540be5ef23be54658354833a01ca95969dd0fe1e94c1b80d168267bfc30`, `source_published=false` at receipt.

## Unit C — Pfaffian minor-sum certificate

The Schur criterion has an equivalent provenance-resolved matching form. Put `d=m-c+1`. Since the R-R block of `N_j` is zero, every perfect matching contributing to `Pf(N_j)` pairs all `c-1` R vertices with distinct selectors; the remaining exactly `d` selector vertices must be internally paired through `C`.

Grouping by the internally paired selector subset `S` yields the exact characteristic-two identity

`Pf(N_j) = sum_(S subset U, |S|=d) Pf(C_S) det(H_j[:,U\S]) mod 2`.

Since `k=1` iff `N_j` is nonsingular, the exact certificate is

`k=1 iff sum_(|S|=d) Pf(C_S) det(H_j[:,U\S]) = 1 in F_2`.

This recovers:

- odd `d` impossible;
- `d=0` gives the old boundary determinant `det H_j`;
- because `C` has only P-Q edges, a nonzero internal Pfaffian needs equal numbers of P and Q selector vertices in `S`, giving the prior block-balance constraints.

On the first genuine off-boundary face `d=2`, this becomes

`k=1 iff sum_(p in S_P^+, q in S_Q^+) C_pq det(H_j[:,U\{p,q}]) = 1`.

For `(r,s)=(9126,9125)`, `j=3`, the six P-Q pairs with `C_pq=1` are

`(17,97),(17,1153),(17,1489),(137,97),(137,1153),(601,97)`.

Their complementary 4x4 H-minor determinants are

`1,1,1,1,1,0`,

whose parity is 1. This is a channel-resolved exact certificate for the same off-boundary `k=1`, without choosing a kernel basis.

Control-bridge staged artifact:
`p000_p11_type4_pfaffian_minor_sum_certificate_20260923.md`, final upload request `p000-pfaffian-minorsum-upload-20260923-r11-2210`, SHA-256 `be366c8fe904395e6f18a342fa70551ca0335eaf717804739a6712cef1efb011`, `source_published=false` at receipt.

## Prior-art boundary checked in this run

Wang–Zhang, *On the quadratic twist of elliptic curves with full 2-torsion* (arXiv:2303.05058), develops generalized Monsky matrices, Rédei matrices, Cassels pairing and residue-symbol equidistribution for the related family `y^2=x(x-a^2 n)(x+b^2 n)` with `a^2+b^2=2c^2`. This validates the classical surrounding toolkit but does not directly subsume the present P11 carrier `y^2=x(x-P^2)(x-Q^2)`: the sign/model, the fact that P/Q/R are simultaneously constrained by one Euclidean core, and the exact P11 reconstruction/provenance filters differ. Its distribution theorem varies an external squarefree twist `n` under residue conditions; it does not prove that the correlated Euclidean-core prime patterns needed here occur infinitely often. Do not transport that infinitude without a separate arithmetic realization theorem.

## BRC resolution

`COMPOSE_APPLIED`.

For the sole Selmer-nullity observer `k`, the full labeled matrix factors exactly through `rank(H_j)` and `rank(C|ker H_j)`, or equivalently through the Pfaffian minor-sum. For reconstruction or future arithmetic, retain the full P/Q/R labels and Euclidean-core provenance. The off-boundary counterexample proves that the internal P-Q repair coordinate cannot be dropped globally.

## Current control boundary and next exact action

Latest canonical continuation for this exact task remains `HANDOFF_READY / NEEDS_DISPATCH`, `execution_authorized=false`, `persisted_checkpoint=NOT_FOUND`, `durable_frontier=null`, `progress_reference_readback=null`, and `continuation_seed=null`. The publication-id last-progress reference is still absent from the immutable artifact manifest. Do not replay the previously rejected predecessor mutations unless the packet/contract changes.

Smallest next scientific unit: on the `d=2` face, control the explicit scalar parity

`sum C_pq det(H_j[:,U\{p,q}])`.

Either derive a Euclidean-core reciprocity law that forces/constrains it, or construct an infinite primitive family on which it is 1. The boundary-only conjecture is killed by `(9126,9125)` and must not be revived. Do not redo TYPE-5+ or the local descent.
