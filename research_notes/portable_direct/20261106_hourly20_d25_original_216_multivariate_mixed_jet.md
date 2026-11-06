# D25 — exact original-216 multivariate mixed-jet transport across four carry shells

Date: 2026-11-06. Status: **AUTHOR-PROVED / EXACT RATIONAL AND p-LOCAL ALGEBRA / 207-PRIME FINITE-CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT**.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.
Builds on the previously proved four-shell source valuation and first-order original-216 port. This unit supplies the previously missing explicit **multivariate mixed derivative and exact signed prefactor** for *every* shell, including double and triple carries. The original-class p373 H0/B0 is a separate native experiment.

## Exact specialization

Let `p=6m+1` be prime, `m>=1`; set `s=(a,b,c)=(2m,3m,4m)`, `v=(-1/3,-1/2,-2/3)`. For `0<=j<p` define

`U_j(x_1,x_2,x_3)=(-1/2)^j prod_{i=1}^3 binom(s_i+x_i,j)`

over p-local rationals, and
`h_j=2^(-j) (1/2)_j (1/3)_j (2/3)_j/(j!)^3`.

Then **exactly in rational arithmetic**, for every `0<=j<p`,

`h_j = U_j(p v_1,p v_2,p v_3)`.

Indeed, `-a+p/3=1/3`, `-b+p/2=1/2` and `-c+2p/3=2/3`; three rising factorials become three generalized binomials with the required sign.

## Theorem: graded source tensor / p-adic leading coefficient

Let `I_j={i in {1,2,3}:j>s_i}`, `r_j=|I_j|`. For every `j<p`,

`v_p(h_j)=r_j`

and, with `partial_{I_j}=prod_{i in I_j} partial_{x_i}` (the identity operator for `I_j=empty`),

`boxed( h_j / p^{r_j} = (prod_{i in I_j} v_i) (partial_{I_j} U_j)(0,0,0) mod p )`.

Both sides belong to the p-local rationals and the congruence is in `F_p`. The right side is a **nonzero** field element for every j. Thus the original p-adic leading coefficient is a signed labelled mixed derivative, not just a valuation count.

**Proof.** In `binom(s_i+x_i,j)=prod_{t=0}^{j-1}(s_i-t+x_i)/j!`, every denominator is a p-unit. If `j<=s_i`, the constant term is `binom(s_i,j)`, a p-unit. If `j>s_i`, exactly one factor (`t=s_i`) vanishes at zero, with first derivative
`s_i! (-1)^(j-s_i-1) (j-s_i-1)!/j!`, also a p-unit. Hence the complete product has a single first-order factor for each index in `I_j`, and no other p-factor for the specialization `x_i=pv_i`, since all `v_i` are p-units (`p>=7`). Its leading `p^{r_j}` term is precisely the product of those derivatives times the remaining constants. All higher terms are divisible by `p^{r_j+1}`. QED.

Therefore the four source intervals and exact prefactors are:

| indices | carry r | labelled leading coefficient `h_j/p^r mod p` |
|---|---:|---|
| `0<=j<=2m` | 0 | `U_j(0)` |
| `2m<j<=3m` | 1 | `(-1/3) partial_1 U_j(0)` |
| `3m<j<=4m` | 2 | `(+1/6) partial_1 partial_2 U_j(0)` |
| `4m<j<p` | 3 | `(-1/9) partial_1 partial_2 partial_3 U_j(0)` |

These are coefficient-level first-nonzero term identities. The weight `6j+1` of the W observer remains a separate labelled source; at the exceptional j=m it introduces an additional factor p. This does not erase the unweighted coefficient's nonzero leading term.

## Executed certificate

The adjacent file `d25_original_216_mixed_jet_20261106.py` runs two independent constructions: original Pochhammer recurrence modulo `p^4` and the factored mixed-derivative product modulo p. It checked **every j<p** for all 207 primes `p=1 (mod 6), 7<=p<=3000`: `207/207 PASS`, all observed leading coefficients nonzero. Shell counts: p13 `[5,2,2,4]`; p19 `[7,3,3,6]`; p373 `[125,62,62,124]`. For p373, signed weighted leading-shell sum residues are `[0,27,266,278]` in order r=0,1,2,3 (these residues belong to separate p-adic orders and are not directly summed as one unweighted scalar).

The algebra above proves the statement for every stated p and j; tests are regression certificates. The exact binomial shift is a source-transport identity within the p-local scalar model and is not presented as a native six-axis theorem.

## Next executable unit

Combine this exact source-labelled mixed-jet transfer with the earlier three-direction recoverability theorem `20261106_hourly20_d25_three_source_jacobian_reconstruction.md`. Compute the compensated scalar `Theta_p` as an explicitly declared projection of the full source tensor, identify its precise kernel and test p13/p19/p373. The second-digit four-channel observer recently developed independently must be reused by exact pin instead of recredited. Maintain frozen `Delta_p-R_p=0 mod p` for p13,19 mod24 and open native p373 H0/B0, Frobenius, eta/kappa, and independent-review obligations.
