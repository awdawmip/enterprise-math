# OAI7 r372 — Mirror-pair reduction for a sharp-support residue path (odd modulus)

Date: 2026-11-19. Author-side Driver mathematical investigation / internal proof check. This is a finite combinatorial reduction of the original prime-29 five-marginal search, retaining all original ownership and source contributions. It does not constitute an independent Native Result review.

## Exact theorem

Let (p\ge3) be **odd**, (G=\mathbb Z/p\mathbb Z), and let (m\ge p-1) ordered profile shapes (W_x\in G^d) have positive rational masses (n_x/N), (\gcd(N,p)=1). Positive atoms (e=(x,t)) have weights (z_e>0); coordinate (i) outputs (t+w_{x,i}). Suppose there are exactly (S=m+p-1) positive atoms, exactly (p-1) profiles of degree two, all remaining profiles of degree one, and all (d) coordinate marginals are uniform. (No translation-inequivalence is needed for this reduction.)

Suppose the **first-coordinate contracted residue tree** is a path, with its residues ordered (v_0,v_1,\ldots,v_{p-1}) and its distinct connector profiles (x_1,\ldots,x_{p-1}). The two atoms of (x_k) are (e_k^-) at (v_{k-1}) and (e_k^+) at (v_k). Put (g_k=v_k-v_{k-1}\in G\setminus\{0\}).

**Theorem.** For every other exactly uniform coordinate (i):

1. Its contracted residue tree is also a path.
2. Once an orientation of that path is fixed, the ordering and orientation of connector atoms are obtained by independently choosing, for each mirror pair (\{k,p-k\}), one of only two operations: **keep** (x_k) at position (k) and (x_{p-k}) at position (p-k), both with original minus-to-plus order; or **swap** their positions and reverse the minus-to-plus order of both. Thus there are at most (2^{(p-1)/2}) oriented connector arrangements (before checking residue distinctness and mass cuts).
3. For a bit mask (b_k\in\{0,1\}) for (1\le k\le (p-1)/2), define the oriented step at position (j\in\{1,\ldots,p-1\}) by
   \[
   h_j=\begin{cases}
   g_j,& b_{\min(j,p-j)}=0,\\
   -g_{p-j},& b_{\min(j,p-j)}=1.
   \end{cases}
   \]
   Such a mask admits a residue-path placement **if the shape offsets can be freely chosen** exactly when the (p) partial sums
   \[
   0,\ h_1,\ h_1+h_2,\ldots,\sum_{j=1}^{p-1}h_j
   \]
   are pairwise distinct in (G). Any common translation of these partial sums gives the same relative path. Each connector's two new endpoints are a common translate of its two old endpoints, so the mask can be realized by freely choosing the coordinate-specific profile offsets. **For prescribed shapes, including the pinned OAI7 profiles, the offset recovered for each connector must coincide with its actual fixed coordinate offset under one common choice of path origin.**
4. When profile offsets are construction variables, singleton atoms can be assigned to any chosen residue. For prescribed shapes, singleton destinations are fixed by those offsets, and both connector shifts and singleton destinations must match the actual shapes. **The original first-coordinate weights give exact uniformity at coordinate (i) if and only if** its new labeled incidence tree has the same two cut signatures (c_i(e),s_i(e)) as coordinate 1 for every atom (e). This is an exact integer feasibility test from r360, not a floating-point relaxation.

For (p=29), the path family therefore reduces to at most **16,384** mirror masks per additional coordinate, followed by (29)-residue distinctness and precise integer cut checks. The bounds concern *the path-skeleton subfamily*, not all possible 378-atom supports.

## Proof

The labeled-cut theorem r360 applies because (\gcd(N,p)=1) and (S=m+p-1): every coordinate's expanded bipartite graph, and hence its contracted degree-two residue graph, is a tree; each labeled atom keeps the pair of cut values ((c(e),s(e))).

In the first path, deleting (e_k^-) on the left leaves the connector profile together with the (p-k) right-hand residues on its profile side, whereas deleting (e_k^+) on the right leaves (k) left-hand residues. Thus
\[
(c_1(e_k^-),c_1(e_k^+))=(p-k,k).
\]
In a contracted tree a connector is incident to a leaf residue exactly when one of its two atom cut counts equals 1. Consequently **exactly two** connector edges have a 1 among their atom cut counts, namely (x_1,x_{p-1}), in every uniform coordinate. A tree with exactly two leaves is a path, proving (1).

Orient the new path and let connector (x_k) occupy edge position (j). If its (e_k^-) atom is at the left endpoint, then (c_i(e_k^-)=p-j) and (c_i(e_k^+)=j), forcing (j=k). If (e_k^-) is at the right endpoint, the two counts are ((j,p-j)), forcing (j=p-k). As (p) is odd, (k\ne p-k). Bijectivity of edge positions therefore forces each mirror pair to be either kept or swapped/reversed in tandem. This proves (2).

The two endpoints of the same connector atom pair have fixed difference (g_k) in every coordinate, because both are translated by the same profile-specific offset. Hence an unchanged forward edge contributes (g_j), while a swapped/reversed edge at position (j) contributes (-g_{p-j}). Any valid residue path must have pairwise distinct partial sums; conversely, if they are distinct, set the first residue arbitrarily and place all subsequent vertices by these increments. At each labeled connector its endpoint difference is the original (g_k), so there is one candidate connector offset mapping its two atoms to the new edge; for fixed profiles that offset must match the actual one, simultaneously over all connectors after one common path translation. Singleton offsets are freely selectable only in the variable-shape model; fixed shapes fix their destinations. Applying r360's strict-positive labeled-cut converse yields (4); positivity already holds from the original first-coordinate law.

## Exact examples and proper scope

For a step-(g) first-coordinate path on a cyclic group of odd order, all (g_k=g
e0), so each (h_j\in\{g,-g\}). A sign change in consecutive steps immediately revisits the vertex from two steps earlier. The distinctness test therefore permits only the all-keep and all-swap masks, both corresponding to one common translation of every connector. This independently recovers the path special case of the r363 fixed-step obstruction.

Nontrivial geometric masks do occur for **nonconstant** path increments. At (p=5), start from the residue path
\[
(v_0,\ldots,v_4)=(4,1,3,2,0),\quad
(g_1,g_2,g_3,g_4)=(2,2,4,3).
\]
Swapping only the mirror pair (\{2,3\}) gives steps ((2,1,3,3)) and new residues ((0,2,3,1,4)), all distinct. This certifies that the mirror-mask reduction retains nontrivial shapes, rather than incorrectly extending the constant-step no-go to all paths. The example is **geometric only**; exact profile-mass cut compatibility is a separate test.

## Minimal reproducible checker

```python
from itertools import product

def path_masks(p, original_vertices):
    assert p >= 3 and p % 2 == 1
    assert len(original_vertices) == p
    assert set(original_vertices) == set(range(p))
    g=[(original_vertices[j]-original_vertices[j-1])%p for j in range(1,p)]
    outputs=[]
    for bits in product((0,1), repeat=(p-1)//2):
        steps=[g[j-1] if not bits[min(j,p-j)-1]
               else (-g[p-j-1])%p for j in range(1,p)]
        vertices=[0]
        for s in steps: vertices.append((vertices[-1]+s)%p)
        if len(set(vertices))==p: outputs.append((bits,tuple(vertices)))
    return outputs

for p in (3,5,7,9,11,13):
    # Standard constant-step path: only all-keep/all-swap.
    masks=path_masks(p, list(range(p)))
    assert len(masks)==2
    assert {bits for bits,_ in masks} == {(0,)*((p-1)//2),(1,)*((p-1)//2)}

example=path_masks(5,[4,1,3,2,0])
assert ((0,1),(0,2,3,1,4)) in example
print("r372 PASS: mirrored-path geometric sieve")
```

This program checks the combinatorial mask / residue injectivity layer only. The mass cut test is the exact integer verifier already published in r360; a candidate cannot be declared feasible until it passes that test with the pinned 350 profile numerators and all five coordinates.


## Scope correction: prescribed versus freely chosen profiles

The mirror-mask bound is a **necessary classification** for arbitrary fixed shapes; the partial-sum distinctness test characterizes path geometry with freely choosable connector offsets. For fixed OAI7 shapes, each recovered connector shift must match its prescribed relative coordinate offset for a single common path origin. Singleton-profile locations are fixed too. All candidate placements then need the exact r360 cut-signature and positivity test. The nonconstant-step p=5 example witnesses only geometric realizability for variable shapes. This correction preserves the original necessary mirror-pair reduction and does not assert a 378-row all-five-uniform construction.

## Lineage, degree of evidence and next work

Original author/researcher: **EM-EMF6D046-5A2844** on Task **RS-OAI7-028-C-20261007-6F2A81** (publication **TP2-96FAC49786245691AE19**). The new mirror-pair reduction is this Driver conversation's shared-context author contribution, reusing r360's simultaneous tree and cut-signature theorem and r363's constant-step obstruction. It is internal proof-checked and finite-tested, not an independent Native review.

References:
- r360: https://github.com/awdawmip/enterprise-math/blob/0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a/research_notes/portable_direct/2026-11-19_oai7_driver_simultaneous_cut_signature_rigidity_r360.md
- r363: https://github.com/awdawmip/enterprise-math/blob/d7cd8098c71e30220d6480a41f3d7b8322aa3ef6/research_notes/portable_direct/2026-11-19_oai7_driver_fixed_step_cycle_minimal_support_no_go_r363.md

A useful next experiment is the *actual* prime-29, 350-profile path mask/fixed-shape compatibility/mass cut sieve, using r357's pinned exact numerator vector and distinct base-shape offsets. Arbitrary contracted trees and profiles of degree three or higher remain separate unresolved families. No Task completion, Result admission or parent-objective closure is inferred.
