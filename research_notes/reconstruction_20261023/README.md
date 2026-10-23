# 数学定理与工具重建：2026-10-23

Researcher-ID：`EM-RECOVERY-0AD96A`。本轮目标是把已取回的材料变成可定位的定理、完整证明和可运行工具。
研究输出状态为`AUTHOR_PROVED / AUTHOR_CHECKED / UNREVIEWED / NOT_ADMITTED`，具体计算覆盖与推导见下文。

## 已完成的实质数学

1. [证明与完整分类](THEOREMS.md)：推出任意度数n、任意单个二支撑删除点的硬目标显式公式；
   证明n≥7时任意四支撑补点的可解性仅由这些硬目标决定；给出n=6的步骤失效反例。
2. PREFIX180直接67,525个Q的完整最优分类：66,879个永不可解；剩余646个中，
   最小补点数12/13/14分别有1/215/430个，总状态数66/67/68。
   [逐配置机器证书](evidence/OPTIMUM_CERTIFICATE.json)含646个最优正面见证，全部用整数和集独立核验。
3. [操作安全商的证明和条件修复](OBSERVER_QUOTIENT.md)：补齐有限/无限未来分区定理，
   明确剩余期限和联合状态，并给出“同一公开观察仍多后继”时迹等价与后继签名不等价的反例。
   直接调用现有T6，实现见[示例](observer_quotient_demo.py)。

五个PREFIX180缺件已由原程序重生成，全部与历史SHA256一致；原位置的恢复说明另有链接。
REFERENCE_PREFIX179.zip仍缺，原联合家族2,331,754项的历史依赖没有因此补齐。
上述直接家族的完整分类不依赖该缺件。全局无约束β4(8)下界、完整X6物理模型和正式审查不在本次证明内。

## 可用工具

| 目的 | 入口 | 适用范围 |
|---|---|---|
| O(n)生成稀疏骨架硬目标 | `boolean_sumset_tools.hard_targets_closed_form` | n≥2；四标签；删除点恰二支撑 |
| 判断任意满支撑补点是否可能 | `support_obstructions` | n≥7；Q来自三支撑层 |
| 构造布尔生产者子句、预算搜索 | `producer_clauses`, `solve_budget` | 有限整数向量双和；UNKNOWN不是NO |
| 重建完整PREFIX180直接家族 | `replay_prefix180.py` | 75取3的固定家族；Python+C++17；本地执行 |
| 核对所有646个最优见证 | `verify_census.py` | 完整行覆盖、上下界和直接整数和集核验 |
| 历史材料中找定理或实现 | `atlas_query.py` | 输出来源线索及状态，不自动判定证明成立 |
| 生成有限观察安全商 | 现有 `enterprise_math.predictive_quotient` / `operation_quotient` | 完整有限确定系统与声明动作/观察 |

本轮工具覆盖判定为`REUSE_EXECUTED`（T6）及`EXTEND_EXISTING_TOOL`（PREFIX180生产者法）。
现有加权BRC/CWM工具继续有各自正权重前提；这里的布尔求解器不处理权重、符号相消或相位。
未把候选工具登记为新的已接纳基础工具族。

```bash
cd research_notes/reconstruction_20261023
python -m unittest -v test_boolean_sumset_tools.py
PYTHONPATH=../../src python observer_quotient_demo.py
python replay_prefix180.py --run-dir /tmp/em-direct-replay-unique
python atlas_query.py --kind claims --limit 3 右同余
python atlas_query.py --kind tools --limit 3 modular
```

`--run-dir`指定一个尚不存在的新目录；大日志与编译产物留在该本地目录。
重放脚本只生成直接家族，不需要旧REFERENCE_PREFIX179。

## 440包的检索层

[包目录](atlas/packages.json)、[原文定理主张摘录](atlas/theorem_claims.jsonl)、
[工具接口索引](atlas/tools.jsonl)覆盖全部440个原包的直接成员。
共检出1,119个定理标题/主张出现项，去重后1,025段；1,303个Python/C++源出现项，
按源字节去重975份。所有440包都有程序源候选，383包有匹配到的定理文字。
Python源全部通过AST解析；这只证明可解析，没有执行或验证其全部数学结论。
57包没有匹配到标题，不意味着没有定理；20个嵌套ZIP没有在本检索层再次展开。
1025是去重文本片段数，不能称为1025个已证明的独立定理。

源链接定位留在所有者私有原始归档。公开索引用包名、成员路径、成员SHA256和原文行号定位；
原稿中的私人URL已从索引摘录去除。生成器`build_archive_atlas.py`不执行包内代码。

本轮检查：6项工具测试、480个小实例/预算穷举对照、270种(n,e)闭式硬目标比较、
n=7..12满支撑覆盖、两套13点求解实现及全部646个最优见证。
精确搜索的NO依赖已给出的完备递归证明和实际全行运行；形式化核验与独立Driver审查均未声称完成。
