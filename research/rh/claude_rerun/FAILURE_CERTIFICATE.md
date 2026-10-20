# FAILURE_CERTIFICATE

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`

## Certificate A — rumor-level Claude object

earliest_failed_node: `A_DET_BRIDGE`  
exact_statement: `det_ζ(L²_{Φ,K}^{reg}-(z²+1/4)) = C Ξ(z)` with exact divisor, multiplicity and completeness  
required_for: converting the Claude V6 self-adjoint operator program into RH  
attempted_proof: the locked source explicitly leaves this as OPEN; the square-difference bounded-coupling eigenvalue route is separately closed by counting mismatch  
failure_type: `SPECTRAL_BRIDGE_GAP`  
counterexample_or_missing_theorem: bounded/compact perturbation gives `N_H(Λ)~Λ^(1/4)` whereas squared zeta ordinates require `~sqrt(Λ) log Λ`; an alternative trace/determinant bridge would need a new theorem  
can_be_repaired: `UNKNOWN for a materially different operator/trace architecture; NO for exact eigenvalue bijection in the frozen bounded square-difference realization`  
repair_would_imply_RH_itself: `a genuine exact determinant/divisor bridge plus self-adjointness would contain essentially the missing Hilbert–Pólya content`  
downstream_nodes_invalidated: `full spectral identification; RH closure`  
surviving_results: `weighted symmetry; Hilbert–Schmidt threshold sigma>1/2; bounded-coupling counting obstruction; route-closure theorem`  

**Source-specific status:** `SOURCE_FOUND_NOT_FULL_RH_CLAIM`.

---

## Certificate B — strongest full RH claim with Claude assistance (Gershon v1)

earliest_failed_node: `Lemma 10 — Spectral-gap factorisation`  
exact_statement: for the entire generating function `g(z)=sum gamma_m z^m`, Hadamard factorisation yields `gamma_m = R1 rho1^m + R2 rho2^m + O(delta3^m rho1^m)` with fixed `rho1=1/|z1|>0`  
required_for: spectral-gap reduction; universal unitarity bound; Proposition 22; `D_r(n)>0` for all `r,n`; PF∞; Laguerre–Pólya; RH  
attempted_proof: source says this Taylor-coefficient expansion follows from Hadamard factorisation of `g`  
failure_type: `FALSE_LEMMA`  
counterexample_or_missing_theorem: Cauchy–Hadamard. Since `g` is entire, `limsup |gamma_m|^(1/m)=0`; the claimed nonzero leading exponential forces `limsup=rho1>0`. A simple polynomial Hadamard product also refutes the generic inference.  
can_be_repaired: `not by a local edit; the expansion belongs naturally to reciprocal/log-derivative coefficients, so the global spectral-gap argument must be rebuilt`  
repair_would_imply_RH_itself: `a valid replacement uniformly controlling all determinant levels and all relevant complex zeros would supply a substantial portion of the missing global RH-level bridge`  
downstream_nodes_invalidated: `Lemma 10-dependent Region C1; Proposition 22 as proved; claimed unconditional unitarity; Theorem 11 universal positivity; final PF∞/LP closure`  
surviving_results: `finite certifications remain finite evidence; TP2/log-concavity and other independent bounded lemmas are not refuted by this certificate`  

Earlier unclosed node: `Lemma 8` is already `UNPROVED_LEMMA`, but Lemma 10 is the earliest load-bearing node for which this rerun establishes an outright contradiction.

---

## Certificate C — Yamaguchi spectral determinant fallback

earliest_failed_node: `Hadamard Rigidity proof, real-zero factorization of xi(1/2+iz)`  
exact_statement: `xi(1/2+iz)=xi(0) product_k (1-z^2/gamma_k^2)` obtained by pairing all nontrivial zeros at `1/2 +/- i gamma_k`  
required_for: logarithmic-derivative equality; local-uniform determinant-ratio convergence; exact zero-set correspondence; RH  
attempted_proof: treats the completed zeta divisor as an already-real paired divisor  
failure_type: `CIRCULARITY`  
counterexample_or_missing_theorem: without RH, a zero `rho=beta+i gamma` maps to `z=gamma-i(beta-1/2)`, generally non-real. The asserted divisor parameterization is equivalent to the desired conclusion.  
can_be_repaired: `only by proving the exact divisor/determinant bridge without assuming real zeros`  
repair_would_imply_RH_itself: `YES, in substance`  
downstream_nodes_invalidated: `ratio convergence argument as stated; pointwise correspondence; final self-adjointness implication`  
surviving_results: `finite Hermitian matrix construction and numerical matches may remain evidence; they do not close RH`  

---

## Negative-control certificate

object: `CIPHER/RTSG functional bridge`  
expected_result: FAIL  
observed_result: FAIL  
reason: bridge equation collapses to a functional-equation tautology; public archive independently reaches the same diagnosis  
verifier_calibration: `PASS`
