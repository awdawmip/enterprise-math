# F7 A6: Smith invariants of all minimum-index fixed-scalar survivors

**Status:** AUTHOR_SIDE / SHARED_EXPOSED_CONTEXT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. This is a corollary of the frozen-input *auxiliary* A6 scalar model in SHARP_INDEX.md and TORSION_EXTENSION.md. It is not a Driver review, a new formal Result, or a change to the F7 reversible no-go.

## Theorem

Let C=[[1,1],[1,-1]], D=diag(C,C), and let P range over the 16 permutations sending input channels 1 and 2 to different output channel pairs. For signs epsilon_i in {+1,-1}, set A=D P diag(epsilon_i) D. These are the 256 distinct minimum-index free endomorphisms from the fixed four-channel support-conservation classification.

Every such A has Smith normal form diag(1,2,2,4). Consequently

    Z^4 / A Z^4  ≅  (Z/2Z)^2 ⊕ Z/4Z.

For every injective torsion-coupled extension

    F(w,t) = (A w, K w + B t mod 3)

on G=Z^4 ⊕ (Z/3Z)^2, where K is arbitrary over F_3 and B belongs to GL_2(F_3), the quotient G/F(G) is isomorphic to the same finite abelian group. In particular, all 80,621,568 minimum-index extensions already counted in TORSION_EXTENSION.md share a cokernel **isomorphism type**, not merely a cardinality 16.

## Universal proof

1. Each output-slot/input-slot 2x2 block of A receives exactly one signed channel contribution because P splits channels 1 and 2, and then 3 and 4, across the two output pairs. That block is an outer product of a column and a row of C, multiplied by a sign. Hence every entry of A is +1 or -1.
2. Since D^T D=2 I, and P and diag(epsilon_i) are orthogonal, A^T A=4 I. Thus det(A)=+16 or -16 and A^{-1}=A^T/4.
3. Let d_j denote the gcd of all j-by-j minors of A, with d_0=1. All entries are signs, so d_1=1. Every 2-by-2 minor is in {-2,0,2}, and some such minor is nonzero since A has rank four; therefore d_2=2.
4. The adjugate identity yields adj(A)=det(A) A^{-1}=+4 A^T or -4 A^T. Every 3-by-3 cofactor has absolute value 4; hence d_3=4. Finally d_4=16.
5. The invariant factors are d_j/d_{j-1}, giving (1,2,2,4). This is a proof for all 256 matrices, not an inference from enumeration.
6. Invertible B lets one attain every output torsion coordinate over any free output in A Z^4, by adjusting the input torsion t. Therefore the free projection induces G/F(G) ≅ Z^4/A Z^4, independently of K.

## Scope / evidence / follow-up

The support scalar Q(w,t)=#supp(Dw)/2 remains conserved and yet the image has an exponent-four cokernel. This distinguishes scalar conservation from surjectivity **only inside this fixed auxiliary group model**. It does not prove full F7 R/J/S-equivariance of F, an arbitrary-scalar statement, an Enterprise-native X6 transformation, three-dimensional-slice dynamics, or any physical conclusion.

The standard-library verifier SMITH_CHECK.py enumerates every 16 x 16 split-permutation/sign combination, checks A^T A=4 I, computes all determinantal divisors by exact integer minors and confirms 256 distinct matrices. SMITH_CHECK_RESULT.json records the finite execution. The universal claim rests on the six proof steps, not on a finite test.

Original F7 frozen Result RR-AA38973D56330E59D315, blob 3366edeae347e76b1f6a50bc45a6c6e4cd2dd472, and all historical authors/reviews remain unchanged. Next formal action requires a current authorized, contribution-independent Driver with the exact current Result and review set; this note is author-side material only.
