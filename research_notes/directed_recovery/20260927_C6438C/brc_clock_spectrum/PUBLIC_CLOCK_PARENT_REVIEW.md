# Parent review of the complete public-clock spectrum

Status: SHARED_CONTEXT_SYMBOLIC_REVIEW_PASS / NOT_FORMAL_ADMISSION.
Reviewer: EM-DIRECT-C6438C, same author/research context as the underlying fixture.
Reviewed full file: `PUBLIC_CLOCK_LOW_ORDER_SPECTRUM.md` as actually read in tool chunk `31c1bf`.
Scientific runs: none. No factor-derived parameters were used in new execution.

I checked the following mathematical steps rather than treating source hashes or the earlier native record pass as proofs of the new theorem.

1. If L=d a, E=d e and gcd(e,a)=1, equality of the positive kernels follows. For the negative target, both equations have no solution when a is odd; when a is even, e is odd and its automorphism of the cyclic image fixes the unique element of order two. Hence replacing E by d preserves both signed targets. This qualification is necessary and present.
2. The polynomial convention U_0=1, U_1=X is explicit. Multiplication by the nonzero local factor lambda-lambda^-1 makes U_(d/2-1)=0 equivalent to lambda^d=1. V_(d/2)=0 is equivalent to lambda^d=-1. Regularity and odd characteristic justify these equivalences.
3. For the (+,-) type, d=66 and both quotient groups have odd order: exactly 32 inverse pairs survive after excluding +1,-1, and no negative target exists. For (-,+), d=4: k=0 is the positive target at each side, while only the p-side admits the two order-eight traces k^2=2.
4. The proof excludes spurious roots of U_32 in the opposite torus types by their intersection gcd of 2; k=0 and k^2=2 have the asserted local types. The J=-1 compressed gcd formulas therefore hold for the entire regular branch under the stated prime/cross-gcd hypotheses. They are not merely necessary conditions.
5. The (+,+) and (-,-) counts reuse the d=2 branches correctly. In the (-,+) row, subtracting same-positive and same-empty pairs gives C_p- + 3 C_q+ - 4; opposite signed returns remain successes. Summing the four displayed expressions yields the two conditional character rates and the full regular numerator 17p+18q-2123. Adding exactly-one-side setup failures contributes 2(p-2)+2(q-2), giving 19p+20q-2131 over all pq parameters.
6. The rate is attached to an explicitly different hypothetical uniform sampler. The actual frozen k=3 run remains a single failed deterministic proposal. Unknown primality of the disclosed labels is retained. The theorem is conditional on a family of prime pairs; it does not prove those conditions for the fixture.
7. The exact gcd equivalence is lifted via squarefreeness. Prime-power ideal depth is not claimed from matching zero sets. The subsequent proposed straight-line ideal certificate is labeled an unconstructed sufficient interface, not a supplied generic compiler.

The new theorem changes the next action: this whole fixed-clock family has an explicitly sparse success set for the stated structural family. Optimizing transport alone preserves that set. Short observer computation and a selector that changes the success distribution must be evaluated separately.

The review does not establish novelty, a generic lower bound, an implementation, an accepted theorem promotion, or completion of Shor. Existing BRC/heartbeat exact arithmetic restrictions remain attached to any future numerical work; they do not prevent portable symbolic continuation.

Global-Knowledge-Sync: main@2450bbb / GLOBAL_KNOWLEDGE_V1
