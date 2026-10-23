# C266 / Research2 — five newly certified four-free pair hulls (AUTHOR_EXACT)

**Status:** author exact rational certificate; not an independent Research Driver review, formal Source Result, CLAIM, Working Truth, or native six-dimensional GF(2)-BRC theorem. This note is a durable continuation checkpoint, not admission.

## Pinned sources

- GLOBAL_KNOWLEDGE_V1: `main@674c44f8c3c194a82c63f0bba6da995d1d307ad3`.
- Enterprise Math: `main@fbe4038159c6601026c312a7b2f9d5fc3e0be7af`.
- Frozen parent C265 author ZIP SHA256: `dcf541ec1158d872eec5559548296197908e496da209a539f172955cbc73ff31`.
- Exact raw 79-node rational inputs, the 75 positive fixed branch weights and all analytic formulas are reproduced from the existing C265 standalone replay in the two-file C266 verifier. The model is C195/H168 **auxiliary** F, not a BRC signed/phase operation.

## Exact proposition

Let `I=(5,50,55,56)`, `J={0,...,78}\\I`, `Q=2^128`, `H=2^166`, `Z=141421356237309504880/10^20`, and `A=6912*50000^2/17^2`. Let `u_j` denote the 79 fixed exact rational nodes and let the positive integer `B_j` for `j in J` be

`B_j=floor(Q*A/(H*((2-u_j^2)*(3-u_j^2))^3)*product_{r != j} (Z-u_r)/abs(u_j-u_r)) > 0`.

The four-variable positive auxiliary function is

`F(v)=sum_{j in J} B_j * product_{p in I} [(Z-v_p)/(Z-u_p)*abs(u_j-u_p)/abs(u_j-v_p)]`
` + sum_{k in I} Q*A/(H*((2-v_k^2)*(3-v_k^2))^3) * product_{j in J}[(Z-u_j)/abs(v_k-u_j)] * product_{p in I, p!=k}[(Z-v_p)/abs(v_k-v_p)]`.

**C266-R2 author exact theorem:** Every legal real four-tuple in each of these *entire closed rectangles* satisfies `F(v) >= Q + 4638422976475146033089763949860511 > Q`.

| Root pair, zero-based | v5 | v50 | v55 | v56 | Strict leaves | Minimum floor(LB)-Q |
|---|---|---|---|---|---:|---:|
| (4,16) | [2/271,6/409] | [7/10,42/59] | [60/77,11/14] | [4/5,9/11] | 581 | 5158902987695659637439900477932651 |
| (12,29) | [3/371,6/409] | [7/10,27/38] | [18/23,53/67] | [19/24,4/5] | 88 | 46890424184761894156170614618712718 |
| (27,30) | [2/189,3/205] | [7/10,12/17] | [32/41,37/47] | [4/5,17/21] | 360 | 4638422976475146033089763949860511 |

The exact C254 interval containment check proves the first root also contains two other previously unknown pair hulls `(4,26)` and `(4,30)`. Thus **five old-unknown hulls** become strict-positive: `(4,16), (4,26), (4,30), (12,29), (27,30)`.

Relative to frozen C265, the **363 eligible** hulls change from `213 strict-negative witnesses + 103 continuous-positive proofs + 47 unknown` to `213 negative + 108 positive + 42 unknown`. The other 232 original combinations are outside this method's applicability and not claimed certified.

## Continuous, exact proof and executable evidence

The sibling `C266_R2_COMPACT_EXACT_CERTIFICATE.json` encodes three complete preorder bisection trees. Every internal `0/1/2/3` splits that coordinate at an **exact rational midpoint**, with left/right closed children covering the closed parent. Every `B/A/C/D/E` leaf selects the previously established exact BASE or SHARED_(5,50,55,56) convex-tangent lower bound for the full auxiliary function F; it never substitutes a floating estimate for a proof inequality.

The sibling `C266_R2_STANDALONE_EXACT_REPLAY.py` reconstructs all 79 rational nodes, 75 fixed positive masses, and each of the 1029 exact leaf bounds with Python standard-library `fractions.Fraction`. Every leaf verifies `floor(LB)-Q>0`. The certificate has **1029 positive leaves and 1026 rational bisections**; Python execution in the author environment ended in `C266_R2_AUTHOR_EXACT_PASS 1029 1026 4638422976475146033089763949860511`. This is **author replay**, not independent Driver admission or Lean formalization. Exploratory floating-point tree selection is not a universal proof.

**Replay:** save the two sibling files together and run `python C266_R2_STANDALONE_EXACT_REPLAY.py`. The statement and checker are explicitly confined to the four-active-variable auxiliary model. Branch labels, phase, ports, time and future-operation fidelity to native GF(2)-BRC remain unproved; positive branch mass is not signed amplitude. BRC applicability status: `NOT_APPLICABLE_TO_THIS_AUXILIARY_INEQUALITY_WITHOUT_BRIDGE`.

## Control, storage, and next discriminating task

The native service reported `em_control_tasks=CONTROL_QUOTA` and `em_session_start=STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`; no true active owner could be verified. This branch saves **author evidence only**; it does not replace native registration, task CLAIM, formal Result freeze or independent review.

The next mathematical target is a rigorous 2-shared-coordinate joint Hessian/tangent minorant for high-coverage four-dimensional hull `(0,16)`, which contained 21 previously unknown pairs at the C265 frontier; a bounded numeric split search did not certify the root at 2500 cuts. That bounded failure is not a counterexample. Validate new bounds with exact fractions; use native BRC only after establishing a typed auxiliary/native bridge.

**Provenance:** C265 parent, fixed C254 35-box coverage, C256 213 exact negative witnesses, and C265 103 positives; no unseen later research branches are assumed integrated.
