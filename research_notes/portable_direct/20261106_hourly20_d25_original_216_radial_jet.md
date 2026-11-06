# D25 — exact radial-jet compression for the pinned original-216 source path

Date: 2026-11-06. Status: **AUTHOR-PROVED / SOURCE-PATH-RESTRICTED EXACT ALGEBRA / 207-PRIME FINITE-CHECKED / UNREVIEWED / NOT_ADMITTED**.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific input pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.

This result combines the newly established three-source coefficient Jacobian and exact original-216 mixed-jet transfer. It gives a **valid one-parameter compression for the particular original-216 p-adic source path and its leading carry-shell coefficients**. It does not identify arbitrary three-source perturbations, for which the preceding Jacobian theorem proves full rank three.

## Radial specialization theorem

For any prime `p=6m+1>=7`, put
`s=(2m,3m,4m)`, `alpha=(1/3,1/2,2/3)`, `v=-alpha`, and
`U_j(x)=(-1/2)^j prod_i binom(s_i+x_i,j)`, for `0<=j<p`.
Write `r_j=#{i:j>s_i}` and `R_j(t)=U_j(t s_1,t s_2,t s_3)`.

Let `h_j=2^(-j)(1/2)_j(1/3)_j(2/3)_j/(j!)^3`.

**Exact identity (rational):** `h_j=U_j(pv)`.

**Radial congruence (p-local):**
`h_j - R_j(p) is divisible by p^(r_j+1)`.

**Leading source-jet identity (in F_p):**
`boxed( h_j/p^r_j = [t^r_j]R_j(t) mod p )`, and this coefficient is nonzero.

In particular the *same single scalar t* recovers the leading signed coefficients in all four carry shells (r=0,1,2,3), with the source labels `s_i`, original rational shift vector and weighted index kept as metadata. This one-direction compression is only for this particular source specialization and the declared leading-order observer.

**Proof.** Since `s_i=(p-1)alpha_i`, the actual p-shift direction satisfies
`v_i=-alpha_i=s_i-p alpha_i`; hence
`p v_i=p s_i-p^2 alpha_i`.
The exact identity is the rising-factorial/generalized-binomial transformation from the preceding mixed-jet theorem.

At a fixed `j<p`, the factor `binom(s_i+x_i,j)` has a nonzero constant term when `j<=s_i`, or a simple zero with p-unit derivative when `j>s_i`. Thus `U_j` has exactly `r_j` independent vanishing source factors. Evaluating these at `p v_i` or `p s_i` changes the leading product only in order at least `p^(r_j+1)`: the factors differ by `p² alpha_i`, and `s_i` and `v_i` are congruent nonzero elements modulo p. All nonvanishing factors differ in order p². Consequently `h_j=U_j(pv)` and `R_j(p)=U_j(ps)` have the same nonzero normalized leading coefficient modulo p.

Finally the ordinary Taylor coefficient `[t^r_j]R_j(t)` is the product of the `r_j` simple-zero first derivatives (each multiplied by `s_i`) and all remaining constant factors. This equals the original mixed-jet leading coefficient because `s_i=v_i mod p`. QED.

## Source-scope and compression boundary

The general first-order map `x->(delta_1(x),delta_2(x),delta_3(x))` has rank three for p>=13 (proved in `20261106_hourly20_d25_three_source_jacobian_reconstruction.md`). There is no contradiction: that theorem allows arbitrary source perturbations; this theorem uses only the *fixed radial ray* equal to the original-216 shift modulo p. Valid projection depends on both the input manifold and the future observer. Other tangent directions and higher-order information are not declared equivalent.

## Executed exact verification

The adjacent independent certificate `d25_original_216_radial_jet_20261106.py` checks every j<p for all 207 primes p=1(mod6), 7<=p<=3000, using the original Pochhammer recurrence modulo p⁴ and the radial-jet leading derivative factors modulo p. **207/207 PASS**, all four shell leading coefficients nonzero. At p373 shell cardinalities are `(125,62,62,124)` and the separately weighted shell-leading sums modulo 373 are `(0,27,266,278)`.

## Next

Use the new exact radial source path to parameterize the *specific* compensated Theta regular/one-carry expression and search a finite WZ/telescope identity while retaining the mixed-derivative source tensor for possible higher operations. Resolve the pending original native continuation receipt and staging-transition issue before any new Source CLAIM/OPEN/checkpoint. The frozen second-digit mother objective and authentic p373 H0/B0/Frobenius/eta/kappa and independent review remain open.
