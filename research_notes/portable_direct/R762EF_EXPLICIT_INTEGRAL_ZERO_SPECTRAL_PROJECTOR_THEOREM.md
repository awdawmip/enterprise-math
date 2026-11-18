# R762EF — Explicit integral BRC null generators and minimal-denominator rational projector

Date: 2026-11-18, Asia/Shanghai. Research lineage: task RS-X6-TRIADIC-CLOSURE-DYNAMICS, historical researcher EM-X6-3050F6, existing Source session MCP-4b2d70a97f594366a7c94a0f8b45df38. Mathematical status: author-proved relative to the earlier R762ED zero-locus theorem, exact finite author checks PASS, independent review NOT_REVIEWED.

## Frozen science and mathematical scope

P000 is pinned to awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json; taskbook is pinned to awdawmip/enterprise-math@e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. This is a *terminal, positive six-named-branch BRC observer* theorem; no signed TRIADIC_CLOSURE_E Cell/Link/Port event licence or V17/V29/V39 transport is asserted. The full native X6, order, path provenance and residual information remain carried by the underlying model.

Let Q=3^a (a≥1), d=Q/3, and R=Z[(Z/Q)^3] with X^Q=Y^Q=Z^Q=1. The named six-branch terminal polynomial is

\[
P(X,Y,Z)=1+X+Z+XY+YZ+XYZ.
\]

Define a(r)=2 when r≡0 (mod 3) and a(r)=-1 otherwise. For U^Q=1 put

\[
T(U)=\sum_{r=0}^{Q-1}a(r)U^r,\qquad D(U)=\sum_{r=0}^{Q-1}U^r.
\]

## Theorem (all powers of 3)

Define the following four integer elements in R:

\[
K_A=T(Y)D(YZ^{-1}),\quad
K_B=T(X)D(XZ),\quad
K_C=T(X)D(XY^{-1}),\quad
K_D=T(XY)D(X^2YZ^{-1}).
\]

Then:

1. Each K_J is **integrally** annihilated by P, i.e. PK_J=0 in R. Each rational ideal K_J Q[(Z/Q)^3] has dimension 2Q.
2. These four rational ideals span the full kernel of multiplication by P, of dimension 8Q-12.
3. The rational group-ring element
\[
E=\frac{\sum_J K_J}{Q^2}-\frac{\sum_{J<K}K_JK_K}{Q^4}
\]
is an idempotent, annihilated by P, and acts as the identity on the entire rational kernel. Every coefficient of each K_J K_K is divisible by Q.
4. The *integer* group-ring element
\[
\boxed{N=(Q^3/3)E\in R,\quad PN=0,\quad N^2=(Q^3/3)N}
\]
exists for every a≥1. Moreover **L=Q^3/3=3^{3a-1} is the least positive integer with LE integral**.
5. For I=Σ_J K_J R, the full integral kernel is the Z-saturation of I, with
\[
Q^4\ker_R(m_P)\subseteq I\subseteq\ker_R(m_P).
\]
Thus the quotient lattice is finite of exponent dividing Q^4.

The minimal denominator refers to the exact rational idempotent projector, not to general individual null vectors.

## Proof

Let ζ be a primitive Q-th root of unity and ω=ζ^d be primitive cubic. Since a(r)=ω^r+ω^{-r}, geometric summation yields, for any character exponent h∈Z/Q,

\[
T(\zeta^h)=Q(\mathbf1_{h=d}+\mathbf1_{h=2d}),\qquad
D(\zeta^h)=Q\mathbf1_{h=0}.
\]

Consequently K_A evaluates to Q² precisely at characters (i,j,k)=(s,t,t); K_B at (t,s,-t); K_C at (t,t,s); K_D at (s,t-s,t+s), with s arbitrary and t∈{d,2d}; each is zero at all other characters. R762ED (GitHub PR #2705, immutable commit 2f4e9aefe8156c50e60a75be319f077a99cbc615) proved these eight lines form exactly the zero locus of P, with twelve pairwise double-overlap points and no triple intersections. Character diagonalization of the finite abelian group ring is faithful, so each PK_J=0 integrally, each ideal's dimension is 2Q, and the four ideals exhaust the rational kernel.

Write e_J=K_J/Q². It evaluates to an indicator on the corresponding pair of lines. Since no character belongs to three different pairs, their union indicator equals Σ e_J - Σ_{J<K}e_Je_K. Hence E is exactly the Fourier-space projection onto ker(m_P). Therefore E²=E, PE=0 and E is identity on this kernel, proving (1)-(3) apart from the divisibility claim.

For distinct J,K, the intersection of their character sets consists of two points {v,-v}; each component of v is divisible by d. By inverse character transform, for any coefficient index g=(x,y,z),

\[
[K_JK_K]_g=\frac{Q^4}{Q^3}(\zeta^{v\cdot g}+\zeta^{-v\cdot g})
=Q\,a((v\cdot g)/d).
\]

Here v/d is an integer residue triple and a is 3-periodic. Therefore K_JK_K/Q∈R, and every coefficient of that quotient is congruent to -1 modulo 3. There are exactly six pairs, so

\[
Q^3 E=Q\sum_JK_J-\sum_{J<K}K_JK_K/Q
\]
has all coefficients divisible by 3: Q is divisible by 3 and -6≡0 (mod 3). This establishes N∈R. Its annihilation and the equation N²=(Q³/3)N follow from E's identities.

The coefficient at the group identity of Q³E is the size of the zero-character set, 8Q-12, by Fourier inversion. For every Q=3^a (a≥1), v_3(8Q-12)=1: for Q=3 the integer is 12; for a≥2, it is 4(2Q-3) with valuation one. Thus E's identity coefficient has reduced denominator Q³/3. Combined with integrality of (Q³/3)E, this is the exact *least* positive denominator.

Finally the four K_J span the rational kernel, so the integral kernel is exactly the saturation of I. If v∈ker_R(m_P), then Ev=v, so the projector formula gives

\[
Q^4v=Q^2\sum_J K_Jv-\sum_{J<K}K_JK_Kv\in I.
\]

This proves the index bound and the theorem. QED.

## Reproducible verification and evidence

Companion files R762EF_VERIFY.py and R762EF_EVIDENCE.json compute exact integer group-ring coefficients, the four generators, all six pairwise products and their Q-divisibility formulas, integral annihilation PK_J=PN=0, projection denominator, and direct N²=LN at Q=3 and Q=9. The finite checks cover Q=3,9,27, respectively 27,729,19683 characters, or 162+4374+118098=122634 pair-product coefficient checks. All author-side assertions passed. No floating point/trigonometry is used; the all-Q theorem is proved symbolically from R762ED. External independent mathematical review remains NOT_REVIEWED.

## Unfinished research

Find the *exact* exponent/index and sparse generators for ker_R(m_P)/(Σ K_J R); the proved bound is Q⁴. Use this constructive nullspace to derive coefficientwise nondivisibility witnesses for the still-unresolved R762DN all-horizon content conjecture. Independently obtain the legal signed native TRIADIC_CLOSURE_E event predicate and V17/V29/V39 transport before asserting native future-safe compression.
