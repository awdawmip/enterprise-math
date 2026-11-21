# X6 R82 — Degree-four weighted BRC: six-candidate sufficiency on Ports 23–38 and the sharp 27-Port exchange

Date: 2026-11-21 (Asia/Shanghai)
Status: FINITE_EXHAUSTIVE_EXACT_INTEGER_CERTIFICATE + SYMBOLIC_EXCEPTION_LEMMA / AUTHOR_CHECKED / NOT_INDEPENDENTLY_REVIEWED.
Frozen science: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`.
Prior science: R80/R81; this result is independently exhaustive over the stated finite integer domains and **does not invoke** R72's 28-candidate atlas.

## Observer and exact statement

In the *conditional* positive-count degree-four BRC star-histogram observer, with unknown common additive offset, define for nonzero integer \`a=(a2,a3,a4)\`:

\`\`\`text
q(a)=max(sum(max(a_d,0)), sum(max(-a_d,0))),
z=(0, 2a2+6a3+12a4, 6a2+24a3+60a4, 14a2+78a3+252a4),
g_ij(a)=|z_i-z_j|/2, i<j,
F(a;w)=max_{i<j} g_ij(a)/(w_i+w_j), w=(A,B,C,D)>0,
eta*(p,w)=min{F(a;w):a!=0, q(a)<=p}.
\`\`\`

Let

\`\`\`text
S_22 = {(3,-4,1),(6,-4,1),(9,-5,1),(10,-5,1),(15,-6,1),(21,-7,1)}
S_27 = {(3,-4,1),(6,-4,1),(9,-5,1),(10,-5,1),(15,-6,1),(24,-14,3)}.
\`\`\`

**Theorem.** For all \`w in R_{>0}^4\`,

\`\`\`text
eta*(p,w)=min_{s in S_22} F(s;w), 23<=p<=26,
eta*(p,w)=min_{s in S_27} F(s;w), 27<=p<=38.
\`\`\`

Every vector in each displayed six-member core is indispensable **within that chosen core**: it wins strictly against the other five at an explicit positive integer weight. This statement does not assert global uniqueness or global minimum cardinality among *arbitrary alternative* sufficient families; full-domain ties can occur.

There is a strict Port-27 transition at \`w=(163,165,1809,388)\`:

\`\`\`text
eta*(26,w)=1/328, eta*(27,w)=3/986,
eta*(26,w)-eta*(27,w)=1/161704 > 0.
\`\`\`

## Exact finite exhaustion

Because \`q(a)<=p\` implies \`|a_d|<=p\`, all feasible differences lie in the cube \`[-p,p]^3\`. The six pair gaps are unchanged by \`a -> -a\`; enumerate only the representative whose first nonzero coordinate is positive. At \`p=26\`, the complete representative domain has **31,031** elements (62,062 signed); **every** six-gap vector is componentwise no smaller than that of a member of \`S_22\`. Deterministic first-witness allocation in the displayed order is \`[29463,1385,43,131,2,7]\`.

At \`p=38\`, the complete representative domain has **95,133** elements (190,266 signed). Every vector except exactly \`b=(21,-7,1)\` is componentwise dominated by a member of \`S_27\`. The first-witness counts are \`[91611,3140,97,266,3,15]\` and sum to 95,132. This is a complete finite-domain claim, with executable verifier and no floating tolerance.

Because \`S_22\` already fits within 22 Ports, the p=26 domination proves sufficiency throughout 23–26. Similarly \`S_27\` fits within 27 Ports, and the p=38 domination plus the following lemma covers 27–38. The order of quantifiers is: for every real positive weight, for every Port p in its stated interval, the corresponding exact minimum is given.

## Symbolic exception lemma

Write \`R=F(b;w)\`, \`U=F((24,-14,3);w)\`, \`V=F((10,-5,1);w)\`. The respective gap vectors (12,13,14,23,24,34) are:

\`\`\`text
b: (6,9,0,3,6,9)
U: (0,6,0,6,0,6)
V: (1,0,1,1,0,1).
\`\`\`

Thus

\`\`\`text
R = max(6/(A+B),9/(A+C),3/(B+C),6/(B+D),9/(C+D))
U = max(6/(A+C),6/(B+C),6/(C+D))
V = max(1/(A+B),1/(A+D),1/(B+C),1/(C+D)).
\`\`\`

**Lemma: \`min(U,V)<=R\` for every \`A,B,C,D>0\`.** If \`U<=R\`, done. Otherwise, as \`R>=9/(A+C),9/(C+D)\`, the only term in U that can exceed R is \`6/(B+C)\`; hence \`6/(B+C)>R>=6/(A+B)\`, implying \`C<A\`. All terms of V other than \`1/(A+D)\` are strictly below R by its displayed lower bounds. Were \`V>R\`, then \`1/(A+D)>R>=9/(A+C)\`, forcing \`A+C>9(A+D)\`, or \`C>8A+9D>A\`, a contradiction. Therefore \`V<=R\`, as required. This accounts for the *single* undominated integer vector and completes the universal weight proof.

## Six-member internal indispensability certificates

For the first five vectors in both core lists, choose respectively:

\`\`\`text
(18,12,1,1):       (3,-4,1)   eta=9/19, runner-up within core=1/2
(1,1,1,24):        (6,-4,1)   eta=12/25, runner-up=1/2
(1,1,6,12):        (9,-5,1)   eta=6/13, runner-up=1/2
(1,1,1,1):         (10,-5,1)  eta=1/2, runner-up=3
(1447,167,166,1850): (15,-6,1) eta=1/336, runner-up=1/333.
\`\`\`

For the sixth member, respectively:

\`\`\`text
(1,179,153,15):  (21,-7,1)  eta=9/154, runner-up=1/16 (S_22)
(163,165,1809,388): (24,-14,3) eta=3/986, runner-up=1/328 (S_27).
\`\`\`

These are exact pairwise rational comparisons among the six listed directions. A signed vector elsewhere in the full feasible cube may tie a core direction; no unsupported global strict-uniqueness claim is inferred.

## Verification and boundaries

- A standalone built-in Node.js BigInt verifier enumerates the integer domains, recomputes the six gaps, certifies componentwise domination, the unique p=38 exception, the six positive-integer weight witnesses in each core, and the exact p26→27 jump.
- Independent local Python \`Fraction\` enumeration reproduced domain populations, exception lists and the jump; this is an author-side crosscheck, not an independent peer review.
- Original P000 is frozen. This result is scoped to the stated BRC positive-count *observer*, not an established faithful projection of native six-axis Cell/Link/Port, whole triadic force events, branch identities, time trajectories or future update operations.

## Next mathematical question

Classify p=39–124. Initial exact search identifies \`(36,-16,3)\` as a new gap-undominated direction at q=39 and \`(39,-20,4)\` at q=43; determine the **minimal** full-domain weight-sufficient family, including multi-vector envelope inequalities, rather than confusing coordinatewise Pareto minimality with true weighted optimality. Independently investigate the source-faithful mapping from named native X6 events to this observer.
