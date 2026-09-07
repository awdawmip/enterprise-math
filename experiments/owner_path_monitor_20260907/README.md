# 原生路径顺序 × BRC 有限端口 consumer

状态：非 canonical 实验；复用现有 T0/T6，不声明新工具族、Foundation、无界闭式、收敛或复杂度定理。

母题在当前范围内已闭合：**若未来观察读取路径是否曾出现相邻原生反向步，必须在端口消元/路径聚合前保留该观察状态。** 本目录实现有限 graph×monitor 乘积、正长度 excursion 和保留 monitor 边界的有限端口拼接，并与不调用监测器转移的显式路径枚举比较。

## 输入和输出合同

- `Node(label, coordinate)`：非空标签、六个 raw signed 整数。节点标签允许表示已有 routing 状态；不同标签可以位于同一空间 Cell。
- `Edge(label, source, target, step, weight)`：边标签唯一；`step∈{±1,…,±6}` 表示 `±E_i`；权重仅允许正 `int/Fraction`，不接受 bool/float。
- `NativeGraph(nodes, edges)`：有限图，逐边核验两端坐标差恰为声明的 signed primitive step。不把复合对角位移伪装为一步，不增添空间轴。
- `ports`：同一图中明确命名的非空节点子集；不按空间坐标自动合并 routing ports。
- `horizon`：调用者声明的非负整数路径长度界。有限 horizon 不等于高效枚举承诺。

核心调用：

```python
monitor = reverse_step_monitor()
excursions = port_excursion_series(graph, ports, horizon, budget=1000000)
walks = compose_port_series(excursions, budget=1000000)
enumerated = enumerate_port_walks(graph, ports, horizon, budget=1000000)
audit = verify_port_series(graph, ports, horizon, walks, enumeration_budget=1000000)
if audit["status"] == "VERIFIED":
    hist = coefficient(audit["verified_series"], source, target, length, initial=START, final=HIT)
```

每个系数索引为 `(source_port, target_port, length, initial_monitor, final_monitor)`，值是现成 `WeightHistogram`。原生 endpoint 从图端点坐标读出；路径/边标签在输入图与独立枚举 witness 中保留。聚合系数自身不宣称恢复完整来源词。

monitor 有初始 N、最近一步的十二种方向、已命中 H，共十四态。H 吸收；last=a 遇 -a 进入 H。实际调用现有 T6 `family_future_partition_sequence`，得到 hit/nonhit 的两类到十四类，之后稳定。H 与其他态由空后缀区分；last=a 与任意其他非命中态由 -a 区分，因此是该有限观察及全部后缀语言的最小确定监测器。监测状态记录历史，不是新空间或时间坐标。

## 为什么先乘积再消元

excursion 至少一条边，起止均为 port，中间不再访问任何 port。到达 port 时立即结束该 excursion。长度 0 **仅**属于完整路径的 identity。

在 graph×monitor 上先传播正权 histogram，得到 excursion 系数 `E_l`。完整端口路径逐长度满足

`K_0=I`，`K_n=Σ_{l=1}^n K_{n-l} E_l`。

这里矩阵的边界索引同时含 port 和 monitor state；乘法必须匹配前段的末状态与后段的初状态，不能先把 monitor 边界相加。正确性由唯一的逐次 port-visit 切分承担：每条非空 port path 唯一分为此前的完整 port path 和末段 first-return excursion。由于所有 excursion 长度为正，任何固定 n 的切分有限。乘法用 `histogram_serial`，替代用 `histogram_recoalesce`；没有创建新的长度/count/histogram 算术。

核心反例：

`u=(+E1,-E1,+E2,-E2)`；`v=(+E1,+E2,-E1,-E2)`。

四方向权重分别为 `2/3,3/5,5/7,7/11`。两条路径都回到同一空间 Cell，长度 4，方向计数和完整权重 histogram 都为 `[2/11]`；只有 u 命中相邻反向观察。单独闭路图的普通端口 excursion 签名相同；产品监测器的 hit 端口系数分别为 `[2/11]` 与零。观察结果既然不同，就不可能从已经相同的普通签名补回。

未来后缀例：P→Q 的 `+E1` 权重 `2/3`，Q→R 的 `-E1` 权重 `3/5`。P 和 R 是同 Cell 的不同 routing 标签。保留 Q 的 monitor 边界后，P→R 的 hit histogram 为 `[2/5]`；若在 Q 把监测器重置为 N，后缀本身不会命中。把 Q 改为内部节点再消元，P/R 的全部 monitor blocks 保持相同。

## 实际复用与已有接口边界

- `src/enterprise_math/brc_histogram.py`：实际调用 `WeightHistogram.from_weights`、`histogram_serial`、`histogram_recoalesce`。
- `src/enterprise_math/operation_quotient.py`：实际调用 T6 并验证 `2→14`。
- `src/enterprise_math/brc_moment_transfer.py`：测试实际调用 WBRC-T33 `moment_walk_series_coefficients`，逐长度核验忘记末 monitor 后的 0、1、2 阶矩；实际调用 T35 `moment_transition_matrix` 与 `moment_port_kernel_at_z`，在 hidden DAG 的完整 degree-4 excursion 多项式上交叉核验。
- 已检查 `brc_recurrent_ports.py`：其稳定 rational Schur 接口不是本任务的有限 horizon、所有 monitor block 的 histogram 系数接口。这里采用标准有限转移/first-return 动态规划作为 typed consumer，未重复实现矩阵求逆或声称延伸稳定性 theorem。

当前 P000 的六维离散空间、一维时间、120° 原生正角、signed primitives 均为既定前提。本工具只读取一个原生 primitive-step word，不额外假定一步等于某个物理时间刻，也不把“相邻反向”定义成散射、能量或其他尚未给定的物理机制。

## 预算与未完成状态

预算是声明的逻辑工作计数，**不是**墙钟时间或位复杂度上界：产品传播/卷积按参与的 histogram 乘积项计数，显式枚举按独立 path-edge extension 计数。两种计数不可比较为性能结论。

耗尽后返回 `INCOMPLETE`、`complete_through` 和已得到的 partial coefficients。当前未完成长度的系数可能只含部分正贡献；缺失 key 不证明该传递为零。便捷读出 `coefficient()` 拒绝整个 INCOMPLETE 结果，`compose_port_series()` 拒绝不完整 excursion 输入。零预算下的空 partial dict 已纳入反例测试。长度 0 的已知 identity 不被当成全 horizon 完成。

## 外部结果的独立验证

`SeriesResult` 是公开可构造、可通过 `dataclasses.replace` 改写的容器。**`COMPLETE` 标签本身不构成独立验证；`coefficient()` 仅是已有计算结果的便捷读出。** 外部传入或持久化后重新读取的 series，必须针对独立给定的原 graph、ordered ports、horizon 调用 `verify_port_series`。

该验证入口只支持 `WALKS/ENUMERATED_WALKS`：先绑定图及 raw frame、port 标签顺序和 horizon，严格检查各系数的监测状态、整数长度及完整 exact histogram，随后重新枚举原图有限路径并直接扫描 signed words。它不调用 product-monitor 的转移来校对自己，也不信任输入提供的 witnesses。伪造系数、删去非零系数、替换 graph/frame/ports、扩大 horizon 但遗漏较长路径均会被拒绝。

结果分为 `VERIFIED`、`REJECTED`、`UNVERIFIED`。独立枚举预算耗尽只能返回 `UNVERIFIED`，附过程状态 `INCOMPLETE`；即使待验证结果标为 COMPLETE，或其伪系数为空，也不会通过。`EXCURSIONS` 因没有单独实现独立 first-return 枚举，明确不支持核验，返回 UNVERIFIED；不能把其完成标签当成另一种证明。

VERIFIED 绑定的是图/frame、ports、horizon 和全部 monitor coefficient blocks；原输入的运行时预算记录及 provenance witnesses 不在核验范围内。返回的 `verified_series` 来自这次独立枚举，提供已冻结的系数快照用于后续读取。

## 运行与验证

```powershell
python -X utf8 -m unittest discover -s experiments/owner_path_monitor_20260907 -p test_path_monitor.py -v
python -X utf8 experiments/owner_path_monitor_20260907/run_certificate.py
```

真实输出保存在同目录 `validation_20260907.txt`、`certificate_20260907.json`。测试覆盖全部 monitor blocks 的独立路径枚举、u/v 信息损失、跨 port 后缀、hidden cycle/parallel branches、现成 moment/port 接口、零长度、horizon 一致性、预算耗尽、raw coordinate/label/weight 输入、数据冻结，以及独立 verifier 的删项/伪值/scope 标签/预算拒绝边界。

已闭合的是这个明确的有限反向步 consumer。一般 monitor 最小化、多个观察器的有效共享、巨大图的复杂度、任意 hidden access、无限路径总量与收敛仍未处理。没有具体新 consumer 或信息缺口时，不因本次测试通过自动续开一个新的工具族。
