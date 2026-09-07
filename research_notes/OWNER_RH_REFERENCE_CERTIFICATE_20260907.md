# eta=9/10 的 N=8 prime+Cauchy reference 精确证书

状态：`AUXILIARY FINITE-MATRIX CERTIFICATE / EXACT VERIFIED / SOURCE BOUND / NOT_FOUNDATION`。
日期：2026-09-07。生产者 `/root/exact_solver`；独立有理惯性工具 `/root/stability_research`；复用数学及新源码审查 `/root/branch_scout`；owner 负责最终集成。不是正式 task、claim 或 Researcher-ID。

## 1. 冻结目标及当前真实结果

目标是四标签正弦分支 O-、O+、S-、S+，每支 k=1..8 的 32 维子空间，eta=9/10 的 cutoff-free 参考矩阵

`H_ref = [[81/100 A, B_prime+B_Cauchy],[(B_prime+B_Cauchy)^T,D]]`。

A、D 都保留完整 arch、有限 prime 和两个 pole 通道；reference cross 排除 pole cross 和 regular arch cross。标签、归一化、支撑与原 first-step 完全相同，不作 parity/inversion 合并。

生产 run002 已得到完整严格条目包围。owner 随后用独立标准库 Fraction 证书器验证：`M-delta I` 与 `M+delta I` 均为 **8 负、24 正、0 零**，所以实际区间内的 H_ref 也有恰好 8 个负特征值。候选 q=8 没有作为证书器事实输入。

该次有理误差为

`delta = 2024912878742577611153949018957860044801 / 91343852333181432387730302044767688728495783936`，

约 2.22e-8。最终 `reference_inertia_report_run003.json` 记录 status CERTIFIED、verification_complete=true、scope INPUT_INTERVAL_FAMILY_ONLY；它的输入 SHA 与来源绑定 run003 一致。条目确实包围指定参考矩阵的语义另由 producer/reuse 数学审查负责。run003 的 eta、labels、bounds 与 run002 的规范 JSON 逐字一致，故 owner 重绑并重验同一精确惯性核心；旧 JSON 没有补写事后来源字段。

## 2. 数学构建与实际工作量

复用脚本 `scripts/rh_log3_n8_arb_certificate.py` 的 SHA256 是 `4e337855d8605125ded80c029022fdc950d1b92cf78ce772480a7b99b9dad49b`，owner 已确认与历史 source head `d0a4eca2a49a9167848ba4d5d5cfd7eb03d355f7` 的同文件逐字节一致。本轮仅调用其对角、prime、pole 构建函数，没有执行旧 eta=1 正定验证。

参数实际为 K=256、P=10、384 bits，使用 exact prefix + Hurwitz-zeta tail + explicit remainder balls。新消费者对全部 product denominator 的 `1-rho>0` 做 Arb 严格判断，不把 K 足够收敛误当误差足够惯性。独立推导见 `OWNER_RH_REFERENCE_REUSE_AUDIT_20260907.md`。

Cauchy cross 对每一 old/shell 对先按真实区间左右排序，再计算 `-1/2 integral_0^C0 L_ij(c)dc`。C0=20000；有限求积在 16 个 dyadic panels 上调用官方 acb.integral meromorphic 回调。每条目加入 `10240/C0^3=1.28e-9` 的明示绝对尾球；没有解析尾加速或无界提高 C0。

实际 run002 完成 256 条目、4096 panels、174828 次回调，复用已保存组件后约 2.99 秒。数学资源限制为每 panel 4000、每 entry 100000、全 run 2000000 evaluations、depth20、degree32、容差目标 2^-60。容差目标不是自动成功标记；返回真实球，过宽时交独立惯性层判未定。

所有 arch/Cauchy 尾、有限求积误差和舍入均包含在最终 bounds 中。没有另外的 arch 频率 cutoff，不重复加旧 T=2000 PSD 尾。

## 3. 证据、导出及错误处理

生产源码为 `experiments/owner_rh_reference_20260907/reference_builder.py`，运行及数学合同详见同目录 README。矩阵顺序是 O-1..8、O+1..8、S-1..8、S+1..8；每条目导出 exact rational `{lo,hi}`，上下三角镜像。

每个球先取 Arb directed lower/upper，再用精确 mantissa/exponent 做向外 2^-160 dyadic 舍入，增加每端误差小于 2^-160。没有读取显示字符串生成证书。该设计修复 run001 中极小半径分母超过 Python 4300 字符限制的表示错误；run001 的 UNDETERMINED 及有效组件缓存均保留。

run002 生产后只增加了显式 trusted cache SHA 合同和 `producer_source_sha256` 字段。旧 run002 JSON 不修改。其历史源码通过反向应用唯一已记录后置补丁得到只读 snapshot，并明确注明该恢复方式；不将恢复时算出的 SHA 冒充运行时采集值。最终 source-bound run003 的比较已经 PASS，来源及组件显式可信哈希都经独立核对。

独立接口负测还确认：缺失或错误 trusted cache SHA 在零次积分回调时拒绝；entry_eval_limit=1 的测试经 python-flint 的 SystemError 异常链后，由顶层返回 UNDETERMINED、无 bounds，未出现假 ENCLOSED。该后端在异常展开期间共调用 12 次回调，因此本实现不声称 callback 内的 Python 异常会干净原样传播，也不声称触发预算后外部库绝不再回调。

最终文件绑定如下，均位于 `experiments/owner_rh_reference_20260907/`：

| 文件 | SHA256 |
| --- | --- |
| `reference_builder.py` | `67a15aaebe4a27b59dd29b1e833da456e85581705eb601eeba712818c37f92ca` |
| `reference_bounds_run003.json` | `385ea5b8806f302b6bf403842a0ae496233f67227841c8e5c320ff82f5e9453a` |
| `reference_inertia_run003.json` | `8d962dc8b4018e0aac5e349171db1dde80941bf3abff8115797433324a6022ba` |
| `reference_inertia_report_run003.json` | `035c011386ae2153ac3704bc9b8997223cf1dc710f7ef2dd7f7ed6f72b49f48b` |
| `reference_run002_run003_comparison.json` | `018f7f2ced5ab51686e008feb043e0a29e75d4f50dc3ac1feefeaea460ef579d` |

组合后的 bounds/labels 规范 JSON 哈希是 `b0324548bc6f86843a23075b8ae32eefedb8b78e9c9d4f84f4724db625928559`。不扩大 K、P、C0，不对其他 eta 自动外推。

## 4. 结论边界

这是一个明确的有限矩阵 reference 惯性结论。它不等于 full-cross 惯性，不等于 eta=1 的完整 Gram 正定性，不涉及 Galerkin complement，不证明整个 H_log3 或 RH。没有改变 P000、原生 X6 空间轴、分支标签或任何物理动力学合同。

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
