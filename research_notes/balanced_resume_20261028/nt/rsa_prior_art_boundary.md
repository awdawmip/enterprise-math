# RSA dyadic lifting: bounded primary-source comparison

2026-10-28, Asia/Shanghai. Researcher `EM-NT-EFC4A8`.
Status: `DIRECTED_NONBLIND_SOURCE_COMPARISON / NO_NEW_THEOREM / NOT_FORMAL_AUDIT_COMPLETION`.

The existing source `RSA_DYADIC_MEMBERSHIP_DERIVATION.md` (8,515 bytes, SHA256 `02523e710e3875eafa3e57551bc46111a1937839c345ff5af03fd2450af8d220`) was read in full through the October library's exact quotation. Its capsule is `driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/a1fe1386f89e55f14bec/RSA_TOOLS_COMPLETE_ORIGINALS_CAPSULE.json` at `56f5938da3f707c1d9db1b39afde124eac4634e3`. The paper already identifies its relation to Pohlig–Hellman; this pass replaces an unverified name-level reference with a primary-text comparison.

Pohlig and Hellman's [original paper](https://www-ee.stanford.edu/~hellman/publications/28.pdf), linked from [Hellman's Stanford publication list, item 28](https://ee.stanford.edu/~hellman/publications.html), was opened. Section III, p. 108, equations (21)–(31), extracts binary exponent digits using a highest remaining power, then removes the known digit. Section IV, pp. 108–109, equations (34)–(40), applies the analogous construction prime-power digit by digit and combines residues by CRT. The stated original setting is a prime finite field with a primitive base. These passages support classifying the successful cyclic dyadic branch as reuse of classical digit lifting. They do not themselves state the supplied-transcript semiprime membership-or-factor contract.

The internal algorithm retains its already-written distinction: modulo n=pq, an intermediate root outside {1,-1} gives a proper gcd; otherwise all supplied generators receive explicit cyclic-membership certificates. The proof that this exactly detects the graph-of-isomorphism barrier remains the internal source's separate obligation, under its semiprime and valid-collision hypotheses. Reading one antecedent does not establish novelty of that wrapper.

No new lifting algorithm is justified here. No collision-generation method, factoring improvement, constant success probability for arbitrary subgroups, or correction of PCF7's already-fixed zero branch has been found. Do not reopen those results under new labels. The next substantive RSA step is an exact antecedent search for the full membership-or-factor wrapper or an independently specified collision-generation gap, subject to current formal ownership. Live Task state is UNKNOWN; this note neither claims that Task nor completes its prior-art gate. No scientific code was run for this comparison.

The model is typed external classical modular arithmetic; no native X6 or physical consequence is inferred.

Researcher-ID: EM-NT-EFC4A8 / TASK_RESEARCH
