# R5: Seven exact facets, twelve 13-edge vertices, and a triangle-times-square coupling polytope

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_EXACT_FINITE_CERTIFICATE / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED.

## Source, scope and frozen science

This note continues **PR #1859**, immutable author-side commit `f63a0250714f2445e8b406754b85f26d983ec3a6`, specifically its exact fixed marginal pair `nu=M(X)`, `mu=M(Y)`, and the complete four-parameter Blackwell coupling representation `E(q)=P+sum(q_k V_k)`, with 17 potentially positive edges. Earlier provenance: PR #1855 (dual) and #1856 (optimal face/fiber).

Frozen scientific input pins remain global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Normative sources are current-read separately. All theorems below refer to **this exact fixed seven-LR-node marginal pair** and *all* its nonnegative Blackwell couplings; this is an auxiliary statistical observer, not a P000 native-space assertion.

In the predecessor, 21 exact mass and LR-moment equations reduce to 17 edge coordinates with rank 13 and four free coordinates:
`q1=E_(2,1)`, `q2=E_(3,1)`, `q3=E_(3,2)`, `q4=E_(2,3)`. The entire feasible polytope is
`Q={q in R^4: E_e(q)>=0 for all 17 permitted support edges}`.

## Theorem A: an irredundant seven-inequality H-representation

Write
`a=3997/690000`,
`b=170189123/37621284000`,
`d=8294919533/677183112000`.
Then the **whole** four-dimensional coupling polytope is exactly

```text
q1 >= 0,
q2 >= 0,
13*q1 + 18*q2 <= 23*a,
q3 >= 0,
q4 >= 0,
18*q3 <= 23*b + 13*q1 + 13*q4,
10*q4 <= 23*d + 5*q2 + 5*q3.
```

These are, respectively, the nonnegative edge weights at
`(2,1),(3,1),(4,1),(3,2),(2,3),(4,2),(0,3)`.
All seven inequalities define actual facets; the ten remaining edge nonnegativity constraints are strictly slack everywhere in Q.

Proof and completeness: `q1,q2` are bounded by the first three inequalities. The last two bound `q3,q4`: substituting `q4 <= 23*d/10+q2/2+q3/2` into `18*q3 <= 23*b+13*q1+13*q4` yields
`(23/2)*q3 <= 23*b+13*q1+(299/10)*d+(13/2)*q2`, so this seven-inequality polyhedron is bounded. Every vertex consequently lies at a linearly independent set of four active facet hyperplanes. Exact enumeration of all `C(7,4)=35` quadruples gives **12 distinct feasible vertices**. Independently enumerating all `C(17,4)=2380` quadruples for the original 17-inequality polyhedron gives the same 12 vertices; 324 four-tuples have full rank. At those 12 vertices all ten omitted edge weights are strictly positive (the script gives each exact rational minimum), so the 7-inequality and full 17-inequality polyhedra coincide. Each selected inequality vanishes at vertices that affinely span a 3-dimensional face; it is irredundant.

This is a finite exhaustive certificate with a justified finite candidate set and rational Gaussian elimination, not numerical sampling.

## Theorem B: exact face lattice and support sparsity

The four-dimensional polytope Q is **simple**, with
```text
f-vector (vertices, edges, two-faces, facets) = (12,24,19,7).
```

Every vertex lies on exactly four facets, and all 12 vertex matrices have **exactly 13 strictly positive transport edges**. The three 8-vertex facets are indexed by `(2,1),(3,1),(4,1)`, forming the triangle factor. The four 6-vertex facets are indexed by `(3,2),(2,3),(4,2),(0,3)`; their intersection graph is a square (four adjacent pairs of intersection size 3, two opposite pairs disjoint). At each vertex precisely two facets from each group are active. The incidence lattice is therefore that of a product of a triangle and a square:
```text
Q is combinatorially Delta_2 x [0,1]^2.
```
This is a **combinatorial equivalence**; no affine-product identity is claimed.

**Sharp minimum support theorem for the fixed marginal pair:**
```text
min{# positive E_e : E is a nonnegative feasible Blackwell coupling} = 13.
```
Every vertex gives an attainable 13-edge coupling. If a feasible coupling had at least five zero edges, it would lie in the common zero face of those five nonnegative affine weights. Every nonempty face of a compact polytope has a vertex, giving a vertex with at least five zero edges, contradicting the exact vertex list (each has exactly four zeros and the other 13 positive). This proves the lower bound for **all** couplings.

## Theorem C: full exact atlas-escape mass interval

The predecessor established the exact cost functional for the old 16-edge atlas S:
```text
epsilon_S(E(q)) = 225713944957/3385915560000
                + (28/23)*q2+(5/23)*q3+(13/23)*q4.
```
A linear functional on compact Q attains extrema at vertices. Exhaustive rational vertex evaluation gives the **sharp global range across all feasible couplings of this fixed pair**:
```text
225713944957/3385915560000 <= epsilon_S(E)
                            <= 8555233477/73606860000.
```
The minimum is realized at two vertices and the segment between them (already found in PR #1856). The maximum is attained at a unique vertex:
```text
q = (0, 3997/540000, 6636239129/147213720000,
     222511289/4089270000).
```
Every intermediate cost occurs by convexity.

The corresponding highest-cost coupling still uses only 13 positive edges: high atlas escape mass does not intrinsically require a dense support. The BRC residual observer used here is **positive mass outside a declared atlas**, not cancellation amplitude or an assertion about original physical energy.

## Exact verification and recovery

Run `python3 VERIFY.py` under any Python 3 version with standard-library `fractions.Fraction`; `EXACT_OUTPUT.txt` records the executed exact enumeration outcome. The code contains the complete predecessor P and four kernel directions, a rational 4x4 solver, both independent finite enumerations, 7-facet incidence checks, exact 4D face counts, and the cost extremal checks. The predecessor's `VERIFY.py` at `f63a025...` separately checks the 21 transport equations, physical capacities and frozen marginal formulas; this note relies on those as declared inputs.

The finite enumeration plus the stated boundedness and affine nonnegativity arguments prove the continuous real-parameter results for the fixed pair. Independent mathematical review and formal task admission remain open. No new Owner/CLAIM, native spatial theorem, or all-physical uniform 14-edge claim is inferred.

**Next discriminating action:** Perturb the exact physical marginal pair transverse to the zero-price Phi hyperplane. Track which of these seven facet inequalities survives and whether the 12 simple vertices extend into adjacent marginal chambers. In parallel test a *different* physical pair for a 15-edge necessity witness. Preserve the input pin and provenance of each perturbation.
