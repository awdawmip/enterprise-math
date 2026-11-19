# OAI7 r360 — Simultaneous tree-cut signature rigidity at minimum support

Date: 2026-11-19. Exact, author-side combinatorial theorem refining the r356–r359 five-uniform-coordinate support frontier. This note preserves the original OAI7 researcher and r347–r359 derivation provenance; it is not an independent Native Result Review.

## Theorem: identical cut signatures in every coordinate

Let \(p\ge2\), \(m\ge1\), and let \(n_x\in\mathbb Z_{>0}\), \(N=\sum_{x=1}^m n_x\), \(\gcd(N,p)=1\). For each profile \(x\), fix an ordered \(d\)-tuple \(W_x=(w_{x,1},\ldots,w_{x,d})\in(\mathbb Z/p\mathbb Z)^d\). An atom \(e=(x,t)\) has strictly positive mass \(z_e\) and output \(b_i(e)=t+w_{x,i}\pmod p\) at position \(i\). Distinct atoms have distinct \((x,t)\), and \(\sum_{e:x(e)=x}z_e=n_x/N\).

Assume \(S=m+p-1\) positive atoms, and **all \(d\) position marginals are uniform** on the \(p\) residues. For every \(i\), form the bipartite incidence graph \(B_i\) on all \(m\) profile vertices and all \(p\) residue vertices, with an *edge labeled by the same atom \(e\)* joining \(x(e)\) to \(b_i(e)\).

Then:

1. **Simultaneous trees.** Every \(B_i\) is a spanning tree (not merely \(B_1\)).
2. Delete a labeled edge \(e\) from \(B_i\). Let \(X_i(e)\) be the profiles and \(A_i(e)\) the residues in the component containing the profile endpoint of \(e\). The two integer cut signatures
   \[
   c_i(e)=|A_i(e)|,\qquad s_i(e)=\sum_{y\in X_i(e)} n_y
   \]
   are **independent of coordinate**:
   \[
   \boxed{c_i(e)=c_j(e),\quad s_i(e)=s_j(e)\quad(\forall e,i,j).}\tag{1}
   \]
3. **Exact converse and certificate.** Suppose a proposed \(S=m+p-1\) labeled support has \(B_1,\ldots,B_d\) all spanning trees. Put
   \[
   Z_e=p\,s_1(e)-N\,c_1(e),\qquad z_e=\frac{Z_e}{pN}.
   \]
   This proposed support carries a strictly positive law with the specified profile masses and all \(d\) exactly uniform marginals **if and only if** (a) \(Z_e>0\) for every edge and (b) (1) holds for all labeled edges. The weights are then unique.

This yields a two-stage exact filter: reject a candidate immediately if any coordinate incidence graph is disconnected/cyclic, or if any **residue cut size** differs across coordinate graphs; only surviving candidates need the profile-numerator cut sums. Unlike a floating-point linear feasibility solver, this test uses finite graph traversal and integer arithmetic.

## Proof

For any position \(i\), every connected component of \(B_i\) contains entire profile vertices and their full masses. If a component has \(a\) residue vertices, its mass is both \(a/p\) and an integer multiple of \(1/N\). Hence \(p\mid a\), by \(\gcd(N,p)=1\). All \(p\) residue vertices have positive uniform demand and all \(m\) profile supplies are positive, so \(B_i\) is connected. It has \(m+p\) vertices and \(S=m+p-1\) edges, therefore is a tree.

In a tree, summing the profile supplies and uniform residue demands on the profile-side component after removing \(e\) gives exactly the sole crossing-edge flow:
\[
pNz_e=p\,s_i(e)-N\,c_i(e).\tag{2}
\]
The same physical atom has the same mass in all coordinates, so for any \(i,j\)
\[
p(s_i(e)-s_j(e))=N(c_i(e)-c_j(e)).
\]
Coprimality forces \(p\mid(c_i(e)-c_j(e))\). Since deletion of an edge of a spanning tree puts at least one vertex of each type of endpoint on opposite sides, \(0\le c_i(e),c_j(e)\le p-1\). Therefore \(c_i(e)=c_j(e)\), and the preceding equality then gives \(s_i(e)=s_j(e)\). This proves (1).

Conversely, for a bipartite tree with fixed profile supplies \(n_x/N\) and residue demands \(1/p\), the unique (possibly signed) solution to the vertex-balance equations is the cut flow in (2). One may check this by deleting leaves successively; all supplies/demands sum to 1. Condition (1) says that the \(B_1\) cut-flow vector, edge by edge, equals the unique cut-flow solution on every \(B_i\). Positivity makes it an admissible law. Necessity was already proved. QED.

### Prime-29 OAI7 consequence

The pinned r351/r357 minimax profile masses have \(p=29\), \(m=350\), \(N=13,297,022,452\), \(N\bmod29=17\), and five ordered positions. If the 378-support endpoint of the open five-uniform problem is feasible, **each of its five residue/profile incidence graphs must be a spanning tree**. For each of the 378 labeled atom edges, the five profile-side cut counts \(c_i(e)\) must all agree in \(\{0,\ldots,28\}\), and the five integer sums \(s_i(e)\) must all agree. This is a substantially more local candidate-tree sieve than computing 145 full marginal sums for each proposed support; it is a necessary-and-sufficient exact validator when all trees and positive cut masses are supplied.

The result **does not decide** whether an OAI7 378-support five-uniform sampler exists. The proven support interval remains 378–490. It refines the feasible-support search and the exact certification route, not the parent Gaussian-prime/X6 transfer.

## Finite demonstration and standalone verifier (Python 3)

The following small example uses \(p=3\), \(N=2\), two profiles with masses \(1/2,1/2\), and the same four labeled edges \(A0,A1,B1,B2\) in coordinate 1. Both coordinate incidence graphs are trees even with differing offsets, so treehood alone is insufficient. If the second-coordinate offsets are +1 for A and +2 for B, the per-edge residue cut counts differ; no strictly positive four-atom law can have both coordinates uniform. If both offsets are +1, the signatures match and the first-coordinate masses \((2,1,1,2)/6\) also make the second marginal uniform.

~~~python
from collections import defaultdict

def cuts(p, numerators, edges, offsets, coord):
    m=len(numerators)
    assert len(edges)==m+p-1
    adj=defaultdict(list)
    endpoints=[]
    for e,(x,a) in enumerate(edges):
        u=x
        v=m+(a+offsets[x][coord])%p
        adj[u].append((v,e)); adj[v].append((u,e))
        endpoints.append((u,v))
    seen={0}; stack=[0]
    while stack:
        for v,_ in adj[stack.pop()]:
            if v not in seen:
                seen.add(v); stack.append(v)
    if len(seen)!=m+p:
        return None
    sig=[]
    for e,(u,v) in enumerate(endpoints):
        seen={u}; stack=[u]
        while stack:
            for vv,ee in adj[stack.pop()]:
                if ee!=e and vv not in seen:
                    seen.add(vv); stack.append(vv)
        assert v not in seen
        sig.append((sum(y>=m for y in seen),
                    sum(numerators[y] for y in seen if y<m)))
    return sig

p=3
numerators=(1,1)
N=sum(numerators)
edges=[(0,0),(0,1),(1,1),(1,2)]
first=cuts(p,numerators,edges,((0,1),(0,2)),0)
bad=cuts(p,numerators,edges,((0,1),(0,2)),1)
good=cuts(p,numerators,edges,((0,1),(0,1)),1)
assert first==[(2,2),(1,1),(1,1),(2,2)]
assert bad==[(1,1),(2,2),(2,2),(1,1)]
assert good==first
weights=[p*s-N*c for c,s in first]
assert weights==[2,1,1,2]
assert all(z>0 for z in weights)
for offsets,expect in [(((0,1),(0,2)),False),
                       (((0,1),(0,1)),True)]:
    totals=[[sum(z for (x,a),z in zip(edges,weights)
                  if (a+offsets[x][i])%p==b)
             for b in range(p)] for i in range(2)]
    assert (all(col==[N]*p for col in totals))==expect
print("r360 PASS: simultaneous-tree cut-signature rigidity")
~~~

## Provenance and integration

Original Task: \`RS-OAI7-028-C-20261007-6F2A81\`, immutable publication \`TP2-96FAC49786245691AE19\`, original researcher \`EM-EMF6D046-5A2844\`. Extends [r356](https://github.com/awdawmip/enterprise-math/blob/b8d5997425d3a86110f9e2463b3e87b3e24b601a/research_notes/portable_direct/2026-11-19_oai7_driver_modular_uniform_support_gap_r356.md), [r357](https://github.com/awdawmip/enterprise-math/blob/22bd6c41175866bc05595faf26ec7745f84b3b54/research_notes/portable_direct/2026-11-19_oai7_driver_one_uniform_coordinate_support_378_r357.md), [r358](https://github.com/awdawmip/enterprise-math/blob/e6a108eda7ce6c6566fd7893e73ba48d57e97093/research_notes/portable_direct/2026-11-19_oai7_driver_fourier_rank_and_two_shape_rigidity_r358.md) and [r359](https://github.com/awdawmip/enterprise-math/blob/12c7809e30111287c70430fdaae51bd402be626d/research_notes/portable_direct/2026-11-19_oai7_driver_tree_cut_congruence_r359.md). This is author-side proof/computation, not independent native review, acceptance, formal Activity linkage, a task CLAIM, or mother-objective closure.
