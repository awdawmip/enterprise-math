# OAI7 r373 — Exact orientation quotient for odd path mirror masks

Date: 2026-11-19. Driver-side author research, building on r360 and the corrected, fixed-shape-scoped r372. Original OAI7 Task \`RS-OAI7-028-C-20261007-6F2A81\`, publication \`TP2-96FAC49786245691AE19\`, original researcher \`EM-EMF6D046-5A2844\`. Shared-context mathematics, **not** an independent frozen-Result review.

## Theorem

Let \(p=2r+1\) be odd and \(v_0,\dots,v_{p-1}\) be any ordering of all residues in \(G=\mathbb Z/p\mathbb Z\). Write \(g_j=v_j-v_{j-1}\) for \(1\le j\le p-1\). For each bit mask \(b=(b_1,\dots,b_r)\), define oriented path steps as in r372:

\[
h_j^b=\begin{cases}
g_j,&b_{\min(j,p-j)}=0,\\
-g_{p-j},&b_{\min(j,p-j)}=1.
\end{cases}
\]

Put \(y_0^b=0\), \(y_j^b=\sum_{k=1}^j h_k^b\) mod \(p\). A mask is *geometrically admissible* when the \(p\) values \(y_j^b\) are all distinct. Let \(\bar b\) be its bitwise complement. Then:

1. **Path-reversal identity**, for every mask (whether admissible or not),
\[
\boxed{y_j^{\bar b}=y_{p-1-j}^b-y_{p-1}^b\pmod p.}
\]
Consequently \(b\) is geometrically admissible if and only if \(\bar b\) is.

2. **Identical labeled connector placement.** Under r372's mapping of the original edge labels and the two original endpoint atoms, the two masks induce exactly the same connector-atom destination residues **up to one common translation** by \(-y_{p-1}^b\). In particular, the connector-wise offsets recovered for \(\bar b\) equal those for \(b\) minus this same group element.

3. **Complete quotient.** Among admissible masks, the only two masks yielding a given *common-translation class of labeled connector placements* are \(b,\bar b\). Thus the exact number of geometrically distinct connector-offset templates, up to common translation, is \(|\mathcal A|/2\), where \(\mathcal A\) is the set of admissible masks. The trivial all-zero and all-one masks are a complement pair and are always admissible.

Therefore, for the OAI7 sharp-support **path topology** with \(p=29\), one needs at most
\[
\boxed{2^{13}=8{,}192}
\]
geometric template classes per additional coordinate, rather than the 16,384 oriented masks of r372. Each template still needs (i) compatibility with the **prescribed**, fixed OAI7 profile offsets using a common origin and (ii) the r360 exact positive integer cut signatures. This quotient is independent of the particular rational profile masses.

## Proof

From the definition, for all \(j\),
\[
h_j^{\bar b}=-h_{p-j}^b.
\]
Telescoping \(y_j^{\bar b}=\sum_{k=1}^j(-h_{p-k}^b)\) gives
\[
y_j^{\bar b}=-(y_{p-1}^b-y_{p-1-j}^b)
\]
and proves (1).

In the r372 path picture, the original connector \(x_k\) is placed on new edge \(k\) with its original endpoint orientation when \(b_{\min(k,p-k)}=0\); it is placed at edge \(p-k\) with both endpoint-atom labels reversed when the bit is 1. Reversing the entire new path swaps the edge index \(j\leftrightarrow p-j\) and reverses its orientation, precisely switching every mask bit. By (1), reversing also produces a single common translation of all the new residue labels. Hence **each labeled atom** (not only its unlabeled edge) moves by that same translation, proving (2).

If two admissible masks produced the same labeled connector placements up to translation, they would determine the same underlying connected path with all \(p-1\) connector labels. A finite path has exactly two orientations. In a fixed orientation the connector's index and endpoint order identify every bit uniquely, by r372. Reversing orientation uniquely complements every bit. This proves (3). The all-zero mask reproduces the original residue order translated to start at zero, and all-one reverses it, so both are admissible.

## Exact finite audit: 29-point path masks

An exact residue-only checker (no floating point) enumerated all \(2^{14}\) masks for each of 64 deterministic Fisher–Yates paths on \(\mathbb Z/29\mathbb Z\). A 32-bit LCG generates the reproducible shuffle state; this sample is not a completeness census of all \(29!\) paths. Every valid mask was paired with its bitwise complement. Observed valid oriented-mask counts across the 64 paths were:

| Valid masks | Number of paths |
|---:|---:|
| 2 | 42 |
| 4 | 15 |
| 8 | 5 |
| 16 | 2 |

Thus the sample produces respectively 1, 2, 4 and 8 distinct orientation-quotient templates. It demonstrates nontrivial mirror masks in the prime-29 geometry but does **not** establish any fixed-profile five-coordinate sampler or improve the global \(378\le S_{\min}\le490\) bound.

Standalone reproducible Python 3 checker:

~~~python
def seed_path(seed,p=29):
    a=list(range(p))
    x=seed
    for i in range(p-1,0,-1):
        x=(1664525*x+1013904223)&0xffffffff
        j=x%(i+1)
        a[i],a[j]=a[j],a[i]
    return a

def admissible_masks(p,v):
    r=(p-1)//2
    g=[(v[j]-v[j-1])%p for j in range(1,p)]
    valid=[]
    for mask in range(1<<r):
        y=[0]
        for j in range(1,p):
            bit=(mask>>(min(j,p-j)-1))&1
            h=g[j-1] if not bit else -g[p-j-1]
            y.append((y[-1]+h)%p)
        if len(set(y))==p:
            valid.append(mask)
            other=mask^((1<<r)-1)
            yy=[0]
            for j in range(1,p):
                bit=(other>>(min(j,p-j)-1))&1
                h=g[j-1] if not bit else -g[p-j-1]
                yy.append((yy[-1]+h)%p)
            assert tuple(yy)==tuple((y[p-1-j]-y[-1])%p for j in range(p))
    return valid

from collections import Counter
counts=Counter()
for seed in range(1,65):
    valid=admissible_masks(29,seed_path(seed))
    counts[len(valid)]+=1
    assert set(valid)==set((x^((1<<14)-1)) for x in valid)
assert counts=={2:42,4:15,8:5,16:2}
assert len(admissible_masks(29,list(range(29))))==2
print("r373 PASS: exact orientation quotient, 64 reproducible p29 path geometries")
~~~

## Current scope and research consequence

This is a strict search-state reduction: carry only one canonical representative \(b<\bar b\) per admissible complement pair. The only actual OAI7 candidate sampler would additionally satisfy prescribed representative shape offsets, all 350 pinned profile numerators, strictly positive weights, and all five exact marginal tests. The same non-path trees and degree-three-or-more profile families remain open.

Sources: [r360 cut-signature theorem](https://github.com/awdawmip/enterprise-math/blob/0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a/research_notes/portable_direct/2026-11-19_oai7_driver_simultaneous_cut_signature_rigidity_r360.md); [corrected r372 path theorem](https://github.com/awdawmip/enterprise-math/blob/6ba73383f3e87b5f0e90aca1392044fa717ef362/research_notes/portable_direct/2026-11-19_oai7_driver_path_mirror_pair_reduction_r372.md). Author-side exact theorem and finite audit only. No Source Activity admission, Native Result acceptance, task completion or mother-objective completion.
