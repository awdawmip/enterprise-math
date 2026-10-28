# PREFIX-333｜两条完整相位弧的精确最小包围球与四接触点 BRC 证书

日期：2026-10-29。类别：作者侧精确解析证明和实际运行的 SymPy 复算，`UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`。本对话本地研究身份 `EM-R006-333A`，GitHub 认证用户 `awdawmip`。本研究不等于 native CLAIM、Source Result、独立 Driver 复审或原生 X6/Detector/时间演化的保真映射。

## 固定输入与来源

研究使用 Enterprise Math 科学输入 `main@bedbfe8c57227caaf083032e748eb0d439e457bd`；账户级 `GLOBAL_KNOWLEDGE_V1 main@35b80a3eb28b1951ff3e60cec86d0d985d444ce9`。已读 AGENTS.md、p000_reality_foundation.json、ACTIVE Heartbeat World/残差与联合观察约束，以及 docs/PORTABLE_RESEARCH_PROTOCOL.md、docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md。复用 S7-3 BRC 五 Port 的来源保真构造，方法标注 `REUSE_APPLIED`。保留每个 Port 的九个有序来源路径对；本辅助 C³ 是外部复幅值模型，不声称已构成原生 X6 三维切片或原生动力学。

采用 `U=A/8`，矩阵 A 五行依次为 `(4,4,0)`、`(0,-4,4)`、`(-5+3i,0,-3+i)`、`(-2-2i,4+4i,2+2i)`、`(-2,0,5+2i)`。Port j 中 `v[j,k]=U[j,k]a[k]`，`Q_j(a)=sum_(k,l) v[j,k] conj(v[j,l])=|(Ua)_j|²`。固定

`q=(1/2,1/4,5/32,13/8,29/64)`，

报告在第四 Port 为 `(r,0)`，`r=sqrt(13/8)`，其余四个 Port 都为 `(0,0)`，每个实、虚坐标误差不超过 1。令 S 为 C³ 内符合全部五个准确 q 和十项报告的完整来源集合；与 PREFIX-332 完全相同。

## 定理1：两个高斯有理来源的全部允许相位弧，MEB²=2

取 `a=(0,1+i,1)` 与 `b=(0,1-i,1)`。保留有序来源路径对的 BRC 质量核算得到两者 `Q=q`，第四 Port 输出 `p_a=(1+5i)/4`、`p_b=(5+i)/4`。两者模长为 `r`，各自源范数平方为 3。定义 `n_a=a conj(p_a)/r`、`n_b=b conj(p_b)/r`，从而 `(Un_a)_4=(Un_b)_4=r`。

对 `|u|=1`，第四 Port 是 `ru`。其两项报告 `|r Re u-r|<=1`、`|r Im u|<=1` 当且仅当 `Re u>=sqrt(5/13)`。因为虚部界与单位模长给出 `|Re u|>=sqrt(5/13)`，实部报告给出 `Re u>=1-1/r>0`；反向用 `r-sqrt(5/8)<1`。其它四个 Port 的准确质量均小于1，它们的实虚分量对零报告自动合格。故两条轨道在 S 内的完整允许弧恰为

`T_a={u n_a: |u|=1, Re u>=sqrt(5/13)}`，
`T_b={u n_b: |u|=1, Re u>=sqrt(5/13)}`。

取 `c=(0, sqrt(10)(1-i)/5, sqrt(10)(1-i)/10)`。复欧氏内积的精确恒等式为

`||c||²=1`，`<c,n_a>=<c,n_b>=sqrt(13/5)`（实数）。

对每个弧上的任意点 x=u n_a 或 u n_b，

`||x-c||²=3+1-2 sqrt(13/5) Re u <=4-2 sqrt(13/5)*sqrt(5/13)=2`。

这是对**所有连续可行相位**的单一显式包围球，不依赖有限抽样。

## 定理2：四接触点严格正 KKT 证书，唯一球心

令 `s=sqrt(10)`，以下顺序放置四个弧端点：

`x_(a,±)=((s±4i)(1-5i)/26) a`；
`x_(b,±)=((s±4i)(5-i)/26) b`。

它们在第四 Port 的复读数为 `sqrt(5/8)±i`，满足全部十项报告且 `||x_i||²=3`、`||x_i-c||²=2`。按顺序 `a-,a+,b-,b+` 赋权

`lambda=(1/4+s/80,1/4-s/80,1/4-s/80,1/4+s/80)`。

四权严格正，和为1；直接高斯有理加 `sqrt(10)` 运算给出精确重心等式 `sum_i lambda_i x_i=c`。因此对**任意**球心 `z∈C³`，

`sum_i lambda_i||x_i-z||²=sum_i lambda_i||x_i-c||²+||z-c||²=2+||z-c||²`，

故 `max_i||x_i-z||²>=2+||z-c||²>=2`，等号只在 z=c 才可能成立。结合定理1上界：

**`MEB²(T_a union T_b)=2`，且最优中心唯一，为 c。**

该证书同时给出四个严格正接触权、全中心下界及完整连续相位上界。

## 完整 S 的科学增量与边界

`T_a union T_b ⊆ S`，因此由两项定理及 PREFIX-332 已证上界得到

**`2 <= MEB²(S) <= 475/124-sqrt(5/2) < L=1062562/458329`。**

相比 PREFIX-332 的完整 S 下界 `24/13`，新的平方半径下界严格提高 `2/13`；`L-2=145904/458329>0`。本轮确切求解的是两条高斯有理轨道的完整相位弧，而不是包含另两条代数来源轨道的整个 S；完整 S 的精确 MEB 仍属于 PREFIX-334 证明任务。

## 实际运算与文献对应

已执行 `python verify_prefix333.py > RESULTS_PREFIX333.json`，返回 PASS。程序使用 SymPy 精确根式及带来源标签的逐 Port 九项有序路径对，对两个种子来源与四端点共核验 270 个有序路径对、相位归一内积、四接触点、正权重、重心、半径及基准比较。连续相位与所有候选球心结论由前述符号恒等式推导。代码和机器结果存于本目录。

2026-08-15 Zhiqiang Xu, *The Minimal Measurement Number for Almost-Everywhere Complex Phase Retrieval*, arXiv:2608.15003 (https://arxiv.org/abs/2608.15003) 证明复维数 d 中 <=2d−1 个强度观测无法几乎处处唯一恢复；本轮在 d=3、m=5 的**特定**辅助 BRC 矩阵上额外给出报告相容性及显式最小球的精确证书，不借一般性不唯一结论推得本轮球半径。

本轮原生 Sites 只读身份结果 `research_authority_granted=false`，任务 owner/CLAIM 控制读取返回 `CONTROL_QUOTA`。GitHub 写入是保全作者侧研究材料，不是正式研究活动注册或 Source Result；原生状态待有效控制路径后续核实。
