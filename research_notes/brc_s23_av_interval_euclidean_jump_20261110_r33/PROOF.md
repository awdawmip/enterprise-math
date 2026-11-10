# Enterprise Math R33 — Certified interval-Euclidean Farey jumps

Date: 2026-11-10. Frozen scientific pin: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Parent: R32 Draft PR #1929, source commit \`87fdeff1cba7055f50a5fd8dadaad390476d9da1\`. Scope: auxiliary irrational-circle observer, author-side lemma and exact finite validation, independent mathematical review pending.

## Certified common-prefix jump theorem

Let \`a/q < theta < c/j\` be Farey neighbors, \`q,j>=1\`, \`cq-aj=1\`, for irrational \`theta\` in a rational open interval \`(L,U)\`. Define \`A=q*theta-a>0\`, \`B=c-j*theta>0\`.

**Lower jump.** If \`A>B\` on the interval and \`A(t)>k*B(t)\` at both endpoints \`t=L,U\`, the next \`k\` Stern–Brocot updates replace only the lower neighbor; after update \`s\`, its value is \`(a+s*c)/(q+s*j)\`, \`1<=s<=k\`.

**Upper jump.** If \`B>A\` and \`B(t)>k*A(t)\` at both endpoints, the next \`k\` updates replace only the upper neighbor; after update \`s\`, it is \`(c+s*a)/(j+s*q)\`.

An exact integer-only certificate is the minimum of the two endpoint quotients: lower case \`k=min(floor(A(L)/B(L)),floor(A(U)/B(U)))\`; upper case \`k=min(floor(B(L)/A(L)),floor(B(U)/A(U)))\`, followed by explicit strict endpoint checks. These yield the maximal common *certified prefix within the two endpoint quotient bounds*. The entire continued-fraction quotient need not agree across \`(L,U)\`. Truncate the selected \`k\` to the next finite horizon boundary if applicable.

**Proof.** During lower updates the residual is \`A-sB\` for the \`s\`th new lower candidate, divided by its positive denominator. Since \`A-kB>0\`, it is positive for each \`1<=s<=k\`, so each mediant lies below theta. Conversely, upper updates have positive residual \`B-sA\`. Determinants remain one because adding a multiple of one neighbor to the other preserves \`cq-aj=1\`. Every inequality is affine in theta, and strict inequalities at both rational endpoints imply the stated inequalities throughout the intervening open interval. Thus the jump reproduces exactly the corresponding sequence of individual mediants. QED.

## Frozen-input finite result

With history \`m=128\`, horizon \`N=10^12+128\`, and exact open enclosure

\`262204504569236716045286/10^24 < theta < 262204504569236716045287/10^24\`,

the accelerated generator uses **28 certified quotient decisions**, versus **88** independent one-mediant tests. It constructs exactly the same **78 ordered Farey stages**, all of whose six integer fields match the independently saved R32 table. The first stage is \`(a,q,c,j)=(27,103,16,61)\`; six initial batches reach it, followed by 22 batches. Under R31's previously proved source-age conditions, the resulting stages yield **74 event-bearing stages** and **148 positive interval blocks** without enumerating individual events. Consequently R32's verified 298 affine-risk segments and trillion-step endpoint remain unchanged by replacing only its Farey-stage generator.

**Precision witness.** The full upper quotient near the final horizon is not uniform on the frozen enclosure: for \`(a,q,c,j)=(165937423910,632854970141,31385949441,119700267898)\`, the two endpoint upper quotients are \`4\` and \`1\`. Their shared first update is certified; it already reaches the requested truncated horizon. Requiring equality of full endpoint quotients would wrongly reject this valid finite computation.

## Independent validation

The included \`VERIFY_R33_PORTABLE.py\` uses only standard-library exact integer arithmetic, independently constructs both the jump and the single-mediant generator, and asserts equality of every Farey stage. On S23/AV it checks the 74/148 source-block counts. It also checks two non-S23 inputs:
- An enclosure of \`sqrt(2)-1\` with \`m=8,N=10000\`: 17 stage records, 12 quotient decisions versus 20 one-step tests.
- An enclosure near \`1/20001\` with \`m=8,N=20000\`: 19,992 stage records, **2 quotient decisions versus 19,998 one-step tests**.

A separate complete local checker \`VERIFY_R33.py\` also matched the original R32 78-row fixture and emitted a 35 KB source-labelled certificate (all batches and 148 blocks). The repository portable checker carries the essential self-contained reproducibility path; full local certificate is retained as a separate conversation artifact.

## Cost, limitations, next step

At endpoint precision \`P\` and horizon \`N\`, each quotient comparison/division has \`O(P+log N)\`-bit operands. With \`B\` certified batches and \`S\` emitted stages, algorithmic count is \`O(B+S)\` big-integer operations plus output; bit costs must include division/multiplication and interval construction. Fully certified Euclidean quotients group by continued-fraction partial quotients, giving logarithmically many direction-changing groups before denominators exceed \`N\`. A finite-width enclosure may force partial jumps, so \`B\` remains a measured quantity unless precision stability is established. No wall-clock speedup, general complete bit bound or native X6 theorem is asserted here.

Next portable unit: replace R32's 261 explicit prefix-risk updates by an exact rank/select or floor-sum arc-max query, preserving provenance and tie maxima; test other history lengths; complete independent review and event-scope handoff.
