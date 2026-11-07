# D25/LIFT 作者侧接续 — 持续标签的二源 BRC 时间矩

日期 2026-10-30。母目标：在 P000 六轴心跳世界的真实来源、时间、观察与允许操作下验证 BRC 商的未来保真，或取得最小原生带标签失败见证；科学 Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` 不变。本单元与前轮作者侧结果均属于当前作者 staging，Source 未验证其为 predecessor `completed_units`，因此若以后 seed 状态为 `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`，`completed_units=[]`，不可改填本草稿或 PR 已存材料。

## 本轮新增精确数学

- 对二源二进制观察和**不等整数来源总质量** `(s1,s2)`，在固定两通道边缘下全部相关正整数核恰为 `J=P+k(1,-1,-1,1)`，其中 `-min(P00,P11)≤k≤min(P01,P10)`，该整数 `k` 是必要且充分的双来源耦合差值坐标。
- 当共有标签只选一次、跨时间**保持不变**，给定标签独立重复抽取观测时，完整 t 步历史 `H_t=Σ_l w_l(P+k_l Z)^{⊗t}`；两个隐藏类型在 `t` 步历史观察下相同 iff 它们加权 `k` 矩 `M_j=Σ_l w_l k_l^j` 对全部 `j≤t` 相同。未来所有时间的最粗充分隐藏残差是 `λ(k)=Σ_{l:k_l=k}w_l`；统一有限证书 `t*=min(K-1,2|B|-1)`。
- 对权 `(1,2)`、`P=(4,4,4,4)`，两个隐藏类型 `k=(2,-1)` 和 `(0,0)` 初始、单步和单来源边缘完全相同，持续标签二步历史却相差 `6 Z⊗Z`，原始 `L1` 差96、每边历史整数总量768。每步重新抽取标签时二步观察相同，故标签生命周期必须保留。该证明不重复此前的通道数高阶独立性反例。
- 标准库精确 checker 对256个边缘配置枚举692个可行联合核，23,814次时间矩/历史比较，全部 `PASS`。经典列联表与矩问题思路不称原创新数学方法。

## 当前证据与未落定点

见 `D25_BRC_PERSISTENT_SHARED_LABEL_BINARY_COUPLING_MOMENT_HIERARCHY_20261030.md`、`d25_persistent_shared_label_binary_coupling_checker_20261030.py`、`d25_persistent_shared_label_binary_coupling_author_check_20261030.json`。在实际 GitHub 提交及回读前均只算本地文件；提交后以回读 commit/blob 为准。

2026-10-30T15:42Z 本研究员读到 Gateway 0.6.11 `research_authority_granted=false`、`executor_binding_configured=false`、`control.state=CODE_REVIEW_REQUIRED`、新 job 容量 5/5；Sites 为 `static_machine_readonly`，`write_relay_enabled=false`。两个历史 ID `r40_20261029_0840_exact_d25_continuation_read_v1`、`emr20261029_1650_source_continuation_read` 已按原 ID 读回 `CONTROL_REQUEST_NOT_FOUND`；自己 `em_checkpoint_get(line=TASK_RESEARCH)` 返回 `ACCESS_DENIED`。当前连接未暴露独立 typed `recovery_status` 调用工具。`session_id/claim_id/run_id/packet_request_id/continuation_seed` 均未获 Source 核实，不新造身份、不声称 NO_DISPATCH，不重发受拒写动作，也不创建 formal checkpoint。

UR V2 四文件真实 bundle 应满足同一对象94,687字节及 SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`；尚未见到核验对象，既有 UR 数学不重做。真实原生 X6 固定 heartbeat 程序在2026-10-30读取的 `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json` 仍为 `null`，不能由本辅助模型代替。

下一精确动作：权限运维按自己的当前 Source 绑定路径恢复真实研究执行者身份与权限；本 lane 后续先读 exact continuation/原请求回执并据 schema open/resume/checkpoint，已证明数学仅补 provenance 和独立审阅。科学上取得本机原生共享标签是否跨事件持久、核的整数边缘与时间操作定义，检验上面的矩证书并保留最小带标签六轴反例（若违反）。保留本 lane 原有频率、相位、启用和通知行为，不变更 P000、ACTIVE 世界观或冻结 pin，不新增调度器、Actions或托管 cron。
