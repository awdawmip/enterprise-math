# Stage270 — exact adjacent Bellman face across Stage269 C–D

Date: 2026-10-29. Portable author `EM-R2-RESEARCH2-20261029-STAGE270-LOCAL` (not a Source-issued role/session/CLAIM). Class `AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED`. This is a finite external ternary IID sequential decision theorem, not a native P000 six-dimensional Cell/Heartbeat result.

## Sources and boundaries

Verified read snapshots: `awdawmip/chatgpt-global-knowledge main@bf2d12d1d8fbbe1efeac9ce8a37d11d6114fba36`, `awdawmip/enterprise-math main@4d641868367e435cb350b7dbaa46b02f48f976d3`, plus predecessor Stage269 author research commit `b35a4b8167e6c55e076c484968fd87c7a73d66df` (PR #1571). Read global bootstrap/manual, mathematics/code/output policies, P000 project projection (Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`), ACTIVE world constraints, project AGENTS and portable research protocol. Native em_status version 0.6.11 reported `research_authority_granted=false`, authenticated Sites client read-only and active-job quota 5/5. We performed portable author reasoning and ordinary GitHub research-artifact publication only; live owner/CLAIM and independent Driver review require separate native Source evidence.

## Problem and exact point theorem

On `{0,1,2}`, strictly positive IID laws are `P=(1/8,1/24,5/6)` and `Q=(1/12,1/12,5/6)`. At most `N=12` observations; any randomized **complete ordered-history** sequential strategy may decide P, decide Q, or continue before N. Set `eP=P(decide Q)`, `eQ=Q(decide P)`, `tP=E_P[T]`, `tQ=E_Q[T]`, and `V12(a,b)=min max(tP,tQ)` with errors at most `(a,b)` (infinite if infeasible).

For exact caps

    a270=402360299687/5283615080448
    b270=431878115465/557256278016

we prove

    V12(a270,b270)=267107458235/46438023168
                  ≈ 5.751912764862507.

The exact globally valid Lagrange support is

    lambdaP=134304895492096/947487230457
    lambdaQ=48948392988/643236409
    thetaP=0, thetaQ=1
    H=34613913912513106850567/458327437076524179456.

## Entire real-cap equality face

Define these four vectors in `(eP,eQ,tP,tQ)` order, not merely their two error coordinates:

    C=(1135528662191/15850845241344,146193716605/185752092672,
       27574125092087/5944066965504,254314824805/46438023168)
    D=(1281650262191/15850845241344,424896849815/557256278016,
       10159335564029/1981355655168,280411524805/46438023168)
    E=(1133161305691/15850845241344,146231594105/185752092672,
       27588964539587/5944066965504,84859115435/15479341056)
    F=(1279282905691/15850845241344,425010482315/557256278016,
       10164282046529/1981355655168,31186005145/5159780352).

All four are deterministic Bellman-minimizing full-history strategies. They satisfy `F−D=E−C` in **all four coordinates**, `tQ>tP`, and `lambdaP*eP+lambdaQ*eQ+tQ=H`. Their error pairs form the strictly convex parallelogram

    R270=conv(C,D,F,E),
    area(R270)=123370733132421875/69007679864054552199168.

**Theorem (all real caps).** For every `(a,b) in [0,1]^2`,

    V12(a,b)=H−lambdaP*a−lambdaQ*b   iff   (a,b)∈R270.

The new region shares the *entire C–D edge* with Stage269 `R269=conv(W,Z,D,C)` and their interiors do not intersect. Explicit signed orientations are

    orient(C,D,E)=−123370733132421875/69007679864054552199168,
    orient(C,D,W)=+15006059401671875/17251919966013638049792,

where W is Stage269's old W corner. Together with strict convexity and exact common endpoints these establish complete-edge adjacency.

## Proof and full-history exhaustiveness

For counts `s=(i,j,k)` define `p_s=(1/8)^i(1/24)^j(5/6)^k`, `q_s=(1/12)^(i+j)(5/6)^k`. On each *individual ordered prefix*, the unnormalized exact Bellman recurrence is

    B_s=min(lambdaQ*q_s,lambdaP*p_s,q_s+Σ_{x=0}^2 B_{s+e_x})

before depth 12; omit the continue action at depth 12. The options are stop-P, stop-Q, and continue. Backward induction over the full ordered tree shows that the minimum value depends only on these counts; this is an exact sufficient-state quotient for **this finite IID law and these four observers/future actions**, not a claim that history identity can be discarded in native P000. The root equals H, so any full-history randomized strategy satisfies

    lambdaP*eP+lambdaQ*eQ+tQ >= H.

Both multipliers are strictly positive and `max(tP,tQ)>=tQ`, yielding the stated lower bound for any feasible cap pair.

The accompanying standard-library `Fraction` checker covers **all 455 count states and all 1274 legal action costs**, finding **817 strictly positive action gaps** with minimum `89351863/1931388047598192427008`. There are exactly two ties: `T=(0,0,5): stop-P/continue` and `U=(1,2,2): stop-Q/continue`. Every other available action has a unique strict minimizer.

The T and U prefixes are both depth 5 but have incompatible counts, so neither is ancestor of the other. T is reached at exactly one ordered prefix; U at exactly ten, irrespective of decisions at T/U. Each U prefix has the same positive P and Q source likelihood and identical Bellman-minimal suffix effects. Thus arbitrary history-dependent randomization at the ten U prefixes affects all four observables only through their mean continuation probability `u∈[0,1]`; T has an independent continuation probability `r∈[0,1]`. Every Bellman-equal history policy therefore yields **exactly**

    Obs(r,u)=C+r*(D−C)+u*(E−C), 0<=r,u<=1.

Conversely every such pair is implemented by randomizing these tied actions (or by a lottery over the four deterministic corners). Since `tQ>tP` at every corner it holds throughout the whole face. Strictly positive error multipliers force **both** caps to be saturated whenever the affine lower bound is attained. The attainable error pairs of all Bellman-equal strategies are precisely R270. The finite ordered-history stochastic decision kernels form a compact polytope and their observer maps are continuous, so minima are attained whenever feasible. Hence outside R270 equality cannot occur, including by a limiting sequence. This establishes the full-real iff claim.

## Exact primal meeting the dual

The two independent tie probabilities for the target are **r=49/100 and u=1/50**. The corresponding full four-observer tuple is

    (402360299687/5283615080448,
     431878115465/557256278016,
     3221924873893/660451885056,
     267107458235/46438023168).

Both errors exactly equal their caps and

    tQ−tP=5192430789043/5944066965504 > 0.

Thus max time equals tQ, and this primal reaches the global Bellman dual lower bound exactly. The Stage269 exterior feasibility upper bound is now established as the **precise optimum**.

## Actual verification and BRC provenance boundary

`REPRO_STAGE270.py` is the locally executed self-contained `Fraction` certificate; `REPRO_STAGE270_EXECUTED_STDOUT.txt` records actual output. Four deterministic corner policies were independently evaluated (1) by positive rational P/Q source mass with integer count multiplicities and (2) by an unmerged DFS traversing every concrete ordered word. Independent DFS counted **13084 nodes and 8724 terminal branches** across the four corners; each source's terminal mass is exactly one, and all four observer coordinates match. Reached tie multiplicities T=1 and U=10 were explicitly checked. The program terminates with `STAGE270_EXACT_ALL_REAL_FACE_PASS`.

This is BRC-compatible *source/branch/multiplicity fidelity*, but not an implementation of native typed BRC arithmetic. Exact sufficiency here is restricted to the four declared IID observers, the specified future stopping actions, and horizon 12; it does not erase general joint relations, signed phases, X6 steps or Cell provenance. No transfer to P000 native 6D Cell dynamics is asserted without a specific six-axis embedding, three-dimensional slice/third-coordinate semantics, readout/update correspondence, and relation-preservation certificate.

## Stage271 handoff

The program also proves a strict-exterior **feasible** Stage271 witness across R270's E–F edge: change the E policy at reached count `(1,2,3)` (20 concrete histories) from stop-Q to continue and mix `49/100 E + 49/100 F + 1/50 changed(E)`. Caps are

    a271=133853268599/1761205026816
    b271=431993556815/557256278016
    V12(a271,b271) <= 89124381535/15479341056.

The exact orientation is `orient(E,F,target)=−4050750660078125/69007679864054552199168`, opposite the old C-side. Next research should reconstruct the matching Stage271 Bellman support and entire all-real face with full ordered-mass verification. This witness is only a feasibility statement in this Stage270 artifact.
