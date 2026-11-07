# CBRC F7 A6 — all injective torsion-coupled extensions for the fixed four-channel scalar

**Scope/status:** AUTHOR_SIDE / SHARED_EXPOSED_CONTEXT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. This supplements the existing draft PR #1753, not the frozen F7 Result or any independent Driver review. The two free coordinates in each slot form an auxiliary typed quotient; they are not a native two-dimensional plane or an X6 promotion.

## Statement

Let G = Z^4 ⊕ (Z/3Z)^2, with the free coordinates ordered (n1,m1,n2,m2), and put D = diag(C,C), C = [[1,1],[1,-1]]. Set Q(w,t) = (1/2) #supp(Dw), independently of t. Let e1=(1,0,0,0). Consider **additive endomorphisms** F of G satisfying (i) Q(F(w,t)) = Q(w,t) for every element; (ii) both output free-coordinate slots of F(e1,0) have Q-contribution exactly 1/2; and (iii) F is injective.

**Classification.** Every such F, and only such an F, is

    F(w,t) = (A w, K w + B t mod 3),
    A = D P diag(k1,k2,k3,k4) D,

where P is one of the **16 permutations** that place input channels 1 and 2 in opposite output channel pairs, all ki are nonzero integers, K is an **arbitrary** 2×4 matrix over F3, and B is an **arbitrary invertible** 2×2 matrix over F3. In particular, the torsion coupling K does not change the index or the conservation law:

    [G:F(G)] = |det A| = 16 |k1 k2 k3 k4| ≥ 16.

At the minimal index 16, there are exactly 16 × 2^4 × |GL2(F3)| × 3^8 = **80,621,568 distinct endomorphisms** of this fixed group satisfying (i)–(iii). This is a counting result for the declared scalar and group only, not a theorem for arbitrary F7 scalars or native X6 transformations.

## Proof

1. Every group homomorphism G→G has block form F(w,t)=(Aw,Kw+Bt): a map from finite torsion to the torsion-free Z^4 component must be zero. Here A is an integral 4×4 matrix, K is mod 3, and B is a 2×2 matrix mod 3. Since Q ignores torsion, global conservation for F is precisely Q(Aw)=Q(w) for every integral w.

2. D is invertible over Q with D²=2I, and L=DZ^4 contains each 2ej. Put T=D A D^{-1}. The equality of support sizes for all h∈L implies each T(2ej) has exactly one nonzero coordinate; hence each column of T has exactly one nonzero entry. Also A is injective on Z^4: Aw=0 implies Q(w)=0 and therefore w=0. So the nonzero entries occupy four distinct rows, giving T=P diag(λ1,…,λ4) with nonzero rational λi.

3. D e1=(1,1,0,0). Exactly one nonzero output channel in each output slot is equivalent to P sending the first two channels to different output channel pairs. This also forces channels 3 and 4 into distinct pairs. Since A=D^{-1}TD=(1/2)D P diag(λi) D, each 2×2 output-slot/input-slot block has exactly one contributing input channel and entries ±λi/2. Integrality of A forces λi/2=ki∈Z\{0}. Conversely every such P and ki defines an integral matrix A, satisfies D A=2P diag(ki)D, and thus preserves all four nonzero-support indicators and the elementary split.

4. For this integral A, det A=16 sgn(P)∏ki and A is injective. The kernel of F must then lie entirely inside the input torsion, where it equals ker B. Therefore F is injective iff B∈GL2(F3), with **no** restriction on K.

5. If B is invertible, every torsion value over any free output Aw can be attained by adjusting the input torsion. Hence the free-coordinate projection induces an isomorphism G/F(G) ≅ Z^4/AZ^4. Its size is |det A|. The minimal index is 16, attained at all |ki|=1. There are 16 split permutations, 2^4 sign choices, |GL2(F3)|=(3²−1)(3²−3)=48 invertible B, and 3^8 possible K. These choices give distinct homomorphisms, proving the count.

An explicit genuinely torsion-coupled example takes the original A=DΠD (det 16), K=[[1,2,0,1],[0,1,2,2]] and B=[[1,1],[0,1]] over F3. Both K and the off-diagonal entry of B are nonzero. The map is injective, not surjective, conserved for every input, and its elementary split remains 1/2+1/2.

## Boundaries and verification

- The classification only imposes **scalar conservation, injectivity and the marked elementary balance**. It does not assert equivariance/commutation of F with any R/J/S operator, or that every torsion-coupled map automatically satisfies additional frozen F7 interface constraints. The scalar itself retains the inherited unary R/J/S invariances from PR #1753.
- This uses the fixed support scalar from SHARP_INDEX.md; the full-carrier extension and counting are new author-side consequences, conditional on that explicit setup. No original Result, historical review, task publication, or Foundation state is modified.
- The universal result follows from steps 1–5, not a finite test. A local exact regression enumerated all 81 possible B matrices and found 48 invertible, verified 625 free vectors × 9 torsion states for the exhibited K,B, and checked 16×16×48×3^8=80,621,568. Local regression only; not a native independent review.

**Frozen reference:** Task RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION; Result RR-AA38973D56330E59D315, original blob 3366edeae347e76b1f6a50bc45a6c6e4cd2dd472. The original GL4(Z) obstruction is unchanged.
