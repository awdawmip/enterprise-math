# Parent review of the Jacobi torus selector

Status: PASS / FULL_TEXT_SYMBOLIC_REVIEW / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED.

The root coordinator read the complete JACOBI_TORUS_SELECTOR.md, SHA-256 30fc0de14df7eef7f43c30838fbe1dd47c60db85982ac5d92bfc0c863d2cdf2f, and its author self-review 63e18a0cff8e6f6be0e496b359a8221c7861cb773956d430cc9f537851202928. The underlying exact-fiber proof and separate shared-context review were also read in full. The raw typed Jacobi source and proof were previously read without importing or running them. This review makes no numerical reference evaluation.

The pointwise theorem is correct on its explicit promise. For a product of distinct primes congruent to 3 modulo 4, regular discriminant Jacobi -1 forces one split group of order twice an odd number and one nonsplit group. An even dyadic exponent has no regular positive or negative return in the split group: the positive kernel consists only of the excluded eigenvalues, and the negative congruence is insoluble. Thus either signed marked main-clock gcd is 1 or the nonsplit prime. This is a no-saturation result, not a guarantee of a nonunit result. The promised prime congruences cannot be inferred from N modulo 4.

The two orientation weights correctly use trace counts rather than equal weights. With R=(p-2)(q-2), expanding the two cross-type counts gives (R-1)/2 accepted traces and conditional acceptance (R-1)/(2R). Conditioning on an orientation leaves uniform local trace distributions in their respective type sets. Removing the exceptional inverse-fixed eigenvalues gives exactly (d-2)/(r-1) for the positive event and h/(r-1) for the negative event. Their union and the weighted accepted probability are consequently correct. The p=3 boundary has one empty orientation but a positive total denominator and is treated without dividing by the empty set size.

The dyadic rate cap is substantive. A large unknown odd part of the nonsplit group order is still present. The filter can remove simultaneous return while leaving almost all accepted trials as units. It does not establish a useful unconditional or adaptive first-hit rate. In particular, the rate for a fixed accepted parameter distribution must not be reused after arbitrary adaptive changes in parameters or clocks.

The second-clock distinction is necessary and correctly stated. E+2 need not be dyadic, so the scalar translated section can combine a main return in one component with a second-clock return in the other. The source promises no no-saturation result for that union. The adjacent-trace numerical run in this milestone does not call Jacobi and is not an execution of this selector.

The identified primitive is the generic typed_jacobi_trace, source ce7168c8724d1fff216b903f09cdaf7fe16c8074c48488f7b26fb80584060402 and proof fc51f6feb6134b2d1443efd9751f26621478a25512cc2d3784ae63045c5c7161. Its old QFT/square-schedule interfaces have separate hypotheses and are excluded from the proposed integration. A future implementation must bind the typed discriminant producer, actual Jacobi trace, admission outcome and paid observer. Rejected proposals and any reused gcd evidence retain their real costs.

No correction is required within this scope. This is a useful conditional component and a clear continuation interface; it is not a complete factor-blind exponent selector, a new benchmark, a generic factoring advantage or Shor closure. Standard torus/Jacobi mathematics is not claimed as globally novel because it has been expressed through this project's native interfaces.

Global-Knowledge-Sync: main@8c23cca / GLOBAL_KNOWLEDGE_V1.
