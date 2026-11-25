# Riesel：任意预算的候选阶上界与次指数阶谱

在原 \(R_1\) 及其三个子族 \(R_2,R_3,R_4\) 上，固定20素数旧字典 \(P\)。对任一正整数预算 \(b\)，令
\[
\mathcal D_b=\left\{d\ge 1:\ \sum_{p^e\parallel d/\gcd(d,210)}e(p-1)\le b-1\right\}.
\]
则给定 \(a\)，考察固定坐标和所有 \(\operatorname{ord}_q(2)\in\mathcal D_b\) 的奇素数根余数，已经足以判定 \(\delta_P(a)\le b\)。结论同样适用于全部未来余数。只有潜在可用的阶，不断言每一阶或每枚素数都必要。推论是
\[
\Omega_b(R_i),\widehat\Omega_b(R_i)\le210\cdot 2^{b-1},
\quad |\mathcal D_b|\le16\exp\!\big(\pi\sqrt{2(b-1)/3}\big).
\]
对 \(b=1\) 可直接数16个 \(210\) 的因子。这一计数说的是不同乘法阶的种类，不是素数个数或最小观察模数的位数。结合[已证的固定十锚下界](https://github.com/awdawmip/enterprise-math/blob/2ae5de00bf7e8f1e2571ef5666e95f82a25dc429/research_notes/portable_direct/riesel_r4_twelve_observer_lower_20261125/REPORT.md)，四族在任意预算 \(b\ge11\) 的上下界相差常数至多 \(128/3\)。

## 用孔集的周期，替代字典全部轨迹的周期

[原先九预算的孔集公式](https://github.com/awdawmip/enterprise-math/blob/9b3680ea1c07b1364af5464a3469313ee616d408/research_notes/portable_direct/riesel_nine_frontier_20261124/prefix/proof.md)表明，旧字典未覆盖的指数恰为 \(n=2u\)，其中 \(u\bmod105\) 落在固定36点集 \(H\)。全部 \(P\) 的共同周期是6720，但“有无被 \(P\) 覆盖”的布尔图周期已经是210。重放脚本从原根固定余数出发逐位核完6720项，验证两个孔集写法相同。原 \(R_1\) 的定义固定了全部 \(P\) 坐标，所有子族共用这些相位。

若 \(a>1\) 是正根，选任一包含极小的至多 \(b\) 枚补全。对其中某枚非空通道取它的私有指数 \(n_0\)，在 \(n\equiv n_0\bmod210\) 的整条进程里没有旧字典命中。目标通道在这条进程的相对周期为 \(m=d/\gcd(d,210)\)。套用[私有点数位引理](https://github.com/awdawmip/enterprise-math/blob/2ae5de00bf7e8f1e2571ef5666e95f82a25dc429/research_notes/portable_direct/riesel_r4_twelve_observer_lower_20261125/REPORT.md)：\(\sum e(p-1)\le b-1\)。这是每一枚补充素数的必要筛选条件。因此所有可能的最小补全都在 \(\mathcal D_b\) 内，可由相位布尔判据读出。真因子也没有小值例外：补全只处理偶数指数 (n=2u)（(uge1)），而 (F_{2u}(a)=(a2^u-1)(a2^u+1)) 对原族的 (a>1) 必为合数；旧 (P) 的真因子性质已由固定原族保证。

因为 \(p\le 2^{p-1}\)，有 \(m\le2^{b-1}\)，而 \(d/m\mid210\)，所以可用的上界从字典轨迹证明的 \(6720\cdot2^{b-1}\) 降为 \(210\cdot2^{b-1}\)。专门的十二预算已有更强上界120960，不被这个通用界替代。

## 阶谱计数

对每个 \(m\)，把它编码为由 \(e\) 份 \(p-1\) 构成的整数划分，其总和至多 \(B=b-1\)。编码单射。每个 \(m\) 至多对应16个 \(d\)，因为 \(d/m\) 为210的因子。对 \(B>0\)，取 \(s>0\)。总划分数（含空划分）至多
\[
e^{sB}\prod_{j\ge1}(1-e^{-sj})^{-1}
\le \exp\left(sB+\frac{\pi^2}{6s}\right).
\]
最后一步来自对数展开和 \((e^{sk}-1)^{-1}\le1/(sk)\)。取 \(s=\pi/\sqrt{6B}\) 即得所示次指数界。实际计数可只使用素数减一作为部件：脚本按无界背包的生成函数计算相对阶种类，预算12为84，预算32为3,226，预算64为126,872。乘16是简单上界，有些因子选择不满足原 gcd 等式，还可进一步剔除。

`node verify.js` 输出孔集对照及精确的相对阶计数。此稿为直接可复算推导，不是项目独立 Review。
