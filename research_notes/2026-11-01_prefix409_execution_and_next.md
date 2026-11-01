# PREFIX-409 — 执行证据、来源、权限与下一问题

日期：2026-11-01。任务：进取数论研究6 / portable author-side math research。成果等级：AUTHOR_SIDE_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING。未获得 formal CLAIM、Result、Review、Foundation 准入。

## 本次新证明范围

原始五 Port 外部复线性模型，规范 I1=1、I2=1、Cu=2 严格准确；I3∈[0,10^-6]，Cv∈[1−10^-4,1+10^-4]，I5∈[709/32−10^-4,709/32+10^-4]，I4∈[41−κ,41+κ]。经完整正负支路及连续复来源判定得到最优且可达到的 κ*：

```
T* = 2977473/3922000 - 61*sqrt(14890729919)/9805000
  = small root of 196100000000*T^2 -297747300000*T +6389
κ* = 4-(792/10000-176*T*)/61
   = 15171031/2451250 -22*sqrt(14890729919)/1225625
   ≈ 3.998701701255273162645
```

`κ>=κ*` 当且仅当存在相干复来源。显式最优见证 `u=i, v=(10^-4−T*)/2 + i(39T*−84×10^-4)/61`，正好达到 Cv、I5 两个窄观察区间的上端。当 Cv、I5 **准确** (η=0) 且 β<14884/9805 时，最优阈值为 κ=4。证明细节在本次主研究文档中，不能将此有条件结果扩充为全部六项带噪的通用定理。

## 实际执行、独立交叉验证

本轮在本地研究环境实际执行了以下源码（远程均有对应 GitHub 原文）：

```text
python3 prefix409_exact_joint_threshold.py
PASS_PREFIX409_EXACT_NARROW_CV_I5_SHARP_ALGEBRAIC_THRESHOLD
python3 prefix409_independent_fraction_port.py
PASS_PREFIX409_INDEPENDENT_FRACTION_ORIGINAL_A_RATIONAL_NOISY_WITNESS
```

主检查器从原始 A 的前3行逆矩阵出发，验证两支路精确恒等式、二次根式、根隔离、有理导数界、最大强度单调性、负支路排除、代数见证全部等式；独立 Fraction 检查器不依赖 SymPy 或复端口消元公式，直接对原始 A 进行有理复数高斯消元，并计算以下真来源：

```text
u=i
v=2499/50000000 -69i/500000
I3 = 53855001/2500000000000000 < 1/1000000
Cv-1 = 249953855001/2500000000000000 ∈ (0,1/10000)
I5-709/32 = 1948654315053/20000000000000000 ∈ (0,1/10000)
I4 = 5781452403855001/156250000000000
κ_witness = 624797596144999/156250000000000 ≈3.9987046153
```

作者侧全部 PASS 不等于独立数学审阅；解析全称证明来自 Banach 压缩和有理单调性，不由有限案例枚举代替。没有执行原生 typed BRC/X6 或全六项带噪 CAD。

## 固定来源与权限实读

- GLOBAL_KNOWLEDGE_V1 规范快照：`awdawmip/chatgpt-global-knowledge main@aa0cb116abe430e33dc4db4b8a72210160b5dd97`，本轮全局相关读取均固定在该 commit，原始 P000 与启动投影 blob 匹配。
- Enterprise Math 输入快照：`awdawmip/enterprise-math main@a673d9c9852957727a17317b223423451f48f6a1`；此前 PREFIX-408：`ca3a36728e8452c131b82a03bd7988c4a492ce3c`。
- 已读规范：全局 00_BOOTSTRAP / OPERATING_MANUAL / ACTIVE 我眼中的世界；项目 AGENTS / 原生 P000 / HEARTBEAT X6 / PORTABLE_RESEARCH_PROTOCOL / AUTONOMOUS_RESEARCH_OPERATIONS。
- GitHub 认证用户 `awdawmip`；原生企业数学服务 0.6.11 `research_authority_granted=false`；本次活跃 owner 只读查询 `em_control_tasks` 原样错误 `CONTROL_QUOTA`，因此没有核验当前 owner、没有真实 CLAIM、没有独立审阅身份。
- BRC 优先接口：`COMPOSE_APPLIED`（来源、支路、复相位、联合观察残差保真），并非 `REUSE_EXECUTED`。静态复模型不证明 P000 的原生 X6、三维切片或 typed BRC 动力学。
- 相关已公开框架：Candès/Strohmer/Voroninski PhaseLift arXiv:1109.4499；Huang/Li coded diffraction PhaseLift arXiv:2608.02450（2026-08-03）。随机衍射模型与这里的固定五 Port 不同，不进行错误对比。

## 保存与下一研究动作

GitHub 本轮文件应以最终提交可复核的 readback 为准；本地另保存包含扩展中文证明、执行源代码、原始日志、结果 JSON、SHA256 清单的完整资料包 `PREFIX409_COMPLETE_RESEARCH_EVIDENCE.tar.gz`，压缩包 SHA256 `f5967bb30a24dfb177b793c33cfb142a28ddac44e7b59d7afba1aa1949cd3391`。

后继 PREFIX-410：将 I2、Cu 同时扩展为有理非零误差、保留 Cv/I5/I3 的联合窄误差，确定最优 κ*(ε) 的精确或带证书界，特别研究原切点引起的 O(sqrt ε) 方向不稳定；证书需保留 u 共轭分支、v 来源与全局相干 rank-one 关系。原生 typed BRC 与 P000 X6 桥接继续单独要求证明。
