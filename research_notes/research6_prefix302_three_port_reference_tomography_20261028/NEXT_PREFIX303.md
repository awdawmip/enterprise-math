# PREFIX-303｜固定五 Port 基础读数上的最少额外相干参考

上轮完成：对于 PREFIX-299 的 S4/S7 全部6+6高斯整数 Port 左轨道，已证明固定 E/C 加**任意**一个保留 Port 的复振幅可逆地确定三来源 Q(i) 态。仅加入独立固定参考 1 和 i，在这三条 Port 上各观察 Q0/Q1/Qi 的九个带来源 BRC 正质量，可精确恢复全部来源；36个核耦合系数无零，统一下界 |T_j|²≥8，若自适应选最强 Port 则 min max_j|T_j|²=68，结果全部在 PREFIX-302 中解析证明及实跑核验。不能重复 PREFIX-298/299 的旧轨道枚举。

**第一可执行问题：** 固定已有五个 Port 的无参考基础质量全部可读（不计为额外成本），允许为某些 E/C/R_j 选择固定标签的独立参考 1 或 i，每种添加一个 `|z+r|²` 新读数。对 S4/S7 的12类分别寻找**使整个 Q(i)^3（或声明的有限 C4 来源字母域）全局单射**的最少额外参考读数。必须区分 (a) 全体 Q(i)^3 的严谨代数/实代数结论与 (b) 216元有限来源字母集上的穷尽。给出可复现的构造/下界、显式输入碰撞证书、哪些 Port 选择适用；不能由局部 z=i/-i 反例径直推断全仪器最优成本。

**第二可执行问题：** 研究 K0 五元质量商对各 S4/S7 M 的非 C4 额外等价类，给出一对不处于同一全局 C4 轨道但五 Port 完整基础质量相同的 Q(i)^3 状态，或证明在指定有限域内不存在；保持所有来源和逐 Port 标签。未知差异保留 UNKNOWN。

**原生接入：** 对真正 Source 签发的 `model_law_id`、合法 Detector 门集和未同步参考来源的可达性进行接口核查；对 X6 原生 Cell、场、联合来源、边界、独立时间及测后态提供明确嵌入/读出与未来组合保真合同。不得将 Q(i) 三源辅助模型或外部相干参考自动提升为原生物理规律。

**证据/执行：** 精确输入 `research_notes/research6_prefix299_rank2_left_orbits_20261027/RESULTS_PREFIX299.json`；当前证明 `research_notes/research6_prefix302_three_port_reference_tomography_20261028/PREFIX302_THREE_PORT_REFERENCE_TOMOGRAPHY.zh-CN.md`，源码 `research_notes/research6_prefix302_three_port_reference_tomography_20261028/verify_prefix302.js`，结果 `research_notes/research6_prefix302_three_port_reference_tomography_20261028/RESULTS_PREFIX302.json`。运行 `node verify_prefix302.js` 复核。现有成果均为作者侧 `UNREVIEWED / NOT_ADMITTED / NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION`，原生 Owner/CLAIM `CONTROL_QUOTA` 未核实，正式研究会话/RA 不假定已注册。
