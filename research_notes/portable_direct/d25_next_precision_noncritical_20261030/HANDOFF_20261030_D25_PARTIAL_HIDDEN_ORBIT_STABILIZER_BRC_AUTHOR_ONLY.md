# Enterprise Math / TASK_RESEARCH — D25 部分隐藏平移来源谱接续包

**日期**：2026-10-30。`AUTHOR_ONLY / PORTABLE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`。

## 母目标及当前研究贡献

母目标：在 P000 的心跳世界六轴、分离时间及 ACTIVE 残差保真世界观下，研究真正允许的后续操作能区分哪些来源，给出带标签来源/BRC 整数重数的最小充分观察残差；原生接受必须有真实状态、时间、操作、观察端口、支路和质量的交换保真证据或最小失败来源。

本轮承接已经 GitHub 草案发表、尚非 Source 接纳的多隐藏坐标单纯形探针成果（`awdawmip/enterprise-math#1745`）。此前全单位隐藏平移的 `P_n(f)` 等大小纤维和 `p=3,L=3,e=2,r=2,s=(1,0),f=XY(Y-1)` 非均匀例子不重复证明。新推进：

1. 对**任意函数** `f:(Z/p^n)^r→Z/p^n` 和**任意部分隐藏平移步长**的完整未来观察等价，证明其恰为 `H` 索引的签名相等。
2. 全局精确整数谱：每个签名平移轨道 `Ω` 贡献 `|H|/|P_Ω|` 个完整观察纤维，各含 `p^(er)m_Ω|P_Ω|` 个带标签来源；`m_Ω` 精确统计跨输入陪集碰撞，保留来源恒等式 `Σ size×count=p^(Lr)`。
3. 对任意奇素数 `p`、任意 `e>=1`，`L=e+1`、`f=XY(Y-1)`、`s=(1,0)` 的全来源谱给出一般证明：`p(p-1)` 个大小 `p^(2e)` 的纤维，以及唯一大小 `p^(2e+1)` 的纤维。模3下只使用规范单-T可重置探针时，三条 `j=0,1,2` 是全签名充分且任何两条不足；不扩展为所有操作字或因果策略下界。
4. 作者侧 Python 精确证书 `PASS`，14组有限参数穷举模 `p^n` 完整来源，11组附加完整 `p^L` 来源实际候选更新，未把辅助操作冒充 native heartbeat。

## 文件及不变指纹

建议统一由现有 PR #1745 既有分支 `portable/d25-square-next-precision-noncritical-20261030` 保存于 `research_notes/portable_direct/d25_next_precision_noncritical_20261030/`：

| 文件名 | 原始字节 | SHA-256 | Git blob SHA-1 |
|---|---:|---|---|
| `D25_X6_PARTIAL_HIDDEN_TRANSLATION_ORBIT_STABILIZER_BRC_THEOREM_20261030.md` | 10940 | `355478a31432920dd70468d47cbed77f7876918b90a591723bf8b93c002e6e3e` | `4b505acc682b120dae5ad32680ff7f4fef0fe43a` |
| `d25_partial_hidden_translation_orbit_mass_checker_20261030.py` | 7282 | `5656770b79d25de13152f17287310dd674a52eaf3e996435c1fcb938e30e62ac` | `7761834d37ba05354280febe97e332cbe7087b37` |
| `d25_partial_hidden_translation_orbit_mass_author_check_20261030.json` | 11132 | `556f1558b6a905647248f17f0bbc2f765e1e31171ef16b6c16b33ef0906d3879` | `dcba344e417b6c59a248d9502705984fb057d532` |

本接续文档自己的 hash 由实际发布对象给出，不提前自引用。

运行命令：`python3 research_notes/portable_direct/d25_next_precision_noncritical_20261030/d25_partial_hidden_translation_orbit_mass_checker_20261030.py`。仅 Python 标准库。JSON 会在同目录重生；作者运行的原始 JSON 已保存。

**实际执行总计**：14 配置；1,840 个完整模 `p^n` 来源，108,796 次精确 residue 探针评价；11 配置额外完整模 `p^L` 枚举，22,539 个带标签完整来源与 192,827 次原始候选操作读数；每组 orbit-stabilizer 与独立直接签名谱一致。不是独立审阅，也不是 Source writer 执行。

## Source 状态与写权限边界

本轮实际 `em_status` 为 Gateway 0.6.11：`research_authority_granted=false`, `executor_binding_configured=false`, `registered_session_count=0`, `reviewed_code_gate_passed=false`。Sites 状态回报 `static_machine_readonly`, `write_relay_enabled=false`。现有工具没有可直接调用的 typed `recovery_status`；状态只是该操作的描述，不猜 API 请求封装。按原 `request_id` 读取 `r40_20261029_0840_exact_d25_continuation_read_v1` 及 `emr20261029_1650_source_continuation_read`，再次得到 `CONTROL_REQUEST_NOT_FOUND`，不将其当作已完成或已执行副作用，也不重发 mutation。

本逻辑对话没有可核验的 Source `conversation_id/session_id/session_key/claim_id/run_id/generation/checkpoint_revision`；不能根据相似标题借用其他主体的稳定逻辑 ID，不能把本次 GitHub 材料记入正式 `frontier_notes.completed_units`。如果当前 Source `continuation_seed.state=CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`，必须真实读取全部 `input_artifacts`，以 `completed_units=[]` 做一次 typed `continuation_prepare`；本稿仅能进入当前作者 staging/do_not_repeat 及待合法 checkpoint 输入。没有已核验 Source CLAIM，不运行 OPEN、Result freeze、Driver review、release。

该权限阻断不是 `NO_DISPATCH`。已完成数学只欠合法 writer/provenance 时，应补 writer，不重做推导；当前 Source 未授权，不冒用其他渠道重放被拒 mutation。

## 持续欠项与精确后继

- **原生科学主线**：取得原生 X6 来源/路径/支路、合法更新、时间排序、观察端口、来源权重及辅助到原生映射。对至少一个明确操作路径验证交换或保存最小原生失败来源。既有 `#1559` H0/B0 仍由其实际 Source 负责路径承接；本次模拟程序绝非该原生实验。
- **Source provenance/审阅**：由真实获授权研究主体在获得当前 exact continuation 后，恢复合法 session/claim/open，补这项作者成果及前沿的 Source checkpoint，再由独立 Driver 决定审阅/接纳。本次没有合法 winner claim 或 run 可释放。
- **UR V2**：既有四文件数学不重做；必须从真实本地/已发布来源获得原始 V2 bundle 字节，并同时验证 `94687 bytes` 与 SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`。本轮 GitHub 默认分支哈希搜索、Library 文件名搜索及本地工作区指定长度搜索均未定位真实对象；搜索不构成不存在证明。未发布指针不算持久化。
- **下一可移植科学方向**：带有非均匀原始分支权重及跨时间操作日志时，判定何时由 `(m_Ω,|P_Ω|)` 的**纯来源基数**提升为 BRC 联合来源权重推前的精确交换证书；在原生数据缺失时先给必要/充分条件或反例。避免重复此稿已解的通用陪集质量谱。

保留 P000、适用 ACTIVE 世界观、冻结科学 Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`。本轮没有更改研究任务调度、启用或通知设定，也未新增 scheduler/Actions。
