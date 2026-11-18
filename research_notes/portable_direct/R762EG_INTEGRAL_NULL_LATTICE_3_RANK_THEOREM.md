# R762EG — Exact 3-rank of the integral BRC null-lattice defect

Date: 2026-11-18, Asia/Shanghai. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; existing researcher EM-X6-3050F6. Author-side theorem and exact finite checks; independent review NOT_REVIEWED.

## Model and exact dependencies

P000 remains frozen at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, and the Task science is pinned to the taskbook at @e3f42efac29a2da2d95be391f3231a664e2fade0. This result concerns the positive six-named-branch terminal BRC observer, not native signed TRIADIC_CLOSURE_E updates.

For q=3^a, a>=1, let R=Z[(Z/qZ)^3], with generators X,Y,Z and P=1+X+Z+XY+YZ+XYZ. Put K=ker_Z(m_P) and I=K_A R+K_B R+K_C R+K_D R, with the four explicit integer annihilators of R762EF (https://github.com/awdawmip/enterprise-math/pull/2707):

K_A=T(Y)D(YZ^-1), K_B=T(X)D(XZ), K_C=T(X)D(XY^-1), K_D=T(XY)D(X^2YZ^-1).

Here D(U)=sum_{r=0}^{q-1} U^r and T(U)=sum_{r=0}^{q-1} a(r)U^r, with a(r)=2 if 3 divides r, otherwise -1. The R762ED eight-line zero-locus theorem implies rank_Z K=8q-12. R762EF proves I has full rank in K and q^4(K/I)=0. These are the precise dependencies for the all-q statement.

## Theorem

For C=K/I, a finite abelian 3-group,

$$
\boxed{\dim_{\mathbb F_3}(C/3C)=4q-8.}
$$

Thus the exact minimal number of generators of C is 4q-8 and its order is at least 3^(4q-8). At q=3 the complete finite classification is C isomorphic to (Z/3Z)^4, verified by exact integer Smith normal form.

## Proof

First reduce the four generators modulo 3. Since 2 equals -1 in F_3, T(U)=-D(U). The two arguments of each K_J generate a subgroup H_J of G=(Z/qZ)^3 of order q^2, so K_J mod 3 is the negative sum of the elements of H_J. Its translates span exactly the functions constant on H_J-cosets in the coefficient-vector space F_3^G.

The quotient maps of the four subgroups, expressed on a coefficient index (x,y,z), are

$$
\ell_A=x,\quad \ell_B=y,\quad \ell_C=z,\quad \ell_D=x-y+z\pmod q.
$$

For D, the two subgroup directions are (1,1,0) and (2,1,-1), each annihilated by x-y+z; they are independent over Z/qZ because their last and first coordinates determine the parameters. Consequently, the mod-3 image of I is the image of the linear map

$$
\Phi(f,g,h,k)(x,y,z)=f(x)+g(y)+h(z)+k(x-y+z),
$$

from four copies of F_3^{Z/qZ} to F_3^{G}.

We determine ker Phi exactly. If Phi(f,g,h,k)=0, replace x by x+b and subtract, obtaining

$$
f(x+b)-f(x)+k(t+b)-k(t)=0,\quad t=x-y+z.
$$

For fixed x,b, varying y makes t range over all residues. Every difference k(t+b)-k(t) is therefore independent of t. Thus k(t)=k(0)+L(t), with L an additive homomorphism from Z/qZ to F_3. Since q=3^a, L(t)=lambda (t mod 3) for a unique lambda in F_3. Substitution forces the other three functions to be affine with slopes -lambda,+lambda,-lambda respectively. The four constants satisfy one linear condition. Hence ker Phi has dimension 3+1=4, and

$$
\boxed{\operatorname{rank}_{\mathbb F_3}(I\bmod 3)=4q-4.}
$$

The kernel K of an integer linear map R->R is a primitive sublattice, because R/K is isomorphic to the image of m_P and is torsion-free. Therefore K/3K injects into R/3R. The image of I in K/3K has dimension exactly 4q-4. Its quotient C/3C consequently has dimension

$$
(8q-12)-(4q-4)=4q-8.
$$

The established q^4 annihilation implies C is a finite 3-group. The finite abelian group structure theorem identifies dim_F3(C/3C) with the number of its nontrivial cyclic 3-power factors, proving the minimal-generator and cardinality claims.

For q=3 an exact 27 x 108 integer matrix lists all group translates of K_A,...,K_D. Its Hermite image basis has 12 columns and Smith diagonal eight 1's followed by four 3's. Since K is the saturation of I, this directly proves C=(Z/3Z)^4. The q=3 Smith computation is a finite calculation and is not used in the symbolic all-q proof.

## Verification and open frontier

The companion pure-Python standard-library checker performs exhaustive sparse F_3 elimination on four coset families at q=3,9,27, finding image ranks 8,32,104 respectively; the corresponding quotient 3-ranks are 4,28,100. The optional SymPy HNF/SNF check produces the q=3 invariant factors and group order 81. All checks are exact integer/finite-field arithmetic; see R762EG_EVIDENCE.json. The all-q theorem is conditional on the earlier author-proved R762ED/R762EF zero-locus/nullspace results, which have not received independent mathematical review.

Next determine the multiplicities of cyclic factors 9,27,... for q>=9, sharpening the q^4 exponent bound; explore coefficientwise nondivisibility witnesses for the full three-coordinate all-horizon content(P^n). Native signed TRIADIC_CLOSURE_E Cell/Link/Port event licence and V17/V29/V39 transport remain a distinct task.
