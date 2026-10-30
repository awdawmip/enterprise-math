# Enterprise Math / D25 LIFT — 全精度临界来源谱作者侧接续

**日期 2026-10-30；角色 TASK_RESEARCH；状态 `AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / PR_PUBLICATION_PENDING`（本地写稿时）。** 此为**同一既有作者研究流的可移植材料**，不是 Source continuation、predecessor completed research、Research Activity 登记、CLAIM、OPEN、Result 或独立 Driver review。

## 母目标、权威和冻结范围

研究进取数论的来源保真、BRC 合法商以及观察操作的精确可识别性。复用 `GLOBAL_KNOWLEDGE_V1` main@`d81efb6ab014935b49d4da1d824b126ef82ad480`（2026-10-30本轮已读入口和相应角色/数学路由）；项目 `p000_reality_foundation.json` 为 ACTIVE_LOCKED，空间原生 X6 六轴、独立时间一轴。冻结**科学** Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`，不随 Gateway 控制读取 pin、Git main 或 PR 分支改变。所有本文 `Z/p^L` 证明仅属辅助模型，原生 X6 保真映射 `TRANSFER_NOT_PROVED`。

## 最新不可变作者侧研究前沿

现有同一作者 PR [#1745](https://github.com/awdawmip/enterprise-math/pull/1745) 在本轮初始 head `5dac481392abd5b9cd9183ab5a5c88c2ec10453b` 已保存**全部奇素数、全部 L,e 的非临界接触及全单位最小观察数**，以及此前 `L=2e+2` 临界来源谱。上一最新作者侧 handoff：`research_notes/portable_direct/d25_next_precision_noncritical_20261030/HANDOFF_20261030_D25_SQUARE_PORT_ALL_PRECISION_PHASE_AUTHOR_ONLY.md`，本轮已完整读取。现新增的实质不同单元是**任意奇素数 p、任意 L,e≥1、任意偶 d≥2、单位 λ 下，两临界球的完整未来纤维大小和类别数**。

设 `c=ceil(L/2)`, `m=max(0,L-e)`, 每个临界球的平方坐标 `z=u/sqrt(1+u)` 是等距双射。`x~∞ y` 等价于 `z(x)^2=z(y)^2 (mod p^L)` 和 `z(x)=z(y)(mod p^m)`。对于 `1≤t<c`：若 `t<m`，每类 `F_t=p^min(t,e)` 个来源，类数 `N_t=(p-1)p^(L-t-1-min(t,e))`；若 `t≥m`，每类 `F_t=2p^t`，类数 `N_t=(p-1)/2*p^(L-2t-1)`。零平方层每类 `F_*=p^(L-max(c,m))`，类数 `N_*=p^(max(c,m)-c)`。**这些均为每一个临界球的确切整数数目**；全临界类数把两个球相加；如果不同层相同大小则累加其计数。此前非临界完整未来1/2来源谱只复用、不重算；结合两者已有全单位完整未来整数纤维谱。

关键新结构：当 `e>floor(L/2)`，完整未来仍可能保留两个逆根球，出现 `2p^t` 来源纤维。`p=5,L=5,e=4,d=2,λ=1` 的实际精确证书：两个临界球总计 **100类×10、4类×50、2类×25**，来源守恒1250。原始反演对 `(6,521)`,`(26,601)` 的初始和更新观察分别均为529、629。BRC解析器保留 `source_id/s/t/z/m/observer/time/provenance/integer multiplicity`，先证全未来等价再商掉重复来源，`COMPOSE_APPLIED`。

## 精确计算、可复现材料

本轮直接执行了 checker：**420组** `(p,L,e,d,λ)`，`p∈{3,5,7,11}`，各精度的全部带标签临界来源，逐层谱及 `(O0,O1)` 与精确同余等价的纤维集一致；**21组**进一步检查真实多项式状态置换全周期内的每个纤维观察相等。共111,768个按配置计数来源、439,032次实际双因子观察、481,662次多项式更新，全部断言 `PASS`。数值覆盖不外推成一般证明；理论的任意量词由证明的因子恒等式、等距坐标和两根球分类支撑。此前所有来源的其他作者/同作者证据仍独立保存，无本轮“独立复现”主张。

| 文件（相对本研究PR目录） | 原始字节 | SHA-256 |
| --- | ---: | --- |
| `D25_SQUARE_PORT_ALL_CHAIN_CRITICAL_FIBER_INTEGER_SPECTRUM_20261030.md` | 10438 | `82c1e36ea63f17e59729b0d240271b4daf137e5408bcaf32254da0388c8dc2c1` |
| `d25_critical_all_precision_fiber_checker_20261030.py` | 6555 | `4f09a9be9078e1d219186ffb5c4e355a71cb44ae5feeba47c724ab363fb81a43` |
| `d25_critical_all_precision_fiber_author_check_20261030.json` | 257673 | `d81107ab5048d790f345fb1ff8da2b20d364b984ee91f20d92068e971f962f5e` |

发布目录：`research_notes/portable_direct/d25_next_precision_noncritical_20261030/`。此表由本轮本地原始文件计算；只有**GitHub 实际写入后对所读 blob/树/提交的核对**才能升级 `PR_READBACK_VERIFIED`。PR Draft 是研究交接，不代表 Source 业务准入。

## Source 回执、主体和欠项

本轮 `em_status` Gateway `0.6.11` 的直读字段：`research_authority_granted=false`, `executor_binding_configured=false`, `source_sync.control.state=CODE_REVIEW_REQUIRED`; 站点 `static_machine_readonly`, `write_relay_enabled=false`，允许的 scopes 为 `em:access,source:read,control:read`。`em_checkpoint_list` 读返 `ACCESS_DENIED`。对原请求 `r40_20261029_0840_exact_d25_continuation_read_v1` 和 `emr20261029_1650_source_continuation_read` 的原 ID reconcile 调用被本站点边界以 `STATIC_READONLY_SCOPE_DENIED`、`operation_sent=false` 拦截，**未触及 Source 原请求状态**；本轮无新的 Source 副作用。当前实际逻辑 conversation_id、session_key、winning claim、open run 和目标请求 receipt 均 **UNKNOWN / UNVERIFIED**；没有假设前一逻辑对话的 ID 或拥有权，没有调用 Source continuation_prepare/dispatch/claim/open/checkpoint。`recovery_status` 是 `em_status` 中的协议说明，当前连接没有暴露可调用的自身只读投影，不据此认定“空队列”。

若未来 exact Source continuation_seed.state=`CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`，须完整读取其 input_artifacts，然后 typed continuation_prepare 且 `frontier_notes.completed_units=[]`；当前稿件为 author staging/do_not_repeat，**不写进 predecessor completed_units**。正式 writer/provenance/checkpoint 仅在自己合法 Source subject/session/winning claim 确认后补已有证明，不重做数学。严格审阅须由真实独立 Driver 完成，不能以新会话名义自证独立。

UR 四文件 V2 原件要求**同一对象**大小 **94687 bytes** 与 SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`；本轮 `/mnt/data` 实际文件大小查询没有候选，Library 的指纹文本查询只发现接续说明，尚不能核验原始字节。不可把分散上传、草稿、PR 说明或历史指针算为原件。已完成 UR 数学不重算。原生 H0/B0 原类 p373 实验由 [Issue #1559](https://github.com/awdawmip/enterprise-math/issues/1559) 追踪，2026-10-30本轮 GitHub Issue 读取为 OPEN，未找到真实负责执行者；下一步需合法 native evaluator、原始 [X]U mod139129、Frobenius/eta、秩与 κ/Green/Hesse 证据，并经独立验收，不能由模环 toy 证书代替。

## 接续动作和验收

1. **科学下一单元（尚未执行）**：先核对跨流 Source/独立证据后，最小研究对象选择不同二次平方端口 `k=r²` 的信息保真与反演来源重数是否在合法变换下保持，或构造原生 X6 时序/观察者交换图的必要充分条件/精确反例。不要重复本稿任意精度临界谱与上一份非临界谱。
2. **正式 Source 下一动作**：在研究者授权/绑定恢复、当前实际 session 和 exact continuation/claim 校验获胜后，回读 PR 已保存的证明、checker和JSON；对已有结果补 writer/provenance/checkpoint，在正确的 Source head/CAS 写后回读，再路由独立 Driver。不能绕过静态只读 Sites 当前拒绝，更不能借旧 identity 变更通道重放。
3. **UR 与原生**：恢复真实 V2 bundle 的两项 byte 证书后仅补 writer/provenance；H0/B0 支持实际执行者和原生实验 receipt 尚待完成。
4. **既有自动任务**：保留频率、相位、启用状态与通知行为。不新增 scheduler、Actions 或托管 cron，不变更 P000、ACTIVE 世界观与冻结科学 Source pin。
