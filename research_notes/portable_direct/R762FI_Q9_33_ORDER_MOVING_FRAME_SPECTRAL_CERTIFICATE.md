# R762FI — Exact 34-degree q9 moving-frame spectral law and 33-state-image recurrence

Date: 2026-11-19 (Asia/Shanghai).
Status: **AUTHOR_PROVED / EXACT_CYCLOTOMIC_ENUMERATION_AND_MATRIX_CHECK_PASSED / NOT_REVIEWED**.
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable frozen taskbook awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8. Continue R762FH moving-centered orbit compression; earlier R762EM/EO (127-degree full-coordinate spectral model), R762FE/FF (251 scalar criterion) and R762FG (factor-nine period-gap obstruction) retain original evidence/review status. Scientific domain: equal-positive six-named-branch BRC endpoint convolution within selected three-coordinate observation of full P000 X6; not primitive signed TRIADIC_CLOSURE_E.

## Mathematical setup

Let q=9, G=(Z/9Z)^3. Define P=1+X+Z+XY+YZ+XYZ. Inverse of 2 mod9 is c=5, and D=diag(1,-1,1). For F_n(g)=[g]P^n define h_n(y)=F_n(nc(1,1,1)+D y). As proved in R762FH, the h_n are invariant under H=S3 x {±I}, and each is specified by its 85 orbit values. Let C be the 85x85 **integer** update matrix on these orbit values, induced by the six centered signed-step vectors T=D(S-c1) and multiplicity-preserving convolution. Then h_(n+1)=C h_n.

Write ζ=ζ_9 and K=Q(ζ). The 85 H-orbits in the dual group G^* index a basis of H-invariant Fourier functions. For a character u=(u1,u2,u3), the eigenvalue is the exact cyclotomic integer
λ(u)=sum_{t in T} ζ^(u·t).
As T is H-invariant, this value depends only on the dual H-orbit.

## FI1 — 34 exact eigenvalues and minimal polynomial

An exhaustive, entirely integral enumeration of the **85 distinct dual H-orbits** gives exactly **34 distinct algebraic integers** λ(u). Zero is one of them and occurs with multiplicity **6** in the full 85-dimensional H-invariant Fourier space. The eigenvalue-collision histogram (number of dual orbits sharing one λ) is
{multiplicity 1: 5, multiplicity 2: 13, multiplicity 3: 12, multiplicity 4: 3, multiplicity 6: 1}.

The operator C is diagonalizable over C, because finite abelian-group convolution diagonalizes in the Fourier-character basis, and the H-invariant subspace is the direct sum of the corresponding dual-orbit sums. Therefore its **exact minimal monic polynomial over Q** is

μ_C(T)=T Q(T),   deg(μ_C)=34,   deg(Q)=33,

where Q(T)=product over the **33 distinct nonzero** λ(u) of (T-λ(u)) belongs to Z[T]. Exact coefficients below are in ascending-power order (T^0,...,T^33):

[-35126124336, -33404255496, 494463335220, 80927835480, -2424772369917, 893378361609, 5174614267803, -3602916482643, -5480907808095, 5538001341411, 2860442623503, -4523567996151, -418901654160, 2173478400108, -321833010726, -630844592526, 209061245835, 106100806905, -58427601858, -8032977846, 9305831529, -370276353, -873783045, 140091201, 44801505, -13153833, -800280, 600588, -29646, -12726, 1617, 63, -21, 1].

Exact cyclotomic multiplication and reduction in the six-term integral basis {1,ζ,...,ζ^5}, using ζ^6=-ζ^3-1, establishes that every non-leading coefficient of the product has zero components along ζ,...,ζ^5, i.e. the displayed Q has ordinary **integer** coefficients. All pairwise distinctness comparisons of the exact six-integer λ vectors are exhaustive. The proof of minimality is that all 34 eigenvalues actually occur in the Fourier-invariant subspace, and C is diagonalizable.

In particular, **Q(C) C=0** on the entire 85-dimensional orbit-count space, and for every fixed centered endpoint y, the scalar sequence h_n(y) obeys the same **33rd-order monic integer recurrence from n≥1**. The degree 33 is minimal on im(C), because all its 33 nonzero eigenvalues occur there.

## FI2 — strong 3-adic coefficient bounds

The same exact enumeration proves for every one of the 34 distinct eigenvalues λ:

λ^3 ∈ 3 Z[ζ_9].

Consequently v_3(λ)≥1/3 for every nonzero λ, using the 3-adic valuation extended to K and normalized by v_3(3)=1. Write

Q(T)=T^33 + a_1 T^32 + ... + a_33.

For each 1≤j≤33, as a_j is the jth elementary symmetric sum of the 33 nonzero algebraic-integer λ, each product term has valuation at least j/3. Since a_j∈Z, its valuation is integral, giving the **uniform exact divisibility certificate**

**3^ceil(j/3) divides a_j, for every j=1,...,33.**

All 33 integer coefficients have been tested against these precise bounds, and the full 85x85 integer-matrix identity **Q(C)C=0** was also checked using every basis unit vector; the latter is a separate exact finite verification of the symbolic proof.

## FI3 — 33x85 full-terminal periodicity sufficiency certificate

Let L>0 be divisible by **9**, so b=L/3 is integral and the centered chart aligns at n and n+L. For integer n define f(n)=max(0,floor(n/3)-2), and assume P^n/3^f(n) and P^(n+L)/3^f(n+L) are coefficientwise integral in the range being compared (as established for n≥9 in the prior q9 author-side R762ER work).

Define the *unnormalized centered difference*
δ_n(y)=h_(n+L)(y)-3^b h_n(y).

For n≥1 it obeys Q(C)δ_n=0, hence the 33-term monic recurrence of FI1. Its coefficients satisfy FI2. Take N≥9 and integer h≥1. If

**δ_n(y) ≡ 0 (mod 3^(f(n)+b+h))**

holds for each of the **33 consecutive times n=N,...,N+32** and each of the **85 orbit representatives**, then it holds at every later n≥N. Indeed, for j=1,...,33,

f(n+33)-f(n+33-j) ≤ ceil(j/3),

so the valuation of each recurrence term is at least the required exponent at time n+33; induction propagates the bound. Because q|L, the moving charts align, and the resulting statement is the complete 729-terminal normalized period relation

**3^-f(n+L) P^(n+L) ≡ 3^-f(n) P^n (mod 3^h), for all n≥N.**

This **2,805 (33x85) coefficient-congruence sufficient certificate** improves the *dimension of the full-vector recurrence window* over R762ES's earlier 127x729 checks, and avoids R762FE/FF's independently excessive 57-trit individual scalar surcharge. It is not itself an executed h7/h8 period certificate; its 2805 high-index congruences remain to be tested at the target period(s). The condition is on full orbit-vector differences and does not claim completeness for arbitrary unsigned/signed branch-decorated readouts.

## Exact reproducibility

R762FI_SPECTRAL_VERIFY.py implements:
1. all 85 dual H-orbits, with an exact canonical key;
2. each λ as six integer coefficients in Z[ζ_9];
3. full exact enumeration of eigenvalue collisions, zero eigenvalue and 33-dimensional nonzero distinct spectrum;
4. exact multiplication Q=product(T-λ), verifying every coefficient outside Z vanishes;
5. every λ^3 divisible by 3 in Z[ζ_9];
6. all 33 3-adic coefficient bounds;
7. separate full 85x85 integer identity Q(C)C=0 by evolving every unit orbit basis vector.

Local execution: **PASS**. R762FI_EVIDENCE.json preserves all coefficients, valuation bounds, zero multiplicity, collisions and check results. Arithmetic is unbounded Python integers; no floating point, heuristic eigensolver or approximation. Only q=9 is exhaustively proved by this enumeration; q=27 exploratory spectrum results are not required by FI1–FI3.

## Follow-up

Execute the 33x85 orbit-vector h7 and h8 high-index period certificates, comparing bit costs, wall time, modulus arithmetic and any native proof dependency. A separate task remains the *lower* period bound factor-nine gap R762FG: the shorter sufficient certificate alone does not establish minimality. Preserve P000 and the frozen signed Cell/Link/Port triadic-event target.

Review: NOT_REVIEWED. Existing Source claim, Result, Activity and global-journal states are independent of this scientific proof.