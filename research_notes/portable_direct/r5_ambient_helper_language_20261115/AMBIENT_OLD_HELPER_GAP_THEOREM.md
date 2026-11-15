# R5 — an unbounded ambient-old-state repair gap in the mixed weighted suffix observer

Date: 2026-11-15. Parent scientific freeze: \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`.
Evidence: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.
Scope: the auxiliary radius-two indexed-center, mixed half-unit-weight optimizer **with two separately declared admissible suffix languages**. This is a model-internal theorem, not a native X6 embedding.
Provenance: previous R5 [mixed weighted optimizer classification](https://github.com/awdawmip/enterprise-math/commit/0683f51f871695db1bec29bef864df788c317d5f) and [hypercube domination reduction](https://github.com/awdawmip/enterprise-math/commit/35defb50c340afac5cf31fc8f4b3026b4bdb3fcd), both on Draft PR #2427.

## 1. Exact population and two-language operation

Use the original R5 event gaps \`(3,2,2,3,(2,1)^m)\`, center radius 2, budget \`m+3\`, and mixed penalty
\`g_mix(S)=1_{[0∈S OR (1_{2∈S} XOR 1_{8∈S})]}\` with objective \`J_t(S)+g_mix(S)/2\`. Put \`d=m-2\` (thus \`m=d+2\`).

The inherited old optimal seven-event cores are
\`O0=0125, O1=0135, O2=0235, O3=0245, O4=0246\`.
For the single closure a, the new cores are
\`1235,1245,1246\` with first suffix bit \`s=1\`, and
\`1345,1346\` with \`s=0\`.
For the double closure ab, add the core \`1236\` with \`s=1\`.

The remaining suffix \`v\` is an element of \`Q_d={0,1}^d\`.
Write an old optimizer as \`(Oj,s,u)\` and a new optimizer as \`(C,s',v)\`. The exact replacement distance inherited from the disjoint-center suffix decomposition is

\`rho((C,s',v),(Oj,s,u))=|C \ Oj| + 1_{s'≠s} + Hamming(v,u)\`.

This distance is directed new-to-old, with both center sets having the same cardinality.

Let **X** be the allowed old suffix language and **Y** the allowed new suffix language (nonempty subsets of \`Q_d\`). Old configurations range over all five \`Oj\`, both old first bits, and \`u∈X\`. New a/ab configurations range over the declared new core/first-bit pairs with \`v∈Y\`. Define
\`kappa_t(X,Y;2) = min{|L|: L subseteq Old(X), forall n in New_t(Y) exists o in L with rho(n,o)<=2}\`.

The comparison **keeps the new targets Y fixed and only changes which old repair resources remain available**; it is not an assertion that an absent old helper is invalid merely because it has no current new-target counterpart.

## 2. Unbounded exact gap theorem

For every integer \`d>=r>=3\`, let \`e_i=2^i∈Q_d\` be the indexed unit bit vectors and put

\`Y_r={e_0,...,e_(r-1)}\`,
\`X_restricted=Y_r\`, and \`X_ambient=Q_d\`.

Then, for the a and ab closures and radius-two repair libraries,

\`\`\`
kappa_a(X_restricted,Y_r;2) = 2r,
kappa_a(X_ambient,Y_r;2)    = r+2,
kappa_ab(X_restricted,Y_r;2)= 2r,
kappa_ab(X_ambient,Y_r;2)   = 2r.
\`\`\`

Consequently, deleting old suffix helpers solely because their suffix is absent from the new target language increases the minimum a-repair library by exactly \`r-2\`. This gap is unbounded as \`r\` grows. The cost ratio \`2r/(r+2)\` tends to 2.

### 2a. Core distance certificate

Columns in order \`O0,O1,O2,O3,O4\`:

| new core (first suffix bit) | O0 | O1 | O2 | O3 | O4 |
|---|---:|---:|---:|---:|---:|
| 1235 (1) | 1 | 1 | 1 | 2 | 3 |
| 1236 (1, ab only) | 2 | 2 | 2 | 3 | 2 |
| 1245 (1) | 1 | 2 | 2 | 1 | 2 |
| 1246 (1) | 2 | 3 | 3 | 2 | 1 |
| 1345 (0) | 2 | 1 | 2 | 2 | 3 |
| 1346 (0) | 3 | 2 | 3 | 3 | 2 |

These entries are exact set differences \`|C\Oj|\`, independently reproducible by the accompanying verifier.

### 2b. Forced baseline, valid for both old languages

For each \`e_i∈Y_r\`, the target \`(1346,0,e_i)\` can be repaired in radius two only by \`(O1,0,e_i)\` or \`(O4,0,e_i)\`. The core distance already uses the entire radius of two, so both suffix bit and full suffix must match. Hence any repairing library has at least **r pairwise distinct baseline entries**. Neither type of baseline entry can repair \`(1245,1,e_i)\`: its core distance is two and changing the first suffix bit costs one more.

### 2c. Restricted old language: lower bound 2r, matching upper bound

Distinct \`e_i,e_j\` have Hamming distance two. Every new core has core distance at least one from any old core. Thus an old entry at suffix \`e_j\` cannot repair any target at distinct suffix \`e_i\`, regardless of first suffix bit.

For each \`e_i\`, a baseline is necessary for target 1346 and a **second** old configuration is necessary for target 1245. Therefore \`kappa_a(X_restricted,Y_r;2)>=2r\`. The same bound holds for ab.

Take, for every \`e_i\`, the two old entries
\`(O1,0,e_i)\` and \`(O0,1,e_i)\`.
By the displayed matrix they repair all five a-target cores, and also the ab-only core 1236, at the same suffix. Hence both restricted minima equal \`2r\`.

### 2d. Ambient old language: a upper bound r+2

Retain the \`r\` old baseline entries \`(O1,0,e_i)\`, one per target, and add just two ambient helpers

\`H_0=(O0,1,0)\`, \`H_4=(O4,1,0)\`.

The helper suffix \`0\` is excluded from \`Y_r\` but belongs to the old ambient language \`Q_d\`. For each \`e_i\`, the five a-target cores are repaired as follows:

| target | helper | replacement distance |
|---|---|---:|
| (1235,1,e_i) | (O1,0,e_i) | 1+1=2 |
| (1245,1,e_i) | H_0 | 1+1=2 |
| (1246,1,e_i) | H_4 | 1+1=2 |
| (1345,0,e_i) | (O1,0,e_i) | 1 |
| (1346,0,e_i) | (O1,0,e_i) | 2 |

This produces an explicit radius-two library with \`r+2\` entries.

### 2e. Ambient old language: a lower bound r+2

Suppose there were a library with at most \`r+1\` entries. The forced baseline consumes \`r\` entries, leaving at most **one additional helper**. Because no baseline repairs \`(1245,1,e_i)\`, this same helper must repair every such target.

Its old first bit must be one: with first bit zero, even the smallest core distance one plus the first-bit mismatch one leaves no allowance to change suffix, so it can cover only one of the distinct \`e_i\`. With first bit one, its old core must be \`O0\` or \`O3\` (the only cores at distance one from 1245), and its suffix \`u\` must be at Hamming distance at most one from every \`e_i\`. As \`r>=3\`, the **unique** binary vector adjacent to all these distinct unit vectors is \`u=0\`. (Any other \`u\` is adjacent to at most two distinct unit vectors; this holds in all dimensions \`d>=r\`.)

So the only possible sole helper is \`(O0,1,0)\` or \`(O3,1,0)\`. It cannot repair any \`(1345,0,e_i)\`: its core distance is two, first-bit mismatch one and suffix distance one. Thus the \`r\` baselines must all be \`(O1,0,e_i)\`; an O4 baseline has core distance three from 1345. But none of those O1 baselines can repair \`(1246,1,e_i)\`, and the sole O0/O3 helper has core distance two plus suffix distance one from it. Contradiction. Therefore \`kappa_a(X_ambient,Y_r;2)>=r+2\`, completing its exact value.

### 2f. Double closure: exact 2r even with ambient helpers

In the ab case the target \`(1236,1,e_i)\` has core distance at least two from every old core. Every radius-two repair therefore must use old first bit one **and exactly suffix \`e_i\`**. These \`r\` required entries are disjoint from the \`r\` first-bit-zero baselines for 1346. Thus even the full ambient old language requires \`2r\` entries. The restricted construction of §2c attains it.

## 3. Falsifiable numerical consequences and interpretation

For \`r=d=3\`, a exact set-cover enumeration yields
\`kappa_a(Y,Y)=6\`, \`kappa_a(Q_3,Y)=5\`, and
\`kappa_ab(Y,Y)=kappa_ab(Q_3,Y)=6\`.
For \`r=d=8\`, the formulas give a-repair library sizes \`16\` versus \`10\`, a saving of six complete pre-stored old configurations.

This is a **typed observer-residual obstruction**: the new-target suffix language alone does not determine which old states may be safely removed before a declared future repair operation. The relevant retained datum is the old-helper admissibility language \`X\` and its relation to \`Y\`. The theorem proves loss for this one-step radius-two repair observer; it does not claim an unspecified infinite-horizon equivalence.

## 4. Verification and remaining questions

The accompanying \`VERIFY_AMBIENT_HELPERS.py\` checks the exact core-distance matrix, exhaustive minimum set-cover on the entire 3-bit universe with old languages \`Y\` and \`Q_3\`, validates explicit old libraries for every \`r=3,...,8\`, and checks forced 1346 certificates. All operations use exact integer set differences and bit-count Hamming distances. The all-\`r\` assertion above follows from the proof, not extrapolation from those finite checks.

Research continuation: classify the two-language general case \`(X,Y)\` with a graph-annotated residual kernel for radius-two repair; identify which ambient old helpers are operation-redundant under an exact observer/future-horizon certificate. Independently audit the inherited mixed optimizer classification before any status promotion.

Formal control: independent Draft PR source preservation under own historical R5 research provenance. No active formal Task-ID/CLAIM was asserted and no protected Activity/Result/Review write was performed.