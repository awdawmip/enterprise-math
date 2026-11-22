# X6 R112 — Two open twelve-near chambers beyond the R110/R111 certificates

Date: 2026-11-22. Status: AUTHOR_PROOF / EXACT_RATIONAL_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.

Scientific ontology remains pinned to \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\` (P000 V5). This is a theorem about the **conditional auxiliary four-positive-weight six-pair BRC observation norm** of R104–R111, not native Cell/Link/heartbeat time dynamics. The six joint pair directions and original Port/signed lattice are all retained. Predecessors: R104@48009c76, R110@21fad2aa, R111@3ad58ecf.

## Model

For nonzero \`a=(x,y,z) in Z^3\` identify \`a~-a\`. Write

\`\`\`
q(a) = max(sum(max(a_i,0)), sum(max(-a_i,0)))
u=x+3y+6z; v=3x+12y+30z; h=7x+39y+126z
F_w(a) = max(|u|/(A+B), |v|/(A+C), |h|/(A+D),
             |v-u|/(B+C), |h-u|/(B+D), |h-v|/(C+D))
eta_p(w) = min_{a!=0,q(a)<=p} F_w(a)
N_p(w) = {±a:q(a)<=p, F_w(a)<3 eta_p(w)/2}
\`\`\`

The four weights are positive real numbers, while Port \`p\` is an integer. All finite arithmetic certificates here use exact rationals.

## Theorem (two strict, open, twelve-near chambers)

Take the following two centers:

| Case | \`w0=(A,B,C,D)\` | \`p0\` | \`eta_p(w0)\` for every \`p>=p0\` | Maximum inside score | Smallest outside score |
|---|---|---:|---:|---:|---:|
| I | \`(60,1,10,46)\` | 51 | \`1/11\` | \`7/53\` | \`9/61\` |
| II | \`(6,47,45,2)\` | 92 | \`6/49\` | \`3/17\` | \`9/47\` |

For every integer \`p>=p0\`, each center has **exactly twelve** unoriented strict-\`3/2\)-near directions, listed below. The other mod-3 sign orbit is \`{±(0,1,2)}\`.

More strongly, for **every positive real** \`w\` satisfying \`max_i |w_i-(w0)_i| <= 1/25\`, and every integer \`p>=p0\`, \`N_p(w)\` contains precisely the same twelve directions as \`N_p(w0)\`. This proves two positive-volume four-dimensional parameter chambers where the attainable twelve-near count persists.

Both chambers are disjoint from the sufficient-condition domains of R110 and R111. These prior sufficient conditions are useful but not necessary.

### Complete direction lists

Case I:

| \`a\` | \`q(a)\` | \`F_w0(a)\` |
|---|---:|---:|
| \`(5,-1,0)\` | 5 | \`6/47\` |
| \`(10,-5,1)\` | 11 | \`1/11\` |
| \`(11,-5,1)\` | 12 | \`6/47\` |
| \`(15,-6,1)\` | 16 | \`6/47\` |
| \`(21,-10,2)\` | 23 | \`6/47\` |
| \`(25,-11,2)\` | 27 | \`6/47\` |
| \`(26,-11,2)\` | 28 | \`1/11\` |
| \`(31,-15,3)\` | 34 | \`6/47\` |
| \`(36,-16,3)\` | 39 | \`6/61\` |
| \`(41,-17,3)\` | 44 | \`8/61\` |
| \`(46,-21,4)\` | 50 | \`7/61\` |
| \`(47,-21,4)\` | 51 | \`7/53\` |

Case II:

| \`a\` | \`q(a)\` | \`F_w0(a)\` |
|---|---:|---:|
| \`(10,-5,1)\` | 11 | \`1/8\` |
| \`(14,-9,2)\` | 16 | \`1/8\` |
| \`(24,-14,3)\` | 27 | \`6/47\` |
| \`(31,-12,2)\` | 33 | \`3/17\` |
| \`(34,-19,4)\` | 38 | \`7/47\` |
| \`(35,-16,3)\` | 38 | \`1/8\` |
| \`(45,-21,4)\` | 49 | \`6/49\` |
| \`(55,-26,5)\` | 60 | \`7/53\` |
| \`(59,-30,6)\` | 65 | \`1/8\` |
| \`(69,-35,7)\` | 76 | \`6/49\` |
| \`(79,-40,8)\` | 87 | \`7/53\` |
| \`(83,-44,9)\` | 92 | \`3/17\` |

## Whole-integer-lattice proof

The integer moment map has determinant 36. Its exact inverse is

\`\`\`
x=(h+19u-8v)/2
y=(-h-14u+7v)/3
z=(h+11u-6v)/12
\`\`\`

and is integral exactly when \`v=0 mod 3\`, \`h-u=0 mod 6\`, and \`h-u-6v=0 mod 12\`. Fix the complete upper cutoff \`R=9/61\` for center I or \`R=9/47\` for center II. For any integer direction with \`F_w0(a)<=R\`, the first three ORIGINAL pair observations yield the integer moment boxes

\`\`\`
I:  |u|<=9, |v|<=10, |h|<=15
II: |u|<=10, |v|<=9, |h|<=1
\`\`\`

Apply all three congruences and the *other three original pair constraints* \`|v-u|<=R(B+C)\`, \`|h-u|<=R(B+D)\`, \`|h-v|<=R(C+D)\`. Complete enumeration gives exactly **fourteen** nonzero unoriented integer directions in each box: the twelve displayed directions, plus

\`\`\`
I:  (51,-22,4), (57,-26,5): both F=9/61 (q=55 and 62)
II: (21,-7,1), (93,-49,10): both F=9/47 (q=22 and 103)
\`\`\`

Every other nonzero integer vector has score **strictly greater than R** by the complete moment-box argument. The minimum score among the fourteen is \`1/11\` (center I; witnessed at q=11) or \`6/49\` (center II; witnessed at q=49). Hence the exact minima hold for all \`p>=p0\`, and the strict-near cutoff separates all twelve table rows from the two outsiders and from every other integer vector. This covers the unbounded integer lattice without a finite Port truncation.

The companion \`x6_r112_dual_chambers_verify.py\` uses the standard-library exact \`Fraction\` type, exhausts both **complete** integer boxes and verifies the integrality conditions, 14/12 counts, exact scores, maximal Port, the missing mod-3 orbit and every rational perturbation margin. The JSON output contains every candidate.

## Uniform real-weight perturbation proof

Let \`epsilon=1/25\` and \`dmin=min_{i<j}(w0_i+w0_j)\`, which equals \`11\` and \`8\`, respectively. If all four coordinates move by at most \`epsilon\`, every one of the six pair denominators changes by at most \`2 epsilon\`. Put \`t=2 epsilon/dmin<1\`. For every integer \`a\`,

\`\`\`
F_w0(a)/(1+t) <= F_w(a) <= F_w0(a)/(1-t).
\`\`\`

Exactly the same comparison holds for minima over the unchanged Port-feasible set. Thus every ratio \`F_w(a)/eta_p(w)\` lies between \`1/K\` and \`K\` times the center ratio, where \`K=(1+t)/(1-t)\`.

For center I, \`K=277/273\`, the largest inside ratio is \`77/53\` and the smallest outside ratio is at least \`99/61\`. For center II, \`K=101/99\`, the corresponding ratios are \`49/34\` and at least \`147/94\`. Exact inequalities are

\`\`\`
(77/53)*(277/273) < 3/2 < (99/61)*(273/277)
(49/34)*(101/99) < 3/2 < (147/94)*(99/101).
\`\`\`

All twelve inside vectors therefore remain strictly near; every other vector stays out, for **every** \`p>=p0\` simultaneously. Port does not depend on the weight perturbation, so feasibility is retained.

## Strict extension beyond R110/R111 tests

The R110 upper bound \`U=min(F(s),F(t))\` for \`s=(10,-5,1), t=(24,-14,3)\`, and the R111 bound \`V_b=F(b)\` for \`b=(9,-5,1)\`, are each required by those tests to be \`<=min(2/(A+B),6/(C+min(A,B)),8/(D+min(A,B,C)))\`. At centers I and II:

\`\`\`
I: U=1/11, V_b=3/11, while 2/(A+B)=2/61
II:U=1/8,  V_b=3/4,  while 2/(A+B)=2/53.
\`\`\`

These strict failures persist throughout the declared neighborhoods, using the same multiplicative score lower bound and \`2/(A+B)<=2/(A0+B0-2epsilon)\`. Therefore both regions lie genuinely outside those earlier sufficient cones; no earlier theorem is contradicted.

## Scope and continuation

This is a conditional auxiliary BRC mathematical result, with author proof and exact checking, not an independent Review or an admitted native time-dynamics law. It does not alter P000, the frozen task inputs, the separate R063 six-file native benchmark, or another researcher's CLAIM/Result/Activity.

The global question remains whether 13 nonzero mod-3 sign orbits can all occur strictly within \`3 eta_p/2\` for any positive real four-weight BRC norm. These two new open chambers omit \`±(0,1,2)\` despite failure of both previous easy sufficient certificates. A useful follow-up is a six-pair joint-observer incompatibility test across all possible residues, or an exact 13-orbit witness with certified Port feasibility.
