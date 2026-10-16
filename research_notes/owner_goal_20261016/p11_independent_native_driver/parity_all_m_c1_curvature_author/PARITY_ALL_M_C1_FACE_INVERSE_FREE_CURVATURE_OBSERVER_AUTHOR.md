# The next Parity face: an explicit finite curvature observer

AUTHOR PAPER CANDIDATE, EM-DVR-BFF6DC. NONBLIND, derived interface, UNREVIEWED. This is a paper-only continuation of the actual all-m tangent-face question, not an execution of its published Task, not a new Task, not a positive trace certificate, and not a restart of the permanently stopped m7 r∈[7,8] certificate branch. No scientific program, expansion, sample or solver was used.

The completed result below is an explicit inverse-free finite formula for the next coefficient of a precisely normalized numerator. Its coefficientwise sign remains OPEN. Ordinary matrix differentiation, polynomial interpolation and the already established codimension-one residue-dual carrier are reused; no generic method novelty is claimed.

## 1. Fixed input and the exact coefficient being studied

Fix m≥2 and n=m−1. Retain the original actual synchronization
r0=mS, L=ma, r=r0+L, with S≥0,a>0.
For the second gap c put N=L+mc. The nodes are
X_i=r0+(i+1)/m, 0≤i≤n.
Let w_i=(−1)^i binom(n,i), and set
η_i(r)=n!/product_(k=0)^n(r+(i+1)/m+k),
d_i(r)=w_i η_i(r)/m, D(r)=diag(d_i(r)).

Write φ_j(x)=(x)_j/j!, j≥0, and use the original normalized secant frame
G_L[i,j]=[φ_j(X_i+L)−φ_j(X_i)]/L, 1≤j≤n.
It extends polynomially to L=0, but the physical first gap remains positive. Its columns span E=ker w^T, and its Gram matrix
H(L)=G_L^T D(r0+L) G_L
is the original normalized quotient form up to the fixed congruence already used in the source trace. Thus the exact defect is
T(c)=tr(H(L+mc)^−1 H(L))−n.

The source proves that E is nondegenerate for this alternating metric and that
S_r=sum_i w_i/η_i(r)
=(−1)^n [mr+(m²+1)/2]/m^(m−1)≠0.
It also proves the endpoint determinant, the all-m positive tangent face and the inverse-free three-index expression for the whole trace. Those are inputs, not discoveries here.

Put W=m², x=mr=W(S+a), β=(W+1)/2,
G_W(x)=product_(k=1)^W(x+k).
To avoid any ambiguity about optional polynomial cancellations, fix the COMMON denominator
D_c=(x+Wc+β)G_W(x)
and define the source-normalized numerator
P(c)=D_c T(c)/c.
This is a specified normalization, not an assertion that it is primitive or fully reduced for every m. The coefficient studied here is P1=[c]P(c).

The existing three-index source formula implies D_c T(c) is polynomial over Q in(S,a,c): reciprocal later-endpoint Beta factors are polynomials, the only scalar inverse is S_(r+mc), and multiplying by G_W(x) clears every first-endpoint Beta denominator in the contiguous block. Normalized mixed minors are polynomials because all divided differences are polynomial. At c=0 the numerator vanishes identically, so division by c is polynomial divisibility. Consequently P and P1 are genuine rational-coefficient polynomials, although the compact formula below displays rational factors that cancel.

For m=6, the source's printed denominator is2D_c. Hence its primitive P_6 differs from this P only by the explicitly printed positive rational content. No universal reduced-content statement is assumed from that example. A negative coefficient of this normalization would not refute the trace inequality.

## 2. A finite differentiation matrix on the labeled nodes

Let J be the matrix which differentiates the unique polynomial of degree≤n interpolating a vector at the nodes X_i. Explicitly,
J_ij=w_j/[w_i(X_i−X_j)] for i≠j,
J_ii=sum_(k≠i)1/(X_i−X_k).
These are rational numbers depending only on the equally spaced differences, not on r0. They are the derivatives of the ordinary Lagrange basis polynomials at the nodes.

Evaluation identifies R^m with polynomials of degree≤n. Therefore J^m=0. Its image lies in E, the values of polynomials of degree<n; in particular w^T J=0 and J^n annihilates E. These statements include m=2, where E consists of constants.

Define FINITE matrix polynomials
F_L(J)=sum_(k=0)^n L^k J^k/(k+1)!,
F_L(J)^−1=sum_(h=0)^n [I−F_L(J)]^h,
Γ_L=(∂_L F_L(J)) F_L(J)^−1.
The inverse identity follows because F_L−I is a polynomial in J with zero constant term and hence its(n+1)st power is zero. There is no matrix solver, unknown inverse or division by L in this definition.

Every term of Γ_L contains a positive power of J. It lowers polynomial degree, has image in E, and is nilpotent. Its restriction to E and the square of that restriction have trace zero. This is an algebraic degree filtration statement, not an eigenvalue-positivity assumption.

The original derivative-average formula for the secant is
G_L[i,j]=integral_0^1 φ_j'(X_i+tL)dt.
Because φ_j' is polynomial of degree at most n−1, ordinary finite Taylor expansion gives
G_L=F_L(J)Y, Y[i,j]=φ_j'(X_i).
Consequently
∂_L G_L=Γ_L G_L.                                      (1)
This is the actual internal frame velocity for the source's normalized secant family. It is retained rather than discarded merely because det of its basis change is1.

## 3. The existing rank-one projection eliminates the Gram inverse

All derivatives in this section hold r0 fixed, so dr/dL=1. Define
z=D(r)^−1 w, s=w^T z=mS_r,
Π=I−z w^T/s,
Λ=diag(λ_i), λ_i=−sum_(k=0)^n1/(r+(i+1)/m+k).
Here z_i=m/η_i(r) and s is the nonzero linear scalar above. Λ=D^−1 D'. Thus every entry is explicit in the old Beta factors.

Π is the D-orthogonal projection onto E along span(z):
Π²=Π, Πz=0, w^TΠ=0, DΠ=Π^T D.
The old codimension-one restriction is nondegenerate precisely because s≠0. Its inverse-free ambient expression is this rank-one projector. If
K=H^−1 H', B=H^−1 G_L^T D,
then B G_L=I and G_L B=Π.
These equalities are used only in the proof; K and the Gram inverse do not occur in the constructed answer.

For an ambient matrix C use its D-adjoint C*=D^−1 C^T D. Define
Ω=Π(Γ_L+Γ_L*+Λ)Π.                                   (2)
It is an explicit m by m rational matrix built from finite polynomial sums, diagonal reciprocals and the SINGLE known scalar s. It contains no inverse of H, no determinant, no mixed minor and no unknown interpolation data.

Differentiating H and using(1) gives
H'=G_L^T(Γ_L^T D+DΓ_L+D')G_L.
Hence
G_L K B
=Π D^−1(Γ_L^T D+DΓ_L+D')Π
=Ω.
The decomposition R^m=E⊕span(z) identifies Ω with K on E and with zero on the complementary line. Thus for every integer j≥1,
tr(Ω^j)=tr(K^j).                                     (3)
In particular tr Ω² is the required inverse-free curvature statistic.

The alternating metric is retained. The notation Ω² does not imply tr Ω²≥0: an operator self-adjoint for an indefinite form has no such general positivity guarantee. No forbidden positive-real-spectrum shortcut is being used.

As a consistency check, Γ_L lowers polynomial degree on E, so its trace on E is zero; the D-adjoint has the same trace. Therefore
tr Ω=tr(ΠΛΠ)=tr Λ−(w^TΛz)/s.
This equals the already known first logarithmic determinant derivative. It is not a new tangent-face theorem.

## 4. Exact next-face formula

Let
ell(x)=sum_(k=1)^W1/(x+k)−1/(x+β),
h2(x)=sum_(k=1)^W1/(x+k)^2−1/(x+β)^2.
These are known contiguous-block rational functions; h2 is not assigned a sign.

Set ℒ(L)=log|det H(L)|. The old endpoint determinant formula gives
ℒ'(L)=−m ell(x),
ℒ''(L)=m² h2(x).                                     (4)
The absolute value causes no difficulty: the real Gram form is nondegenerate with fixed inertia throughout the stated domain.

For H_c=H(L+mc), ordinary inverse differentiation at c=0 gives
T'(0)=−m tr K,
T''(0)=m²[tr(K²)−ℒ''(L)].                            (5)
For clarity, the second identity follows from
T''(0)=m²[2tr(K²)−tr(H^−1H'')]
and
ℒ''=tr(H^−1H'')−tr(K²).
It does not replace tr(K²) by(tr K)².

Since D_c'=W G_W(x) and D_0=(x+β)G_W(x), coefficient comparison in P=D_c T/c gives
P0=D_0 T'(0)=W[(x+β)G_W'(x)−G_W(x)],
recovering the old positive face with its exact positive factor.

The completed new interface is
P1
= W² G_W(x) ell(x)
  + (W/2)(x+β)G_W(x)[tr(Ω²)−W h2(x)].                (6)

Equivalently,
P1=(W/2)(x+β)G_W(x)
   [tr(Ω²)+W(2ell(x)/(x+β)−h2(x))].

Every object on the right is specified by the original labels(m,S,a) through finite sums and products in(1)–(4). No scientific execution or expansion is needed to define it. Equation(6), together with the polynomiality argument in§1, is an all-m explicit formula for the next source-normalized face, retaining the actual secant-frame motion.

The formula is not just the generic matrix identity(5) with an unnamed inverse or derivative: Γ_L is a finite polynomial in the fixed interpolation differentiator, Π is the existing explicit rank-one projector and Λ consists of labeled Beta logarithmic derivatives. Thus the only remaining sign comparison concerns an explicit finite quadratic observer, rather than an unspecified derivative of an inverse Gram matrix.

## 5. Exact scope and the remaining sign problem

This paper proves(1)–(6) for every m≥2, S≥0,a>0. The finite construction also has a regular algebraic L=0 interpretation, but no physical zero-gap assertion is required. For m=2, J annihilates E, so the Γ terms disappear on E; the formula reduces to the scalar endpoint calculation without an empty-matrix exception.

It does NOT prove coefficientwise positivity of P1, let alone that of every higher face. It does NOT assert that determinant data alone determine the curvature statistic. It retains the extra term explicitly and makes no unproved minimality claim for it. Whether(6) admits a sign-resolved labeled complement-factor or positive-basis expression is the remaining precise question.

The fixed denominator matters. This formula is not automatically a formula for a numerator after every possible nonconstant gcd cancellation, and coefficientwise positivity cannot be transferred through arbitrary positive-factor division without proof. Any later comparison with a primitive numerator must retain that distinction. On the actual positive domain, D_c>0, so a proved positive expression for this P would still imply the original trace inequality.

The old small-c strip already proves positivity near c=0 for each fixed m and bounded a by using the positive tangent and an absolute coefficient bound. It does not prove the sign of this next coefficient. The old signed-moment paper fixes a=c=1 and provides a comparison/certificate interface, not an all-m c-face formula. No claim of new coverage of either old theorem is made. Large-r Horner/trace work at fixed m and the stopped m7 compact attempt are separate and are neither rerun nor repaired here.

This is a partial all-m structural formula on an existing mother route, not closure of the formal TANGENT_FACE_INDUCTION Task. Its current Native ownership was not queried and no execution authority is asserted from its READY book. HCM0, other mixed coefficients, the actual AP all-m determinant and the parent Goal remain OPEN.

## 6. Source reuse and contribution record

Actual source anchor: c71860de7f02168af423a53878e32c4b5259c232, Goal OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M / OG-9CD71978EC19A9D5B7FA, and the current all-m, extreme-parity and tangent-face books.

Mathematical inputs: Source623a4ee81911cc79d07ed5db1887a06ebe91ffd5, prefix research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/, with the handoff, extreme signed-branch reduction, tangent-face theorem, codimension-one Krein normal, dual-hyperplane inverse and actual-block semigroup papers. The original M6 certificate fixes its printed denominator/content comparison only; it is not an all-m sign proof.

All these texts were personally fetched through the managed GitHub connector and read before this author paper. Own exact byte/hash/blob gates accompany the eventual handoff. Existing FB0860 and other authors keep all original identities and finite results. Classical interpolation, finite Taylor averaging, nilpotent inversion and matrix derivative identities are reused without novelty claims. Bounded dedup is limited to these actual bodies and my previously reviewed weighted/small-c papers; no whole-repository absence claim is made.

I, EM-DVR-BFF6DC, am the author of the new explicit curvature observer and its exact next-face application and cannot independently approve this paper. My prior Driver/CM24/P11/LC/CONTROL history remains disclosed. Root selected a return to an underserved Parity mother line and supplied no formula or repair. The direction freeze followed preliminary reasoning and is not represented as blind preregistration.

No new Researcher identity, borrowed SID/DA, formal Task, claim/run, Native scientific ticket, shared Tool or Source mutation was created for this paper. No scientific program/import/AST/compilation/test/numeric calculation/parameter scan occurred. Only paper reasoning and CONTROL text/custody utilities were used. A genuinely different nonauthor must now assess correctness, scope and whether this interface adds useful information beyond the cited whole-trace carrier. The original m7 fixed-certificate STOP and every old budget remain unchanged.

