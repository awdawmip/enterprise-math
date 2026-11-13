# R345｜BRC Newton 内区 TP₂ 正性：无界余阶带扩展至 300 条

状态：**AUTHOR_SIDE / EXACT_COMPUTATION_ASSISTED / CONDITIONAL_ON_R330 / UNREVIEWED / NOT_ADMITTED**。此处的六边有序 BRC 是独立辅助组合模型，不能将该模型自动提升为 P000 心跳世界原生 X6 Cell 动力学定理。

固定账户知识快照：`awdawmip/chatgpt-global-knowledge main@75eb1260e8d5d61a1f075ab675984d3f94d4ea55`；开始时项目 `main@55abd52563ee8b722ecbdd770547eda9fe64d678`。已读取 `00_BOOTSTRAP.md`、`OPERATING_MANUAL.md`、P000、ACTIVE 世界观及 portable research 协议，未修改保护内容。本研究以 R344（`618c5976eea8ab587f21392974d814a11da4ef94`）为精确前沿，新增 `r=256,...,300`。

## 1. 原始对象与依赖

令 `B_0(t)=1+t`，`B_s(t)=J_s(t)+Σ_{i=1}^{min(12,s)}K_i(t)B_{s-i}(t)`。所有 K/J 系数和有符号高次尾项均由 `R345_VERIFY.py` 的 `K,J` 给出，未提前删除域外负系数。定义

[
D_{q,k}=sum_{v=0}^k(-1)^{k-v}inom{k}{v},2^{q-v}[t^q]B_{q+v}(t),
quad 0le kle q,
]
[
M_{q,k}=D_{q,k}D_{q+1,k+1}-D_{q,k+1}D_{q+1,k}.
]

**载重前提（R330；作者侧，尚待独立审查）：** 对任意整数 `r,u≥0`，

[
D_{r+u,u}=5^u H_r(u),quad H_rinmathbb Q[u],quaddeg H_rle r.
]

对 `r=0,...,301`，本轮从原始递推重新构造 `H_r(0),...,H_r(r+1)` 的全部所需点；检查次数界的额外差分 `Δ^{r+1}H_r(0)=0`。这些有限一致性检查不替代 R330 的全指标证明。

## 2. 相邻二阶子式的无界条件正性

对 `r=q-k≥1` 定义 `L_r(v)=5^rH_r(v)` 和

[
Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1).
]

直接逐项代入得

[
M_{r+k,k}=5^{2k+1-2r},Q_r(k-1),qquad kge1. 	ag{1}
]

由 R330 次数界，`deg Q_r≤2r`。本轮对每个 `1≤r≤300`，精确计算完整 Newton 差分列

[
t_{r,i}=Delta^i Q_r(0),qquad 0le ile2r.
]

**验证结论：90,600 项 `t_{r,i}` 全部严格大于零**。相比 R344 的 `1≤r≤255`（65,535 项），新增 `256≤r≤300` 的 **45 条斜带、25,065 项完整正差分系数**。由 Newton 精确插值

[
Q_r(v)=sum_{i=0}^{2r}t_{r,i}inom vi>0
quad(vinmathbb Z_{ge0}),
]

结合 (1) 得到作者侧条件定理

[
oxed{M_{q,k}>0quadorall kge1, 1le q-kle300.}	ag{R345-A}
]

这里的 `q` 随 `k` 沿带可无限增长；**未证明全部 `q,k` 或余阶 `r≥301` 的内区 TP₂**。

## 3. Catalan 最高 Newton 系数

原始 H 的最高 Newton 系数满足 `Δ^rH_r(0)=6^r`（本轮复验 `r≤301`）。于是 L 的最高幂系数是 `30^r/r!`。比较 Q 的最高幂系数，

[
[v^{2r}]Q_r(v)=30^{2r}
left(rac{1}{r!^2}-rac{1}{(r-1)!(r+1)!}ight).
]

从而

[
oxed{Delta^{2r}Q_r(0)=30^{2r},rac{1}{r+1}inom{2r}{r}
=30^{2r}operatorname{Cat}_r.}	ag{2}
]

`r=1,...,300` 的 **300 项恒等式**全部与原始递推计算一致。正的最高项本身不足以保证其它系数为正，其余项已独立穷尽检验。

## 4. 非相邻内区 TP₂ 薄楔推论

从本轮重新构造的 `H_r` Newton 系数正性、R330 次数界可得本次所用 D 元素全部正；超过本次 `r≤301` 范围的 D 元素不由本轮声称。考虑

[
1le k<ellle q<p,qquad p-kle301.
]

在合法矩形每个相邻二阶位置 `(a,j)` 均有 `1≤a-j≤300`，故 (R345-A) 保证严格正；对正元素取比例，逐行望远镜，再逐列相乘，得到

[
oxed{D_{q,k}D_{p,ell}-D_{q,ell}D_{p,k}>0.}	ag{R345-B}
]

此结论只覆盖 `p-k≤301` 的薄楔，而不是全局二维全非负性。R339 在 `k=0` 的负二阶反例、R342 的内区负三阶反例继续有效。

## 5. 复现与证据

运行 `python R345_VERIFY.py --max-r 300 --out R345_EVIDENCE.json` 即可无外部输入从完整 12 项带符号 K/J 整数递推重建证书。可额外传入既有 `--prior R331_INTERPOLATION_EVIDENCE_256.json` 和 `--r332 R332_EXACT_EVIDENCE.json`，完成对前33153项 H Newton 系数逐项比对、R331 摘要和 R332 的44条带端点/次数摘要逐条交叉核对。

实现使用任意精度整数与 `Fraction`，在 `B_s` 的 `s≤905` 区间截断于 `t^{603}`。因为全部所需 `[t^q]` 指数满足 `q≤603` 且递推的乘积只有非负幂，截断不影响任何所需系数；所有有符号尾项在保留的次数范围内原样参与。无浮点符号推断。

新增 `r=256..300` 系数的规范 UTF-8 `r,i,decimal_difference\n` 序列 SHA256：

`5835f388f9a78bbcde8bff10a4ff5bfa85364794a8658084efb48526d5fbb136`

全部 `r=1..300` 的序列 SHA256：

`5f897213f1bc399a6f649b7a9bb3932a1d670cbae4eb7baa98a08eee96c9b384`

R344 原有 `r=1..255` 65,535 项摘要复验为 `6b3f762cada37f8b00a51541a2568d93633911d6839fe0fee9bcf2ebf85aa795`。实际机器证据、复现程序及后继问题分别见本目录 `R345_EVIDENCE_SUMMARY.json`、`R345_VERIFY.py`、`HANDOFF.md`。

## 6. 结论边界与下一问题

**类型：计算辅助的作者侧条件证明，不是独立接纳。** 尚欠 R330 有理抽取及全 r 次数界的独立数学复核；没有获得原生活跃 Task Owner / CLAIM / Source Result、独立 Driver 审查或 Working Truth、Foundation 晋升。

下一最小单元：针对 `r=301` 的完整 `Q_{301}` Newton 正性/首个非正精确系数（需要 `H_{302}`），以及对 `r,k` 同时增长的统一正锥机制或真正内区 TP₂ 反例。继续独立审查 R330 核心引理。
