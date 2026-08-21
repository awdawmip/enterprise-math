# R062 Stage 0 — BRC Enrichment Tower Theorem

Researcher-ID: `EM-R062-7C4A91`  
Status: `PATH_BRC_WITNESS_SEMANTICS_EXACT / N_BRC_MULTIPLICITY_SEMANTICS_EXACT / BOOLEAN_BRC_SUPPORT_SEMANTICS_EXACT`

## 1. Common typed skeleton

All three levels use the same component-labeled native transition skeleton from `R062_STAGE0_LABELED_NATIVE_RELATION_MODEL.md`. Only the entry carrier changes.

### B2 — PATH_BRC

For typed states `x,y`, define `Path_BRC(x,y)` as finite formal `N`-sums of concrete composable path witnesses `x -> y`.

A witness records enough data to reconstruct translated start vertex `P`, sector `(ij)`, generator word, every prefix cell trajectory and terminal typed cell.

Addition is formal sum. Multiplication is typed path concatenation, extended distributively. This is most honestly a many-object path/category algebra, not merely an untyped scalar semiring.

### B1 — N_BRC

Replace each formal path sum entry by its total multiplicity in `N`. One-step native component edges carry weight `1`; composition uses finite matrix/category convolution:

`(M*N)(x,z) = sum_y M(x,y) N(y,z)`.

For each frozen native trace:

`N_BRC(P,ij;a,b) = binom(a+b,a)`.

### B0 — BOOLEAN_BRC

Apply support: `beta(n)=0 iff n=0`, otherwise `beta(n)=1`.

This returns canonical BRC/result-support semantics. Merge becomes OR; composition becomes existential shared-middle composition.

## 2. Exact native fiber theorem

For every tested translated trace with `a+b<=12` in all three sectors and seven translated starts, the same generated source gives:

`|Path_BRC trace fiber| = N_BRC terminal multiplicity = binom(a+b,a)`

and `Boolean_BRC terminal support = 1`.

The exhaustive finite checker covers `1,911` translated trace cases and `172,011` concrete path witnesses, with zero duplicates and zero mismatch.

The structural formula is independent of that finite cutoff: a path witness is precisely a choice of the `a` positions occupied by `X_i` among `a+b` positions, hence is in bijection with the `a`-subsets of an `(a+b)`-set.

## 3. Minimal commuting diamond

For `(a,b)=(1,1)`:

- `Path_BRC`: two witnesses `X_iX_j`, `X_jX_i`;
- `N_BRC`: multiplicity `2`;
- `Boolean_BRC`: support `1`;
- trace quotient: one component trace.

Exact machine witness: `R062_STAGE0_COMMUTING_DIAMOND_WITNESS.json`.

## 4. 3-4-5 branch

For translated `T_{P;3,4}^{(ij)}`:

- native length remains `5` by the frozen R061 component gauge;
- `Path_BRC` contains exactly `35` distinct prefix trajectories;
- `N_BRC` records `35`;
- `Boolean_BRC` records `1`;
- trace quotient contains one trace class.

For `(4,3)` the count is also `35`; the axis-degenerate `(0,5)` and `(5,0)` branches each have one path. Therefore the one-sector `N=25` fiber total is `72`.

Exact certificate: `R062_STAGE0_N25_BRC_MULTIPATH_CERTIFICATE.json`.

## 5. The key classification

Canonical BRC is not refuted. It is correctly typed as the **Boolean/result-support shadow** of the richer native multipath object, provided the native component skeleton is retained.

The enrichment does not merely attach a scalar to an unlabeled adjacency relation. Component/trace typing and coefficient enrichment solve independent information losses.
