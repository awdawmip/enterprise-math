# Stage276–277: two adjacent exact Bellman faces (author evidence)

Date: 2026-10-29. Status: **PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**. External ternary IID N=12 sequential-decision auxiliary model only; neither P000 native X6 nor canonical Source theorem admission. This authored research is not an active CLAIM, formal Result, independent Driver review, or authority to edit protected worldview.

Frozen source reads:
- GLOBAL_KNOWLEDGE_V1: `awdawmip/chatgpt-global-knowledge main@6629bd6fe79d111d72f54b1b01ec1e031254bf64`.
- Enterprise Math: `awdawmip/enterprise-math main@3168a61827f6ae43f20d501cadbb02fa2767fd97`.
- Prior author frontier: Stage275 at `61863c12dd7f3faada4963950c68f508c4211b3b`, same Draft PR #1571.
- Native service read reported v0.6.11, `research_authority_granted=false`, `CODE_REVIEW_REQUIRED`, active control jobs 5/5 and no verified owner; no native Source mutation attempted.

## Novel exact results

For P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=12 and arbitrary randomized **full ordered-history** policies:

**Stage276**:
- Caps `a=1162027955941/15850845241344`, `b=868777330255/1114512556032`.
- `V12(a,b)=19001515155589573655/3257327614233673728`, strictly sharper by `3508358828125/203582975889604608` than the previous upper bound.
- Bellman multipliers `lambdaP=2145488384/11690591`, `lambdaQ=1072744192/11690591`; `H=16434433593089254321/180962645235204096`; exactly two ties at (0,0,5) and (0,1,11).
- For **every real** (a,b) in [0,1]^2, `V12(a,b)=H-lambdaP*a-lambdaQ*b` iff (a,b) belongs to the strictly convex non-parallelogram face `R276`, area `19622268829345703125/103511519796081828298752`; shares full W–X boundary with Stage275.
- Exact nested-history randomized domain `0<=r<=1; 0<=k<=5+r` (S reached on 5/6 ordered prefixes). Exact positive primal mixture matches the global dual bound.

**Stage277**:
- Bellman multipliers `lambdaP=8245757952/44495173`, `lambdaQ=4104296772/44495173`; `H=7860156606936445891/86094494776590336`; exactly two ties at (0,0,5) and (1,2,8).
- Nested-history domain `0<=r<=1; 0<=k<=145+10*r` (S reached 145/155 ordered prefixes).
- Strictly convex full-real equality face `R277`, area `1357884918212890625/207023039592163656597504`; shares entire U–V edge with R276, interiors disjoint.
- For `a=674027955941/15850845241344`, `b=937402330255/1114512556032`, the exact global optimum is `V12=541791009235/92876046336`.

Both are **author-level exact derivations** with full-primal/dual proof; they are not independently admitted theorems.

## Files, completeness and reproducibility

Files are separately UTF-8 readable in this GitHub directory and also preserved as a single compressed archive:
- [Full mathematical proof](PROOF_STAGE276_277.md), 10,787 bytes; SHA256 `e50df2842494c3211d98bace1d8323cf304113eb50556fd253608b9be2f7d6c7`.
- [Executed exact Fraction checker](REPRO_STAGE276.py), 9,146 bytes; SHA256 `97742e85e810dbddad6b40ca334f13dd3b13355ecdfddce354386e62d68271be`.
- [Recorded executed stdout](REPRO_STAGE276_277_EXECUTED_STDOUT.txt), 3,030 bytes; SHA256 `8ed5c6bd6bbb5dee687327429142434a8a4ff905f19f93d2bd23d9764fd3df3d`.
- [Stage278 research handoff](NEXT_TASK_PACKET_278.md), 2,872 bytes; SHA256 `e89647756f44230ebd98fad140b099026b6cd9f2a717aaf64f8b8eb9474eb6b0`.
- [Complete four-file .tar.xz archive](STAGE276_277_AUTHOR_EVIDENCE.tar.xz), 9,484 bytes; SHA256 `d387f11f08e0822a8698cae389851d0d962fa4fc165e8e37b7ce22dfa152098f`, Git blob `091ead981ccabba30e47e333baf5f105a22b2c6e`. Locally `xz --test` passed.

Run `python REPRO_STAGE276.py` (Python standard library only), or `tar -xJf STAGE276_277_AUTHOR_EVIDENCE.tar.xz` then run the extracted checker. Actual sentinels: `STAGE276_EXACT_ALL_REAL_FACE_PASS`, `STAGE277_EXACT_ALL_REAL_FACE_PASS`. Each exact Bellman pass covers 455 states, 1,274 legal action costs and 817 strict gaps. Independent unmerged full-word P/Q DFS: Stage276 four policies 42,616 nodes/28,412 terminal histories; Stage277 four policies 43,516 nodes/29,012 terminal histories; both source total termination masses exactly one.

BRC-compatible reuse: rational source weight, ordered path identity and multiplicity. Count compression is justified only for the declared IID Bellman future suffix law and observer; no native-X6, sign/phase or infinite horizon transfer is asserted.

Next independently actionable task: [Stage278 packet](NEXT_TASK_PACKET_278.md), seeking the next adjacent exact face and the separately typed P000/native-X6 BRC observer bridge, with original assumptions preserved.
