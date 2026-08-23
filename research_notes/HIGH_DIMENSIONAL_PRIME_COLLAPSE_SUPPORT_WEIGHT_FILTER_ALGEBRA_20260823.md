# 高维坍缩素数实验 E3 — 支撑权重滤波代数与 λ=2 共振

Status: `FREE_RESEARCH / DERIVED_EXPERIMENTAL_CARRIER_STRUCTURE / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-HDPB-2308A9`

## 1. 动机

E1/E2 表明：raw single-dimension shell count 很快被高维组合膨胀淹没，而跨维 alternating filter 在 d=4,8,10,12 暴露出精确或统计算术结构。

本阶段不预设 native negative axes，也不预设“sign completion 必须特殊”。直接给每个非零坐标一个形式权重/颜色参数 `lambda`。

## 2. 支撑权重族

令 `A_s(n)` 为恰有 `s` 个严格正坐标的 ordered square-sum states。

定义

`W_{d,lambda}(n) = sum_s binom(d,s) A_s(n) lambda^s`.

等价地，若

`S(q)=sum_{m>=1} q^(m^2)`,

则

`W_{d,lambda}(n) = [q^n] (1 + lambda S(q))^d`.

因此：

- `lambda=1`: `W=C_d`, 原始 `N_0^d` shell;
- `lambda=2`: 每个 active coordinate 有两个 decorations；数值上等于 classical signed shell multiplicity，但该解释不需要把 negative axis 加进 native carrier;
- `lambda=0`: 只保留 zero-support state;
- `lambda` polynomial coefficients 精确恢复 support spectrum.

## 3. 复合律

在 generating carrier `F=1+S` 上定义

`T_lambda(F)=1+lambda(F-1)`.

则

`T_lambda(T_mu(F)) = T_(lambda*mu)(F)`.

所以 support recoloring/filter family 具有乘法半群律：

`T_lambda o T_mu = T_(lambda mu)`.

这给出一个不依赖外部 modular-form vocabulary 的 dimension-filter algebra。

## 4. 与向下坍缩率的统一

有

`d/dlambda W_{d,lambda}(n)|_{lambda=1} = sum_s s binom(d,s) A_s(n)`.

因此 raw shell 中的 mean support 为

`E_d[s] = W'_{d,1}(n) / W_{d,1}(n)`.

而此前 fixed-face downward-collapse survival 恰为

`F_d(n)=C_{d-1}(n)/C_d(n)=1-E_d[s]/d`.

故同一个 `lambda`-family 同时编码：

- support spectrum;
- raw high-dimensional shell;
- mean active dimension;
- fixed-face collapse survival;
- binary-decoration arithmetic audit at `lambda=2`.

## 5. λ 消融扫描

P5000 exact scan：对 integer

`lambda in {-4,-3,-2,-1,1,2,3,4,5}`

以及 even `d=4,6,8,10,12`，按 `p mod 8` 分组。每组尝试用 degree `d/2-1` 的 polynomial in `p`：最少点 exact interpolation，其余全部 exact holdout。

结果摘要：

### d=4

- `lambda=2`: all four mod-8 classes rigid;
- every other scanned nonzero lambda: only the `7 mod 8` birth-4 channel remains trivially rigid; other residue classes fail.

### d=6

- only `lambda=2` makes all four residue classes rigid.

### d=8

- only `lambda=2` makes all four residue classes rigid.

### d=10

- `lambda=2` keeps classes 3,7 rigid;
- classes 1,5 retain the 2D angular echo and fail one-variable rigidity.

### d=12

- no scanned lambda gives the naive residue-conditioned one-variable polynomial rigidity across all channels.

This scan does not prove global uniqueness over arbitrary real/complex lambda. It establishes a strong integer ablation and motivates the exact d=4 projector calculation below.

## 6. d=4 的非零共振唯一性

对 odd prime `p`，`A_1(p)=0`，故

`W_{4,lambda}(p)=6 lambda^2 A_2 + 4 lambda^3 A_3 + lambda^4 A_4`.

4-square audit relation给出 support-linear wall

`24 A_2 + 32 A_3 + 16 A_4 = 8(p+1)`.

若要求一个 **support-independent projector**：`W_{4,lambda}` 对所有允许的 `(A_2,A_3,A_4)` 只读取该 wall，而不保留额外 support composition，则其系数向量必须与

`(24,32,16)`

成比例。

因此必须有

`6 lambda^2 / 24 = 4 lambda^3 / 32 = lambda^4 / 16`.

对 `lambda != 0`，前两项给 `lambda=2`，后两项也给 `lambda=2`。

所以

`lambda=2`

是 d=4 中唯一的非零 support-independent wall projector。

这说明 2 的特殊性可以从盆地支撑消元反向导出；不需要把“正负号”作为 Phase-A 起点。

## 7. 当前层级图

实验至此形成：

`support spectrum A_s`

`-> lambda-filter semigroup W_{d,lambda}`

`-> lambda=1 raw shell / derivative = collapse survival`

`-> lambda=2 resonance`

`-> d=4 sigma_1 wall`

`-> d=8 sigma_3 wall`

`-> d=10 2D angular echo`

`-> d=12 semicircle-distributed residual`.

这是目前最紧凑的统一描述。

## 8. Verdict

Freeze:

`HDPB_E3_SUPPORT_WEIGHT_FILTER_SEMIGROUP_FOUND`.

`HDPB_E3_LAMBDA2_IS_UNIQUE_NONZERO_D4_SUPPORT_INDEPENDENT_WALL_RESONANCE`.

Claim status：

- combinatorial identities / semigroup law: exact on the experimental carrier;
- d=4 lambda=2 projector uniqueness: exact under the stated support-independent projector criterion;
- integer lambda scan in d=4..12: finite computational evidence;
- no claim that this structure is a new theorem in classical theta-function language.

## 9. Next executable question

Do not merely increase d.

Next test:

> determine whether the d=10 angular residual and d=12 semicircle residual can be obtained as successive irreducible components of the same `lambda=2` dimension-filter algebra after quotienting the lower d=4/d=8 divisor walls.

This is the first route that could turn the observed sequence `wall -> angular echo -> distributed residual` into an intrinsic high-dimensional collapse decomposition rather than a list of classical coincidences.
