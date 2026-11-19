# OAI7 r361 — Northwest-corner connector collision obstruction and the exact r357 witness

Date: 2026-11-19. An exact structural audit of the previously published r357 **one-coordinate** 378-atom minimax construction, following the r360 simultaneous-tree theorem. Author-side result, preserving the original OAI7 scientist and r347–r360 contribution provenance.

## General cyclic connector theorem

Let \(p\ge3\) be prime (or let \(\gcd(N,p)=1\)), with \(m\) positive rational source-profile masses \(n_x/N\) and uniform target masses \(1/p\). Use the standard northwest-corner transportation allocation, in any fixed source order, to give each profile \(x\) one or two output atoms, with first coordinate \(a\in\{0,\ldots,p-1\}\). Assume the support consists of the sharp \(m+p-1\) positive cells, as happens when \(\gcd(N,p)=1\) and no interior row and column boundaries coincide.

There are exactly \(p-1\) **connector profiles**, each split across adjacent first-coordinate columns \(a_x,a_x+1\), one connector for each boundary \(a_x=0,\ldots,p-2\). All other profiles occupy a single cell. Fix an ordered shape \(W_x\in(\mathbb Z/p\mathbb Z)^d\), and obtain coordinate \(i\) by the common translation \(a\mapsto a+w_{x,i}-w_{x,1}\).

For coordinate \(i\), associate to each connector the residue-edge start
\[
\boxed{s_{x,i}=a_x+w_{x,i}-w_{x,1}\pmod p.}\tag{1}
\]
Its two output residues are \(s_{x,i}\) and \(s_{x,i}+1\), so the \(p-1\) connector edges lie in the cyclic graph \(C_p\) on the \(p\) residues.

**Exact structural result.** Let \(k_i\) be the number of **distinct** connector-edge starts in position \(i\). The corresponding bipartite profile/residue incidence graph has exactly
\[
\boxed{p-k_i\text{ connected components}.}\tag{2}
\]
Consequently all-position uniformity requires \(k_i=p-1\) for every position \(i\). In particular, **one duplicated start in any other coordinate rules out that coordinate's exact uniformity** for the given northwest support. Pairwise distinct connector starts are necessary for feasibility, not sufficient: r360's further cut-signature equalities must still hold.

**Proof.** A singleton profile is a leaf and cannot join two residue vertices. Each connector profile is degree two and is equivalent, for residue connectivity, to an edge from \(s_{x,i}\) to \(s_{x,i}+1\). A proper subset of edges of the \(p\)-cycle is a forest; because at most \(p-1\) different edges are selected, there are \(p-k_i\) connected residue components. Adding the \(m\) profile vertices by subdivisions and leaves changes no component count. If the output marginal were uniform, the coprime-mass connectivity argument of r356/r360 would force a single component, hence \(k_i=p-1\). QED.

## Exact finite audit of the pinned prime-29 r357 allocation

Reconstruct the 350 canonical loss-profile representatives from r350's full test-signature grouping. Use r357's **published 350-entry ORDER** and its positive integer profile numerator vector, and perform its exact northwest allocation (29 column targets, 378 occupied cells). For each split profile, determine the pair of consecutive first-coordinate columns and evaluate (1) for all five ordered coordinates. The exact counts are:

| Ordered coordinate \(i\) | Distinct connector starts \(k_i\) | Incidence components \(29-k_i\) |
|---|---:|---:|
| 1 | 28 | 1 |
| 2 | 18 | 11 |
| 3 | 20 | 9 |
| 4 | 22 | 7 |
| 5 | 17 | 12 |

Thus **the particular published r357 northwest allocation fails all-five-coordinate uniformity already at the unweighted incidence-graph level**. This is a check of that concrete allocation, not an impossibility result for other 378-atom allocations.

A short exact witness in coordinate 2 consists of three different connectors whose starts all equal 1 modulo 29 (0-based profile row indices from r357):
- Row 12, parent orbit 47, \(W=(0,1,2,3,10)\), first-coordinate cells \((0,1)\), second-coordinate edge \((1,2)\);
- Row 296, parent orbit 37, \(W=(0,6,8,16,21)\), first-coordinate cells \((24,25)\), second-coordinate edge \((1,2)\);
- Row 309, parent orbit 23, \(W=(0,5,8,11,20)\), first-coordinate cells \((25,26)\), second-coordinate edge \((1,2)\).

Only the first two rows suffice to certify a collision. Two distinct connector profiles bridge the same pair of residues, creating the four-edge cycle \((x,1,y,2,x)\) in the coordinate-2 bipartite graph. A uniform coordinate would require a tree at 378 support by r360, so the collision is a complete exact obstruction for the published allocation.

## Reproducible extension to the pinned r350/r357 checkers

Run the unmodified **r350** checker through its \`g\`, \`CS\`, \`C\`, \`S\` and \`P\` assignments, and the unmodified **r357** checker through \`order\`, \`numerators\`, \`N\` and \`allocation\`. Then append the following deterministic integer-only verification. The two original checkers specify the finite profile grouping and exact assignment of the 350 ordered family entries; no LP or random seed is used.

~~~python
from collections import defaultdict, Counter

support_meta=[(j,c) for j in S for c in C[j]]
assert len(support_meta)==378 and len(g)==350
by_family=defaultdict(list)
for indices in g.values():
    j,c=support_meta[indices[0]]
    by_family[j].append(c)
assert all(len(by_family[j])==(14 if j in (1,2,6) else 28) for j in S)
iter_family={j:iter(by_family[j]) for j in S}
shapes=[]
for j in order:
    c=next(iter_family[j])
    shapes.append(tuple(t for t in range(P) if c&(1<<t)))
assert len(shapes)==350 and all(len(w)==5 for w in shapes)

columns=defaultdict(list)
for x,col,z in allocation:
    columns[x].append(col)
split={x:cc for x,cc in columns.items() if len(cc)==2}
assert len(split)==P-1
assert sorted(cc[0] for cc in split.values())==list(range(P-1))
assert all(cc[1]==cc[0]+1 for cc in split.values())

distinct=[]
for i in range(5):
    starts=[(cc[0]+shapes[x][i]-shapes[x][0])%P
            for x,cc in split.items()]
    distinct.append(len(set(starts)))
assert distinct==[28,18,20,22,17]
assert [(P-k) for k in distinct]==[1,11,9,7,12]
assert shapes[12]==(0,1,2,3,10) and split[12]==[0,1]
assert shapes[296]==(0,6,8,16,21) and split[296]==[24,25]
assert shapes[309]==(0,5,8,11,20) and split[309]==[25,26]
assert all((split[x][0]+shapes[x][1]-shapes[x][0])%P==1
           for x in (12,296,309))
print("r361 PASS: exact connector starts and component counts")
~~~

The output is an **exact finite combinatorial exclusion** of one published support. The loss-profile masses, r347 minimax value, the r357 one-uniform-coordinate result, the existence of a five-uniform vertex with at most 490 atoms from r353, and the open 378-atom five-uniform question are unchanged.

## Research frontier and provenance

The stronger new filter suggests searching first for connector assignments whose shifted starts are a permutation of 28 of 29 residues in **each** of the five coordinates. Survivors must then pass r360's invariant edge-cut signatures and strict positivity. This separates a small, inexpensive graph-level feasibility requirement from the heavier integer flow equations.

Original Task \`RS-OAI7-028-C-20261007-6F2A81\`, publication \`TP2-96FAC49786245691AE19\`, researcher \`EM-EMF6D046-5A2844\`. Source the original [r350 profile grouping](https://github.com/awdawmip/enterprise-math/blob/2737a8ea300816066714ef0ff8d72b62c6df2e46/research_notes/portable_direct/2026-11-19_oai7_driver_loss_profile_twin_compression_r350.md), [r357 northwest allocation](https://github.com/awdawmip/enterprise-math/blob/22bd6c41175866bc05595faf26ec7745f84b3b54/research_notes/portable_direct/2026-11-19_oai7_driver_one_uniform_coordinate_support_378_r357.md), [r359 cut test](https://github.com/awdawmip/enterprise-math/blob/12c7809e30111287c70430fdaae51bd402be626d/research_notes/portable_direct/2026-11-19_oai7_driver_tree_cut_congruence_r359.md), and [r360 simultaneous rigidity](https://github.com/awdawmip/enterprise-math/blob/0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a/research_notes/portable_direct/2026-11-19_oai7_driver_simultaneous_cut_signature_rigidity_r360.md). Author-side mathematics; no Native Result, review, Source/Activity link, CLAIM or Task/parent completion is asserted.
