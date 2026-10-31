# EC49BB — exact all-real optimal causal BRC observer on η∈[21/50,43/100]

**2026-10-30; AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_SYMPY_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.** Conditional on the previously author-proved sparse-edge representative lemma EC49AV; independent mathematical review pending. Strictly-positive auxiliary 18+18 P/Q probability BRC only, **not** signed/phase BRC, native X6, native 3D slice, Heartbeat World dynamics or empirical physics.

## Frozen model and interval theorem

Hidden w∈{0,1,2} is uniform. The first-stage action c∈{0,1,2,3,STOP} has cost (1,1,2,2,0). For a row-stochastic x[w,c], its expected cost is C1=43/48. Conditional observed u∈{0,1} has probability Pr(u|w)=1/2+(2u−1)(1−w)η. The second-stage coin p(c,u)∈[0,1] observes only (c,u), not hidden w, with exact expected purchase cost C2=13/16. Sensor outcome z∈{0,1,2} is visible only on purchase, and final acceptance depends only on bought (c,u,z). Put q_z(c,u)=x[z,c]Pr(u|z)/3, T(c,u)=Σ_z q_z, V(c,u)=Σ_z[43q_z−16T]_+/172. Optimal observable acceptance gives H=α−177β/172=Σ_(c,u)p(c,u)V(c,u).

**Theorem (conditional on EC49AV sparse reduction):** for every real η∈[21/50,43/100] and every lawful real causal policy,

[
\boxed{H_{\max}(\eta)=\frac{2752\eta^2+42\eta+1397-172(1-2\eta)\sqrt{19-26\eta}}{8256(1+2\eta)}}.
]

The optimizer is explicit. Set

[
t_*(\eta)=\frac{27-10\eta-4\sqrt{19-26\eta}}{8(1+2\eta)},\quad
p_*(0,1)=\frac{8\eta+\sqrt{19-26\eta}}{4(1+2\eta)}.
]

Take x rows `((11−8t*)/16,0,t*/4,0,(5+4t*)/16)`, `(0,1,0,0,0)`, `(1,0,0,0,0)`. Buy all positive-mass paid fibers except (c,u)=(0,1), where purchase occurs independently with probability p*. Accept exactly the bought observable outcomes `(0,0,2),(0,1,0),(1,0,1),(1,1,1),(2,0,0),(2,1,0)`. Exact algebra verifies 0<t*<1, 0<p*<1, both costs, β=13/48, and α=Hmax+(177/172)β. At η=21/50 the formula is `593779/4747200−sqrt(202)/2760` (EC49AZ); at η=43/100 it is `267209/2132800−7sqrt(782)/44640` (EC49BA). This closes the **entire continuous real interval** not just two endpoints.

## Why all causal policies reduce to these families

The inherited EC49AV lemma starts at a global maximizer (x,p). Fix p: the exact paid-mass condition is linear in x; H(x,p) is convex in x. Choose a maximizing extreme point of the polytope with three row-sum constraints, first-cost equation and paid-mass equation, giving at most five nonzero x entries. Fix the chosen x, replace p by an optimal extreme point of the one-resource purchase knapsack, leaving at most one fractional positive-mass fiber. A feasible at-most-five-supported point satisfying the original four first-stage equalities lies in an original polytope vertex or edge. Thus it suffices to optimize over every original first-stage edge. This is the **nontrivial predecessor logical dependency**, not independently reviewed here.

Full exact Fraction enumeration reproduces **168 first-stage vertices, 924 edges**, of which **720** have maximal purchasable mass below 13/16; **204** clipped edges remain. For λ≥0 use the valid sensor-cost dual
[
D_\lambda(x,\eta)=\lambda\frac{13}{16}+\sum_{c,u}[V_\eta(c,u)-\lambda T_\eta(c,u)]_+\ge H(x,p,\eta).
]
On **196** ordinary edges, the executed checker gives an exact common rational λ for the four corners formed by both *clipped* edge endpoints and η endpoints 21/50,43/100. Exact cap at η=21/50 is `CAP0=617983/5160000`; cap at η=43/100 is `CAP1=151/1250`. At fixed λ, Dλ is separately convex in x and η (q and the positive-part score are affine in either argument holding the other fixed). Hence at every x on each of these edges, and for all real η in the interval,
[
H\le L(\eta)=\frac{534500\eta+393493}{5160000}.
]
All 196 exact prices appear in the published full JSON report.

The other **8** clipped edges have identical full q-fiber signatures up to relabeling; their supports are `(0,2,4,6,10)`, `(0,3,4,6,10)`, `(0,6,10,12,14)`, `(0,6,10,13,14)` and `(1,2,4,5,11)`, `(1,3,4,5,11)`, `(1,5,11,12,14)`, `(1,5,11,13,14)`. A representative has x rows as above with variable t∈[0,1]. Its total paid mass is (43−4t)/48, requiring withholding (1−t)/12.

## Exact optimizer on all eight exceptional edges

Every one of 24 atomic score expressions 43q_z−16T has a fixed sign on rectangle [0,1]×[21/50,43/100], proved by bilinearity and exact four-corner checks. Positive scores occur at precisely the six visible acceptance events above. The fiber `j=1=(c=0,u=1)` has the lowest positive reward per purchased mass. The differences `V_j T1−V1 T_j` are nonnegative for all t,η, with exact factors:

- j=0: `(2η−1)(2η+1)(8t−27)(8t+5)/36864`.
- j=2,3: `−(2η−1)/144`.
- j=4: `t(2η−1)^2/576`.
- j=5: `−t(2η−1)(2η+1)/576`.

All remaining fibers have zero reward. Since `T1=(27−10η−(8+16η)t)/96` and `T1−(1−t)/12=(19−η(10+16t))/96>0`, the best purchase at each t buys every other positive-mass paid fiber and uses `p1=1−(1−t)/(12T1)` on fiber 1. The resulting exact objective for every real t,η is
[
H_{\rm best}(t,\eta)=h(\eta)-\frac{at^2+bt+c}{2064(d-ft)},
]
where `h=77/688+(674η−175)/16512`, `d=27−10η`, `f=8+16η`, `a=344(1−4η²)`, `b=2436η²+1568η−1201`, `c=2060η²−5096η+1769`.

Let `M(t)=at²+bt+c`. Its quotient derivative numerator is `N(t)=−aft²+2adt+bd+fc`, strictly increasing since `N'(t)=2a(d−ft)>0`. Exact evaluations
[
N(3/4)=43(2\eta-1)(484\eta^2-508\eta+137)<0,
]
[
N(4/5)=\frac{43}{25}(2\eta-1)(12996\eta^2-13084\eta+3009)>0
]
hold for the whole η interval (their quadratic signs follow from exact endpoint and derivative bounds). Hence the unique maximizing t lies between 3/4 and 4/5. The exact polynomial identity
[
a(ad^2+bdf+cf^2)=1376^2(1-4\eta^2)^2(19-26\eta)
]
yields the t* radical, and substitution yields the Hmax radical formula without numerical fitting.

## Strict uniform separation from ordinary edges

A fixed **rational** t=3/4 lawful special-edge policy, with the optimal observation-only purchase, satisfies
[
H_{\rm best}(3/4,\eta)-L(\eta)=
\frac{1314500\eta^2-307192\eta-122669}{10320000(22\eta-21)}>0.
]
On [21/50,43/100], the numerator is strictly increasing and still negative at 43/100; the denominator is negative throughout. Thus the eight-edge maximum strictly exceeds **all** 196 ordinary-edge upper bounds uniformly; combined with exhaustive 720+196+8 and the inherited reduction lemma, this proves the theorem conditional on that dependency.

## Evidence and scope

Actually executed on 2026-10-30: Python 3 `Fraction` exact rational classification and price computation, plus SymPy 1.14.0 exact symbolic equations, events, density ordering, derivative, endpoint radicals, both costs and α/β/H. Ran `python VERIFY_EC49BB.py > EXACT_REPORT_EC49BB.json` and repeated byte-for-byte successfully. Executed source SHA256 `ff32aeb73ddea3f809c422a29fac99c37d53b8bbb560153a8e6e929ba203e916`; full executed JSON SHA256 `fea1f13f554738fb126b8d5c443cc3ad89ad533fa929dcf0fd6f1e67bc7975fe`. Both exact raw files are archived losslessly as `VERIFY_EC49BB.py.gz.b64`, `EXACT_REPORT_EC49BB.json.gz.b64` in the same research directory. Decode using Python `base64.b64decode` then `gzip.decompress`, verify raw SHA256, then execute; the verifier is self-contained and imports no sibling files.

Frozen inputs: GLOBAL_KNOWLEDGE_V1 `main@ae95db422329f57935973df82b6b5a08e2c9d59a`; EM `main@4f75ce4f2301660419479a6dfdca6748bb41c10a`; predecessor PR #1730 head `d57f4b67f21d6f2c9871c963dbc5000e13492b2c`. P000 and ACTIVE worldview read only. Native Enterprise Math service 0.6.11 returned `authority_granted=false`, owner lookup `CONTROL_QUOTA` and session creation `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. No formal Source-native Research-Activity, CLAIM, Result, Driver review or acceptance; no native signed/phase BRC/X6/Heartbeat transfer proof.
