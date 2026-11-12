# R5 follow-on — Three globally valid, shortest moving first-zero words

Date: 2026-11-12 Asia/Shanghai; same frozen 28-coordinate P/Q–BRC auxiliary fixture and input pins as sibling \`RESEARCH.md\`.

## Theorem

Let \`x=X[(target1,source3)]\`, \`H[(target1,source3)]=-23\`, \`U=1/23\`, \`E=9/115400000\`. For \`q in {15,12,3}\` define

\[
 \rho_q=\frac{1-qE/x}{23},\qquad
 u_q(r)=\frac{x(1-23r)}q.
\]

For **every real** \`r in [rho_q,U)\`, the following *same ordered word* is legal at \`eps=u_q(r)\` in **all 28 nonnegative mass coordinates**, and its final state has zero mass in coordinate \`k1=(target1,source3)\`:

| q | Uniform ordered word (1-based atom labels) | Minimum number of operations |
|---:|---|---:|
| 15 | (6,1) | 2 |
| 12 | (1) | 1 |
| 3 | (6) | 1 |

This covers the full corresponding moving-family active interval \`rho_q<r<U\`, including all 3,432 fixed/moving collision pairs. The \`r=rho_q\` endpoint supplies an exact ray-endpoint witness; \`r=U\` supplies a nonnegative zero-\`eps\` limit for convex interpolation.

### Proof

For any fixed prefix \`A\` of one of the three words, define its state at moving time as

\[
 F_A(r)=X+x rH+\frac{x(1-23r)}{36q}P_A.
\]

This is affine in \`r\`. At \`r=U=1/23\` its operation coefficient vanishes, so \`F_A(U)=X(U)\ge0\`, using the already verified maximum admissible hidden-state interval. At \`r=rho_q\`, \`u_q(rho_q)=E\`; exact 28-coordinate substitution confirms \`F_A(rho_q)\ge0\` at **every** prefix, including the empty prefix. Any \`r\` between these endpoints gives a convex combination of the two endpoint vectors, hence every intermediate state is nonnegative.

The three final words have integer \`k1\` changes \`P_A[k1]=-36q\`; therefore

\[
 F_{A,k1}(r)=x(1-23r)+\frac{x(1-23r)}{36q}(-36q)=0
\]

throughout the interval. Their lengths are optimal for obtaining this coordinate zero: q=12 and q=3 have singleton negative changes, while q=15 requires both negative-change atoms 1 and 6; no single atom has \`P[k1]=-540\`.

### Exact endpoint margins

At the activation gate, the complete word has only the intended zero coordinate \`k1\` and strictly positive mass in the other 27 coordinates. The smallest strictly positive mass is always attained at \`k0=(target0,source3)\`:

| q | Minimum positive mass at gate after complete word |
|---:|---|
| 15 | 13289444035517 / 14507005871120000000 |
| 12 | 10649520956717 / 14507005871120000000 |
| 3 | 2729751720317 / 14507005871120000000 |

At \`r=U\`, every prefix is \`X(U)\` and has precisely \`k1\` as its zero coordinate. These assertions use exact integer fractions and can be rechecked with sibling \`VERIFY_THREE_MOVING_UNIFORMS.py\`.

## Consequence for the full event-sweep certificate

A complete *witness-aware sorted first-zero event stream* may attach (i) the preexisting **1,144** globally valid fixed-threshold ordered witnesses, and (ii) the **three** globally valid moving-threshold words above. The 3,432 crossings then change the order of two labeled capacity entries, with their independently valid witnesses already attached. No fresh 28-coordinate path search is needed at each crossing after the source lemmas and 1,147 words have been verified.

The sibling exact dual-zero census gives further information about whether **one and the same prefix** witnesses *both* crossing coordinates; 1,065 pairs permit that and 2,367 do not. That stronger dual-zero property is not required to maintain one valid witness per capacity entry.

The statement is a theorem inside the frozen 28-coordinate external auxiliary model, without upgrading its status to native X6 or formal Source acceptance. Future work: construct a compact verifiable data structure pairing the three moving words with rank events and the 1,144 fixed witnesses, and test independent replay from the pinned original source bytes.
