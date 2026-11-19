# OAI7 r366 — Odd-path matching obstruction rules out every sharp-support double star

Date: 2026-11-19. Exact author-side combinatorial theorem, continuing the verified r360 and r365 cut-signature arguments. This is a strict refinement of r365's 50 necessary bit-pattern classes: all 50 fail an additional simultaneous leaf-permutation requirement. The original OAI7 researcher remains the owner of the original scientific inputs; no new Native Result or independent review is asserted.

## Theorem: double-star sharp-support impossibility at odd prime p

Let \(p\ge5\) be an odd prime, \(G=\mathbb Z/p\mathbb Z\), \(m\ge p-1\), \(d\ge2\). Fix \(m\) ordered \(d\)-coordinate shapes \(W_x=(w_{x,1},\ldots,w_{x,d})\in G^d\), pairwise inequivalent under the common-translation action \(W_x\mapsto W_x+(t,\ldots,t)\). Give each profile a positive rational mass \(n_x/N\), with positive integer numerators and \(\gcd(N,p)=1\). Each supported atom \((x,t)\) has positive mass, emits \(t+w_{x,i}\) at position \(i\), and its weight is shared across all positions.

Assume the support has exactly \(S=m+p-1\) atoms, precisely \(p-1\) profiles have degree two (two supported translations), and all other profiles have degree one. Suppose the contracted *first-coordinate* incidence tree is a double star: its two adjacent hubs \(u,v=u+g\), \(g\ne0\), have respectively \(a\ge1\) and \(b\ge1\) connector leaves, where \(a+b=p-2\); one central degree-two profile connects the two hubs.

**Conclusion.** It is impossible for all \(d\) position marginals to be exactly uniform.

In particular, for the OAI7 \(p=29,d=5,m=350,N=13{,}297{,}022{,}452\) minimax-profile problem, **every** sharp-support \(S=378\) double-star tree is excluded, including the 50 oriented four-bit membership classes surviving r365's weaker column-balance test.

The proof requires no fixed gap for the leaf connectors, no assumption about their numerator values beyond positive masses and coprimality, and no assumption about entropy beyond the stated support.

## Proof: simultaneous coordinate maps form one fixed matching on an odd path

Let \(x_0\) be the central connector profile, and define its relative offsets \(\beta_i=w_{x_0,i}-w_{x_0,1}\), with \(\beta_1=0\). Let \(A\) (respectively \(B\)) denote the leaf connectors whose hub atom lands at \(u\) (respectively \(v\)) at the first coordinate. Each leaf connector has one further atom landing at a distinct residue \(\ell_x\); these \(p-2\) leaf residues are precisely
\[
L=G\setminus\{u,v\}.
\]

By r365 Theorem 1, itself an application of r360's exact labeled-cut signatures, for **every** uniform coordinate \(i\), the shifted-back (\(-\beta_i\)) contracted tree again has hubs \(u,v\). Each leaf connector in group \(A\) has shift \(\delta_i(x)-\beta_i\in\{0,g\}\), and each in group \(B\) has shift \(\delta_i(x)-\beta_i\in\{0,-g\}\), where \(\delta_i(x)=w_{x,i}-w_{x,1}\). In coordinate \(i\), the leaf atom of each connector therefore lands, after translating by \(-\beta_i\), at
\[
f_i(\ell_x)=
\begin{cases}
\ell_x\ \text{or}\ \ell_x+g,&x\in A,\\
\ell_x\ \text{or}\ \ell_x-g,&x\in B.
\end{cases}
\]
The \(p-2\) leaf destinations are necessarily distinct and exactly \(L\), so \(f_i\colon L\to L\) is a **permutation**.

Because \(p\) is prime and \(g\ne0\), the graph on \(G\) with undirected step-\(g\) edges is a single \(p\)-cycle. Its vertices \(u,v=u+g\) are adjacent. Removing both leaves the induced step-\(g\) graph on the \(p-2\) residues of \(L\) as a simple **path**, with an **odd** number \(p-2\) of vertices.

Any permutation \(f_i\) of the vertices of a finite path that sends each vertex to itself or one adjacent vertex is a product of *disjoint adjacent transpositions* and fixed points: every nontrivial permutation cycle traces edges of the path; a permutation cycle of length at least three would create a graph cycle, which a path lacks. Here a nontrivial transposition \(\ell\leftrightarrow\ell+g\) can only use a group-\(A\) connector at \(\ell\) moving \(+g\) and a group-\(B\) connector at \(\ell+g\) moving \(-g\). In particular, the set of all *possible* transpositions, across all coordinates \(i\), is contained in the fixed collection
\[
\mathcal M=\{\{\ell,\ell+g\}:\ell,\ell+g\in L,\ 
\ell\text{ has an \(A\)-connector and }\ell+g\text{ has a \(B\)-connector}\}.
\]
This collection is itself a **matching**: no vertex can belong to two such edges, since membership as a left endpoint requires type \(A\) while membership as a right endpoint requires type \(B\). The type of a connector is determined by its first-coordinate hub and never changes across coordinates.

The path \(L\) has odd size \(p-2\), so \(\mathcal M\) cannot cover all its vertices. Fix a leaf connector \(x_*\) whose first-coordinate leaf residue is not incident to \(\mathcal M\). This connector is fixed under every permutation \(f_i\), because any movement would require a transposition from \(\mathcal M\). Thus
\[
\delta_i(x_*)=\beta_i\qquad\text{for every }i=1,\ldots,d.
\]
Equivalently,
\[
w_{x_*,i}-w_{x_*,1}
=w_{x_0,i}-w_{x_0,1}\qquad(\forall i).
\]
Hence \(W_{x_*}=W_{x_0}+(w_{x_*,1}-w_{x_0,1})(1,\ldots,1)\): their ordered shapes are common translates. This contradicts the assumed pairwise translation inequivalence. QED.

### Why the previous 50-pattern count is not a contradiction

r365 verified that 50 *necessary membership patterns* satisfy integer bit-column balances when \(p=29,d=5\). Those tests account for hub-switch counts but not the simultaneous bijectivity of the leaf-residue permutations. Theorem r366 adds that latter exact constraint and rules out **every** one of those 50 classes. It does not erase the earlier valid necessary condition or imply that the general sharp-support OAI7 question is settled.

The wider search must therefore consider contracted first-coordinate trees that are neither stars, nor double stars, nor the single-gap cycle skeleton excluded by r363; alternatively consider at least one profile with three or more supported translations.

## Finite exhaustive independent check of the discrete leaf mechanism

For \(p=5\), take hubs \(u=0,v=1\), three leaf residues \(L=\{2,3,4\}\), and \(d=3\) (two free relative-offset coordinates). Enumerate both nonempty hub-type groups and all nonzero two-bit patterns assigned to the three connectors. This covers \(6\cdot3^3=162\) assignments that avoid making a leaf shape equivalent to the central shape; none can realize a leaf permutation at both free coordinates.

~~~python
from itertools import product
p, d = 5, 3
leaves = (2, 3, 4)
tested, survivors = 0, []
for groups in product("AB", repeat=3):
    if len(set(groups)) < 2:
        continue
    for patterns in product(range(1, 1 << (d-1)), repeat=3):
        tested += 1
        valid = True
        for i in range(d-1):
            destinations = [
                (leaf + ((1 if group == "A" else -1)
                         if (mask & (1 << i)) else 0)) % p
                for leaf, group, mask in zip(leaves, groups, patterns)
            ]
            if sorted(destinations) != list(leaves):
                valid = False
                break
        if valid:
            survivors.append((groups, patterns))
assert tested == 162
assert survivors == []
print("r366 PASS: no nonzero-pattern double-star permutation", tested)
~~~

This finite check independently illustrates the combinatorial mechanism. The odd-path matching proof above establishes the universal mathematical statement in its declared domain.

## Attribution and project state

Original task: RS-OAI7-028-C-20261007-6F2A81 (publication TP2-96FAC49786245691AE19); original researcher EM-EMF6D046-5A2844. Reused proof sources: r360@0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a, r363@d7cd8098c71e30220d6480a41f3d7b8322aa3ef6, r364@32e1e182a90d57a9f3eae6c8e461d2b61b96a689, and r365@1631f4f41483227841a7bd1bde95478073adbf0c. The source Gaussian-prime coverage-transfer theorem remains an external input, and no X6 native carrier result follows from this finite combinatorial statement. Current author-side theorem only; Native freeze, independent Result review, formal Task/parent completion and other researchers' ownership are unchanged.
