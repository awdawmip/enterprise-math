# R762HS — Exact Walsh parity projector for Port-edge selections; sharp ten-source veto and Pasch separation

**Scope:** original six-axis **composite candidate** Port model of R762HR, on frozen P000 input \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Historical R762HR HR1 is reused, not modified. Independently authored portable mathematical work; review \`NOT_REVIEWED\`. No primitive \`TRIADIC_CLOSURE_E\` event, new CLAIM, or formal Result is asserted. Preserve ordered Port/Link/source information for any subsequent operation.

## HS1 — All-length exact degree-parity character formula

Let \`X={0,1,2,3,4,5}\` and \`V=binom(X,2)\`, the fifteen **named Ports**. An individually distinguished occurrence of three-axis support \`S={a,b,c}\` chooses exactly one of three undirected edges of the Port triangle \`T(S)\` on vertices \`ab,ac,bc\`. For a multiset of \`m\` source occurrences \`M=(S_1,...,S_m)\`, let \`E(M)\` be the number of edge choices (one per occurrence) for which every Port vertex has even degree. Connectivity is **not** imposed in \`E\`.

For \`x in {0,1}^V\`, put

\`F_S(x) = (-1)^(x_ab+x_ac)+(-1)^(x_ab+x_bc)+(-1)^(x_ac+x_bc)\`.

Then the following **integer identity holds for every nonnegative event count**:

\[
\boxed{E(M)=2^{-15}\sum_{x\in\{0,1\}^{15}}\prod_{t=1}^{m}F_{S_t}(x)}
\]

and each factor has exactly two values:

\[
F_S(x)=\begin{cases}
3,&x_{ab}=x_{ac}=x_{bc},\\
-1,&\text{otherwise}.
\end{cases}
\]

Fixing any one Port bit at zero halves the summation range and denominator:

\[
\boxed{E(M)=2^{-14}\sum_{x:x_{01}=0}\prod_t F_{S_t}(x).}
\]

**Proof.** For an edge \`e={P,Q}\`, define its degree-boundary \`∂e=e_P+e_Q\` in \`F_2^V\`. The finite Walsh identity \`1_{z=0}=2^{-15}\sum_x(-1)^{x·z}\` applied to the XOR of the selected edge boundaries yields the product of three local character sums. If all three Port bits agree the three terms equal \`+1\`; otherwise precisely one equals \`+1\` and two equal \`-1\`. A global flip \`x↦x+1_V\` does not affect any edge character, establishing the reduced formula. No cancellation of source multiplicity is performed: the character signs are a computational projector, while \`E(M)\` is a nonnegative **integer count** of individually distinguished BRC source choices. QED.

For fixed six-axis Ports the reduced formula evaluates in \`O(m·2^14)\` integer arithmetic operations with constant auxiliary space. With a 20-type support histogram, repeated factors can be preaggregated. Use arbitrary-precision integers for unbounded \`m\`.

**Port-realizability consequence.** By R762HR HR1, a closed Port realization exists iff an **even-degree and connected** choice exists. Hence \`E(M)=0\` is a rigorous rejection certificate; \`E(M)>0\` is only the degree-parity feasibility stage.

## HS2 — Complete ten-occurrence overlap-connected obstruction is Port-parity impossible

Exhaustively enumerate every unordered 10-occurrence multiset from the twenty named triple types, preserving separate identities when testing the six-axis half-degree/positive-source coefficient. Counts:

| Property of the 20-type unordered multiset | Exact count |
|---|---:|
| all multisets, \`binom(29,10)\` | 20,030,010 |
| all six coordinate occurrences even | 632,996 |
| eligible but zero sign-completion count | 29,360 |
| additionally connected under overlap of at least two axes | 240 |
| in that last class, \`E(M)>0\` | **0** |

The last row is new: **every one of those 240 overlap-connected, coordinate-even but unsignable 10-event multisets fails even the necessary Port-degree parity test**. This is a finite, exhaustive exact classification for \`m=10\`, upgrading R762HR's one explicit Port-obstruction witness to all 240. No claim for unbounded \`m\` follows.

The attached \`R762HS_CHECK.cpp\` loops over precisely \`binom(29,10)\` nondecreasing type index words; for coordinate-even cases it tests all \`binom(10,5)=252\` source subsets, then exact overlap connectivity and the HS1 integer character count for each of the 240 resulting bad connected instances. It asserts all reported counters and prints \`PASS R762HS\`.

## HS3 — An all-length Pasch family separates even-degree feasibility from connected Port realizability

Consider these four specific supports:

\[
A=012,\quad B=034,\quad C=135,\quad D=245.
\]

Every two distinct supports intersect in **exactly one native axis**; every one of the six native axes belongs to exactly two of the four supports. Give each support an **odd positive multiplicity** \`n_A,n_B,n_C,n_D\`. The original six-axis incidence totals are all even.

This entire family has **zero sign-balanced source completions**. Indeed, let \`z_i\` be the number of positive selections among occurrences of type \`i\`, and \`d_i=2z_i-n_i\`. Since the six axes correspond bijectively to the six unordered pairs of the four types, zero signed Cell displacement would require \`d_i+d_j=0\` for **every** distinct pair \`i,j\`. The triangle relations force \`d_i=0\` for all four types, impossible when all \`n_i\` are odd.

For a single Port triangle with \`n\` distinguished occurrences the number of choices with even Port degrees is

\[
e(n)=\frac{3^n+3(-1)^n}{4}
\]

(by HS1 on its three relevant Port bits). The four Pasch triangles have **pairwise disjoint Port-vertex sets**. Therefore their degree-parity choices are independent and

\[
\boxed{E(M)=\prod_{i\in\{A,B,C,D\}}\frac{3^{n_i}-3}{4}}
\quad\text{for odd }n_i.
\]

For every odd \`n_i>=3\`, this count is strictly positive, but **no choice can be connected**: the selected edges lie in four separate nonempty Port-vertex components. Thus the HR1 connectivity condition is indispensable, even when all six axis degrees are even and the degree-parity count is positive. This is an infinite exact family, not a numerical extrapolation.

Two integer examples:
- \`(n_A,n_B,n_C,n_D)=(3,3,3,3)\`: \`m=12\`, \`E=6^4=1,296\`.
- \`(5,3,3,3)\`: \`m=14\`, \`E=60·6^3=12,960\`.

Both were recomputed by the independent full fifteen-Port HS1 projector; they are **support multisets, not legal closed Port histories**. Hence they do not contradict R762HM's theorem covering genuine Port closed histories of length at most 12.

## Verification scope and outstanding mother question

Local execution: \`g++ -std=c++17 -O3 -Wall -Wextra -pedantic R762HS_CHECK.cpp -o hs && ./hs\` returned \`PASS R762HS\`, with the exact counters above. Arithmetic in this fixed \`m<=14\` checker is integer, and the 15-Port character projector uses 64-bit signed products; arbitrary lengths require wider integers. The finite scan is exhaustive only over the stated \`m=10\` support-multiset population; the Pasch proof is valid at every declared odd multiplicity.

**Next:** Extend the source-preserving Port-Euler filter beyond ten events, or derive an all-length constructive signing of coordinate-even *genuine* closed Port histories. In particular find an actual HR1-connected, coordinate-even and unsignable source multiset, or retain the question as open. Continue the separate P000 native signed triadic force/Cell/Link/Port/time/rotation dynamics. R762HR/R762HQ and other authorship/CLAIM/RA bindings remain unchanged.
