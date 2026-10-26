# R307 — 进取数论研究3：可接续研究交接

Date: 2026-10-26 (Asia/Shanghai)
Research-Activity-ID: RA-R3T11-20261026-NEWTON400
Researcher-ID: EM-DIRECT-R307T11 (locally allocated, not a native MCP research session)
Research mode: author-side independent mathematical unit; no native CLAIM / Source Result / Driver review.

## Frozen authority and upstream

- Account snapshot: awdawmip/chatgpt-global-knowledge main@f92f32e5d65551909fb6826bbbc875ec84deb781 / GLOBAL_KNOWLEDGE_V1. Read 00_BOOTSTRAP.md, OPERATING_MANUAL.md, P000 (startup projection original blob checked), ACTIVE worldview, Math/Code/BRC policies and EM project/TASK routing at this single commit.
- Source control/protocol snapshot: awdawmip/enterprise-math main@55d2534d9f950a7e4db9c72a0e6be547d0c9b97a; docs/PORTABLE_RESEARCH_PROTOCOL.md and docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md.
- Scientific inputs: R305 full ordered six-edge BRC fibre model and rational generating function @fef7b1db71a9884f55de16ad24d94699412a38d1; R306 linear defect strip proof and exact verification @d5a27384074f732a7f26bbc7e40734bd44975b65.
- Separate other R306 author branch proved quadratic bound n >= ceil(5d^2/2). Do not conflate with R306 2<=d<=200 unbounded-n linear strip.

## Completed new science

Set D_d(n)=P_n(+,2-n+2d)-P_n(-,2-n+2d) and T_d=4d+4. Reuse F_d(x)=Q_d(x)/(1-x)^d with deg Q_d<=3d+3. Define polynomial P_d(n)=sum_k [x^k]Q_d binom(n-k+d-1,d-1) and K_s(d)=Delta^(d-1-s) P_d(T_d). New exact identity:

K_s(d) = sum_k [x^k]Q_d(x) binom(5d+3-k,s)
       = [u^s] (1+u)^(5d+3) Q_d((1+u)^(-1)).

1. For each fixed s>=0, K_s(d)=(2^s/s!)d^s+O_s(d^(s-1)) as d->infinity, hence eventually positive. Derived from full Q(x,w)=F(x,(1-x)w) rational kernel by singular-coefficient extraction at w=1. The threshold can depend on s.
2. For s=0,1,2,3,4,5, closed polynomials K_s(d) in R307_NEWTON_DIAGONALS_AUTHOR_PROOF.zh-CN.md are strictly positive for every d>=s+1 (proved with h=d-s-1 polynomial expansions with positive rational coefficients).
3. For all integer 2<=d<=400 and ALL integers n>=4d+4, D_d(n)>0. Complete exact Python arbitrary-precision computation checked all sum(d, d=2..400)=80,199 Newton values positive; minimum coefficient 1. Polynomial/Newton identity extends each checked defect d to unbounded n. This is **not** a theorem for all d.

Actual command: python R307_verify_newton_frontier.py --dmax 400
Actual machine result: EM_R307_NEWTON_TOP_DIAGONALS_AND_EXTENSION_V1 / PASS.
Code original bytes SHA256: 98bf39ef16e18249ab0454355f99ba76a61e4e40e4e209d55e1fde0aa4fda25a.
Evidence original bytes SHA256: 887ebf0b11ff53f7d41cad469bd557025799d158461ad0027f4c69b551116ac1.
The code and actual output are byte-identical to the executed local files at the recorded SHA256 hashes.
Original R306 six-edge DP (0..80, 3111 items) is reused as previous evidence, not represented as freshly rerun here.

## Complete research artifacts

- R307_NEWTON_DIAGONALS_AUTHOR_PROOF.zh-CN.md — full Chinese proof, exact rational identities and six diagonal closed forms.
- R307_verify_newton_frontier.py — exact standard-library checker (no floats or Internet).
- R307_EXACT_EVIDENCE.json — raw complete output from actual run, PASS with exact sampled decimal BigInts and scope.
- HANDOFF.md — this provenance and next-unit package.
Canonical account activity registration (separate from native research CLAIM):
https://github.com/awdawmip/enterprise-math/blob/2fc58c45f2d48259be0e236f01ff0a44dfea51ef/research_activity_records/RA-R3T11-20261026-NEWTON400.json

## Permission and acceptance truth

GitHub identity awdawmip, push/admin permission; author-side artifacts are remote research branch provenance. Native em_control_tasks read returned CONTROL_QUOTA and em_session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Therefore active owner, native Researcher session and CLAIM, formal Result, independent Driver review and mathematical admission are NOT verified. Local RA main record is not native session authority. No change to protected P000 or ACTIVE worldview. BRC reuse: REUSE_APPLIED on ordered six-edge source kernel with complete epsilon/k provenance, not native Cell physics.

## Single next mathematical question

Prove **uniformly for all integers d>=2 and 0<=s<=d-1** that K_s(d)>0, perhaps via a positive two-variable rational coefficient representation; alternatively find an exact counterexample with d>400. The fixed-s leading term (2^s/s!) d^s does NOT control s growing with d; do not extrapolate. If all-d strip is settled, only then connect separately to 28 central effects / N_peak=81 under native provenance and independent review.

Source formal admission should be resumed only with actually verified active owner and native authorization; prior immutable R305/R306/R307 proof/evidence should not be needlessly repeated.
