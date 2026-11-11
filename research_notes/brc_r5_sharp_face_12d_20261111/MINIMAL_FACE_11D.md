# Addendum — the **unique minimal common face** of all 49 sharp edges has dimension 11

Date: 2026-11-11 (Asia/Shanghai). Same frozen seven-ratio model, exact physical witness and 49-edge census as \`RESEARCH.md\`. This is a **strict strengthening** of its 12-dimensional source-3-only containing-face theorem, rather than a different physical fiber.

## Sharp theorem

Let \(\mathcal E_{\mathrm{sharp}}\) be the collection of the 49 actually realized, exact four-\(K_{2,3}\)-atom adjacent edges of the frozen physical fiber \(\mathcal F=\{E\ge0:CE=CE^0\}\) from PR #2049. Then the **unique smallest face** (under set containment) of \(\mathcal F\) containing *all* the 49 edges is

\[
\boxed{
G_{\min}=\{E\in\mathcal F:
E_{0,3}=E_{1,3}=E_{6,1}=E_{6,3}=0\}
}
\]
and it has the exact affine dimension

\[
\boxed{\dim G_{\min}=26-15=11}.
\]

The 12-dimensional face \(\,G=\{E\in\mathcal F:E_{0,3}=E_{1,3}=E_{6,3}=0\}\,\) from the parent \`RESEARCH.md\` is a **proper** superface of this unique minimal 11-dimensional face. In particular all 49 sharp adjacent edges lie in a codimension-four affine face of the original 15-dimensional fiber.

## Proof with an exact relative-interior and minimality certificate

Use the 49 rational strict edge-midpoint vectors \(E^{(k)}\) constructed from the finite exhaustive loop of \`VERIFY_SHARP_FACE.py\`, and define their average

\[
B=\frac1{49}\sum_{k=1}^{49}E^{(k)}.
\]

All \(E^{(k)}\) satisfy \(CE^{(k)}=CE^0\) and are nonnegative; thus so is \(B\). Since every summand is nonnegative, a coordinate of \(B\) vanishes **if and only if** it vanishes on all 49 strict edge interior points; because each of the 49 edge endpoints is a limit of points on its own edge, the same four vanishing coordinates are common to the whole set of edges. The completed exact finite computation establishes that the zero-coordinate set is

\[
Z_B=\{(0,3),(1,3),(6,1),(6,3)\},
\]

with all the other 26 allowed arc masses of \(B\) **strictly positive**. Hence \(B\) is in the relative interior of

\[
F_B=\{E\in\mathcal F:E_a=0\;\forall a\in Z_B\}.
\]

The face \(F_B\) contains all 49 sharp edges. To prove it is the **smallest** possible face, let \(F'\) be *any* face of \(\mathcal F\) containing all 49 edges. It contains every \(E^{(k)}\) and their average \(B\). For any \(Y\in F_B\), because \(B_a>0\) for all \(a\notin Z_B\), there is a sufficiently small rational or real \(\lambda\in(0,1)\) such that

\[
W=\frac{B-\lambda Y}{1-\lambda}\ge0,\qquad CW=CE^0.
\]

Then \(B=\lambda Y+(1-\lambda)W\in F'\) and the defining face property implies \(Y\in F'\). Therefore \(F_B\subseteq F'\) and \(G_{\min}=F_B\) is the unique minimal face containing every sharp edge.

Finally, remove the four zero columns from the 21-by-30 observer. Exact SymPy integer rank computations give

\[
\operatorname{rank}\bigl(C_{\mathcal A\setminus Z_B}\bigr)=15,\qquad
|\mathcal A\setminus Z_B|=26.
\]

The strict relative interior point \(B\) makes the affine dimension equal to \(26-15=11\), as claimed.

To show \(G_{\min}\subsetneq G\), use the explicit signed \(K_{2,3}\) residual \(H\) and epsilon from the parent theorem. Its repaired transfer \(E^\star=B+\varepsilon H\) satisfies the three source-3 zero constraints defining \(G\) yet has

\[
E^\star_{6,1}=5\varepsilon=
\boxed{\frac{227917436204790631}{173489924418985999104}}>0.
\]

Thus \(E^\star\in G\setminus G_{\min}\). QED.

## Independent extension check

Execute \`python3 VERIFY_MINIMAL_FACE.py\` alongside \`VERIFY_SHARP_FACE.py\`. It invokes the full **actual exact** 15,120-support/49-edge/35-mask checker in the same directory, checks the four zero coordinates, the 26-column rank, the strict outside-edge repair and the resulting dimension. Output in \`MINIMAL_FACE_OUTPUT.txt\`, marker \`PASS_R5_MINIMAL_SHARP_COMMON_FACE_11D\`. Both original and extension scripts executed locally; all numbers are integer or exact Fraction, rank is exact SymPy linear algebra. Proof relies on the finite domain and exact original frozen witness.

## BRC interpretation and next problem

The average \(B\) is a positive **joint branch-mass** carrier for the union of 49 residual edges, preserving labeled source-target arcs and revealing a four-coordinate exact shared obstruction. The K2,3 residual \(H\) is a **different, certified observer-invisible branch repair** that takes us *out of* the minimal 11D face and into its adjacent 12D superface, without changing the observer. This is a concrete example of how different observer-equivalent residual modes can be excluded by one extreme-edge family yet remain accessible elsewhere in the full fiber.

Next: classify all vertices and edges of the 11D minimal face, especially which non-sharp edges join the nine sharp-only trees. Test the other six source3 four-target row-only masks for full 30-arc feasibility using exact rational certificates. No shared task/Result acceptance or P000 change is inferred.