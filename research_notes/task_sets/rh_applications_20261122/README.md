# RH 应用研究任务集：六项、四档权重

Taskset: `TS-RH-APPLICATIONS-20261122`  
Parent objective: `OBJ-RH-APPLICATIONS-WEIGHTED-20261122`  
Publisher: `EM-DVR-2D6C6F`  
Prepared at: `2026-11-22T09:47:03.977967+00:00`

按用户本轮“发布不同权重的任务集”指令，将上一轮已保存的RH应用评估转为六个可独立推进的开放研究单元。P0/P1/P2/P3采用现有调度基础权重40/30/20/10；本次只为这六项设置档位，沿用现有等待、方向轮转和可执行状态规则。

## 任务与权重

| 任务 | 优先级 | 基础权重 | 精确任务 ID |
|---|---|---:|---|
| [已知 RH 下完整道路实际输出的净成本与短证书](../../../research_tasks/RS-RH-ROAD-CERTIFIED-NET-COST-20261122.md) | P0 | 40 | `RS-RH-ROAD-CERTIFIED-NET-COST-20261122` |
| [EC49 真实锚点族的素数分母密度与统一供给](../../../research_tasks/RS-EC49-PRIME-DENOMINATOR-FAMILY-20261122.md) | P0 | 40 | `RS-EC49-PRIME-DENOMINATOR-FAMILY-20261122` |
| [稳定匹配的误差、参数规模与有效常数](../../../research_tasks/RS-RH-MATCHING-PRECISION-TRADEOFF-20261122.md) | P1 | 30 | `RS-RH-MATCHING-PRECISION-TRADEOFF-20261122` |
| [Riesel 构造的兼容同余素数供给与实际覆盖收益](../../../research_tasks/RS-RIESEL-GRH-COMPATIBLE-SUPPLY-20261122.md) | P2 | 20 | `RS-RIESEL-GRH-COMPATIBLE-SUPPLY-20261122` |
| [P017 平方窗相关余项中的 RH 输入压力测试](../../../research_tasks/RS-P017-RH-LOCAL-CORRELATION-20261122.md) | P3 | 10 | `RS-P017-RH-LOCAL-CORRELATION-20261122` |
| [因数库存的约数和读出与有效约束](../../../research_tasks/RS-INVENTORY-DIVISOR-SUM-INTERFACE-20261122.md) | P3 | 10 | `RS-INVENTORY-DIVISOR-SUM-INTERFACE-20261122` |

## 科学起点与增量

- 已有稳定匹配族的平方根包络、O(log A)窗口能量、真实骨架/逐层核预算，以及EC49的27/40例子，均作为已保存输入。道路成本研究比较同一实际输出和同一精度；匹配任务研究epsilon与参数代价的新关系。
- EC49新增真实锚点族、素数分母与变动模数；Riesel新增确实兼容原条件的同余供给子问题；P017从G4/Walsh相关前沿开始；库存研究先建立真实约数和接口。低权重探索可交付范围明确的正结果或障碍。
- 六项无相互硬依赖。道路成本可以利用匹配精度任务的后续改进，但可直接从原构造开工。Task书保留可验收目标与输入，方法由研究者自主选择。

## 来源、去重与归属

- 原RH父任务 RS-RH-METHOD-TRANSFER-20261121 / TP2-677F61D1BCF81D4E4FE3 的出版者为EM-DIRECT-B5750A。两项道路任务以CONTINUATION保留谱系，专门采用已知RH输入，保留原无条件相位抵消研究。
- 原生只读请求 rh-taskset-dedup-rh-20261122-0940 于2026-11-22T09:36:20.025454+00:00观察该父任务为HANDOFF_READY / NEEDS_DISPATCH、无当前CLAIM。该观察是父任务去重证据，不是新任务的执行授权。
- P017历史父任务 RS-P017-P018-ANALYTIC-MASS 已SUPERSEDED；新任务固定PR170的90251d026b4d422a98de007f76de2a1e3de9337e G4/Walsh来源（当次观察未合并），没有恢复旧容量/独立密度目标。
- EC49FWS来源95507f064ee46910b32e26d1c49e6df4a05b84fc保留分支/未独立Review状态。Riesel原作者EM-DIRECT-970E1C、库存原作者EM-DIRECT-0CF8AC的贡献与母问题保留。
- 查重读取了当前canonical任务ID/path集合及相关精确任务书；范围是与这批任务直接相关的已保存对象和目标。已有O(log A)、27/40及原有限结果不作为本批新产出。

## 出版与复核

六份任务书使用当前canonical prepare、taskbook dispatch lint、build_record和严格immutable-record audit函数验证。远端按一个原子提交同时包含六份任务书和六份匹配出版记录，采用当前main父提交的非强制CAS；实际发布后按不可变提交逐文件回读。此处记录的是任务出版，不是数学成果审查结论。

当前Driver登记请求：rh-weighted-taskset-20261122-af81-driver-start-v1；激活请求：rh-weighted-taskset-20261122-af81-driver-activate-v1。原报告贡献继续归属EM-DIRECT-8C7F06，本批未将作者复核称为独立Review。

[已有完整RH应用报告](../../portable_direct/rh_impact_20261122_af81e5b398b7/REPORT.md) · [机器可读任务集](TASKSET.json)
