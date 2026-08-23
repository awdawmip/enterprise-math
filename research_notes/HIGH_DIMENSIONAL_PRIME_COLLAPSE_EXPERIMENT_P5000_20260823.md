# 高维坍缩下素数排列实验 E1 — P5000 维数壁与 2D→10D 回声

Status: `FREE_RESEARCH / EXPERIMENT_CHECKPOINT / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-HDPB-2308A9`

Owner branch: `research/free-highdim-prime-collapse-basins-20260823`

Parent basin packet: `research_notes/HIGH_DIMENSIONAL_PRIME_COLLAPSE_BASIN_TABLE_2D_19D_20260823.md`

## 1. 实验范围

主批次：

- quadratic collapse carrier only;
- `n <= 5000`;
- `d = 2,...,19`;
- 669 primes;
- exact integer dynamic programming, no floating fitting in the wall identities.

额外压力检验：

- odd `n <= 100000` for the 4D and 8D prime-wall predicates;
- primes `p <= 100000` for support-existence continuity through dimension 19.

高维 `d>=3` 仍是 `EXPERIMENTAL_COMPUTATION_CARRIER`，不是 canonical native geometry。

## 2. 维数塔的精确 Newton 结构

令 `A_s(n)` 表示恰有 `s` 个严格正坐标的有序平方和表示数：

`x_1^2 + ... + x_s^2 = n`, `x_i > 0`.

令 `C_d(n)` 表示 `N_0^d` 中平方和为 `n` 的有序状态数。

则精确有

`C_d(n) = sum_s binom(d,s) A_s(n)`.

因此 `C_d` 是 `A_s` 的二项式 / Newton lift，并且

`A_s(n) = Delta^s C_0(n)`.

这给出一个原生的“维数差分谱”：维数塔本身可逐阶剥离出恰需 `s` 个活动坐标的成分。

更一般地，若把每个非零坐标的符号选择仅作为 **classical audit multiplicity** 而非 native negative axis，定义

`R_d(n) = sum_s 2^s binom(d,s) A_s(n)`,

则由 Newton inversion

`R_d(n) = sum_{j=0}^d (-1)^(d-j) 2^j binom(d,j) C_j(n)`.

这说明 signed-completion audit 没有增加新的 shell 数据；它只是维数塔上的一个精确有限差分滤波器。

## 3. P5000 出生维数

669 个素数的 birth histogram：

- birth 2D: `330`;
- birth 3D: `168`;
- birth 4D: `171`.

对奇素数精确按 mod 8 分层：

- `p == 1 mod 8`: 161 个，全部 birth 2D;
- `p == 5 mod 8`: 168 个，全部 birth 2D;
- `p == 3 mod 8`: 168 个，全部 birth 3D;
- `p == 7 mod 8`: 171 个，全部 birth 4D.

该 birth 分层是经典二平方/三平方/四平方同余结构在本盆地坐标中的重述，不主张新颖性。

## 4. “出生后连续充满”经验规律

在 `p <= 5000` 中，658/669 个素数的 support set 在 birth 后直到 dimension 19 无空洞。

仅有 11 个例外：

`5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41`.

因此本批次中所有 `p >= 43` 均满足：

`A_s(p) > 0 for every birth(p) <= s <= 19`.

额外只做 existence 的压力检验扩展至 `p <= 100000`（9592 primes），仍只有同一组 11 个小素数例外。

但是 composite control 表明 support-continuity 不是强 prime-specific signal：对 odd nonsquares，较大范围内也快速进入同类饱和。故该现象保留为几何/组合盆地性质，不作为素数判别主信号。

## 5. 4D 精确素数壁

定义

`Q4(n) = 2 C_4(n) - 4 C_3(n) + 3 C_2(n)`.

实验在所有 odd `3 <= n <= 100000` 上得到零误判：

`n prime <=> Q4(n) = n + 1`.

Phase-B classical audit 给出精确解释。对 odd `n`，Jacobi four-square identity 给出

`R_4(n)/8 = sigma_1(n)`.

而维数滤波关系给出

`R_4(n)/8 = -C_1(n) + 3C_2(n) - 4C_3(n) + 2C_4(n)`.

因此

`Q4(n) = sigma_1(n) + C_1(n)`.

其中 `C_1(n)` 在 `n` 为平方时等于 1，否则为 0。

于是对 odd `n>1`：

- prime: `sigma_1(n)=n+1`, `C_1=0`, so `Q4=n+1`;
- composite: `sigma_1(n)>n+1`, hence `Q4>n+1`.

定义 4D collapse excess

`E4(n)=Q4(n)-(n+1)`.

则 odd primes 精确位于 `E4=0` 的仿射壁，odd composites 位于 `E4>0` 一侧。

在计数坐标

`B(n)=(C_2(n),C_3(n),C_4(n))`

中，奇素数严格满足

`3C_2 - 4C_3 + 2C_4 = n+1`.

这比单独观察任一高维 raw shell count 更强。

## 6. 8D 第二张精确素数壁

定义

`Q8(n) = 16C_8 - 64C_7 + 112C_6 - 112C_5 + 70C_4 - 28C_3 + 7C_2`.

实验在所有 odd `3 <= n <= 100000` 上同样零误判：

`n prime <=> Q8(n) = n^3 + 1`.

Phase-B classical audit：对 odd `n`，Jacobi eight-square identity gives

`R_8(n)/16 = sigma_3(n)`.

维数滤波器的 `C_1` 系数为 `-1`，因此

`Q8(n)=sigma_3(n)+C_1(n)`.

故 prime 恰处于最小 divisor-power wall `n^3+1`，composite 严格越过该壁。

4D 与 8D 因而形成两张独立的 exact divisor walls：

- 4D reads `sigma_1`;
- 8D reads `sigma_3`.

## 7. Raw shell count control

同余类匹配的邻近 composite control 显示：不能把 raw high-dimensional count 本身当 prime signal。

以 `log(1+C_d)` 和每个 prime 附近同 mod-8 的最近 composite 作比较，P5000 的代表性 median gaps 为：

- d=2: approximately `0`;
- d=4: approximately `-0.2747`;
- d=8: approximately `-0.0148`;
- d=10: approximately `+0.0074`;
- d=19: approximately `+0.0007`.

高维 raw count 的 prime/composite 差异很快被普通组合膨胀淹没；真正干净的信号来自维数之间的 **alternating exact filter**，不是单层计数。

## 8. 10D：2D 角向信息再次显影

对 signed-completion audit shell `R_10(p)`：

### 8.1 inert channel: p == 3 mod 4

P5000 中全部 339 个 `p == 3 mod 4` 素数精确满足

`R_10(p)=12(p^4-1)`.

该通道保持一变量刚性。

### 8.2 two-square channel: p == 1 mod 4

对唯一正整数二平方分解（交换不计）

`p=a^2+b^2`,

定义四次角向量

`H4 = a^4 - 6a^2b^2 + b^4`.

P5000 中全部 329 个 `p == 1 mod 4` 素数精确满足

`5 R_10(p) = 68(1+p^4) + 64 H4`.

等价地

`H4 = p^2 - 8 a^2 b^2`.

因此 10D shell residual 可反向恢复

`u=(p^2-H4)/8=(ab)^2`,

再由

`(a^2-b^2)^2 = p^2 - 4u`

恢复 `{a^2,b^2}`，从而恢复 `{a,b}`。

本批次 329/329 exact recovery。

Phase-B comparison：这正对应 Liouville ten-square formula 中的 fourth angular / Gaussian two-square term。因此不把它声明为新的 classical identity；本项目新增的是其 collapse-tower interpretation：

`2D two-square angular datum -> 10D shell echo -> exact low-dimensional recovery`.

## 9. Even-dimension rigidity scan

对 even dimensions `2,4,...,18`，按 `p mod 8` 分组，尝试用 degree `d/2-1` 的单变量 polynomial in `p` 拟合 signed shell `R_d(p)`：用最少点插值，其余全部作为 exact holdout。

结果：

| dimension | mod-8 class behavior |
|---|---|
| 2 | all four classes exact polynomial (two are zero channels) |
| 4 | all four exact |
| 6 | all four exact, split into two mod-4 formulas |
| 8 | all four exact |
| 10 | classes 3,7 exact; classes 1,5 fail one-variable polynomial because angular term survives |
| 12 | all four fail naive one-variable polynomial |
| 14 | all four fail |
| 16 | all four fail |
| 18 | all four fail |

This is only a model-ablation statement. `fail` means “not captured by this residue-conditioned single-polynomial ansatz”, not randomness and not absence of exact arithmetic structure.

The first interpretable rigidity break occurs already at d=10 in the two-square channel, where the missing coordinate is exactly H4.

## 10. Factorization side consequence

For an odd nonsquare semiprime

`n=pq`, `p != q`,

4D wall value gives

`Q4(n)=sigma_1(n)=(p+1)(q+1)=n+p+q+1`.

Hence

`Q4(n)-(n+1)=p+q`.

Together with `pq=n`, this determines the two factors as roots of

`t^2-(p+q)t+n=0`.

This is a structural side channel, **not currently a complexity breakthrough**: the present exact DP computes the shell table in time polynomial in numeric `n`, not polynomial in bit-length `log n`. The open question is whether native collapse structure can compute the wall excess without enumerating the full shell.

## 11. Reproducibility

Executable:

`scripts/highdim_prime_collapse_experiment_p5000.py`

Default run:

`python scripts/highdim_prime_collapse_experiment_p5000.py --max-n 5000 --d-max 19`

It generates a compact prime fingerprint CSV and asserts:

- Newton reconstruction;
- 4D wall correctness inside the requested range;
- 8D wall correctness inside the requested range;
- 10D rigid/angular identities;
- exact two-square recovery for the `1 mod 4` channel.

The independently generated P5000 compact fingerprint stream used during this research turn had SHA-256:

`cb39a8dcafcd9999666b15b089c3364d08ab87f4ec4a3d9c8a3ea82204a55f42`

This digest covers 669 prime rows with birth/support-continuity, C2..C8, Q4, Q8, R10 and the recovered two-square/angular fields.

## 12. Current verdict

Freeze experimental verdict:

`HIGH_DIMENSIONAL_PRIME_COLLAPSE_EXPERIMENT_E1 = DIMENSION_FILTER_WALLS_AND_LOW_DIMENSION_ECHO_FOUND`.

More specifically:

1. raw high-dimensional multiplicity is mostly a poor prime signal after matched controls;
2. alternating finite-dimension filters are dramatically stronger than single-layer counts;
3. dimension 4 exposes an exact sigma_1 prime wall;
4. dimension 8 exposes an exact sigma_3 prime wall;
5. dimension 10 is the first observed channel where a 2D angular invariant reappears and can be recovered from the high-dimensional shell;
6. the most promising next experiment is therefore not “go to still higher d and count more points”, but to classify which low-dimensional invariants reappear under each higher-dimensional filter and whether any can be computed by local collapse without full shell enumeration.

No novelty claim is made for the classical Jacobi/Liouville identities themselves.
