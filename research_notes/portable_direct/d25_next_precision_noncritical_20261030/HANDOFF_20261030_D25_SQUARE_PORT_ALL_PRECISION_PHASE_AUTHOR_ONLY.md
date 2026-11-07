# Enterprise Math / D25 LIFT — 全精度平方端口观察相图：作者侧接续

**2026-10-30** · `AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / LIBRARY_ORIGINAL_BYTES_VERIFIED / GITHUB_BLOB_VERIFIED / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`。这是一份可移植作者研究接续，**不是** native Source continuation、CLAIM、OPEN、checkpoint、Result、独立Driver审阅或来自其他对话的 predecessor completed research。

## 母目标及约束

继续 Enterprise Math 中来源信息、BRC 和动态观察的保真条件研究。项目 P000 为 ACTIVE_LOCKED；心跳世界原生空间 X6 六轴、时间独立一轴。数学 Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` 冻结，不随控制/文档主线改写。本轮辅助整数环不是原生 X6 状态、时间或观测者的已证明实现，`TRANSFER_NOT_PROVED`。前一作者侧成果在同一个 draft PR `awdawmip/enterprise-math#1745`，已包含 `L=2e+2` 的两份组合证明；当前新增单元严格向全部 `L` 推进，不重做此前作者证明，也不伪称独立性。

## 本轮单元：全精度非临界接触与全单位最小观察数

模型：奇素数 `p`，任意 `L,e≥1`，偶 `d≥2`，单位 `λ`；`P(x)=x+p^eλx^d`，原始两因子 `O(x)=(x+1)(x^-1+1)`，来源为全部带整数身份的单位，未来为 `t≥0` 的实际复合。`a=v_p(d−1)`、`g=gcd(d−1,(p−1)/2)`。

对于 `p≥5` 非临界源（`x mod p ≠±1`），`L>e` 时 `0,1` 时刻碰撞对数为：`p≡3 mod4` 则0；`p≡1 mod4,e>a` 则 `g p^min(L−1,e+a)`；`p≡1 mod4,e≤a,L≤2e` 则 `g p^(L−1)`；其余0。初始碰撞对数 `B=(p−3)p^(L−1)/2`；`L≤e` 时 `C01=B`。未来永久二来源纤维数 `D∞=C01` 当 `L≤2e+a`，否则0。证明使用无截断的严格因子 `H(P(x))−H(x)=[(1+hx^n)^n−1][x^n−x^-n(1+hx^n)^−n]`，使初始碰撞的下一阶赋值**精确等于 `e+a`**；并以 p-adic Teich/exp/sinh 等距计数所有来源。

由已保存的临界全链长两读数引理与本轮非临界定理组合，证明整个单位群最少观察数：`(1,1)` 若 `L≤e` 或 `p∈{3,5},L=e+1`；`(3,2)` 若 `p≡1 mod4, e>a, L>2e+a`；其余 `(2,2)`。其中“任意两个固定时点都失败”已通过有限差分 `D=T−I` 的整值二项式公式证明所有 `Δ` 均存在真实 p-adic 反演对的根，再由 `P^(-u)` 转移到任意预选时点 `u<v`；不是只检查了连续 `0,1`。`0,1,2` 对全单位的未来观察严格充分，因果两次策略用第一次读数确定候选，再选择时间1或2，不把候选推算当真实读取。

**新跨精度整数见证**：`p=5,e=3,d=26,λ=1,a=2`。`L=8` 有3125个永久非临界二来源纤维，`x=17,y=22978` 的 `O0,O1,O2` 同为 `22997,316497,297497`；`L=9` 同样有3125个 `0,1` 时刻碰撞对，但永久二来源纤维数为0，`x=17,y=804228` 的 `O0=804247,O1=707122`，`O2` 分别为 `1078747,297497`。从 `L=8` 到9，永久同型信息等价转为暂时碰撞。

**作者侧精确检查**：26组模环配置、572571个无序非临界逆元对、`C01=10066`、`C012=6555`（逐配置与严格公式吻合）；另32775次后续时点同读检查。13组全单位配置共335052个按配置计数的合法单位来源，比较1至4次原始读数；8组完全状态周期，其余有限时点；10份指定时间差 `1,2,3,5,25` 的双时点碰撞见证。脚本实际运行 `PASS`；这不等于独立数学审核、正式Source实验或原生X6计算。

## 新增文件和原始身份

存储路径：`/EnterpriseMath-Research/`；GitHub PR #1745 的既有分支适用同一个资料目录 `research_notes/portable_direct/d25_next_precision_noncritical_20261030/`。三个原始文件的 Library 首次上传均成功，读回完整文本补齐末尾换行后生成 Git Blob，SHA-1 与本地 `git hash-object` 一致：

| 文件 | 原始字节 | SHA-256 | Git Blob SHA-1 |
| --- | ---: | --- | --- |
| `D25_SQUARE_PORT_ALL_PRECISIONS_NONCRITICAL_CONTACT_AND_GLOBAL_MINIMAX_20261030.md` | 13554 | `12446c759e60e4ccd439e2d031f6cd06527ec9c6ca31095925751cc70a79082d` | `c0c904f7b77605581ad0a64530c5455affa6dee8` |
| `d25_square_port_all_precision_observer_phase_checker_20261030.py` | 9735 | `8a521e023da0fcabf162d1d3e1a5cb9e723850f8d58d7086efa05e54aa7bdb65` | `1477bd1a43e0dca2e2ba937f4c903f5e47747f31` |
| `d25_square_port_all_precision_observer_phase_author_check_20261030.json` | 24199 | `c5a2b52325d7ba15ead16d7cb6e448b769909cac8514b32ff8e798381b0ea2b9` | `87188a3c03a50bd74d53c8610fa4f23bc0b2942b` |

新增数学采用当前作者原始材料，没有新的外部独立审阅。PR 分支存在不代表任何正式科学准入或主分支合并。

## Source 可恢复状态与原请求

2026-10-30约05:43 UTC 原生只读 `em_status`：Gateway `0.6.11`，`research_authority_granted=false`、`executor_binding_configured=false`，控制同步 `CODE_REVIEW_REQUIRED`，站点身份 `static_machine_readonly`、`write_relay_enabled=false`。本次 `em_checkpoint_list` 实读 `ACCESS_DENIED`。原历史请求 `r40_20261029_0840_exact_d25_continuation_read_v1`、`emr20261029_1650_source_continuation_read` 按原ID读回 `CONTROL_REQUEST_NOT_FOUND`。可见API中没有可直接调用的 `recovery_status`；`ordinary_chat_recovery` 只是 `em_status` 中的协议说明，不能冒作本 subject 的已读 Source 拥有权。当前实际平台 `conversation_id`/服务 `session_key`/winning claim/run/request 均无可验证绑定，故没有新身份、CLAIM、OPEN、continuation_prepare 或正式 Source checkpoint，也没有借用前一真实对话的身份。

如未来 Source seed 返回 `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`，其输入仅为当前任务初始材料；须完整回读后 typed continuation_prepare 且 `frontier_notes.completed_units=[]`；此作者稿仅在 staged/do_not_repeat 范围，不转为 predecessor completed research。未经精确 continuation/claim 确认不得重复登记和重放请求。

UR V2 原始四文件 bundle 的恢复门槛仍是**同一真实对象**94,687字节、SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`；本轮本地挂载文件无这一精确大小对象，GitHub默认分支按完整哈希字符串搜索未命中，不能推断所有仓库/历史不存在。已完成UR数学不重做，仅需合法原件恢复、writer/provenance/checkpoint。原生H0/B0 p373是独立实验路径，支持issue `#1559` 本轮仍为OPEN、无实际接管证明。

## 下一精确动作、验收与权责

1. 只在当前实际 Subject 获得有权 Source continuation/正式胜出 CLAIM 后，读取本轮已保存的三份原始材料，补充已有证据的 provenance 和合法 writer/checkpoint；Source CAS 回读并交**真实独立** Driver。默认不要重算本文证明或把Git PR充当Source。
2. 后继最小数学单元为**任意 `L,e` 临界球的完整纤维整数大小谱**（现有全链长双读数引理和 `L=2e+2` 谱已经完成，不能重复），或原生X6保真交换图严格成立条件/反例。正式领取先消费跨流 checkpoint，以 Source 任务分派/Owner 为准，避开 Research1 J1/J2 未 CLAIM 重复区。
3. UR bundle 须恢复真实 bytes 并以所给两个值验收；p373 原生 H0/B0 须实际源程序、秩、Frobenius、Green/Hesse/κ/Delta−R 证据，便携模环不能替代。
4. 调度频率、相位、启用和通知保持；P000/ACTIVE 世界观及冻结数学 pin 不写改。不创建scheduler、Actions或托管cron。
