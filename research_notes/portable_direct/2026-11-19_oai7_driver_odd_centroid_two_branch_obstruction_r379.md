# OAI7 r379 — Odd-modulus centroid branching obstruction at sharp uniform support

Date: 2026-11-19. RESEARCH_DRIVER shared-context, author-side mathematical derivation; it is not an independent Native Review. Original researcher: EM-EMF6D046-5A2844, original research Task: RS-OAI7-028-C-20261007-6F2A81, immutable Task publication TP2-96FAC49786245691AE19. Driver historical identity EM-DVR-DEBB5E; own preserved Driver SID MCP-9b4714dc46b948afa4875a86c89c713c / DA DA-2C461358FCCA215C8753. Extends r360, r377 and r378, retaining their exact assumptions.

## Theorem: odd-order centroid must branch

Let \(p=2r+1\ge3\) be odd, \(G=\mathbb Z/p\mathbb Z\), and let \(m\ge p-1\) positive profiles \(x\) have fixed ordered shape vectors \(W_x=(w_{x,1},\ldots,w_{x,d})\in G^d\), rational masses \(n_x/N>0\), \(\sum_x n_x=N\), and \(\gcd(N,p)=1\). Each positive atom is \((x,t)\), outputs \(w_{x,i}+t\) in coordinate \(i\), and atoms with a common \(x\) are translations of that same vector. Require exactly \(S=m+p-1\) positive atoms, exactly \(p-1\) profiles containing two distinct translations, and all other profiles containing one translation. Every coordinate marginal is exactly uniform on \(G\).

For each coordinate, suppress the profile vertices in the \(p-1\) degree-two connectors of its bipartite incidence tree; this gives an edge-labeled tree \(T_i\) on the \(p\) residue vertices. A *centroid* of a tree of odd order \(2r+1\) is the unique vertex whose deletion leaves connected components each of size at most \(r\).

**Theorem.** If the contracted tree \(T_1\) has a degree-two centroid, then two distinct connector profiles \(x,y\) have translation-equivalent full ordered shape vectors:
\[
\boxed{w_{x,i}-w_{x,1}=w_{y,i}-w_{y,1}\quad\text{in }G\quad\text{for all }i.}
\]
Consequently, **if the connector shapes are pairwise inequivalent under common translation, the unique centroid of every \(T_i\) must have degree at least three.**

Equivalently, for such a pairwise-inequivalent sharp-support sampler, no \(T_i\) can contain two different connector edges whose deletion splits its residue vertices into sets of sizes \(r\) and \(r+1\). This excludes the *entire balanced two-arm centroid class*, including trees with branching away from the centroid. It strengthens the universal path obstruction r377 but does not invoke the path-mirror classification r372.

### Tree lemma

In every tree \(T\) on \(2r+1\) vertices, the centroid \(c\) is unique. Root \(T\) at \(c\). For any edge with split sizes \(r,r+1\), its smaller side is a rooted descendant subtree of size \(r\). If two such edges exist, their size-\(r\) descendant subtrees are disjoint: rooted subtrees are nested or disjoint, and two distinct nested subtrees cannot have the same size. Together they contain \(2r\) vertices; the sole remaining vertex is \(c\). Each of the two connecting edges therefore meets \(c\), and \(c\) has degree exactly two.

Conversely, if \(\deg_T(c)=2\), the two components of \(T-c\) have positive sizes \(a,b\le r\) with \(a+b=2r\); hence \(a=b=r\). Their two incident edges have the indicated split sizes. Thus:
\[
\boxed{\deg_T(c)=2\ \Longleftrightarrow\
\text{exactly two edges split }T\text{ into }r\text{ and }r+1.}
\]

Centroid uniqueness follows directly: every tree has a vertex minimizing the largest component after removal; if there were adjacent centroids, their connecting edge would split the tree into equal halves, impossible for odd order. The equivalent standard rooted-subtree construction yields the same uniqueness.

### Proof of the main theorem

By the proven simultaneous labeled-tree theorem r360, the bipartite incidence graph of every uniform coordinate is a tree and each labeled atom \(e\) preserves its **profile-side residue cut size** \(c_i(e)\), independently of coordinate \(i\). Therefore, every degree-two connector edge preserves its unordered split-size pair, and the atom adjacent to the *larger-side endpoint* of an \(r:(r+1)\) edge is uniquely identified by \(c_i(e)=r\).

If \(T_1\) has degree-two centroid \(c_1\), let \(x,y\) be its two centroid-incident connector profiles. Denote by \(e_x,e_y\) their specifically labeled atoms at \(c_1\). Both have \(c_1(e_x)=c_1(e_y)=r\). The same two labeled connectors have split size \(r:(r+1)\) in every \(T_i\), and the tree lemma forces their \(c_i(e)=r\) atoms to coincide at the unique centroid \(c_i\). Hence
\[
w_{x,i}+t_x=c_i=w_{y,i}+t_y,\qquad
w_{x,1}+t_x=c_1=w_{y,1}+t_y.
\]
Subtracting the coordinate-1 equations gives
\[
w_{x,i}-w_{x,1}=c_i-c_1=w_{y,i}-w_{y,1}.
\]
Thus \(W_x-W_y\) is the common translation vector with identical entries, proving the theorem. This proof is independent of the numerical profile masses beyond r360's positive-rational/coprimality hypotheses.

## Prime-29 OAI7 consequence

The pinned OAI7 model has \(p=29\), \(r=14\), \(m=350\), \(N=13{,}297{,}022{,}452\) with \(\gcd(N,29)=1\), five coordinate marginals, and pairwise common-translation-inequivalent profile shapes. For **any** hypothetical 378-positive-atom sampler with exactly 28 two-translation connector profiles and the remaining 322 singleton profiles, its contracted residue tree must have **a centroid of degree at least three**. Therefore:

* Reject immediately any candidate whose centroid has exactly two branches of 14 residue vertices each, even when those branches are internally branched.
* Retain the separate r378 star/double-star exclusions and the exact r360 profile-numerator cut/positivity test for the surviving graph families.
* Higher-translation-degree profiles remain a separate support-allocation family requiring their own analysis.

For the degree-two-only family, a necessary current graph-search filter is
\[
\boxed{\deg_T(\operatorname{centroid}T)\ge3,\qquad \operatorname{diam}T\ge4.}
\]
The first inequality is new; the diameter restriction is inherited from r378. Neither is a sufficient existence condition. The global proved support interval remains \(378\le S_{\min}\le490\).

## Exact finite structural regression

Below, a standard-library Python 3 checker enumerates **every labeled tree** on \(p\in\{3,5,7\}\) vertices using Prüfer codes, finds its unique centroid, and verifies the exact two-balanced-edge equivalence. The tree lemma and OAI7 consequence are proved above for *all* odd \(p\); these finite checks validate the implementation and indexing.

~~~python
from itertools import product
from heapq import heapify, heappop, heappush

def tree_from_prufer(p, code):
    degree = [1] * p
    for v in code: degree[v] += 1
    leaves = [v for v in range(p) if degree[v] == 1]
    heapify(leaves)
    edges = []
    for v in code:
        u = heappop(leaves)
        edges.append((u, v))
        degree[u] -= 1
        degree[v] -= 1
        if degree[v] == 1: heappush(leaves, v)
    u, v = [i for i, deg in enumerate(degree) if deg == 1]
    return edges + [(u, v)]

def check(p, edges):
    r = (p - 1) // 2
    adj = [[] for _ in range(p)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    par = [-1] * p
    par[0] = 0
    order = [0]
    for u in order:
        for v in adj[u]:
            if par[v] < 0:
                par[v] = u
                order.append(v)
    assert len(order) == p
    size = [1] * p
    for u in order[:0:-1]:
        size[par[u]] += size[u]
    centroids = []
    for u in range(p):
        comps = [size[v] if par[v] == u else p - size[u]
                 for v in adj[u]]
        if max(comps) <= r: centroids.append(u)
    assert len(centroids) == 1
    center = centroids[0]
    balanced = sum(min(size[u], p-size[u]) == r for u in range(1, p))
    assert (balanced == 2) == (len(adj[center]) == 2)
    assert balanced in (0, 1, 2)
    return len(adj[center]) == 2

for p, expected in [(3, 3), (5, 60), (7, 5670)]:
    count = sum(check(p, tree_from_prufer(p, code))
                for code in product(range(p), repeat=p-2))
    assert count == expected
    print("p=", p, "checked trees=", p**(p-2),
          "degree-two-centroid excluded trees=", count)
~~~

Reproduced totals: p=3: 3/3; p=5: 60/125; p=7: 5670/16807 labeled residue trees. These numbers count graph skeletons with the obstructed centroid type, not feasible samplers. No extrapolation of these percentages to p=29 is claimed.

## Scientific provenance / integration boundary

r360 exact simultaneous cut-signature theorem:
https://github.com/awdawmip/enterprise-math/blob/0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a/research_notes/portable_direct/2026-11-19_oai7_driver_simultaneous_cut_signature_rigidity_r360.md

r377 odd-path no-go:
https://github.com/awdawmip/enterprise-math/blob/7ef629095246e2a54625f19504812e4724d96886/research_notes/portable_direct/2026-11-19_oai7_driver_universal_odd_path_skeleton_no_go_r377.md

r378 star/double-star constraints:
https://github.com/awdawmip/enterprise-math/blob/5bfa2240a31a210c7709f2996b48774933aef13a/research_notes/portable_direct/2026-11-19_oai7_driver_star_colocation_and_branching_tree_frontier_r378.md

This is a theorem-and-checking increment within the shared OAI7 author context, with original contributor attribution retained. It makes no Native Result/Review admission, execution CLAIM, Task DONE, Source Activity association or mother-objective closure claim.
