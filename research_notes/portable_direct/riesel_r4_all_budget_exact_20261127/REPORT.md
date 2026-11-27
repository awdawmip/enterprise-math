# 固定 Riesel R₄：所有预算的锐利观察阶

2026-11-27 · 知情作者证明与精确复算 · 待项目独立评审

**定理。** 固定[原 74 素坐标族 \(R_4\)](https://github.com/awdawmip/enterprise-math/blob/9b3680ea1c07b1364af5464a3469313ee616d408/research_notes/portable_direct/riesel_nine_frontier_20261124/r4/proof.md)和原二十素数辞典 \(P\)。对 \(F_n(a)=a^22^n-1\)、\(n\ge1\)，令 \(\delta_P(a)\) 为覆盖全部指数所需的最少额外严格真素因子数。对每个整数预算 \(b\ge11\)，判定 \(\delta_P(a)\le b\) 的根余数和未来项余数观察，两者的最大必要素坐标乘法阶均为
\[
\Omega_b(R_4)=\widehat\Omega_b(R_4)=T_b=5040\cdot2^{b-11}.
\]
原作者 EM-DIRECT-970E1C 的构型和任意预算 CRT 下界保留原归属。原固定库存的素性以及 Bang–Zsigmondy 定理沿用原范围。 [原下界](https://github.com/awdawmip/enterprise-math/blob/2ae5de00bf7e8f1e2571ef5666e95f82a25dc429/research_notes/portable_direct/riesel_r4_twelve_observer_lower_20261125/REPORT.md)

已有上界覆盖预算 11 至 21，且从预算 20 起统一处理有同时含 5、13 的预算内补全的根。本轮解决所有更高预算中漏掉至少一枚的情形。它把旧的「删位后仍须为大相对周期」条件放宽为「删位后进入已经允许的普通库存」，从而只需新增预算 22 至 25 的有限核验。 [预算 21 与保留两枚的统一上界](https://github.com/awdawmip/enterprise-math/blob/863b3c6c096af904e745a9701e3771ee4cb1e2e3/research_notes/portable_direct/riesel_r4_twenty_one_20261127/REPORT.md) · [预算 11 至 18](https://github.com/awdawmip/enterprise-math/blob/f869b78cc5143b7f73e7d59880917fe9ee024b5e/research_notes/portable_direct/riesel_r4_eighteen_sharp_20261125/REPORT.md) · [预算 19](https://github.com/awdawmip/enterprise-math/blob/4113a2b7cfad6bb28b44df62c14a43a22ab69d78/research_notes/portable_direct/riesel_r4_nineteen_sharp_20261125/REPORT.md) · [旧漏项有限归约](https://github.com/awdawmip/enterprise-math/blob/0803f17a9ce72d75c0987b69896e10c6659191d8/research_notes/portable_direct/riesel_r4_twenty_one_20261127/OMISSION_DESCENT.md)

## 漏项模型

两枚都省略时取步长 \(s=2\)。保留一枚时取 \(s=4\)，在另一偶支上依奇偶标签分别核验。原孔集依模 105 的 \(u=n/2\) 给出，任选原可用固定额外类的子集 \(C\)，令 \(L\) 为 105 与这些类在步进变量中的有效周期的最小公倍数。孔集 \(D\bmod L\) 固定。自由类的有效周期记为 \(h\)，相对周期为 \(m=h/\gcd(h,L)\)。任何原阶 \(d>T_b\) 的目标都满足 \(sh>T_b\)。

复算所用的放宽模型保留原低库存的两项限制。第一项是有限有效阶的计数。\(s=2\) 的有限阶为 \(11,13,33,17,25,39\)，\(s=4\) 为 \(11,13,20,33,22,17\)。第二项是相对期至 30 的其余有效阶必须通过原库存脚本的 \(\mathrm{hasFree}(h,s)\) 测试。该测试在 \(h\le150\) 时只要求至少一个可用原阶坐标的必要条件，\(h>150\) 时保守放行。通过这一测试的普通类，以及相对期超过 30 的类，都可取任意相位和数量。放宽模型包含实际补全。 [固定库存和步进几何](https://github.com/awdawmip/enterprise-math/blob/660f791ed86d245524e32610ee73bbb65db38085/research_notes/portable_direct/riesel_r4_nineteen_sharp_20261125/reproduction.json)

## 按低库存删除数位

取一个包含极小余覆盖及超界目标的私有点。其模 \(L\) 纤维里，目标类的相对期 \(m\) 的每个 \(p\) 进数位都需要 \(p-1\) 个互异竞争类。令 \(\gamma=1+|C|+\mathbf1_{s=4}\)，因此 \(W(m)=\sum_{p^e\parallel m}e(p-1)\le b-\gamma\)。由 \(sL\le15120\) 和 \(sh>T_b\) 得 \(2^{W(m)}/m<3072\)。对 \(p\ge17\)，单个素因子已贡献 \(2^{p-1}/p>3072\)，故只需 \(p=2,3,5,7,11,13\)。

对固定分支，列出所有相对期至 30 且属于有限计数库存或未通过 \(\mathrm{hasFree}\) 的有效期，称为受限有效期。设
\[
k_p=2+\max\{v_p(h'/\gcd(h',L)):\ h'\text{ 为受限有效期}\},
\]
空集取最大值 \(-1\)。若目标的 \(e=v_p(m)\ge k_p\)，就把联合 CRT 模数中 \(p\) 坐标的第 \(v_p(L)+e\) 位固定成私有点的该位，再删去该位。固定类只依赖模 \(L\)，故孔集保持。指数低于所删位的类保持。受影响的类若存活，周期除以 \(p\)，新相对周期的 \(p\) 指数至少为 \(e-1\)，严格大于所有受限有效期在该坐标的指数。因此变后的类进入普通库存。有限计数槽的使用量只会减少。

改变私有点在该位的 \(p-1\) 个替代值，得到同一模 \(L\) 纤维中的 \(p-1\) 个探针。每个都必须由竞争类覆盖，且该竞争类在所删位上要求这个替代值。这些类互异，全部消失。删位保持目标私有点，目标有效期减为 \(h/p\)。取新预算 \(b-(p-1)\)，目标仍超界，因为 \(2^{p-1}\ge p\)。所删位也可位于某些竞争类有效周期的内部，坐标限制后按原次序拼接上下数位，仍是一个同余类。

对每个 \(C\) 枚举低库存得到 \(k_p\)。再枚举 \(0\le v_p(m)<k_p\)，用 \(sh\le sLm\) 和 \(W(m)+\gamma\le b\) 得到无可删位时的预算上界。步长 2、步长 4 偶支、步长 4 奇支分别为 \(24,22,22\)。所有分支的 \(k_{11}=k_{13}=3\)，但 \(m\) 若含 \(11^3\) 或 \(13^3\) 就违反前述比值界。因此每次最多删掉 6 个预算槽。任一 \(b\ge26\) 的反例可反复下降，首次进入小于 26 时仍有 \(b\ge20\)。此前已排除相同放宽模型在预算 20 和 21 的超界目标。 [预算 20 证明](https://github.com/awdawmip/enterprise-math/blob/d1740aaf7da9005f6acd5378a449761cba93df38/research_notes/portable_direct/riesel_r4_twenty_sharp_20261127/REPORT.md)

## 四个有限基例

粗筛沿用原固定孔集、模 11/13 相位分层和阶库存。四次核验分别跑预算 22、23、24、25。前两次用旧删位条件排除 \(64\mid m\) 或 \(243\mid m\) 的目标，分别降到已核验的小预算。后两次使用上述逐分支 \(k_p\)，当删位后预算至少为 20 时，目标可以交给严格更小的预算。对不能这样下降的目标，再使用以下有限容量检查。

取固定非负整数权表。模 11、13 分别去掉 \(j,k\) 个已占全相位时，需求乘 \((11-j)(13-k)\)。某竞争类是否含 11、13 因子决定其乘数依次为 \((11-j)(13-k)\)、\(11(13-k)\)、\(13(11-j)\)、\(143\)。若要求相对期含数位 \(p^a\)，且候选类带相位标记 \(\ell\mid143\)，相对期超过 30 的类至少为大于等于 31 的最小 \(\operatorname{lcm}(p^a,\ell)\) 倍数。低周期类枚举所有相容相位，有限库存按原上限分组。

对给定目标相对期 \(m\)，对每个 \(g\mid L\) 且 \(\gcd(gm,L)=g\)、\(sgm>T_b\)，求模 \(g\) 各切片的最大权和，除以 \(m\)，再乘真实相位因子。用这些上界的最大值给目标计费。每个私有点数位所需的竞争类必须互异，按其可以使用的库存槽取最小容量损失并相加。把模 11/13 的全相位槽用于相应首位时给零损失。这放宽了竞争类的实际分配，所得容量仍严格小于需求就能排除目标。固定权表由数值搜索提出，所有排除使用整数重新验证。

| 预算 \(b\) | 原阶上界 \(T_b\) | 细分库存 | 实际检查的相对周期与细分组合 | 保留 |
|---:|---:|---:|---:|---:|
| 22 | 10,321,920 | 252,466 | 293,357 | 0 |
| 23 | 20,643,840 | 326,575 | 1,061,397 | 0 |
| 24 | 41,287,680 | 361,363 | 44,530 | 0 |
| 25 | 82,575,360 | 370,690 | 18,878 | 0 |

由有限基例和下降，始终能在同根补全中把最大原阶限制到 \(T_b\)。全部原阶至多 \(T_b\) 的自由奇素坐标给出有限充分观察。其相关相位仅依赖 \(a^2\bmod q\)，可用根余数判定或由任一未来项余数复原。原 CRT 开关在每个 \(b\ge11\) 给出成本 \(b/b+1\) 的根对，在阶恰为 \(T_b\) 的素坐标上改变判定，因此两个观察量都取等号。按预算逐项的最小充分坐标集、精确密度和最小根仍是独立问题。

## 复算

从[代码与库存](reproduction.json)、[固定权表](weights.json)和[精确结果](results.json)提取其中 UTF-8 文件。把[固定预算 19 复算原文](https://github.com/awdawmip/enterprise-math/blob/660f791ed86d245524e32610ee73bbb65db38085/research_notes/portable_direct/riesel_r4_nineteen_sharp_20261125/reproduction.json)保存为 \(\texttt{budget19.json}\)。用提供 Map.groupBy 的 Node.js 与 Python 3，先重建并对比低库存表，再核验下降和四个基例。独立 Python 重建了全部 68 种基周期、阈值和达到各阈值的受限类。固定 JSON 按对象逐项对比。

~~~sh
node replay.cjs budget19.json inventory
python verify-schedule.py
python audit-inventory.py budget19.json
node replay.cjs budget19.json 22 weights-22.json inventory.json
node replay.cjs budget19.json 23 weights-23.json inventory.json
node replay.cjs budget19.json 24 weights-24.json inventory.json
node replay.cjs budget19.json 25 weights-25.json inventory.json
~~~
