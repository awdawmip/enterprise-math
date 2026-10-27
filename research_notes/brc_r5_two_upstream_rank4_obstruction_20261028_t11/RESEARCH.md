# R5: two upstream LR signatures collide — exact rank-four obstruction

Date: 2026-10-28 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. This is an author-research note, **not** a canonical native CLAIM/Result or accepted theorem. All claims concern a precisely restricted finite sequential-observer policy class.

## Sources / scope

Verified starting Global Knowledge V1 snapshot: `main@382a6ea6794814c820ce9e3af03f66a5c2575ca1` (`00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, applicable worldview and math/EM guidance). Verified project starting source: `main@b8a5f932bfa67272cab5960e3c0d91e07b91c757`, including `p000_reality_foundation.json`, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`, `AGENTS.md`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, and the prior R5 optional-upstream-masking proof / next task.

P000 is retained: discrete native six-axis spatial Cell torsor, separately typed time, no native plane. This note is **external exact statistical observer arithmetic**, not native BRC–Shor, physical heartbeat dynamics or a full-X6 propagation claim. Observer bridge: assign every finite history h a different raw X6 chart-relative Cell label c(h)=anchor+k(h)E_1 with an injective integer k, and separately record decision time t∈{1,2,3}. History, branch provenance and future actions remain retained; (t,R_t=P(h)/Q(h)) is a many-to-one observer readout. This assignment is a labeling bridge, not a claim that probabilistic transitions are primitive Cell steps. Only the declared four readouts and the allowed action subfamily are assessed.

## Rank-four collision lemma (all real behavioral mixing parameters)

Suppose two independent upstream LR signatures A/B have continuation probabilities x_A,x_B∈[0,1], but their downstream histories meet the *same* later LR signature, where seedless LR strategies must use one common continuation probability y∈[0,1]. With all other decisions fixed, the four-dimensional output has the form

    F_LR = O0 + x_A U_A + x_B U_B + x_A y V_A + x_B y V_B.

The full-history analogue can use independent y_A,y_B instead. Let M=[U_A U_B V_A V_B]∈R^{4×4}. If det(M)≠0, then (i) the true seedless LR image is nonconvex, and (ii) its convex hull is strictly smaller than the restricted full-history convex hull.

Proof of (i): the midpoint of F_LR(1,0,1) and F_LR(0,1,0) is T=O0+(U_A+U_B+V_A)/2. It lies in the LR convex hull. If T were a real seedless LR image, invertibility of M would give (x_A,x_B,x_Ay,x_By)=(1/2,1/2,1/2,0), forcing y=1 and y=0 simultaneously. Thus it is unattainable.

Proof of (ii): choose λ uniquely through M^T λ=(-1,-1,-1,+1). Then

    λ·F_LR = λ·O0 - x_A - x_B + y(-x_A+x_B).

For every real 0≤x_A,x_B,y≤1 the minimum is λ·O0−2 (multi-affinity gives endpoints; directly y=0 and y=1 each give minimum -2). In the full family the choice (x_A,x_B,y_A,y_B)=(1,1,1,0) attains λ·O0−3; the independent terms cannot improve beyond -3. Hence a strict exact support gap 1. QED.

**Boundary:** the theorem is for this fixed-other-decisions subfamily. Releasing earlier stop/declaration, side-state, or terminal actions may fill the hole and remove the separation. Neither global unrestricted LR nonconvexity nor unrestricted convex-hull separation follows without a separate certificate.

## Six strictly positive P/Q leaves

At t1: Q(A)=Q(B)=1/2; P(A)=1/4, P(B)=3/4; R1(A)=1/2,R1(B)=3/2.
At t2: A→C has (Q,P)=(1/6,1/6) at R2=1, A→L has (1/3,1/12) at R2=1/4; B→C has (1/4,1/4) at R2=1, B→H has (1/4,1/2) at R2=2. Both C histories share the LR signature (t2,R=1) while retaining different history.

| leaf | Q | P | terminal P/Q |
|--|--:|--:|--:|
| A,C,low | 1/12 | 1/24 | 1/2 |
| A,C,high | 1/12 | 1/8 | 3/2 |
| A,L | 1/3 | 1/12 | 1/4 |
| B,C,low | 1/8 | 1/32 | 1/4 |
| B,C,high | 1/8 | 7/32 | 7/4 |
| B,H | 1/4 | 1/2 | 2 |

Both total P and total Q equal one, with strictly positive leaves. The hidden histories' next LR kernels at C differ: (1/2,3/2) vs (1/4,7/4), each with Q probability (1/2,1/2), respecting the conditional likelihood martingale.

Restricted actions: At t1 choose stop-and-declare-P or continue independently for A/B. On t2 side states L/H necessarily stop and declare P. On t2 C stop means declare P; continue means observe t3 and declare Q only on the respective low outcome, otherwise P. Full-history may choose separate y_A,y_B at C; seedless LR chooses one y, with no shared persistent random seed. All probabilities are allowed to be arbitrary real in [0,1].

For O=(e_P,e_Q,E_Pτ,E_Qτ), where e_P=P(declare Q), e_Q=Q(declare P), exact leaf summation yields:

    O0=(0,1,1,1)
    U_A=(0,0,1/4,1/2)   U_B=(0,0,3/4,1/2)
    V_A=(1/24,-1/12,1/6,1/6)
    V_B=(1/32,-1/8,1/4,1/4)

The determinant det[U_A U_B V_A V_B] = 1/1536. With signed λ=(-80,-32,0,-2), one has λM=(-1,-1,-1,+1), hence for the **entire real restricted parameter cubes**:

    min_full λ·O = −37;
    min_seedless_LR λ·O = −36;
    exact minimum gap = 1.

A full strategy (x_A,x_B,y_A,y_B)=(1,1,1,0) gives O_full=(1/24,11/12,13/6,13/6). The seedless LR convex-hull midpoint

    T=(1/48,23/24,19/12,19/12)

has inverse coordinates M^{-1}(T−O0)=(1/2,1/2,1/2,0), hence is not realizable by any real seedless LR policy in this restricted family, though it is the midpoint of two valid LR deterministic policy points.

## Exact verification and external context

Actually executed the Python Fraction algorithm in `VERIFY.py`: 6 P/Q-positive leaves and prefix constraints, 16 deterministic restricted full-history tables, 8 restricted LR tables, vector identities, determinant, λ minima, and midpoint inverse. Exact output is `EXACT_OUTPUT.txt`, ending ALL EXACT CHECKS PASSED. Multi-affinity proves finite-vertex optimization covers all real randomized strategies; nonconvexity uses exact linear inverse, not a grid. The locally executed verifier SHA-256 was `5108e60cb2e0dd8ac5dfbc535634615daee5d81da8fe8edbd194e48fab258026`; output SHA-256 `874f7d44682d36e2b2cfab8457d2b231615e56a187cd94082bd8421055fb2f2a`. Remote verifier source consistency is independently checked at publication.

External comparison only: Laroche & Tachet Des Combes (ICML / PMLR, 2023), *On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs*, https://proceedings.mlr.press/v202/laroche23a.html. It describes Markov/non-Markov occupancy equivalence for correctly chosen MDP states; it cannot justify collapsing different hidden prediction kernels to an insufficient LR-only state. No assertion is made about originality relative to all literature.

This run's live EM gateway returned `CODE_REVIEW_REQUIRED`, `research_authority_granted=false`, active native jobs `5/5`, and `em_control_tasks → CONTROL_QUOTA`. Thus active Owner and canonical CLAIM were not verified; author note is NOT_ADMITTED pending true control authorization and independent Driver review.

## Exact next question

Release all other t1/t2 stop/declaration and terminal decision controls on the same six-leaf tree. Enumerate exact full/LR deterministic four-observation vertices, solve rational convex-hull membership or separation *globally*, and only then attempt real-parameter LR image exclusion. Search masked / rank-deficient multi-upstream collision families if this model fails global hull equality. Preserve X6/native observer bridge and the original signed four-metric scope.
