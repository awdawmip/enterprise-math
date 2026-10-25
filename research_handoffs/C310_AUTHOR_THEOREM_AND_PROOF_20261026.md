# C310 — Pairwise prime-field branch collision and exact extra p-adic content valuation

**2026-10-26 | AUTHOR HAND PROOF + EXACT LOCAL CERTIFICATES | NOT NATIVE SOURCE ADMITTED.**

## Exact provenance and scope

Account authority was read at one canonical \`GLOBAL_KNOWLEDGE_V1 main@28719731af88def01da147f49d19fb0a91474b5d\` snapshot. Enterprise Math mathematical inputs/P000/portable research protocol were read at \`main@6974c5530449705a1105bbadf5349c90ee65f574\`; this author branch may use a newer write-base main without changing those scientific pins. Immediate predecessor: C309 at \`research/c309-structural-content-prefix-20261026-research2@3b1d56d2b8256c0372f382abe0ad0125d5173c6c\`. Frozen C293 125-path input SHA256: \`03083a77480e6be5615797c2f4ffc503eee6603e9e60cbad1f11fb3ea83b3c89\`.

The application concerns the **C195/H168 79-positive-rational-branch auxiliary scalar** only; it depends on C300's still author-level exact factorization/cancellation identity. It is **not** native GF(2)-BRC or Heartbeat X6 propagation mathematics. P000's six native spatial axes and separately typed time are unchanged.

## Theorem A: exact joint-content quotient identity

Let \`s>=1\`, \`C,P,J_1,...,J_m∈Z[t]\`, \`content(C)=1\`, and \`CP=Σ_a J_a\`. Set \`content(0)=0\` and
\[
L=\gcd(s,\operatorname{content}(J_1),\ldots,\operatorname{content}(J_m)).
\]
Then all \`J_a/L\` and \`P/L\` lie in \`Z[t]\`, and with \`R=Σ_a J_a/L=C(P/L)\`:
\[
\boxed{\gcd(s,\operatorname{content}(P))
=L\,\gcd(s/L,\operatorname{content}(R)).}
\]
For **every** integer \`n>=1\`, \`n|content(P/L)\` iff \`R=0\` in \`(Z/nZ)[t]\`. If \`p|s/L\` is prime, \`R≡0 (mod p)\` and \`R\not\equiv0 (mod p²)\` prove \`v_p(content(P/L))=1\`.

**Proof.** \`L\` divides every coefficient of every \`J_a\`, hence \`R\` is integral. The C309 Gauss-content lemma gives \`L|content(P)\`, hence \`P/L\` integral. Since \`C\` primitive, Gauss multiplicativity gives \`content(R)=content(P/L)\`. Substitute \`s=L(s/L)\` and \`content(P)=L content(P/L)\` into gcd to obtain the boxed equality. Reduction of an integer polynomial modulo \`n\` is identically zero iff each coefficient is divisible by \`n\`; the prime and prime-square claims follow. QED.

## Theorem B: factor-bag certificate of branch collision

Fix a prime \`p\`. Reduce each factorized branch \`J_a/L\` modulo \`p\`. Normalize every nonzero factor as a leading scalar times a **monic** polynomial in \`F_p[t]\`; absorb leading scalars and constant factors into \`λ_a∈F_p\`, and preserve nonconstant monic factors as a **multiset** \`B_a\` (with multiplicity). If exactly two branches \`a,b\` remain nonzero, \`B_a=B_b\`, and \`λ_a+λ_b=0\`, then \`R≡0\` as a polynomial modulo \`p\`, proving the additional \`p\` in Theorem A. This does not depend on interpolation or sampled values.

**Proof.** Both surviving terms equal their scalar times the same product of monic factors; their sum is \`(λ_a+λ_b)∏B_a=0\`. All other branches vanish individually. \`R=0\` in \`F_p[t]\`, hence apply Theorem A. QED. For example \`J_1=t+1, J_2=t-1, C=1,s=2\` have termwise lower bound \`L=1\` but \`P=2t\`, showing the need for joint cancellation.

## Complete 19-path certificate

The C309 author audit exposed 19 paths with \`G_i/L_i\` equal to 2 (15 paths) or 3 (4 paths), where \`G_i\` was its historical C306 complete-Newton comparator. **That comparator selected a candidate p, not the congruence proof.** The exact frozen 79-term model circuit was independently reduced as a polynomial modulo \`p\` and \`p²\` for each of the 19.

Every one of the 19 has precisely **two surviving branches among 79**, their normalized factor bags agree exactly, and their normalized scalars add to zero. Full coefficient convolution modulo \`p\` independently yields the zero polynomial; a coefficient modulo \`p²\` gives an exact nonzero witness:

| Path indices | p | Surviving branches, zero based | First nonzero degree k modulo p² | Exact coefficient modulo p² |
|---|---:|---|---:|---:|
| 3 | 3 | (76,77) | 15 | 3 |
| 8 | 3 | (76,77) | 15 | 6 |
| 38 | 3 | (76,77) | 100 | 6 |
| 56 | 3 | (76,77) | 95 | 6 |
| 6,26,27,29,30,33,34,75,76,108 | 2 | (75,76) | 243 | 2 |
| 7,11,12,17,97 | 2 | (75,76) | 252 | 2 |

Hence the additional \`p\` factor in \`content(P_i/L_i)\` is **present and of exact p-adic valuation one** in all 19 cases, conditional only on the exact inherited factorized identity. In the parity cases the normalized scalar pair is (1,1); in the mod-3 cases it is (1,2) or (2,1). All remaining 77 branches vanish individually modulo the candidate prime.

**Executed exact scope:** 19/19 factor-bag equality and two-survivor checks; 19/19 complete coefficient reductions \`R mod p=0\`; 19/19 nonzero \`R mod p²\` witnesses; a second **stdlib-only truncated coefficient** algorithm independently recomputed each of the 19 reported p² witness residues. The two implementations share the C305 upstream factorized source: this is algorithmic cross-checking, **not** independent audit of C300.

**Important limitation:** exact p-primary valuation does not, by itself, exclude additional prime factors of \`s_i/L_i\`; the equalities \`G_i=L_i p\` for the full gcd remain supported only by the older C306 author comparator. No independent native Driver or Foundation theorem acceptance is claimed.

## BRC provenance and next discriminating question

The precise observer here is \`gcd(s,content(P))\` of a projected auxiliary scalar numerator. The complete 79-branch labels, positive branch masses, original ports, phase/sign, provenance and allowed future X6 operations are **not** proven preserved by this scalar reduction. It is not a native BRC branch cancellation. There is no native-state/readout-and-future-operation bridge, so P000 remains the only fixed native premise.

**Next C311:** construct a short composite-modulus coefficient/Bezout certificate independent of C306 that excludes *other* primes for the 19 exceptions, and arrange independent verification of C300 cancellation before project admission. The accompanying code and audit are author-level portable research evidence.

## Real authority/persistence boundary

Authenticated GitHub identity: \`awdawmip\`, repository \`push=true\`. Native gateway v0.6.11: \`em_control_tasks → CONTROL_QUOTA\`; \`em_session_start → STATIC_READONLY_SCOPE_DENIED\`, \`operation_sent=false\`. Current active Owner and official CLAIM could not be verified. GitHub author-branch saving does not imply Source Result, authenticated research activity, mathematical review or admission.