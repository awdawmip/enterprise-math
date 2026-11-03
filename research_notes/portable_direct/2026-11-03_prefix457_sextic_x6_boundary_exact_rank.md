# PREFIX-457 — Exact sixth-degree X6/BRC boundary rank for every q ≥ 6

Date: 2026-11-03. Status: AUTHOR_EXACT_COMPUTER_ASSISTED_PROOF / UNREVIEWED. Continues PREFIX-456 (f58cedae3d5a4cbaaa487b98d36bebc794f17db8). Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.

## Model and theorem

Use P000 signed native X6 chart. Each path is an ordered sequence of N native signed unit-axis steps. Its historical sector is the number of −e₁ steps modulo q. Observe every six-axis joint endpoint monomial of total degree ≤6 against nonnegative rational path-source masses in each sector. There are B₆=binom(12,6)=924 standard moment coordinates per sector. The exact statement concerns rational-linear snapshot rank at the declared fixed path length and supports, retaining upstream ordered-path provenance.

**Theorem.** For every integer q≥6, at duration N=q+4, the exact rational rank of the complete sector-separated degree-≤6 observation is

    R₆(q) = 924q − 80.

Every residue r=0,...,q−2 has full rank 924; the last residue r=q−1 has exact rank 844 (defect 80). This is an infinite family in q, with one explicitly certified finite kernel lemma. The result extends the earlier degree-3/4/5 deficiencies 32/48/64 to degree 6, deficiency 80, while the unrestricted arbitrary-degree formula remains open.

## Proof 1: full ranks in the earlier residues

Let D={+e₁,±e₂,±e₃,±e₄,±e₅,±e₆}, containing 11 legal native steps. For a fixed residue r≤q−2, concatenate r steps −e₁, then q−r−2 steps +e₁, then six D-steps. The total length is q+4 and the negative first-axis count is r. Choose D-vectors v₀=−e₂ and v₁,...,v₆=(+e₂,+e₁,+e₃,+e₄,+e₅,+e₆). Their six differences vⱼ−v₀ have determinant of absolute value 2. Their sixfold sums contain an invertible affine image of the complete six-variable integer simplex of degree≤6. Multivariate falling-factorial interpolation on that simplex is nonsingular, so each early sector has rank 924.

## Proof 2: terminal residue and exact integer certificate

For r=q−1, the negative first-axis step count is r+ℓq. Because 2q−1>q+4 for every q≥6, only ℓ=0 occurs. Removing the q−1 negative steps leaves five D-steps. Hence, after translation of the first axis, the terminal support is W₅, the set of five-step D-endpoints. Its degree-≤6 polynomial evaluation rank is unchanged by translation.

Enumerating every five-step D-endpoint gives exactly 1925 different integer points in Z⁶. Evaluate all 924 standard monomials of degree≤6, producing A in Z^(1925×924). The attached executed Python/NumPy program constructs and verifies the following characteristic-zero proof certificate:

1. Exact modular Gaussian elimination at p=32003 and p=32009 gives rank 844 at both primes, with identical pivot columns. A nonzero modular minor proves rank_Q(A)≥844.
2. In each modulus construct the full 924×80 nullspace basis with the 80 free monomial coordinates forming the identity. Combine the two residues modulo 1,024,384,027 and perform bounded rational reconstruction via the integer Euclidean algorithm. Clear denominators at most 15. This produces 80 explicit integer coefficient columns K, each associated with its own nonzero free monomial and zero coefficients at the other free monomials. Hence these 80 columns are linearly independent over Q.
3. Multiply the full integer matrices A K and verify all 1925×80 entries equal exactly zero. K has 1020 nonzero integer coefficients in total, maximum absolute coefficient 345. Thus nullity_Q(A)≥80, giving rank_Q(A)≤924−80=844.

Combining the exact lower and upper bounds proves terminal rank 844 and the all-q theorem. All matrix products in the supplied implementation are safely within signed 64-bit integer limits for these exact inputs; rational reconstruction uses arbitrary-precision Python integers. The result is an exact author-side computer-assisted proof for one complete finite matrix, not a floating-point estimate.

## One transparent kernel polynomial

The certificate contains the explicit identity

    P(x)=x₃x₄x₅x₆(3x₁+3x₂²+x₃²+x₄²+x₅²+x₆²−7) = 0 for every x in W₅.

If the four-factor product is nonzero, at least four steps are committed to nonzero axes 3–6. The fifth step is then either +e₁, a step in ±e₂, or an additional step in one of axes 3–6. In each case the bracket is zero (or an axis cancels, making the product zero). The other 79 exact independent kernel relations are generated and exhaustively checked by the executable certificate.

## Typed BRC readout and exact decoding

At the known terminal support W₅, the 844 pivot monomials form a rational basis for all degree-≤6 polynomial readouts. The 80 reconstructed kernel columns solve each omitted free moment as a rational linear combination of pivot moments, because their free-coordinate submatrix is diagonal with positive integers. Retain all 924 coordinates in each earlier residue. Reconstruct the full 924q standard port before finite parallel addition, positive-rational history-conditioned branching or rational-affine polynomial pullbacks; this preserves all degree-≤6 observations within that declared future language. Recheck or change the decoder when support changes. The result does not erase ordered path provenance or supply physical-time/phase/Shor claims.

## Evidence, scope and continuation

- prefix457_sextic_exact_kernel_certificate.py: executed source; builds all W₅ points and 924 monomials, computes two modular nullspaces, performs CRT/rational reconstruction, checks 80 independent exact integer kernel vectors and the all-q rank formula.
- PREFIX457_EXACT_EXECUTION.log: captured execution output (PASS), including W₅=1925, rank_mod=844 at both primes, integer A*K=0, 80 independent relations, and coefficient bounds.
- Independent review, native Result/Admission, a conceptual arbitrary-degree proof, direct invocation of upstream BRC classes in this round, and d=7 rank are distinct further work. PREFIX-452 contains a previous pinned native BRC class integration check.

**Next PREFIX-458:** derive a general graded polynomial-ideal/interpolation argument for candidate deficiency 16(d−1); probe d=7 via explicit exact kernel construction. As an independent engineering route, implement and benchmark the 80-coordinate terminal sextic decoder in the native typed BRC interface, preserving source-support scope and rational coefficient lengths.

## Source and authority

Current applicable global canonical main was verified at c3ad67de41dbb3841d2d07c52c4a4ee0a2591e52 and Enterprise Math control main at f2f96e8338c0753d55c03f19d9166172fcc327c0 on 2026-11-03; scientific input remains frozen at f42f2906d77f24085c123f3ccfe9667d41caa96d. Actual GitHub account: awdawmip (repository push/admin). Native Site gateway reports research_authority_granted=false; bounded task owner lookup returned CONTROL_QUOTA. This is an author-side GitHub scientific publication, not a formal native CLAIM, Result, Review or admission.
