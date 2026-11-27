# X6 的 $t=0$ 第二段斜率带排除

冻结 Port 10、六对联合 BRC、权重 $(17t,B,22t,D)$、1,935 个方向、严格 $3/2$ 近优方向集及合法最优项。沿用必要支撑墙和五层纯线性后缀容量上界。假设六深树只在根使用一个满秩二次查询 $Q=a t^2+b B^2+cD^2+d tB+e tD+fBD$，并整体交换严格芽分支以定向 $c>0$。本轮排除整个
$$
-18c\le f<-12c,\qquad e+17f\ge-31c
$$
斜率带。与此前闭室合并，剩余根必须满足 $f<-18c$、$3e+68c<0$、$e+17f+31c<0$ 中至少一项。总体 $K_6$ 锐界仍待判定。辅助连续参数用于权重系数。 [此前 $-12c$ 边界结果](https://github.com/awdawmip/enterprise-math/blob/6cc7a12082a8bd1120b28bdbf3d5c3da08852565/research_notes/portable_direct/2026-11-27_x6_adjacent_infinity_boundary/README.md)

## 阈值的严格次序与并列

取 $(x,y,z)=(e+17f+31c,-f-12c,c)$。新域为 $x\ge0,\ 0<y\le6z$。正比例归一到 $x+y+z=1$，闭包三个齐次顶点为 $(1,0,0),(0,6,1),(0,0,1)$。冻结的 $t=0$ 铅笔纵标是 $0,11,12,18$，端点编号为 18、2、0、36。阈值依次为 $0,11(z+y),12y,18(y-6z)$。在 $0<y\le6z$ 时，递减阈值顺序为端点 2、0、18、36，只有最后两位在 $y=6z$ 并列。其余铅笔保留原阈值次序，$B=17t$ 的首两位 26、19 在 $x=0$ 时并列。执行前对每个相邻阈值差在闭包三个顶点验非负，并对两处指定并列外的行在 $(0,6,1)$ 验严格正。因为域内 $y>0$，每个点在该顶点的凸组合权非零，因而没有额外并列。两条新边相交于 $(e/c,f/c)=(275,-18)$。 [冻结端点和容量输入 R247](https://github.com/awdawmip/enterprise-math/blob/7e54892a45579bdc497c27e061399339d1fb3512/research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md)

每条铅笔按阈值顺序枚举负号段、零类和正号段。潜在并列对取不同符号时强制对应墙严格在内侧，同时为零时强制墙等号并使用共同截距阈值。两个零端点及全部出芽均保留。继承四行截距关系和有理裁剪，在每个前缀将斜率带内部及两条墙分别核验。在闭裁多边形上，每条严格行都有一个正见证顶点，等价于存在同时满足各严格条件的点，见证平均即可。墙约束下使用该墙上的顶点。同一个前缀可以保留多个可实现标签。

## 精确容量结果

端点阶段处理全部 17 条铅笔，执行 11,703,458 次容量分割检查，保留 152 个部分分割，无全严格候选。可在开室实现的有 93 项，其中 7 项同时保留 $x=0$ 标签。其余 59 项只在边界可行，全部保留 $y=6z$ 标签，其中 5 项还保留 $x=0$ 标签。两个标签表示各自可行，角点按精确裁剪覆盖。具有 2、3、4、5 个零点的候选数分别是 10、45、66、31。

切线阶段逐零端点独立枚举协向量的首阶符号，首阶零时计算目的端点给出的二阶符号。两端均零且首阶也零会使整条直线为零，与满秩矛盾。完整芽分割、零点集和墙标签均保留。12,962 次部分选择和 6,050,988 次容量分割检查后，无任何完整分割存活。独立切线选择的放宽已有矛盾，因而无需进一步耦合同一个二次型。 [切线阶段的已发布复算包](https://github.com/awdawmip/enterprise-math/blob/691c53c7ec6de17d75f663ce00fac1bb51afef04/research_notes/portable_direct/2026-11-27_crt3x3_ec49_x6_reproduction.json)

对 $f\le-12c$ 而 $e+17f\ge-31c$ 的部分，$e\ge173c$，已含 $3e+68c\ge0$。所以此前闭域与此新斜率带恰并为 $c>0,\ f\ge-18c,\ 3e+68c\ge0,\ e+17f+31c\ge0$ 的闭侧域。更负的 $f/c$ 可以在四个剩余 $t=0$ 阈值次序区间分别处理；$B=17t$ 仅在相同外侧壁等号处并列。R272 保留另一路四零点证据。 [R272](https://github.com/awdawmip/enterprise-math/blob/c3e405cc28d132404e5c9280b364d58a179a8ef8/research_notes/portable_direct/2026-11-27_r2_x6_r272_double_pencil_four_anchor_affine_scan.md)

## 本地复算

从 [代码与固定结果](reproduction.json) 提取本轮代码，并使用 R247 原文 `R247.md`、此前固定的 `replay.cjs`、已发布单调闭室目录的 `tangent.js`。

```sh
node replay.cjs R247.md strip.js > /tmp/x6-second-strip-endpoints.json
node replay.cjs R247.md tangent.js /tmp/x6-second-strip-endpoints.json > /tmp/x6-second-strip-tangents.json
```

按 JSON 对象对比两份固定结果。该回合完成 BigInt 证据，未作 Lean 形式化或正式独立审定。 [固定加载器包](https://github.com/awdawmip/enterprise-math/blob/9eacaaa7040c51c3be61f204a9c5d8e464f95936/research_notes/portable_direct/2026-11-27_x6_c_nonzero_threshold_faces/reproduction.json)
