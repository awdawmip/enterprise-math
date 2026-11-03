# PREFIX-455 — Exact quartic near-threshold X6–BRC rank and universal degree-d separation

**2026-11-03, author-side exact mathematical certificate; pending independent review.** Scientific pin: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Continues PREFIX-454 (\`6a21cce1c03d10a71cc562bec47757adb1a77a70\`). Applicable rule reads: Global Knowledge \`304466f6e86bb6d8c098d7c21f8b55f9cbf02aa6\`; Enterprise Math \`382dcea1fe369159a2d2161211c4a80494ea13d9\`. P000 native X6 is retained.

## Model

Fix integers q≥2 and d≥1. A path has N=q+d−2 signed primitive steps in six-dimensional native X6, and history residue r=(number of −e₁ steps) mod q. Its endpoint x∈Z⁶ is chart-relative. In each residue retain all degree≤d joint monomial observations of arbitrary nonnegative rational histogram masses on the reachable endpoints. Each full nominal sector has B_d=binom(d+6,6) coordinates. Rank and minimality below are over Q for **linear moment snapshot encoders**.

Let D={+e₁,±e₂,...,±e₆} and W_m(D) be its distinct m-step endpoint set. With k=r+ℓq negative e₁ steps, the exact support is

\`S_(q,d,r) = ⋃_{ℓ≥0:r+ℓq≤N} (−(r+ℓq)e₁ + W_(N−r−ℓq)(D)).\`  (1)

For every earlier r≤q−2, paths with r negative e₁ steps, q−r−2 positive e₁ steps and then d D steps have exactly the specified residue and duration. Within D choose v₀=−e₂ and the six alternatives +e₂,+e₁,+e₃,+e₄,+e₅,+e₆. Their differences from v₀ have determinant of absolute value 2, so the d-step terminal set contains an invertible affine image of the complete integer simplex {α∈N⁶:|α|≤d}. Multivariate falling-factorial interpolation is triangular on that simplex, with nonzero diagonal ∏ᵢαᵢ!. Therefore **each earlier sector has full B_d rank**, uniformly in q,d.

## Theorem A — All q≥2, degree 4, N=q+2

The exact total rank of the sector-separated quartic port is

\`R₄(q)=379 (q=2); 583 (q=3); 210q−48 (q≥4).\`

All earlier sectors have rank 210. The final residue has rank 169 for q=2, 163 for q=3 and 162 for q≥4.

Proof of the remaining fixed finite lemma: set z=x₁+q−1 and y=(x₂,...,x₆). In the terminal sector, equation (1) becomes

\`T_(q,4)= ⋃_{ℓq≤3} (W_(3−ℓq)(D) − ℓq e₁)\`

in coordinates (z,y). For q≥4, this is precisely W₃(D), with **242** points. For q=3, add only (−3,0,0,0,0,0), making **243** points. For q=2, add only (−1,0,0,0,0,0) and (−2,±eᵢ) for i=2,...,6, making **253** points. Evaluate the 210 monomials of degree≤4 on these finite integer point sets. The attached executed, standard-library-only exact integer rank certificate processes every row via fraction-free primitive integer Gaussian elimination, yielding ranks 162,163,169, respectively. Elimination replaces a row by b·row−a·pivot with b≠0 and divides by its nonzero integer gcd; it preserves rational row span exactly. The analytic reduction (1) and the exact finite rank certificates prove the all-q formula, rather than inferring it by finite sampling.

The script also transposes each evaluation matrix and selects independent **monomial column** observers. Since cubic moments are fully independent on these supports, the last-sector minimal bases contain all 84 degree≤3 moments plus 85 (q=2), 79 (q=3), or 78 (q≥4) selected degree-four monomials. Hence the minimal **added** quartic coordinates over the full 84q cubic snapshot are 211, 331 and 126q−48, respectively.

## Theorem B — All q≥5, degree 5, N=q+3

For q≥5, the final residue has no second winding count, because 2q−1>N. Its support is an affine translate of the same 743-point W₄(D) for every such q. The attached exact integer 743×462 evaluation-matrix elimination returns rank **398**; by the simplex proof, all q−1 earlier sectors have rank 462. Thus

\`R₅(q)=462q−64\`, for all integers q≥5.

The final-sector minimal basis consists of all 210 degree≤4 monomials and 188 additional independent quintic monomials. The fixed-support 64-coordinate defect is exact. Whether the observed defects 32,48,64 at degrees 3,4,5 generalize to 16(d−1) for every d≥3 with q≥d remains open.

## Theorem C — A universal positive-weight BRC information-loss witness

For any q≥2,d≥1, use q−2 initial +e₁ steps and then d steps ±e₂. The path with j positive e₂ steps ends at x(j)=(q−2,2j−d,0,0,0,0) and has residue 0. Source A assigns the nonnegative integer mass binom(d,j) if (−1)^(d−j)=+1; source B assigns it when (−1)^(d−j)=−1. Each source has total mass 2^(d−1). The d-th alternating finite-difference identity proves **all joint moments of total degree<d coincide**, while their degree-d x₂ moment differs by the exact positive integer

\`Σ_{j=0}^d (−1)^(d−j) binom(d,j)(2j−d)^d = 2^d d!.\`

For d=4, the masses [1,0,6,0,1] versus [0,4,0,4,0] at second coordinates [−4,−2,0,2,4] yield equal cubic ports but quartic moments 512 and 128, difference **384**. For d=5 the difference is **3840**. This is a native six-axis, positive-integer-weight history-preserving counterexample to replacing the higher-degree moment observer by the lower-degree port.

## Observer scope, evidence, and next step

The finite-rank terminal snapshot can be encoded by weighted sums of selected monomials. Each omitted degree-d moment is a rational linear combination of these retained moment evaluations on the **known support**. The coefficients follow from exact rational elimination on the same matrix. Reconstruct the standard full degree-d jet before passing it through finite positive-rational parallel/conditional rational-affine BRC updates; polynomial pullback then gives exact future degree-d readouts. A changed terminal support requires an appropriate decoder or full jet, not automatic reuse of the old reduced basis. This scope preserves the joint history and mixed-axis observations required by the P000/BRC residual contract.

\`prefix455_compact_integer_certificate.py\` is the **executed** Python-standard-library exact finite certificate, using only integer arithmetic; \`PREFIX455_COMPACT_LOG.txt\` records actual stdout. All four fixed-size matrices and the arbitrary-degree witness are checked without floating-point or modular approximations. Larger local evidence includes expanded proof, deterministic pivot lists, and an extended certificate. BRC reuse status: REUSE_APPLIED to existing frozen X6 signed-path and rational moment-port semantics.

Native research authority was not granted (\`research_authority_granted=false\`); bounded live owner query returned \`CONTROL_QUOTA\`, so active owner/Researcher-ID/CLAIM remain unconfirmed. GitHub publication is source evidence, not Result, independent Review, or theorem Admission. Next PREFIX-456: classify the higher-degree kernel on W_(d−1)(D), test/prove the proposed 16(d−1) pattern, and integrate a typed native quartic moment decoder with full bit-complexity, serialization, and streaming measurement.
