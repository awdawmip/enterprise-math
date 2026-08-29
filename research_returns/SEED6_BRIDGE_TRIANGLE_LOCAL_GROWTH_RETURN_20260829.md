# Seed-6 Bridge Triangle Local Growth — Research Return

Task: `RS-SEED6-BRIDGE-TRIANGLE-LOCAL-GROWTH`  
Publication: `TP2-262052627FA7DD9E5FF7`  
Researcher: `EM-S6T-A65497`  
Claim: `chatgpt-s6t-20260829-2042-a65497`  
Execution record: `ER-4C84BFAF80DD68EA2839`  
Execution branch: `research/seed6-bridge-triangle-local-growth-em-s6t-a65497`  
Hard target: `SEED6_LOCAL_BRIDGE_TRIANGLE_GEOMETRY_CLASSIFIED`  
Terminal verdict: `SUCCESS`

## 1. Executive result

For every prime `r>3`, let

\[
T_r=\{6,2r,3r\},\qquad L=6r.
\]

The strongest exact local classification is not the square-product identity. The cell is the **rank-2 coatom layer of the Boolean divisor lattice `B3` of the squarefree integer `L=2*3*r`**.

Equivalently, the three carrier atoms are `{2,3,r}` and

\[
6=L/r,\qquad 2r=L/3,\qquad 3r=L/2.
\]

Thus the three elements of `T_r` are exactly the three maximal proper divisors of `L`. Their pairwise gcds are the three carrier atoms and every pair has the same lcm `L`:

\[
\gcd(6,2r)=2,\quad \gcd(6,3r)=3,\quad \gcd(2r,3r)=r,
\]

\[
\operatorname{lcm}(6,2r)=\operatorname{lcm}(6,3r)=\operatorname{lcm}(2r,3r)=6r.
\]

This yields a canonical local carrier-incidence cell. The object-only version is a gcd-edge-labelled triangle; the faithful rank-aware version is the Levi incidence graph between the three carrier atoms and the three coatoms, which is a 6-cycle `C6` with its carrier/object bipartition remembered.

The exact 500-prime census (`r=5` through `r=3583`) found no exception. Every normalized rooted typed cell is isomorphic to every other one. Consequently, **the local combinatorics does not encode the numerical identity or size of `r` once `r` is normalized to the role “fresh carrier”**. What survives across `r` is the Boolean carrier-incidence type, not a new `r`-dependent local shape.

The product-square observation

\[
6(2r)(3r)=(6r)^2
\]

is therefore classified as a derived checksum, not an independent discovery: it follows because each of the three carrier atoms occurs in exactly two coatoms.

## 2. Exact local models

### Model A — object triangle with gcd carrier labels

Let the object vertices be

- `s=6` (seed vertex),
- `x=2r`,
- `y=3r`.

Take the complete graph on `{s,x,y}` and label each edge by the gcd of its endpoints:

- edge `s-x` carries `2`;
- edge `s-y` carries `3`;
- edge `x-y` carries `r`.

This model is compact. It already remembers the complete carrier-incidence data because each vertex is the product of the labels on its two incident edges:

\[
s=2\cdot3,\qquad x=2\cdot r,\qquad y=3\cdot r.
\]

Hence, inside the frozen prime domain, exact edge-gcd labels reconstruct both the carrier-incidence type and the numerical vertices.

### Model B — carrier/coatom Levi graph

Introduce carrier nodes `{c_2,c_3,c_r}` and object nodes `{v_6,v_{2r},v_{3r}}`. Connect carrier `c_p` to object `v_n` exactly when `p|n`.

The six incidences are

\[
2\mid6,\ 3\mid6,\ 2\mid2r,\ r\mid2r,\ 3\mid3r,\ r\mid3r.
\]

The resulting bipartite graph is

\[
2-6-3-3r-r-2r-2,
\]

a 6-cycle. Remembering the bipartition is essential: if one forgets which side is “carrier” and which side is “object”, the graph admits rank-reversing symmetries that are not multiplicative carrier automorphisms.

### Comparison

Model A and Model B encode the same local incidence information when edge labels are retained, but they expose different structure.

- Model A is minimal for object-object gluing and edge typing.
- Model B is the faithful divisor-lattice incidence picture and cleanly separates carrier atoms from coatom objects.
- The unlabelled triangle alone is too coarse: it forgets the multiplicative incidence entirely.
- The unranked `C6` is also too coarse: it introduces extra graph symmetries by allowing carrier/object exchange.

For subsequent global work, Model B or Model A plus explicit edge-carrier labels is therefore the safe local interface.

## 3. Boolean coatom theorem

### Theorem 1 — Seed-6 Boolean coatom classification

For prime `r>3`, with `L=6r`, the divisor lattice of `L` is the Boolean lattice on the three atoms `{2,3,r}` and

\[
T_r=\{L/2,L/3,L/r\}.
\]

Hence `T_r` is exactly the full coatom layer of that Boolean lattice.

### Proof

Because `r` is prime and `r` is distinct from `2,3`, the integer

\[
L=2\cdot3\cdot r
\]

is squarefree with exactly three prime atoms. Its divisors correspond bijectively to subsets of `{2,3,r}`, ordered by inclusion of supports, so the divisor lattice is `B3`.

The coatoms of a squarefree three-atom divisor lattice are obtained by omitting exactly one atom from the full product. They are

\[
L/2=3r,\qquad L/3=2r,\qquad L/r=6.
\]

These are precisely the members of `T_r`. QED.

### Corollary 1 — meet/join signature

For the three coatoms, each pairwise meet is one atom and each pairwise join is the top:

\[
\gcd(6,2r)=2,\quad\gcd(6,3r)=3,\quad\gcd(2r,3r)=r,
\]

and all three pairwise lcms equal `L=6r`.

This meet/join signature is an `EXACT_STRUCTURAL` invariant of the frozen family.

## 4. GCD labels reconstruct the local cell

### Theorem 2 — carrier reconstruction from edge labels

Let the three object vertices be `v_0=6`, `v_1=2r`, `v_2=3r`, and let

\[
g_{ij}=\gcd(v_i,v_j).
\]

Then

\[
g_{01}=2,\qquad g_{02}=3,\qquad g_{12}=r,
\]

and each vertex satisfies

\[
v_i=\prod_{j\ne i} g_{ij}.
\]

Thus the exact gcd-edge-labelled triangle uniquely reconstructs the local numerical cell.

### Significance

This is a structural reconstruction statement, not a factor-search proposal. The point is that the local object triangle and its carrier-incidence graph are equivalent descriptions within the declared family.

If exact labels `{2,3,r}` are replaced by the role labels `{fixed-left,fixed-right,fresh}`, the numerical value of `r` is intentionally forgotten while the normalized local type survives.

## 5. Valuation-support signature and the index-2 lattice

Order carrier rows as `(2,3,r)` and object columns as `(6,2r,3r)`. The support/valuation matrix is

\[
A=
\begin{pmatrix}
1&1&0\\
1&0&1\\
0&1&1
\end{pmatrix}.
\]

Every column has weight `2`, every row has weight `2`, every two columns intersect in exactly one carrier, and every two rows meet in exactly one object. This is the incidence matrix of the rank-1/rank-2 layers of `B3`.

Moreover,

\[
\det A=-2.
\]

The gcd of all `1x1` minors is `1`, the gcd of all `2x2` minors is `1`, and the absolute determinant is `2`; hence the Smith normal form is

\[
\operatorname{SNF}(A)=\operatorname{diag}(1,1,2).
\]

Therefore the integer lattice generated by the three coatom exponent vectors has index `2` in the carrier exponent lattice `Z^3`.

Each coatom vector has even coordinate sum, so the generated lattice lies in

\[
E=\{(a,b,c)\in\mathbb Z^3:a+b+c\equiv0\pmod2\}.
\]

Both lattices have index `2` in `Z^3`, therefore they are equal:

\[
\langle(1,1,0),(1,0,1),(0,1,1)\rangle_{\mathbb Z}=E.
\]

This parity/index signature is `EXACT_STRUCTURAL`. It is not an independent mysterious numerical law; it is the algebraic footprint of the `B3` incidence cell. It is nevertheless a useful compact interface for later gluing because it records an integral obstruction lost by purely real/rational linearization.

## 6. Local automorphism classification

The symmetry group depends sharply on which structure is remembered.

| Model / remembered data | Automorphism group size | Classification |
|---|---:|---|
| object triangle, no labels | `6` (`S3`) | too coarse |
| product-square relation alone | `6` | relation is fully symmetric and adds no local distinction |
| object triangle, edge types `fixed/fixed/new` | `2` | swaps the two seed-carrier sides |
| object triangle, exact gcd edge labels `2,3,r` | `1` | exact labels rigidify the cell |
| Levi `C6`, no rank/bipartition | `12` | includes rank-reversing graph symmetries |
| Levi `C6`, carrier/object bipartition preserved | `6` (`S3`) | rank-preserving Boolean automorphisms |
| rank-preserving Levi cell with seed coatom fixed | `2` | swaps carriers `2` and `3` together with `2r` and `3r` |
| exact carrier labels fixed | `1` | fully rigid |

The meaningful normalized Seed-6 cell is therefore naturally **rooted but not necessarily oriented**. If the two seed carriers are treated as an unordered pair, a residual `C2` symmetry remains. If an ordered boundary `(2,3)` is declared, that symmetry is removed.

## 7. Candidate invariant audit

### C1. Boolean coatom / meet-join signature

Status: `EXACT_STRUCTURAL`.

Signature:

- exactly three carrier atoms `{2,3,r}`;
- exactly three coatoms `{6,2r,3r}`;
- pairwise gcds are the three atoms;
- pairwise lcms are the common top `6r`.

This is the strongest coordinate-free local classification found.

### C2. gcd carrier-incidence signature

Status: `EXACT_STRUCTURAL`.

The gcd-edge-labelled object triangle and the rank-aware Levi graph determine one another. Each object equals the product of its two incident carrier labels.

### C3. valuation-support / Smith-normal-form signature

Status: `EXACT_STRUCTURAL`.

The binary incidence matrix has determinant `-2`, Smith normal form `(1,1,2)`, and coatom exponent lattice equal to the even-sum sublattice of `Z^3`.

### C4. fixed/fixed/new edge-type interface

Status: `EXACT_STRUCTURAL`.

Relative to the distinguished seed vertex `6`, its two incident edges are the two fixed seed-carrier ports and the opposite edge is the fresh-carrier edge. This survives normalization `r -> N`.

### C5. product-square relation

Candidate:

\[
6(2r)(3r)=(6r)^2.
\]

Status: `TAUTOLOGICAL` as an independent invariant.

Reason: each carrier atom appears in exactly two coatoms, so multiplying the three coatom labels automatically squares the product of all atoms. It is a useful checksum but carries no information beyond the carrier-incidence signature.

### C6. canonical orientation without ordering the seed carriers

Status: `MODEL_DEPENDENT`.

The rooted typed cell admits the reflection swapping the two seed carriers and simultaneously swapping the two mixed vertices. Therefore there is no canonical left/right orientation unless an ordered seed boundary is added as extra structure.

If the project later chooses an ordered seed interface `(2,3)`, the ordered port pair `(2r,3r)` becomes exact relative data; it is not intrinsic to the unordered local cell.

### C7. numerical `r` as a normalized combinatorial invariant

Status: `COUNTEREXAMPLE_FOUND`.

Witness:

\[
T_5=\{6,10,15\},\qquad T_7=\{6,14,21\}.
\]

They are numerically different and exact-label-preserving isomorphism does not identify them, but after replacing the fresh carrier label by the role symbol `N`, their rooted typed carrier-incidence cells are isomorphic. The same holds for every pair of primes `r,s>3`.

Hence no invariant depending only on the normalized local combinatorics can recover or distinguish the numerical fresh prime.

## 8. Cross-r rigidity theorem

### Theorem 3 — one normalized local isomorphism type

For any primes `r,s>3`, the map

\[
6\mapsto6,\qquad 2r\mapsto2s,\qquad 3r\mapsto3s,
\]

with carrier map

\[
2\mapsto2,\qquad3\mapsto3,\qquad r\mapsto s
\]

is an isomorphism of rooted typed carrier-incidence cells.

If the exact numerical carrier labels are part of the structure, cells with `r\ne s` are distinct. If only carrier roles are retained, all prime cells lie in one isomorphism class.

This freezes an important negative boundary for the Seed-6 program: any genuine variation across primes must enter through **how multiple cells are related/glued/ordered**, through extra arithmetic labels, or through a larger structure. It does not arise from the isolated normalized triangle itself.

## 9. Exact 500-prime census

The checker enumerates the first 500 primes `r>3`:

- first: `5`;
- last: `3583`;
- count: `500`.

For every sample it verifies, with exact integers:

1. `6r` is squarefree with exactly prime atoms `{2,3,r}`;
2. `T_r` is exactly the coatom set `{L/2,L/3,L/r}`;
3. pairwise gcd labels are `2,3,r`;
4. every pairwise lcm is `6r`;
5. each vertex equals the product of its two incident gcd labels;
6. the product-square checksum holds;
7. normalized support/incidence signature is constant;
8. exact gcd-labelled automorphism count is `1`;
9. fixed/fixed/new typed automorphism count is `2`.

The checker separately verifies the abstract Levi symmetry counts `12,6,2,1` under progressively stronger remembered structure.

No in-domain counterexample was found; the symbolic proofs above show the census laws hold for every prime `r>3`, so the finite census is confirmatory rather than evidentiary for universality.

## 10. Boundary guards outside the frozen domain

The task delegated degeneracies elsewhere, but four small guards are useful to show exactly what the prime hypothesis protects.

- `r=2`: `T_r={6,4,6}` is not a three-distinct-coatom cell.
- `r=3`: `T_r={6,6,9}` is not a three-distinct-coatom cell.
- `r=25`: `6r` is not squarefree, so the prime-atom divisor lattice is not `B3`.
- `r=35`: `6r` is squarefree but has four prime atoms `{2,3,5,7}`; the three displayed values are not the full coatom layer of the prime divisor lattice.

These are guards only; their full stratification belongs to the separate degeneracy task.

## 11. Minimal local interface for global gluing

The smallest safe reusable interface is the rooted rank-aware cell

\[
\mathcal I_r=(P_r,V_r,I_r,s),
\]

where

- carrier set `P_r={2,3,r}`;
- object/coatom set `V_r={6,2r,3r}`;
- incidence `p I_r n` iff `p|n`;
- distinguished seed object `s=6`.

Equivalent boundary description:

- fixed seed spine: `2 -- 6 -- 3`;
- fresh ear: `2 -- 2r -- r -- 3r -- 3`.

In the object-only triangle, the corresponding port types are

- seed-to-left-mixed edge: carrier `2`;
- seed-to-right-mixed edge: carrier `3`;
- mixed-to-mixed edge: fresh carrier `r`.

For a role-normalized interface, replace `(2,3,r)` by `(L,R,N)` and decide explicitly whether `(L,R)` is ordered. No global topology, cycle law, holonomy, or surface construction is imposed here.

A compact algebraic companion may also be exported:

- incidence matrix `A` above;
- Smith signature `(1,1,2)`;
- coatom exponent lattice = even-sum sublattice.

This is sufficient for the global bridge/surface task to test whether gluing multiple local cells creates structure not already forced by repeated copies of the same `B3` cell.

## 12. What is genuinely learned vs. what collapses

### Survives as exact structure

1. `T_r` is the full coatom layer of a three-atom Boolean divisor lattice.
2. gcd labels are exact shared-carrier labels.
3. all pairs share the same multiplicative join `6r`.
4. the rank-aware local graph is a bipartite `C6` incidence cell.
5. the valuation/support matrix has integral index `2` and Smith signature `(1,1,2)`.
6. rooted fixed/fixed/new port typing survives normalization across every prime `r>3`.

### Collapses / must not be promoted

1. the product-square identity is a consequence of the 2-regular carrier incidence;
2. an unlabelled triangle contains almost no multiplicative information;
3. an unranked `C6` has spurious rank-reversing graph symmetries;
4. the isolated normalized cell has no `r`-dependent combinatorial shape;
5. a canonical orientation does not exist without ordering the two seed carriers.

## 13. Hard-target closure

`SEED6_LOCAL_BRIDGE_TRIANGLE_GEOMETRY_CLASSIFIED` is satisfied.

- A. Two natural local models defined and compared: `PASS`.
- B. Exact gcds proved; carrier-incidence reconstruction proved: `PASS`.
- C. Local automorphisms classified at unlabeled, typed, rooted, rank-aware, and exact-label levels: `PASS`.
- D. More than three candidate invariant classes analyzed: `PASS`.
- E. Every candidate explicitly tagged `TAUTOLOGICAL / MODEL_DEPENDENT / EXACT_STRUCTURAL / COUNTEREXAMPLE_FOUND`: `PASS`.
- F. Exact standard-library checker plus 500-prime census and active cross-r/boundary counterexample audit: `PASS`.
- G. Minimal local interface exported without prescribing global topology: `PASS`.

## 14. Recommended downstream use

The next global/bridge-rectangle work should consume the local cell as a **rooted Boolean `B3` coatom-incidence block**, not as an arbitrary numerical triangle and not as a square-product coincidence.

The highest-leverage question downstream is now precise:

> when many copies of the same rooted `B3` cell are glued through shared seed carriers/seed object or through pairwise bridge rectangles, does any invariant survive that is not already the direct sum/repetition of the local incidence matrix and its index-2 parity signature?

That is where a genuinely new multiplicative geometry could first appear. The isolated prime triangle itself is structurally rigid and universal across `r` after role normalization.

## 15. Reproducibility

Exact checker:

`research_checks/SEED6_BRIDGE_TRIANGLE_LOCAL_GROWTH_CHECK_20260829.py`

Census certificate:

`research_artifacts/SEED6_BRIDGE_TRIANGLE_LOCAL_GROWTH/census_summary.json`

The checker uses the Python standard library and exact integer arithmetic only.
