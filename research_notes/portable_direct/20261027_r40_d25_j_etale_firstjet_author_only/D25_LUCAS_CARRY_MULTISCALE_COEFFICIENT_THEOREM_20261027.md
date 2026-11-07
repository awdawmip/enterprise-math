# D25 — Lucas law and all-scale carry certificate for finite-Cauchy coefficients

2026-10-27. **AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE / REGISTER_PENDING**. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen mathematical source c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Same shared D25 author context, **not independent review**. No Source CLAIM/OPEN/checkpoint established.

## Statement — all primes p >= 5, all integers n >= 0

Let c_n = (3n)!(2n)!/[216^n (n!)^5] = binom(3n,n) binom(2n,n)^2 / 216^n, with 216 a p-unit. Write n = sum_i n_i p^i with 0 <= n_i < p. Then:

1. **Full base-p Lucas law:** c_n = product_i c_{n_i} modulo p. In particular c_n is a p-adic unit **if and only if** every digit n_i <= floor((p-1)/3). For any e >= 1, the number of nonzero residues among c_0,...,c_(p^e-1) is exactly ceil(p/3)^e. This counts Boolean support; it does not classify signed weights or residues modulo higher powers.
2. **Exact all-scale valuation:**
   
   v_p(c_n) = sum_(a>=1) [floor(3n/p^a)+floor(2n/p^a)-5 floor(n/p^a)]
            = [5 s_p(n)-s_p(3n)-s_p(2n)]/(p-1)
            = kappa_p(n,2n)+2 kappa_p(n,n),

   where kappa counts base-p carry events (with propagation). Equivalently the same valuation is the nonnegative suffix sum
   
   v_p(c_n)=sum_(a>=1) [floor(3(n mod p^a)/p^a)+floor(2(n mod p^a)/p^a)].
   
3. **Sharp limitation on D25 finite p^3 cutoff:** for all e>=1, c_(p^e) = c_1 = 1/18 modulo p, and v_p(c_(p^e))=0. By contrast v_p(c_k)=3 on ceil(2p/3)<=k<p. Thus the previously certified suppression of k>=ceil(2p/3) is valid inside k<p, **not globally across k>=p**. Also the mod-p Lucas equality must not be lifted to mod p^2: at p=5, c_5=12 (mod25), c_1=7 (mod25).

## Proof and reuse boundary

Use the exact integer-binomial factorization above. If every base-p digit is at most floor((p-1)/3), neither 2n nor 3n causes carries, so Lucas's theorem applied to both binomial factors and Fermat 216^(p^i)=216 (mod p) yield the product law, and every factor is nonzero.

If some digit >= ceil(p/2), addition n+n has a carry. By Kummer p divides binom(2n,n). Otherwise all digits are <p/2 (and doubling has no carries). A digit >=ceil(p/3) necessarily gives a carry in n+2n, so p divides binom(3n,n). Therefore in either case c_n=0 (mod p). The same digit makes the one-digit factor c_(n_i)=0 using the previously established v_p(c_k)=floor(3k/p)+floor(2k/p) for 0<=k<p. This proves the full Lucas congruence also in its vanishing case and the support-language count.

Legendre's factorial formula proves the first exact valuation expression and the digit-sum expression. Kummer applied separately to binom(3n,n) (n+2n) and binom(2n,n)^2 (twice n+n) gives the two labeled carry channels. For each p^a, writing n=q p^a+r makes floor(3n/p^a)+floor(2n/p^a)-5 floor(n/p^a)=floor(3r/p^a)+floor(2r/p^a) >=0. The digit word of p^e is 1 followed by e zeros and has no carries, so c_(p^e)=c_1 modulo p and its valuation is 0. The finite one-digit valuation cliff is already proved in the D25 finite Cauchy second-jet note (prior Git blob ecb8b8fe0584bf6a2a7af6d6bce5c73733ff1107). This completes the stated proof without re-proving prior Cauchy signed-tail results.

## Actual checks, applicability and safety

Companion standard-library program computes factorial-binomial residues directly, not via its Lucas prediction; independently compares all-digit product, Legendre and suffix valuations, digit sums and support, finite valuation cliff, and mod p^2 counterexamples. An actual author-side run passed 2225 (p,n) checks for p=5,7,11,13,19,31,37,43; all 0<=n<p^2 for first five p; at most 500 indices for other three. The independent author-check JSON is evidence, not an all-prime proof or native H0/B0 run.

Typed BRC carrier: full digit word, signed source-indexed coefficient, separate carry channels n+n and n+2n, integer valuation and mod-p readout. For any future signed Cauchy convolution, support-only projection loses mod p^2/p^3 unit data; retain provenance, residue and valuation before any deletion. Auxiliary n is an arithmetic index and is **not** a native Heartbeat X6 spatial cell or proof of native transfer.

**Unresolved:** build and prove a finite-state exact support selector {0<=n<N: v_p(c_n)<3} at N>p, preserving signed p^3 boundary and computational cost. Establishing original H0/B0/Frobenius and LIFT transfer, including real p=373 native evidence (Issue #1559), remains separate. The UR V2 original 94,687-byte 4-file bundle with SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 remains unverified; do not re-prove UR or assert a different bundle's provenance.

GitHub storage is **portable author material only**: no independent review, no Source-owned session/CLAIM/OPEN/checkpoint or mathematical admission. If actual Source continuation_seed is CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS, input_artifacts are current initial inputs and predecessor frontier_notes.completed_units=[]; never promote these staged author results into predecessor completed research.

Original complete local proof SHA256 f5cc220487f182473f1010f321df4fcef5e406032440203f85a6217d4d258ea5 (the present remote note is a concise publication version). Original local checker SHA256 2ad36473a269bec50ddd937c7158c17f23fa600fe1d06634790a8ddeee82cf69; original local author-check JSON SHA256 35bb98e6fe83a8c2d144a32790227cc37a57ec6684e92dff0094eff46b5af68c.
