# 复算固定表直径与免表尾部传输

从本说明所在目录运行。将 `EM_SOURCE_ROOT` 设为 Enterprise Math 源码树的位置。参考快照为 `7b32ae2ad9d1c13a13ff4668d1d218adda99390d`。三个脚本均用 Python 标准库，原测量用 CPython 3.12.14，正常模式运行以执行断言。

```sh
export EM_SOURCE_ROOT=/path/to/enterprise-math
python deletion_work/check.py
python tailwork/verify.py
python tailwork/ablation.py
```

- **删除核。** 冻结内核源于 `c4d450536bf71ed87fd74555295ec60485262f0a`，其 Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176` 在上述参考快照相同。脚本校验内核，逐一枚举四种端点模板各 1,296 个有序来源。最后输出 `W 1e-18 enclosure 21728677752503435 21728677752503436`。这两个整数各乘以 10⁻¹⁸ 即为切向宽度的上下界。[冻结删步任务](https://github.com/awdawmip/enterprise-math/blob/7b32ae2ad9d1c13a13ff4668d1d218adda99390d/research_tasks/RS-X6-DELETION-FIXED-TABLE-PHASE-RANGE.md)
- **免表尾部。** 冻结传输入口是 `24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14` 下的 `src/enterprise_math/brc_table_free_tail.py`，其 Git blob `aaef03c9d8e68de5ace75b6736d1169faa4b2918` 在参考快照相同。首个脚本输出 `checks (52119, 381, [24700, 27204, 215])`，随后测量九组规模和阶数。第二个脚本用相同输入检查共享版与重复求幂版的完整结果，并测量四组配对时间。计时随机器、解释器和负载浮动。原测量见 `tailwork/measure.txt` 和 `tailwork/ablation.txt`。[冻结传输实现](https://github.com/awdawmip/enterprise-math/blob/24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14/src/enterprise_math/brc_table_free_tail.py)

移植复验从另一工作目录启动，清除预设的 `PYTHONPATH`，三个命令均通过。所有整数检查和校正次数与首轮相同。复验中，重复求幂版耗时与共享版耗时之比的配对中位数，按 (188,2)、(1128,8)、(3482,2)、(3482,32) 依次为 1.006、1.078、0.991、1.001；其中 3482 位二阶组在两次测量中跨过 1。共享公式确定地少算一次大幂，各输入上的实际加速幅度须以本机计时衡量。
