# OAI7 r381 — Equal-cut core capacity and a coordinate-count obstruction

Date: 2026-11-19. Author-side finite-tree deduction from the already saved r360 labeled cut-signature theorem and r380 equal-arm saturation result. This is shared-context Driver mathematical work, not independent Native Review or frozen Result admission. Original OAI7 Task: RS-OAI7-028-C-20261007-6F2A81; immutable publication: TP2-96FAC49786245691AE19; original researcher: EM-EMF6D046-5A2844. Historical Driver: EM-DVR-DEBB5E, SID MCP-9b4714dc46b948afa4875a86c89c713c, DA DA-2C461358FCCA215C8753. All other original research contributions retain their actual authors.

## Theorem: core-size capacity for a repeated split size

Keep the r360 hypotheses: a cyclic group G=Z/pZ, positive integer profile masses n_x/N with gcd(N,p)=1, exact uniformity in all d coordinate marginals, S=m+p-1 distinct positive atoms, exactly p-1 degree-two connector profiles, all others supported once. Consequently, suppressing connector-profile nodes gives an edge-labeled tree T_i on p residue vertices in each coordinate. The *same labeled atom* preserves its profile-side residue cut size across coordinates.

Fix any integer s with 1 <= s < p/2 and let E_s be all degree-two connector labels whose edge separates s residues from the other p-s residues. Its membership is independent of coordinate. Write q=|E_s| and h=p-qs. Then:

1. **Finite core:** q s <= p-1, so h>=1. In each T_i the s-residue sides of these q edges are pairwise disjoint pendant rooted subtrees, and the complement C_i is a connected subtree of precisely h vertices. Each selected connector's original labeled atom e_x with profile-side residue cut size c_i(e_x)=s has its coordinate-i residue a_i(x) in C_i.
2. **Profile code capacity:** for each a in C_1, let E_s(a)={x in E_s : a_1(x)=a} and q_a=|E_s(a)|. At most h^(d-1) members of E_s(a) can have pairwise distinct ordered shapes modulo common translation. Therefore, under pairwise common-translation inequivalence,
   
   \[
   \boxed{q_a\le h^{d-1}\quad\text{for every }a\in C_1,\qquad q\le h^d.}
   \]
   
   Whenever h>=2, a nonempty group of size q_a imposes the necessary coordinate-count bound
   
   \[
   \boxed{d\ge 1+\lceil\log_h q_a\rceil.}
   \]
   
   For h=1, all q selected connector shapes are equivalent, so pairwise inequivalence forces q<=1.

These are **necessary** bounds for a candidate support topology; they do not claim sufficiency or replace the exact integer cut-sum/positivity tests of r360.

### Proof

Root each T_i at a centroid c_i. Every rooted child component of a centroid has size at most floor(p/2). For an edge with split sizes s,p-s and s<p/2, its s-residue side is necessarily the rooted descendant side: otherwise the first child component toward that edge would have at least p-s>p/2 vertices, contradicting centricity. Two distinct rooted descendant subtrees of equal size s cannot nest strictly, hence they are disjoint. Their union has qs vertices; deleting all q pendant subtrees leaves the connected rooted core C_i with exactly h=p-qs vertices.

For a selected connector x, the distinguished atom e_x has c_i(e_x)=s. That atom meets the larger-side residue endpoint of the connector, which is in C_i. The atom is the same translation t_x of the same profile in every coordinate, so for all i,

\[
a_i(x)=w_{x,i}+t_x,\qquad
w_{x,i}-w_{x,1}=a_i(x)-a_1(x)\pmod p.
\]

Fixing a_1(x)=a, each other a_i(x) can take only the h residue values in C_i. There are at most h^(d-1) possible ordered relative-offset vectors. Two connectors sharing that vector have common-translation-equivalent complete ordered shapes. Therefore q_a<=h^(d-1) is necessary for pairwise inequivalence. There are at most h initial attachment residues in C_1, giving q<=h^d. At h=1, all relative-offset vectors are the same, yielding the r380 saturation obstruction as a special case. QED.

## A surviving-tree-family example that is excluded at d=2

Consider p=9, d=2, the following labeled residue tree, with a 3-vertex core 0--1--2 and six pendant leaf edges:

\[
(0,1),(1,2),(0,3),(0,4),(0,5),(0,6),(1,7),(2,8).
\]

It has six edges whose smaller split side is s=1, so q=6 and h=9-6=3. Four selected connectors (edges from 0 to 3,4,5,6) share a_1=0. Since h^(d-1)=3<4, they must contain a common-translation-equivalent pair in every hypothetical two-coordinate exact-uniform sharp-support realization. This eliminates this labeled topology under pairwise-inequivalent connector shapes, without testing profile masses. Its diameter is 4 and its centroid degree is at least 3, so this is a distinct *low-coordinate* filter beyond merely requiring non-path/non-star shape. This example makes **no assertion of an additional elimination for the fixed OAI7 d=5 case**.

## OAI7 prime-29 relevance and the true remaining frontier

For p=29,d=5, the saturation case h=1 recovers r380's equal-arm exclusions. The general capacity formula gives a cheap necessary prefilter for any candidate with many equal-size cut branches; numerical profile supplies and the original five ordered offsets remain necessary to decide actual feasibility. This note does **not** tighten the currently proved 378 <= S_min <= 490 interval for the original OAI7 model.

It gives an explicit structural criterion applicable before full mass checks and a general coordinate lower bound in related cyclic models. The two still promising original-p=29 branches are unequal-arm contracted trees (degree-two-only allocation) and configurations with at least one profile of translation degree >=3.

## Reproducible finite check

The proof is universal. The following Python 3 standard-library checker exhausts all labeled trees for p=3,5,7 via Prüfer codes and verifies disjoint equal-s rooted branches, connected residual cores, and the exact h=p-qs size. It reports 3, 245 and 47047 total (tree,s)-family instances, respectively. This checks the finite-tree implementation, not the universal proof nor the complete OAI7 distribution.

~~~python
from itertools import product
from heapq import heapify, heappop, heappush
from collections import defaultdict

def tree(p, code):
    deg=[1]*p
    for v in code: deg[v]+=1
    leaves=[v for v in range(p) if deg[v]==1]
    heapify(leaves); edges=[]
    for v in code:
        u=heappop(leaves); edges.append((u,v))
        deg[u]-=1; deg[v]-=1
        if deg[v]==1: heappush(leaves,v)
    u,v=[i for i,x in enumerate(deg) if x==1]
    return edges+[(u,v)]

def check(p,edges):
    adj=[[] for _ in range(p)]
    for a,b in edges: adj[a].append(b);adj[b].append(a)
    cent=[]
    for c in range(p):
        sizes=[]
        for nb in adj[c]:
            seen={c}; todo=[nb]; n=0
            while todo:
                x=todo.pop()
                if x in seen: continue
                seen.add(x); n+=1
                todo.extend(adj[x])
            sizes.append(n)
        if max(sizes)<=p//2: cent.append(c)
    root=cent[0]
    par=[-1]*p;par[root]=root; order=[root]
    for v in order:
        for w in adj[v]:
            if par[w]<0:par[w]=v;order.append(w)
    sizes=[1]*p
    for v in reversed(order[1:]):sizes[par[v]]+=sizes[v]
    groups=defaultdict(list)
    for v in order[1:]:
        if sizes[v]<p/2:groups[sizes[v]].append(v)
    for s,vs in groups.items():
        blocks=[]
        for v in vs:
            block={v}; stack=[v]
            while stack:
                x=stack.pop()
                for w in adj[x]:
                    if w!=par[x]:
                        block.add(w);stack.append(w)
            assert len(block)==s
            blocks.append(block)
        assert all(not (a&b) for j,a in enumerate(blocks) for b in blocks[j+1:])
        core=set(range(p))-set.union(*blocks)
        assert len(core)==p-len(vs)*s
        seen={next(iter(core))};stack=list(seen)
        while stack:
            for w in adj[stack.pop()]:
                if w in core and w not in seen:seen.add(w);stack.append(w)
        assert seen==core
    return len(groups)

for p,want in ((3,3),(5,245),(7,47047)):
    total=sum(check(p,tree(p,code)) for code in product(range(p),repeat=p-2))
    assert total==want
    print(p,total)
~~~

## Source and admission boundary

Primary load-bearing theorem: [r360](https://github.com/awdawmip/enterprise-math/blob/0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a/research_notes/portable_direct/2026-11-19_oai7_driver_simultaneous_cut_signature_rigidity_r360.md). Immediate preceding equal-arm special case: [r380](https://github.com/awdawmip/enterprise-math/blob/4726e75e08ce406da2a8c9dcc2fc909f35bc8e5b/research_notes/portable_direct/2026-11-19_oai7_driver_equal_arm_saturation_obstruction_r380.md).

This author-side proof does not imply Native Result admission, independent Review, Task DONE, mother-objective completion, Source Activity linkage, a new CLAIM, or any change to existing task owner. The Driver's original queued OAI7 continuation request remains separately tracked under its own request ID.
