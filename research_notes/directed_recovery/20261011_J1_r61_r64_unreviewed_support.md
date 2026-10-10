# J1 finite-field auxiliary research: r=61..64 exact square certificates

Status: UNCLAIMED_SUPPORTING_RESEARCH / UNREVIEWED / NOT_ADMITTED.
Date: 2026-10-11 Asia/Shanghai.
Task context: RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT (TP2-39ACFC69F85D8661CFBF). This independent arithmetic support DOES NOT finish the task's external prior-art audit or replace a native CLAIM/Result/Driver review.
Pinned source: global-knowledge main 7b33f8066e9993e7c941959a9d738ed405248eb8; enterprise-math main 5873e3e48b549cf7a23d310c3c0ea6926943dc6c. P000 six-dimensional native reality remains the project premise; this is a separately typed classical finite-field lemma.

## Exact definitions and proof of the branch formula

Let q be an odd prime, s>=3 odd, k=(q-s)/2>=1, and Lambda_s(a)=-s*a-(2*a)^(-1) mod q for a in F_q^*. Set J_s={-(s-1)/2,...,(s-1)/2} mod q; E(q,k) is the NUMBER OF INPUTS a with Lambda_s(a) outside J_s, counting all multiplicities.

For any output b, the equation 2s*a^2+2b*a+1=0 has 1+chi_q(b^2-2s) roots. The exterior outputs form k pairs +/-b_j, b_j=(s+1)/2+j (0<=j<k). With i=k-1-j, 4(b_j^2-2s)=(2i+1)^2+16k mod q. Thus, exactly,
E(q,k)=2*sum_{i=0}^{k-1} (1+chi_q((2i+1)^2+16k)).
This is a branch-count observer, not merely the size of the output set.

## Four new exact integer witnesses

For each r=61,62,63,64 set k=2^r, N_j=(2j+1)^2+16k, q_min=2k+3. A separate machine-readable certificate supplies odd-size distinct index lists I_r, exact proper divisor witnesses 0<d_j<N_j with 0<d_j,N_j/d_j<q_min, and exact integer T_r with product_{j in I_r} N_j=T_r^2.

r=61: count 913, max j 693731, max divisor 19483, T decimal digits 8933.
r=62: count 1035, max j 882899, max divisor 36821, T decimal digits 10282.
r=63: count 1131, max j 921969, max divisor 44683, T decimal digits 11406.
r=64: count 1365, max j 1180399, max divisor 80669, T decimal digits 13971.

For every allowed prime q>=q_min, none of the N_j is divisible by q. The Legendre product of an odd number of nonzero N_j equals +1 because their integer product is a square; hence not all individual Legendre symbols can be -1. A +1 contributes 4 to E. Therefore E(q,2^r)>=4 for all allowed q and r=61..64.

The original full certificate, standalone standard-library verifier, proof report, search code/logs, earlier verified archive and SHA256 manifest have been generated together as EM_R2_J1_r61_r64_portable_bundle.zip in the conversation holding this support contribution. Full certificate SHA256: f4d79e8cb9d480b71a6b8f111e4271d1d58c0abb74be98812355657fa16398c1. Portable ZIP SHA256: 8d2a94c2fb18e823722e688e4e4408a40c630cf064087e3e33942f5bc1cbcb15. These referenced conversation artifacts are NOT asserted to reside in this Git repository.

Local independent verification: 4/4 newly constructed exact square witnesses PASS; historical r=5..50 archive rerun 46/46 PASS and r=51..60 10/10 PASS. If the inherited separately established non-power-of-two theorem is accepted, the finite interval exclusion now extends to 17<=k<=2^64. NO infinite-r statement follows.

Bounded abstract-level prior-art sampling: O. Kucuksakalli (2014), Value sets of Lattes maps over finite fields, DOI 10.1016/j.jnt.2014.04.014; D. R. Heath-Brown (2016), Small solutions of quadratic congruences..., DOI 10.1112/S0025579315000364; T. W. Cusick (1998), Value Sets of Some Polynomials..., DOI 10.1137/S0097539794270352. No exact symmetric-consecutive-residue containment statement was established from these limited abstracts; this is NOT a novelty finding or complete full-text audit. The already Source-documented generic x+alpha/x image-cardinality antecedent remains in place.

Pending: deposit all complete machine certificates to the authorized research artifact destination and independent review; current native session_start was refused STATIC_READONLY_SCOPE_DENIED (operation not sent). Task live Source was HANDOFF_READY / NEEDS_DISPATCH, NO_LIVE_CLAIM; this document creates no formal ownership. The next mathematical unit is r=65 and/or a uniform r proof, with full J1 interval-containment source comparison still independently required.
