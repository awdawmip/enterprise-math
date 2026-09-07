# Owner 精确可行性与恢复接入：独立本地审计

辅助审计工作包：`/root/stability_research`。作者为其他 owner 工作包；本审计未编辑被审计四文件，
未创建正式 Driver review、task、claim 或 Foundation disposition。

结论：**PASS_WITH_EXPLICIT_SCOPE**。在本节固定源码字节上，没有发现需阻断该本地原型集成的数学或实现错误。
它实现有限有理 `A x = b, x >= 0` 的已核验可行解或已核验 Farkas 分离证书，
并修复此前已知的 21 支点可行实例。它不构成含噪恢复算法、一般唯一性判定或效率提升定理。

## 1. 被审计的精确字节

基目录：`experiments/owner_joint_observer_20260907/`。

| 文件 | SHA256 |
|---|---|
| `recovery.py` | `503282c2b6c07f2a9fece03a16f242d3ae5442ed333990a073ce9d0daa5d3b24` |
| `exact_feasibility.py` | `874b480ccb9f073f26e851c48bf6955ac745152698cf66710277f3e7a48691ec` |
| `test_recovery.py` | `4239c804a55f36e00cc4de3cc109e06054a318c0dc45b19d2d413df3df2e22db` |
| `test_exact_feasibility.py` | `093da1616afb70f46b782761ba2dfca5fb9d6bbbbae7ae37ca8779cb2a87021f` |

原生/BRC边界另读 `observer_certificate.py`：raw signed 六轴空间 Cell、不可变坐标、正有理分支、
现有 `WeightHistogram` 的 total-mass 读出。当前基础源快照沿用 owner 的 `ef1893382`；
上述审计对象是本地新实现，不能将其 hash 与 Foundation 已接纳状态混同。

## 2. Phase I、Bland 与 dual 符号逐项核对

设原系统有 m 行 n 列，`D[i,i] = -1` 当 `b[i] < 0`，否则为 1。
实现构造 `(D A | I)`、右端 `D b >= 0`，以人工变量为初始基，目标为人工变量总和。

1. 人工单位块保证增广矩阵满行秩，因此原系统有零行或冗余行也不破坏基的定义。
   起始表为 `B^-1 (D A | I)` 和 `B^-1 D b`，人工块始终就是 `B^-1`。
2. 初始原变量 reduced cost 为 `-sum_i (D A)[i,j]`，人工变量的 reduced cost 为0；
   等于标准 `c - c_B^T B^-1 A_aug`。
3. entering 选最小下标的负 reduced cost；基本变量的 reduced cost 在精确消元下恒为0，
   因此虽然代码不另列 nonbasic 集合，也不会让基本变量成为 entering。
4. leaving 在正 pivot 系数中先取最小非负比值，再按当前基本变量下标最小打破平局。
   这同时满足 Bland 对 entering 与 leaving 的规定；只用其中一半不足以排除退化循环。
5. pivot 行除 pivot，其他行精确消元；reduced cost 更新与 objective 的单独更新
   `objective += old_reduced_cost[entering] * new_rhs` 符号一致。
   `zip(reduced_cost, pivot_row)` 有意不包含 pivot 行末尾的 rhs，objective 已在另一句处理。
6. 人工目标非负。目标为0即可返回原变量 primal，无需为剩余人工零基变量再跑 Phase II。
   正目标且无负 reduced cost 才进入不可行证书分支。
7. 最优时令 `pi^T = c_B^T B^-1`。原变量 reduced cost 非负给出
   `-pi^T D A >= 0`；同时 `pi^T D b = objective > 0`。
   因而代码的 `y = -D pi` 精确满足
   `A^T y >= 0` 与 `b^T y = -objective < 0`。
   这与 verifier 的 Farkas 符号约定完全一致。
8. 若有改善方向却没有可离基行，或出现负目标/负基本量，代码抛出 `ArithmeticError`；
   不把不变量失败包装成 `INFEASIBLE`。

Bland 原论文的 Rule I 和 Theorem 1.1 规定了上述最小下标选择及有限性；本次已核对原论文，
不是以测试运行终止替代 anti-cycling 论证。来源：[Bland, 1977, *New Finite Pivoting Rules for the Simplex Method*](https://pubsonline.informs.org/doi/abs/10.1287/moor.2.2.103?journalCode=moor)，
[原文镜像，§1](https://web.ist.utl.pt/mcasquilho/acad/or/ftp/1977MathOR_Bland.pdf)。
在此具体 Phase I 中，人工目标有零下界，故改善方向不能无界向下；有限基数及 anti-cycling
给出有限步保证。该一般保证可能是指数级，Fraction 位长和密集表的空间开销也没有多项式承诺。

## 3. 原系统证书边界与恢复器接入

`verify_certificate` 只读取原 `A,b` 与证书，不读取 pivot 历史或目标值，也不调用求解器。
可行证书要求准确维数、exact int/Fraction、逐项非负、每一原方程精确成立；
不可行证书要求准确维数、`A^T y >= 0`、`b^T y < 0`。
status 与 primal/dual 必须互斥。`pivots` 只是诊断，故其异常数值不参与真伪判断是有意设计。

`recovery.py` 的接入保持两道独立校验：

- RREF 把自由量设0产生廉价候选；即使增广系统不一致、存在冗余行或候选带负量，
  它也必须通过**所有原始行**的 verifier 才能接受，否则转 Phase I。
  未利用“解了一个独立子系统”替代原方程验证。
- Phase I 的任何返回值再经原行 verifier；成功 primal 还重建 `Branch`，
  直接调用既有 BRC histogram 读出重新生成全部二十张边缘表逐项比较。
  缺失的零项由 complementary join 的支持约束保证，没有漏掉隐含零表项的方程义务。

对任意非负实现，每个正质量 Cell 的六坐标都必须来自两个互补三轴表的地址拼接，
并在所有另外三轴投影上落入已观察正支持。这证明 candidate join 包含全部合法可行支撑；
它不是为了稀疏答案随意删除竞争点。

只有回收空间支点数 `<8` 才返回 `UNIQUE_BY_SUPPORT_BOUND`；更多支点仅为
`FEASIBLE_UNIQUENESS_UNCLASSIFIED`。八对八 parity 零噪声例和 21 支点压力例均未被错误宣告唯一。
同一 Cell 的多条正路径会聚合为空间质量，不会以路径数代替空间支点数。

## 4. 运行证据与故障注入

本审计独立运行：

```powershell
$env:PYTHONPATH = Join-Path $env:TEMP 'em-owner-math-deps'
python -X utf8 -m unittest test_exact_feasibility test_recovery -v
```

工作目录为上列实验基目录。实际输出：`Ran 25 tests in 11.109s`，`OK`。
数字25是这两个模块的测试方法数，不与其他 observer 模块或子实例数混算。

有效覆盖包括：

- 729 个符号 2×2 整数系统对独立小规模列支撑顶点枚举 oracle；
  48 个有理含冗余行系统对相同 exact linear-algebra oracle。
- 负 rhs、零行、冗余/矛盾等式、零变量、空约束、退化零步长 pivot、大整数与分母。
- **已知21支点可行实例必须恢复成功**，且重建全部 raw/BRC 边缘精确一致；
  这个测试没有把过去错误改写成“允许失败”的通过条件。
- 56 个非均匀有理稀疏分布、120 个跨所有四活动轴的删点 parity 例。
- 错误维数、float/bool、未知status、同时含 primal/dual、伪 primal、零 dual、反符号 dual 被拒绝。
  patch verifier 依赖的 solver 抛错而 verifier 仍工作，验证二者未形成自我背书。
- recovery 注入伪 primal/dual 时只抛 `ArithmeticError`，不泄漏虚假数学成功/不可行报告。

另由本审计单独编写并运行 `owner_stability_feasibility_probe_20260907.py`（输出同名 JSON）：

- 向一支点恢复注入维数、秩、非负性都正确但质量为2的错误 RREF 候选。
  原数据质量为1。原全方程检查拒绝该候选，Phase I 随即恢复正确质量1。
- 在这个确实进入 Phase I 的输入上分别注入 `MemoryError`、`ArithmeticError`、`RuntimeError`。
  三个原异常原样传播，均未转成 `InfeasibleMarginalsError` 或可行性结果。

这些有限检查发现具体实现回归；一般正确性仍由上面的不变量、dual 推导和经典终止定理承担。

## 5. 异常语义与未作的承诺

- 输入格式/负边缘/总量不一致属于契约 `ValueError/TypeError`；预算超限消息明确
  `no mathematical conclusion`。资源或内部失败不创建数学不可行证书。
- join 为空的输入通过支持必要性已有组合性不可能证明，当前以普通 `ValueError` 返回；
  本次没有将该入口宣称为携带数值 Farkas witness 的 `InfeasibleMarginalsError`。
- 非空 join 的线性非负不可行结论只在已核验原方程 Farkas witness 后使用专门异常，
  并随异常保留 rows/rhs/candidates/certificate，便于独立重查。
- 这里的 `recover` 仍是**精确一致边缘**接口，要求非负且总量一致。
  新的 `OWNER_X6_STABILITY_20260907.md` 证明有噪质量误差上界，
  不意味着此函数现在接受任意噪声表或已实现残差最小化。
- 有限 candidate budget 与 Phase-I最坏情况开销明确存在。本次没有宣称解决大规模性能问题。

本地独立审计已完成。若四个被审计文件后续改变，应对实际变更重新核对，
不能无条件沿用本 hash 绑定结论。

辅助工作包：`/root/stability_research`；无正式角色分配或审查记录注册声明。

Global-Knowledge-Sync: main@ccd838a / GLOBAL_KNOWLEDGE_V1
