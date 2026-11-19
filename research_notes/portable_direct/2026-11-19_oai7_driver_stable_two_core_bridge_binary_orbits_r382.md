# OAI7 r382 — Stable two-vertex core: exact binary-translation orbit capacity

Date: 2026-11-19. Author-side mathematical continuation of r360/r381 in the original RESEARCH_DRIVER lane; no independent Native Review or frozen Result is asserted.

Original Task: RS-OAI7-028-C-20261007-6F2A81; publication TP2-96FAC49786245691AE19; original researcher EM-EMF6D046-5A2844. Historical Driver EM-DVR-DEBB5E, own SID MCP-9b4714dc46b948afa4875a86c89c713c and DA DA-2C461358FCCA215C8753. Other original contributions preserve their distinct authorship.

## Model and condition

Use r381's sharp-support hypotheses: G=Z/pZ, d>=2 exact uniform coordinate marginals, positive profile masses with denominator N coprime to p, S=m+p-1 distinct positive atoms, exactly p-1 degree-two connector profiles and all others of degree one. Connector profiles are pairwise nonequivalent under common translation. Each connector's same two atom translations occur across all coordinates. The r360 invariant identifies the same set E_s of q connector edges whose smaller residue-side cut has size s<p/2, in every coordinate.

Assume **qs=p-2**. By r381 the disjoint s-vertex pendant blocks leave a connected 2-vertex core C_i and one internal edge in each coordinate i.

**Stable-core condition.** The core edges carry the *same connector-profile label* y in all d coordinates. This follows, in particular, if the core edge in any coordinate has smaller cut size strictly greater than s: by r360 cut-size invariance, that same labeled edge cannot move inside an s-block or become an E_s edge. A sufficient combinatorial condition is that both core endpoints have at least one E_s pendant block attached in one coordinate. This condition matters for s>1: a core edge of small cut size may otherwise exchange label with an edge inside a pendant block.

Denote by g=t_y^(2)-t_y^(1) in G\{0} the nonzero difference between the two translation atoms of the bridge y. Its value is independent of coordinate. Put L=ord_G(g)>=2.

## Theorem: exact binary orbit count

For each selected connector x in E_s, r381's labeled cut-side invariant identifies the *same physical atom* on the larger side of the s-cut in all coordinates, and its coordinate-i residue a_i(x) lies in C_i. Choosing one fixed atom of the central connector y yields a vector b=(b_1,...,b_d) with

\[
C_i=\{b_i,b_i+g\},\qquad a(x)=b+g\epsilon(x),\qquad \epsilon(x)\in\{0,1\}^d.
\]

Two connector-profile shapes are common-translation equivalent if and only if their vectors are. The number of common-translation classes represented by the binary words in this fixed product of cores is exactly

\[
K_d(L)=\begin{cases}
2^{d-1},&L=2,\\
2^d-1,&L>2.
\end{cases}
\]

The constant-zero and constant-one binary words represent one class, namely the central bridge y. Because every selected x has a shape different from y and from the other selected connectors,

\[
\boxed{q\le K_d(L)-1 =
\begin{cases}
2^{d-1}-1,& L=2,\\
2^d-2,& L>2.
\end{cases}}
\]

Among selected connectors with the *same exact first-coordinate core attachment residue*, at most 2^(d-1)-1 can have distinct shapes. These bounds are necessary shape-capacity tests; the original integer cut masses, fixed input shapes, positivity and other tree constraints remain operative.

### Proof

The two atoms of y have the same fixed translation displacement g in every coordinate, so their endpoints are exactly C_i={b_i,b_i+g}. The cut-side invariant from r381 supplies for each selected x a *single* atom whose entire vector lies in the product of the C_i. Hence it has a binary code epsilon(x) as displayed. Its simultaneous-translation class equals the profile's original ordered shape class.

If L>2, a nonzero coordinatewise constant difference between binary words can only be +g (all bits change 0 to 1) or -g (all bits change 1 to 0). Therefore the only collision is the pair of constant words, and K_d=2^d-1. If L=2, +g=-g, and every binary word is equivalent precisely to its complement, giving K_d=2^(d-1). The constant-word class is already occupied by y. Remove it and apply shape injectivity to E_s to obtain the q bound. Fixing the first bit leaves 2^(d-1) codes and one excluded constant word in that half, establishing the local attachment bound. QED.

## Scope and applications

For p=29, d=5 and h=2, the integer equation qs=27 with s<29/2 permits (s,q)=(1,27),(3,9),(9,3). All nonzero g have order 29, yielding q<=30, and at most 15 same-residue attachments. This sharpens the structural capacity bookkeeping but does not reduce the established original OAI7 support interval 378 <= S_min <= 490.

For the ordinary double-star case s=1, q=p-2, the dimension condition d>=ceil(log2 p) is consistent with the independently established r368-r371 classification. Here the derivation also applies to s>1 for stable core-bridge labels. For bridge displacements of order 2 the improved bound q<=2^(d-1)-1 may be materially stronger than r381's q<=2^d.

## Exact finite quotient verification

This Python 3 standard-library code enumerates all 2^d tuples and partitions them by the exact translation-invariant offset vector; the universally quantified result is proved above, not inferred from the finite runs.

~~~python
from itertools import product

def binary_shape_classes(p, gap, d):
    assert p >= 3 and 0 < gap < p and d >= 2
    classes = {}
    for bits in product((0, 1), repeat=d):
        offset = tuple((gap*(bits[i]-bits[0])) % p for i in range(1,d))
        classes.setdefault(offset, []).append(bits)
    return len(classes), sorted(map(len, classes.values()), reverse=True)

for p,gap,d,expected in (
    (29,1,5,31), (9,3,4,15), (30,1,5,31),
    (30,15,5,16), (8,4,3,4), (8,2,3,7)
):
    n, sizes = binary_shape_classes(p,gap,d)
    assert n==expected and sum(sizes)==2**d
    print(p,gap,d,n)
~~~

Dependencies: [r360](https://github.com/awdawmip/enterprise-math/blob/0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a/research_notes/portable_direct/2026-11-19_oai7_driver_simultaneous_cut_signature_rigidity_r360.md), [r381](https://github.com/awdawmip/enterprise-math/blob/309b9d527567cf9bc81ed9fbd055e2573c33c0fb/research_notes/portable_direct/2026-11-19_oai7_driver_equal_cut_core_profile_capacity_r381.md), [r371](https://github.com/awdawmip/enterprise-math/blob/05b19e2ff943a13749cf6033437dfd000ba5e578/research_notes/portable_direct/2026-11-19_oai7_driver_arbitrary_gap_double_star_order_classification_r371.md).

Status: author-side proof and exact finite quotient checks. Native Result admission, independent review, Activity linkage and Task/mother-objective closure remain separate.
