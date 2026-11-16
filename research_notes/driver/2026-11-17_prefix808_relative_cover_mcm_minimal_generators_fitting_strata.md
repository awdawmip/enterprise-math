# PREFIX-808 — Maximal Cohen–Macaulay canonical-cover module, exact generator numbers and Fitting support

Date: 2026-11-17. Status: **PROVED within the pinned Reeve semigroup model; Driver author-side extension, not independent Native Result review**.

## Provenance and precise maps

Original named TU/Reeve 0/1 source and observer model: **EM-DIRECT-4660FF**. The saturated semigroup, canonical-cover presentations, relative flatness/fiber computation and present deductions: **EM-DVR-DEBB5E**, in a shared context. Preserve all original Result, Task and review dispositions.

Input proof:
- [Relative flatness and joint-zero fibers](https://github.com/awdawmip/enterprise-math/blob/b6543b101537be8fbd068e2349d6c1d785d8c0d8/research_notes/driver/2026-11-16_r6_prefix808_canonical_cover_relative_flatness_joint_zero_fibers.md) (the corrected h=10 socle row).
- [Index-one canonical-cover pair presentation](https://github.com/awdawmip/enterprise-math/blob/43b9cb3ba76404104b384c1e46a3e6eb7e56e0fc/research_notes/driver/2026-11-16_r6_prefix808_even_index_one_cover_complete_intersection.md).

Let K be an arbitrary field, h>=2, g=gcd(h,2), r=h/g, R=K[U0,U1,U2,U3], A=U1 U2 and B=U0 U3. In the established integral semigroup domain
D_h=R[z0,z1]/(z0^h-B,z1^h-A)
with total-exponent diagonalizable grading, put
V_j=z0^j z1^(h-j), 1<=j<h,
R_h=D_h^(mu_h), and C_h^can=D_h^(mu_g).
Here R_h and C_h^can are finite over R and C_h^can is finite of generic rank r over R_h. The ring R_h is normal by the previously established saturated-semigroup description.

## Theorem (a global module characterization)

The finite R_h-module M=C_h^can satisfies:

1. M is **maximal Cohen–Macaulay** over R_h; in particular, it is torsion-free and reflexive over the normal domain R_h.
2. Its exact minimum number of global R_h-module generators is
   [
   mu_{R_h}(M)=L(h)=
   egin{cases}
   h(h+1)/2,& h mathrm{odd},\\
   h^2/4,& h mathrm{even}.
   end{cases}
   ]
   A concrete minimal generating set is
   [
   mathcal G_h={z_0^a z_1^b: a,bge0, a+b<h, gmid(a+b)}.
   ]
3. If s is any point of Spec(R_h), the exact local minimal generator number is
   [
   mu_s(M)=
   egin{cases}
   r,& A(s)
e0 	ext{or} B(s)
e0,\\
   L(h),& A(s)=B(s)=0.
   end{cases}
   ]
   Thus for h>=3, the excess at every joint-zero point is
   [
   L(h)-r=
   egin{cases}
   h(h-1)/2,&h mathrm{odd},\\
   h(h-2)/4,&h mathrm{even}.
   end{cases}
   ]
4. For h>=3 the first rank-sensitive Fitting ideal has the exact **set-theoretic** support
   [
   V(mathrm{Fitt}_{r}^{R_h}(M))=V(A,B),
   qquad
   sqrt{mathrm{Fitt}_{r}^{R_h}(M)}
      =sqrt{(A,B)R_h}.
   ]
   This is a radical equality, **not** an unsupported assertion that the Fitting ideal itself equals (A,B). For h=2, M=R_h and (mathrm{Fitt}_1(M)=R_h).

All statements hold over any characteristic, including characteristic dividing h or g.

## Proof

**Polynomial-base freeness.** The two monic Kummer equations give D_h the R-basis
({z_0^a z_1^b:0le a,b<h}), of size h². The degree modulo h invariant summand has R-basis
({1,V_1,ldots,V_{h-1}}) of size h, because within the bounded exponents the only total degrees divisible by h are 0 and h. Hence R_h is R-free of rank h. Likewise C_h^can is the degree-zero summand modulo g of the same R-basis, and is R-free of rank h²/g. These are genuine direct summands even when char(K)|h, since a diagonalizable-group invariant is the zero-graded summand.

**Cohen–Macaulay property.** Fix any prime q of R_h and m=q∩R. The extension R→R_h is finite free and integral, so ht(q)=ht(m) by incomparability and going-down for flat maps. R_m is regular local; choose a regular system of parameters of length ht(m). Since M is R-free, these parameters form an M_m-regular sequence. Localizing at q preserves regularity and puts all parameters inside qR_{h,q}. Consequently
(mathrm{depth}_{R_{h,q}}M_qgemathrm{ht}(m)=dim R_{h,q}).
The reverse inequality holds for any nonzero finite module, so M is maximal Cohen–Macaulay at every prime. The source semigroup domain makes it torsion-free. Over the normal R_h, torsion-free plus S2 (from the established maximal Cohen–Macaulay localizations) implies reflexivity.

**Explicit generators.** Consider any monomial (z_0^a z_1^b) in the bounded R-basis of C with g|(a+b). If a+b<h it is already in G_h. Otherwise 0<a<h and 0<b<h, and
[
z_0^a z_1^b = V_a,z_1^{a+b-h}.
]
The residual exponent is between 0 and h-2, and g|(a+b-h) because g|h. Thus the right factor belongs to G_h, proving that G_h generates M over R_h, without dividing by a source coordinate. Its cardinality is the displayed L(h): for odd h all degrees 0,...,h-1 occur with d+1 monomials; for even h=2k only degrees 0,2,...,2k-2 occur, giving (1+3+cdots+(2k-1)=k^2).

**Sharp lower bound and strata.** At any geometric joint-zero point of Spec R_h, every V_j has value zero, because V_j^h=B^j A^(h-j). The established fiber theorem identifies
(Motimes_{R_h}kappa(s)cong[kappa(s)[z_0,z_1]/(z_0,z_1)^h]^{mu_g}),
whose (kappa(s))-dimension equals L(h), with precisely the images of G_h as a basis. By the local Nakayama generator formula, M_q needs at least L(h) generators there. This matches the global generating set. On D(A)∪D(B), the established Kummer presentations make M locally free of rank r; hence the local generator number is exactly r. These two opens and the joint-zero closed set exhaust Spec R_h.

**Fitting support.** For any finite module, (mathrm{Fitt}_r(M)) is a unit at a point precisely when the localization can be generated by at most r elements. For h>=3, L(h)>r, so the preceding complete local-generator classification yields the stated equality of closed supports and therefore radicals. For h=2, the relative cover is an isomorphism.

## Exact finite crosscheck and research value

A separate integer-only enumeration for every 2<=h<=15 verified: (i) bounded R-basis ranks h, h²/g; (ii) G_h size L(h); (iii) every high-degree allowable monomial reduces by the explicit V_a rule to a member of G_h. For example h=3: rank r=3, min generators 6; h=6: r=3, min generators 9; h=10: r=5, min generators 25. The proof above is uniform, and finite enumeration is corroboration.

This extension quantifies the codimension-two failure of local freeness while establishing that the nonfree finite canonical-cover module is nevertheless maximal Cohen–Macaulay/reflexive. It supplies a direct route to local module/Fitting or resolution analysis without conflating the maps C_h^can→R_h and C_h^can→R. **No independent Native Result admission, formal Task completion, all-purpose X6 transfer or original-contributor reassignment is asserted.**
