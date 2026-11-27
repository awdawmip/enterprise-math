# X6 首步二次观察的非零顶点参数域

2026-11-27。知情补充推导与本地 BigInt 复算。沿用 Port 10、正权重 `(17t,B,22t,D)`、六对 BRC、1,935 个方向、严格 $3/2$ 近优全集和合法最优项。证明使用 $(t,B,D)$ 的辅助权重系数，复用冻结的 BRC 观测边界和线性后缀。范围不涉及原生空间坐标或时间动力学。

Researcher-ID `EM-DIRECT-8327F7` · Activity `RA-184AE178188022AA92EFE075`

> 闭象限结论已由完整配对复核确认。切线去重与末步耦合以[开斜率室补证](../2026-11-27_x6_monotone_chamber_correction/README.md)为准。

## 结论

写唯一二次首查询为 $Q=a t^2+bB^2+cD^2+d tB+e tD+fBD$。在继承必要支撑墙及五层纯线性后缀的精确容量上界下，任何正确的 6 深度树若只在根使用一个二次查询，且 $c=Q(p_{24})\ne0$，则把两分支交换为 $c>0$ 后，必有 $e<0$ 或 $f<0$。此范围完整包含 $e=0$、$f=0$ 和其它端点恰为零的情况。原先 $1\le K_6\le2$ 的总界仍待判定。可回读的原范围由 [R242 的可约根排除](https://github.com/awdawmip/enterprise-math/blob/92b9c31df5b741322107e6fa70319d20d320ddfb/research_notes/portable_direct/2026-11-26_r2_x6_r242_reducible_quadratic_root_closure.md)、[R258 的内部位置排除](https://github.com/awdawmip/enterprise-math/blob/b0960b0e767177f2b6bb7437275bf19aa662f7f0/research_notes/portable_direct/2026-11-27_r2_x6_r258_complete_internal_quadratic_closure.md)及 [R266 的 $c=0$ 一条多点铅笔排除](https://github.com/awdawmip/enterprise-math/blob/e0c470356c96463ed9b4349d91a1057d4974878b/research_notes/portable_direct/2026-11-27_r2_x6_r266_all_single_multipoint_zero_closure.md)确定。

对必要的芽分割，可将满秩根乘以负号并交换分支。满秩二次型在任何芽上都不会恒为零。根对恰落在零线上的完整输入如何约定分支，不影响这个必要条件。

## 非零顶点的有限降维

冻结的 51 个端点、98 个有向芽、47 个必要支撑标签与 2,225 个线性分割来自 [R247](https://github.com/awdawmip/enterprise-math/blob/7e54892a45579bdc497c27e061399339d1fb3512/research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md)。记 $G(S,5)$ 为该证明中芽集合 $S$ 的单调五层线性后缀容量检查。$G$ 对实际树存在性提供必要条件。以下每次排除在已知部分芽的分支上检查容量，仍保留未知芽。

令 $c>0$ 后可按正倍数归一 $c=1$。在经过 $p_{24}=(0,0,1)$ 的一条铅笔上，有限端点写为 $(rT,rU,D)$，其中 $(T,U)$ 是固定的原始整数方向，$r>0$，纵标 $y=D/r$。符号由 $K-\tau(y)$ 确定，其中
$$
K=aT^2+dTU+bU^2,\qquad \tau(y)=-y^2-(eT+fU)y.
$$
同一铅笔上任意两个不同纵标的阈值之差是 $-(y-y')(y+y'+eT+fU)$。故在斜率平面中，阈值的完整弱序只可在 $eT+fU=-(y+y')$ 的直线改变。每个排列开室、开边或顶点固定弱序。$h$ 个不同阈值对应 $2h+1$ 个截距符号词，阈值相等的端点同取零。每个符号词给一个下界和一个上界确定的开截距区间，或者给定一个截距单点。两端的有限极值都是确定的斜率仿射函数。

忽略跨铅笔的共同系数限制时，单条带 $n$ 个不同纵标的铅笔共有 $1+2n^2$ 个三值符号词。无零词由空的或连续的负号段确定，共 $1+n(n+1)/2$ 种。固定一个零点后，可在其一侧取相邻非空负号段，也可没有负号，共 $n$ 种。两个零点之间恰好为负号段，共 $n(n-1)/2$ 种。逐类均可选择相应实根或无实根。

对任意四条不同铅笔，四个截距行 $v_i=(T_i^2,T_iU_i,U_i^2)$ 的系数秩为三，且每个三行子集独立。其带符号余子式向量 $w$ 给出唯一线性关系 $\sum w_i v_i=0$。四条铅笔的符号词共同可行，当且仅当四个加权截距区间的 Minkowski 和包含零。只要有一个开区间，和便是开区间，有限上下界用严格比较。四个单点时用精确等式。少于四个不同方向时可独立选择截距。对任意固定斜率，Helly 定理在三维截距系数空间中给出全部四元关系的充分性。所有四元关系必须在**同一**斜率面上同时满足。这样，给定一个弱序面和各铅笔符号词，有限端点的共同可行性归为二维有理线性约束，可含严格、弱或等式条件。[R261 的共同零版本](https://github.com/awdawmip/enterprise-math/blob/b091d79f5b7b493918b181750b2494c3688799a2/research_notes/portable_direct/2026-11-27_r2_x6_r261_all_pencil_circuit_helly.md)

[排列计数](https://github.com/awdawmip/enterprise-math/blob/9eacaaa7040c51c3be61f204a9c5d8e464f95936/research_notes/portable_direct/2026-11-27_x6_c_nonzero_threshold_faces/reproduction.json)在冻结端点上得到 135 条不同直线、6,118 个交点、12,395 条开边及 6,278 个开室，共 24,791 个面。六个多点方向的直线数为 6、36、65、10、15、3，逐线约去正公因数并合并重复。交点按齐次有理坐标归一，重数分布是二重 6,095、三重 22、四重 1。若交点重数为 $m_p$，把线逐条加入可得开室数 $1+135+\sum_p(m_p-1)$，每条线的顶点分段给开边数 $135+\sum_p m_p$。本计算给出候选参数面的精确划分，尚未在所有面上运行容量测试。

## $c>0,\ e,f\ge0$ 的排除

**端点与容量。** 在此范围内每条铅笔的 $-\tau(y)$ 按已冻结的非负纵标严格递增。每条铅笔允许任一端点恰好取零，也允许所有端点均严格。把 $(e,f,c)$ 按正倍数归一到单纯形 $e+f+c=1$，保留 $c>0$。程序对每个符号词前缀精确计算上述截距关系。为处理严格约束，先用所有弱不等式裁剪闭多边形，再检查每条原严格关系在某一顶点取正。若每条都有正见证，取见证顶点的有限平均便同时满足全部严格关系。由此也覆盖退化面和边界点。所有非零端点的出芽固定其常数项符号。$p_{24}$ 的芽为正。对每个部分分割检查每侧最多 31 个支撑及 $G(S,5)$。17 个方向均处理完成，容量递归执行 21,231,689 次检查，留下 317 个部分分割。各候选有 1 至 5 个有限零点，没有全严格候选。[端点词、计数与候选](https://github.com/awdawmip/enterprise-math/blob/9eacaaa7040c51c3be61f204a9c5d8e464f95936/research_notes/portable_direct/2026-11-27_x6_c_nonzero_threshold_faces/reproduction.json)

**零点切线。** 把 $Q$ 写成 $x^\mathsf{T} A x$。若 $Q(p)=0$ 且 $Q$ 满秩，其非零切线协向量 $L_p=2p^\mathsf{T}A$ 满足 $L_p(p)=0$。因此所有从 $p$ 出发的芽的首阶符号是二维对偶空间的齐次线排列。程序在每条排列射线和两个相邻扇区取精确代表，计算首阶符号。若从 $p$ 指向 $q$ 的首阶为零，其二阶为 $Q(q-p)=Q(q)$。若此时 $Q(q)=0$，整个直线都使齐次二次型为零，导致可约，与满秩矛盾。允许不同零点各自选择切线签名，是保留所有实际二次型的放宽。再做标签和精确后缀测试。遍历 26,612 个部分选择、执行 10,548,962 次后缀检查，仅剩 12 个完整分割。其零点集只有 $\{6,18,19,29\}$ 与 $\{6,18,19,40\}$ 两种，各有 9 与 3 个残余分割。[切线放宽和完整残余](https://github.com/awdawmip/enterprise-math/blob/9eacaaa7040c51c3be61f204a9c5d8e464f95936/research_notes/portable_direct/2026-11-27_x6_c_nonzero_threshold_faces/reproduction.json)

**恢复同一二次型。** 每组四个零点的二次评价行独立，齐次核为二维。取一个正 $c$ 原点和一个 $c=0$ 的方向，则所有 $c>0$ 二次型按正比例都落入同一实仿射参数线。对每个芽的常数、一阶和二阶行以及 $(e,f)$ 约束，保留所有有理断点。在断点本身和相邻开区间求精确字典序符号。两组各有 180 和 175 个断点。满足 $e,f\ge0$ 的代表各为 4 和 2 个，都覆盖其全部可行区间与端点，各只给同一种完整芽分割。两种分割均与对应切线残余不相交。故即使末步不再限制二次型行列式，也无法实现任何剩余分割。这排除了闭象限内原题所需的满秩根。[共享系数的精确扫线](https://github.com/awdawmip/enterprise-math/blob/9eacaaa7040c51c3be61f204a9c5d8e464f95936/research_notes/portable_direct/2026-11-27_x6_c_nonzero_threshold_faces/reproduction.json)

只使用冻结端点和芽做上述辅助系数计算。未重新计算 BRC 方向分数，未作形式化、独立定理审定或正式 Task/Result 接纳。

## 本地复算

将 [R247 原文](https://github.com/awdawmip/enterprise-math/blob/7e54892a45579bdc497c27e061399339d1fb3512/research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md) 保存为 `R247.md`，程序按原文第一个 JavaScript 围栏调用冻结端点和后缀代码。从[固定复算包](https://github.com/awdawmip/enterprise-math/blob/9eacaaa7040c51c3be61f204a9c5d8e464f95936/research_notes/portable_direct/2026-11-27_x6_c_nonzero_threshold_faces/reproduction.json)提取同名文件，逐个比较 JSON 结果，掩码用十六进制精确保存。

```sh
node replay.cjs R247.md arrangement.js > /tmp/x6-arrangement.json
node replay.cjs R247.md quadrant.js > /tmp/x6-quadrant.json
node replay.cjs R247.md tangent.js /tmp/x6-quadrant.json > /tmp/x6-tangent.json
node replay.cjs R247.md coupled.js /tmp/x6-tangent.json > /tmp/x6-coupled.json
```

最直接的续题是把闭象限拓宽到含原点的完整开斜率面。归一 $c=1$ 时，该面恰由 $f>-11$、$e>-68/3$、$e+17f>-31$ 划定。逐一取六条多点铅笔各自最小的两纵标之和，本应另加 $e+4f>-257/2$、$e+9f>-143$、$2e+5f>-52$。前两条由单变量下界推出，最后一条用组合 $(29/17)e+(5/17)(e+17f)>-2437/51>-52$ 即得。在此面可复用相同符号词和切线完成法。边界有阈值并列，沿弱序求符号词。其余斜率面与 $c=0$ 的多零铅笔分支有各自的证据范围。
