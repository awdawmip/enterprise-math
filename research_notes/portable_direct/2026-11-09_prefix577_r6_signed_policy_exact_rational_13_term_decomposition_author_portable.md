# BRC-X6: constructive exact rational decomposition into at most 13 pure controllers, sharp

**Research date:** 2026-11-09 Asia/Hong_Kong. **Role:** TASK_RESEARCH, author-only portable mathematical evidence. **Status:** AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED. **Frozen science pin:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Native kernel SHA-256: `d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0`.

## Exact model

Use the four source ports `(6,7,28,29)` with signs `(+1,-1,-1,+1)`, six original action labels per port and the original **(next port, R1,R2,R3,R4,R5,R6,K)** output atoms for nine frozen roots `0,±e1,±e2,±e3,±e4`. Let `P` be the polytope of nonnegative rational policies with source-row sums 1 and signed masses cancelling separately at every original output atom. The preceding exact native incidence proof (commit `7886a552ff372fee6d68dada88d1219d9916016e`) gives a 12-dimensional network-flow polytope with exactly 38 deterministic 0–1 vertices `v_0,...,v_37`, ordered lexicographically by their four action labels. Full native observer labels remain intact.

## Theorem 1: deterministic rational decomposition, at most 13

For every rational `x∈P`, a constructive algorithm produces `x=Σ w_j v_{i_j}` with `w_j>0, Σw_j=1, m≤13`. Enumerate the 38 vertices by original native atom equality. Starting with residual `r=x` and mass `s=1`, repeatedly select the lexicographically first vertex whose four positive coordinates lie in the positive support of `r`. Such a vertex exists because `r/s` lies in a face of `P`. Put `t=min_{e:v_e=1}r_e` and replace `(r,s)←(r-tv,s-t)`. Each step eliminates at least one positive coordinate, and a nonzero feasible residual has at least four positive coordinates. Thus ≤21 vertices are extracted, preserving the exact rational vector.

For every remaining affine dependence `Σ α_j(1,v_{i_j})=0`, choose an exact rational null vector with both signs, put `δ=min_{α_j>0} w_j/α_j` and `w_j←w_j−δα_j`. At least one positive coefficient vanishes. The augmented vertex rank is 13; after ≤8 eliminations the remaining vertices are affinely independent, hence `m≤13`. Each pure policy separately preserves the native signed atom.

**Cost and exactness:** Preprocessing tests `6^4=1296` action quadruples against the original four seven-reward+target atoms. Per rational input, ≤21 peel iterations each test ≤38×4 source-action supports, plus ≤8 nullspace solves of at most a 25×21 rational 0–1 matrix. No subset enumeration or floating optimization occurs. If each input fraction has denominator bit-length ≤L, a common denominator has ≤24L bits. Final independent 0–1 minor bounds via Cramer's rule give numerator/denominator bit-length ≤24L+25; intermediate arithmetic remains polynomial in L with these fixed matrix dimensions. General variable-size complexity is not claimed.

## Theorem 2: explicit exact witness requiring 13 terms

Let `B=2^26=67108864`, `S=Σ_{i=0}^{37}B^i`, and `x★=(Σ_{i=0}^{37} B^i v_i)/S`. Then `x★∈P` and it cannot lie in the affine span of any ≤12 vertices.

**Proof:** The 38 binary vertices have affine dimension 12. A 12-coordinate affine chart is given by original action-coordinate indices `(0,1,2,3,4,6,7,10,12,13,14,16)` (zero-based). The projected points `z_i∈{0,1}^{12}` span `Q^{12}` affinely. For any collection of ≤12 such points, select an independent set of augmented 13-coordinate rows of rank `r≤12`. Cofactors of an `r×(r+1)` full-row-rank submatrix furnish a nonzero integer affine form `ℓ(z)` annihilating them. Hadamard gives coefficient bounds `|a_j|≤r^{r/2}≤12^6`; thus for every binary vertex, `|ℓ(z_i)|≤13·12^6=38817792=:M`. This form cannot vanish on all 38 full-dimensional vertices. Let `j` be the largest index with `c_j=ℓ(z_j)≠0`. Since `B−1>M`, the leading base-`B` term dominates: `|c_j|B^j≥B^j>M(B^j−1)/(B−1)≥|Σ_{i<j}c_iB^i|`. Hence `ℓ(x★)≠0`, excluding every ≤12-vertex affine span. Theorem 1 attains 13, so the bound is **sharp for this explicit rational policy**.

## Sharp special-case decomposition of uniform input

For the uniform policy `x[p,a]=1/6` on all 24 source/action coordinates, **six** preserving pure controllers are necessary: each pure policy has exactly four nonzero coordinates, so covering all 24 strictly positive coordinates requires at least `ceil(24/4)=6` policies. The exact certificate attains six using these four-action tuples with coefficient `1/6` each: `(0,0,0,0)`, `(1,1,3,3)`, `(2,2,1,1)`, `(3,3,2,2)`, `(4,4,4,4)`, `(5,5,5,5)`. Every source uses all six action labels exactly once, and each controller independently satisfies native full-output signed atom balance for all nine roots. Thus the minimum support for this explicit uniform rational input is exactly **6**, while the constructed `x★` witnesses the sharp global **13**.

## Exact certificates and reproduction

The full seven-file portable package `PREFIX577_R6_SIGNED_POLICY_EXACT_RATIONAL_13_TERMS_AUTHOR_PORTABLE_20261109.zip` includes:
`frozen_native_kernel_prefix577.py`, original edge snapshot, `verify_signed_rational_decomposition.py`, `independent_readback_signed_decomposition.py`, `SIGNED_POLICY_EXACT_DECOMPOSITION_CERTIFICATE.json`, expanded theorem and SHA-256 file manifest. Package SHA-256:
`772e9dc14f0ddca18a89a4117bc45ffda7287c61ef2ec26e5c8daa2c28479a7d`.
Run both Python scripts in a directory containing these files (requires `sympy`). Exact checks: all 38 pure controllers for all nine roots, affine rank 13, six sample policies including the displayed `x★`, 80 seeded positive-integer mixtures, exact 24-coordinate reconstruction, and an independent native full-output-atom readback. All passed, including isolated fresh-extraction replay and manifest verification. Certificate SHA-256 `d585c30954cbc94b150efa44b30d134d6b811200ea4bdaae91206c13186235be`.

**Provenance and remaining:** Reuses—not recredits—the previous 38 vertices and 18 facets/434 edges. This is portable author evidence, not the canonical D25 divided-power/Frobenius/κ result or original CM experiment. Source CLAIM/open/checkpoint and independent Driver acceptance remain pending valid session authority. The historical UR V2 four-file bundle remains an exact byte recovery target: 94,687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; no reconstructed artifact is described as original. Next localized open question: exact minimum number of pure controllers for a given rational feasible policy beyond the now-sharp universal bound.
