# Stage159 — exact full-real affine optimum (external N14 ternary iid model)

**Evidence class:** AUTHOR exact-rational computation-assisted proof, with two structurally distinct author implementations. No independent Research Driver review, Source-native CLAIM/Result, Lean acceptance, or P000/X6 native transfer.

## Sources and frozen scope

Global Knowledge canonical input: awdawmip/chatgpt-global-knowledge main@35005f59b5c1065b74ee44e1a4f5a7ae05821bd9. Its two normative entries, Enterprise Math task bootstrap, P000 startup (original blob SHA1 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), ACTIVE worldview, math/code policies and BRC route were read. EM scientific input: awdawmip/enterprise-math main@2f04c99d7a09da6453081fcf82b9e1f3d0786982, its current docs/PORTABLE_RESEARCH_PROTOCOL.md and the already completed Stage158 author proof and Stage159 handoff. GitHub authenticated identity was awdawmip. Native em_control_tasks returned CONTROL_QUOTA. Native em_session_start RESEARCHER was rejected with STATIC_READONLY_SCOPE_DENIED, operation_sent=false, so current active native owner and formal Researcher/CLAIM/Result authority remain unverified.

Let N=14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Policies may randomize based on **arbitrary complete ordered histories**, and stop by observation 14. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P tau, tQ=E_Q tau. Define V14(alpha)=min over such policies with eP,eQ<=alpha of max(tP,tQ). This is an external finite iid auxiliary problem, NOT the native six-dimensional Cell-space model.

## Theorem — all real points

For every REAL delta satisfying

    0 <= delta <= 9439560065/243657671368796798976,

we prove

    V14(alpha158+delta)=V158-(1146263643534/1887912013)*delta,

with inherited Stage158 author endpoint

    alpha158=763167995878686618305/2192919042319171190784
    V158=3292184925194961698843/274114880289896398848.

The new exact endpoint is

    alpha159=381583997981821329445/1096459521159585595392
    V159=13168739674988914815857/1096459521159585595392.

The corresponding supporting line is STRICTLY BELOW V14(alpha) for every alpha>alpha159 (sharp right endpoint). This is not a mere finite sampling statement.

## 1. Global Bellman dual certificate

For count state s=(n,a,b), the likelihood ratio is R(s)=Q(s)/P(s)=2^(a+b)/3^a. Set

    K=580027221414/1887912013
    L=566236422120/1887912013.

Under P-based continuation the Bellman value is

    H(s)=min{K*R(s) [decide P], L [decide Q],
             1+sum_x P(x)*H(child_x(s)) [continue, if n<14]}.

Enumerating all 680 finite count states with exact Fractions gives precisely two ties:

- I=(9,5,4), immediately Q versus continue;
- J=(10,2,0), immediately P versus continue.

There are 1238 strictly positive non-minimal action gaps, with minimum 20367756/1887912013; zero negative gaps. At the empty history,

    H(root)=11547482842531895473750632541/51710401982598719383535616.

At ANY ordered history, not just count-state policies, the same likelihood-ratio Bellman induction yields

    H(root) <= tP+K*eQ+L*eP
            <= max(tP,tQ)+(K+L)*alpha.

The order matters: K multiplies Q's false-P probability eQ, and L multiplies P's false-Q probability eP. Both K and L are strictly positive.

## 2. BRC ordered first-hit evidence and exact four-observer law

We retain distinct ordered prefixes (branch identities and multiplicities), and positive rational P/Q masses before applying an iid sufficient-count quotient. Under strict Bellman actions elsewhere, the true first-hit prefixes are:

| State | Ordered first hits | Total P mass | Total Q mass |
|---|---:|---:|---:|
| I=(9,5,4) | 30 | 5/1811939328 | 5/859963392 |
| J=(10,2,0) | 45 | 1953125/11943936 | 1953125/26873856 |

Their reached path cones are disjoint: I already contains four occurrences of symbol two (b=4) whereas J requires b=0; J is at later depth, so cannot precede I. Across prefixes reaching a fixed count state the P/Q likelihood ratio and iid conditional suffix distribution are constant. Consequently, even history-dependent Bellman-equality decisions can be averaged into one effective coin per tie for these **four observers only**. This does not imply a native P000 observer quotient.

Let i=Pr(immediate Q at I), j=Pr(immediate P at J), and M=(eP,eQ,tP,tQ). A pair of exact author computations gives

    M(i,j) = M00 + i*dI + j*dJ,

with the following exact rational vectors:

    M00=(1220759941128584035/3505953353861431296,
         223211418240365/641959232274432,
         5281452609775796317/438244169232678912,
         68763293274229/5944066965504)

    dI=(199825/1603087953297408,
        -23215/213986410758144,
        -812545/200385994162176,
        -134155/17832200896512)

    dJ=(-3201171875/3962711310336,
         771484375/557256278016,
        -30224609375/165112971264,
        -4150390625/46438023168).

The exact four-vector mixed difference M11-M10-M01+M00 is (0,0,0,0). All four corners were computed by (a) conditional suffix Fraction recursion on count states and (b) **literal unmerged ordered-prefix DFS with integer likelihood weights** P=(3,1,20)/24, Q=(1,1,10)/12. Both methods matched coordinate-for-coordinate at all corners. The DFS visited 448000,446920,446560,445480 nodes at (i,j)=00,01,10,11, and both terminal probability masses sum to 1 separately under P and Q. These are two author algorithms, not independent Driver validation.

## 3. Primal attainment on the whole real interval

Error equalization eP=eQ solves EXACTLY

    j(i)=1036789387122389/4611571200000000
        +(163474367/1537190400000000)*i.

Both j(0) and j(1) are strictly inside (0,1), and so is j(i) for every real 0<=i<=1. The equal common error increases strictly in i, from alpha158 to alpha159, by the width 9439560065/243657671368796798976. Thus every real alpha in the interval occurs.

The endpoint tP-tQ gaps are strictly positive:

    i=0: 253249280016335608715/548229760579792797696
    i=1: 506498552912101258645/1096459521159585595392.

Affineness gives tP>tQ throughout. At both endpoints, direct exact computation gives

    tP+K*eQ+L*eP=H(root),

hence also at every point in between. Therefore each primal strategy attains the universal dual lower bound and proves the stated all-real V14 formula, with slope K+L=1146263643534/1887912013.

## 4. Strict right sharpness under arbitrary complete-history policies

For finite horizon 14, the full ordered-history behavioral policy space is a compact finite product of action simplices, and all four observer functionals are continuous. Thus a feasible minimum is attained. Equality to this SAME dual support for alpha>alpha159 would force (K,L>0) eP=eQ=alpha, tP>=tQ, and selection only of Bellman-minimizing actions at every reached P-positive prefix. The exact positive gap certificate excludes all alternatives except the I/J tie coins. The ordered first-hit and likelihood-proportionality argument gives the same M(i,j) for any potentially history-dependent equality policy, with 0<=i,j<=1. Equal errors force j=j(i). Since common error strictly increases with i, its maximum is alpha159 at i=1. Contradiction. Hence strict right sharpness. No claim about native P000 dynamics follows.

## 5. Exact next dual candidate: Stage160

After I's immediate-Q coin saturates at i=1, preserve the J P/continue dual tie along

    (K,L)=(K159,L159)+t*(-1,-25280/14751).

The first strictly positive affine-gap closure is

    t160=6084006567309/15514860922834
    K160=2521611/8218
    L160=1229640/4109.

A new tie S=(13,5,2) decide P/continue appears; J=(10,2,0) decide P/continue persists. A fresh exact 680-state Bellman evaluation gives 2 ties, 1238 strictly positive gaps (minimum 565771/37868544), none negative. **Stage160 remains DUAL-ONLY:** no primal real interval is established.

Next: compute J/S true ordered first-hit masses; check cone overlap, full four observer corners by both methods, mixed term and error-balance feasibility, then the full-real primal interval or explicit rational infeasibility witness.

## Reproduction and evidence classification

PORTABLE_VERIFY_STAGE159.py is an exact standard-library checker executed locally and reproduced the dual census, literal unmerged DFS, observer corners, compensation, endpoint dualities, dominance and width. SCAN_STAGE160.py is the separate exact dual ray checker executed locally. Exact structured certificates and execution evidence accompany this note. These files are AUTHOR source artifacts, not remotely executed code, independent review, Source-native Result, Working Truth or Foundation promotion.
