# X6 负 $e$ 双变序带推进至 $-100c$

冻结 Port 10、六对联合 BRC、权重 $(17t,B,22t,D)$、1,935 个方向、严格 $3/2$ 近优集与合法最优项。假设六深树唯一的满秩二次查询位于根，写 $Q=a t^2+b B^2+cD^2+d tB+e tD+fBD$，把严格芽分支整体定向为 $c>0$。沿用必要支撑墙及五层纯线性后缀容量上界，并复用 R274 的双铅笔各两零排除。本轮排除全带
$$
-100c\le e<-66c,\qquad x=e+17f+31c\ge0,
$$
含两侧边及内部所有并列。合并既有闭域，剩余首步二次根必有 $e<-100c$ 或 $x<0$。总体 $K_6$ 仍待定。 [此前 $-66c$ 界](https://github.com/awdawmip/enterprise-math/blob/7277e45989ff76b3ecdba7b8d176ac5f4f37791b/research_notes/portable_direct/2026-11-27_x6_negative_e_third_strip/README.md) · [R274](https://github.com/awdawmip/enterprise-math/blob/a62a9006a863589ba0c7dacb503719e4a9a5eb88/research_notes/portable_direct/2026-11-27_r2_x6_r274_all_double_pencil_four_anchor_closure.md)

## 精确区域与相容性

置 $(x,y,z)=(e+17f+31c,-e-66c,c)$。带内 $x\ge0,\ 0<y\le34z$，逆变换 $e=-y-66z,\ f=(x+y+35z)/17$。闭包归一 $x+y+z=1$ 后的三个齐次顶点是 $(1,0,0),(0,34,1),(0,0,1)$。阈值 $\tau(s)=-cs^2-(eT+fU)s$ 对这三个参数线性。逐条核对固定铅笔的相邻阈值差，除 $B=17t$ 首对在 $x=0$ 并列外，其余差在整个带内严格。两个变序铅笔如下。 [冻结输入 R247](https://github.com/awdawmip/enterprise-math/blob/7e54892a45579bdc497c27e061399339d1fb3512/research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md)

| 铅笔 | 归一斜率范围 | 并列值数 | 符号词数 |
|---|---|---:|---:|
| $B=0$ | $e/c\in[-100,-66)$ | 10 | 62 |
| $(T,U)=(2,5)$ | $(2e+5f)/c\in[-3055/17,\infty)$ | 14 | 69 |

对 $(2,5)$，归一斜率是 $(5x-29y-2069z)/(17z)$。两个斜率扫描均取每一个允许的并列值和开区间代表，并保留阈值截点及其间隙的所有三值词。各铅笔仅最低四个纵标可能离开固定顺序链。固定链最小邻接和分别为 $201/2>100$、$185>3055/17$。每个有限上、下端由相关移动阈值以及固定链的极端一行确定，所以每条四元方向至多展开 $5\times5=25$ 个仿射和。共同斜率图上联合检查全部行，保留严格不等式和相等阈值。全部 131 个词和 6,040 次极值对照由独立 Python Fraction 复核。独立计算还确认公共顶点 $(e/c,f/c)=(-100,69/17)$ 恰有两组并列端点 $(11,38)$、$(19,26)$。 [四元截距关系](https://github.com/awdawmip/enterprise-math/blob/863b3c6c096af904e745a9701e3771ee4cb1e2e3/research_notes/portable_direct/2026-11-27_x6_infinity_low_wedge/README.md)

## 通用的极值行压缩

对没有标零的符号词，任何负符号阈值集合的最小值都由最小和最大纵标中的一项取得。这是因为 $\tau(s)$ 对纵标 $s$ 为凹二次式。正符号阈值集合的最大值则可用相邻纵标筛选。将该集合纵标写为 $s_1<\cdots<s_k$，归一斜率设为 $\lambda=(eT+fU)/c$。由
$$
\tau(s_i)-\tau(s_j)=c(s_j-s_i)(s_i+s_j+\lambda)
$$
可知，$s_i$ 达到最大值的条件恰是 $\lambda$ 在 $[-(s_i+s_{i+1}),-(s_{i-1}+s_i)]$ 中。首、末缺失的端取相应无穷。因为其它更远纵标给出的同向条件更宽，只需相邻正符号纵标。将这个闭窗口与实际归一斜率范围相交，即可移除在该范围内始终达不到最大的行。带有零点的词则固定为零阈值单点并验证严格项。

这一压缩适用于任意变序数。本轮额外以 6,040 个 Fraction 精确比较验证压缩后的极值。对实际 62 与 69 词库，两个铅笔的下端列表分别至多 3 与 5 行，上端均至多 2 行，故后续同域实现可把每一四元方向降至至多 15 行。本回搜索使用固定链压缩的 25 行上界。

## 完整排除及原证书复用

先前作者的 R272–R274 已处理 6,237 个双铅笔各两有限零点的锚组，覆盖附带更多零点的情况。对此处任一二次型，沿每条铅笔最多有两个有限零点。搜索遇到第二个有双零的铅笔即应用该作者证明。实际略去 48,208 项前缀转换，数量是枚举中的前缀次数。

端点阶段执行 44,316,398 次容量分割检查，保留 234 个部分分割，无全严格候选。233 个可在带的两边内侧实现，1 个只在 $e=-100c$ 边实现。203 项没有双零铅笔，31 项恰有一个。1、2、3、4、5 个有限零点的候选数依次是 3、27、86、89、29。独立 Python 从 R247 重新读取固定端点组与芽位，核对全部阶段计数、零点来源和 R274 锚组总数。

切线阶段 13,404 次部分选择和 6,845,480 次容量分割检查后留下 26 个完整芽分割与零点集配对。按同一 R247 编号，将每项有序正负掩码当整数比较，零点集合逐项比较，全部匹配此前的 26 项无域矛盾证书。无新签名。由于原证书在任意 $c>0$ 下都无需 $e,f$ 的域约束，直接复用即可排除本域全部剩余项。 [既有切线实现](https://github.com/awdawmip/enterprise-math/blob/a81e850c387f2759776498bcb60245a587624e7f/research_notes/portable_direct/2026-11-27_x6_monotone_chamber_correction/reproduction.json) · [原证书包](https://github.com/awdawmip/enterprise-math/blob/7277e45989ff76b3ecdba7b8d176ac5f4f37791b/research_notes/portable_direct/2026-11-27_x6_negative_e_second_strip/reproduction.json)

更负的 $e/c$ 情形出现新变序，但仍可用通用极值行窗口来计算精确行。处于 $x\ge0$ 时，$B=4t$ 首次可能出现新并列在 $e/c=-4121/26$ 的边界。另一半平面 $x<0$ 与总代价 $K_6$ 仍开放。这里只处理冻结 BRC 观测权重系数。未做 Lean 形式化或正式独立审定。

## 复算

取 [本轮源码与精确结果](reproduction.json)，使用固定 R247 原文 `R247.md` 与此前的 `replay.cjs`、`tangent_provenance.js`。从原证书包提取 `coupled.json`，另存为 `prior-veto.json`。

```sh
python check_local_words.py replay.cjs R247.md strip.js
node replay.cjs R247.md strip.js > /tmp/x6-negative-e-fourth-endpoints.json
python check_census.py replay.cjs R247.md strip.js /tmp/x6-negative-e-fourth-endpoints.json
node replay.cjs R247.md tangent_provenance.js /tmp/x6-negative-e-fourth-endpoints.json > /tmp/x6-negative-e-fourth-tangents.json
python match_veto.py prior-veto.json /tmp/x6-negative-e-fourth-tangents.json
```

逐对象核对 5 份固定 JSON。 [固定加载器包](https://github.com/awdawmip/enterprise-math/blob/9eacaaa7040c51c3be61f204a9c5d8e464f95936/research_notes/portable_direct/2026-11-27_x6_c_nonzero_threshold_faces/reproduction.json)
