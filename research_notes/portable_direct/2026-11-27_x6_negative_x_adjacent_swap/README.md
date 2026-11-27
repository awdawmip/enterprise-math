# X6 首步二次观察的第二个负 $x$ 换序室

2026-11-27。继续冻结 Port 10、六对联合 BRC、权重 $(17t,B,22t,D)$、1,935 个方向、严格 $3/2$ 近优集与合法最优项。假设六深树唯一的满秩二次观察位于根，记 $x=e+17f+31c$，统一定向 $c>0$。置 $r=-x$。本轮排除整室

$$
39c/2<r\le65c/2,\qquad 29e-5r+729c\ge0,\qquad e+r\le156c.
$$

下边 $r=39c/2$ 沿用已证结论，其余闭边和顶点由本轮检查。两室合并给出统一排除 $-65c/2\le x<0$、$-1133c/58\le e\le247c/2$。$K_6$ 仍在 $[1,2]$。[前一换序室](https://github.com/awdawmip/enterprise-math/blob/7e250ebc8a8dc5d53be7b89296982e338e26f97d/research_notes/portable_direct/2026-11-27_x6_negative_x_single_swap/README.md)

## 换序与可行性

在 $c=1$ 归一图上，以 $(r,e)$ 表示的四个闭包顶点按边依次为 $(39/2,-1263/58)$、$(65/2,-1133/58)$、$(65/2,247/2)$、$(39/2,273/2)$。$B=17t$ 的前三项阈值由前室的 $(p_{19},p_{26},p_{34})$ 变为 $(p_{19},p_{34},p_{26})$，其纵标依次为 $22,83/2,9$。其后的阈值和其它铅笔仍保序。各相邻阈值差在四顶点取非负值，内部严格。闭包仅允许以下四对并列。

| 端点编号 | 边 |
|---|---|
| $(18,2)$ | $e+r=156c$ |
| $(19,34)$ | $2r=65c$ |
| $(34,26)$ | $2r=39c$，本轮开边 |
| $(4,14)$ | $29e-5r+729c=0$ |

沿用已保存的有理多边形裁剪、四截距余子式相容与零点切线放宽。生成器只变更固定前一引擎中的四处内容，即域顶点、开边、前三项排序和并列对。17 条铅笔共 121 个带弱边界的词，含在开边随后被裁去的一项双零词。端点阶段 15,966,057 次分割检查，借用 R274 跳过 1,346 次第二个双零铅笔的前缀转换，留下 285 个部分掩码，其中 53 项恰有一个双零铅笔。R275 的全域严格前缀与单项式块压缩归其独立研究。[R247 冻结输入](https://github.com/awdawmip/enterprise-math/blob/7e54892a45579bdc497c27e061399339d1fb3512/research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md) · [R274](https://github.com/awdawmip/enterprise-math/blob/a62a9006a863589ba0c7dacb503719e4a9a5eb88/research_notes/portable_direct/2026-11-27_r2_x6_r274_all_double_pencil_four_anchor_closure.md) · [R275](https://github.com/awdawmip/enterprise-math/blob/001076e59298e45715cb58c87ab3395c53d005a8/research_notes/portable_direct/2026-11-27_r2_x6_r275_monic_block_compression_and_strict_prefix.md)

## 完整排除

端点部分掩码的 1、2、3、4、5、6、7 个零点计数依次为 5、47、115、96、21、0、1。零点切线放宽允许各零点独立取切线签名，因而包含每个真实满秩二次型。28,440 次切线部分选择中，9,711 次受 31 标签界排除，17,044 次受递归容量排除，共执行 13,564,746 次分割检查。没有任何完整芽分割通过。至此该室已由容量排除，已有 35 项无域矛盾证书仍可供后续室使用。独立 Fraction 程序重建了域顶点、全部铅笔的内部顺序和闭边并列，并核对各阶段词数和零点来源。

## 复算与续接

[生成器和固定输出](reproduction.json) 内含端点、切线和独立几何校验结果。将 R247 原文另存为 `R247.md`。从[前一室复算包](https://github.com/awdawmip/enterprise-math/blob/7e250ebc8a8dc5d53be7b89296982e338e26f97d/research_notes/portable_direct/2026-11-27_x6_negative_x_single_swap/reproduction.json)提取 `single_swap.js`、`check_geometry.py`。从[固定加载器包](https://github.com/awdawmip/enterprise-math/blob/9eacaaa7040c51c3be61f204a9c5d8e464f95936/research_notes/portable_direct/2026-11-27_x6_c_nonzero_threshold_faces/reproduction.json)取 `replay.cjs`，从[切线包](https://github.com/awdawmip/enterprise-math/blob/a81e850c387f2759776498bcb60245a587624e7f/research_notes/portable_direct/2026-11-27_x6_monotone_chamber_correction/reproduction.json)取 `tangent_provenance.js`，从[边界变形包](https://github.com/awdawmip/enterprise-math/blob/096aac42193eb50d60fcbc56e4cf1ec0595de828/research_notes/portable_direct/2026-11-27_x6_boundary_transport/reproduction.json)取 `replay.py`，另名 `transport_replay.py`。

```sh
python make_adjacent.py single_swap.js > adjacent_swap.js
node replay.cjs R247.md adjacent_swap.js > endpoints.json
node replay.cjs R247.md tangent_provenance.js endpoints.json > tangents.json
python check_adjacent.py R247.md transport_replay.py adjacent_swap.js endpoints.json tangents.json
```

纯 $B=17t$ 的下一相邻室由越过 $r=65c/2$ 时 $p_{19}$、$p_{34}$ 交换产生。靠近 $r=0$ 时，其它铅笔已变序的扇区及 $x\ge0,e<-100c$ 也仍开放。本轮处理冻结 BRC 的辅助权重系数，证据为作者证明与本地精确复算。
