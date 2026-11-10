#!/usr/bin/env python3
"""Render the phase-three report from the completed, frozen measurement."""
from pathlib import Path
import csv
import json

root = Path(__file__).resolve().parent
j = json.loads((root / "analysis_summary.json").read_text())
execution = json.loads((root / "execution_all_frozen.json").read_text())
freeze = json.loads((root / "frozen_manifest.json").read_text())
assert execution["result"] == "PASS" and j["conditions"] == 24 and j["rows"] == 624
run = execution["commands"][-1]
receipt = json.loads(run["stdout"])
fresh = [x for x in j["condition_results"] if x["stage"] == "heldout"]
combined = "selection_combined_1024"
selection = "selection_density_gap_1024"
fused = "selection_fused_1024"
previous = "adaptive_combined_1024"
cf = j["stage_summary"]["heldout"][combined]
rows = list(csv.DictReader((root / "results_all.csv").open()))
by = {(r["family"], r["algorithm"]): r for r in rows}

def table_fresh():
    lines = ["| 新条件 | n | 上一版 µs | 只改输出 µs | 只改选择 µs | 组合 µs | 最快旧对照 | 对照 µs | 对照/组合 |",
             "|---|---:|---:|---:|---:|---:|---|---:|---:|"]
    for c in fresh:
        t = c["median_us"]
        lines.append(f"| {c['family'].removeprefix('selection_fresh_')} | {c['n']:,} | "
                     f"{t[previous]:.3f} | {t[fused]:.3f} | {t[selection]:.3f} | {t[combined]:.3f} | "
                     f"{c['best_control']} | {c['best_control_us']:.3f} | "
                     f"{c['speedup_vs_best_control'][combined]:.3f}× |")
    return "\n".join(lines)

def table_summary():
    lines = ["| 固定新策略 | 对23旧对照胜出 | 至少1.10倍 | 至少慢10% | 对照/新版几何平均 | 上一版/新版几何平均 |",
             "|---|---:|---:|---:|---:|---:|"]
    for name in (fused, selection, combined):
        s = j["stage_summary"]["heldout"][name]
        a = s["control"]
        lines.append(f"| {name} | {a['median_wins']}/12 | {a['at_least_10pct_speedup']} | "
                     f"{a['at_least_10pct_slower']} | {a['geometric_mean_ratio']:.3f} | "
                     f"{s['previous']['geometric_mean_ratio']:.3f} |")
    return "\n".join(lines)

def table_work():
    lines = ["| 条件 | 算法 | 根残差 | 全递归输入总量 | 成功节点输出写入总量 |",
             "|---|---|---:|---:|---:|"]
    for family in ["adaptive_fresh_tail_7pct_high", "selection_fresh_tail_8pct_high",
                   "selection_fresh_tail_8pct_low", "selection_fresh_tail_12pct_asymmetric"]:
        for name in (previous, fused, selection, combined):
            r = by[(family, name)]
            lines.append(f"| {family} | {name} | {float(r['spills']):,.3f} | "
                         f"{float(r['recursive_input_total']):,.3f} | "
                         f"{float(r['total_output_writes_total']):,.3f} |")
    return "\n".join(lines)

text = f"""# BRC 残差排序：密度选择、间隙修复与直接输出

日期：2026-11-10。研究记录：`EM-DIRECT-10677F / TASK_RESEARCH`；活动：`RA-851F29EFE6B4190069FE0D3B`。

## 本轮结果

本轮把“分组能覆盖多少样本、要花多少计数槽”和“怎样把计数与残差写成最终数组”分开实现，再组合测量。
在冻结后的12个新种子条件中，组合版相对上一版有 **{cf['previous']['median_wins']}/12** 个中位数胜出，速度比几何平均 **{cf['previous']['geometric_mean_ratio']:.3f}**；
对同场最快的23个既有对照，胜出 **{cf['control']['median_wins']}/12**，其中 **{cf['control']['at_least_10pct_speedup']}** 项达到至少1.10倍，
**{cf['control']['at_least_10pct_slower']}** 项至少慢10%，速度比几何平均 **{cf['control']['geometric_mean_ratio']:.3f}**。
完整表保留所有失败条件，并分别报告固定变体，不逐条件挑选最好的新版本拼接总成绩。

数学上得到两个具体结果：一是成功计数节点的最终值输出可以恰好写n个元素；二是给出了最多两次间隙修复就能恢复小计数表的20簇输入族。
这些结果推进了有局部结构的整数排序；完整实现的固定字长复杂度类别仍与既有线性整数排序一致。

本次所有旧对照均重新编译并同场计时。宿主已经变为 **{execution['cpu']}**，编译器为 **{execution['compiler']}**；
没有把此前Intel宿主上的绝对耗时与本轮AMD耗时直接相除。

## 1. 实现对象与三个消融版本

输入是有限`uint64_t`自然数多重集合，输出是完整的数值非递减数组，保留重复次数。BRC分组是中间表示：每个实际出现次数进入精确计数或显式残差。
当前接口只返回数值，不涉及附带记录的稳定次序。

前一轮源码固定在[第二轮提交](https://github.com/awdawmip/enterprise-math/tree/1001e80fd510c8de6a9761dc20068e0e3c8c671d/experiments/brc_residual_sort_adaptive_20261110_b0e94005)。
本轮保留此前23个实现，增加以下三个版本：

| 实现 | 选择分组 | 输出 |
|---|---|---|
| `selection_fused_1024` | 原逐级修剪与局部放弃 | 按区间直接输出 |
| `selection_density_gap_1024` | 密度装组与多数侧间隙修复 | 原计数展开加逆向归并 |
| `selection_combined_1024` | 密度装组与多数侧间隙修复 | 按区间直接输出 |

样本量`S=min(n,1024)`；小于等于256的节点用`std::sort`；递归深度到16用偏移基数排序；计数预算为
`min(2^22,max(4096,floor(n/2)))`个槽。跨度和比值交叉乘法使用128位中间值。

原始连续区间或完整网格能满足预算时直接复用。否则把正宽度分组按“样本观测数/填充后宽度”递减排列，
比值相同时依次按观测数较多、宽度较小、原编号较小排序。整组能放入剩余预算便保留，不能放入便跳过。
只有保留至少`ceil(原始S/2)`个样本观测，提议才通过。

若密度装组失败，将原样本排序一次，在当前窗口中寻找最大的可用正间隙：至少一侧保留原始S的一半，保留样本较多的一侧，
两侧相同时保留低值一侧；间隙相同时用较低切点。重新建立网格并尝试连续区间、完整网格、密度装组，最多切三次。
相等值不会被切开，分母始终是原始S。第一个可行模型只接受一次真实扫描；实际残差超过`floor(n/2)`便停止并回退完整原数组。

## 2. 为什么直接输出能少写

保留的计数区间有序、互不重叠。实际扫描把落在这些区间内的每个值全部计入，故真实残差不在任何保留区间中。
残差递归排序后，可以在每个区间之前二分定位并复制较小的残差块，然后展开该区间计数，最后复制残差尾部。
每个成功节点的n个最终输出值恰好写一次，不需要另分配n大小的输出数组。

设该节点有e个残差，旧逆向归并的元素写入数为W。当e>0：

`W = e + 计数部分中严格大于最小残差的出现次数`。

因此旧计数展开加归并共写`n + 上述出现次数`，直接输出节省`W-e`次按元素计的输出写入。
当残差全在高端时可以完全不省写入；低端残差则可能迫使大量计数值在旧归并中再次移动。高低镜像输入用来检验这种方向效应。

当前实现每个保留区间做一次`lower_bound`，输出阶段成本为`O(L+n+B log(e+1))`，L为计数槽数、B为保留区间数。
“恰好n次”只指成功计数节点的元素级输出写入，不指机器存储指令、缓存传输或整次排序总工作量；子层、计数更新和回退另计。
证明及边界值处理见[THEORY.md](THEORY.md)。

## 3. 冻结和测量设计

实现、生成器、分析程序和二进制于 **{freeze['frozen_at_utc']}** 冻结，早于校准计时和新输入生成，见[frozen_manifest.json](frozen_manifest.json)。
校准后没有修改三种策略、参数或生成器。

24个条件分为8个精确复用的旧校准、12个新种子条件、4个确定性机制。新条件含5个百万规模输入：8%高端及其低端镜像、12%不对称双尾、
窄范围偏移、全64位均匀数；另有15%高低镜像、常见宽组、稀有宽组、内部污染、128簇加12%尾部、40%不对称双尾。
高低镜像共享同一随机流并作`MAX_VALUE-x`，属于配对评价，不能称为独立分布。

每条件8个输入库、每算法7轮；轮内算法顺序随机。每轮名义目标12毫秒，按完整输入库循环取整，慢算法可能超过目标。
计时包括输入复制、样本学习、分配、完整输出及析构；诊断另跑。26个候选在同一优化二进制中用CPU0串行测量，团队没有同时编译或运行其他基准。
编译参数`-std=c++20 -O3 -DNDEBUG -march=native -Wall -Wextra`。共享云宿主仍有频率和噪声限制。

比较基准是每个条件下23个旧候选的最快中位数。这是回顾性参考，未实现自动选择该算法。速度比定义为“对照耗时/候选耗时”，大于1才更快。
几何平均等权计算条件，未按规模或实际业务比例加权。七轮经验分位数和10%幅度只作描述，不是置信区间或显著性检验。
新分布是依据前轮问题定向设计，不能估计任意业务数据上的平均收益。

## 4. 冻结的新输入完整结果

单位为微秒；所有数据均取正式最终运行，不混用先前校准计时。

{table_fresh()}

{table_summary()}

![全部新条件相对旧对照的速度比](analysis_heldout_speedup.png)

完整24条件表见[analysis_table.md](analysis_table.md)；全部624条算法汇总和七轮计时见[results_all.csv](results_all.csv)。

## 5. 工作量与输出消融

以下为8个输入库的诊断平均。根节点若提前拒绝，残差字段是停止时的前缀数量；不能当作完整输入残差数。
输出写入仅包含成功计数节点的展开与合并，未计入叶子和回退内部写入。

{table_work()}

7%高端条件中的43,591.625降至7,000说明旧修剪把正常主体大量推入残差；新间隙选择在这一家族主要留下真实尾部。
每个输入分别检查更换输出方式前后的模型与实际残差逐节点一致性；配对高低镜像用于分析输出方向效应。
直接输出节省写入不保证每个条件的实测耗时都更小，二分、填充、缓存行为与编译布局也有成本。

## 6. 可证明的修复能力和下一处缺口

20簇充分条件：n至少为1024，簇为`2^62+j*2^20+{{0,...,7}}`，j从0到19；可选尾点为`2^62±2^60`。
原样本严格过半来自主体，每簇的两个端点均出现，实际尾部不超过输入的一半。
样本出现尾部时，初始粗网格把主体合成一个超过预算的宽组；多数侧间隙在至多两次切分中只去掉尾部。没有采到尾部时可直接接受小网格。
恢复后的20簇计数表最多360个槽，实际残差恰好为尾部。这是源码兼容的充分条件定理，不是无分布假设下的普遍保证。

密度选择也有精确反例：宽度`(6,5,5)`、质量`(12,9,9)`、预算10时，贪心只保留12，未达原样本半数15；后两组却能保留18。
单独的精确有限枚举检验了156,250个三组配置，1,629个存在“贪心未过半但某子集可过半”的情况。计数只是这套有限枚举域的结果，不能读成实际输入概率。
程序和实际输出为[selection_certificate.py](selection_certificate.py)、[selection_certificate_results.json](selection_certificate_results.json)。

分数背包上界可以精确拒绝不可能过半的固定网格，质量索引DP可以精确处理其余子集选择。
这两种方法在本轮THEORY中推导，但不属于本轮三个被计时的实现；后续修复需要另冻结、验证并测量其成本。

实际残差减半使递归节点大小总和小于2n，不能据此说所有操作少于2n。固定64位字长、样本/分组上限和深度下，完整实现仍为O(n)时间和O(n)辅助空间。
同样模型下既有基数排序已有线性界，参见[Open Data Structures §11.2](https://opendatastructures.org/ods-cpp/11_2_Counting_Sort_Radix_So.html)。
这不推广为无限精度自然数排序的线性位复杂度，也不构成新的通用复杂度突破。

## 7. 验证和复现

优化构建和ASan/UBSan构建分别通过734个输入数组、4,456次输出检查，其中新版本诊断/nullptr路径4,404次，旧组合消融参考52次。
包括341个穷举短数组、340个提升数组、32个随机边界数组、21个定向条件；8个密度直接用例、48,884个间隙有限检查、6个直接输出用例，覆盖17条路径。
核验每个递归节点实际归属、前缀拒绝、样本门槛、原样本分母、相等值、最大整数及强制深度回退。

正式测量另核验{receipt['validated_input_banks']}个输入库的全部26个算法两条输出路径，共{receipt['validated_algorithm_outputs']:,}次完整数组比较；
产生{receipt['rows']}条性能行、{receipt['trace_nodes']:,}条节点轨迹、{receipt['trace_attempts']:,}条提议轨迹，进程耗时{run['elapsed_seconds']:.3f}秒。
这些检查包括重复次数，与`std::sort`完整输出一致。ASan设置`detect_leaks=0`，未检查泄漏。
唯一最终编译警告来自历史包含文件中从未调用的重命名main缺少返回值。作者侧核对见[REVIEW.md](REVIEW.md)。

验证回执：[优化构建](execution_harness_verify_v2.json)、[ASan/UBSan](execution_sanitized_verify.json)、[正式运行](execution_all_frozen.json)。
详细轨迹：[节点](results_all.csv.selection_nodes.csv)、[提议](results_all.csv.selection_attempts.csv)。

下载[brc_sort_reproducibility.zip](brc_sort_reproducibility.zip)，解压后相邻目录含所有固定源码、此前报告、许可证和本轮证据，不含预编译程序或凭据。

```bash
cd brc_residual_sort_selection_20261110_b0e94005
python run_experiment.py --verify-only --cpu 0
python run_experiment.py --sanitize --verify-only --cpu 1
python run_experiment.py --skip-build --skip-verify --cpu 0 --subset all
python analyze_results.py results_all.csv
```

选择本机允许的CPU编号；需要Linux taskset、支持C++20的GCC和Python标准库，绘图另需NumPy和Matplotlib。
新测量应写入另一个输出路径以保留原始结果。所有结果是本机实测与作者侧证明/审阅，不代表外部独立评审、项目定理验收或新颖性认定。
"""
(root / "README.md").write_text(text)
print(root / "README.md")
