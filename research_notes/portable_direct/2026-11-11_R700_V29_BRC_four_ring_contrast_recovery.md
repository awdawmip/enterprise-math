# R700 — Four-port V29 PASS-ring carrier for positive BRC source bins

Date: 2026-11-11 (Asia/Shanghai). Task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`; immutable publication \`TP2-8B7E13C5904A2D6F1142\`. Candidate research by actual service-issued Researcher \`EM-X6-5CA182\`, Activity \`RA-0C0FAA1156DB28848F34B175\`. Status: exact hand proof and full finite checker; **UNREVIEWED**, no formal CLAIM, Result, or Foundation promotion. Frozen task scientific input pins unchanged.

## 1. Input and typed BRC carrier

R699 frozen E* source: \`awdawmip/enterprise-math@55743642c88a24377ad4797cc2c6359c98b20553:research_notes/portable_direct/2026-11-11_R699_anisotropic_known_s_probe_frontier.md\`. The positive-BRC candidate has 60 distinct labeled tokens, divided into four group/output bins of capacity \`N=(24,18,6,12)\`. For an independently selected subset, retain individual token IDs \`(j,k)\` and the output histogram \`v=(e,t,c,z)\`, \`0≤v≤N\`, \`s=e+t+c+z>0\`. The raw packet preserves token identities, multiplicities and ordering when these are required by the future observer. We study a declared count-only projection, not a projection of full physical source history.

V29 native counting grammar source: \`research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md\` (current canonical Source blob 6849ebd3fc776fb7da3b46627376490aba3dad99). V39 declared based-loop future language: \`research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md\` (blob 8151d0b6a4b65225b93d858bbc8a5d7037bf9cef). These are author-side published FREE research sources, not asserted P000 Foundation.

## 2. Exact positive-BRC to V29 grammar encoding

Select one Cell with four **typed port identifiers** \`p0,p1,p2,p3\`. Define a candidate group-to-event carrier:
- each positive BRC token in bin 0 emits \`PASS(p0→p1)\`;
- bin 1 emits \`PASS(p1→p2)\`;
- bin 2 emits \`PASS(p2→p3)\`;
- bin 3 emits \`PASS(p3→p0)\`.

Use one independently identifiable PASS occurrence per token, initially zero V29 nonnegative ledger \`M\`; \`Rin=Rout=0\`. By the V29 primitive PASS increment law, \`M[0,1]=e, M[1,2]=t, M[2,3]=c, M[3,0]=z\`, and all other entries are zero. This is a positive multiset-to-count-monoid morphism, preserving multiplicity. The assignment of an E* source group to ports is **part of this proposed encoding**, not an established physical X6 Link/Port identification. Serialization/order must remain in the raw packet when future operations inspect it.

The native V29 contrast is \`u=M1−Mᵀ1=(e−z,t−e,c−t,z−c)\`; its signed circulation matrix is \`Ω=M−Mᵀ\`; \`Σu_i=0\` exactly. The PASS counter \`P=ΣM[a,b]=s\` for this packet, or \`ΔP=s\` from a declared baseline. Matched TRANSFER events leave M and P unchanged. Other PASS occurrences must be counted separately before inferring an E* gate count.

## 3. Theorem R700.1 — full recovery from contrast plus total

For every integer histogram \`v\` in the declared capacity box, the pair \`(u,s)\` determines \`v\` uniquely. The exact inverse is

\`\`\`text
e=(s+u0−2u1−u2)/4
t=e+u1
c=e+u1+u2
z=e−u0.
\`\`\`

**Proof.** The last three ring-difference equations express \`t,c,z\` in terms of \`e,u\`. Summing yields \`s=4e+2u1+u2−u0\`. Substitute and solve. For all realizable inputs, the integer congruence \`s≡2u1+u2−u0 (mod 4)\` follows. ∎

## 4. Theorem R700.2 — exactly seven possible contrast-only source histograms

For fixed \`u\`, two histograms differ by a common integer multiple of \`(1,1,1,1)\` because all their adjacent differences coincide. Since group-bin count \`c\` is between 0 and 6, every fixed-u fiber has at most seven distinct histograms. This bound is attained for

\`v_k=(k+1,k,k,k), k=0,…,6\`.

All seven satisfy \`N=(24,18,6,12)\`, are nonempty and give the same \`u=(1,−1,0,0)\`. Their totals are 1,5,9,13,17,21,25. Therefore, if one retains **only u**, the exact additional worst-case fixed-length memory required to identify the original four-bin histogram is \`ceil(log2 7)=3 bits\`, both necessary and sufficient. This is an information bound for the declared histogram observer, not for all raw source token IDs or all V39 futures. ∎

## 5. Theorem R700.3 — sharp tolerance for one noisy count channel

Let \`u\` be exact but measure \`s\` by \`ŝ\` with deterministic absolute error \`|ŝ−s|<2\`. The integer residue formula above restricts all feasible totals to one residue class modulo four; any distinct legal totals differ by at least four. Hence \`ŝ\` uniquely identifies the compatible total and the inverse reconstructs v.

The threshold is **uniformly sharp**. The legal pair \`(1,0,0,0)\` and \`(2,1,1,1)\` has identical \`u=(1,−1,0,0)\` but totals 1 and 5. The midpoint observation \`ŝ=3\` has error 2 for each; equality allows ambiguity. ∎

If \`u0,u1,u2\` are themselves observed with individual absolute error strictly less than 1/2, exact integer rounding followed by \`u3=−u0−u1−u2\` and the above total decoder gives a simple joint sufficient bound. Its full optimal anisotropic region remains to be studied.

## 6. Complete exact execution

The accompanying \`R700_V29_BRC_RING_VERIFY.js\` is the actually executed, self-contained V8 JavaScript exact-integer verifier. It emits each independent typed PASS increment for each selected positive token, not merely algebraic matrix formulas. Exhaustive enumeration covers all \`(25×19×7×13)−1=43,224\` nonempty legal histograms. It checks V29 M counts, exact conservation, integer inverse, congruence and uniqueness of \`(u,s)\`. It groups all histograms by u and verifies the maximum fiber seven and all seven explicit witnesses.

Observed run: \`R700_EXACT_BRC_V29_RING_PASS\`; 43,224 histograms, 43,224 distinct (u,s) signatures, **12,121 contrast fibers**, maximal fiber 7. All mathematics here is native BRC-positive-token counting and V29 integer PASS algebra; no classical π/trigonometric/series fallback was executed.

## 7. Native next step and unchanged mother task

The four arcs are syntax-admissible under V29's primitive count update. A **real X6** realization still requires specifying the actual Link/Port topology, the active signed triadic frame, legal schedulable PASS/TRANSFER words, full Path/BRC provenance, dependency order, and a V39 based loop with joint \`(j,h)\` cycle current and S3 holonomy. V39's \`L_JH\` observer is different from this count-only \`u,s\` observer. In particular, event-order futures, raw path witnesses and frame futures may distinguish histories with the same u,s.

The next discriminating experiment is to build one actual legal X6 loop packet with the full V29 ledger and V39 holonomy. Determine whether the four group-to-port rules are realizable; preserve an exact obstruction if any, and try an alternate native assignment. No change is made to P000, the frozen task publication, or the larger triadic closure/rotation-covariance mother question.
