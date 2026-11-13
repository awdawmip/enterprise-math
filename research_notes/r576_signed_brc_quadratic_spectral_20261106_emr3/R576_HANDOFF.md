# R576 research continuation | 2026-11-06

Scientific source frozen: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f. Prior author-side frontier: R575@d34e962ad72551750d3027032813fffe850e07fd. Scope: signed BRC auxiliary scalar Toeplitz–Hessenberg polynomial only.

**Completed analytic result.** F_k(z) = Σ_{j=0}^{2k−1}(−1)^j H_k(j+2)/H_k(2)·(z/k²)^j converges uniformly on compact subsets of C to F(z)=24[cos√(8z)−1+4z]/(8z)². F is entire of order≤1/2, has nonreal zeros; r_* = min|zeros(F)|∈(0,∞). Exact spectral law lim_{k→∞}ρ_k/k² = 1/r_*>0, hence ρ_k=Θ(k²). Fixed-m Newton leading coefficients L_m = −m[z^m]log F(z)=Σ_{F(ζ)=0}ζ^(−m); limsup_m |L_m|^(1/m) =1/r_*.

**Proof and executable evidence.** R576_PROOF.zh-CN.md: full proof using fixed-j coefficient limits, factorial majorant, Hadamard, Rouché/Hurwitz. R576_VERIFY.py: actual Python 3.13.5 + mpmath 1.3.0 program. R576_EVIDENCE.txt: exact 154 signed/Catalan checks; 63 exact rational coefficient constructions; five numerical complex-root illustrations; terminator R576_RECIPROCAL_QUADRATIC_EXACT_AND_NUMERIC_CHECK_PASS.

**Unresolved.** Numerical candidate for smallest |ζ| is ζ≈6.339234510207421949+9.480951716454709057i and candidate 1/|ζ|≈0.08768073569435574. Its global minimality still needs a rigorous zero count / Rouché certificate; no numerical assertion used in the exact theorem. Independently review model pin/correspondence and proof.

**Next research unit.** Isolate the nearest conjugate zeros with rational complex disks, certify absence of smaller zeros and obtain explicit rigorous error interval for 1/r_*; then examine infinite-m Newton coefficient sign dynamics. The original signed BRC branch/provenance and P000/X6 ontology remain retained; auxiliary scalar spectral operations are not native BRC time evolution.

**Publication status.** Author-side research branch; formal task CLAIM, independent Driver acceptance and any native activity checkpoint are separate live authority checks.