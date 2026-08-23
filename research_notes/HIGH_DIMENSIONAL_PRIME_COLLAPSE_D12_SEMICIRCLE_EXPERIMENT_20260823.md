# 高维坍缩素数实验 E2 — 12D 主项剥离后的半圆残差

Status: `FREE_RESEARCH / EXPERIMENT_CHECKPOINT / CLASSICAL_COMPARISON_OPENED / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-HDPB-2308A9`

Parent: `HIGH_DIMENSIONAL_PRIME_COLLAPSE_EXPERIMENT_E1`

## 1. 实验定义

对 prime `p`，令 `R_12(p)` 为 quadratic support spectrum 经 sign-completion audit 得到的 12-square ordered signed shell multiplicity。

定义归一化残差

`t_p = (R_12(p) - 8(p^5+1)) / (32 p^(5/2))`.

该量完全由已经建立的 2D→19D support spectrum 通过维数滤波得到；signed completion 只是 audit multiplicity，不改写 native carrier。

## 2. P5000 数值结果

样本：全部 668 个 odd primes `p<=5000`。

得到：

- minimum `-0.9893465583042172` at `p=577`;
- maximum `+0.9867696397703942` at `p=3907`;
- mean `0.00557234600285308`;
- standard deviation `0.49538606594445506`;
- second moment `0.24543840537189948`;
- fourth moment `0.1198174347547953`;
- sixth moment `0.07283325612033248`.

对半圆密度

`rho(t)=(2/pi)*sqrt(1-t^2), -1<=t<=1`,

对应理论偶矩为

- `E[t^2]=1/4=0.25`;
- `E[t^4]=1/8=0.125`;
- `E[t^6]=5/64=0.078125`.

P5000 empirical CDF 对该半圆 CDF 的 Kolmogorov-Smirnov distance：

`D_KS = 0.01711928645513039`.

这不是显著性检验结论，只作为 shape diagnostic；样本矩和 CDF 都已经非常接近半圆形。

## 3. mod-8 ablation

按 prime birth residue class 分开：

| p mod 8 | N | mean | std | KS-to-semicircle |
|---:|---:|---:|---:|---:|
| 1 | 161 | 0.00467191497 | 0.47742335543 | 0.04531793541 |
| 3 | 168 | 0.01340874535 | 0.50724703210 | 0.03269206086 |
| 5 | 168 | 0.01288603903 | 0.50816764375 | 0.04605388937 |
| 7 | 171 | -0.00846418103 | 0.48709707651 | 0.03570304068 |

因此 2D/3D/4D birth 的 mod-8 分层虽然控制低维首次出现，但在这个 12D normalized residual 中不是主导 shape；四个 residue channels 都分别接近相同半圆包络。

## 4. Phase-B classical comparison

外部经典比较确认：该 normalized 12-square prime residual 正是已知 Sato-Tate 型例子。公开数论教材明确陈述，当 `p` 遍历 primes 时

`(r_12(p)-8(p^5+1))/(32 p^(5/2))`

按密度 `(2/pi)sqrt(1-t^2)` 分布。

因此：

`SEMICIRCLE_DISTRIBUTION_IS_NOT_NEW_CLASSICAL_MATHEMATICS`.

本实验真正保留的项目解释是：

`DIMENSION_12 = FIRST OBSERVED GLOBAL STATISTICAL ECHO AFTER LOWER-DIMENSION RIGID/ANGULAR CHANNELS`.

在本次 dimension scan 中：

- d=4: exact divisor wall;
- d=8: exact divisor-power wall;
- d=10: exact 2D angular echo;
- d=12: after smooth main-term removal, bounded residual enters a nontrivial semicircle distribution law.

这给出一个非常清楚的高维层级变化：

`RIGID WALL -> ANGULAR ECHO -> DISTRIBUTED MODULAR RESIDUAL`.

## 5. Reproducibility

Executable:

`scripts/highdim_prime_collapse_d12_semicircle.py`

Default:

`python scripts/highdim_prime_collapse_d12_semicircle.py --max-n 5000`

Outputs per-prime `R12,t12`, moments, mod-8 ablations and KS distance.

## 6. Experimental verdict

Freeze:

`HDPB_E2_D12_SEMICIRCLE_RESIDUAL_REDISCOVERED_AND_CLASSIFIED_AS_CLASSICAL_SATO_TATE_ECHO`.

No novelty claim is made for Sato-Tate itself.

The next genuine research question is internal to the collapse program:

> Can the transition from exact walls (4D/8D), to recoverable angular information (10D), to distributed residual information (12D) be described by one native dimension-raising / dimension-filter algebra, without importing modular-form vocabulary as a premise?
