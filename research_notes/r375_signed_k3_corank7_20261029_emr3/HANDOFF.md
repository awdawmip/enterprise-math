# R375｜可移植研究接续（作者侧，非 Source CLAIM）

研究增量：原始十二项带符号 BRC K/J，单负支路 `K3[t²]=−8(1+θ)`，θ>−1；七余阶15项原始 D 观察的 Newton 序列 PF₂ iff `−1<θ≤ρ7`，`ρ7` 是 R375_PROOF 中 `c0` 的唯一根 `(126/125,1009/1000)`，近似 1.00895127386。R374 σ6<0.902，所以前七阶共同区间仍由 σ6 控制。本研究不以待独审 R348/R363 无限抽取为前提；不能扩张到原生 X6。

原始输入：PR #1592 的 `r346_unbounded_interior_tp2_corank301_20261028_emr3/R346_verify.py`（`K,J` 完整12项正负支路）；`r369_signed_k3_branch_top_catalan_20261029_emr3/R369_check.py` 是额外精确点交叉路线。仅变动 K3 的既有 t² 负系数。

复现：在包含这些既有源文件的 PR 分支执行 `python research_notes/r375_signed_k3_corank7_20261029_emr3/R375_verify.py --independent`。程序将写入完整的 `R375_EVIDENCE.json`，应返回 `R375_EXACT_PASS`、34个多项式/598个严格正 Bernstein 系数、45个独立有理点系数等式、15项原始差分多项式 SHA256 `de6539567f5129ec656ee0caa871c92baaad89eb658a49548bdfbd727456e2e8`。由 `R375_PROOF.zh-CN.md` 给出符号证明和完整连续参数域覆盖，机器证据文件含全部系数。

状态：`AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED`。原生 Sites research_authority_granted=false、当次 Owner 读取 `CONTROL_QUOTA`；没有原生 CLAIM、正式 Source Result 或独立 Driver 审阅。GitHub 只是科学证据来源保全。固定全球知识读取 `main@cb56d78d5f8109f05c0510686677a238aa8d2cbf`；EM控制 `main@919f879a4b29e686117930e148bbd19b722317f5`。P000/ACTIVE worldview 保持不变。

**下一最小单元**：r=8 的17项原始 D 观察是否在全部 `−1<θ≤σ6` 上 PF₂？优先对整段求全部 c_j/T_j 的精确 Bernstein 证书；若失败，隔离最小参数阈值并给单一精确有理反例。并保留 R363 全指标抽取独立审查。
