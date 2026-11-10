# R5: a four-dimensional product-type Blackwell transport face at the interior 14-edge contact

Date: 2026-11-10 (Asia/Shanghai). Status: **author-side exact proof and computational certificate**. No independent reviewer admission or formal R5 CLAIM is asserted. Frozen scientific sources unchanged: GLOBAL \`a01383f825ef9d43b4b754254303298c64041568\`; Enterprise Math \`86149263e38c22292c9def1e0f69092efa1be77e\`. Source: predecessor Draft PR #1954 at \`6f01b6424cc5563db7976fa8131ef687c15091ca\`, in particular \`research_notes/brc_r5_first_contact_sheet_20261110_t1235/RESEARCH.md\`. The accompanying standalone verifier reproduces the frozen exact seven-likelihood-ratio model without executing any prior script. P000 and ACTIVE X6 worldview remain unchanged.

## Exact theorem: 18-arc face with product combinatorics

In the frozen 30-arc, 21-marginal/martingale-equation Blackwell model and lawful eight-parameter physical family \`p(z)=p0+P*(tstar+z)\`, take
\[
R=\frac{49948501046391}{3920403670319950000},\qquad z_c=R(-1,1,1,-1,-1,-1,-1,1).
\]
Define ten forced arc labels
\`\`\`text
F={(0,0),(0,1),(0,2),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6)}
G1={(2,1),(3,1),(4,1)}
G2={(3,2),(4,2)}
G3={(0,3),(2,3)}
\`\`\`
Set all other arc masses to zero except these 10+3+2+2+1=18 allowed arcs \`D18=F∪G1∪G2∪G3∪{(1,5)}\`. Because the original transport polytope is defined by nonnegativity and linear equalities, its intersection with these coordinate equalities is a face.

**At zc this restricted coupling face has affine dimension four and is combinatorially equivalent to \(\Delta_2\times\Delta_1\times\Delta_1\), with f-vector (12,24,19,7).** Its 12 distinct vertices are all strictly positive on exactly 14 arcs: all ten of F, the fixed arc (1,5), and exactly one label chosen from each of the groups G1,G2,G3. Its seven facets correspond exactly to zeroing one of the 3+2+2 group arcs. The 3 G1 facets each contain 8 vertices, and each of four G2/G3 facets contains 6. No 13-or-fewer-arc coupling lies within this 18-arc face. The barycenter of these 12 couplings has all 18 arcs strictly positive.

Let
\[
 n=(34101,-293725,-85599,42525,937899,293725,85599,-3287440),\quad
 H=\{z:n\cdot(z-z_c)=0\}.
\]
There is a nonempty relative-open seven-dimensional neighborhood inside H where the 18-arc face remains nonempty and has exactly the same 12 strictly-positive-on-14-arcs vertices and face lattice. This supplies a locally stable four-dimensional **transport-observer fiber** at every such physical point. Product terminology concerns the combinatorial face lattice; it makes no metric independence claim for physical parameters or edge masses.

## Proof and exact finite exhaustion

1. The full arc column \`(i,j)\` in the 21-row Blackwell system is \`e_i+e_(7+j)+r_i*e_(14+j)\`, for \`r=(1/10,1/2,3/4,1,5/4,3/2,19/10)\`. A specified 15-row reduction has rank 15; its restriction to D18 has exact rank **14**. At zc the original five physical equalities hold and all 26 physical capacity slacks are nonnegative: only the structural indices 4,15,23 vanish, the others are strictly positive.

2. For each of the \`3*2*2=12\` choices \`(a,b,c)∈G1×G2×G3\`, solve the corresponding 14-column matrix for the fixed physical right-hand side with rational arithmetic. Each matrix has rank 14 and yields 14 strictly positive rational edge masses. Verify the complete **21 original marginal and martingale equalities**, not only the rank-reduced rows. These are 12 distinct vertices.

3. To show completeness independent of predecessor support enumerations, express all 18-arc solutions as \`E=E0+K*t\` using the 18×4 rational nullspace matrix K. This is a bounded dimension-four polytope, and the barycenter of the exhibited vertices is strictly positive in every coordinate. Therefore each vertex is an intersection of at least four independent active coordinate inequalities \`E_e=0\`. Enumerate all \`C(18,4)=3060\` four-coordinate subsets, solving each exact 4×4 rational system. Exactly **324** systems are nonsingular, and exactly **12 distinct** resulting solutions are coordinatewise nonnegative; these coincide with the twelve constructed vertices. This is a complete finite proof for **the restricted 18-arc face**, including degenerate intersections.

4. Compute the affine rank of each coordinate-zero vertex set. Exactly seven zero-coordinate sets yield facets of affine rank 3: those indexed by G1∪G2∪G3. Every vertex is incident to exactly four facets (two unchosen G1, one unchosen G2 and one unchosen G3), which is the incidence of \`Δ2×Δ1×Δ1\`. Neighboring vertices differ in exactly one group choice; there are \`12*4/2=24\` edges and, by the Euler identity for the 3-dimensional boundary of this four-dimensional polytope, \`f2=f1+f3-f0=24+7-12=19\`.

5. The restricted 15×18 matrix has a one-dimensional left kernel. The compatibility functional of its right-hand side has parameter slope proportional to the exact primitive integral normal n, and vanishes at zc. Hence the right-hand side stays in its image for every z∈H. Each of the 12 nondegenerate 14-column vertex masses depends affinely and continuously on z and is strictly positive at zc. For the other finitely many nonsingular candidate intersections, some coordinate is strictly negative at zc, so a sufficiently small common relative neighborhood excludes all of them. Physical strict slacks and the incidence conditions persist, proving the relative-open H theorem.

## Certificate and reproducibility

\`VERIFY_FACE.py\` is a self-contained checker using only standard Python \`fractions.Fraction\`, \`itertools\`, and SymPy rational linear algebra. It executes all 3,060 intersection tests (324 nonsingular) and all 12 full original 21-equation checks, asserts the seven facet ranks, f-vector, and frozen physical constraints. \`EXACT_OUTPUT_FACE.txt\` contains the stdout of an actual local execution of this specific program. There is no floating-point tolerance, random sampling, unexecuted previous program, or inferred numerical LP output.

The full-30-arc minimum-support classification near zc remains as certified and scoped in predecessor PR #1954 and its earlier sources; the new complete 3,060-set enumeration is specifically for D18. Prior proof review and formal Result admission remain separate.

## Typed BRC interpretation

Population: positive-rational nonnegative transports on the 30 labelled allowed arcs; the declared observer is the full 21-row Blackwell right-hand side (not merely total mass). Branch identities are ordered likelihood-pair labels (i,j), not native spatial X6 axes. The 18-arc support restriction preserves a four-dimensional hidden transport fiber while the observable stays fixed. The twelve sparse extremal branches cannot be reconstructed from the observer alone: retain a one-of-3, one-of-2 and one-of-2 branch-choice coordinate when the selected coupling matters. All statements concern nonnegative positive mass, not signed/amplitude cancellation.

## Next research unit

For each of the twelve 14-arc vertex bases, find the first lawful hyperplane inside H where a currently positive edge mass vanishes, accounting for all 26 original physical slacks. Test these boundary points for a **global** 13-arc coupling among all 30 allowed arcs, and if found certify its optimality by finite ≤12-edge exclusion. Distinguish a change to the 18-arc face from a change to the global minimum support.