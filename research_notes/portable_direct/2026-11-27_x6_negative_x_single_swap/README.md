# X6 首步二次观察在 (x<0) 的首个换序室

2026-11-27。冻结 Port 10、六对联合 BRC、权重 $(17t,B,22t,D)$、1,935 个方向、严格 $3/2$ 近优集与合法最优项。沿用必要支撑墙与五层纯线性后缀容量。设六深树唯一的二次观察位于根，满秩齐次型为 $Q=a t^2+bB^2+cD^2+d tB+e tD+fBD$，方向归一为 $c>0$，记 $x=e+17f+31c$。本轮排除完整参数域

$$
-39c/2\le x<0,\qquad e\ge-68c/3,\qquad e\le156c+x,\qquad 29e+5x+729c\ge0.
$$

这包含 $-43c/3\le x<0$、$-68c/3\le e\le425c/3$ 的统一宽度矩形。各闭边及顶点均保留。前稿给出了从 $x=0$ 推出的少量负芽必要条件。本轮在此域内把五层容量与共同二次型逐项联立，连同所有可能的边界变形阻碍一起排除。$K_6$ 仍在 $[1,2]$。[前稿](https://github.com/awdawmip/enterprise-math/blob/096aac42193eb50d60fcbc56e4cf1ec0595de828/research_notes/portable_direct/2026-11-27_x6_boundary_transport/README.md)

## 参数域与阈值顺序

令 $r=-x$。在 $c=1$ 图上，域的闭包在 $(r,e)$ 坐标的五个顶点依次为 $(0,-68/3)$、$(43/3,-68/3)$、$(39/2,-1263/58)$、$(39/2,273/2)$、$(0,156)$。只在 $r=0$ 开边。对有限端点 $(hT,hU,D)$，取纵标 $s=D/h$，共同截距 $J=aT^2+dTU+bU^2$。端点号由 $J-\tau(s)$ 决定，其中 $\tau(s)=-cs^2-(eT+fU)s$，$f=(-r-e-31c)/17$。每条铅笔的相邻阈值差关于 $(r,e,c)$ 仿射。逐顶点核对得到，只有 $B=17t$ 的首对纵标 $p_{26},p_{19}$ 相对 $x>0$ 反序。括号以下标表示编号，弱序上仅有五个相邻并列。

| 铅笔 | 依阈值降序的并列对 | 并列边 |
|---|---|---|
| $t=0$ | $(18,2)$ | $e+r=156c$ |
| $B=17t$ | $(19,26)$ | $r=0$ |
| $B=17t$ | $(26,34)$ | $2r=39c$ |
| $B=0$ | $(10,15)$ | $3e=-68c$ |
| $(T,U)=(2,5)$ | $(4,14)$ | $29e-5r+729c=0$ |

固定弱序的每个端点词由负前缀、连续零点和正后缀组成。无零及单零词逐一取阈值间隙或阈值。双零只可能取表中的同一相邻对。若相邻有并列可能而符号不同，就加入严格阈值差。双零词加入相等行。17 条铅笔共 122 词，包含随后因 $r>0$ 被裁去的 $r=0$ 双零词。第 51 端点 $p_{24}$ 的号为正。[冻结端点及容量源码 R247](https://github.com/awdawmip/enterprise-math/blob/7e54892a45579bdc497c27e061399339d1fb3512/research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md)

## 从端点词到共同二次型

在任一固定斜率下，每条铅笔的词给一个截距开区间，或一个截距单点。四条不同铅笔的截距存在唯一余子式关系，各三行独立。四截距的加权区间之和必须含零，开区间用严格界，四个单点用等式。全部四元条件在同一斜率上共同成立，再用 Helly 等价判定三维截距。此域每个截距的有限上、下端各占一条仿射行。对闭多边形做有理齐次裁剪，逐条严格行都须至少一个顶点严格满足。对这些顶点取有限平均，便同时严格满足全部严格行。搜索在每个词前缀应用固定容量检查及 R274 的双铅笔各双零排除。[四元截距条件](https://github.com/awdawmip/enterprise-math/blob/9eacaaa7040c51c3be61f204a9c5d8e464f95936/research_notes/portable_direct/2026-11-27_x6_c_nonzero_threshold_faces/README.md) · [R274](https://github.com/awdawmip/enterprise-math/blob/a62a9006a863589ba0c7dacb503719e4a9a5eb88/research_notes/portable_direct/2026-11-27_r2_x6_r274_all_double_pencil_four_anchor_closure.md)

端点阶段 16,827,540 次分割检查，略去 1,559 次有第二个双零铅笔的前缀转换，剩 298 个部分划分。其中 81 项恰有一个双零铅笔。1 至 6 个零端点的计数分别为 5、52、127、89、18、7。沿用 R247 同编号的零点切线放宽。切线阶段 46,246 次部分选择及 26,677,479 次分割检查，保留 10 个有序完整芽掩码与零点集配对。

其中 1 项逐位命中既有 26 项无域证书。另 9 项全部由正整数行组合否证，8 项用两条必要行，1 项用四条。设 $Q(z)=z^{\mathsf T}Az$。必要行来自严格端点评价，或从零点 $p$ 到 $v$ 的有向首阶量 $2p^{\mathsf T}Av$。若目标符号可由二阶项 $Q(v)$ 实现，首阶行用弱号，否则用严格号。用六个原系数直接有理行归约，将每个正组合对零点评价行取模。两项化为 $0$ 但含严格行，其余八项化为正数 $c$ 的负倍数。十项证书均与本轮斜率域无关，可凭相同有序掩码和完整零点集复用。新九项与旧 26 项给出 35 个不同配对。[旧证书与行消元代码](https://github.com/awdawmip/enterprise-math/blob/7277e45989ff76b3ecdba7b8d176ac5f4f37791b/research_notes/portable_direct/2026-11-27_x6_negative_e_second_strip/reproduction.json)

## 复算和剩余域

[源码与固定输出](reproduction.json) 保留整个端点与切线余项，包含新证书和独立六系数校验。Python 从固定端点独立重建五个顶点、122 个词的数目、五组并列和端点到切线的计数关系。取前引 R247 原文为 `R247.md`。从固定[加载器包](https://github.com/awdawmip/enterprise-math/blob/9eacaaa7040c51c3be61f204a9c5d8e464f95936/research_notes/portable_direct/2026-11-27_x6_c_nonzero_threshold_faces/reproduction.json)取 `replay.cjs`，从[切线包](https://github.com/awdawmip/enterprise-math/blob/a81e850c387f2759776498bcb60245a587624e7f/research_notes/portable_direct/2026-11-27_x6_monotone_chamber_correction/reproduction.json)取 `tangent_provenance.js`，从[前一带的包](https://github.com/awdawmip/enterprise-math/blob/6cdc7b061d6579d6993f2fbc30d396d9a5c29047/research_notes/portable_direct/2026-11-27_x6_negative_e_fourth_strip/reproduction.json)取 `match_veto.py`，从旧证书包取 `coupled.js` 及 `coupled.json`，将后者另名 `prior-veto.json`。独立核对脚本复用前稿中解析和校验固定 R247 原文的 `replay.py`，另存为 `transport_replay.py`。[固定解析器](https://github.com/awdawmip/enterprise-math/blob/096aac42193eb50d60fcbc56e4cf1ec0595de828/research_notes/portable_direct/2026-11-27_x6_boundary_transport/reproduction.json)

```sh
node replay.cjs R247.md single_swap.js > endpoints.json
node replay.cjs R247.md tangent_provenance.js endpoints.json > tangents.json
python match_veto.py prior-veto.json tangents.json > matched.json
node replay.cjs R247.md coupled.js matched.json > new_certificates.json
python check_geometry.py R247.md transport_replay.py single_swap.js endpoints.json tangents.json
python check_certificates.py R247.md transport_replay.py tangents.json prior-veto.json new_certificates.json
```

余下 $x<0$ 室会在表中相应边界外出现第二次换序或其它铅笔的第一次换序。最小的后续比较是 $r=39c/2$ 后仅 $p_{26},p_{34}$ 交换的相邻室，逐项核对 35 个可复用证书是否已覆盖其全部完整配对。$x\ge0,e<-100c$ 仍是另一未知域。本轮处理冻结辅助权重系数，给出作者推导和本地精确复算。
