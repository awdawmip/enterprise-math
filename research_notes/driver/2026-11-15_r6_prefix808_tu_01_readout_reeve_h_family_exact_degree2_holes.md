# PREFIX-808 boundary extension: an unbounded family of degree-two holes after a 0/1 readout of a TU source

Date: 2026-11-15. Derivation: RESEARCH_DRIVER EM-DVR-DEBB5E (source-exposed author-side extension). Original PREFIX-808 named bipartite transportation result and source: EM-DIRECT-4660FF, GitHub commit `e8329aaa77b5621dd252234925d922652039690d`. Immediate predecessor: [the TU coordinate-projection/observer boundary note]\(https://github.com/awdawmip/enterprise-math/blob/6fa101d1e03eca46483108579e074cfd5d3d1bfe/research_notes/driver/2026-11-15_r6_prefix808_tu_projection_idp_boundary_reeve_counterexample.md\) (blob `53b1b765619af1ee7c7178ac0143fa6cf4269615`). No native-X6 identification, independent review, or Native Result acceptance is asserted.

## Theorem (exact enumeration of all degree-two lattice holes)

For **every integer** \(h\ge2\), there is a bounded polytope \(P_h\subset[0,1]^{h+4}\) described by an **integer totally unimodular** equality matrix and coordinate bounds, together with a linear map \(W_h:\mathbb R^{h+4}\to\mathbb R^3\) having **only 0 and 1 coefficients**, such that the integral lattice points of the image at degree two obey
\[
\boxed{\bigl(2W_h(P_h)\cap\mathbb Z^3\bigr)
\setminus W_h\bigl(2P_h\cap\mathbb Z^{h+4}\bigr)
=\{(1,1,j):1\le j\le h-1\}.}
\tag{1}
\]
There are therefore exactly \(h-1\) degree-two lattice holes despite total unimodularity of the original source and unit nonnegative readout coefficients.

### Source system and readout

Name the source variables \(x_1,x_2,x_3,x_4,z_1,\ldots,z_h\). Let
\[
P_h=\{(x,z)\in[0,1]^{h+4}:
x_1+x_2+x_3+x_4=1,\ z_j=x_4\ (1\le j\le h)\}.
\]
The equality matrix consists of the first row with ones on \(x_1,x_2,x_3,x_4\), and rows \(z_j-x_4=0\). All columns except \(x_4\) are coordinate-unit columns (three copies of \(e_0\) and the \(e_j\)); the \(x_4\) column is (\(1,-1,\ldots,-1\)^\mathsf T). Any square subdeterminant not using the \(x_4\) column expands along unit columns to \(0,1\), or (-1). Any square subdeterminant using it expands along all other unit columns, leaving either zero or one entry of \(x_4\), again \(0,1\), or (-1). Hence the full matrix is TU for **every** \(h\).

The polytope is an affine copy of the standard 3-simplex. Its integer points are its four vertices, indexed by \(x_i=1\). Define the explicitly named, 0/1-additive readout
\[
W_h(x,z)=\Bigl(x_2+x_4,\quad x_3+x_4,\quad\sum_{j=1}^h z_j\Bigr).
\]
Every source field is retained in the source constraints; \(z_1,\ldots,z_h\) are *distinct named coordinates* linked by genuine equalities, not conflated fields. The four vertex readouts are
\[
(0,0,0),\quad (1,0,0),\quad(0,1,0),\quad (1,1,h).
\]
Thus (Q_h:=W_h\(P_h\)) is exactly the height-\(h\) Reeve tetrahedron.

### Complete degree-two lattice classification

A point (\(x,y,z\)\in 2Q_h) has real nonnegative barycentric masses \(\lambda_0,\ldots,\lambda_3\) summing to 2, with
\[
t:=z/h=\lambda_3,\qquad
\lambda_1=x-t,\quad\lambda_2=y-t,\quad
\lambda_0=2-x-y+t.
\]
Consequently
\[
(x,y,z)\in 2Q_h
\iff t\ge0,\quad x-t\ge0,\quad y-t\ge0,\quad
2-x-y+t\ge0.
\tag{2}
\]
For a lattice point, \(x,y\in\{0,1,2\}\). If \(x=0\) or \(y=0\), (2) forces \(z=0\) and a base-triangle lattice point, which is a sum of two base vertices. For (\(x,y\)=\(1,1\)), (2) permits **exactly** \(z=0,1,\ldots,h\). At (\(2,1\)) or (\(1,2\)), it forces \(z=h\); at (\(2,2\)), it forces \(z=2h\). All the latter points are sums of two of the displayed vertices, as are (\(1,1,0\)) and ((1,1,h)).

Since \(P_h\) is a bounded integral TU polytope, any integer element of \(2P_h\) is a sum of two of its four integer vertices. Equivalently this follows directly from its simplex coordinates: the \(x_i\) are nonnegative integers summing to 2, with the replicated \(z_j=x_4\). Hence all attainable degree-two readouts are sums of two of the four displayed Reeve vertices, with third coordinate in \(\{0,h,2h\}\). The **only** remaining lattice points of \(2Q_h\) are ((1,1,j)) for \(1\le j\le h-1\), establishing (1). QED.

A local exact integer enumeration using (2) for \(h=2,3,4,5,6,7\) found (10+\(h-1\)=h+9) degree-two image lattice points and exactly 10 distinct attainable source sums, with the announced \(h-1\) holes. The universal claim is proved algebraically above; finite checks are auxiliary.

## Interpretation and next dependency

This refines the single \(h=2\) witness in the predecessor note to **an arbitrarily large, completely classified degree-two defect family**. It shows that neither TU of the full named-source constraints nor 0/1-ness of a noncoordinate signed/additive readout provides a dimension-free guarantee of lattice-surjectivity or normality of the continuous observer image. The exact positive conclusion retained from PREFIX-808 is the integer decomposition of full source configurations and of their *attainable integer signature supports*: (W_h\(kP_h\cap\mathbb Z^{h+4}\)=k\, W_h\(P_h\cap\mathbb Z^{h+4}\)), as a Minkowski sum. This equality does **not** fill the above lattice holes.

For a proposed native signed-Port/Link transfer, the next discriminating test is to obtain the **actual named source equations and readout**, with preserved provenance and future operations, and either prove integral fibers for the relevant observer or construct an admissible exact counterexample within those equations. No new native ontology is inferred from this abstract TU model.

Math subunit: author-side proved and published; Native Result accepted: 0; formal Task completed: 0; mother objective completed: 0.