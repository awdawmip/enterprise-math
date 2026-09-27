# Review of the joint-character signed-return fibers

Status: PASS_FULL_TEXT_PURE_SYMBOLIC_REVIEW / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED.

Reviewed in full:

- JOINT_CHARACTER_FIBERS.md, SHA-256 5a60e21262e880797af799b8fd5e23155f6a1cec2a26f8ecc2cbe7375b0a1323.
- JOINT_CHARACTER_FIBERS_SELF_REVIEW.md, SHA-256 41dbf26baf2ee9f7b03d994411b775e60f4e5dd0cd11ebd5aad2665a46dd7737.
- NATIVE_DUAL_CHARACTER_INTEGRATION_AUDIT.md, SHA-256 8737b9ed675d21a3792b4d311b884df3bb83e46451845057ee8bbedab855f867.

This is a separate review by a collaborator sharing the same author context and prior proofs, not independent mathematical admission. No scientific module was imported, no reference arithmetic or numerical fixture was evaluated, and no provider query was made. This unit does not alter or enlarge the already frozen adjacent-trace experiment.

## Local character classes and the exceptional roots

For an odd prime r and regular trace k, the split or norm-one eigenvalue group has even size L=r-sigma. Inversion pairs every element except 1 and -1, and the torus square character eta=(-1)^i is invariant under that pairing. The split and nonsplit derivations of eta=Legendre(k+2) in section 1 are correct; regularity is used before dividing by lambda+1.

Each character class initially has L/2 elements. The root 1 removes one element only from eta=+1, and -1 removes one only from eta=h=(-1)^(L/2). The remaining elements all have inverse orbits of size two. This proves the first expression for C_r in equation (2), including its integrality and nonnegativity. Because h=alpha_r*sigma, expanding the two indicators gives the stated second expression. The four-column table and both small-prime empty-class boundaries follow symbolically. A zero class must retain weight zero; it must not be treated as a conditional distribution.

## Signed power fibers

Write g=gcd(E,L), a=L/g. Positive solutions have exponents i=a*t for 0<=t<g. When a is odd, g is even, giving half the solutions in either character class; when a is even all solutions have eta=+1. This proves equation (3).

Negative solutions require g to divide L/2, which is equivalent to a being even. In that case (E/g)i=a/2 modulo a has an invertible odd coefficient and an odd inverse. Hence every solution has parity a/2 modulo 2, independent of any further odd part of E/g. Adding a preserves that parity, so all g solutions belong to precisely the class eta=(-1)^(a/2). When a is odd there are no negative solutions. In particular a=1 uses no modular inverse. Equation (4) is therefore correct.

The corrections in equation (5) remove exactly the actual exceptional solutions. The root 1 is always positive; -1 is positive for even E and negative for odd E. Neither correction may be copied into other character classes. After these removals, inversion again divides each count by two. The two signs cannot overlap in odd characteristic. This establishes equation (6), rather than relying on numerical checks of nonnegative fractions.

The E=0 boundary is included consistently: g=L and a=1 give the full class as positive and no negative return. At E=1 only the excluded roots could satisfy either equation, so both regular counts vanish. The source's symbolic r=3 boundary is consistent with its four-element norm-one group. Negative exponents are not silently introduced as an implemented feature.

## Global normalization and dependence

For N=pq with distinct odd primes, CRT makes the local parameters independent before the two global constraints are imposed. It does not make the characters independent. Summing equation (2) over local classes gives the four totals r-2, -1, -1 and -alpha_r. Expanding the indicator of the prescribed global signs j and e therefore gives

    Z = ((p-2)(q-2) + j + e + alpha_p*alpha_q*j*e)/4.

This proves equation (7), including the cross term. The orientation weights C_p(sigma,eta) C_q(j*sigma,e*eta) are the correct counts, not four equal weights. Empty orientations contribute zero; the conditional law is formed only when Z>0. Uniformity over all residues and uniformity conditioned on regularity have the distinct acceptance denominators N and (p-2)(q-2) specified in the source.

Equation (8) follows from the same totals. For distinct odd primes R=(p-2)(q-2)>1, so (alpha R-1)/R^2 is nonzero. The two observable Jacobi signs are thus correlated under that law. The example of a balanced conditional sign when alpha=1 and j=-1 is compatible with this covariance, not a claim of independence. A repeated-prime modulus or a different proposal distribution has no automatic entitlement to this two-prime conditional law.

## Readout categories and admissible clocks

For one sign, the four count products in equation (9) partition every orientation's CRT product. Their sum is C_p*C_q. This formulation avoids dividing by an empty local class and gives the proper four divisor labels on a squarefree semiprime. The p and q labels are analysis only; they are not supplied to the algorithm.

For both main signs, the three local labels are positive, negative and neither. Equal labels produce no proper divisor from those two specified primitive observers, whereas any unequal labels produce a proper divisor. This proves equation (10), including mixed positive/negative returns. Ordinary trace or individual-coordinate observers are different contracts and do not change this calculation.

At one fixed sign, the sets for E and E+2 are disjoint on regular traces: membership in both forces lambda^2=1. Consequently the same three-label argument applies to the marked first clock and its exact second-clock quotient. The warning about opposite signs at the two clocks is necessary; fourth roots can create an overlap, so all four events cannot be treated as four disjoint categories.

The public E=N-j is fixed after conditioning on j,e and may be inserted into the formulas. Its common local kernel size and nonsaturating negative branch are reused correctly. Additional character conditioning cannot create a pointwise impossible simultaneous negative return. The analysis still depends on unknown local group orders and their gcds and provides no numerical rate oracle to production. If E or the parameter proposal depends on additional observations of k, the within-class law must be derived again. Retry or first-hit laws also need their full selection process, not merely a reuse of the one-proposal marginal.

## Limited check of the proposed native interface

The integration audit is consistent with a limited read-only source check performed for this review. The generic typed_jacobi_trace and verify_typed_jacobi definitions, imports and cost construction were read from typed_jacobi.py at ce7168c8724d1fff216b903f09cdaf7fe16c8074c48488f7b26fb80584060402. The Arithmetic constructor, retention, add/compare/multiply/divide interfaces and CALLS binding were checked in lazy_modular.py at 08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4. No functions were imported or invoked. This was not a new review of the old QFT theorem or the entire arithmetic implementation.

Each Jacobi call creates its own operation stream while using the source-bound catalog through the shared loaded module. Label wiring is separate from arithmetic digit work. The verifier actually calls the arithmetic routine again; it is scientific replay and cannot be charged as a file-only audit. Both actual numerator producers must be linked to their certificates. The original setup gcd remains chargeable under literal reuse. Forming the integer E=N-j requires a paid add or compare/difference operation with the correct integer output contract, not an unrecorded host expression or an arbitrary modular subtraction substituted for integer construction.

The audit correctly requires rejection/factor outcomes, both character costs, chosen exponents, propagation, observers, exact divisions and validation to remain in the ledger. An exact probability formula does not supply a sampler, factor oracle or favorable proposal law. The frozen four-case experiment did not execute this composition.

## Outcome

No substantive mathematical or interface-plan correction is required. The deliverable is a proved joint count law with explicit local exclusions, dependence and sampling scope. A useful continuation must now derive factor-blind bounds or selection information that addresses the remaining odd-order component, and pay for any native integration. This review adds no runtime, success-rate experiment, speed claim or Shor closure.

Global-Knowledge-Sync: main@a668c14 / GLOBAL_KNOWLEDGE_V1. The shipped helper actually returned PASS/BEFORE_WRITE_REFRESHED at a668c148c80cf836ff7e520ccb57e8d0e919b731, fetched 2026-09-27T12:55:37.4075110Z with a six-hour lease. The three canonical entry files were read; the change from the previously read b304760 snapshot comprised two journal additions and no policy changes. Earlier authors' source markers remain their own provenance.
