# Stage153 — ordered-first-hit primal analysis (OPEN; exact dual candidate)

**Research status:** Stage152 AUTHOR_EXACT full-real auxiliary theorem completed and source-persisted on this research branch; Stage153 DUAL_CANDIDATE_ONLY, **not** a primal optimality theorem. No native CLAIM/independent Driver acceptance.

Frozen model: ternary iid N=14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Arbitrary randomized **complete ordered-history** sequential policies. Errors eP=P(decide Q), eQ=Q(decide P); times tP,tQ; minimize max(tP,tQ) with eP,eQ<=alpha. External auxiliary model only; P000/native-X6 does not follow from it.

## Consume, do not repeat

Read the Stage152 source artifacts in research_notes/n14_aux_iid_affine_152_20261026: PROOF_STAGE152.md, VERIFY_STAGE152.py, certificate152.json. The proved real interval runs from

    alpha151 = 18373001785623238325/52808422392537808896
    V151 = 318746112099955105013/26404211196268904448

to the **right-sharp** endpoint

    alpha152 = 18373003413933759925/52808422392537808896
    V152 = 318745538371909741813/26404211196268904448

with dual K152=12844717560/36346217, L152=12768141608/36346217 and slope K+L=25612859168/36346217.

The Stage152 two tied states are B=(11,0,1) Q/C and W=(8,3,3) Q/C. At the endpoint W Q-stop is saturated (w=1); B's Q-stop coin is strictly interior:

    b(1) = 2686983670724537/2714624000000000.

All Stage152 finite Bellman/DFS evidence is author-checked, not native reviewed.

## New Stage153 *dual-only* exact scan

Hold B Q/C equality while treating W as strict Q-stop. Use ray

    (dK,dL)=(-1,-112/129).

Under the frozen Stage152 minimizers, W's continuation-minus-Q-stop gap has strictly positive directional slope

    36346217/13866909696,

so saturation remains locally valid. Scan every nonchosen action in all 680 count states. The smallest positive closure parameter is

    t_first = 500973822/617885689

at new state

    Z=(12,2,2), Q-stop / continue.

A fresh exact full Bellman evaluation at the candidate yields

    K153 = 5994/17
    L153 = 5960/17
    H153(root) = 79691642847444362851/310422953206480896

Exactly B and Z are tied, both Q/C. There are 1238 strictly positive nonminimum gaps, minimum 71917/33841152, zero negative gaps.

**This certifies only the dual candidate.** The equality of errors, primal legal range, tP/tQ ordering, real optimal interval and right sharpness have **not** been proved at Stage153.

## First discriminating scientific task

Compute reached complete-ordered-history first-hit collections for B=(11,0,1) and Z=(12,2,2); they appear incomparable because Z has a=2 whereas B has a=0 and the depth ordering is opposite. Verify this from the strict Bellman policy rather than assuming nominal combinatorial reachability. At both ties, use Q-stop/continue coins b,z.

Compute all four exact observer vectors M(0,0), M(0,1), M(1,0), M(1,1) by two structurally different methods: Fraction backward recursion and literal integer-weight P=(3,1,20)/24, Q=(1,1,10)/12 ordered-prefix DFS. Check mixed four-vector and P/Q first-hit masses. Solve eP=eQ for b(z), legal coin interval, monotonicity of alpha and tP/tQ. Test the dual support equality at both endpoints and prove the *whole real interval* with right sharpness or give the exact obstruction. Do not infer full-history results from a count-only observer without this check.

Preserve BRC positive rational ordered branch provenance and all known P000/native-X6 ontological constraints; this finite external theorem asserts no native transfer.

## Authority, source pins and actual status

Turn source snapshot GLOBAL_KNOWLEDGE_V1 main@43639a1bd021e9c6e90e699fbb7b5021855fbef7; EM main@e5f859b01b76e84cb6b68b899cbe7d6390eb5b83. GitHub authenticated as awdawmip with push permission. Native control tasks -> CONTROL_QUOTA; native researcher session_start -> STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Active owner/CLAIM and formal Source Result remain unverified. This is disjoint SOURCE_ONLY author research; do not overtake an active task or represent branch storage as native mathematical acceptance.
