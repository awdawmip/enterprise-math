# X6 联合观察证书与精确恢复原型

研究实验；不自动授予 Foundation 或 Working Truth。源理论与完整边界见
`research_notes/OWNER_FREE_CANDIDATE_20260907.md`。

- `observer_certificate.py` 直接复用 BRC `WeightHistogram` 与 T6，生成三轴相同、四轴可区分的精确见证；空间坐标和来源标签另外保留。
- `recovery.py` 只读全部20张 **raw signed** 三轴边缘表，互补连接、筛选、精确消元及非负求解后重新计算所有边缘。输出少于8个支点时给出全有限非负竞争分布范围内的唯一证书。
- `parity_certificate.json`、`recovery_certificate.json` 是示例运行结果，不代替一般证明。

坐标锚点必须一致。`can3` 观察必须额外保留 common depth 才能交给恢复器。返回的 `recovered:*` 是输出行标签，不是找回原来的路径/分支身份。

## 运行

Python 3.11+。恢复器额外依赖 `sympy==1.14.0`，观察证书只需标准库与仓库现有代码。

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

本轮发现 SymPy 的直接等式 LP 可返回不满足等式的答案。满列秩现在直接用精确 RREF；欠定问题消去等式，只对自由质量变量求非负可行点。该求解器仍可能失败，所有输出必须经非负性与原表重算。`ArithmeticError` 表示没有得到合格的求解器证书，不能作为数学无解或反驳支点定理。

实验未承诺：含噪鲁棒性、无限支持、完整原生旋转群、路径身份恢复、线性或多项式时间复杂度、所有输入均能由第三方求解器完成。
