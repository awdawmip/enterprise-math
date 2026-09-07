# Independent rational interval-family inertia certificate — validation

辅助工作包：`/root/stability_research`，非正式 task/claim/Driver review。
仅负责标准库有理惯性证书。未修改 `reference_builder.py`，未调用 Arb、浮点特征值或生产者报告的真值 q；没有运行实际 reference 矩阵消元，真实 run002 的连接器与证书由 root 独立执行。

## 输入和公开 API

```python
certificate = certify_interval_inertia(bounds, labels, max_dimension=64)
result = verify_interval_inertia(bounds, labels, certificate, max_dimension=64)
# aliases: certify, verify
```

实现：[inertia_certificate.py](D:/em/owner-20260907/experiments/owner_rh_reference_20260907/inertia_certificate.py:304)。

`bounds` 是非空 n×n 实对称区间矩阵，每项恰为 `{"lo": q1, "hi": q2}`。q 可以是精确 `int`、标准库 `Fraction` 或规范、约分、正分母的 `"numerator/denominator"` 字符串；拒绝 bool、float、字符串小数、反序区间、缺项、多余字段及非对称区间。不会用交集悄悄修复非对称输入。

生产者的 `owner_rh_reference_bounds_v1` JSON、`status=ENCLOSED`、`eta="9/10"`、dimension、parameters/provenance 等由 root 连接器负责检查。本模块只消费其中 bounds、labels，所有误差尾必须已经进入 bounds；没有额外 beta 参数。

labels 有且仅有 n 个；每个 label 可以是嵌套的 exact JSON value，即 null/bool/string/int/list/字符串键字典，拒绝浮点数。label 本身允许 bool 是 JSON 类型约定，bounds 数值仍拒绝 bool。不同基标签的规范 JSON 必须不同；外层顺序保留，字典键排序不改变标签身份。标签内容的 branch/k/端点含义由生产者和消费者验证，本模块不替代这项语义检查。

输入绑定以规范化的有理 bounds 和 canonical JSON labels 组成 SHA256；有理 int/Fraction 与等值规范字符串拥有相同绑定。这是数据匹配，不是作者身份签名，不是 Weil 构造的真实性证明。

certificate 全部可 JSON 序列化，字段恰为：

```text
schema = owner_rational_interval_inertia_v1
dimension
input_sha256
delta = canonical p/q
minus = {permutation, L, blocks, inertia}
plus  = {permutation, L, blocks, inertia}
status = CERTIFIED | UNDETERMINED
negative_count = integer | null
```

其中 `minus` 对应 `M-delta I`，`plus` 对应 `M+delta I`；`blocks` 是连续分块的 `{start,size,D}` 列表，size 为1或2，D 为有理对称块；inertia 含精确 nonnegative integer 的 `negative/zero/positive` 三计数。

## 认证数学的完整边界

令 `M_ij=(lo_ij+hi_ij)/2`、`R_ij=(hi_ij-lo_ij)/2`，取 `delta=max_i sum_j R_ij`。对任意属于输入区间族的实对称 H，有 `E=H-M` 满足 `|E_ij|<=R_ij`。由 R 对称和 `2|v_i v_j|<=v_i²+v_j²`，

\[
|v^TEv|\le\sum_{ij}R_{ij}|v_i v_j|
\le\delta\sum_i v_i^2.
\]

故 `M-delta I <= H <= M+delta I`（Loewner 顺序），并且 `delta>=||H-M||_2`。负定子空间在上述序关系下给出

\[
n_-(M+\delta I)\le n_-(H)\le n_-(M-\delta I).
\]

两端负惯性恰相同才证明族内所有 H 的负惯性都是 q。这里只认证**负**惯性；`CERTIFIED(0)` 允许零特征值，因此不是正定证书。

每个端点证书的约定为

\[
A[permutation,permutation]=L D L^T.
\]

算法对当前 Schur complement 优先选择非零对角元作1×1枢轴；若全部对角元为0但存在非零 off-diagonal b，则选择 `[[0,b],[b,0]]` 作2×2枢轴；若剩余块全零，输出零1×1块。每一步严格减小未处理维数，因而有限终止。交换 Schur 行列时同时交换 L 中已完成列，避免破坏原合同恒等式。此处使用标准有理对称消元，没有新惯性理论或新工具 family 声明。

验证器**不重跑上述消元**。它独立检查：

1. 当前原区间族与 labels 的绑定及重新算出的精确 delta；
2. P 确实是完整置换，L 是单位下三角，因此二者均可逆；
3. D 块顺序、大小、对称性及其完整维数覆盖；
4. 以有理数直接重乘每一个原端点矩阵元素，验证完整合同恒等式；
5. 1×1 块按精确有理符号计数，2×2 块由 determinant/trace 精确计数；不信自报 inertia；
6. 两端计数与最终 status/negative_count 一致。

因此任何通过验证的替代合法合同 witness 也可接受；所谓“拒篡改”指拒绝破坏数据绑定或数学恒等式/结论的修改，不是拒绝所有等价的证明编码。

## 状态与可中止边界

独立验证返回 `status, negative_count, negative_count_bounds, reason, scope, verification_complete`，scope 恒为 `INPUT_INTERVAL_FAMILY_ONLY`。

| 情况 | 返回/异常 |
|---|---|
| 两端均验真且负惯性相同 | `CERTIFIED`，q，bounds `[q,q]`，`verification_complete=True` |
| 两端均验真但负惯性不同 | `UNDETERMINED`，q=null，真实夹界 `[n_-(plus),n_-(minus)]`，`verification_complete=True` |
| 格式、绑定、合同恒等式或自报符号/结论无效 | `INVALID_CERTIFICATE`，计数为空，附 reason，`verification_complete=False` |
| 当前验证尺寸预算不足 | `UNDETERMINED`，两个计数字段均空，reason 明示 budget incomplete，`verification_complete=False` |
| 生成器遇到无效输入或预算不足 | 分别抛 `InvalidInput` 或 `ComputationBudgetExceeded`，不返回数学结论 |

默认矩阵最大64维，可显式调整。还有嵌套深度、输入字节、有理位长与字符串长度预算。大整数十进制转换通过局部分块完成，不改变 Python 进程的全局字符串安全设置。一般精确有理消元可能产生很长的分子分母；这里不宣称规模无关成本或总可在固定资源内完成。

## 实现前的有界工具覆盖

已实际运行：`python tools/enterprise_toolbox.py --json coverage rational interval symmetric matrix inertia LDL certificate`，随后只检查与本缺口相关的精确源码。

- `T2_BLOCK_FINITE_CERTIFICATE`：`REUSE_APPLIED` 于有限 witness/独立检查思路。当前匹配到的现成 specialization 是 integer-box Helly/facet 证书，不是对称矩阵惯性 API。
- `brc_weighted_recurrent.py`：有精确 Fraction 矩阵乘法/逆与非负递归质量证书；没有 signed symmetric congruence/inertia witness。不能用非负质量稳定性冒充此问题。
- `c3_chiral_complex_structure.py`：固定2×2整数矩阵运算，不能提供任意 n 的惯性分解。
- `scripts/rh_log3_n8_arb_certificate.py:379` 与 n2 脚本 L219 的 `interval_ldlt`：已精读，遇到非严格正枢轴即返回未定，只做 positivity，依赖 Arb，不输出所需 signed 1×1/2×2 P/L/D witness。
- 在 `src/enterprise_math`、`research_checks`、`scripts`、`experiments` 对 `def ...inertia/ldl`、symmetric pivot/congruence 的有界精确检索，未发现另一个满足本合同的 primitive。这不是全仓库永远不存在的声明。

确认的本地接口缺口是：**只用标准库精确有理数，对已给实对称区间族生成 signed 惯性 witness，并绑定 labels、由独立验真器重乘验证**。本实现是 task-local adapter；不把词面 coverage 记为代码复用，也不注册新 canonical family。

## 已完成的独立回归

[test_inertia_certificate.py](D:/em/owner-20260907/experiments/owner_rh_reference_20260907/test_inertia_certificate.py:1)。实际命令：

```powershell
python -m unittest discover -s experiments/owner_rh_reference_20260907 -p test_inertia_certificate.py -v
```

结果：**15 tests PASS**，其中包括96个固定 seed 的独立有理合同构造，维度1至8。测试从已知签名的1×1正/负/零块及2×2 saddle 块出发，用独立矩阵乘法构造 `L D L^T` 并随机置换；expected q 取自构造前的 D，不取自被测分解或浮点 eigensolver。

其余关键检查：

- `[[0,1],[1,0]]` 必须生成/接受2×2枢轴；后期置换和旧 L 列处理；
- 零矩阵与非零奇异半正定矩阵；跨零区间返回已完整验证的数学未定；
- 非零区间族的独立2×2 determinant 符号检查；
- 非方阵、非对称、上下界反序、bool/float、非规范有理字符串；
- nested JSON 标签的键顺序不变性、顺序/标签更改的绑定拒绝；
- L、D、P、block coverage、delta、符号计数、status、schema 篡改；即使对错误矩阵更新 binding hash，旧合同 witness 仍失败；
- mock 禁用 `_congruence` 后 verifier 仍可验证，证明其不依赖重跑生产算法；
- 32维180-bit有理对角构造，正确负惯性11；
- 超过 Python 默认4300十进制位的有理数，无全局设置更改；
- 预算耗尽不记作无效数学证书或确定惯性。

上述通用测试不包含实际 RH reference 的 q。不能把这15项测试当成真实 Weil 实例的验证。以下另记 root 交付现成真实证书后发生的独立复核，两个证据层保持分开。

## 后续 run002 现成证书的独立审读

root 已执行真实 run002 的构造消元及连接器。本辅助包没有重复消元：在把 `_congruence` mock 为直接报错的环境下，仅调用公开 verifier 对现成 P/L/D witness 重新作全部原矩阵合同恒等式验证。实际返回：

`CERTIFIED, negative_count=8, negative_count_bounds=[8,8], verification_complete=True`。

两个端点经核验的完整 inertia 都为 `negative=8, zero=0, positive=24`。delta 精确为

`2024912878742577611153949018957860044801/91343852333181432387730302044767688728495783936`。

此次使用的现成 artifact SHA256：

- `reference_bounds_run002.json`：`4f72786fd9ef23a8176cda3bdec3e2412d10d3d69b9cbab055c7fed0faeb6e67`；
- `reference_inertia_run002.json`：`2288d3a6c83dd147810e47eaa5d27f7de7a506e11269f816a3eee7603ab92bc2`；
- `reference_inertia_report_run002.json`：`910bc17aa08706d97a2ed35c25e130f468233dc99c15b3f51b8dae5f0a9adade`；
- 审读的 `run_reference_certificate.py`：`0e992b83cff078be39682e828f216f5c5c89974403819e68fee5352c2ec4dca8`。

本实例还能严格推出**整个输入区间族**恰8负、24正、无零，而不仅是通用 API 的8负结论。证明：上端 `M+delta I` 有8维严格负子空间；同子空间上 `H<=M+delta I` 使 H 仍严格负，故 `n_-(H)>=8`。下端 `M-delta I` 有24维严格正子空间；同子空间上 `H>=M-delta I` 使 H 仍严格正，故 `n_+(H)>=24`。H 只有32维，两个下界迫使签名恰为 `(8,0,24)`。也可按升序特征值写 `lambda_8(H)<=lambda_8(M+delta I)<0`、`lambda_9(H)>=lambda_9(M-delta I)>0`。这一无零推论依赖端点完整惯性，不应从一般的 `CERTIFIED(0)` 或仅相等的负计数擅自推出。

连接器只对 `owner_rh_reference_bounds_v1`、ENCLOSED、dimension32、eta9/10、预定JSON标签顺序、已声明 inherited formula source hash、明确 reference target 和全部误差已在 bounds 的合同作检查；读取 `initial_verification` 作为历史记录，**verify 路径不相信它**，而是重新验真核心 witness。其结果保留 `INPUT_INTERVAL_FAMILY_ONLY` 与 `target_identification="Requires the separate producer and analytic-bound audit."`。未发现把任意标签哈希或区间证书升级成 Weil 对象、完整 cross 算子或 RH 真值的范围扩张。所检查的 source hash 字段本身仍只是来源声明，真实生产者代码/公式/包围的正确性由独立生产者审查负责。

如果 run003 仅修复 provenance 而规范化 bounds 与 labels 完全相同，已有**核心**证书可以重新验证复用；外层 packet 绑定的是完整输入文件 SHA256，所以必须为新文件另建正确 envelope，不能让旧 run002 packet 的 full-file binding 假装匹配。若 bounds/labels 数学内容变化，则必须按新输入验证，旧核心 input binding 不能沿用。本次没有写或覆盖 root 的 certificate/report。

## 冻结文件 SHA256

- `inertia_certificate.py`：`eedb0fbdfebfec478a18f418fcf8b3eb386903870bea1ae9b9948afce1e67bc5`
- `test_inertia_certificate.py`：`85ecc880f563e60f83875ea4af532345e680b6372e72f3c73ad90fb7b260ffa1`

辅助工作包：`/root/stability_research`。

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
