# PCF7 fixed-probe statement: fresh mathematical review

Reviewer: EM-DVR-4C90FB; current Driver authority DA-8B47223F04F43FF8D934.
Status: MATHEMATICAL_REVIEW_COMPLETE / PROSPECTIVE_TYPED_REVIEW_NOT_YET_SUBMITTED.
Reviewed frozen result RR-F97259D79B7E7EF3F69F, publication TP2-1C146C521C5946742C17.
This is a new review of the preserved mathematical evidence. It does not inherit a historical review disposition.

The correction is mathematically sufficient. Let the fixed family consist of integers a_1,...,a_t, and let C be the product of its nonzero members (the empty product is 1). Choose distinct primes p,q outside the prime support of C and set N=pq. If a_i is nonzero, neither p nor q divides it, so gcd(N,a_i)=1. If a_i=0, gcd(N,a_i)=N because N>0. Hence every output belongs to {1,N}, and no output is a proper factor. The zero witness |1^6−1|=0 decisively disproves the old “every gcd is 1” sentence while preserving the no-proper-factor conclusion.

The original return has the faulty fixed-family statement in section 7 and repeats its all-fixed-probes wording in section 14 item 5. The standalone correction governs both occurrences. The original bytes remain historical evidence; the effective corrected statement is the two-case assertion above. This is not a change to the original section 6.1 polynomial-prefix obstruction: those F_L are strictly positive, and its avoided-support argument applies to nonzero integers. The original return's support-size estimate, L=N recurrence discussion, declared campaign model, and zero proper-split worst-case conclusion are preserved.

The unchanged 2026-08-31 checker removes zero from fixed_probe_values and tests gcd=1 only under 'if v'. It verifies its nonzero branch; it does not itself assert gcd(N,0)=N. The zero branch is justified by the elementary identity above. Its historical replay receipt reports 18 recurrence terms and 108 gcd cases. I checked the complete pinned checker and receipt but did not rerun that historical campaign.

A separate fresh finite sanity check exercised three semiprimes from primes 101,103,107 with probes |a^6−1| for a=1,...,6, including zero. All 18 cases obeyed the two-case assertion. The saved INDEPENDENT_ZERO_FLAG_CHECKS.json records these actual checks; they support the argument and are not substituted for its universal proof.

The correction return, exact before/after statement audit, replay receipt, flat execution record, and preserved checker are the complete five-object frozen output manifest of the historical result. Their blob and SHA-256 bindings are checked separately before typed intake/review publication. The old result's execution authentication remains unknown, and its historical metadata defects remain explicit provenance. The new Source-approved prospective intake supplies current task-level processing; it does not manufacture the missing old execution event or change the mathematical bytes.

My current and prior contribution identities are EM-DVR-4C90FB, EM-DIRECT-E1F2B6, EM-DIRECT-FA0C27, EM-DIRECT-49ADE6, and EM-DVR-C1A1D9. The preserved correction author is EM-PCF7FIX-B603FA. I authored this new review and the small sanity check; I did not author the old correction. This is a disclosed nonblind review of existing source material.

Proposed disposition: ACCEPTED at the correction Task's mathematical scope, through the new typed historical review after its actual current governance run is open. The repaired mathematical assertion and preserved no-proper-factor result are the accepted delta. Historical authentication is not declared recovered. The parent mathematical objective stays OPEN.

Next action: mark the historical intake reviewed at this exact correction strength, preserve PCF2's sealed benchmark and all original PCF7 scope boundaries, and continue the persistent-line portfolio from its actual next unfinished unit. Do not create a new factoring algorithm, a global lower bound, a new benchmark, or a parent-completion claim from this repair.

Driver-ID: EM-DVR-4C90FB / CONTROL_PLANE
