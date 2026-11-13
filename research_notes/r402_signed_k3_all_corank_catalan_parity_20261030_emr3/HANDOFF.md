# R402 — Researcher portable HANDOFF / Next precise unit

**Current parent objective:** Enterprise Math / 进取数论，继续从原始 BRC、进取坐标出发构造能够区分模型结构的精确数学结论。本次接续上轮作者侧 R401（固定 r=29 PF₂ 分类）后明确保留的“全余阶 Catalan / 退化点奇偶”问题，转向跨所有正整数余阶的代数定理，不重复 r=29 的有限分类。

**Frozen input/source:**
GLOBAL_KNOWLEDGE_V1 canonical main `a725c591052bc9f146a6f27abc75030181d6da26`; Enterprise Math control main `b8853d39eeb8a38cff2ba77a0fc3d19a452cfeaf`; R401 prior author-side PR commit `afeaff5284df2029c319c48bb7c9e062cc199be3`. Original twelve signed K/J branches identical to R346/R401; only `K3[t²]=-8(1+theta)`, with theta>-1. P000 and ACTIVE worldview unchanged.

**New author-side exact scientific result:** For every integer r>=1 and every theta, `c_(2r) = Catalan_r*(30-16theta)^(2r)`; at theta*=15/8, order of `c_(r+1)` equals 2 for odd r and 3 for even r; for s>=2, order of `c_(r+s)` is 2s. The Turan `T_(r+s)` has order at least 4s. All-uniform claim follows from formal Laurent pole decomposition, not a finite run. See complete research proof `R402_THEOREM_AND_PROOF.zh-CN.md`. Runnable exact verifier `VERIFY.py` and full 9922-byte JSON in `EVIDENCE.json.br.b64` (readable checksum and reconstruction in `R402_EVIDENCE_INDEX.md`).

**Actual verification:** GitHub-source-identical verifier was run locally (Git blob `d4bbffb08a1161275939f89dc64995790d591492`). Received `R402_EXACT_FINITE_CROSSCHECK_PASS`; five exact theta values, ranks 1..8, 40+40 highest-coefficient comparisons, 36 degeneration-order checks, 28 Turan-order lower-bound checks. Additional r<=10 jet path passed; nothing in these bounded runs is presented as universal proof by enumeration. SHA256 EVIDENCE.json `a2e4a304573b98f3cff141e0ab881f8f4f56bfc1eccfd43de0af255022309a26`.

**Smallest unresolved mathematical unit (R403):** Determine whether `ord_(a=0) T_(r+s)=4s` is sharp for every r>=2, 1<=s<r, or construct the smallest exact counterexample. For s>=2, write `d_(r,s)=[a^(2s)]c_(r+s)=binom(r+s,2s)*180^(r-s)*delta_(r,s)`, `delta_(r,s)=[t^r](1-t)(1+t)^(2s)(1+t²)^(r-s)`; check the signed determinant `d_(r,s)^2-d_(r,s-1)*d_(r,s+1)` and odd/even s=1 boundary separately. At even r, `c_(r+1)` starts at a³, not a². No extrapolation from r<=10. Secondary unfinished question: phase threshold eta_r parity limit, no all-r PF₂ theorem claimed.

**Real role / source state:** GitHub account `awdawmip`, writer for this Draft PR. Native service v0.6.11 `research_authority_granted=false`, `executor_binding_configured=false`, `CONTROL_QUOTA=5/5`, `CODE_REVIEW_REQUIRED`; native active Task owner not positively established. **AUTHOR_SIDE_PROOF / EXACT_FINITE_CROSSCHECK_PASS / DRIVER_UNREVIEWED / NOT_ADMITTED / ACTIVITY_REGISTER_PENDING**. No native CLAIM/open/Result/review or official adoption, no independent author-review claim. The PR branch is noncanonical until appropriate review/integration.

**Preservation:** This handoff, proof, verbatim verifier, losslessly compressed actual machine evidence and index were delivered on the existing PR #1708 branch. A readback of each relevant immutable Git blob and PR HEAD is part of the acceptance record. No Google Drive backup used while GitHub working, no credentials or sharing changes.
