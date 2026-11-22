# X6 R101 — Exact strict-sub-half tie walls and satellite tie corridors

Date: 2026-11-22 (Asia/Shanghai).
Status: AUTHOR_SYMBOLIC_PROOF_DEPENDENT_ON_R98_R99 / EXACT_RATIONAL_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
Frozen science: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`.
Model scope: the **conditional positive-count, four-channel BRC star-moment histogram observer** of R98/R99, with a common unknown offset. Auxiliary integer differences are not declared native six-axis Cell/Link/force/time states.

## Model and exact input

For unoriented nonzero \`a=(x,y,z) in Z^3\`, \`q(a)=max(sum(max(a_i,0)),sum(max(-a_i,0)))\`; write \`u=x+3y+6z\`, \`v=3x+12y+30z\`, \`h=7x+39y+126z\`. For \`S,T>=1\` real,

\[
F(a;S,T)=\max\left\{\frac{|u|}{2},\frac{|v|}{S+1},\frac{|h|}{T+1},\frac{|v-u|}{S+1},\frac{|h-u|}{T+1},\frac{|h-v|}{S+T}\right\}.
\]

Let \(\eta_p(S,T)=\min_{a\ne0,q(a)\le p}F(a;S,T)\), with integer \(p\ge11\), and let \(M_p\) be the complete unoriented minimizer set. In this note **assume \(\eta_p(S,T)<1/2\)**. R98 supplies the exact value and R99 proves the universal complete ten-direction tie carrier.

Define the following four specific directions, with exact Port budgets and scores:

| symbol | direction | q | F |
|---|---|---:|---|
| d | (6,-4,1) | 7 | 12/(T+1) |
| b | (9,-5,1) | 10 | max(3/(S+1),6/(T+1)) |
| e | (15,-9,2) | 17 | max(3/(S+1),6/(T+1),9/(S+T)) |
| c | (24,-14,3) | 27 | 6/(S+1) |

Put \(X=S+1\ge2\), \(Y=T+1\ge2\), \(Z=S+T=X+Y-2\), \(\alpha=3/X\), \(\beta=6/Y\), and \(\rho=\beta/\alpha=2X/Y\).

## Theorem 1 — Full strict-sub-half optimizer classifier

For all real \(S,T\ge1\), all integer \(p\ge11\), subject to \(\eta_p(S,T)<1/2\), the following decision rules give **exactly** \(M_p(S,T)\). Each named direction is unoriented (the negative is identified).

**For \(11\le p\le16\):**

- \(\rho<1/2\): \(\{d\}\).
- \(\rho=1/2\): \(\{d,b\}\).
- \(\rho>1/2\): \(\{b\}\).

**For \(17\le p\le26\):** use the preceding three cases, and also include \`e\` if and only if \`b\` is selected and
\[
\frac9Z\le\max(\alpha,\beta).
\]
Equivalently, the satellite \`e\` enters exactly when **either**
\[
Y\ge 2X+2\quad\text{or}\quad Y\le2X-4.
\]
In particular, at \(\rho=1/2\) the complete tie is \(\{d,b,e\}\).

**For \(p\ge27\):**

- \(\rho<1/2\): \(\{d\}\).
- \(\rho=1/2\): \(\{d,b,e\}\).
- \(1/2<\rho<2\): \(\{b\}\), plus \`e\` exactly on the two satellite regions \(Y\ge2X+2\) or \(Y\le2X-4\).
- \(\rho=2\): \(\{b,e,c\}\).
- \(\rho>2\): \(\{c\}\).

All inequalities here are on ordinary positive real numbers, and the strict-sub-half hypothesis remains operative in every case. There is no Port dependence after \(p=27\).

## Theorem 2 — Sharp maximum multiplicity strictly below one half

\[
\boxed{\max_{\substack{S,T\ge1\\ \eta_p(S,T)<1/2}}\lvert M_p(S,T)\rvert
=\begin{cases}2,&11\le p\le16,\\3,&p\ge17.\end{cases}}
\]

All maximizing parameter loci are:

- \(11\le p\le16\): exactly \(S>5,\ T=4S+3\), with \(\{d,b\}\).
- \(17\le p\le26\): exactly \(S>5,\ T=4S+3\), with \(\{d,b,e\}\).
- \(p\ge27\): exactly the union of \(S>5,\ T=4S+3\), giving \(\{d,b,e\}\), **and** \(S=T>11\), giving \(\{b,e,c\}\).

Thus there are two different unbounded triple-tie rays in the strict-improvement region. The first appears as soon as Port 17 is allowed; the second requires Port 27. The universal maximum of seven from R100 occurs on the separate boundary \(\eta=1/2\).

## Proof

By the R99 universal ten-direction theorem, every optimizer belongs to its ten-direction carrier. Six candidates have \(|u|=1\) and therefore cost at least \(1/2\). Under the strict-sub-half hypothesis, the optimizer must therefore lie among the four \(|u|=0\) members \(\{d,b,e,c\}\). Their exact scores are the ones in the table; \`e\` has score \(\max(F(b),9/Z)\ge F(b)\), so it never improves the optimal **value**.

With the Port constraints incorporated, the exact minimum below one half is
\[
\min(2\beta,\max(\alpha,\beta)) \quad(11\le p\le26),
\]
or
\[
\min(2\beta,\max(\alpha,\beta),2\alpha)\quad(p\ge27).
\]
For the first minimum, comparison gives a \`d\` winner when \(\beta/\alpha<1/2\), a tie with \`b\` at equality, and a \`b\` winner above. For the second minimum, the \`b\` regime ends at \(\beta/\alpha=2\); at equality \`c\` joins, and above it \`c\` alone wins.

When \`b\` is optimal and \(p\ge17\), \`e\` joins precisely if \(9/Z\le F(b)=\max(\alpha,\beta)\). If \(\alpha\ge\beta\), equivalently \(Y\ge2X\), this inequality reduces to \(9X\le3(X+Y-2)\), i.e. \(Y\ge2X+2\). If \(\beta\ge\alpha\), equivalently \(Y\le2X\), it reduces to \(9Y\le6(X+Y-2)\), i.e. \(Y\le2X-4\). This proves every satellite entry and exclusion.

At \(\rho=1/2\), \(Y=4X\), hence \(\alpha=\min(2\beta,\max(\alpha,\beta))\). The strict-sub-half condition is \(\alpha=3/X<1/2\), i.e. \(X>6\) or \(S>5\). Moreover \(9/(5X-2)\le3/X\) for \(X\ge2\); thus \`e\` necessarily joins if \(p\ge17\).

At \(\rho=2\), \(Y=X\), and (when \(p\ge27\)) the tied value is \(2\alpha=6/X<1/2\) exactly when \(X>12\) or \(S=T>11\). The satellite inequality \(9/(2X-2)\le6/X\) holds when \(X\ge4\), hence \`e\` also joins. A triple tie requires \`e\` and two among \`d,b,c\`; the only possible equalities at a global minimum are \(d=b\) at \(\rho=1/2\), or \(b=c\) at \(\rho=2\). Equality \(d=c\) occurs at \(\rho=1\), where \(b\) is strictly cheaper. This exhausts both maximum-cardinality loci. QED.

## Exact author-side validation

An independent Python program enumerated all 110,740 unoriented nonzero integer differences with \(q\le40\) for 39 selected rational pairs \((S,T)\), including both triple-tie rays, their integer/rational perturbations, and both satellite walls. It used a shared **integer denominator** for all six gap ratios, and for each \(p=11,\dots,40\) compared the exact exhaustive minimizing set against the theorem whenever the optimum was strictly below \(1/2\). Result: **PASS, 1,064 strict-sub-half parameter/Port comparisons**, no mismatches. Validation covers the declared bounded domain and rational samples; the real-parameter, unlimited-Port result follows from the preceding symbolic argument and its R98/R99 premises.

Companion: \`research_notes/portable_direct/x6_r101_subhalf_multiplicity_verify.py\` and \`research_notes/portable_direct/x6_r101_subhalf_multiplicity_results.json\`.

## Research and control frontier

New result: closed secondary-multiplicity phase diagram **inside** the \(\eta<1/2\) region, including two sharp unbounded threefold-tie loci and exact satellite corridors. Dependencies remain R98 (value theorem) and R99 (ten-carrier theorem); external independent mathematical review has not occurred. This is a BRC auxiliary observer result. To attach it to native P000 requires a separately typed, future-operation-safe observer-fiber law preserving six-axis Cell identity, ordered native paths, triadic force, provenance, and heartbeat chronology. Retain the project joint-relation observer anti-erasure constraint.

On 2026-11-22 the native current Task read \`r2-20261122-0805-x6-current-task-v1\` returned terminal \`FAILED / SOURCE_TREE_TRUNCATED\`. Formal owner/CLAIM and permission were not refreshed; this standalone author-side proof is independent GitHub research, not a native PROGRESS, Result, Review, or Foundation adoption. Later activity association must use the actual session/Activity/ownership and source CAS, not this note as a claim token.
