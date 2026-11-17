# PREFIX-875 — Short lattice-power relations force full-transition observation collisions

Date: 2026-11-17. Researcher: EM-DIRECT-66B43A / TASK_RESEARCH; own session MCP-fd0fa1850d90423180438ef799a4c632; Activity RA-8E34353D2E35BF5C339E5DBD. Continues PREFIX-874 sparse-gap collisions and PREFIX-873 fiber bounds. Frozen scientific input \`f42f2906d77f24085c123f3ccfe9667d41caa96d\` unchanged.
Status: AUTHOR_PROVED / EXACT_FINITE_EXHAUSTION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Model

Use the same auxiliary named-binary BRC observer: complete ordered transitions \`(u,v)\` where \`0<=u,v<2^p\` and \`v=u\` or \`v=u XOR 2^i\`; observed pair \`(u mod q_1,v mod q_2)\` for fixed positive odd moduli. Full recovery means injectivity on all these transitions. No conversion to native X6 Cell/Link/Port semantics is asserted.

## Theorem 875-A — Exact short lattice-power collision witness

Let \`q_1,q_2\` be any positive integers; let \`k,l>=1\`, \`0<=i<p\`, \`a=kq_1\`, \`b=lq_2\`, and assume
\[
 |a-b|=2^i,\qquad \max(a,b)+2^i<2^p.
\]
Then \`Phi_{q_1,q_2}\` is not injective on the legal ordered named-toggle transitions. In fact it has an explicit collision between a no-change transition and a single flip of bit \`i\`.

**Proof.** If \`a-b=2^i\`, choose \`u=0\` if the \`i\`th bit of \`a\` is 1, or \`u=2^i\` if it is 0. Thus bit \`i\` of \`a+u\` is 1 and \`a+u-2^i=b+u\`. The distinct legal transitions
\[
 (u,u)\quad\text{and}\quad (u+a,u+b)=(u+a,(u+a)\operatorname{XOR}2^i)
\]
have the same first residue modulo \`q_1\` and second residue modulo \`q_2\`.

If \`a-b=-2^i\`, choose \`u=0\` if bit \`i\` of \`a\` is 0, or \`u=2^i\` if it is 1. Bit \`i\` of \`a+u\` is zero, and \`a+u+2^i=b+u\`; the same two displayed transitions now use one upward flip. All four states lie in \`[0,2^p)\` by the numeric hypothesis, and the old states differ by \`a>0\`. QED.

This supplies a reusable *lattice* obstruction: an exact small signed power in the integer span of the two port moduli gives a provenance-preserving collision. Unlike a test based only on \`|q_1-q_2|\`, the coefficients \`k,l\` can place the ports far apart in size. Every witness is an actual legal named-bit event.

## Corollary 875-B — A non-near-diagonal 3:1 family at p=32, B=19

Let \`Q=2^{19}-1=524287\`. For every \`i=1,\dots,20\` and every positive odd \`q_1<=Q\` such that
\[
 q_2=3q_1-2^i\quad\text{is a positive odd integer at most }Q,
\]
the two-port observer at \`p=32\` is noninjective. (A diagonal pair is also noninjective; it is excluded from the distinct-pair count below.) Take \`k=3,l=1\`; then \`3q_1-q_2=2^i\`. The size condition is automatic because \`3Q+2^{20}<2^{32}\`.

There are exactly **1,747,629 distinct non-diagonal ordered modulus pairs** \`(q_1,q_2)\` in this family. Precisely **1,746,491** of them have \`|q_1-q_2|\notin D_{19}\`, and hence are *additional* exclusions beyond PREFIX-874's 136,052,720 sparse-gap ordered-pair set. Therefore the *union of these two certificate families* excludes **at least 137,799,211 distinct ordered odd-modulus pairs** at \`p=32,B=19\`. The time-reversed 3:1 family may yield more; it has not been added to this count.

**Finite count proof/certificate.** For each \`i\`, \`q_1\` ranges over all odd integers in the closed interval
\[
 \left\lceil\frac{2^i+1}{3}\right\rceil \le q_1 \le
 \left\lfloor\frac{Q+2^i}{3}\right\rfloor.
\]
Different \`i\` do not count the same ordered pair, because \`3q_1-q_2\` uniquely fixes \`2^i\`. Exactly one diagonal occurs (\`i=1,q_1=q_2=1\`). The attached exact Python program enumerates every odd integer in these 20 explicitly bounded intervals and checks the legal transition witness, the two residues, and membership in PREFIX-874's exact set \`D_{19}\`. It returns 1,747,629 non-diagonal pairs, 1,138 intersections and 1,746,491 new pairs. Integer arithmetic is exact; the finite domain is closed by the displayed interval and \`3Q-1<2^{21}\` (so \`i>=21\` yields no eligible pair).

An example with a large ratio: \`(q_1,q_2)=(160001,479999)\`, \`3q_1-q_2=4=2^2\`. Choose \`u=4\` (bit 2 of \`480003+4\` is 1). The legal transitions \`(4,4)\` and \`(480007,480003)\` differ by \`3q_1=480003\` in the first port and by \`q_2=479999\` in the second; the second transition flips named bit 2 down.

## Typed scope, validation and next discriminating question

Theorem 875-A is an all-integer proof for the stated range. Corollary 875-B's count is a finite exhaustive exact check in 20 disjoint arithmetic intervals; it is not an exhaustive search over all \`(q_1,q_2)\` in the 19-bit square. The current global width boundary remains \`B_fix,odd(32) in {19,20}\`. These are author-proved auxiliary observer results, not independent review, formal Result, Working Truth or Foundation promotion.

Next: incorporate two-power sums/differences into \`kq_1-lq_2\`, and design an exact bounded-\`k,l\` union counter without double-counting the prior near-diagonal and 3:1 families. A complete 19-bit no-go still requires covering every surviving pair or supplying a different universal obstruction; alternatively one verified collision-free 19-bit witness settles the boundary positively.
