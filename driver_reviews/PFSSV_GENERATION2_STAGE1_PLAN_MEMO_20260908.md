# PFSSV Stage1 冻结计划：有界独立审查

2026-09-08；owner 内部纸面分析，非正式 Driver verdict。只读三份冻结 metadata，并复用此前已核的原/gen2 taskbook 与原 null 程序。本轮未读仍在编辑的新脚本、未执行数值、未导入生成器、未新增 claim 或修改仓库。

**没有发现计划把恢复零行后的 Null A 误称为无条件 density null，也没有发现足以否定 Stage1 有界实现/资源探针的内部科学矛盾。** 这只评价计划合同；不证明实现正确或 full 21 cells 已具有闭合硬目标的判别能力。

## 已明确且可接受的边界

- `correction_manifest.stage` 为 `STAGE_1_SUBSTRATE_ONLY_NOT_SCIENTIFIC_SCREEN`，`scientific_state=NOT_RUN`，`resource_probe.full_run_authorized=false`。`coordinate_contract.corrected_and_residual` 明确不计算 Stage1 科学向量，不伪造零数组。
- 第 4 项输出计划明确写：恢复零行不证明正确的无条件科学 null；审计容量及细窗口耦合；不能用 scalar p counts 偷造 q-rank 分配。第 6 项明确新 ensemble 是暴露后的重算，不是旧阈值换模型后仍冒充原值。盲态已披露，Null B 不修复 Null A。
- 几何支撑采用非空**整数** q 窗口，不以实际素数 count 是否正决定。完整 prime prefix 给出真正一基 `pi(p),pi(q)`；固定 p 的连续 q 窗口对应连续的 prime-rank 区间，因此用该区间与 rank-bin 的交集计数，可以精确保留真实观测 joint histogram，不必逐对展开。这种观测压缩不定义 synthetic null 的 q 分配。
- `p*p>X` 的合法壳质量保留在 raw/rank 与单列 overflow；不会剪裁进 `u<=1/2` 的最后一格。原始整数总体、derived S3 展示及 signed residual 的类型也分开，未宣称新 family/native ontology。

## 只有以下问题会改变后续 full-run 决策

1. **零行修复后的计算分布仍是有条件的行计数置换。** 原程序第 94–108 行按粗 log-p/p-mod 层，对各 q-residue 分量独立置换。恢复零行改变这个有限分布，但不恢复目的窗口容量、精细局部密度耦合或 q-margin。新计划已诚实承认这一点。若实际审计发现置换质量不能由所声称的合法 q 支撑实现，不能靠截断、删除该抽样或重新抽样后仍称“原 null”。作为抽象 count 随机化，其计算分布仍可定义；作为忠实局部密度模型，其解释需要另行成立。full 21 若仅交付修正后的一维重算和失配账本，有窄价值；不能据此把“密度因素已解释全部残差”作为自动结论。

2. **固定精度预算不等于全部分箱已被证实。** `native_coordinate_scales=[10^6,10^10,10^14]` 与 plan 的有限 refinement/UNRESOLVED 相容。要把一个完整 profile 或阈值称为已判定，所有会影响该统计的 interval 跨格情况必须分离，或给出足以判定该统计的保守误差界；不得取中点、四舍五入或丢行。特别是观测 count 为零、但在其置换层可能接收正质量的行，后续 Null A 仍会需要它的 z-bin：零观测质量不是免除坐标证书的理由。`exact right endpoint -> final bin` 必须以真实等号证据触发，不能把“区间碰到边界”当等号。计划目前允许 unresolved，因此这不是已发现的错误；实现冻结后的证据决定能否从 probe 扩到完整已判定的统计。

3. **joint 图仍是观测诊断；归一化与 joint correction 不可混同。** 每 cell 用 `pi(floor(sqrt(U)))`、`pi(floor(U/2))` 作为 caps 是可声明的几何归一化选择，不会使存储的未归一化 ranks 变假。它也不保证同一格跨 cells 代表相同的绝对 prime-rank 范围。若之后把它用于跨尺度 phase/显著性比较，必须固定确切的 rank-to-bin 公式、边界包含规则和可比对象，不能只写“24x24/caps”就让实现临时选。当前 Stage1 诊断输出可明确保存实际 edges 与完整整数 ranks；它不需要新增 joint null。若 full-run 目标升级为 joint corrected/null 检验，则此前 memo 所述条件随机核和 phase/statistic 合同仍缺失，不能由当前三份 metadata 或全量枚举补出。原/gen2 书要求的 corrected-view 义务应保持 unavailable/partial 边界，不能被诊断图冒名完成。

4. **资源/原生调用观察只能证明实际观察到的范围。** 计划的 `X=2000003` 新 probe、60 秒上限不是原 21 cells 的科学筛选；它适合检验坐标、精度、trace 和资源路径。code-object counters 与保留实际 trace 的计划合理，但计数器/静态检查本身不证明完整传递调用链的原生合规，也不证明最大 cell 的运行成本。发生 refinement 或资源上限应按现约定输出完整 partial receipt，不能省略零行、overflow 或未决 bin 来制造全量成功。原生精确计算不会使一个未识别的概率模型自动成立。

由此，当前计划可以作为 Stage1 有界实现/探针的科学边界；是否运行 full 21，应依据冻结实现的实际精度/支撑证据，以及 root 明确选择的交付目标：完整观测和旧一维检验的暴露后重算，或另有明确合同的科学检验。两者不能在执行成功后才混为一谈。source_binding 的 ER/claim 记录在本轮仅作计划元数据，不重新裁决 root 已处理的运行授权；同样不把其历史 ER prepare 失败改写为成功。

## 来源 hash 与本轮证据范围

三个文件位于 `D:/em/research-pfssv-revision-20260908/research_artifacts/PFSSV_REVISION_20260908/`，均声明冻结时间 `2026-09-08T10:39:58.528352+00:00`。

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `correction_manifest.json` | 7655 | `fe907aa65dd713a57acb327bebb43cf89c4630ac261e8a4a3b25474b2fc33d1c` |
| `native_substrate_plan.json` | 6809 | `fe9dce879b8d735c060aa2dd9018b8ac1002cb8f5b4e5b0d114d9642d629b694` |
| `source_binding.json` | 6734 | `0466d085c9cfd83f11e72756751f0e9d74da18deb9bdb584af93af14a8458a2b` |

source_binding 记录 local baseline `2aa103eee829b78fa7784674ec1be4c3c5052a79`、source execution commit `4dc38cc6cdd6c59922a6ee37b108bed49cf8c9d2`、gen2 `TP2-2029B5CCC5EEC5F0132C`、ER `ER-EB2A78D7B88A292B412B`。本轮核对了三份 metadata 的同 task/publication/claim/identity 与 ER 引用一致；没有把其 `preserve_bytes` 清单当成本轮逐一验证全部依赖源码的证明。

复用此前已读的 main `be350eb1b0eeb2a9a07a23a43ee3c8170e93b4b4` 三来源：原 taskbook SHA256 `b4e6011b736026ab2a5fc247f8a3750163cd33909fe25cf04bec6391078157d3`；gen2 taskbook `e1b35c812f66f105a55af54ad258d3f5381f8de33ac598ff3d806ba7b0ca0c0f`；原 null/checker `8772484435d77abf74e87a6f053a0edaf4fa9395bdbade93ede2413083f22140`。既有纸面 memo：`D:/em/TEMP/pfssv-gen2-null-contract-independent-20260908/NULL_CONTRACT_MEMO.md`，SHA256 `3f74402ff777e3222206b94da98254fa7e3c7eda50d7df841085a3cad028b490`。

实际工作仅为文本/JSON metadata 阅读、hash 核验和本 memo 写入 TEMP。没有数值或实现测试 PASS；没有正式科学接受标签。原样 shipped-sync 本轮实际返回同一已读 canonical snapshot 的 `LEASE_REUSED`。

Global-Knowledge-Sync: main@b2d9cef / GLOBAL_KNOWLEDGE_V1
