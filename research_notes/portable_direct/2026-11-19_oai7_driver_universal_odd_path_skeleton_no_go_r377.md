# OAI7 r377 — Universal odd-modulus path-skeleton no-go for distinct common-translation profiles

Date: 2026-11-19. RESEARCH_DRIVER shared-context author-side proof, independent of any formal Native Result admission. Original OAI7 Researcher EM-EMF6D046-5A2844; original Task RS-OAI7-028-C-20261007-6F2A81; publication TP2-96FAC49786245691AE19. Driver historical identity EM-DVR-DEBB5E. This refines the exact cut-signature theorem r360, corrected path theorem r372, and r376's concrete prime-29 path-signature certificate.

## Universal odd-p theorem

Let p=2r+1>=3 be odd (not necessarily prime), G=Z/pZ, m>=p-1, and positive rational profile masses n_x/N with integer n_x>0, sum n_x=N and gcd(N,p)=1. Each profile x has a fixed ordered d-coordinate shape W_x in G^d; atoms (x,t) have positive masses, total n_x/N for x, and outputs w_(x,i)+t in coordinate i.

Suppose the support has the sharp size S=m+p-1, exactly p-1 profiles of degree two and all other profiles of degree one. Suppose its first-coordinate contracted degree-two connector tree is a path on all p residues, with ordered connector profiles x_1,...,x_(p-1). If EVERY coordinate marginal is exactly uniform, then

\[
\boxed{W_{x_r}\text{ and }W_{x_{r+1}}\text{ are equivalent under common translation in }G^d.}
\]

Therefore, if the m ordered shapes are pairwise inequivalent under common translation, **NO such sharp-support, degree-two path-skeleton sampler exists for ANY odd p, ANY first-coordinate path ordering, ANY number d of coordinates, or ANY allowed strictly positive masses.**

### Proof

Let v_0,...,v_(p-1) be the first-coordinate path residues. The original labeled atom x_r^+ of connector x_r and the original labeled atom x_(r+1)^- of connector x_(r+1) both sit at its central vertex v_r.

By coprimality gcd(N,p)=1, exact uniformity and S=m+p-1, r360 makes each coordinate's labeled profile/residue incidence graph a spanning tree and preserves the two profile-side residue cut counts of every atom. The corrected r372 path theorem then says that every other coordinate has a contracted path and, for the central mirror pair {r,r+1}, there are only two possibilities: retain both connector positions/orientations; or exchange those positions and reverse both labeled endpoint orientations.

In the keep case, x_r^+ remains at the central path vertex, and so does x_(r+1)^-. In the swap/reverse case, x_(r+1) moves to edge r, reversing its minus atom to the right (the central vertex), while x_r moves to edge r+1, reversing its plus atom to the left (the same central vertex). Hence in EVERY coordinate i, the two original atoms x_r^+ and x_(r+1)^- still share one residue z_i.

Because both originally occupied v_r in coordinate 1 and a profile applies the same common translation to its two atoms, their fixed shape offsets are
\[
 w_{x_r,i}-w_{x_r,1}=z_i-v_r
 =w_{x_{r+1},i}-w_{x_{r+1},1}\pmod p.
\]
This is true for every i, so W_(x_r) and W_(x_(r+1)) differ by the single common translation w_(x_r,1)-w_(x_(r+1),1), as claimed. Positivity and the other hypotheses are used only to invoke the exact simultaneous tree/cut theorem. QED.

### Equivalent elementary mask check

For the path-mirror notation of r372, let g_j=v_j-v_(j-1), y_0=0, y_j=sum_(s<=j) h_s mod p, and d_k(b) be the new connector atom shift. At the middle bit b_r:

* If b_r=0, the two middle connectors stay on edges r,r+1, and their atoms x_r^+, x_(r+1)^- meet at y_r.
* If b_r=1, they exchange edges and reverse, and these same two atoms again meet at y_r.

Thus d_r(b)=d_(r+1)(b) for **every** mirror mask b, even before testing that all y_j are distinct. This also follows by substituting h_(r+1)=-g_r when b_r=1.

This direct identity proves that the connector mask-signature map in r376 is **always noninjective at its central pair for every odd-modulus path**, not merely for r375's selected path. The explicit r376 table remains a valid, stronger 20-profile witness for that particular geometry.

## Consequence for the OAI7 exact support endpoint

The OAI7 five-coordinate fixed-profile finite law has p=29, m=350, N=13,297,022,452 with gcd(N,29)=1 and pairwise common-translation-inequivalent ordered shapes. A hypothetical S=350+29-1=378 atom sampler with exactly 28 degree-two connector profiles can therefore **never have a path as its first-coordinate contracted residue tree**.

Any remaining 378-support candidate must use at least one of the following structural possibilities:

1. At least one profile has degree >=3; or
2. All 28 extra degrees come from 28 degree-two profiles, but the contracted tree on the 29 residues has at least one vertex of degree >=3 (is a branching tree, not a path).

These are necessary alternatives. This result leaves the original global support interval 378 <= S_min <= 490 unchanged, and does not affect the separate geometric six-mask counterexample in r375.

## Small exact witness and computational cross-check

For p=5, the original path v=(4,1,3,2,0) and four connector profiles may have all four mirror masks geometrically admissible. The exact p=5, N=11 profile numerator vector (3,2,3,3) yields strictly positive first-coordinate connector atom numerators (Z^-_k,Z^+_k)=(11,4),(7,3),(8,7),(4,11) in units 1/(pN). Under mask b=2 all five destination columns also total 11/(pN)=1/5. But its two central profiles x_2 and x_3 have equal relative-coordinate offset. This illustrates the distinction: **exact uniformity and nontrivial masks can coexist when shape inequivalence is not imposed**.

The following standard-library Python 3 check covers every mask at p=5, p=13 and p=29 and confirms the central identity regardless of geometric admissibility:

```python
examples={
 5:(4,1,3,2,0),
 13:(0,5,2,9,1,3,8,11,4,6,10,7,12),
 29:(23,4,5,2,21,8,15,28,11,12,6,7,18,1,20,25,19,0,3,13,17,10,22,9,14,27,24,16,26),
}
for p,v in examples.items():
    r=(p-1)//2
    g=[(v[j]-v[j-1])%p for j in range(1,p)]
    for mask in range(1<<r):
        y=[0]
        for j in range(1,p):
            bit=(mask>>(min(j,p-j)-1))&1
            y.append((y[-1]+(g[j-1] if not bit else -g[p-j-1]))%p)
        def connector_shift(k):
            bit=(mask>>(min(k,p-k)-1))&1
            j=k if not bit else p-k
            minus=y[j-1] if not bit else y[j]
            return (minus-v[k-1])%p
        assert connector_shift(r)==connector_shift(r+1)
    print(p,1<<r,"middle-shift identities exact")
```

The proof is general; the checks validate the indexed formulas only.

## Research preservation and next route

Do not continue enumerating prime-29 degree-two *path* topologies in the hope that another residue ordering or additional mask classes restores pairwise translation-inequivalent fixed profiles. The distinct current scientific routes at the 378-support endpoint are **branching 29-residue connector trees** and **one or more degree-three-or-higher profiles**, checked using r360's exact cut-signature/positivity identities and the original 350 numerators.

r376 exact pinned Source: https://github.com/awdawmip/enterprise-math/blob/b522bd475c4c384e89481f83bcebf8a0ac5f2af8/research_notes/portable_direct/2026-11-19_oai7_driver_path_mask_signature_obstruction_r376.md
r372 corrected theorem: https://github.com/awdawmip/enterprise-math/blob/6ba73383f3e87b5f0e90aca1392044fa717ef362/research_notes/portable_direct/2026-11-19_oai7_driver_path_mirror_pair_reduction_r372.md
r360 cut rigidity: https://github.com/awdawmip/enterprise-math/blob/0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a/research_notes/portable_direct/2026-11-19_oai7_driver_simultaneous_cut_signature_rigidity_r360.md

This is an author-side mathematical no-go theorem for one specified topology family. It asserts no independent Native review, Source/Activity association, new CLAIM, Result acceptance, Task completion or parent-objective completion.
