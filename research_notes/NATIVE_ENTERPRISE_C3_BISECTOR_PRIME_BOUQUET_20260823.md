# Enterprise 三扇区等坐标射线：C3-balanced prime bouquet

Status: `FREE_RESEARCH_OBSERVATION / COMPUTATIONAL_CENSUS / PRESENTATION-STABILITY_CANDIDATE / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent candidate: `ENTERPRISE_TRI_SECTOR_SPIRAL_V0`

## 1. General cyclic ray orbit

在固定 tri-sector shell spiral 中，取 `S12` 的 primitive address ray

`(a,b,0)=m(u,v,0)`，`gcd(u,v)=1`，`u,v>=0`。

记

`s=u+v`，`r=sm`，`B_r=3r(r-1)/2+1`。

该 ray 及其两次 cyclic axis relabeling 的整数标签为

`F0(m)=B_{sm}+vm`，

`F1(m)=F0(m)+sm`，

`F2(m)=F0(m)+2sm`。

等价地：

`2F0 = 3s^2 m^2 + (-3u-v)m + 2`，

`2F1 = 3s^2 m^2 + (-u+v)m + 2`，

`2F2 = 3s^2 m^2 + (u+3v)m + 2`。

所以每个 primitive native address ray 自动产生一个 C3-orbit of quadratic integer sequences。

## 2. Equal-coordinate ray is algebraically special

取最简单的 sector-equality locus

`u=v=1`。

三个 cyclic rays 为

- `S12: (m,m,0)`；
- `S23: (0,m,m)`；
- `S31: (m,0,m)`。

其标签严格为

`F_-(m)=6m^2-2m+1`，

`F_0(m)=6m^2+1`，

`F_+(m)=6m^2+2m+1`。

冻结观察：

`EQUAL_COORDINATE_C3_ORBIT -> SYMMETRIC_QUADRATIC_TRIPLET`。

并且

`F_+(m)=F_-(-m)`。

因此左右两条 lane 对每个模数具有相同的 root-count profile；它们的 local sieve structure 完全同型。

## 3. Presentation stability

Cyclic axis relabeling只会轮换

`{F_-,F_0,F_+}`。

反向 traversal / orientation reversal交换

`F_- <-> F_+`

并保持中央 `F_0` 的角色。

因此单独哪一条 ray 最亮可能依赖 presentation，但无序三元组

`{6m^2-2m+1, 6m^2+1, 6m^2+2m+1}`

具有更强的 presentation stability。

这是当前比“某条 visually prime-rich line”更值得保留的对象。

## 4. Primitive-ray bounded census

冻结 census：

- primitive `u,v>=0`；
- `u+v<=10`；
- 每个 cyclic slot 取 `m=1,...,1500`；
- 共 33 个 primitive ray classes；
- placement formula 在 primality evaluation 之前固定。

对每个 ray class 记录：

- 三个 slot 的 prime rate；
- mean prime rate；
- `C3_CV = population_std(slot_rates)/mean(slot_rates)`。

结果：`(u,v)=(1,1)` 的 counts 为

`230 / 222 / 219`，

mean rate

`0.149111111111...`，

C3 CV

`0.020757657641...`。

在这 33 个 bounded primitive classes 中：

1. `(1,1)` 的 C3 imbalance 最小；
2. 在 `C3_CV < 0.1` 的 classes 中，`(1,1)` 的 mean prime rate 最高。

因此在这个冻结的小复杂度 census 里，equal-coordinate ray 同时取得：

`HIGH_PRIME_DENSITY + BEST_C3_BALANCE`。

这只是 finite census，不主张全局最优定理。

## 5. Scale stability check

对 `(1,1)` 单独扩大到 `m<=5000`：

- `F_-`: `633/5000 = 0.1266`；
- `F_0`: `628/5000 = 0.1256`；
- `F_+`: `666/5000 = 0.1332`。

mean rate：

`0.128466666667...`。

C3 CV：

`0.026246328213...`。

所以首轮 `m<=1500` 的三路均衡没有在扩大到 5000 时崩掉。

## 6. Small-prime local sieve diagnostic

定义单 polynomial 的有限 local factor product

`S_Q(f)=product_{q prime<=Q} ((1-nu_q/q)/(1-1/q))`，

其中 `nu_q` 是 `f(m)=0 mod q` 的 residue-root 数。

这只是 finite sieve diagnostic，不作为 prime infinitude/asymptotic proof。

取 `Q=100000`：

- `F_-`: `S_Q ≈ 2.11287172315`；
- `F_0`: `S_Q ≈ 2.13812703567`；
- `F_+`: `S_Q ≈ 2.11287172315`。

左右严格同值来自 `m -> -m` 对称；中央 lane 的 finite local factor 也非常接近。

这给 C3 prime-density balance 一个直接 arithmetic explanation：三条 lane 不只是图上相邻，它们的小素数筛余结构也很接近。

## 7. Novelty boundary

Quadratic prime-rich sequences、Ulam-like lines、以及 `6m^2+1` 一类 polynomial prime questions 都已有 classical literature / sequence prior art。

因此不主张这些 polynomial 本身新。

当前值得继续的 Enterprise-specific statement 是：

> 由 `min=0` 三扇区 atlas + `a+b+c=r` shell + equal-coordinate loci 自动选出一个 presentation-stable C3 quadratic bouquet；该 bouquet 在冻结 bounded census 中兼具低 C3 imbalance 和高 prime density。

## 8. Current verdict

`C3_EQUAL_COORDINATE_PRIME_BOUQUET = STRONGEST_NATIVE_PATTERN_CANDIDATE_SO_FAR`。

下一步优先级：

1. 对该 unordered triplet 做 exact local-residue classification；
2. 比较 fixed / alternating orientation，验证 bouquet set 是否严格不变；
3. 扩大 primitive ray census complexity 与 sample depth；
4. 检查 twin-prime / prime-gap / semiprime 是否在三 lane 间形成更强的 cyclic relation；
5. 只有经过这些消融仍存活，再把 bouquet 作为高维 native collapse 的二维 seed。
