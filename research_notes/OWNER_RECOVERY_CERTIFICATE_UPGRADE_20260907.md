# 原始 X6 质量恢复：从拒绝坏答案到精确可行性证书

这是 owner 持续研究的工具补全检查点，不是新 BRC 家族或 Foundation 采纳。

上一版在已知可行的21支点样例上，SymPy 不等式求解仍会产生负质量。拒绝坏答案保住了正确性，但没有完成恢复能力。本次用标准有理 Phase-I + Bland 替换该路径，并把旧的“恢复或安全拒绝”测试收紧为必须恢复。

## 范围与覆盖

实际消费对象仍为同一空间锚点上的有限 signed X6 Cell 正质量分布。全部20份 raw 三轴表经既有 BRC histogram 适配器形成；输入不含原标签或路径历史。候选 join 与支点小于8的唯一性证明继续复用。

工具覆盖检索未找到现成的非负有理线性可行性实现，普通精确 RREF 不能代替非负可行性。裁定为已有原生消费接口的 `EXTEND_EXISTING_TOOL`，标准算法实现补全，不宣称新的数学算法。

新增 `experiments/owner_joint_observer_20260907/exact_feasibility.py`：接受有限有理 A、b，求 A x=b、x≥0。初始负 RHS 行乘−1，添加人工基，最小化人工变量总和。最小索引负 reduced-cost 入基，最小 ratio 并按基变量索引打破平局出基。零目标给 primal；正最优目标给 y，使 Aᵀy≥0、bᵀy<0。

独立 `verify_certificate` 只读原始 A、b 和向量，不依赖 tableau、换基历史、求解器状态或报告目标值。primal 与 dual 的条件互斥：若 x≥0、Ax=b，则 bᵀy=xᵀAᵀy≥0，排除 bᵀy<0。

[Bland 的原始论文](https://doi.org/10.1287/moor.2.2.103) 提供所用有限换基规则。有限基数与防循环保证理论终止，不等于多项式时间；稠密 tableau、Fraction 位长及资源耗尽仍是工程边界。资源错误不能产生不可行结论。

## 接入与证书

`recovery.py` 先尝试廉价的 RREF 基础候选，并直接验证全部原始等式；不合格时调用新 Phase-I。任何返回证书再独立核验一次。可行分布最后重建 Branch 并用 BRC 完整重算二十张表。

不可行的方程系统以 `InfeasibleMarginalsError` 附带原 rows/rhs/candidates 和 Farkas 证书；伪造、缺失或不满足原系统的证书触发 `ArithmeticError`。输入格式错误、支点预算和直接支持矛盾仍有各自明确错误文本。

≤7 支点的成功输出应用原有一般定理，给 `UNIQUE_BY_SUPPORT_BOUND`。≥8 支点保持 `FEASIBLE_UNIQUENESS_UNCLASSIFIED`；本补全没有把通用可行性伪装成通用唯一性判定。

## 实测

root 在完整接入后的工作树执行：

```powershell
python -X utf8 -m unittest discover -s experiments/owner_joint_observer_20260907 -p 'test_*.py' -v
```

26 项测试通过。包括729个 signed 2×2 系统与独立顶点枚举 oracle、48个有理/冗余随机系统、空行列与负 RHS、退化换基、巨大分母、伪 primal/dual、176个 X6 稀疏源，以及21支点旧失败例。

最小三方程 A=[[1,1,0],[1,0,1],[0,1,1]]、b=[1,1,1] 精确返回三个1/2。21支点例为160行、64候选；求解器执行135次换基，输出21个正质量支点，原方程及全部 BRC 表通过核验。这里的有限实测不替代算法论证或一般支点证明。

## 仍开放的工具方向

含噪稳定性由独立数学笔记给条件定理，当前接口只读精确质量表。逐权重 BRC 直方图的整数联合实现是另一个真实缺口；质量 LP 可行不自动实现原始分支直方图。后续扩展须保留这条类型边界。

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@ccd838a / GLOBAL_KNOWLEDGE_V1
