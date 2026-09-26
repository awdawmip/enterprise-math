# Shor 固定原生字模拟：稀疏认证、完整相位与完整分解接口

Progress-Event-ID: sep26-shor-general-c6438c
Researcher-ID: EM-DIRECT-C6438C
Activity-ID: RA-CAAAC604CB513AEA8BBC1DFC
Session-ID: MCP-9e0873ae3aae418192f81173029434e7
Status: AUTHOR_EXECUTED / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Parent objective: 从原对话不同角度试图闭合 Shor 模拟算法；本目标仍保留未证的全域与效率问题。

本包接续 Source `b6625778e869511d85a202a0839eb105a197659e` 的
`research_notes/directed_recovery/20260926_0C08F0/`。不再只增加局部矩统计量，
而是沿完整输出、真实算术成本、一般位宽与可量化因数成功率推进。

发布前对齐到 Source `384a93952abf67a4a1c1741dfb8319d3e3f5609e`，完整读取并承认并行
`HEARTBEAT90_STREAMING_COMMON_SPARSE_20260926.md`：它已复用上一轮流式证明，完成共同根整机与
稀疏地址证书的12例全叶检查。本包不把重叠方向宣称独创，也不把双方计数相加为独立实验。
本包进一步提供实际全加器构造的模乘列、m34完整库、K33尾门、总体成功界与完整分解证书接口。

## 本轮已取得的结果

1. **模乘稠密认证被替换。** 全部工作基列从实际BRC全加器逐位构造，保留输入、进位、减模和来源；
串接、逆、控制直和与任意signed/61模式纤维的等价性有一般证明。认证从稠密平方存储/立方循环变为
O(N log N)逐位步骤及证书。100个原核基列、488个signed坐标、32个指数、12步平方链、96个完整后处理结果一致。
较大N33/257/1009全证书回放通过，8个篡改负控拒绝。生产端准备与后处理都走稀疏路径。

2. **原32/64网格的完整相位库接通。** m34前的32份字共1952个完整基列及逆字实际验证，公共维数重新计算为61。
m34起闭区间稳定，任意有限t可复用已认证字，并得到请求对应的真实误差界。没有提高精度。

3. **证明并运行整载体恒等尾门。** K33策略保留所有残差坐标，只替换m>=33的整个微小相位操作。
误差从随t二次增长改善为 `E_t=(185t-3225+8/2^(t-32))/2^32`（t>=33）。
N21/t34/k1的closed、K34、K33完整状态均已保存；分母位长4045、3919、3793。
N35/a2/t12实际稀疏运行，指定可能历史k341给5、7；随机历史k3072的真实失败完整保留。

4. **当前CF后处理已有明确随机成功界。** 不补倍数也有理想每次至少1/(8n)，编译后减具体TV界。
K33同网格策略的简单重试预算支持n<=856；更大预算的严格正下界支持n<=1208。
这些是保守证书范围，绝非856/1208位整数实跑，也不是超过范围就不可能。

5. **完整或部分因子分解接口已经实现。** 实际全加器组成完美幂、Wilson精确素性和乘积账。
素数叶必须有重放证书；其余合数由稀疏Shor/gcd分裂；失败保留未分解cofactor和重数。
7个输入完整分解（2、9、27、22、35、45、225），2个故意失败输入保留完整部分结果，2项篡改拒绝。
所用示例是种子软件随机/固定重放，不作为无偏随机或成功频率证据。

6. **Stage89共同根接入整机。** 第3阶改为同一原第4阶完整字的平方，三组全部24400坐标与对应新原生全控制电路精确一致。
独立完整列给保守误差819/2^39；门数和分母可能增加，没有冒称整体加速。原库保持。

## 查阅顺序

- `integration/COMPLETE_FACTORIZATION_PROOF.md`：整机合同、递归不变量与全树预算。
- `completion/SUCCESS_AND_COMPLETION_THEOREM.md`：原CF成功下界、固定误差阈值及原先结构性反例。
- `phases/PHASE_BANK_PROOF.md`：完整bank、尾门代数界与深位宽真实执行。
- `sparse/SPARSE_MODULAR_PROOF.md`：全部输入列、来源、组合和成本。
- `integration/INTEGRATION_PROOF.md`：流式整机等价与共同根接通。
- `completion/TYPED_PRECHECK_PROOF.md`：实际整数原语、完美幂与素性证书。

源代码、失败记录、负控、精确数值和完整状态都在相邻JSON/gzip，根MANIFEST钉住字节。
`verify_factorization` 明确只验确定性因子与乘积，返回 `stochastic_budget_verified:false`；不借verified标记虚报随机预算验收。

## 复现输入

冻结源HEAD `0852cad130c1d877174d235687cf60c19f318c58`；Drive bundle `1ox9qTtXGbN0p6Zma29uXtBXM6FcOOXhV`，
61,398,315 bytes，SHA256 `a0eb15a32c4db5a9fd0876f64a0ffd8dbedcd5eabb2a148c247a8886836e5a9c`。
原生核pin `bc7babbb9e890f6d5a7094430a5fbdccf66c77ad`，blob `4e6b3132580e3cd70a20a0d8bd4d28792b961afb`。
`BRC_STAGE87_SOURCE`指向恢复源；`BRC_STREAMING_PREVIOUS`及`BRC_SHOR_ALTERNATIVE`指向前一交付包。
完整相位payload SHA256 `feecbc02808991f6d7b1e2c3179c8da2018b76901ef34c26ef0d28b65729dd5c`。

运行入口为 `integration/check_complete_factorization.py`、`integration/check_general_driver.py`、
`integration/check_common_streaming.py`；其余各单元验证命令见各自证明。无需重新生成理想参考或增加精度。

## 任意新对话的下一步

科研结果是首要输出。直接读上述证明即可做符号核查、反例、误差或支持性证明；工具可用时再追加实际证据。
不要因为没有某个本地执行工具而拒绝整个数学任务，也不要把未执行伪报成执行。

当前继续研究的独立角度：K33字的所有内部轨迹留在
`span_Q(e0,e1,z3,...,z32)`，维数至多32。研究模乘谱值的最小多项式次数能否排除每步Kraus核，
证明良好测量读出严格正概率，从而摆脱整体TV与成功下界相减的位宽范围。
低次数奇部例外需要单独证明和明确事后验证；此段是未验收候选，不是本包已成立结论。

仍未证明一般多项式时间经典Shor模拟。工作载体约N，Wilson基线O(N)模乘，精确整数和来源证书均须计费。
也没有从该软件接口导出物理Born律或自主六轴空间接线。新一轮应继续真正数学缺口，避免重跑已过小例来冒充进展。

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
