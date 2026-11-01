# R469｜signed BRC 辅助标量右缘 s=217–224 无限 k 的精确证书与 PF₃ 条件拼接

日期：2026-11-02。证据类型：作者侧精确整数、符号计算证明；完整半无限 PF₃ 结论依赖以前 R447、R450 等作者侧引理，尚待独立审阅。该模型是 signed BRC 辅助标量，不声称原生 X6 动力学。

## 1. 科学来源、固定输入与研究对象

本轮遵循 GLOBAL_KNOWLEDGE_V1 的现行读取快照 `main@4d8bdb9ad4e90fab69a8dc5d1d22c21b3ed4cd0f`、Enterprise Math 控制快照 `main@90b640853e310b8fdf53dbf1c428dbc77ea8d6de`；P000 已核对启动投影及原文 blob 相符。科学冻结源为 R462 commit `18783e01e3646c72b7aab3b16d3f565e83e6446f`，作者侧最近已验证 R468 commit `1eb6cd74a9337c01464acc0177153c94355bf32e`。冻结公式源码 Git Blob 为 `7c641c985b8c48ef3fb2ddcb2142e38ca0a4ccff`，R468 精确算术源码 blob 为 `9057a6c46814a06cea45bffc20fe6f44f370b0bb`；本轮在本地复用并核实匹配。完整复现指令见 R469_README.md。

对奇数 `r=2k+1`、`2≤s≤r` 定义
\[
H(r,s)={r+s\choose 2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},
\qquad C_k=\frac{1}{k+1}{2k\choose k}>0.
\]
给定 `r` 置 `a_j=H(r,r-j)`（`0≤j≤r−2`），其它 `j` 的 `a_j=0`，并设
\[
D_{2,j}=a_j^2-a_{j-1}a_{j+1},\qquad
D_{3,j}=\det(a_{j+v-i})_{0≤i,v≤2}.
\]

**命题（无限 k、有限 s 集的作者侧精确证明）**：对每个固定整数 `s∈{217,…,224}` 和所有整数 `k≥k₀=⌊(s+2)/2⌋`，取 `r=2k+1,j=r-s`，有 `D₂,j>0` 与 `D₃,j>0`。

## 2. 有限精确符号证书如何给出无限参数结论

对一个固定 s，置 `u=k−k₀≥0`、`F=(2s+4)!`。按冻结 R462 的 E/O/R 多项式恒等式，对于 t=s−2,…,s+2，有
\[
Q_t(u)=F H(2k+1,t)/C_k\in\mathbb Z[u].
\]
记 `A=Q_s,B=Q_(s−1),C=Q_(s+1),D=Q_(s−2),E=Q_(s+2)`。直接计算
\[
P_2=A^2-BC,\qquad
P_3=A^3-2ABC+DC^2+B^2E-DAE.
\]
代入 Toeplitz 行列式并同乘正比例因子，逐点严格等式为
\[
D_{2,j}=\frac{C_k^2}{F^2}P_2(u),\quad D_{3,j}=\frac{C_k^3}{F^3}P_3(u).
\]
`R469_REPRODUCE.py` 调用已发布且未更改的整数 E/O/R 内核。对各 s，完整逐系数确证 `deg(P₂)=4s`、`deg(P₃)=6s`，且 **所有系数严格为正**，共 16 个整数多项式和 **17,656 个正系数**。故每个非负整数 u 上 `P₂(u)>0,P₃(u)>0`，证毕。这不是有限 k 抽样；用任意精度整数、没有浮点误差。

每个 s 另检查完整多项式恒等式
\[
A P_3=P_2^2-(B^2-DA)(C^2-AE)
\]
（8 项），以及 k=k₀,k₀+1、t=s−2,…,s+2 下的原始 signed BRC 卷积和正 Catalan 表达式（各 80 项）。逐参数完整系数流按长度前缀规范编码取 SHA256，8 个数值及次数见 `R469_EVIDENCE_ALL.json`，可用源码全部重算。样本检查仅用于交叉检验，普遍正性来自全系数整数证书。

## 3. 独立有限整行正性核验与条件拼接

对新增奇数 `r=241,243,245,247`，使用与上段不同的正 Catalan 整数表达式
\[
a_{r-s}={r+s\choose2s}
\sum_{q=0}^{\min((r-1)/2,\lfloor(s-1)/2\rfloor)}
{s-1\choose2q}4^q C_{(r-1)/2-q}.
\]
分别对每个 j=0,…,r−2 检验 `a_j,D₂,j,D₃,j>0`，零填充边界同样纳入。每类 972 项，合计 **2,916 项精确整数正性**；在 32 个 (r,s) 点上另比对原始带符号卷积、交替 Catalan 形式各 32 项。独立简化整数实现 `R469_INDEPENDENT_ROW.py` 与完整 `R469_ROW_VERIFY.py` 的系数流和子式流 SHA256 一致：
- 系数流：`86aee71432c6f57db242b935eb5f0616955542b0b2e2b39f9830353faf3fc834`
- D₂、D₃ 流：`19d11c9b9c8b54b169c7e5292cb84ac54030e843416cdf9a98b90104b7b15c21`

历史作者侧左边缘证书覆盖 j≤22，R452—R468 右边缘已覆盖 s≤216，本轮覆盖 s=217,…,224。对奇数 r≤247，若 j≥23 则 s=r−j≤224，因此两边覆盖全部局部位置。**条件为 R447、R450 等左缘与 PF₃ 局部充分判据真实成立**，遂得到
\[
T^{(r)}\in PF_3\qquad(r=99,101,\ldots,247).
\]
这里新增四行 r=241,243,245,247，尚未声称独立 Driver 接纳或从辅助标量推出原生六维物理结论。

## 4. 可复现性、运行范围与待解决点

复用已提交 R468 同目录的 `R462_VERIFY_FROZEN_KERNEL.py` 与 `R468_EXACT_KERNEL.py`（Git Blob 如上）：
```sh
python R469_REPRODUCE.py 217 224
python R469_ROW_VERIFY.py
python R469_INDEPENDENT_ROW.py
```
R468 可选 GMP 大整数加速器不改变运算语义；本轮在执行环境重新编译过加速器。实际 s 计算分组运行以适应调用时限：217–219、220–221、222–223、224 单独运行成功；较长命令遇到时间上限前输出的已完成结果保留，但其余参数使用后续独立运行完成，不将被中断的一次整体批处理称为成功。全部 s 的完整证书、整行哈希和运行记录另打包供复核。

下一步：检查 s=225–232；独立检查 R450 将局部二/三阶正性推出完整 PF₃ 的承重论证；继续寻找 s、k 同时无界时的 Turán 凝聚下界。遇到非正多项式系数时先计算真实合法整数上的 D₂、D₃，以区分当前证书失败与数学反例。

## 5. 权限与成果等级

GitHub 实际身份 `awdawmip`，仓库 `push=true`。原生研究 Site 当前仅有只读作用域；本轮 `em_session_start` 返回 `STATIC_READONLY_SCOPE_DENIED, operation_sent=false`，`em_control_tasks` 返回 `CONTROL_QUOTA`。正式 owner 尚未核实，未宣称 CLAIM、Result、Driver 审查、接纳。P000 与 ACTIVE 世界观未修改。
