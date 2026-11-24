# 复现说明

本目录保存一次完整的 Driver 来源审阅。固定源是 `awdawmip/power@74b386de5f1ca8dcc662935f563c438e1cfeee7e`；原函数算法未改动。`EVIDENCE.json` 是已执行输出，内含计算口径、短反例、阳性对照、遥测和任务原生读取摘要。运行时长受环境影响，逻辑结果与样本判定才是本次复现比较对象。

## 85/86

把 `probe_85_86.py` 放入空目录，按以下原路径放入固定 POWER 源文件：

- `src/power/weapons/high_dim_cohen_bkz_polytope.py`
- `src/power/weapons/padic_mahler_measure_hyperbolic_lattice.py`
- `src/power/weapons/simultaneous_coppersmith_multi_candidate_lattice.py`
- `docs/grand_unified_asymptotic_algebraic_pipeline_results.json`

运行 `python probe_85_86.py`，标准输出即机器可读结果。脚本提取未修改的相关函数/类，去掉未调用的相对导入与包初始化；实际构基、整数 LLL 和候选扫描均为原代码。Engine 通过 `__new__` 建立，未调用的 isolator 置 None，避免把无关依赖引入这个小型检查。

## 87/89

把 `audit_checks.py` 放入另一个空目录，按原路径放入：

- `src/power/weapons/dyadic_hensel_branch_rigidity_filter.py`
- `src/power/weapons/vectorized_bitmask_dyadic_sieve.py`
- `src/power/rsa280_spec.py`
- `docs/vectorized_bitmask_dyadic_sieve_results.json`

运行 `python audit_checks.py`。Python namespace package 直接加载这些原样模块，不需要仓库 `__init__.py`。`sys.settrace` 仅读取原函数的局部状态，不写入或改变函数控制流。输出为 `audit_checks_results.json`。

## 88

把 `check_synth.py` 放入另一个空目录，将固定源 `src/power/weapons/co_optimized_asymptotic_algebraic_synthesizer.py` 按原字节保存为同目录 `synth_code.py`。运行 `python check_synth.py`。

脚本核对原文件 Git blob `217aa66a9a4fd255333a9d49241ce89a4e39a121`，再提取未修改的静态解码方法。输出 `check_synth_results.json`。该检查只证实通用早停判据反例和 slack 公式，不是综合管线或 RSA 长时运行。

## 任务状态证据

`EVIDENCE.json.task_status_snapshot` 保存固定 Source 的目录读结果和每项原生读的 request_id、实际状态、Source 与时间。新四项最终精确状态请求为 `power-progress-current-task-20261124-01` 至 `-04`，均已 SUCCEEDED；实际观察时间见 REPORT 状态附录。旧任务额外实时读没有作为交付前置，其 owner 不从未完成请求推断。CRT 已接受结论来自固定 Source 下精确 Result 和 Review 正文。

本次未运行全仓 pytest；因数分解计时不存在同硬件全链基线。前轮状态精度的 15,625 状态验证及旧稀疏报告的279项验证作为明确历史证据复用，没有记作本轮新运行。
