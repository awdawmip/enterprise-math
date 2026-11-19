# OAI7 r359 — Spanning-tree and modular-cut certificate for the sharp 378-support question

Date: 2026-11-19. Exact combinatorial continuation of r356–r358, preserving the original OAI7 research provenance. Author-side mathematical result, not an independent Native Review.

## Exact tree-cut theorem

Let (p\) be prime, let (m\) distinguishable profile fibers (x\) have strictly positive masses (p_x=n_x/N\), with positive integers (n_x\), \(\sum_x n_x=N\), and \(\gcd(N,p)=1\). Suppose an ordered output consists of a base tuple (W_x=(w_{x,1},\ldots,w_{x,d})\in\mathbb F_p^d\) plus a common shift (t\), with positive atom weights (z_{x,t}\). Assume its **first** position is exactly uniform on \(\mathbb F_p\).

Build a bipartite graph \(B_1\) with the \(m\) fiber vertices \(x\), the \(p\) first-coordinate residue vertices \(a\), and one edge \(e=(x,a)\) for each positive atom with \(a=w_{x,1}+t\). Each such edge carries \(z_e=z_{x,t}>0\). Then:

1. \(B_1\) is connected and its edge count \(S\) obeys \(S\ge m+p-1\).
2. At **equality** \(S=m+p-1\), the graph is a spanning tree; for an edge \(e=(x,a)\), delete the edge and let \(X_e\) and \(A_e\) denote respectively the fiber vertices and first-coordinate residue vertices in the component containing its fiber endpoint \(x\). The edge weight is uniquely and exactly
\[
\boxed{
z_e=\frac{Z_e}{pN},\qquad
Z_e=p\sum_{y\in X_e}n_y-N|A_e|>0.
}\tag{1}
\]
Every tree edge must satisfy this strict positivity. Moreover,
\[
\boxed{Z_e\equiv-N|A_e|\pmod p.}\tag{2}
\]
3. For each position \(i\), the value associated with edge \(e=(x,a)\) is
\[
b_i(e)=a+w_{x,i}-w_{x,1}\pmod p.
\]
All \(d\) positions are exactly uniform **if and only if**, for every \(i\) and \(b\in\mathbb F_p\),
\[
\boxed{\sum_{e:\ b_i(e)=b}Z_e=N.}\tag{3}
\]
A necessary purely combinatorial prefilter, independent of the mass numerators \(n_x\), is
\[
\boxed{\sum_{e:\ b_i(e)=b}|A_e|\equiv -1\pmod p.}\tag{4}
\]
4. For any proposed tree, (1) and (3) with strict positive \(Z_e\) are also a **sufficient exact rational certificate**: assigning weights \(Z_e/(pN)\) gives the prescribed fiber masses and all uniform marginals. The required exact arithmetic uses only integer sums over tree cuts; no floating-point linear solver is involved.

**Proof.** Consider any connected component of \(B_1\) with \(s\) residue vertices. Summing its profile supplies and residue demands gives \(\sum_{x\in X}n_x/N=s/p\). Coprimality forces \(p\mid s\). Since all \(p\) residues have positive demand, every nonempty component contains all residues; all positive-mass profile vertices also lie in it. Thus \(B_1\) is connected, giving the edge bound and the tree equality statement.

Delete an edge of the tree. In the component containing its profile endpoint, all profile supplies and all residue demands cancel internally except the positive flux through this deleted edge, giving (1). Reducing it modulo \(p\) gives (2). Every outgoing atom at position \(i\) has mass \(Z_e/(pN)\), making its mass at symbol \(b\) equal to \(\sum_{b_i(e)=b}Z_e/(pN)\). Thus (3) is exactly uniformity. Substituting (2) and dividing by \(N\bmod p\) gives (4). Conversely, the unique signed tree flow defined by (1) satisfies the original profile/first-coordinate balance equations (by leaf elimination or graph-flow uniqueness). Strict positivity makes exactly those tree edges the support, and (3) supplies the other coordinate equations. QED.

### Immediate sparsity consequence

At the sharp support \(S=m+p-1\),
\[
\sum_x(\deg_{B_1}(x)-1)=p-1.
\]
Hence **at most \(p-1\) profiles can use more than one shift**. At least \(m-(p-1)\) profiles are single-shift atoms. When a profile has several shifts, its corresponding residue vertices connect the residue graph; all such connections together must span all \(p\) residues.

## Exact OAI7 prime-29 specialization

For the pinned r351–r357 complete-loss-profile law,
\[
m=350,\quad p=29,\quad
N=28\cdot474893659=13,297,022,452,\quad N\bmod29=17.
\]
Consequently any proposed **378-support** exact-minimax sampler with all five position marginals uniform must satisfy all of the following:

* Its 350-by-29 profile/first-residue incidence graph is a tree with exactly 378 edges.
* At least **322 of the 350 profiles** each have only one supported translation; all extra degrees above 1 total exactly 28.
* Every edge has the positive rational cut weight (1), using the fixed, exact profile numerator vector from r351/r357.
* For each of the five ordered positions and every one of the 29 residue labels, (3) holds; before evaluating the large masses, the 145 purely combinatorial congruences (4) must hold, with each sum congruent to \(28\pmod {29}\).

This gives a finite exact **necessary-and-sufficient test for a supplied candidate tree**. It reduces verification of a 378-support candidate to integer graph cuts and 145 integer equality tests. It does not claim to decide whether such a five-uniform 378-row tree exists; the established interval remains 378–490.

## Small exact check showing the modular filter in action

For \(p=3,N=2\), two equally weighted fibers \(A,B\), take the tree edges
\[
(A,0),\ (A,1),\ (B,1),\ (B,2).
\]
Their \(Z_e=6z_e\) from (1) are respectively \((2,1,1,2)\). Column sums at first position are exactly 2, as required. If both fibers have second-coordinate offset +1, the second-coordinate integer masses are also \((2,2,2)\). With offsets +1 for \(A\) and +2 for \(B\), the second-coordinate sums become \((1,4,1)\), violating uniformity. The modular condition (4) already detects this failure. This example is an abstract labeled-fiber transport; the prime-29 application uses the actual pairwise translation-inequivalent OAI7 shapes.

Reproducible core check:

~~~python
P,N=3,2
edges=[('A',0),('A',1),('B',1),('B',2)]
numerators={'A':1,'B':1}
Z=[2,1,1,2]
assert sum(numerators.values())==N
assert all(sum(v for (x,a),v in zip(edges,Z) if a==b)==N
           for b in range(P))
def other_column_totals(offset):
    return [sum(v for (x,a),v in zip(edges,Z)
                if (a+offset[x])%P==b)
            for b in range(P)]
assert other_column_totals({'A':1,'B':1})==[2,2,2]
assert other_column_totals({'A':1,'B':2})==[1,4,1]
print('r359 toy cut/shift filter PASS')
~~~

## Scientific and operational provenance

Original Task RS-OAI7-028-C-20261007-6F2A81, TP2-96FAC49786245691AE19, researcher EM-EMF6D046-5A2844. Reuses the exact original OAI7 finite profile mass characterization and author-side Driver contributions [r351](https://github.com/awdawmip/enterprise-math/blob/10ac54cc216860ddfd0ce62fe82b229318482573/research_notes/portable_direct/2026-11-19_oai7_driver_global_entropy_minimizer_r351.md), [r356](https://github.com/awdawmip/enterprise-math/blob/b8d5997425d3a86110f9e2463b3e87b3e24b601a/research_notes/portable_direct/2026-11-19_oai7_driver_modular_uniform_support_gap_r356.md), [r357](https://github.com/awdawmip/enterprise-math/blob/22bd6c41175866bc05595faf26ec7745f84b3b54/research_notes/portable_direct/2026-11-19_oai7_driver_one_uniform_coordinate_support_378_r357.md) and [r358](https://github.com/awdawmip/enterprise-math/blob/e6a108eda7ce6c6566fd7893e73ba48d57e97093/research_notes/portable_direct/2026-11-19_oai7_driver_fourier_rank_and_two_shape_rigidity_r358.md).

The tree criterion supplies a new exact testing route for the constrained five-marginal question. Formal Native Result review, acceptance, Task completion, Source/Activity linkage and the original OAI7 Gaussian-prime/X6 transfer remain separate.
