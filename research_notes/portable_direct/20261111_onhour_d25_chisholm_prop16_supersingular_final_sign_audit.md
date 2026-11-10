# D25 / 原始 supersingular Proposition 16：两个相邻印刷符号的精确不相容证书

日期：2026-11-11 Asia/Hong_Kong。身份/来源：TASK_RESEARCH，声明原 Research logical lane `chatgpt-research-onhour-enterprise-math-20260923`；与维护 lane 分离。本文件是 **AUTHOR_SIDE / EXACT_SOURCE_AND_MODULAR_AUDIT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0_EXECUTION**；不构成任务 CLAIM、原生 checkpoint、Result 或独立审核。

母目标：`ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`；Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`；publication `TP2-B6F4FC938FF94941C1B7`；原冻结科学 pin `c47e13e4aba0e006366f989d6334d443f6333ae3` **不变**。

## 1. 新的、精确限定的来源审核问题

Chisholm–Deines–Long–Nebe–Swisher (2013), *p-Adic Analogues of Ramanujan Type Formulas for 1/π*, Proposition 16 的 supersingular 证明在同一页同时写出：

- 命题规定 supersingular 的符号为 `sgn=-1`，且 `a(p-1)b(p-1) ≡ sgn*b2 (mod p² A)`；
- 证明得到 `a(p-1)b(p-1) ≡ -b2 (mod p² A)`；
- 紧接着一句称 `(a(p-1)b(p-1)-b2)/p` 位于一个 ramified extension 的极大理想，并以此作结束论证。

作者 PDF 预印本标示页18（PDF 从零编号页17）：
https://www.math.rwth-aachen.de/~Gabriele.Nebe/papers/Ramanujan.pdf
期刊 2013 版本 Section 5、Proposition 16，含相同的以上两种符号：
https://www.mdpi.com/2227-7390/1/1/9

**本轮结果：后两种符号结论不能在奇素数且 `v_p(b2)=1` 时同时成立。** 这是印刷证明最后一行的局部校核结论，既不是原论文全部定理的反例，也不是冻结的 D25 LIFT/JT2 反例。

## 2. 全奇素数代数证书

令 `A` 为一离散赋值环，`p>2` 为均匀元，`b2=p*u`、`u in A^×`，`X=a(p-1)b(p-1)`。原文所称 `b2²=±p²` 满足这一单位假设。

若 `X ≡ -b2 (mod p² A)`，则存在 `t in A` 使 `X=-p*u+p²*t`。所以
```
(X-b2)/p = -2*u + p*t,
(X+b2)/p = p*t.
```
第一个表达式为 `A`-单位，因此在任何保持 A 的局部嵌入、延拓其赋值的 ramified DVR 扩张中仍为单位，**不属于极大理想**。第二个表达式确属极大理想。

于是，在原文 supersingular 负号条件下，末段「位于极大理想」所适配的分子是 `X+b2`，而不是印成的 `X-b2`。这一 **符号一致性修正建议** 是来源审核结果，不宣称已完成原论文其余荷载引理的全面独立复核。

## 3. p=373 精确有限证书

取此处纯符号核验的 `p=373`、`p²=139129`、并分别令 `b2=+373` 与 `b2=-373`，`X=-b2 mod p²`：

| 输入符号 | X mod 139129 | ((X-b2)/373) mod 373 | ((X+b2)/373) mod 373 |
|---|---:|---:|---:|
| b2=+373 | 138756 | 371 (= -2) | 0 |
| b2=-373 | 373 | 2 | 0 |

两组精确计算均与全奇素数证明一致；这里的 b2 是**符号条件下的检验输入**，不是新测得的真实 H0/B0 Frobenius 数据。

本轮实际执行的最小整数验证：
```python
p = 373
for b2 in (p, -p):
    X = (-b2) % (p*p)
    assert (X - b2) % p == 0
    assert (X + b2) % p == 0
    assert ((X - b2)//p) % p != 0
    assert ((X + b2)//p) % p == 0
```

## 4. 原生实验可操作的影响、BRC 信息保真

该文 supersingular 算子使用 degree-`p²` 的 Frobenius lifting；证明中还借助在 ramified extension 上的 degree-`p` 中间 lift。符号 `b2`、`-b2`、曲线 `[-p]`、quartic twist、`ω` 与 `ν` 的两个原始列及积分归一化须分别保留。这里采用的观察者是带符号 `X/p` 与 `b2/p`，从 `(X-b2)/p` 到 `(X+b2)/p` 正是非保真合并会错过的第二位差异，故 BRC 分类 `COMPOSE_APPLIED`：在除以 p 之前保留符号、赋值及来源。

**对原生验收的具体修正**：实现者不能把本文末尾打印的 `(X-b2)/p` 当作 supersingular 负号判据；先从原始曲线和 Frobenius/twist/η 证明该符号的对象对应关系，再用 `X+b2` 的候选比较与独立原始输出交叉核对。这个局部审核不能代替真实 `[X]U mod 139129` 计算。

## 5. 接续、状态与下一精确动作

Canonical Source 自身 exact continuation request `onhour11-20261111-0601-exact-cont` 已收到 `SUCCEEDED`；自身恢复 `onhour11-20261111-0600-recovery` 返回 `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`。本轮没有获胜 CLAIM、open run 或 Source 原生写入。Issue #1559 于本轮 fresh GitHub 读取为 `OPEN / PENDING_OWNER`。

最高有效母目标及欠项不变：同一原始 E3/H0/B0 的 divided-power 对象，真实 `[X]U mod373²`、模块秩、`σ` 半线性方向、基底/过滤/η、带符号 κ、Δ-R 和独立复算。冻结 `c47e13e4aba0e006366f989d6334d443f6333ae3`；已完成的 UR/JT0、此前原始 W216 检验、模型 gauge 分类和原论文首位结果均不重做。

**下一精确动作**：有合法原生执行能力者读取原始固定 H0/B0 的操作定义与代码/版本，计算 p373 固定 `[X]U` 并保存双列及带符号证书；应用本源审核对 Proposition 16 的 supersingular 正负号独立核验。若 Source 定义与论文中的 `X`、`b2` 不是同一对象，应记录映射/缺失而不直接移植该检查。支持路径仍为 https://github.com/awdawmip/enterprise-math/issues/1559。

证据等级：**精确全奇素数代数推理 + 2 组已执行的有限整数核验 + 原文 PDF/HTML 符号对照；作者侧未独审、未正式准入，原生 benchmark 未执行。**
