# Stage152 — exact all-real primal segment OPEN (dual candidate only)

## Frozen model and status

External ternary iid sequential test, horizon 14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Policies may randomize on *complete ordered histories*. Observers M=(eP=P(decide Q), eQ=Q(decide P), tP=E_P tau, tQ=E_Q tau). Objective V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha. This is an EXTERNAL AUXILIARY finite model, not P000 native Cell/X6 or Heartbeat dynamics.

Consume the AUTHOR-level Stage151 full-real theorem at
research_notes/n14_aux_iid_affine_151_20261026/PROOF_STAGE151.md.
No independent Driver review or native CLAIM/Result exists.

At its proved sharp right endpoint:

    alpha151 = 18373001785623238325/52808422392537808896
    V151 = 318746112099955105013/26404211196268904448
    K151 = 45154992/127757
    L151 = 6412152/18251

The optimal primal face has
B=(11,0,1) Q/C, Q-stop coin b=8061971501813291/8143872000000000 (strict interior),
U=(9,4,1) P/C, P-stop coin u=1 (saturated).

## Next dual candidate (NOT a primal theorem)

Hold B's Q/C equality, treating U as strictly P-stop; scan along dK=-1,dL=-112/129. Exact forward state/action-gap arithmetic closes first at

    ray_t_star=210556552344/4643483645269
    W=(8,3,3), decide Q / continue

The newly re-evaluated dual is

    K152=12844717560/36346217
    L152=12768141608/36346217
    H152(root)=341463027624594134301829727/1327376472826305935572992

At this candidate, exactly two Bellman ties occur:
B=(11,0,1) Q/C and W=(8,3,3) Q/C.
The remaining 1238 action gaps are strictly positive; the minimum is 204027667/1130512733568. There are zero negative gaps.

## First unanswered scientific unit

1. Under the strict minimizers at (K152,L152), compute B and W's actual **ordered first-hit prefix** counts and P/Q rational masses; determine whether W can reach B. Because W has a=3 at depth8 and B has a=0 at depth11, a nondecreasing, the two true path cones should be provably disjoint. Verify this for reached prefixes.
2. Let b,w be the probabilities to stop Q at B and W respectively. Compute all four rational corner observers M(0,0), M(1,0), M(0,1), M(1,1), both via exact Fraction backward recursion and independent literal ordered-prefix integer DFS. Check mixed four-vector.
3. Solve eP=eQ for a legal b(w), calculate alpha and tP/tQ at feasible endpoints, and test equality to the dual lower bound. Either establish the *whole real interval* with sharp right endpoint, or isolate an exact infeasibility witness. Note that both ties are Q/C; error-balancing or time dominance may behave differently from Stage151.
4. Scan the next dual ray only after any proved endpoint, preserving the precise authority and native-transfer boundary.

## Inputs and executable evidence

Fixed per-run GLOBAL_KNOWLEDGE_V1 main@5a3cc94fb7e833c9f3a5a332d14ff94c1683d65f;
Enterprise Math initial main@14497eb725037b01bf6ef2ec2ff5f82588f2d11d.
Project P000 startup projection blob matched original 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc.
Exact checked source is in this Stage151 directory:
VERIFY_STAGE151.py, INDEPENDENT_ORDERED_STAGE151.py,
SCAN_STAGE152.py, certificate151.json and PROOF_STAGE151.md.

Both author exact Stage151 checkers passed locally, and the exact dual scan passed locally. GitHub saving is a source checkpoint, not remote code execution or mathematical independent review.

Native control task listing: CONTROL_QUOTA.
Native researcher session_start: STATIC_READONLY_SCOPE_DENIED, operation_sent=false.
Thus current active Owner, session/CLAIM, Result and native review remain unknown; do not assume ownership or formal acceptance. GitHub connector principal: awdawmip.

BRC use: preserve positive rational ordered branches and their provenance; iid count compression is limited to observer-sufficient dual recursions. No claim of native X6 embedding.
