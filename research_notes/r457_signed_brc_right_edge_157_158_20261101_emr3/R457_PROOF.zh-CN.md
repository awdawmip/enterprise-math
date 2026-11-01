# R457｜signed BRC 右边缘 s=157、158 的无限参数正性及 r=181 的完整 PF₃

日期：2026-11-01。科研状态：AUTHOR_SIDE_EXACT_INTEGER_SYMBOLIC / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。

## 已固定来源与权限

GLOBAL_KNOWLEDGE_V1: `main@c1d957ec4b54c76df0d5ddcecf4b8f6f6f319f1e`。此一不可变快照读取了两项规范入口、项目 TASK_RESEARCH 入口、P000 原件（blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`，与 P000_STARTUP 相符）、ACTIVE 世界观、研究及代码规范。Enterprise Math 主干读取固定 `main@f3e38a72335239e95d2b020d782b7e67b98c006e`，含 `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`、`docs/PORTABLE_RESEARCH_PROTOCOL.md`、`control_plane/current_control_authority.json` 与适用的 BRC 运算约束。

直接数学输入是 R456 的证明及源程序，固定不可变提交 `12deaa67dc16d629e1cae3cb29fda351a2eaa849`；局部 PF₃ 判据取 R450 `6d79677bda1fbce91c8b5f5af70dc830a33bd9dd`，左端 j≤22 证书取 R447 既有结果。所有继承定理均维持作者侧、未经独立接纳的原始强度。

GitHub 认证为 awdawmip；原生 Gateway v0.6.11 status 显示 `research_authority_granted=false`、`CODE_REVIEW_REQUIRED`、主体活跃作业 5/5。无法由该状态确认当下 live owner。本轮没有 CLAIM、Result、Driver Review 或规范接纳。本提交仅保全可移植研究草稿，不触碰正式 owner 或活动状态机。

## 精确对象

奇数 r=2k+1，2≤s≤r，Catalan 数 C_n=binom(2n,n)/(n+1)，原始 signed 辅助系数

```text
H(r,s)=binom(r+s,2s) [t^r] (1-t)(1+t)^(2s)(1+t²)^(r-s).
a_j=H(r,r-j), j=0,...,r-2; 支撑外 a_j=0.
D2_s=a_s²-a_(s-1)a_(s+1).
D3_s=a_s³-2a_(s-1)a_s a_(s+1)+a_(s-2)a_(s+1)²
     +a_(s-1)²a_(s+2)-a_(s-2)a_s a_(s+2).
```

沿用 R452/R456 的等价式（这里的下标 s 是原始 H(r,s) 的参数；Toeplitz 列位置 j=r-s，不得混用）：

```text
H(2k+1,s)=binom(2k+1+s,2s) * Σ_{q=0}^{floor((s-1)/2)} binom(s-1,2q)4^q C_(k-q)
B_s(k)=H(2k+1,s)/C_k
(2s)! B_s(k)=E_s(k) O_s(k) R_s(k)
E_s=∏_{v=0}^{s-1} 2(k+1-floor(s/2)+v)
O_s=∏_{v=0}^{floor(s/2)} (2k+2v+1)
R_s=Σ_{q=0}^{m} binom(s-1,2q)2^q ∏_{h=q}^{m-1}(2k-2h-1) ∏_{d=0}^{q-1}(k+1-d)
m=floor((s-1)/2).
```

以上是带符号卷积的精确代数等价改写，不将 signed 支路解释成正 BRC 质量，更不是原生 X6 计算。

## 本轮新增定理 A（严格无限参数证书）

对于 s∈{157,158}，所有整数 k≥floor((s+2)/2)，都有 D2_s>0 且 D3_s>0。

**证明**：逐 s 取 k₀=floor((s+2)/2)，u=k−k₀≥0，F=(2(s+2))!。对 t=s−2,...,s+2 令 Q_t(u)=F B_t(k₀+u)，由上述 EOR 分解 Q_t∈Z[u]。令 A=Q_s、B=Q_(s−1)、C=Q_(s+1)、D=Q_(s−2)、E=Q_(s+2)，则

```text
P2=A²−BC,
P3=A³−2ABC+DC²+B²E−DAE,
D2_s=C_k² P2/F²,
D3_s=C_k³ P3/F³.
```

`R457_VERIFY.py` 在 Z[u] 上以 Python 任意精度整数精确生成、穷尽扫描 P2/P3 的**全部系数**，返回：
- s=157：k₀=79，deg(P2)=628、deg(P3)=942，共1572个系数全部严格正，SHA256 `aa234c8c301ba38e74bd3599c2c3f4f289fa0e105c816ef9f77aff08eaaba0a2`。
- s=158：k₀=80，deg(P2)=632、deg(P3)=948，共1582个系数全部严格正，SHA256 `8e5b2e2e0cc1e5fcf332dc8d8e9f7201ac065c15dbf2228b7585c76fd1697ea4`。

共 **3154个系数严格正**、两个完整的 Desnanot–Jacobi 多项式恒等式 `A P3=P2²−(B²−DA)(C²−AE)` 精确相等；每个 s 在 k=k₀,k₀+1、五个 t 上核对原始 signed H 和 Catalan 表达式，分别20次精确等式。全部系数正保证任意 u≥0 时 P2、P3 严格正，故定理成立，不依赖有限 k 抽样。证书编码及完整重建过程见实际执行源码与 JSON、日志。

## 推论 B（拼接至 r=181）

结合 R452—R456 的 2≤s≤156 证书，本轮得到所有奇数 r≥161 对 s=2,...,158 的相邻 D2、D3 严格正。对 r=181，左端 j=0,...,22 已有 R447 证书，余下 j≥23 时 s=r−j≤158、s≥2，均由右端覆盖。由 R450 局部充分判据，`T^(181)` 是整个半无限矩阵 PF₃；连同已有区间，得到所有奇数 `99≤r≤181` 的作者侧 PF₃ 拼接链。这里的新参数为 **r=181**。

独立整数行检验 `R457_ROW_VERIFY.py` 对 r=181 的 180 个系数、180 个相邻二阶及180 个相邻三阶子式做完整判号：**540项全部严格正**，另有10次 signed 原式、10次交替 Catalan 等式交叉检查；完整串行结果 SHA256：`959b66547b21701fc5168e50309853cf7bd5e2296617752654ff9c2203ae395f`。此行的有限穷尽可直接交叉验证拼接结论，不替代定理 A 的无限参数证书。

## 复现、局限与下一单元

分别运行 `python R457_VERIFY.py 157 157`、`python R457_VERIFY.py 158 158`、`python R457_ROW_VERIFY.py`。程序按各自目录输出 JSON；既有终端日志在相应证据文件中以 HASH 和逐行摘要留存。本轮两个 s 单独运行确实分别获得 `R457_EXACT_PASS`；整行获得 `R457_ROW_EXACT_PASS`。更宽的连续批量尝试在运行环境被中断，不属于通过的证明范围。

定理限于原始 signed BRC **辅助标量**，不证明全部奇数 r≥99 的全矩阵 PF₃，不证明整个半无限参数族，不等价于原生三维切片、六维 X6 过程或心跳残差观测。正权 BRC 和 signed cancellation 不混用。P000 与 ACTIVE 世界观未修改。

下一研究单元是 s=159 的独立系数证书。更优先的非枚举问题是：在 E_s O_s R_s 分解下，能否给出任意 s≥2 的 `D2_s>0` 与 Turán 后继 `D3_s>0` 的统一解析归纳证明？若非正多项式系数出现，必须求实际整数 k 的子式符号以区分证书缺陷与数学反例。

本稿为同一研究线程作者延续的实证保全，尚未取得独立评审或正式 STATE_MACHINE admission。
