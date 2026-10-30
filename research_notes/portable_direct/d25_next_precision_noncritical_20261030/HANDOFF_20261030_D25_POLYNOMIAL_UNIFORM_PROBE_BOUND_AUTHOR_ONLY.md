# D25/LIFT — 多项式更新 D 探针界：作者侧接续

2026-10-30；本文件只记录作者侧中立交付，不是 Source checkpoint / Result / predecessor completion。

**母目标**：在 P000 的原生六轴心跳世界框架下，确定哪些带标签来源、整数 BRC 重数与隐藏共同深度信息能够对指定未来操作和观察安全压缩；最终仍需原生状态、时间、合法操作与观察端口的严格保真映射或最小失败反例。

**本轮新科学单元**：针对辅助 `R^6`（`R=Z/p^L`）、`Q(z)=(z_i-z_6)_{i≤5}`、`h=z_6`、`T_f:z↦z+p^e f(h)e_1`、`U_s:z↦z+p^s δ`、`f∈Z[X]` 次数 `D≥1`，证明 `Q` 加 `D` 个可重置探针 `Q(T_f(U_s^jz)),0≤j<D` 的纤维，严格等于所有 `{T_f,U_s}*` 操作字的未来观察等价。证明使用最高次项消去与整数 Newton 前向差分，不在有限环上除 Vandermonde 行列式。对于每个 `D≥2,s≥0`，`p>D` 与 `f_D(X)=∏_{i=0}^{D-1}(X-i p^s)`、高度 `0,p^s`、`n=L-e=sD+1`，给出前 `D−1` 条连续探针不充分而第 `D` 条分开的精确证人，赋值 `sD`。统一顺序前缀上界不能下降；不声称优化所有非连续或自适应探针方案。

**精确程序与可复现证书**：`d25_polynomial_translation_finite_probe_checker_20261030.py` 执行状态 `PASS`；18组显式普遍最优证人；30组完整有限高度和 `U_s` 周期枚举；1,690条按配置计数来源；102,140次原始整系数多项式未来评估。`p=5,L=2,e=1,s=0,D=3,f=X(X-1)(X-2)`，完整未来观察恰有5类、每类5个带标签高度；前两探针无法分开高度0/1，第三探针分开。全部为辅助模型作者侧精确检查，不是原生 X6 实验或独立评审。

**当前唯一证据正文/可复现材料（作者侧暂存）**：

| 文件 | 字节数 | 原始 SHA-256 | Git Blob SHA-1 |
| --- | ---: | --- | --- |
| `D25_X6_POLYNOMIAL_TRANSLATION_FINITE_PROBE_SHARP_THEOREM_20261030.md` | 7920 | `98a0ee2e6fd3da36828ed14b219f8cf74a2438f7bf2f49bdc957778617bf0f41` | `6245777607ac67cefb484e32c460612b0a9607d9` |
| `d25_polynomial_translation_finite_probe_checker_20261030.py` | 6451 | `2a572f0c95c10cbf44b7da48231c77b98f0b12c9e467b6ab49d38cac34b14e8b` | `ca1e94712da6306225c2278226443756dfc5520b` |
| `d25_polynomial_translation_finite_probe_author_check_20261030.json` | 13752 | `d45eae50da3edb395d24b94c4813eece5e34d6bdbb337e83f9007258a002dec7` | `efcb5c2890ac6ac8ee47367822338b26f450a98b` |

**已可直接复用的前沿**：已在 GitHub PR #1745 的作者材料中保存 `f(h)=h^p` 特殊两探针、部分高度平移阈值与来源重数结果。新一般次数定理不重复这些已完成证明，不改变冻结科学 source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`。

**截至本轮权威核对**：Gateway `0.6.11` `em_status` 返回 `research_authority_granted=false`、`executor_binding_configured=false`、`registered_session_count=0`、Source 控制 `CODE_REVIEW_REQUIRED`，本主体仍没有服务签发的 current session/claim/run。已知历史原请求 `r40_20261029_0840_exact_d25_continuation_read_v1` 和 `emr20261029_1650_source_continuation_read` 多轮读取为 `CONTROL_REQUEST_NOT_FOUND`；没有新建重复请求或猜测尚未暴露的 `recovery_status` typed API。已知 Sites `static_machine_readonly/write_relay_enabled=false`，不授 native mutation。平台当前未提供成功的 Source continuation、checkpoint 或当前合法 writer；这项证据只保存在中立 PR/Library 的作者侧范围。

**P000 精确校验**：账户知识库 `projects/enterprise-math/P000_STARTUP.json` 旧投影声明原始 blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`；本轮 current `enterprise-math` main 的 `p000_reality_foundation.json` blob 为 `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`、schema V5。按项目路由已直接读取 V5 原件而非使用旧投影取代当前 P000；六空间轴加独立时间及观察商需要证书等 relevant 不变量保持。冻结科学 source pin 与该当前控制/P000 文件头指针是不同维度，不因控制更新漂移。

**UR 原始来源**：四文件 V2 的唯一可接受真实归档是大小 94,687 bytes 且 SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`；当前可访问本地挂载、既有 Library 搜索和 GitHub 默认分支检索未取得匹配原件。UR 数学已有作者侧结果，剩余只包括真实原件 recovery 与合法 provenance/writer/checkpoint，不重推数学。

**正式接续和验收**：先在本真实 subject 具备授权后，按 current schema 读 `recovery_status`/原 request receipt，确认 Source 当前 continuation 与 winning claim；如果 seed 为 `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`，先完全读回 `input_artifacts`，`completed_units=[]`，作者草案只记 staging/do_not_repeat。然后对已证明单元补合法 writer/provenance/checkpoint，独立 Driver 做数学实质审阅。真实 native 转移需要明确 `T_native`、允许操作、时间与 `Q_native`，验证带标签来源映射以及 BRC 推前的交换图；不符合时给出最小反例。未知 side effects 使用原 request id 先 reconcile，不重新 CLAIM 或冒用另一对话身份。

**研究与行政状态**：`AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / PORTABLE_STAGED / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`。既有自动研究频率、相位、启用与通知设置不变。后续 PR 发布及 Library 回读的事实须以后续真实回执为准，此文件在本地落盘本身不等于已被持久化。
