# Finite support does not repair a normal support obstruction

Author: EM-HODGE-7936BF. TASK_RESEARCH frozen author lemma, after own native open
h0p7936bf-open-20261015-01, ER-BF4F98F4E5E071C9DCF6.
This is an author-frozen mathematical lemma, not Source acceptance or independent review.

## Precise setting and conclusion

Let X be a smooth projective complex variety and i:Z -> X a smooth closed
subvariety with dim Z >= 3. Let D be any zero-dimensional closed subscheme of Z,
including the empty scheme. Put F_D = i_* I_{D/Z}. All deformations below are over
R=C[epsilon]/(epsilon^2). A deformation of a perfect complex means an object
E_R in Perf(X_R) with L i_0^* E_R isomorphic to F_D, not merely equality of
K-theory or Chern characters.

For an infinitesimal projective deformation X_R of X, denote its Kodaira-Spencer
class by kappa. Define
delta_Z(kappa) in H^1(Z,N_{Z/X})
by restricting kappa in H^1(X,T_X) to Z and projecting T_X|Z -> N_{Z/X}.

**Claim.** F_D admits such a perfect deformation on X_R if and only if
delta_Z(kappa)=0. Consequently the complete Atiyah--Kodaira--Spencer map
Omega_D(kappa)=(id_F_D tensor kappa) composed with At(F_D)
has exactly the same kernel as delta_Z. Finite nonreduced schemes D and
arbitrarily large finite length are included. No uniform bound on length is used.

## 1. The normal obstruction is the first-order embedded obstruction

Choose local trivializations of X_R on affine smooth charts of X. Their overlaps
differ to first order by derivations representing kappa. Locally Z is cut out by
a regular sequence; each chart admits the trivial local embedded deformation.
The difference of two local liftings on an overlap is a section of N_{Z/X}.
The resulting Cech 1-cocycle is exactly the image of kappa under restriction and
T_X|Z -> N. Changing the local lifting subtracts a Cech coboundary.
Thus local liftings glue if and only if delta_Z(kappa)=0. The same argument
applies on the nonproper open Z minus Supp(D). This is solely a first-order
statement; there are no higher-order liftings in its conclusion.

## 2. A derived lifting of this sheaf is a flat sheaf

Let M be an alleged perfect lifting of F_D. Since X_R is R-flat,
M tensor_R^L C is F_D concentrated in degree zero. Tensor the exact sequence
0 -> C --epsilon--> R -> C -> 0 of R-modules with M.
The resulting triangle has F_D at both ends, so its cohomology sequence says
M is concentrated in degree zero and gives 0 -> F_D -> M -> F_D -> 0.
Multiplication by epsilon on M is the composite of this quotient and inclusion.
Hence ker(epsilon)=im(epsilon), the flatness criterion over the dual numbers.
This argument does not assume that a derived lifting is already a sheaf.

On U=X minus Supp(D), the special fibre is i_* O_{Z minus Supp(D)}.
A local generator lifts, and Nakayama for the nilpotent ideal (epsilon) makes
O_{U_R} -> M|U_R surjective. Its kernel is Ann(M), independent of the
chosen generator. Thus these kernels define a global R-flat closed subscheme
of U_R deforming Z minus Supp(D). In particular delta_Z(kappa) restricts to
zero in H^1(Z minus Supp(D),N).

## 3. Finite punctures cannot erase this class

The smooth local rings of Z at the finitely many support points of D are regular
of dimension at least three. N is locally free there, so its depth is at least
three. Therefore the local cohomology sheaves with this finite support vanish in
degrees 0,1,2. The spectral sequence for cohomology with support gives
H^q_{Supp(D)}(Z,N)=0 for q=1,2.
The localization long exact sequence consequently gives an isomorphism
H^1(Z,N) -> H^1(Z minus Supp(D),N).
This proves the necessary implication in the Claim. The scheme structure and
length of D play no role in this injectivity.

## 4. A zero normal obstruction allows every finite D to lift

If delta_Z(kappa)=0, Section 1 supplies a flat embedded deformation Z_R in X_R.
It is smooth over R: locally a lift of the regular defining sequence has smooth
special fibre, and smoothness over an Artinian base follows from the smooth
Jacobian criterion. Choose an affine smooth open V of Z containing Supp(D).
Such a V exists because Z is projective and a sufficiently ample divisor can be
chosen disjoint from finitely many points. Its nilpotent thickening V_R in Z_R
is affine. Indeed, the nilpotent two-step filtration reduces higher cohomology
of quasi-coherent modules to that on affine V, so the affine criterion applies.
Write V=Spec(A), V_R=Spec(B). Smoothness of A over C lifts
the identity A -> B/(epsilon) to a C-algebra map A -> B. The resulting map
A tensor_C R -> B is an isomorphism: it is an isomorphism modulo epsilon and
both sides are R-flat; the kernel and cokernel are zero by the two-step
epsilon filtration. This is a noncanonical trivialization of V_R.

Inside this product, take the constant finite subscheme D_R=D x Spec(R).
It is a closed subscheme of Z_R: on V_R it is closed, and its finite
R-proper support is closed in the separated scheme Z_R.
Both O_{Z_R} and O_{D_R} are R-flat, hence so is I_{D_R/Z_R}.
The ideal is perfect on Z_R. Near D this follows by tensoring a finite
projective resolution over the regular C-algebra A with R; away from D it
is the structure sheaf. The immersion Z_R -> X_R is regular of the same
codimension, as can be checked by lifting the regular special-fibre equations
and using the R-flat quotient; its Koszul resolution is exact.
Therefore its pushforward of I_{D_R/Z_R} is a perfect complex on X_R,
R-flat with derived special fibre F_D. This proves sufficiency.

## 5. Connection to the complete object obstruction

The imported obstruction criterion is Huybrechts--Thomas, arXiv:0805.3527v2,
Corollary 3.4, with the square-zero-embedding hypotheses of the introduction.
For a perfect object on the special fibre it identifies existence of a perfect
lifting with vanishing of the Atiyah/Kodaira-Spencer product in Ext^2.
Here F_D is perfect because X is smooth. X_R is projective by hypothesis and
thus embeds in projective space over R; the latter embeds in a smooth
C-scheme P^m_C x A^1_C. Its square-zero ideal restricts to O_X.
Thus the precise input hypotheses, including the ambient smooth embedding,
hold. No Chern-character trace or semiregularity injectivity is substituted
for this complete object obstruction.

Combining the criterion with Sections 1--4 proves
ker Omega_D = ker delta_Z.
In particular, once a finite-dimensional subspace T of H^1(T_X) is fixed,
Omega_D|T factors uniquely as delta_Z|T followed by an injective linear map
from im(delta_Z|T) into Ext^2(F_D,F_D). This factorization is a complete
zero/nonzero obstruction classification on T. It does not assert a canonical
basis for the entire Ext^2 group, which can vary with D.

## Exact primary-source interfaces checked 2026-10-15

- Huybrechts--Thomas, Corollary 3.4 and main-theorem hypotheses:
  https://arxiv.org/pdf/0805.3527 , pp.2 and14.
  Used only for perfect-lift equivalence and Atiyah--KS identification.
- Stacks Project Lemma 47.11.1, tag 0AVZ:
  https://stacks.math.columbia.edu/tag/0AVZ .
  Depth at least three implies local-cohomology vanishing below three.
- Stacks Project Lemma 20.34.5, tag 0G71:
  https://stacks.math.columbia.edu/tag/0G71 .
  Localization triangle gives the cohomology restriction sequence.
- Stacks Project Lemma 51.2.1, tag 0A6T:
  https://stacks.math.columbia.edu/tag/0A6T .
  Identifies module local cohomology with sheaf cohomology with support.

These standard inputs do not decide any graph rank or exceptional seed. The same
non-split model, complete nine-direction map, and nonzero Pi_W[Z] are separate
mathematical inputs being checked in parallel. No algebraicity on a very-general
fibre, higher-order integrability, or unrestricted mixed-family no-go follows.
