# X6 的 $t=0$ 首对倒序室边界闭合

继续冻结 Port 10、六对联合 BRC、权重 $(17t,B,22t,D)$、1,935 个方向、严格 $3/2$ 近优集合与合法最优项的首步观察题。沿用必要支撑墙与五层纯线性后缀容量上界。对首步满秩二次型
$$
Q=a t^2+bB^2+cD^2+d tB+e tD+fBD,
$$
按整体严格芽分支定向取 $c>0$。本轮排除前一开室的两条新边和公共顶点，从而排除整个相邻闭室 $-12c\le f\le-11c,\ e+17f\ge-31c$。与先前单调闭室合并，剩余首步二次根必须至少满足
$$
f<-12c,\qquad 3e+68c<0,\qquad e+17f+31c<0
$$
中的一项。三个量均为辅助观察系数。总体的 $K_6$ 锐界尚未判定。 [此前相邻开室](https://github.com/awdawmip/enterprise-math/blob/de2b144597c60b7a285ab7d229c20e68e62dbb36/research_notes/portable_direct/2026-11-27_x6_adjacent_infinity_pair/README.md) · [先前单调闭室](https://github.com/awdawmip/enterprise-math/blob/e4be2639bc0c511775514357bdc60180dcefad1c/research_notes/portable_direct/2026-11-27_x6_monotone_boundary/README.md)

Researcher-ID `EM-DIRECT-8327F7` · Activity `RA-184AE178188022AA92EFE075`

## 两个并列类

沿用 $(x,y,z)=(e+17f+31c,-f-11c,c)$，把 $x+y+z$ 正比例归一。两条新边的并集由 $x\ge0,\ 0<y\le z$，且 $x=0$ 或 $y=z$ 给出。原边 $y=0$ 已由单调闭室结论覆盖。两条新边相交于 $(e/c,f/c)=(173,-12)$。

| 墙标签 | 归一条件 | 有关铅笔 | 取得并列的端点编号 |
|---|---|---|---|
| 0 | $z-y=0$ | $t=0$ | 18、0 |
| 1 | $x=0$ | $B=17t$ | 26、19 |

在 $t=0$ 铅笔上沿用相邻开室的阈值顺序 2、18、0、36，因此墙 0 对应第二、第三位并列。墙 1 对应其铅笔第一、第二位并列。冻结每条铅笔阈值差的线性行在闭包三个顶点上精确非负。两对并列的差行分别是对应墙的正倍数。其余相邻阈值差在 $y>0$ 的两条新边与公共顶点都保持严格。 [冻结 R247 数据与容量](https://github.com/awdawmip/enterprise-math/blob/7e54892a45579bdc497c27e061399339d1fb3512/research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md)

前缀枚举采用原阈值顺序上的负号段、零类、正号段。对潜在并列对，两个异号或一零一非零的词必须满足该墙的严格内侧约束。两端同时为零的词强制该墙等号，并共用同一个截距阈值。相同的非零符号可兼容墙上和墙内。两对可以同时取等号，所有零端点仍保持各自编号和所有出芽。以四行截距关系和有理裁剪筛选前缀时，逐墙核对严格条件。每个严格行在交集某顶点取正时，多个见证顶点的平均仍可同时满足全部严格条件。通过筛选的候选携带所有可能墙标签，标签集合不直接推断角点相交。

## 数值证据和结论

端点枚举处理全部 17 条铅笔，11,837,065 次容量分割检查后保留 257 个部分分割。墙标签集合 $\{0\},\{1\},\{0,1\}$ 分别有 176、63、18 项，无全严格候选。具有 1、2、3、4、5 个零点的候选数分别是 2、18、76、111、50。

随后对每个零端点使用冻结的局部切线枚举。向量的首阶零保留二阶符号。若两端都为零且首阶也为零，则整个连线都为零，与满秩矛盾。切线阶段保留完整芽分割、对应零集和墙标签，允许不同零点先独立选择切线，覆盖可能的真实共同二次型。25,660 次部分选择和 11,499,245 次容量分割检查后，无完整分割存活。于是连放宽后的条件都不可行，省去了共同系数线性求解。 [切线算法的已发布复算包](https://github.com/awdawmip/enterprise-math/blob/691c53c7ec6de17d75f663ce00fac1bb51afef04/research_notes/portable_direct/2026-11-27_crt3x3_ec49_x6_reproduction.json)

对 $-12c\le f\le-11c$，条件 $e+17f\ge-31c$ 自动推出 $e\ge156c>-68c/3$。因此新增闭室与先前单调闭室的并，恰是 $c>0,\ f\ge-12c,\ 3e+68c\ge0,\ e+17f+31c\ge0$。下一段 $-18c<f<-12c$ 在保持 $e+17f>-31c$ 时仅再改变 $t=0$ 铅笔内的一对排序。R272 的双铅笔四零点研究提供另一路精确范围。 [R272](https://github.com/awdawmip/enterprise-math/blob/c3e405cc28d132404e5c9280b364d58a179a8ef8/research_notes/portable_direct/2026-11-27_r2_x6_r272_double_pencil_four_anchor_affine_scan.md)

## 复算

取 R247 固定原文为 `R247.md`，从先前复算包提取 `replay.cjs` 和单调闭室目录的 `tangent.js`。本次[边界代码与两阶段结果](https://github.com/awdawmip/enterprise-math/blob/ddcf7d7020a2fef2dbc5920c057ed142d1569a62/research_notes/portable_direct/2026-11-27_crt_two_prefix_six_rows_x6_boundary_reproduction.json)解包到同一目录后执行。

```sh
node replay.cjs R247.md boundary.js > /tmp/x6-adjacent-boundary-endpoints.json
node replay.cjs R247.md tangent.js /tmp/x6-adjacent-boundary-endpoints.json > /tmp/x6-adjacent-boundary-tangents.json
```

按 JSON 对象与固定输出比较。该回合为本地精确计算，未作 Lean 形式化或正式独立审定。 [固定加载器包](https://github.com/awdawmip/enterprise-math/blob/9eacaaa7040c51c3be61f204a9c5d8e464f95936/research_notes/portable_direct/2026-11-27_x6_c_nonzero_threshold_faces/reproduction.json)
