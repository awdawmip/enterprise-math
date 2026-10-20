# 进取坐标系素数分配实验：三扇区壳层螺旋

Status: `FREE_PHASE_A_FROZEN_CANDIDATE / PHASE_B_PRIOR_ART_AUDITED / COMPUTATIONAL_EXPLORATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Owner branch: `research/native-enterprise-prime-trisector-spiral-20260823`

## 0. 方向纠偏

此前高维平方和盆地是有意保留的 classical orthogonal control，不再作为本研究主角。

本实验只问：在当前 Enterprise 三正轴、三扇区、非负 canonical 地址

`A_E={(a,b,c) in N_0^3 : min(a,b,c)=0}`

上，怎样先为 **全部正整数** 定义一个低复杂度、非 prime-aware 的地址分配，再观察素数是否形成更清楚的 native pattern。

冻结：

`PRIMALITY_MUST_NOT_CHOOSE_THE_COORDINATE`。

即先排全体整数，后点亮素数，避免目标泄漏。

## 1. 主候选：ENTERPRISE_TRI_SECTOR_SPIRAL

定义地址壳层

`h(a,b,c)=a+b+c=r`。

由于 canonical 条件 `min(a,b,c)=0`，固定 `r>=1` 时壳层恰为三段：

- `S12: (r-j,j,0)`；
- `S23: (0,r-j,j)`；
- `S31: (j,0,r-j)`；

其中每段取 `j=0,...,r-1`，共享端点只计一次。

因此第 `r` 层严格有

`3r`

个地址，前 `r` 层共有

`3r(r+1)/2`

个地址。

这条分层只使用三正轴地址和三扇区 gluing；不需要负轴，不需要 cross-sector subtraction，也不需要把 classical carrier distance 当作 native metric。

### 固定方向版本

从 `E1` 开始，按

`E1 -> S12 -> E2 -> S23 -> E3 -> S31 -> E1`

的 cyclic sector order 放置连续整数。

第 `r` 层起始整数为

`B_r = 3r(r-1)/2 + 1`。

因此在 `S12` 上：

`N(r-j,j,0)=B_r+j`。

在 `S23` 上：

`N(0,r-j,j)=B_r+r+j`。

在 `S31` 上：

`N(j,0,r-j)=B_r+2r+j`。

## 2. 为什么会自然长出“素数线”

固定一条 sector 内的 rational address ray，例如

`(a,b,0)=m(u,v,0)`，`gcd(u,v)=1`。

其壳层指数是

`r=(u+v)m`。

而壳层起点 `B_r` 本身是 `r` 的二次函数，sector 内位相是 `m` 的一次函数。

所以任一固定 rational ray 上的整数标签自动成为 `m` 的二次序列。

因此本图中若出现 prime-rich ray，不需要先把素数放在线上；它是

`THREE_POSITIVE_AXIS COORDINATES -> LINEAR SHELL SIZE 3r -> QUADRATIC RAY LABEL`

的直接结果。

这与 classical Ulam-type prime lines 的“几何直线对应二次多项式”机制兼容，但这里的 shell/ray 是从当前 Enterprise 三扇区 atlas 生成。

## 3. 三条 native axis 的显式二次序列

固定方向版本中：

`E1(r): N = 3r(r-1)/2 + 1`；

`E2(r): N = 3r(r-1)/2 + r + 1`；

`E3(r): N = 3r(r-1)/2 + 2r + 1`。

所以三条 positive native axes 本身就是三条二次 arithmetic lanes。

## 4. 首轮完整壳层实验

取

`r<=114`。

总地址数正好

`N=3*114*115/2=19665`。

其中素数共

`2226`，总体素数密度

`0.113196033562...`。

### 固定 cyclic 方向

三条 native axes 各有 114 个位置，素数数目：

- `E1: 26/114`；
- `E2: 25/114`；
- `E3: 27/114`。

三轴合计：

`78/342 = 0.228070175439...`。

相对于整张图的素数密度，三轴富集比约为

`2.01482479784`。

三个 sector interior 的 prime density：

- `S12 = 685/6441 = 0.106349945661...`；
- `S23 = 700/6441 = 0.108678776587...`；
- `S31 = 763/6441 = 0.118459866480...`。

所以第一轮已经出现：

`NATIVE_POSITIVE_AXES ≈ 2x GLOBAL PRIME DENSITY`

且三条正轴在同一尺度上相当均衡。

这是实验观察，不升格为渐近定理。

## 5. 方向消融：偶数壳反向

为测试视觉/sector imbalance 是否只是固定 traversal orientation 造成，定义最小消融：

- 奇数壳：`E1 -> E2 -> E3`；
- 偶数壳：仍从 `E1` 起，但反向遍历。

在相同 `r<=114` 完整样本上：

- `E1 = 26/114`；
- `E2 = 26/114`；
- `E3 = 26/114`。

三个 sector interior：

- `S12 = 726/6441 = 0.112715416861...`；
- `S23 = 700/6441 = 0.108678776587...`；
- `S31 = 722/6441 = 0.112094395280...`。

这一版本在首轮尺度上呈现更强的三扇区均衡，但该精确 `26/26/26` 不能当成结构恒等式；扩大半径后会出现普通算术波动。

因此：

- `FIXED_CYCLIC` 是更简单、公式最干净的主版本；
- `ALTERNATING_ORIENTATION` 是 symmetry ablation/control。

## 6. 与两个替代壳层的首轮比较

同一 `N=19665` 规模做三个候选比较。

### A. Native norm rank

按当前 origin-based native norm

`L_E^2=a^2+b^2+c^2`

排序，再用一个固定 sector phase 破 tie。

优点：metric provenance 最强。

缺点：在最简单 tie-breaking 下，视觉 prime-lane 信号较弱，而且固定 phase 引入明显 sector arithmetic bias；这说明“canonical radius”与“beautiful integer enumeration”不是同一问题。

### B. Tri-sector sum shell（主候选）

`a+b+c=r`。

优点：

- 只依赖三正轴 atlas；
- 每层严格 `3r`；
- 三 sector 完全同型；
- straight native address rays 自动对应 quadratic sequences；
- 首轮三轴 prime density 约为 global 的两倍。

### C. Address-max shell

`max(a,b,c)=r`。

它会产生 `6r` 的壳层，图像中 prime lanes 更强，首轮三轴总密度约 `84/242=0.3471`。

但它也自然制造六个 carrier directions。当前 foundation 明确只有三条 positive native axes，且不应重新把六向 signed picture 偷渡成 native structure。

因此该版本保留为 **visual high-contrast control**，不作为当前主候选。

冻结：

`STRONGER_VISUAL_CONTRAST != BETTER_NATIVE_PROVENANCE`。

## 7. Phase-B prior-art audit

候选冻结后才打开外部对照。

外部已有：

- Ulam square spiral 及其 quadratic prime lines；
- triangular integer arrays / triangular Ulam-like constructions；
- hexagonal prime spirals。

因此不主张：

- “三角形排素数”本身新；
- “螺旋中出现 prime-rich lines”本身新；
- “六边形 prime spiral”新。

当前真正需要继续检验的是：

1. Enterprise `min=0` 三扇区 atlas 是否选择了一个比 classical presentation 更稳定的 line family；
2. 哪些 prime-rich lanes 对 cyclic axis relabeling、orientation ablation、shell reparameterization 保持不变；
3. 是否存在由 collapse/coordinate semantics 而不是任意 plotting choice 选出的 invariant residue/fingerprint；
4. 是否可把三轴富集写成精确局部 sieve 结构，而不是只做视觉统计。

## 8. 当前 verdict

`ENTERPRISE_TRI_SECTOR_SPIRAL_V0 = SURVIVES_AS_NATIVE-LEANING PRIME-ALLOCATION CANDIDATE`。

最重要的首轮现象：

`THREE-SECTOR SHELL SIZE = 3r`

`=> FIXED RAYS CARRY QUADRATIC INTEGER SEQUENCES`

`=> PRIME-RICH LANES APPEAR WITHOUT PRIME-AWARE PLACEMENT`

并且在 `r<=114`：

`THREE_NATIVE_AXES_PRIME_DENSITY / GLOBAL_PRIME_DENSITY ≈ 2.0148`。

下一步不应先扩大到高维；应先在此二维 native atlas 上做：

`CYCLIC-RELABELING INVARIANTS + RAY POLYNOMIAL CENSUS + SMALL-PRIME SIEVE EXPLANATION + SCALE STABILITY`。

只有 surviving patterns 再进入高维 native collapse extension。
