# 完整联合前缀与带支付误差的实际道路点值 oracle

日期：2026-11-23。作者工作；Researcher-ID `EM-DIRECT-B5750A / TASK_RESEARCH`，既有 Activity `RA-60C6D083A81B19084A74C5BA`。本分支不新建身份、正式 Result 或独立 Review。没有进行远端写入。

本稿对原生 X6 轴上的同一辅助标量读出工作。完整整数人口、单位、合数、背景、全部厚度参数、完整前缀、真实端点继续保留。辅助参考 Λ 只用于一个有明确误差支付的数值 oracle；结论是实际厚度道路 q 的上下界。这里没有把有符号抵消等同于 BRC 正质量抵消，也没有证明无界窗口的真实正能量估计。

## 1. 本轮信息增量

1. 核清实际卷积约定，给出保留单位与背景的联合前缀恒等式及同商分组。说明预处理成本与泛系数单项查询模型的精确读取下界；没有把换求和顺序称为端到端子线性算法。
2. 在已有逐整数厚度匹配误差之上，证明一个新点误差界。当匹配阶数 k≥log B 时，完整道路匹配成本可以去掉旧界中的 log B。
3. 据此构造实际 q 的带支付误差点值 oracle。它只生成辅助参考的共同 prime-power 前缀；不生成完整 D、c、q 数组，不做厚度指数运算。原道路通过解析误差半径包围。
4. 在此前固定的 1,270 个实际采样位置上获得新的闭窗口实际能量夹逼。新上端只比原高精度实际点表的上端增加约 0.031949%。查询几何沿用旧表，本轮没有重新声称发现这套自适应节点。

主要输出为 `paired_prefix_certificate.json`；复算脚本为 `certify_paired_prefix.py`。全部数值向外舍入至分母 10^80，时间只作诊断。

## 2. 实际 c 约定与完整背景的精确消去

设 g_n=n log n，g_0=g_1=0。沿用

\[
D_1=0,\qquad\kappa_n=n\Delta^2g_n,\qquad
c=\mu*(D-\kappa),\qquad c(1)=-2\log2.
\tag{2.1}
\]

因此正确的整除卷积是

\[
D_n-\kappa_n=\sum_{d\mid n}c(d).
\tag{2.2}
\]

把已有 c 当作 μ*D 会漏掉背景，连单位项也会改变。原实际道路的完整前缀公式为

\[
q(y)=y(1+\gamma-\log y)+
\sum_{n\le y}(y/n-1)D_n,
\quad q_0=0,\quad q_1=1+\gamma.
\tag{2.3}
\]

背景有两个不能分别删除的前缀：

\[
\sum_{n\le y}\frac{\kappa_n}{n}=g_{y+1}-g_y,
\qquad
\sum_{n\le y}\kappa_n=y(g_{y+1}-g_y)-g_y.
\tag{2.4}
\]

它们在同一个线性组合中的差精确等于 g_y。因此

\[
\sum_{n\le y}(y/n-1)\kappa_n=y\log y.
\tag{2.5}
\]

式 (2.4) 由一次、一次带 n 权重的离散望远镜求和得到；式 (2.5) 保留了背景的全部贡献，只是在最终联合式中精确消去。把 (2.2) 代入 (2.3)，有限换序给出

\[
\boxed{
q(y)=y(1+\gamma)+\sum_{d\le y}c(d)
\left[\frac yd H_{\lfloor y/d\rfloor}-\lfloor y/d\rfloor\right].
}
\tag{2.6}
\]

这里 H_j=∑_{1≤r≤j}1/r。d=y 的系数为零；d=1 的单位项保留。等价地，从 Δ²q_n=(D_n−κ_n)/n、q_0=0、q_1=1+γ 直接作两次求和，也得到 (2.6)。

## 3. 共同商分组及实际计算边界

记

\[
C_0(v)=\sum_{d\le v}c(d),\qquad
C_1(v)=\sum_{d\le v}\frac{c(d)}d.
\]

把 [1,y] 分成极大整数块 [u,v]，使 k=floor(y/d) 在块内固定。则

\[
\boxed{
q(y)=y(1+\gamma)+\sum_{[u,v],k}
\{yH_k[C_1(v)-C_1(u-1)]-k[C_0(v)-C_0(u-1)]\}.
}
\tag{3.1}
\]

两种前缀使用同一组边界，在合成前不取绝对值或正部。令 s=floor(sqrt(y))，商块数恰为 s+floor(y/(s+1))，至多 2 sqrt(y)。证明可按 d≤s 的单点大商部分和 d>s 的小商部分分类；边界处两部分是否有公共商由第二项精确处理。脚本从 u=1 开始取 k=y//u、v=y//k，再令 u=v+1。

这个公式给出了 **已有 C_0、C_1 查询 oracle 后**的 O(sqrt(y)) 查询代价。它没有自动给出这些前缀的生成算法。若从长度 B 的一般 c 表开始，仍需读完整表并建立两个前缀；只保留所需端点可减少存储，但不能省去通用的全长扫描。若完整 D 表已经生成，则按递增 y 共同维护 ∑D_n 与 ∑D_n/n，仅需 O(B+K) 的批量点值工作，逐点重跑商分组未必更快。

对当前固定 1,270 个位置，精确计数为：

| 项目 | 数量 |
|---|---:|
| y=B=32768 的商块 | 361 |
| 全部查询的商块访问 | 214,964 |
| C_0、C_1 需要的不同端点，含 0 | 4,333 |
| 不同 H_k 参数 | 4,332 |

本轮没有为这些商块重造全长真实 c 表。脚本对一个保留单位的有正有负有理系数族，在所有 1≤y≤96 上精确核对了源求和、直接除数求和和同商分组的三者相等；这是代数及边界核对，既非真实算术抵消证据，也不是端到端性能基准。

### 3.1 泛系数精确读取下界

在只允许查询单个 c(d)、没有额外前缀 oracle 或结构的任意系数输入模型中，精确求 q(y) 必须读取 c(1),…,c(y−1)。事实上对每个 d<y，k=floor(y/d)≥1，

\[
\frac ydH_k-k=\sum_{r=1}^k(y/(dr)-1)>0,
\]

其中首项严格为正而各项非负。若某 c(d) 未被查询，改变它而保持其他输入不变会改变 q(y)，算法却无法区分。因此最坏至少 y−1 次读取。

该下界限定于任意系数的单项 oracle 模型；它不排除实际 c 的解析结构、批量筛法、额外前缀算法或允许受控误差后更好的方法。

## 4. 新的厚度匹配点误差界

本节使用已有的 **直接厚度插值定理**，不从 c−c*=μI 错误地省去除数个数因子。对当前固定 m 个正厚度 a_j、Lagrange 权 ν_j，设

\[
k=m+1,\qquad a_m=\frac{\prod_{j=1}^m a_j}{(m+1)!}.
\]

直接插值给每个整数 n≥2

\[
|D_n-\Lambda(n)|\le a_m(\log n)^k,
\qquad D_1=\Lambda(1)=0.
\tag{4.1}
\]

完整证明的既有定位是 Source `c0a6ba0f7647761f5f0a018bdf03c84714149b00` 下
`rh_arithmetic_next_20261122/ARITHMETIC_FINE_REMAINDER_BOUNDS.md` §1。
核心导数界为：R_a(n)=∏_{p|n}(1−p^(−a)) 满足 |R_a^(j)(n)|≤(log rad(n))^j；又 R_a(n)/a=∫_0^1R'_{ta}(n)dt。对 a=0 的 m 节点插值误差即为 (4.1)。n=1 单独依既定单位约定处理。

定义使用同一 affine 项及完整前缀的辅助参考

\[
q^*(y)=y(1+\gamma-\log y)+
\sum_{n\le y}(y/n-1)\Lambda(n).
\tag{4.2}
\]

则 q−q* 的精确差为

\[
q(y)-q^*(y)=\sum_{n=2}^y(y/n-1)(D_n-\Lambda(n)).
\tag{4.3}
\]

**定理。** 若 y≥2 且 k≥log y，则

\[
\boxed{
|q(y)-q^*(y)|\le E(y):=
a_m(\log y)^k\frac{(y-1)(y-2)}{2y}.
}
\tag{4.4}
\]

**证明。** 对 2≤n≤y，令 z=log(y/n)/log y，0≤z<1。由 1−z≤e^(−z)，

\[
\left(\frac{\log n}{\log y}\right)^k
\le (n/y)^{k/\log y}\le n/y.
\]

式 (4.1) 与 (4.3) 中的权全部非负，因此

\[
|q(y)-q^*(y)|
\le a_m(\log y)^k\sum_{n=2}^y(1-n/y)
=a_m(\log y)^k\frac{(y-1)(y-2)}{2y}.
\]

y=1 两条道路都等于 1+γ，差为零；y=2 的误差也为零，因为唯一非零权对应 n=1 而 D_1=Λ(1)=0。证毕。

### 4.1 完整窗口与任意插值网格

若 k≥log B，令 η_B=a_m(log B)^k。由 E(y)≤η_By/2，

\[
\boxed{
\|q-q^*\|_{w,[A,B]}
\le \frac{\eta_B}{2}\sqrt{B-A+1}.
}
\tag{4.5}
\]

对任意包含真实 A、B 的节点集 Π，同样有 I_ΠE(n)≤η_Bn/2，因为分段仿射插值保持线性函数 n、使用非负重心权。因此

\[
\|I_\Pi E\|_w\le\frac{\eta_B}{2}\sqrt{B-A+1}.
\tag{4.6}
\]

与已有统一源误差推出的 η_B sqrt(B−A+1) log B 相比，这去掉了一个 log B，但增加了明确条件 k≥log B。固定 m 不允许无条件把 B 放到无穷；对随终点变化的匹配族必须逐一核实此条件及 η_B 的大小。该改进控制的是实际道路与参考的差，并不控制 q* 自身的真实正能量。

## 5. 带支付误差的点值 oracle

固定输入 `fixed_matched_family.json` 保留同一组 11 个有理厚度、11 个精确有理权和原 γ 的向外区间；脚本逐项精确核验 ∑ν_j=1、∑ν_ja_j^r=0（1≤r≤10）。输入 `fixed_node_positions.json` 只保存旧节点位置与来源哈希，没有旧实际 q 值。

γ 条目的 `width_upper` 沿用原证书底层区间的宽度元数据，约为 9.42×10⁻⁵⁸；当前显示的 `lower`、`upper` 是扩大舍入后的端点，差为 10⁻⁴⁵。程序只使用这两个安全显示端点，不使用 `width_upper`，也不把旧宽度当作当前显示区间的宽度。

算法先产生所有 p^r≤B 的事件 (p^r,p)，按第一个坐标递增排列。用同一已认证 log p 区间同时维护

\[
S_0(y)=\sum_{p^r\le y}\log p,
\qquad S_1(y)=\sum_{p^r\le y}\frac{\log p}{p^r}.
\]

每个事件只更新一次。在每个请求 y 联合计算

\[
q^*(y)=yS_1(y)-S_0(y)+y(1+\gamma-\log y).
\]

不在这两前缀的相减前取绝对值，也不重置 A 之前的历史。素数幂筛来自辅助 Λ 的定义；原 D 的合数、厚度和其他来源由 (4.4) 的误差支付保留。

设数值计算得到 q*(y)∈[q_*^−(y),q_*^+(y)]，E^↑(y) 是 (4.4) 的有理向上界。给出确定有理端点

\[
\underline q(y)=q_*^-(y)-E^\uparrow(y),
\qquad
\overline q(y)=q_*^+(y)+E^\uparrow(y).
\tag{5.1}
\]

于是它们真正包围实际 q(y)。这更换了点值读取的精度预算，不声称重新获得了每个真实 D 点或 60 位的实际 q 值。使用确定端点也使后续正部支持的符号查找不必处理宽参数区间。

### 5.1 计算成本的准确范围

本实现使用长度 B+1 的 bytearray 素数筛，故仍有至少线性规模的筛空间和预处理。它生成 π(B) 个 log p 区间及所有 prime-power 事件；本实现还排序事件。对 K 个已排序查询位置，事件前缀的高精度累积次数为事件总数，另外每个查询有常数次区间运算、一次 log y 查询及 O(log k) 次区间乘法构造误差。

它节省的是厚度产品、厚度指数 oracle 和完整高精度源数组，并将高精度前缀工作从每个整数改为每个 prime-power 事件。这里没有声称素数筛端到端子线性，也没有把固定 K 的观察复杂度等同于生成算术前缀的工作量。

## 6. 接回实际闭窗口能量

当前 A=1024、B=32768、m=11、k=12。证书核实 log B<12、η_B<10^(−6) 以及 log B+10^(−6)<12。由 1≤κ_n≤1+1/(2n²) 以及 |D−Λ|≤η_B，整个窗口内

\[
-12/n\le f_n=-\Delta^2q_n\le C/n,
\qquad C=1+1/(2A^2)+10^{-6}.
\tag{6.1}
\]

令 v_n=nH_n，则 Δ²v_n=1/n。下述端点函数产生实际上下包络：

\[
U=I_\Pi(\overline q+Cv)-Cv,
\qquad L=I_\Pi(\underline q-12v)+12v.
\tag{6.2}
\]

由离散凸凹割线性质及 (5.1) 的非负重心权，逐个整数都有 L≤q≤U。全部真实端点也包含在内。因此

\[
\|L_+\|_w^2\le S(q)\le\|U_+\|_w^2.
\tag{6.3}
\]

使用上一批 `harmonic_evaluation/certify_fast_harmonic_energy.py` 的六矩精确聚合与符号支持算法，本轮得到向外显示的严格边界

\[
\boxed{
0.00339744175094222292072218385818272
\le S(q)\le
0.00349951536781185863307257718945826.
}
\tag{6.4}
\]

比较如下。前三列中的能量数是阅读近似；完整整数区间在 JSON 中。

| 项目 | 原真实高精度节点输入 | 新有支付误差 oracle |
|---|---:|---:|
| 节点数 | 1,270 | 同一 1,270 |
| 实际正能量下界 | 0.00339846140820011535 | 0.00339744175094222292 |
| 实际正能量上界 | 0.00349839766509688830 | 0.00349951536781185863 |
| B 处匹配点误差预算 | 旧粗界 0.24324849298594951 | 新界 0.01169670887587848 |

新上端增加 0.00000111770271497033，约原上端的 0.03194899%。新点误差界在 B 处比旧粗界小约 20.7963 倍。对真实样本的后验交叉核对显示 1,270 个旧区间全部位于 (5.1) 内；最大观测差在 B，约为 1.43119331842619×10^(−7)。这个观察没有用于缩小误差半径。

插值误差半径的平方能量严格位于

\[
\|I_\Pi E^\uparrow\|_w^2\in
[0.00000000123650583564714649124963458,
 0.00000000123650583564714649124963459],
\]

平方根约 3.51639849227465×10^(−5)。只用统一 (4.5) 的误差平方上界则约 4.045594466744935×10^(−9)。这些是厚度匹配误差的支付，不是对真实 q 能量的新算术抵消定理。

本次运行：3,512 个素数、3,590 个 prime-power 事件，点 oracle 共 4,782 个不同 log 参数；厚度指数调用与厚度乘积更新均为零。旧完整道路证书曾记录 38,632 次厚度指数调用、241,406 次素因子乘积更新和 32,769 个不同整数 log 参数。两次工作输出与精度预算不同，因此这些是被避免的操作类别和数量，不能作为同任务运行时间倍数。

新点 oracle 本次约 0.567 秒，随后上下能量及半径能量聚合约 8.678 秒；平台负载会改变这些时间。旧全证书的总时间包含相位与完整重构等其他工作，不能据此宣称同类端到端加速比。

## 7. 复算与输入来源

从 `/workspace/scratch/35f07cb72083` 执行：

```sh
python3 continuation_20261123/prefix_compute/certify_paired_prefix.py \
  --harmonic-module harmonic_evaluation/certify_fast_harmonic_energy.py \
  --family continuation_20261123/prefix_compute/fixed_matched_family.json \
  --nodes continuation_20261123/prefix_compute/fixed_node_positions.json \
  --comparison-samples inputs/rh_partial_frontier_20261122/sparse_sample_observations.json
```

`--comparison-samples` 可省略；它只在新点 oracle 完成后读取旧实际点值并进行有限包含检查，不参与点值生成或能量保证。复算写回本目录同名证书；运行时间字段正常变化。固定节点位置有来源依赖，其数值位置并未在本轮重新选择。

主要不可变来源：

- 原厚度与 γ 输入：`rh_correlation_rational/rational_window_certificate.json`，SHA-256 `d2c00df289bbac268fa54ed77c187edcc741c1fbc4d052069eef389c93f5815f`；本目录保存所需子集和原文件哈希。
- 原完整道路定义脚本：`rh_joint_certificate/certify_joint_energy.py`，SHA-256 `ff6c4cbbc395a152368f50500d820c4f117f680e49ef04c2ad59a93f96d251bf`。旧操作计数来自同目录 `joint_energy_certificate.json`，SHA-256 `c08c5d37251b5969217c6c5fa54210fd79b161094b19c3a167ab3e045ea804ea`。
- 厚度直接插值证明：Source `c0a6ba0f7647761f5f0a018bdf03c84714149b00`，前缀 `research_notes/portable_direct/rh_adaptive_sampling_20261122_b5750a`，相对路径 `rh_arithmetic_next_20261122/ARITHMETIC_FINE_REMAINDER_BOUNDS.md`；SHA-256 `f4934e4eb8fa7b96f2bd6da500ef45918b41f75ea75ef5fbfd484df98a1ce6a7`。
- 原实际稀疏点表：同一 Source，`rh_partial_frontier_20261122/sparse_sample_observations.json`；SHA-256 `63952b36db78e327b950e8806f0647519f3e9cde5ba4b8201413b984de23bcfa`。
- 谐和六矩聚合：Source `4d63cb1b1fc65a21c940a17e3eae5c691017e24a`，前缀 `research_notes/portable_direct/rh_global_sampling_20261123_b5750a`，`harmonic_evaluation/certify_fast_harmonic_energy.py`；SHA-256 `d1c3201cfe08d770d3b7de48548b7ab575860c984fa823ce9e9ba42765be1377`。

所有本轮生成代码、固定输入及输出的实际哈希另列于 `MANIFEST.json`。这里的推导、精确有理核对与真实有限包含检查全部属于作者工作内的核验，不充当独立 Review。
