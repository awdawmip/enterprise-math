# D25 Katz comparison: incremental Driver audit

Status: BOUNDED_AUDIT_COMPLETE / AUTHOR_SOURCE_BYTES_VERIFIED / NO_BLOCKING_ERROR_FOUND / LIFT_OPEN.
Reviewer: EM-DVR-E33955, session MCP-d5d834098aab44f0a02f749bd9d23870, DA-93D032174BAD288F8F29, authority comment 6060336942.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7.
This is an incremental, conditional-model audit. It is not an RR/DR, whole-Task acceptance, identification of actual c or kappa, or closure of LIFT/JT2.

## Scope and independence

The author is EM-ENTERPRISE-B078A6, session MCP-bb6f343045854a798ca781ee73de2e39, RA-8C8E44B2AA373F98BC5952A3, claim MCP-3d6d72356bcdfef82ab4cfc4, ER-7C265B422DC8E829AD44, authorized run RUN-252e05a5823d9e33ff848863 generation 1. This is the same nonreleased research execution, not a restart of its predecessor.

I reviewed the complete frozen V1 of D25_KATZ_COMPARISON_REPRESENTATIVE_BOUNDARY.md, SHA256 f0b077671308a5133485e3544163e02717b865127bcab2bd3bb233a7c0ba3b00. My sole requested final edit was the precise attribution of the natural-map sentence to the discussion immediately after Theorem 5.1.6, rather than to the theorem statement itself. The proof and its conditional scope required no correction. I checked the complete V1-to-V2 diff: only the version labels and that source attribution changed. Final V2 SHA256 is 12e0c73f71fe6e4e83ef3c9a4bcd536354126dd83f71bcef7353cc7229523269.

My exposure includes the prior D25 frontier, Owner direction, the first new no-go report and its audit, and source discussion with the author. I supplied the author-hosted Katz PDF locator and required map/representative typing; I did not supply the new isomorphism, inverse, perturbation, or coefficient construction. This is independent checking of a directed incremental claim, not blind discovery. A separate source-support Driver extracted primary definitions and page locations without seeing the new proof; that work is source evidence, not a second mathematical verdict.

No mathematical program was run for this addendum by the author at its freeze or by me in this review. Exact coefficient arguments suffice for the declared claim. File hash computations and page renderings are evidence handling, not numerical proof tests.

## Source verification and logical separation

Primary source: Nicholas M. Katz, Crystalline cohomology, Dieudonne modules, and Jacobi sums, author-hosted https://web.math.princeton.edu/~nmk/old/CrCohDModJacSum.pdf. PDF SHA256 547d6d6059d66b3809bed2d3f9c0301a62e07355bd994259ccc0533815b99da0, 1191723 bytes. Printed page equals PDF sequence page plus 164 for the used pages.

I directly inspected the relevant original images on printed pages 193, 194, 198, 199, 202, 203, 204, 205 and 208. This records inspection of the passages used here, not complete proof verification of every statement on those pages. The broader support extraction has its own explicitly narrower reading record; I do not adopt its entire page list as my own.

- Page 193 separates the numerator and denominator conditions. D_p requires integral differential and a group cocycle in pA[[X,Y]], then quotients by zero-constant pA[[X]]. Ordinary D requires only integral cocycle and quotients by zero-constant A[[X]]. Full formal de Rham quotients do not automatically satisfy the primitive/group condition.
- Page 194, immediately after Theorem 5.1.6, says the natural D_I to D map is not in general an isomorphism; its kernel and cokernel are killed by I. This map uses the same primitive on both sides.
- Pages 198–199 assume perfect k and A=W(k). The maps w and psi from Witt covectors are respectively linear and sigma-linear isomorphisms. Diagram 5.5.5 labels a different arrow (1/p)F between the modified and ordinary formal de Rham objects. Diagram 5.5.7 restricts to primitive modules for a p-divisible commutative formal Lie group. The group hypothesis is substantive.
- Pages 202–204 give Theorem 5.7.1 and the crystalline/de Rham/formal restriction diagram for an abelian scheme over Witt vectors of an algebraically closed field. The primitive inclusion is expressly labelled. Page 205 states the proper, smooth, pointed hypotheses for General Fact 5.7.6 and its lifting compatibility.
- Page 208, Corollary 5.7.8 proof, uses a pointed lift of X to X^p and the differential identity d(X^p+pY) in p Omega^1 for its topological-nilpotence purpose. This does not identify every comparison representative or the particular companion used in the 2013 paper.

These passages support the distinction between the natural quotient and the divided Frobenius comparison. They do not by themselves identify the 2013 source's representative-level normalization. No inspected single sentence is claimed to state the full general sigma-substitution definition that remains unlocated in the source-support reader's bounded range.

## Independent proof check

The explicit model has A=W(k), k perfect, p odd, fraction field L, and Witt automorphism sigma. Let M be zero-constant formal primitives with integral derivative, I=X A[[X]], N=M/pI and O=M/I. The author defines Ktilde(U)=U^sigma(X^p)/p and K:N to O.

Writing U as sum u_(n-1) X^n/n proves the output derivative is integral. Replacing U by U+pH changes the output by H^sigma(X^p), which belongs to I. Thus K is well defined and sigma-semilinear. If its output is integral, each coefficient of U belongs to pA after applying the inverse automorphism; its kernel in N is zero.

For B=sum b_(m-1) X^m/m, the proposed inverse primitive has coefficient sigma^(-1)(b_(pn-1))/n at X^n. Its derivative is integral. Applying K retains exactly the terms of B with exponent divisible by p; the remaining terms are integral because their denominators are prime to p. If B changes by an integral H, this inverse changes by p times an integral primitive. This checks surjectivity and independence from the representative. It is a genuine isomorphism of the explicitly specified full formal quotients.

The test q([X])=0 and K([X])=[X^p/p] nonzero distinguishes the two full-formal maps. The author correctly declines to assert that [X] is primitive for a particular formal group. The proof of the full-formal isomorphism is not used as a proof of the primitive restriction or its applicability to the actual CM companion.

Under the author's additional comparison, primitive-class and same-ordinary-class hypotheses, adding p eta X to U is zero in D_p. Its group cocycle is p eta times (X+_G Y-X-Y), so the numerator condition also remains satisfied. The selected output primitive changes by eta^sigma X^p, an integral primitive with integral group cocycle. Both primitive classes and every condition stated only on those fixed classes are preserved.

The leading term of the ordinary differential stays fixed for p>1. In contrast, the leading term of the DP differential changes by p eta. Thus exact DP leading normalization would exclude this family, and normalization modulo p^2 would already fix its residue parameter. The report explicitly retains this boundary; it does not claim ambiguity under a stronger representative-level condition.

Only after the same-class bridge B-B0 in I is assumed does the previous kappa observer apply. Its change is eta^sigma modulo p, covering the residue field. Holding B0 and the regular correction H0 fixed, the coefficient identity in the report reads kappa from u0^sigma/p + [X^p]H0 - [X^p]B0. Its integrality is supplied by the same-class premise. This explains why u0 modulo p^2 is needed, whereas the DP class records only u0 modulo p. It does not compute the actual kappa or identify an actual source choice.

The construction holds the ordinary CM class fixed, so it is not an ambiguity proof for the ordinary scalar c. The 2013 paper's leading-coefficient-one statement still requires identification of the representative layer to which it applies. No source theorem is negated by this conditional example.

## Disposition and next obligation

NO_BLOCKING_ERROR_FOUND for the defined full-formal isomorphism and conditional representative/coefficient boundary. The result is a precise interface clarification. Its applicability to the actual 2013 companion is not established. It cannot close the hard target Delta_p congruent R_p, LIFT/JT2, or the arithmetic parent.

Method harvest: task-specific explicit formal-series coefficient reasoning and source-model disambiguation; no new general-purpose toolbox family is justified. This does not repeat the old fixed-coordinate exclusion or the first increment's impossible literal eigenlift. It also does not replace full compatible class conditions by ordinary cohomology alone.

The minimum remaining data for this model are the actual comparison/section, proof of primitive restriction and same-class relation, and representative normalization through the required extra DP leading digit with H0 and B0 fixed. Until an actual source changes those data, Owner directs that this conditional branch be retained rather than expanded into new unverified model families. The next executable research unit is the actual E3 invariant differential/Picard–Fuchs period gauge and ordinary CM normalization c; it must be frozen and audited separately from any DP lift. No value for c is approved by this audit, and the target product congruence may not be used to define it.

Native P000 space remains six-dimensional discrete Cell space with no native plane. This elliptic/formal algebra has explicit external type and makes no full-X6 propagation claim. The mathematical parent remains OPEN; user_requested_stop=false.

## Actual Source persistence and complete readback

Author V2 was published by checkpoint request d25-katz-final-checkpoint-20261008-r2 (bridge #3311), Source 21e51ac932109ebcdc396eb48ad1f2a419dd7da7. Its artifact prefix is research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT/MCP-bb6f343045854a798ca781ee73de2e39/13f97bdc12e49d101d97/.

I independently fetched the complete report, source extraction, source manifest, source render script and checkpoint through the GitHub connector at that exact Source. Full content SHA256 and Git blob identifiers matched; the four artifact files also matched the reviewed local bytes exactly. Local evidence: KATZ_FINAL_READBACK_0.json through KATZ_FINAL_READBACK_4.json and KATZ_FINAL_EXACT_VERIFICATION.json.

- Report: 12202 bytes, SHA256 12e0c73f71fe6e4e83ef3c9a4bcd536354126dd83f71bcef7353cc7229523269, Git blob 3020a9db339c1b0cf0bf6fef3ca4cab4dfb8f508.
- Source extraction: 12183 bytes, SHA256 f350a6227422dbb582587e1262fba72a70c0ad6263b8184fdbeb4172ebc47afb, Git blob f8159a9239721366dfde6c1601647fbac50ce009.
- Evidence manifest: 8619 bytes, SHA256 cf1aca308ddede8c78861843d521632907f7eaaa35348a68765e41cde52507a7, Git blob c783b136c5527e7e3dea477cf50f7920daa3174c.
- Render script: 2069 bytes, SHA256 ff12b4606af94647619e249b3fc78172bba5dfd1b972683f33b5b2435864a492, Git blob d182208ba15d42a5be771931ed344101e2e88171.
- Checkpoint: 14369 bytes, SHA256 a54251eb49dd472da6441423e19ae8fd1d9d038b82e7ae52d9926d0d9d3e8889, Git blob 357a41a8837ffc4287ec0c81dc281845beedd344.

The checkpoint retains the preceding proved units, old C_p correction and exact no-repeat boundaries. At that checkpoint the ordinary c unit was still in progress; no later c value is retroactively attributed to it. The V1 checkpoint at aa65af5b25d22a797c455cb83fd1a2b4c69ba0f0 remains historical; V2 did not overwrite that publication. This audit does not claim an RR/DR or final release from this nonrelease checkpoint.

Driver-ID: EM-DVR-E33955 / CONTROL_PLANE
