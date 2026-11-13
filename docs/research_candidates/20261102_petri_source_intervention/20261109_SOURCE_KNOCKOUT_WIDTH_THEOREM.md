# 2026-11-09 BRC 来源删除残差：有界支持宽度精确层析（非执行）
**Status:** 作者数学推导 + 本地 Python Fraction 精确检查；尚非 V2 Task/Publication、Result、Review 或 Foundation。

## 问题和查询语义
有限概率历史的来源标签集合为 [m]，每条历史使用的**不同**来源集合为 S⊆[m]；合并历史权重得到 w(S)∈Q≥0，Σ_S w(S)=1。声明删除查询 D(U)=Σ_{S∩U=∅}w(S)。删去含 U 来源的**整条已发生历史**，保留原有权重、不重新归一化；损失质量可作为独立 abort。不同于 Petri 网删转换后重新竞争或重归一化的真实结构干预。

BRC 接口只拟采用正有理质量、来源集合/路径、加法与合法串联；下式中的负号是**派生观察反演**，非原生正权 BRC 算法。X6 保持六条空间轴，来源标签及历史时间另行类型化；此报告未运行原生 typed BRC。

## 定理 A：有界来源宽度的精确恢复
假设 w(S)=0 对全部 |S|>r（0≤r≤m）。只要知道所有 |U|≤r 的 D(U)，数量 N(m,r)=∑_{j=0}^r C(m,j)，就能精确恢复每个 w(S)，并回答**任意阶**来源删除查询。

定义 E(T)=Pr[T⊆S]。对 |T|≤r，有
```
E(T) = Σ_{U⊆T} (-1)^|U| D(U)
w(S) = Σ_{T⊇S, |T|≤r} (-1)^(|T|-|S|) E(T) .
```
证明：X_i=1{i∈S}；D(U)=E∏_{i∈U}(1-X_i)。展开 ∏_{i∈T}[1-(1-X_i)] 得第一式，布尔偏序 Möbius 反演 E(T)=Σ_{S⊇T}w(S) 得第二式。宽度假设消除了 |S|>r 项，因而精确。D(∅)=1 是归一化，余下 N−1 个查询给出全部 N−1 个独立概率参数的可逆线性坐标；仅是线性维度充要性，不是任意有理数编码位数下界。

两次子集变换操作数不超过 2Σ_{j=0}^r C(m,j)2^j 个有理加减，O(N) 个有理表格单元，回答任意 U 需要 O(N) 项筛选求和；位复杂度必须另计分子、分母膨胀。固定 r 时 N=O(m^r)，原始模型需 2^m 个来源集概率参数。

## 定理 B：宽度阈值不能少一阶
对任何 r≥0，令 m=r+1。μ_even、μ_odd 分别在 [m] 的偶数势、奇数势来源子集上等概率分布，每个支持原子质量 2^(1−m)。则全部 |U|≤r 均有 D_even(U)=D_odd(U)=2^(−|U|)，但是
```
D_even([m])=2^(1-m),  D_odd([m])=0 .
```
证明：任何真子集 U 的各固定 0-坐标仍有至少一自由位；完成子集的偶奇计数相等。全体删除仅余空集，它是偶势来源集。r=1,m=2 时两个模型的来源分布分别为 {∅,{1,2}} 各 1/2 和 {{1},{2}} 各 1/2。两种单源删除率均为 1/2，双源删除率为 1/2 vs 0。此 sharpness 是标准奇偶分布低阶边际现象在本查询语言中的精确实例，不主张新发明。

## 运行证书
同目录 `brc_source_deletion_width_20261109.py`，Python 标准库 `fractions.Fraction`，运行检查 m,r=(3,1),(5,2),(6,3),(8,2),(8,3)，分别恢复完整 w 并穷举 2^m 个删除查询；另检查 r=0..6 奇偶反例。**本地全部 PASS**，没有浮点。m=8,r=2 时 N=37 而无约束表是 256；(8,3) 是 93 vs 256。没有实测原生 BRC、数据库、真实 Petri 网时间/内存。

## 外部基线与已有项目重叠
- Green, Karvounarakis, Tannen (PODS 2007), *Provenance Semirings*, DOI 10.1145/1265530.1265535。
- Sen et al., *ProvSQL*, 2025 arXiv:2504.12058：完整来源与概率计算实作基线。
- Leemans et al. (PETRI NETS 2025), *Enjoy the Silence, Part II*, DOI 10.1007/978-3-031-94634-9_15。
- Peled, Yadin, Yehudayoff, *The Maximal Probability that k-wise Independent Bits are All 1* (arXiv:0801.0059)。
- EM 现有 A3 continuation-type kernel (Issue #102) 与 Draft PR #1766 的来源干预模型。本次是更强的**多来源、参数化宽度定理与 sharp 边界**，仍须语义查重。

## 下一个真正有增量的研究单元（候选，非 task）
固定 ≤8 来源、≤6 位置有界 1-safe 随机 Petri 网，明确静默转换、时间/观察语言及删除后重新分配的随机转移概率。比较 static trace-deletion 与真正的结构性 `do(delete U)`；找出不能由上述 Möbius 层析直接覆盖的来源—端口/再分配残差反例及充分条件。以精确逐路径枚举、ProvSQL 半环电路和 EM A3 continuation-kernel 为基线，分别计前处理、有理数位宽、查询、验证、存储的总成本。若没有新的结构条件/反例/成本结果，则把材料并入旧任务的外部测试，不重发任务。

**Control boundary:** 当前材料保存在研究候选 PR 的分支，不等于 canonical main 中的 research_tasks / research_task_records；不授予 Task-ID、CLAIM、owner 或执行权。
