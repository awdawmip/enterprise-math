# X6 R104 — Universal thirteen-class bound, robust 3/2-gap, and finite reduction for arbitrary positive four-channel BRC weights

Date: 2026-11-22 (Asia/Shanghai).
Scientific status: AUTHOR_SYMBOLIC_PROOF / AUTHOR_EXACT_INTEGER_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
Input is frozen at \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`. Current P000 V5, ACTIVE Heartbeat World, joint-relation observer preservation and portable research contracts were read separately. This theorem concerns the conditional auxiliary positive-count four-channel star-moment observer, not a native X6 physical dynamics assertion.
Predecessors: R98–R102 for \`(1,1,S,T)\`; R103 for \`(T,1,1,1)\`.

## Model and exact problem

Let \`a=(x,y,z)\` be a nonzero integer difference, identified with \`-a\`, and define

\[
q(a)=\max\{\sum_i \max(a_i,0),\sum_i\max(-a_i,0)\}
       ={ \|a\|_1+|x+y+z|\over2}.
\]
\[
u=x+3y+6z,\quad v=3x+12y+30z,\quad h=7x+39y+126z.
\]

For **arbitrary real** positive weights \`w=(A,B,C,D)\in(0,\infty)^4\`, define the exact six-pair star-gap norm
\[
F_w(a)=\max\left\{\frac{|u|}{A+B},\frac{|v|}{A+C},
\frac{|h|}{A+D},\frac{|v-u|}{B+C},
\frac{|h-u|}{B+D},\frac{|h-v|}{C+D}\right\}.
\]
The 3-by-3 moment matrix has determinant 36, so \`F_w\` is a genuine norm on real triples. Let \`p\ge11\` be integral and
\[
\eta_p(w)=\min\{F_w(a):a\in\mathbb Z^3\setminus\{0\},\ q(a)\le p\}>0.
\]
All statements retain the explicit finite Port bound. No claim of P000 observer-fiber preservation is made.

## Theorem 1 — Thirteen classes and the sharp 3/2 *threshold of this proof*

For every positive real weight quadruple \`w\` and every integer \`p\ge11\`:

1. The complete set of \`F_w\`-minimizing **unoriented** integer directions has cardinality at most **13**.
2. More strongly, the set
\[
N_p(w)=\{\,\{\pm a\}:q(a)\le p,\quad F_w(a)<3\eta_p(w)/2\,\}
\]
has at most **13** members. Hence the 14th distinct feasible unoriented direction, ordered by \`F_w\`, has value **at least \`3\eta_p(w)/2\`**.
3. For two distinct members \`{\pm a},{\pm b}\` of \`N_p(w)\`, the unordered nonzero residue pairs \`{\pm(a\bmod3)}\`, \`{\pm(b\bmod3)}\` are different. Thus the 13 sign-orbits of the 26 nonzero elements of \`(\mathbb Z/3\mathbb Z)^3\` provide an injective index for every near-optimal direction.

**Proof.** The Port cost \`q\` and observer score \`F_w\` are even, positively homogeneous, and subadditive. Let \`a\` be feasible with \`F_w(a)<3\eta_p/2\`. If \`a\equiv0\pmod3\`, then \`a/3\` is a nonzero feasible integer vector because \`q(a/3)=q(a)/3\le p\`, but \`F_w(a/3)<\eta_p/2<\eta_p\`, contradiction. Hence its residue is nonzero.

Suppose two distinct unoriented near-optimal directions have the same residue sign-orbit. Choose signs so \`a\equiv b\pmod3\`; then \`c=(a-b)/3\` is a nonzero integer vector. Convexity gives
\[
q(c)\le{q(a)+q(b)\over3}\le{2p\over3}\le p,\qquad
F_w(c)\le{F_w(a)+F_w(b)\over3}<\eta_p,
\]
again a contradiction. Exactly 26 nonzero residue classes exist, grouped into 13 sign-orbits because 3 is odd. This proves injectivity, the bound and the 14th-value statement. \`F_w(a)=\eta_p<3\eta_p/2\` gives the minimizer corollary. QED.

The constant 13 is best possible among *arbitrary* three-dimensional norms with this same Port cost: for the unrelated comparison norm \`\|a\|_\infty\`, all 13 unoriented nonzero vectors in \`\{-1,0,1\}^3\` have minimum value 1 and Port cost at most 3. Whether 13 is attained **within the present six-pair BRC norm family** remains open. The strict inequality at \`3/2\` is essential to the residue proof.

## Theorem 2 — Effective finite exact carrier at every fixed weight

Write \`s=(10,-5,1)\`, with \`(u,v,h)(s)=(1,0,1)\`, \`q(s)=11\`. Its exact score is
\[
E_s(w)=\max\left\{\frac1{A+B},\frac1{A+D},\frac1{B+C},\frac1{C+D}\right\}.
\]
Set
\[
U=\lfloor(A+B)E_s\rfloor,\quad
V=\lfloor(A+C)E_s\rfloor,\quad
H=\lfloor(A+D)E_s\rfloor.
\]
Define \`K(w)\` as the set of nonzero integer vectors with moments satisfying
\[
|u|\le U,\quad |v|\le V,\quad |h|\le H,
\quad v\equiv0\pmod3,\quad h-u\equiv0\pmod6,
\quad h-u-6v\equiv0\pmod{12}.
\]
Recover each vector using the **exact** inverse
\[
x=(h+19u)/2-4v,\quad
y=(-h-14u+7v)/3,\quad
z=(h+11u)/12-v/2.
\]
The three congruences are necessary and sufficient for integrality; this defines a finite, fully enumerable carrier without cutting off the original Port domain.

Then for every \`p\ge11\`, the exact minimizers are obtained by minimizing \`F_w\` over \`K(w)\cap\{q\le p\}\`. Indeed \`s\` is feasible, so \`\eta_p\le E_s\`; each minimizing \`a\` obeys the three displayed moment bounds from the first three observer terms, and the inverse identifies exactly those integral vectors. Conversely every candidate is an original feasible difference once filtered by Port.

For a **fixed weight** define \`P_*(w)=\max_{a\in K(w)}q(a)\`. Since \`K(w)\` is finite and includes \`s\`, both the optimal value and **the complete minimizing-direction set are constant for all \`p\ge P_*(w)\`**. A computable Port upper bound is
\[
P_*(w)\le
\left\lfloor\frac{125U+54V+7H}{12}\right\rfloor.
\]
To verify this bound, the inverse gives
\[
|x|+|y|+|z|\le(181U+82V+11H)/12,\quad
|x+y+z|\le(69U+26V+3H)/12.
\]
Use \`q=(\|a\|_1+|x+y+z|)/2\` and integrality. Thus even without a universal finite direction core across all positive weights, the complete optimum at any fixed weight has a closed finite arithmetic decision procedure with an explicit weight-dependent stabilization bound. QED.

## New exact near-optimal witness (12 of 13 possible classes)

At \`w=(9,1,59,41)\`, \`p=40\`, direct integer analysis gives \`\eta_{40}=1/10\`: if \`u\ne0\`, the first pair costs at least \`1/10\`; if \`u=0,h\ne0\`, \`h\in6\mathbb Z\` forces \`|h|/(B+D)\ge6/42>1/10\`; if \`u=h=0,v\ne0\`, the integrality congruence forces \`v\in6\mathbb Z\`, so \`|v|/(B+C)\ge6/60=1/10\`. Both \`s\` and \`c=(24,-14,3)\` attain \`1/10\`.

A finite, exact congruence enumeration shows **12** distinct unoriented directions with \`q\le40\` and \`F_w(a)<3/20\`. Indeed these must satisfy \`|u|\le1,|v|\le10,|h|\le7\`; enumerate only the integer moment triples in that box satisfying the three congruences and inverse formulas. The twelve directions (canonical sign) are
\[
\begin{gathered}
(1,0,0),(5,-4,1),(9,-5,1),(10,-5,1),\\
(14,-9,2),(15,-9,2),(19,-10,2),(23,-14,3),\\
(24,-14,3),(25,-14,3),(29,-18,4),(34,-19,4).
\end{gathered}
\]
Of these, three have score \`1/10\` (the vectors with first coordinate 10,14,24), eight have score \`1/7\`, and \`(34,-19,4)\` has score \`7/60\`. The missing residue sign-orbit is \`{\pm(0,1,2)}\`. The lowest-scoring vector in that orbit within Port 40 is \`(33,-19,4)\`, with score exactly \`3/20\`, confirming why the strict threshold excludes it.

This establishes an **attainable lower bound 12 and a proved upper bound 13** for maximum near-optimal multiplicity in the full positive four-weight observer family. It does **not** assert 12 or 13 as the exact global maximum.

## Author-side calculation and verification scope

The accompanying Python standard-library checker enumerates **110,740 unoriented nonzero triples with \`q\le40\`**; reconstructs each weight's entire congruence-bounded moment carrier; evaluates all six pairs using exact integer cross multiplication; and compares complete optimizing sets for **13 positive integer weight quadruples × 6 Port budgets (78 exact cases)**. It also checks distinct mod-3 sign-orbits for the strict \`3/2\` sublevel and the 12-direction witness. All assertions passed. Those 78 cases verify that sampled finite domains match the symbolic statements; they are not an independent global review.

## Status, provenance, and next questions

Dependencies: R103's exact moment representation, frozen P000; no assumption of native signed/phase or path/time fiber constancy. Theorems 1–2 are author-written infinite-domain proofs for the conditional score and integer Port lattice; the 12-direction witness is finite exact enumeration. No formal Source CLAIM, Result, Review, or Foundation promotion is implied.

Next: decide whether the upper bound **13** is attainable for the actual six-pair BRC family, or prove a sharper maximum; classify the full four-weight parameter chambers under the finite carrier; separately build a typed future-operation-safe bridge to native named Cell/Link, triadic forces, branch provenance and heartbeat time.
