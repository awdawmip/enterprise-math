# EC49FAO — H4/H5/H6-rooted H8/H9 exact 94-edge optimum
2026-11-04 — author-side finite theorem, exact integer JavaScript execution; independent Driver acceptance pending.

## Model and inherited frozen inputs

Scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Prior finite proof EC49FAN at immutable GitHub commit `4d2365a5cc26620899ead9d94b13e67f5249e96a`. For each source schedule 1512, 1513, 2200, 2203, fix all H2–H7 selected operation words, carrying 72 native signed primitive prefix edges, four six-coordinate positive BRC cache keys, six observation signatures, nine exact start states and five buckets. Original seven operation codes and the endpoint condition (2,0,0,0,0,0) remain unchanged.

**New candidate family:** Independently choose each H8 and H9 word by extending *any selected H4, H5 or H6 word* using an arbitrary ordered signed-X6 zero-displacement suffix of the required length. The H8/H9 selection may use distinct roots. Retain one full cache key per horizon, five distinct full keys in total, at most six global observation signatures and nine-history observation matrix rank nine over Q at each horizon.

## Theorem and proof

For each of the four fixed early schedules,

\[
\boxed{E_{H4\lor H5\lor H6\text{-rooted}}^*=94}.
\]

**Finite search exhaustiveness.** Enumerate all ordered words in the seven-letter language of zero *six-axis* displacement at suffix lengths 1,2,3,4,5. Their exact counts are 4,18,88,454,2424. For each fixed root and desired horizon, append every suffix, retain its full native primitive signed sequence, complete positive six-axis BRC key, and the unchanged nine-start observation DFA signature. Eliminate only those violating the inherited six-signature set. Group every surviving word by complete key.

**Key constraint.** The inherited early schedule already uses four keys. In the four complete enumerations, no old key has enough eligible H8 or H9 words for rank nine; H8 and H9 must therefore share exactly one new fifth key K. The numbers of separately rank-nine eligible H8/H9 keys are (28,43) for schedules 1512,1513, and (22,34) for 2200,2203. The numbers of common new keys are 22,22,13,13 respectively: 70 complete cases.

**Rigorous edge inequality.** Let P0 be the fixed set of 72 primitive prefixes. For a given K let W8(K),W9(K) be the complete eligible word pools and Pref(W) their native signed primitive prefixes. Define

\[
d_8(K)=\min_{A\subseteq W_8(K),\;\operatorname{rank}_{\mathbb Q}A=9}
\big|\operatorname{Pref}(A)\setminus P_0\big| ,
\]

\[
d_9^+(K)=\min_{B\subseteq W_9(K),\;\operatorname{rank}_{\mathbb Q}B=9}
\big|\operatorname{Pref}(B)\setminus (P_0\cup\operatorname{Pref}(W_8(K)))\big| .
\]

For any admissible selections A,B, giving H9 all eligible H8 prefixes *for free* is an optimistic credit, hence

\[
E\ge72+d_8(K)+d_9^+(K).
\]

The exact signed-primitive trie dynamic program computes both minima: a state is the OR-mask of up to six represented observation signatures, an edge is charged precisely when its subtree supplies at least one selected signature and its prefix is not free. Exact rank-nine masks are computed by modular elimination modulo 1000003. Hadamard's bound on any 9x9 subdeterminant of the original 0/1 observation matrix is at most 3^9=19683<1000003, so full rank modulo that prime is equivalent to full rank over Q.

**Complete computed certificate.** Every one of the 70 key classes satisfies 72+d8+d9+ >=94. Per schedule the minimum is 94 and occurs at fifth key (5,5,1), (7,3,1), (5,5,1), (7,3,1) (the last three positive coordinates are 0,0,0). The prior verified EC49FAJ witness selecting H8={pc,pd : p in selected H7} and H9={pfg : p in selected H7} is in the newly enlarged rooted family, and has 94 native primitive edges. Therefore 94 is attained for all four cases.

## Execution and reproducibility

A self-contained JavaScript V8 execution in this run enumerated all five zero-net suffix lengths and all 70 key classes, built the exact signed-primitive OR-mask trie-DP, and returned no class with lower bound below 94. Its output summary is in `EXACT_REPORT_EC49FAO.json`. `VERIFY_EC49FAO.py` is a mechanically extended standalone Python version of the previously executed EC49FAN verifier, supplied to reproduce a detailed per-class certificate. Python execution of the adapted file remains pending in this run because the local Python/container executor returned `redis.exceptions.ResponseError`; this is a runtime limitation, not a mathematical inference. The exact JavaScript integer computation is the executed validation for this author-side claim.

## Research frontier and next EC49FAP

The four fixed H2-H7 candidate families now admit independently rooted H8/H9 extensions from H4, H5 or H6; their cost minimum is 94. The unrestricted H9 mother problem continues to have the author-side range 80<=E*_H9<=94. Next inspect selected H3 or earlier roots and, more importantly, optimize earlier H2-H7 schedules rather than repeat closed rooted families. Seek a complete valid 93-edge witness, or obtain a stronger lower-bound certificate. Preserve the native observer, signed primitive order, full key and frozen scientific pin.

## Authority

This is a published author-side proof computation and source artifact; native CLAIM, Result and independent Driver review need current source authority and are recorded separately. P000 and ACTIVE worldview are unchanged.
