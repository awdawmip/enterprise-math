# R339 TP₂ negative minor — portable research handoff

**Objective:** Continue the original signed twelve-term BRC Newton difference array investigation beyond R337/R338. Address true two-parameter entrywise positivity with proof or exact in-domain counterexample.

**New proven counterexample:** D[5,0]=7008, D[5,1]=43600, D[6,0]=80512, D[6,1]=414400; ordered 2×2 minor M[5,0]=-606208000<0. This disproves global TN₂/TP₂ for the original D array; all four entries are positive. Not a counterexample to entrywise or original triangle positivity. Earliest adjacent negative minor, since all 10 earlier admissible minors positive. A bounded scan found k=0 only negative for q5..64, and k=0 negatives through q128; do not extrapolate that finite pattern.

**Source:** R337 original recurrence and rational numerator proof c6ac4da8e2b575a7538b4590d345c2e624057a63, R338 Draft PR #1573. Global fixed read main@d9c91d03eff26a0dfeb2bba85ce7d0a467f35c23 / GLOBAL_KNOWLEDGE_V1, Enterprise Math main@6aae6b092a857449c3ab29c724bb17ed30fe589c. P000/ACTIVE unchanged.

**Evidence:** R339_TP2_COUNTEREXAMPLE_AUTHOR_PROOF.zh-CN.md; R339_VERIFY.py, R339_EVIDENCE.json. Local exact code ran and passed: 2,080 adjacent minors q<=64 (2,020 positive, 60 negative), first 10 positive, k0 sign scan q<=128, 56 crosschecks with independent rational numerator representation, B_s to s130, 8,646 positive triangle coefficients, 3,642 retained negative exterior coefficients. Digest of "q:minor\n" edge sequence: 4bf3269334c9ca8be957e89daa1a6b77bc72dfaa3e9b898a245d73fd9fcb5a52.

**Reproduce remote code:** python R339_VERIFY.py --limit 128 --output reproduced.json. Remote code is a self-contained extension of the original R337 exact helper. Remote byte edition needs its own execution check before claiming identical run, though mathematical witness and independent local verifier are exact.

**Next:** Prove or refute all-q edge-sign assertion M[q,0]<0 for q>=5; investigate restricted k>=1 adjacent minors; prioritize a two-index entrywise nonnegative decomposition not implying global TN₂. Keep historical q<=640 row and r<=321 diagonal positive certificates; don't conflate sufficient-cone failure with negative D entry.

**Authority:** author-side local Researcher-ID EM-AUTO3-R339-TP2-2030; activity RA-EMR3-20261027-R339-TP2-2030 persisted as bookkeeping; owner native verification returned CONTROL_QUOTA, no native CLAIM/Source Result/independent Driver review. No Foundation, Working Truth or X6 native transfer.
