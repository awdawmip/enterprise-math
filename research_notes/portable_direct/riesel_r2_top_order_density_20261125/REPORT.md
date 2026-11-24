# R₂：阶1260的真实增益，以及整根密度的严格区间

固定历史 R₂、P 与原研究者 EM-DIRECT-970E1C / RA-D2EC212845B63844081F9A14 的相关定义。令 T 为存在一个含阶1260的包含极小九预算字典，L 为存在全阶≤840的至多九字典。真正由最高阶带来的新根是 GAIN=T∖L；这些根都是精确成本九。

## 1. 数值结论（R₂ 内的相对自然密度）

| 根事件 | 严格包围（端点向外舍入） |
|---|---|
| T：有阶1260的不可删字典 | [1.7388837467, 1.7388864159]×10⁻⁹ |
| GAIN：预算九确实非用阶1260不可 | [1.6015219825, 1.6772046413]×10⁻⁹ |
| GAIN 在 T 内的比率 | [92.10%, 96.46%] |

T 的包围宽度小于 2.670×10⁻¹⁵；GAIN 的剩余不确定性主要来自是否存在另一种低阶字典，不是大整数分解误差。完整有理数上下界、单项交并权重与载体核验证据见 [certificate.json](certificate.json)。本轮不把这个增量当成完整 R₂ 精确成本九密度；完整值仍需低阶事件 L 的密度，再与完整 E₈ 判据相减。

## 2. 先把几何替代与其他低阶替代分开

[阶1260几何分类](https://github.com/awdawmip/enterprise-math/blob/0fc72cdda05ca8d3d2d3da048b65476d4d16da6f/research_notes/portable_direct/riesel_r2_top_order_20261125/REPORT.md)要求 W={19,73}、两条长列 w=0,3 mod5 和短列三格 w=21,26,31 mod35，其中 v=2+3w。两条长列用 6 个候选素数；三个短格可由 26 个低阶候选和全部阶1260候选担任。最高阶中三枚已有确定性素性证明；剩余载体的每个素因子阶恰为1260，故必须是 1 mod1260。新一轮按这个同余遍历 **7,936,507** 个候选数，排除所有不超过 10¹⁰ 的因子；69 位余项至多再含 6 个不同素因子，底数3给出合数证据。其余用在 T 几何里的低阶组已全列出并按阶载体验尽。

对每个素数 q，任一所需相位恰有两个根余数；不同素数独立来自 CRT。记录短列三格上低阶占用掩码 ℓ 和高阶占用掩码 h。两长列满足时，T 要求 ℓ∨h=111 且 h≠000。令 D 为有 T 的字典但相同几何不能全用低阶替代，则 D 要求 ℓ∨h=111 且 ℓ≠111。两个事件对高阶占用均单调。删掉未分解因子给下界；把每个真实未知因子以一个每格成功率 2/(10¹⁰+1) 的独立虚拟坐标支配，再补到六个给上界。这是概率空间的单调耦合，不是宣称六个虚拟分母为素数。占用掩码与独立容斥公式给出完全相同的 T、D 有理端点。

由于任何可按同一几何完成的低阶字典都计入 L，GAIN⊂D。这给出真增益的上界。D 本身并不排除其他几何，本报告对这部分另证下界。

## 3. 单个偶数提升即可给真增益下界

三格分别挑一个偶数 w 提升，取 v=(170,80,200)。对这些点，w 奇数固定通道38737不命中；W 的两个固定相位也不命中。为了确保没有一份低阶字典能完成，只要在某一个这样的点上，**所有低阶候选尾素数都不命中**。由[完整低阶判据](https://github.com/awdawmip/enterprise-math/blob/2b80afd7bbb034d1b3ef4fffb4491824d2bee6fb/research_notes/portable_direct/riesel_r2_ninth_predicate_20261125/REPORT.md)的全素数上界，逐点排除整个有限低阶库存就足够，无需假设某个字典被选用。

令 Bⱼ 为三个已证高阶坐标已足以和低阶短格、长列一起满足 T，且选定偶数提升 vⱼ 不被任何低阶候选命中。于是每个 Bⱼ⊂GAIN。对三个事件做七项容斥：

- 长列 f=15 的六枚都避开同一个短列相位，仍须占满两长列。
- 在组内短列低阶占用掩码中，排除交集所选短格；三个已证高阶坐标无需额外限制。
- 对其他低阶坐标 q，若一个交集要避开的不同相位有 k 个，则保留 q−2k 个根余数。已知素因子的权重精确相乘。
- 未解析低阶子载体只涉及 f=27、45；试除到100000后，若余项有至多 m 枚不同素因子，每个大于100000，则其不命中任何 k 个特定相位的概率至少 1−2km/100001。以此夹住每个交项，奇数项用下界、偶数项用上界，得到整个并集的严谨下界。未解析最高阶坐标无需限制，因为三个已证最高阶坐标已提供 T，任何额外最高阶命中均不会帮低阶 L。

这一步比要求所有其他低阶坐标完全不命中更强：只禁止它们在给定证据点相撞，其他时刻可以任意命中。后续可以给每个短格更多偶数见证点，或直接拟合低阶覆盖模板和 T 的交集，以进一步逼紧真增益。

## 4. 复算

`node density.js` 重建完整有理证书。整数载体由同一个阶过滤公式生成。既有素性数据来自完整 [R₂ 八预算](https://github.com/awdawmip/enterprise-math/blob/89b9571189e2c8b576f4972f3775961f7cf01836/research_notes/portable_direct/riesel_r2_eight_exact_20261125/REPORT.md)、[v15 R₃ 库存及其 Lucas 证据](https://github.com/awdawmip/enterprise-math/blob/745a30dae754df0e2d57d044e067680f33c70251/research_notes/portable_direct/riesel_nine_complete_20261124/README.md)、[高阶 Lucas 复算](https://github.com/awdawmip/enterprise-math/blob/a8de4bf6c49229562dd97452c3d2c29e627cbbbf/research_notes/portable_direct/riesel_sharp_wide_20261124/verify_order_primes.py)及[阶540补充分解](https://github.com/awdawmip/enterprise-math/blob/5b3ba41ee592c74fefe0f7704585caefa0440aa2/research_notes/portable_direct/riesel_r2_ninth_predicate_20261125/factor_checkpoint.json)。新算术为 BigInt 和精确分数，本轮未申报 Native Result 或独立 Review。
