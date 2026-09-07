# X6 联合观察证书与精确恢复原型

研究实验；不自动授予 Foundation 或 Working Truth。源理论与完整边界见
`research_notes/OWNER_FREE_CANDIDATE_20260907.md`。

- `observer_certificate.py` 直接复用 BRC `WeightHistogram` 与 T6，生成三轴相同、四轴可区分的精确见证；空间坐标和来源标签另外保留。
- `recovery.py` 只读全部20张 **raw signed** 三轴边缘表，互补连接、筛选、精确消元及非负求解后重新计算所有边缘。输出少于8个支点时给出全有限非负竞争分布范围内的唯一证书。
- `exact_feasibility.py` 补全标准有理 Phase-I + Bland 求解，不依赖第三方不等式求解器。可行返回非负有理向量；不可行返回原始方程的 Farkas 分离向量。独立 verifier 完整检查原始输入。
- `histogram_realization.py` 接受完整 WeightHistogram，逐精确权重保留整数分支计数，并完整核验联合实现。均匀二值六轴族中每个权重的纤维重数必须为0或至少2；重数1有 Rao 证书。一般表保持 `UNCLASSIFIED`。构造复用旁边 scout 的 λ=2/3生成器及现有 BRC alternative。
- `noisy_recovery.py` 在声明有限候选D及stacked残差预算η下寻找非负质量拟合，返回原方程证书与实际BRC残差。可附带前提明确的稳定性条件界；不承诺最小残差或唯一拟合。9项回归及独立48个预算边界检查通过。
- `parity_certificate.json`、`recovery_certificate.json` 是示例运行结果，不代替一般证明。

坐标锚点必须一致。`can3` 观察必须额外保留 common depth 才能交给恢复器。返回的 `recovered:*` 是输出行标签，不是找回原来的路径/分支身份。

## 运行

Python 3.11+。恢复器的精确行消元及测试的独立小系统 oracle 依赖 `sympy==1.14.0`；Phase-I 求解器本身、观察证书只需标准库与仓库现有代码。

在仓库根目录执行：

```powershell
python -X utf8 experiments/owner_joint_observer_20260907/observer_certificate.py --output experiments/owner_joint_observer_20260907/parity_certificate.json
python -X utf8 experiments/owner_joint_observer_20260907/recovery.py --output experiments/owner_joint_observer_20260907/recovery_certificate.json
python -X utf8 -m unittest discover -s experiments/owner_joint_observer_20260907 -p 'test_*.py'
```

本轮依赖安装到独立临时目录，没有改全局 Python 包。复现环境可在自己的虚拟环境中执行 `python -m pip install -r experiments/owner_joint_observer_20260907/requirements.txt`。

## 证书与失败语义

`UNIQUE_BY_SUPPORT_BOUND` 只用于已经逐项验证、支点≤7的空间分布。零总体返回 `UNIQUE_ZERO`。其他可行解返回 `FEASIBLE_UNIQUENESS_UNCLASSIFIED`，不把“未证明唯一”误当“已经找到歧义”。

互补连接候选上界为两个表的支点数之积；若生成源有s支点，则≤s²。默认候选预算256，超过预算只是运行范围限制。

最初发现 SymPy 的等式及不等式 LP 可返回不合格答案。当前已替换这条求解路径：先独立验证 RREF 的廉价候选；若不合格，对全部原等式执行有理 Phase-I，采用 Bland 入基/出基规则。任何来源的 primal/dual 都要重新经过独立 verifier；成功质量分布还必须通过 BRC 原表重算。

`InfeasibleMarginalsError` 附带原始 rows/rhs/candidates 与已核验的 Farkas certificate；`ArithmeticError` 表示执行或证书故障。候选预算、内存、时间耗尽不构成无解。标准算法的有限终止依据来自 [Bland 1977](https://doi.org/10.1287/moor.2.2.103)，未声称多项式时间或实际资源总能充足。

精确求解/恢复/观察的26项测试通过，包括729个小型 signed 系统、48个有理随机系统、176个稀疏 X6 样例及原先失败的21支点原表。Histogram consumer 另有18项测试，覆盖完整直方图与质量相等的区别、混合权重、signed二值重标、Rao证书和输入深层别名冻结。测试不是一般证明的替代品。

`recovery.py` 仍只处理精确质量表；含噪数据使用独立的预算拟合接口。空间质量可实现也不等于逐权重分支直方图可联合实现。未承诺无限支持、完整原生旋转群、路径身份恢复或一般整数直方图实现。
