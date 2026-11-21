# X6 R78 — 九个可严格取胜的四通道 BRC 精度开放区域：精确有理数证书

Date: 2026-11-21 (Asia/Shanghai).
Scientific status: CONDITIONAL_FINITE_EXACT_RATIONAL_CERTIFICATE / AUTHOR_CHECKED / NOT_INDEPENDENTLY_REVIEWED.
Source: R72, R77. Frozen P000: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`.
This is a **conditional positive-count BRC star-histogram observer**, not a native X6 Cell/Link/Port time law; it preserves frozen P000, six spatial axes, the native triadic whole-event requirement and provenance-sensitive observer boundaries.

## Statement

Fix maximum successful degree D=4, an integer Port population p>=125, unknown common additive offset b, four positive real error weights w=(w1,w2,w3,w4), and the moment observer
`Y_t=sum_{d=0}^4 c_d d^t+b+e_t`, `|e_t|<=eta w_t` for t=1..4. Recovery target is only the histogram (c2,c3,c4).
A candidate difference a=(a2,a3,a4) has Port demand
`q(a)=max(sum max(a_i,0),sum max(-a_i,0))`.
Let `z=(0, 2a2+6a3+12a4, 6a2+24a3+60a4, 14a2+78a3+252a4)` and
`F(a;w)=max_{1<=i<j<=4}|z_i-z_j|/[2(w_i+w_j)]`.

Let A be the 28 unoriented vectors in the R72 exact finite covering atlas. The following **nine distinct atlas vectors** each uniquely minimize F on a nonempty open subset of the full positive weight cone. Their integer-weight certificates, exact winner cost, strict gap to the second-best atlas vector and guaranteed coordinatewise relative perturbation radius are:

| Port q | candidate a | integer weights w | min F | gap to next candidate | open radius rho |
|---:|---|---|---:|---:|---:|
| 7 | `6,-4,1` | `(8,8,26,187)` | 4/65 | 1/1040 | 1/129 |
| 10 | `9,-5,1` | `(3,3,20,34)` | 6/37 | 1/222 | 1/73 |
| 11 | `10,-5,1` | `(2,2,2,2)` | 1/4 | 5/4 | 5/7 |
| 16 | `15,-6,1` | `(1447,167,166,1850)` | 1/336 | 1/37296 | 1/223 |
| 27 | `24,-14,3` | `(163,165,1809,388)` | 3/986 | 1/161704 | 1/985 |
| 39 | `36,-16,3` | `(199,41,18,18)` | 6/217 | 1/7812 | 1/433 |
| 43 | `39,-20,4` | `(41,46,4,4)` | 3/25 | 1/200 | 1/49 |
| 49 | `45,-21,4` | `(413,4334,3265,364)` | 1/783 | 2/202797 | 1/260 |
| 125 | `114,-56,11` | `(2,47,3,2)` | 12/49 | 1/196 | 1/97 |

At each listed weight, the winner is strictly better than all 27 other atlas vectors. Consequently **any subset of the existing R72 28-vector atlas that preserves the minimum for every positive weight and p>=125 must contain all nine of these vectors**; thus such a subatlas has cardinality at least nine. This is a nontrivial mandatory-core lower bound within R72's exact atlas, not an assertion that the other 19 vectors are redundant.

## Exact proof and neighborhood certificate

1. The companion JavaScript verifier constructs each of the 28 moment-gap sextuples from the stated integer vectors. For each of the nine given positive-integer weight profiles it computes all 28 values of F as reduced fractions of BigInt integers, finds the unique smallest candidate, the nearest competitor, their strictly positive difference and the stated rho. Every comparison is integer cross multiplication. The resulting nine rows are independently reconstructible from the displayed finite input table and code. These exact finite calculations prove nine strict atlas winners; no floating-point inference is used.
2. Fix one profile w with winning value v and next-best value s>v. For any w' satisfying `|w'_i/w_i-1| <= eps` for each i and `0<=eps<1`, every pair denominator changes by a factor in [1-eps,1+eps]. Hence `F(a;w)/(1+eps) <= F(a;w') <= F(a;w)/(1-eps)` for every a. The winner remains strictly optimal whenever `v/(1-eps)<s/(1+eps)`, equivalently `eps<(s-v)/(s+v)=rho`. Each listed positive rho proves a full-dimensional open winning cone, not merely an isolated witness.
3. If R72's author-checked finite-cover theorem holds over all feasible integer differences, these nine winning regions also achieve the **global threshold** eta*(p,w), for every p>=125. Formal independent acceptance of the R72 atlas remains separate. The necessity lower bound applies to subsets of the specified 28-vector atlas.


## Sharp weight-specific Port saturation at the nine certified profiles

There is a stronger consequence of the same exact strict gaps. Fix one listed weight vector w and let q0 be its row's Port demand. R72's finite atlas covers **every** population p>=4 while filtering by q<=p. For p>=q0, the listed vector is feasible and is strictly better than every other atlas vector; hence the exact all-difference optimum equals its displayed F value. For 4<=p<q0, it is absent and every remaining atlas vector has cost strictly larger (indeed at least F+the listed strict gap). Therefore **q0 is the sharp weight-specific saturation Port threshold**, not merely an example of a winner at p>=125. This yields nine exact saturation thresholds `7,10,11,16,27,39,43,49,125` with the corresponding integer weight profiles in the table. The conclusion is conditional on the same author-checked R72 exhaustive finite-coverage certificate; it does not require a new full search over integer differences.

## Reproducibility and coverage

Run `node x6_r78_nine_open_winner_chambers_verify.js` and compare its exact JSON with `x6_r78_nine_open_winner_chambers_results.json`. It uses 28 vectors and nine weight profiles (252 rational objective evaluations, each taking six pair comparisons), confirms all q-values and all nine strict winners. Arithmetic uses BigInt rational fractions and exact reduction. No external software solver or numerical tolerance is needed for this certificate.

Exploratory noncertifying optimization suggests that these nine may be all strict winners of A. **Unresolved:** prove or refute this exhaustiveness with an independently checkable rational polyhedral chamber certificate; if true, determine whether nine suffice uniformly even at shared/tied boundaries. Separately investigate the named native Cell/Link/Port and TRIADIC_CLOSURE_E observer-fiber relation without upgrading this histogram observer to physical dynamics.

Provenance: historical independent portable line EM-X6-214D9C; original Activity RA-545183ADD4EF71C3E4698AEE is not asserted as a live mutation capability. Formal Task CLAIM and PROGRESS remain with their currently authenticated executor.
